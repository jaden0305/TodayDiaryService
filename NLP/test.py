from wordcloud import WordCloud, STOPWORDS
from eunjeon import Mecab
import matplotlib.pyplot as plt
import pandas as pd

# 한글 폰트 패스로 지정
import matplotlib.font_manager as fm
import re
import collections

# 단어 갯수 세기
def count_words(text):
    # 텍스트에서 명사만 추출하는 함수
    out = mecab.pos(text)

    word_counts = {}
    tag = ['NNG','VCP', 'VCN', 'IC', 'MAG', 'VA', 'VV', 'XR']

    for word in out:
        if word[1] in tag:
            word_counts[word[0]] = word_counts.get(word[0], 0) + 1
    return word_counts

def decompose(ls):
    tag = ['VCP', 'VCN', 'NNG', 'IC', 'MAG', 'VA', 'VV', 'XR']
    stopwords=['의','가','이','은','들','는','좀','꽤','주','잘','걍','과','도','를','으로','자','에','와','한','하','다','있']

    word_list = []

    for word in ls:
        if word[1] in tag and word[0] not in stopwords:
            word_list.append(word[0])
    
    return list(set(word_list))

def day_score(text):    
    cnt = 0
    score = 0
    p = []
    n = []
    txt = decompose(text)

    for word in txt:
        if word in delight:
            score += 2
            cnt += 2
            print('d',word)
            feel['delight'] = feel.get('delight',0) + 1    
        elif word in happy:
            score += 3
            cnt += 3
            feel['happy'] = feel.get('happy',0) + 1    
        elif word in minus2:
            score -= 2
            cnt += 2
            if word in horror:
                feel['horror'] = feel.get('horror',0) + 1    
            elif word in angry:
                feel['angry'] = feel.get('angry',0) + 1    
                print('a',word)
            elif word in sad:
                feel['sad'] = feel.get('sad',0) + 1    
        elif word in minus3:
            score -= 3
            cnt += 3
            if word in horror:
                feel['horror'] = feel.get('horror',0) + 1    
            elif word in angry:
                feel['angry'] = feel.get('angry',0) + 1
                print('a',word)
            elif word in sad:
                feel['sad'] = feel.get('sad',0) + 1    
        elif word in pos:
            score += 1
            cnt += 1
            p.append(word)
        elif word in neg:
            score -= 1
            cnt += 1
            n.append(word)
    print('p',p)
    print('n',n)
    return score/cnt


mecab = Mecab()
text = open('text.txt', "r").read()
# 텍스트를 형태소 단위로 나누는 함수. 파라미터의 norm은 문장을 정규화, stem은 각 단어에서 어간을 추출
# out1 = mecab.morphs(text)
# 텍스트에서 명사만 추출하는 함수
# out2 = mecab.nouns(text)
# 각 품사를 태깅하는 함수. 텍스트를 형태소 단위로 나눈 후 나뉘어진 형태소를 해당하는 품사와 함께 리스트화.
# 파라미터에는 norm, stem, join(나눠진 형태소와 품사를 형태소/품사 형태로 리스트화)
out3 = mecab.pos(text)
# print('morphs',out1)
# print('nouns',out2)
# print('pos',out3)
# print()

out4 = count_words(text)
print('word count', out4)

pos = open('pos.txt', "r").read().split('\n')
neg = open('neg.txt', "r").read().split('\n')

pos.pop()
neg.pop()

print(len(pos))
# print(neg)

공포 = pd.read_csv('공포.txt', encoding='UTF-8', names=['word'], sep='\n')
# print(' '.join(공포.T.values[0]))
horror = decompose(mecab.pos(' '.join(공포.T.values[0])))
# print(horror)
기쁨 = pd.read_csv('기쁨.txt', encoding='UTF-8', names=['word'], sep='\n')
delight = decompose(mecab.pos(' '.join(기쁨.T.values[0])))
놀람 = pd.read_csv('놀람.txt', encoding='UTF-8', names=['word'], sep='\n')
surprise = decompose(mecab.pos(' '.join(놀람.T.values[0])))
분노 = pd.read_csv('분노.txt', encoding='UTF-8', names=['word'], sep='\n')
angry = decompose(mecab.pos(' '.join(분노.T.values[0])))
슬픔 = pd.read_csv('슬픔.txt', encoding='UTF-8', names=['word'], sep='\n')
sad = decompose(mecab.pos(' '.join(슬픔.T.values[0])))
sad.append('싫')
지루함 = pd.read_csv('지루함.txt', encoding='UTF-8', names=['word'], sep='\n')
boring = decompose(mecab.pos(' '.join(지루함.T.values[0])))
행복 = pd.read_csv('행복.txt', encoding='UTF-8', names=['word'], sep='\n')
happy = decompose(mecab.pos(' '.join(행복.T.values[0])))
down2 = pd.read_csv('down2.txt', encoding='UTF-8', names=['word'], sep='\n')
minus2 = decompose(mecab.pos(' '.join(down2.T.values[0])))
down3 = pd.read_csv('down3.txt', encoding='UTF-8', names=['word'], sep='\n')
minus3 = decompose(mecab.pos(' '.join(down3.T.values[0])))

feel = {}
score = day_score(out3)
print(score)
print(feel)

# spwords = set(STOPWORDS)

# wordcloud = WordCloud(max_font_size=200, font_path='/content/drive/My Drive/Colab Notebooks/malgun.ttf',
#                      stopwords=spwords,
#                      background_color='#FFFFFF',
#                      width=1200,height=800).generate_from_frequencies(out4)


# plt.figure(figsize = (8, 8), facecolor = None) 
# plt.imshow(wordcloud) 
# plt.axis("off") 
# plt.tight_layout(pad = 0) 
  
# plt.show() 