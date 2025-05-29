import sys
import os
from logger import *
from filter import getWords
from teleBot import startBot

from constants import *

def parsingFile(file_path):
    try:
        log_and_print("info", f"Считывание {FILE_NAME}")
        with open(os.path.abspath(file_path), 'r') as file:
            words = [line.strip() for line in file]
            log_and_print("info", f"{FILE_NAME} успешно прочитан.")
            getWords(words)

    except FileNotFoundError:
        log_and_print("error", f"Файл {FILE_NAME} не найден.")
        sys.exit(0)

def main():
    creatLoggingFile(LOG_FILE_NAME, os.path.dirname(sys.argv[0]))

    len_arg = len(sys.argv)
    if len_arg == 1:
        parsingFile(FILE_NAME)
    elif len_arg == 2:
        parsingFile(sys.argv[1])
    else:
        log_and_print("error", "Слишком много аргументов.")
        log_and_print("debug", f"Аргументов {len_arg}: {sys.argv}")
        sys.exit(0)

    startBot(API_TOKEN)

    log_and_print("info", f"Программа [{os.getpid()}] завершилась с кодом 0.")

    sys.exit(0)

if __name__ == "__main__":
    main()
