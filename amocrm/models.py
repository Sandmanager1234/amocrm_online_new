import os
from dotenv import load_dotenv
from loguru import logger
from datetime import datetime, timedelta
from typing import Optional


load_dotenv()

class TelegramChat:
    astana: int = int(os.getenv('group_astana'))
    almaty: int = int(os.getenv('group_almaty'))
    online: int = int(os.getenv('group_online'))

    pipeline_astana: int = int(os.getenv('pipeline_astana'))
    pipeline_almaty: int = int(os.getenv('pipeline_almaty'))
    pipeline_online: int = int(os.getenv('pipeline_online'))

    chat_id: int

    def set_chat_id(self, pipeline_id: int):
        match pipeline_id:
            case self.pipeline_astana:
                self.chat_id = self.astana
            case self.pipeline_almaty:
                self.chat_id =  self.almaty
            case self.pipeline_online:
                self.chat_id = self.online
            case _:
                self.chat_id = None


class Learner:
    first_name: str = ""  # Имя ученика
    last_name: str = ""  # Фамилия ученика
    grade: str = ""  # Класс ученика
    departament: str = ""  # Отделение

    learning_direction: str = ""  # Цель обучения
    profile_subjects: str = ""  # Предметы ученика

    def __str__(self):
        """Возвращает строковое представление ученика"""
        return (
            f"Ученик:\n"
            f"--Имя: {self.first_name}\n"
            f"--Фамилия: {self.last_name}\n"
            f"--Класс и отделение: {self.grade}{self.departament}\n"
        )


class Manager:
    id: Optional[int] = None
    name: str = ""
    comment: str = ""  # Комментарий менеджера

    def set_name(self, data: dict):
        self.name = data.get("name", "")

    def __str__(self):
        """Возвращает строковое представление менеджера"""
        return (
            f"Менеджер:\n"
            f"--ID: {self.id}\n"
            f"--Имя: {self.name}\n"
            f"--Комментарий: {self.comment}"
        )




class BranchIsNotOnline(Exception):
    pass


class Parent:
    id: Optional[int] = None
    name: str = ""
    phone: str = ""
    email: str = ""

    def set_email(self, data: dict):
        # if not (self.name == data.get("name", "None")):
        #     return
        email = None
        fields = data.get("custom_fields_values", []) if data.get("custom_fields_values", []) else []
        for field in fields:
            if field["field_name"] == "Email":
                email = field["values"][0]["value"]
                break
        self.email = email if email else ""

    def __str__(self):
        """Возвращает строковое представление родителя"""
        return (
            f"Родитель:\n"
            f"--ФИО: {self.name}\n"
            f"--Телефон: {self.phone}\n"
            f"--Email: {self.email}"
        )


class Payment:
    date: str = ""
    amount: str = ""
    credit: str = ""
    credit2: str = ""
    credit3: str = ""
    credit4: str = ""
    method: str = ""
    debt: str = ""
    expected_amount: str = ""
    
    parent: Parent = Parent()

    def __str__(self):
        """Возвращает строковое представление оплаты"""
        return (
            f"Оплата:\n"
            f"--Дата: {self.date}\n"
            f"--Сумма: {self.amount}\n"
            f"--Долг клиента: {self.credit}\n"
            f"--Метод оплаты: {self.method}"
        )


class Lead:
    def __init__(self, id: int):
        """
        Инициализация объекта Order.

        :param id: Идентификатор заказа
        """
        self.id = id  # Уникальный идентификатор заказа
        self.name: str = ""

        # Ученик
        self.learner: Learner = Learner()

        # Объект менеджера
        self.manager: Manager = Manager()
        self.pp_manager: Manager = Manager()  # ПП Менеджер

        # Оплата
        self.payment = Payment()

        # Информация о родителе
        self.parent: Parent = Parent()  # родитель

        self.telegram_chat: TelegramChat = TelegramChat()

        # Дополнительные данные о заказе
        self.city: str = ""  # Город
        self.branch: str = ""  # Филиал
        self.learning_duration: str = ""  # Срок обучения
        self.start_date: str = ""  # Дата начала обучения
        self.end_date: str = ""  # Дата окончания обучения
        self.learning_time: str = ""  # Время обучения
        self.phone: str = ""  # Телефон
        self.email = ""  # Почта
        self.base_course = ""
        self.intensive_cource = ""
        self.summer_camp = ""
        self.status: str = ""  # Статус лида
        self.prodlenie: bool = False  # Флаг продления

    def __get_value_from_json(self, field: dict, _all: bool = False) -> str:
        """Приватный метод для получения значения из JSON"""
        try:
            if not _all:
                value = (
                    field["values"][0]["value"]
                    if field["values"][0]["value"] is not None
                    else ""
                )
            else:
                value = ", ".join(
                    [
                        value["value"]
                        for value in field["values"]
                        if value["value"] is not None
                    ]
                )
            logger.debug(f"{field.get('field_name','Неизвестное')}: {value}")
            return value
        except (KeyError, IndexError, TypeError) as e:
            logger.warning(
                f"Ошибка при обработке поля `{field.get('field_name','Неизвестное')}`: {e}"
            )
            return ""

    @classmethod
    def from_json(cls, data: dict) -> "Lead":
        """Обрабатывает вкладку `Основное` в сделке."""
        try:
            self: Lead = cls(data.get("id", ""))
            self.name =  data.get("name", "")
            self.manager.id = data.get("responsible_user_id", None)
            self.telegram_chat.set_chat_id(data.get('pipeline_id', -1))

            fields = data.get("custom_fields_values", []) if data.get("custom_fields_values", []) else []
            for field in fields:
                match field.get("field_name", None):
                    case None:
                        continue

                    case "Имя ученика":
                        self.learner.first_name = self.__get_value_from_json(field)

                    case "Фамилия ученика":
                        self.learner.last_name = self.__get_value_from_json(field)

                    case "Класс":
                        self.learner.grade = self.__get_value_from_json(field)

                    case "Отделение":
                        self.learner.departament = self.__get_value_from_json(field)

                    case "Статус Ученика":
                        self.status = self.__get_value_from_json(field, _all=True)

                    case "Цель обучения":
                        self.learner.learning_direction = self.__get_value_from_json(
                            field
                        )

                    case "Предметы":
                        self.learner.profile_subjects = self.__get_value_from_json(
                            field, _all=True
                        )

                    case "Коммент ОП":
                        self.manager.comment = self.__get_value_from_json(field)

                    case "ФИО родителя":
                        self.parent.name = self.__get_value_from_json(field)

                    case "Дата оплаты":
                        date = self.__get_value_from_json(field)
                        if date != "":
                            date = (
                                datetime.fromtimestamp(
                                    int(self.__get_value_from_json(field))
                                )
                                + timedelta(days=1)
                            ).strftime("%Y-%m-%d")
                        self.payment.date = date

                    case "Город?":
                        self.city = self.__get_value_from_json(field)

                    case "Сумма 1 транша":
                        self.payment.amount = self.__get_value_from_json(field)

                    case "Сумма 2 транша":
                        self.payment.credit = self.__get_value_from_json(field)

                    case "Сумма 3 транша":
                        self.payment.credit2 = self.__get_value_from_json(field)

                    case "Сумма 4 транша":
                        self.payment.credit3 = self.__get_value_from_json(field)

                    case "Сумма 5 транша":
                        self.payment.credit4 = self.__get_value_from_json(field)

                    case "Метод Оплаты":
                        self.payment.method = self.__get_value_from_json(field)

                    case "Филиал":
                        self.branch = self.__get_value_from_json(field)

                    case "Срок обуч (мес)":
                        self.learning_duration = self.__get_value_from_json(field)

                    case "Дата начала учебы по договору":
                        date = self.__get_value_from_json(field)
                        if date != "":
                            date = (
                                datetime.fromtimestamp(
                                    int(self.__get_value_from_json(field))
                                )
                                + timedelta(days=1)
                            ).strftime("%Y-%m-%d")
                        self.start_date = date

                    case "Дата конца учебы":
                        date = self.__get_value_from_json(field)
                        if date != "":
                            date = (
                                datetime.fromtimestamp(
                                    int(self.__get_value_from_json(field))
                                )
                                + timedelta(days=1)
                            ).strftime("%Y-%m-%d")
                        self.end_date = date

                    case "Время обучения":
                        self.learning_time = self.__get_value_from_json(field)

                    case "Номер телефона родителя":
                        self.parent.phone = self.__get_value_from_json(field)

                    case "Баз-й курс (мес)":
                        self.base_course = self.__get_value_from_json(field)

                    case "Летний лагерь":
                        self.summer_camp = self.__get_value_from_json(field)

                    case "Инт-й курс (мес)":
                        self.intensive_cource = self.__get_value_from_json(field)
                    case "ФИО оплатившего родителя":
                        self.payment.parent.name = self.__get_value_from_json(field)
                    case "ПП Менеджер":
                        self.pp_manager.name = self.__get_value_from_json(field)
                    case "Долг клиента":
                        self.payment.debt = self.__get_value_from_json(field)
                    case "Ожидаемая сумма":
                        self.payment.expected_amount = self.__get_value_from_json(field)
                    case "готово к продлению":
                        self.prodlenie = self.__get_value_from_json(field)
                    case _:
                        pass
            # ОШИБКИ ОБРАБОТКИ
            # if self.branch != "Онлайн":
            #     raise BranchIsNotOnline(f"Филиал не онлайн")
            try:
                if data.get("_embedded") and data["_embedded"].get("contacts"):
                    self.parent.id = data["_embedded"]["contacts"][0]["id"]
            except:
                pass
            return self
        except KeyError as e:
            logger.error(f"Ключ не найден в данных: {e}")
            raise
        except BranchIsNotOnline as e:
            logger.warning(e)
            raise e
        except Exception as e:
            logger.error(f"Общая ошибка обработки данных: {e}")
            raise

    def __str__(self):
        """Возвращает строковое представление объекта Lead"""
        return (
            f"Заказ #{self.id}:\n"
            f"Город: {self.city}\n"
            f"Филиал: {self.branch}\n"
            f"Статус: {self.status}\n"
            f"{self.manager}\n"
            f"{self.learner}\n"
            f"{self.parent}\n"
            f"Срок обучения: {self.learning_duration}\n"
            f"Дата начала: {self.start_date}\n"
            f"Дата окончания: {self.end_date}\n"
            f"Время обучения: {self.learning_time}\n"
            f"Баз-й курс (мес): {self.base_course}\n"
            f"Инт-й курс (мес): {self.intensive_cource}\n"
            f"Летний лагерь: {self.summer_camp}\n"
            f"{self.payment}\n"
        )
    
class Event:
    def __init__(self, id: str) -> "Event":
        self.id: str = id
        self.entity_id : str = ''
        self.after_pipeline_id : str = ''
        self.before_pipeline_id : str = ''

    @classmethod
    def from_json(cls, data: dict) :
        try:
            self : Event = cls(data.get('id'))  
            self.entity_id = data.get('entity_id')
            self.after_pipeline_id = data.get(
                'value_after', [{}]
            )[0].get(
                'lead_status'
            ).get(
                'pipeline_id'
            )
            return self
        except Exception as e:
            logger.error(f'Ошибка обработки события: {e}')

