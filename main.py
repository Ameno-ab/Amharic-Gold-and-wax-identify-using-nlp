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
    double_meaning_identifier(stop_word_string)

def double_meaning_identifier(words):

# to identify words with double noun meanings
  double=list()
  noun_dict = {}
  for word in words:
      n = 0
      for key in noun:
         for noun_word in noun[key]:
            if noun_word == word:
                 n += 1
                 noun_dict[word]= ['NN',n]
  print("noun_key->", noun_dict)

# to identify words with double verb meanings
  verb_dict = {}
  for word in words:
      v = 0
      for key in verb:
          for verb_word in verb[key]:
              if verb_word == word:
                  v += 1
                  verb_dict[word] = ['VV', v]
  print("Verb_key->", verb_dict)

# to identify words with double noun and verb meanings
  noun_verb_dict = {}
  for n_key  in noun_dict:
      for v_key in verb_dict:
          # print("key", v_key)
          if v_key == n_key:
           noun_verb_dict[n_key] = ['NV', noun_dict[n_key][-1] + verb_dict[v_key][-1]]
  print("noun_verb_key", noun_verb_dict)

#to merge all the identified meanings
  merged={}
  merged.update(noun_dict)
  merged.update(verb_dict)
  merged.update(noun_verb_dict)
  print('merged',merged)

#to set hebir kal with biggest counter number and tagger
  hebir_kal=''
  nn = False
  for L_counter in  merged:
   if merged[L_counter][0] == 'NV' and merged[L_counter][-1] > 1 and nn != True :
        hebir_kal = L_counter
   elif merged[L_counter][0] == 'VV' and  merged[L_counter][-1] > 1 :
        hebir_kal = L_counter
        break
   elif merged[L_counter][0] == 'NN' and merged[L_counter][-1] > 1:
        hebir_kal = L_counter
        nn=True

  print("hebitr kal",hebir_kal)
  return hebir_kal



if __name__ == '__main__':
   text_preprocessing(" በላ ለማ አበበ አበባ  ")



