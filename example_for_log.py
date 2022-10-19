# example_for_log.py

import logging
from logging.handlers import RotatingFileHandler

# глобально
logging.basicConfig(
    level=logging.DEBUG,
    filename='program.log', 
    format='%(asctime)s, %(levelname)s, %(message)s, %(name)s'
)

# локально
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = RotatingFileHandler('my_logger.log', maxBytes=50000000, backupCount=5)
logger.addHandler(handler)

# использоваие форматера
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
handler.setFormatter(formatter)


logging.debug('123')  # Когда нужна отладочная информация 
logging.info('Сообщение отправлено')  # Когда нужна дополнительная информация
logging.warning('Большая нагрузка!')  # Когда что-то идёт не так, но работает
logging.error('Бот не смог отправить сообщение')  # Когда что-то сломалось
logging.critical('Всё упало! Зовите админа!1!111')  # Когда всё совсем плохо


