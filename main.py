from etnltk import Amharic
from etnltk.tokenize.am import sent_tokenize
from etnltk.tokenize.am import word_tokenize
from etnltk.lang.am import normalize, remove_stopwords
from etnltk.lang.am import preprocessing
from etnltk.lang.am import clean_amharic
from dataset import STOP_WORDS



def text_preprocessing(qnie):
    cleaned = clean_amharic(qnie, abbrev=False)
    print('cleaned',cleaned)
    normalized_text = normalize(cleaned)
    print('text_normilized', normalized_text)
    stop_word_remover(cleaned)



def stop_word_remover(strings_set):
    words =list()
    str1 = " "
    for string in strings_set.split():
     if string not in STOP_WORDS:
         words.append(string)
    stop_word_string=str1.join(words)
    words = word_tokenize(stop_word_string)
    print('word_tokinize',words)



if __name__ == '__main__':
    text_preprocessing("ወደ አዳባባይ ወጥተህ፣ ከባለጋራህ ተሟግተህ፣ ክርክር ገጥመህ ወደ ማታ፣ለማፈር ነው ስትረታ")


