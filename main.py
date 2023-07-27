from etnltk import Amharic
from etnltk.tokenize.am import sent_tokenize
from etnltk.tokenize.am import word_tokenize
from etnltk.lang.am import normalize, remove_stopwords
from etnltk.lang.am import preprocessing
from etnltk.lang.am import clean_amharic
from stopwords_dataset import STOP_WORDS
from wordnet import *



def text_preprocessing(qnie):
    str1 = " "
    normalized_text = normalize(qnie)
    print('text_normilized', normalized_text)
    words = word_tokenize(normalized_text)
    print('words', words)
    cleaned = words
    print('cleaned', cleaned)
    stop_word_remover(cleaned)



def stop_word_remover(strings_set):
    words =list()
    str1 = " "
    for string in strings_set:
     if string not in STOP_WORDS:
         words.append(string)
    stop_word_string=words
    print('word_tokinize',stop_word_string)



if __name__ == '__main__':
    text_preprocessing("ያችማ የኔ እት ቤት ሠርታ ነበረች፣ ሳትቀመጥበት ላፈርሰው ነው አለች።")
    for key in noun:
        for word in noun[key]:
            print("noun_key",key, '->', word)
    for key in verb:
        for word in verb[key]:
            print("verb_key", key, '->', word)


