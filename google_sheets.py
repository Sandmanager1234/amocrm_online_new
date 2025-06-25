import gspread
import os
from loguru import logger


class GoogleSheets:

    def __init__(self):
        try:
            logger.info("Инициализация GoogleSheets")
            gc = gspread.service_account(filename="credentials.json")
            sh_online = gc.open_by_key(os.getenv("table_id_online"))
            self.worksheet_online = sh_online.worksheet("amo new")
            sh_offline = gc.open_by_key(os.getenv('table_id_offline'))
            self.worksheet_offline = sh_offline.worksheet("amo new")

            logger.info("Успешное подключение к таблице")
        except Exception as e:
            logger.error(f"Ошибка при инициализации GoogleSheets: {e}")
            raise

    def insert_row(self, row_data, index: int, worksheet_type: str):
        """Вставляет строку данных на указанный индекс."""
        try:
            logger.info(f"Вставка строки на позицию {index}: {row_data}")
            if worksheet_type == 'online':
                self.worksheet_online.insert_row(
                    row_data, index, value_input_option="USER_ENTERED"
                )
            else:
                self.worksheet_offline.insert_row(
                    row_data, index, value_input_option="USER_ENTERED"
                )
            logger.info("Строка успешно вставлена")
        except Exception as e:
            logger.error(f"Ошибка при вставке строки: {e}")
            raise

    def get_row_count(self, worksheet_type: str):
        """Возвращает количество строк, включая пустые."""
        try:
            logger.info("Получение общего количества строк")
            if worksheet_type == 'online':
                row_count = self.worksheet_online.row_count
            else:
                row_count = self.worksheet_offline.row_count
            logger.info(f"Количество строк в таблице: {row_count}")
            return row_count
        except Exception as e:
            logger.error(f"Ошибка при получении количества строк: {e}")
            raise

    def get_filled_row_count(self, worksheet_type: str):
        """Возвращает количество заполненных строк (игнорируя пустые строки)."""
        try:
            logger.info("Получение количества заполненных строк")
            if worksheet_type == 'online':
                filled_rows = len(self.worksheet_online.get_all_values())
            else:
                filled_rows = len(self.worksheet_offline.get_all_values())
            logger.info(f"Количество заполненных строк: {filled_rows}")
            return filled_rows
        except Exception as e:
            logger.error(f"Ошибка при получении количества заполненных строк: {e}")
            raise
