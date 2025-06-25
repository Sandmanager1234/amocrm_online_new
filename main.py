import os
import asyncio
from amocrm import AmoCRMClient
from amocrm.models import Lead, BranchIsNotOnline, Event
from aiogram import Bot
from dotenv import load_dotenv
from loguru import logger
from google_sheets import GoogleSheets
from datetime import datetime

from scheduler import Scheduler


# Загрузка переменных из .env файла
load_dotenv()

SECONDS = int(os.getenv('seconds'))
UPDATED_FIELDS = (
    691104, # first_name
    691102, # last_name
    691120, # grade
    691118, # department
    802046, # status
    691138, # learning direction
    799986, # city
    803170, # pp_manager name
    691136, # learning time
    691134, # branch
    691128, # subjects
    691170, # amount
    693110, # credit
    803189, # credit 2
    803191, # credit 3
    803193, # credit 4
    799680, # method
    800320, # base_course
    800322, # intensive cource
    798554, # summer camp
    691152, # start date
    691176, # end_date
    803014, # payment parent name
    691010, # parent name
    691108, # parent phone
    802044, # Коммент ОП comment
    670397, # email
    803201, # долг клиента
    803203 # ожидаемая сумма
)
# Получение имени текущей директории
current_directory_name = os.path.basename(os.getcwd())

os.makedirs(".", exist_ok=True)  # Создание папки logs, если её нет

log_file_path = os.path.join(
    "logs", f"{current_directory_name}_{{time:YYYY-MM-DD}}.log"
)


# Настройка ротации логов
logger.add(
    log_file_path,  # Файл лога будет называться по дате и сохраняться в поддиректории с названием текущей директории
    rotation="00:00",  # Ротация каждый день в полночь
    retention="7 days",  # Хранение логов за последние 7 дней
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",  # Формат сообщений в файле
    level="INFO",  # Минимальный уровень логирования
    compression="zip",  # Архивирование старых логов
)

bot = Bot(os.getenv("telegram_token"))
google = GoogleSheets()
amo_client = AmoCRMClient(
    base_url="https://teslakz.amocrm.ru",
    access_token=os.getenv("access_token"),
    client_id=os.getenv("client_id"),
    client_secret=os.getenv("client_secret"),
    permanent_access_token=True,
)


async def send_to_telegram(lead: Lead):
    await bot.send_message(
        lead.telegram_chat.chat_id,
        f"<u>Примите нового ученика</u>.😊\n"
        f"Дата оплаты: <b>{lead.payment.date}</b>\n\n"
        f"🤓Ученик: <b>{lead.learner.last_name} {lead.learner.first_name}</b>\n"
        f"✔️Класс и отделение: <b>{lead.learner.grade} {lead.learner.departament}</b>\n"
        f"⏰Время: <b>{lead.learning_time}</b>\n"
        f"👩‍👦 Родитель: <b>{lead.parent.name}</b>\n"
        f"📞 Телефон: <b>{lead.parent.phone}</b>\n"
        f"🏠 Филиал: <b>{lead.branch}</b>\n\n"
        f"🔷 Срок обучения: <b>{'' if lead.learning_duration == '' else lead.learning_duration + ' мес.'}</b>\n\n"
        f"🟢 Дата начала обучения: <b>{lead.start_date}</b>\n"
        f"🔴 Дата конца обучения: <b>{lead.end_date}</b>\n\n"
        f"🎯Направление обучения: <b>{lead.learner.learning_direction}</b>\n"
        f"📚Профильные предметы: <b>{lead.learner.profile_subjects}</b>\n"
        f"ℹ️Новый или продление: <b>{lead.status}</b>\n"
        f"📨Комментарий ОП: <b>{lead.manager.comment}</b>\n\n"
        f"😎Менеджер: <b>{lead.manager.name}</b>",
        parse_mode="HTML",
    )


def send_to_google(lead: Lead):
    data_insert = [
        datetime.now().strftime("%Y.%m.%d %H:%M:%S"),
        datetime.strptime(lead.payment.date, "%Y-%m-%d").strftime("%Y.%m.%d"),
        lead.city,
        lead.manager.name,
        lead.pp_manager.name,
        lead.learner.last_name + " " + lead.learner.first_name,
        lead.learner.learning_direction,
        lead.learner.grade,
        lead.learner.departament,
        lead.learning_time,
        lead.branch,
        lead.learner.profile_subjects,
        lead.payment.amount,
        lead.payment.credit,
        lead.payment.credit2,
        lead.payment.credit3,
        lead.payment.credit4,
        lead.payment.method,
        lead.payment.debt,
        lead.payment.expected_amount,
        lead.base_course,
        lead.intensive_cource,
        lead.summer_camp,
        lead.status,
        "",
        lead.start_date,
        lead.end_date,
        lead.parent.name,
        lead.payment.parent.name,
        lead.parent.phone,
        lead.manager.comment,
        lead.parent.email,
    ]

    google.insert_row(
        data_insert, 
        google.get_filled_row_count(
            'online' if lead.branch == 'Онлайн' else 'offline'
        ) + 1,
        'online' if lead.branch == 'Онлайн' else 'offline'
    )


async def update_leads(timestamp: int, curr_timestamp: int):
    try:
        leads_response = await amo_client.get_updated_leads(timestamp, curr_timestamp)
        event_response = await amo_client.get_update_events(timestamp, curr_timestamp)
        events_json = event_response.get('_embedded', {}).get('events', {})
        events = {}
        for event_json in events_json:
            if event_json.get('entity_id') not in events:
                events[event_json.get('entity_id')] = []
            events[event_json.get('entity_id')].append(event_json.get('value_after', [{}])[0].get('custom_field_value', {}).get('field_id'))
        leads_json = leads_response.get('_embedded', {}).get('leads', {})
        if leads_json:
            for lead_json in leads_json:
                try:
                    lead = Lead.from_json(lead_json) 
                    if lead.manager.id:
                        lead.manager.set_name(await amo_client.get_user(lead.manager.id))
                    if lead.parent.id:
                        lead.parent.set_email(await amo_client.get_contact(lead.parent.id))
                    if lead.id in events:
                        field_ids = events.get(lead.id, [])
                        for field_id in field_ids:
                            if field_id in UPDATED_FIELDS:
                                send_to_google(lead)
                                break
                except Exception as e:
                    logger.error(f'Ошибка при обновлении сделки: {e}')
    except Exception as ex:
        logger.error(f'Ошибка при запросе обновлении сделок: {ex}')
    pass


async def polling_leads(timestamp: int, curr_timestamp: int):
    amo_client.start_session()
    try:
        response = await amo_client.get_events(timestamp)
        events_json = response.get('_embedded', {}).get('events', {})
        if events_json:
            for event_json in events_json:
                try:
                    event = Event.from_json(event_json)    
                    if event.entity_id:
                        lead = Lead.from_json(await amo_client.get_lead(event.entity_id)) 
                        if lead.manager.id:
                            lead.manager.set_name(await amo_client.get_user(lead.manager.id))
                        if lead.parent.id:
                            lead.parent.set_email(await amo_client.get_contact(lead.parent.id))
                    await send_to_telegram(lead)

                    send_to_google(lead)
                except BranchIsNotOnline:
                    pass
                except Exception as e:
                    logger.error(f"Ошибка при обработке сделки: {e}")
        # update_leads(timestamp, curr_timestamp)
    except:
        pass
    finally:
        await amo_client.close_session()


async def main():
    scheduler = Scheduler(polling_leads, SECONDS)
    bot_info = await bot.get_me()
    logger.info(f"Бот[{bot_info.id}] @{bot_info.username}")
    while True:
        try:
            await scheduler.start()
            await asyncio.sleep(600)
        except Exception as ex:
            print(ex)
        finally:
            await scheduler.stop()


# Запуск приложения
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    