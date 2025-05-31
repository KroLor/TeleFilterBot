import logging
from colorama import init, Fore

init(autoreset=True)

def creatLoggingFile(LOG_FILE_NAME, log_path):
    global logger

    logger = logging.getLogger("logger")
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(log_path + f"/{LOG_FILE_NAME}", mode='w', encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)

    file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)

    logger.addHandler(file_handler)

def log_print(level, message):
    if level == "debug":
        logger.debug(message)
        return
    elif level == "info":
        logger.info(message)
        print(message)
    elif level == "warning":
        logger.warning(message)
        print(Fore.YELLOW + "WARNING: " + message)
    elif level == "error":
        logger.error(message)
        print(Fore.RED + "ERROR: " + message)