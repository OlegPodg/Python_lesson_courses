import logging

"""
"""
logging.basicConfig(filename="log.log", level=logging.DEBUG, format="%(asctime)s %(levelname)s %(funcName)s || %(message)s")
try:
    print(10/0)
    logging.info("Great! Success!")

except Exception as e:
    logging.error(e)  # вывод в наш файл log.log сообщение об ошибке
    # logging.exception(e)  # Если хотим увидеть подробности ошибки, то пишем так

"""
Уровни логирования (по умолчанию - WARNING):
DEBUG – подробное и детальное логирование всей системной информации для последующего использования в отладке;
INFO – подтверждение, информация о событиях, не приводящих к ошибкам в работе модулей;
WARNING – информация о событиях, которые могут привести к ошибкам в работе модулей;
ERROR – информация об ошибках, возникших в работе модулей;
CRITICAL – информация о критических ошибках, возникших в работе модулей.
"""
