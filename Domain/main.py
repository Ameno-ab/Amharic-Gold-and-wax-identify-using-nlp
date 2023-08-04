from etnltk import Amharic
from etnltk.tokenize.am import sent_tokenize
from etnltk.tokenize.am import word_tokenize
from etnltk.lang.am import normalize, remove_stopwords
from etnltk.lang.am import preprocessing
from etnltk.lang.am import clean_amharic

from Domain.stopwords import *
from Domain.wordnet import *
from Domain.ai import answer


def text_preprocessing(qnie):
    str1 = " "
    normalized_text = normalize(qnie)
    print('text_normilized', normalized_text)
    words = word_tokenize(normalized_text)
    print('words', words)
    cleaned = words
    print('cleaned', cleaned)
    return stop_word_remover(cleaned)


def stop_word_remover(strings_set):
    words = list()
    str1 = " "
    for string in strings_set:
        if string not in STOP_WORDS:
            words.append(string)
    stop_word_string = words
    print("stop words", stop_word_string)
    return double_meaning_identifier(stop_word_string)


def double_meaning_identifier(words):
    #
    # # to identify words with double noun meanings
    double = list()
    noun_dict = {}
    for word in words:
        n = 0
        for key in noun:
            for noun_word in noun[key]:
                if noun_word == word:
                    n += 1
                    noun_dict[word] = ['NN', n]
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
    for n_key in noun_dict:
        for v_key in verb_dict:
            # print("key", v_key)
            if v_key == n_key:
                noun_verb_dict[n_key] = ['NV', noun_dict[n_key][-1] + verb_dict[v_key][-1]]
    print("noun_verb_key", noun_verb_dict)

    # to identify words with double adjective meanings
    adjective_dict = {}
    for word in words:
        adj = 0
        for key in adjective:
            for adjective_word in adjective[key]:
                if adjective_word == word:
                    adj += 1
                    adjective_dict[word] = ['Adj', adj]
    print("adjective_word->", adjective_dict)

    # to identify words with double noun and adjective meanings
    noun_adjective_dict = {}
    for n_key in noun_dict:
        for adj_key in adjective_dict:
            # print("key", v_key)
            if adj_key == n_key:
                noun_adjective_dict[n_key] = ['AdjN', noun_dict[n_key][-1] + adjective_dict[adj_key][-1]]
    print("noun_adjective_key", noun_adjective_dict)

    # to identify words with double verb and adjective meanings
    verb_adjective_dict = {}
    for v_key in verb_dict:
        for adj_key in adjective_dict:
            # print("key", v_key)
            if adj_key == v_key:
                verb_adjective_dict[v_key] = ['AdjV', verb_dict[v_key][-1] + adjective_dict[adj_key][-1]]
    print("verb_adjective_key", verb_adjective_dict)

    # to identify words with double adverb meanings
    adverb_dict = {}
    for word in words:
        adv = 0
        for key in adverb:
            for adverb_word in adverb[key]:
                if adverb_word == word:
                    adv += 1
                    adverb_dict[word] = ['Adv', adv]
    print("adverb_word->", adverb_dict)

    # to identify words with double noun and adverb meanings
    noun_adverb_dict = {}
    for n_key in noun_dict:
        for adv_key in adverb_dict:
            # print("key", v_key)
            if adv_key == n_key:
                noun_adverb_dict[n_key] = ['AdvN', noun_dict[n_key][-1] + adverb_dict[adv_key][-1]]
    print("noun_adverb_key", noun_adverb_dict)

    # to identify words with double verb and adverb meanings
    verb_adverb_dict = {}
    for v_key in verb_dict:
        for adv_key in adverb_dict:
            # print("key", v_key)
            if adv_key == v_key:
                verb_adverb_dict[v_key] = ['AdvV', verb_dict[v_key][-1] + adverb_dict[adv_key][-1]]
    print("verb_adverb_key", verb_adverb_dict)

    # to identify words with double adjective and adverb meanings
    adjective_adverb_dict = {}
    for adj_key in adjective_dict:
        for adv_key in adverb_dict:
            # print("key", v_key)
            if adv_key == adj_key:
                adjective_adverb_dict[adj_key] = ['AdvAdj', adjective_dict[adj_key][-1] + adverb_dict[adv_key][-1]]
    print("adjective_adverb_key", adjective_adverb_dict)

    # to merge all the identified meanings
    merged = {}
    merged.update(noun_dict)
    merged.update(verb_dict)
    merged.update(noun_verb_dict)
    merged.update(adjective_dict)
    merged.update(noun_adjective_dict)
    merged.update(verb_adjective_dict)
    merged.update(adverb_dict)
    merged.update(noun_adverb_dict)
    merged.update(verb_adverb_dict)
    merged.update(adjective_adverb_dict)
    print('merged', merged)

    # to set hebir kal with biggest counter number and tagger
    hebir_kal = ''
    nn = False
    nv = False
    adj = False
    adv = False
    adjV = False
    adjN = False
    advV = False
    advN = False

    for L_counter in merged:
        if merged[L_counter][0] == 'NV' and merged[L_counter][-1] > 1 and nn != True:
            hebir_kal = L_counter
            nv = True
        elif merged[L_counter][0] == 'VV' and merged[L_counter][-1] > 1:
            hebir_kal = L_counter
            break
        elif merged[L_counter][0] == 'NN' and merged[L_counter][-1] > 1:
            hebir_kal = L_counter
            nn = True
        elif merged[L_counter][0] == 'Adj' and merged[L_counter][-1] > 1 and nn != True and nv != True:
            hebir_kal = L_counter
            adj = True
        elif merged[L_counter][0] == 'Adv' and merged[L_counter][-1] > 1 and nn != True and nv != True and adj != True:
            hebir_kal = L_counter
            adv = True
        elif merged[L_counter][0] == 'AdjV' and merged[L_counter][
            -1] > 1 and nn != True and nv != True and adj != True and adv != True:
            hebir_kal = L_counter
            adjV = True
        elif merged[L_counter][0] == 'AdjN' and merged[L_counter][
            -1] > 1 and nn != True and nv != True and adj != True and adv != True and adjV != True:
            hebir_kal = L_counter
            adjN = True
        elif merged[L_counter][0] == 'AdvV' and merged[L_counter][
            -1] > 1 and nn != True and nv != True and adj != True and adv != True and adjV != True and adjN != True:
            hebir_kal = L_counter
            advV = True
        elif merged[L_counter][0] == 'AdvN' and merged[L_counter][
            -1] > 1 and nn != True and nv != True and adj != True and adv != True and adjV != True and adjN != True and advV != True:
            hebir_kal = L_counter
            advN = True
        elif merged[L_counter][0] == 'AdvAdj' and merged[L_counter][
            -1] > 1 and nn != True and nv != True and adj != True and adv != True and adjV != True and adjN != True and advV != True and advN != True:
            hebir_kal = L_counter

    print("hebitr kal",hebir_kal)
    # return hebir_kal

    return answer(hebir_kal)


if __name__ == '__main__':
    text_preprocessing("አሳላፊው ሁሉ ባይሆነን ወዳጅ፣ ሳያድለን ቀረ እኛን ጠላ ጠጅ፡፡")

#  "አምላክ ግብር ጠርቶ ያበላል ይላሉ፤ አንድም ቀሪ የለም ሁሉም ይጠራሉ።"(ይጠራሉ)
# "አራሲቱ ወተት ጠጪ ይሻልሻል፣ አልቦ ይዞ ባልሽ ያስፈርድብሻል፡፡"አልቦ:(ከወርቅና ከብር በዶቃ አምሳል የተሠራ የሴቶች እግር ጌጥ)
#  "አርባ ሑዳዴን መሖደድ፣ አክፍለት አለ የግድ፣ የሰው ሁሉ መጎጃው፣ በማማት እንጂ ነው፡፡"(በማማት)
# "አምናና ካችአምና ደኀና ሰው ነበረች፣ በሽታዋ መጣ ትተኩስ ጀመረች፡፡"(ትተኩስ)
#  "አሳላፊው ሁሉ ባይሆነን ወዳጅ፣ ሳያድለን ቀረ እኛን ጠላ ጠጅ፡፡"(ሳያድለን)
# "አሳብም የለብኝ እኔስ ዐርፌያለሁ፣ በቆላም በደጋም ዘሬን ጨርሻለሁ፡፡"(ዘሬን)
# "አሽከሬ ጠፍቶኛል በቅሎዬም ጠፍቶኛል፣ አፋልገኝ ጎጃሜ በባል ቀን ይገኛል፡፡"(በባል)
# "እናትና አባትሽ ሥጋ ነው እርማቸው፣ አንዠት ትበያለሽ አንቺማ ልጃቸው"(አንዠት)
# "እናት አባት ንቃ ወጥታ ከፈቃድ፣ እዩዋት ይችህን ወጣት ባልጋ ስትሄድ፡፡"(ባልጋ)
# "ሳላይ ነው እንጂ በድንገት፣ ሚስቴን ሳይ በወሰዳት"(ሳይ)
