import os
import docx2txt
from kiwipiepy import Kiwi
import numpy as np
from keybert import KeyBERT

file_list = os.listdir('./C_team/new_folder')
# print(file_list)
kiwi = Kiwi(load_default_dict=True)
#kiwi.load_user_dictionary('user_dictionary.txt')
kiwi.prepare()

topic_list = []
kiwi.add_user_word("3D", "NNG")
kiwi.add_user_word("AR", "NNG")
kw_model = KeyBERT(model='paraphrase-distilroberta-base-v1')


for i in range(100):
    text = docx2txt.process('./C_team/new_folder/'+file_list[i])

    # print(text)
    # 용언품사 = ['VV', 'VA']
    result = kiwi.analyze(text)
    # result = kiwi.tokenize(text, split_sents=True)

    cont = ''
    for token, pos, _, _ in result[0][0]:
        if pos.startswith('NN'):
            cont += token +' '

    # KeyBert 활용하여 keyword추출
    #stop_words=None 불용어 제거 하는 기준 None ex) stop_words=['3d']
    keywords = kw_model.extract_keywords(cont, keyphrase_ngram_range=(1, 1), stop_words=None, top_n=10)
    #np_keywords = np.array(keywords)
    # print(keywords[0][0])
    #print(np_keywords[0])

    topic_list.append(keywords[0])

# print(file_list[:10])
print(topic_list)




# import os
# import docx2txt
# from kiwipiepy import Kiwi
# from keybert import KeyBERT
# from multiprocessing import Pool

# file_list = os.listdir('./new_folder')[:200]
# kiwi = Kiwi(load_default_dict=True)
# kiwi.add_user_word("3D", "NNG")
# kiwi.prepare()
# kw_model = KeyBERT(model='paraphrase-distilroberta-base-v1')

# texts = [docx2txt.process('./new_folder/' + filename) for filename in file_list]

# def extract_keywords(text):
#     cont = ' '.join(token for token, pos, _, _ in kiwi.analyze(text)[0][0] if pos.startswith('NN'))
#     return kw_model.extract_keywords(cont, keyphrase_ngram_range=(1, 1), stop_words=None, top_n=10)[0]

# with Pool() as pool:
#     topic_list = pool.map(extract_keywords, texts)

# print(file_list)
# print(topic_list)