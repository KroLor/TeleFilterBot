import re
from logger import *
import Levenshtein

from constants import SIMILARITY_THRESHOLD

def getWords(_words):
    global words

    words = _words

def cleanWord(word):
    word = re.sub(r"[^a-zа-я]", '', word)
    word = re.sub(r"(.)\1+", r"\1", word)
    return word

def calculateSimilarityRatio(word1, word2):
    distance = Levenshtein.distance(word1, word2)
    max_length = max(len(word1), len(word2))
    if max_length == 0:
        return 1
    return (1 - distance / max_length)

def searching(message):
    log_print("debug", f"message: {message}")

    if any(word in message for word in words):
        return True
    
    message_words = re.findall(r"\b\w+\b", message)
    log_print("debug", f"message_words: {message_words}")

    for word in words:
        for message_word in message_words:
            message_word = message_word.lower()

            message_word = cleanWord(message_word)
            log_print("debug", f"clean_message_word: {message_word}; word: {word}")

            similarity_ratio = calculateSimilarityRatio(word, message_word)
            log_print("debug", f"similarity_ratio: {similarity_ratio}")
            if similarity_ratio >= SIMILARITY_THRESHOLD:
                return True
    
    return False