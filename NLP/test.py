from wordcloud import WordCloud, STOPWORDS
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

def decompose(ls,score):
    tag = ['VCP', 'VCN', 'NNG', 'IC', 'MAG', 'VA', 'VV', 'XR']

    if score == 1:
        tag.pop(1)
    elif score == -1:
        tag[1:]
    
    word_list = []

    for txt in ls:
        out = mecab.pos(txt)
        for word in out:
            if word[1] in tag:
                word_list.append(word[0])
    
    return list(set(word_list))

def day_score(text):
    
    cnt = 0
    score = 0
    p = []
    n = []
    txt = decompose(text,0)
    for word in txt:
        if word in pos:
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


from eunjeon import Mecab
mecab = Mecab()
text = "희망고문을 주다"
# 텍스트를 형태소 단위로 나누는 함수. 파라미터의 norm은 문장을 정규화, stem은 각 단어에서 어간을 추출
out1 = mecab.morphs(text)
# 텍스트에서 명사만 추출하는 함수
# out2 = mecab.nouns(text)
# 각 품사를 태깅하는 함수. 텍스트를 형태소 단위로 나눈 후 나뉘어진 형태소를 해당하는 품사와 함께 리스트화.
# 파라미터에는 norm, stem, join(나눠진 형태소와 품사를 형태소/품사 형태로 리스트화)
out3 = mecab.pos(text)
print('morphs',out1)
# print('nouns',out2)
print('pos',out3)
# print()

out4 = count_words(text)
print('word count', out4)

positive = pd.read_csv('positive.txt', sep="\t", engine="python", encoding = "utf-8")
pos = decompose(positive.T.values[0],1)
with open('pos.txt', 'w') as f:
    f.write(str(pos))
f.close()

negative = pd.read_csv('negative.txt', sep="\t", engine="python", encoding = "utf-8")
neg = decompose(negative.T.values[0],-1)
with open('neg.txt', 'w') as f:
    f.write(str(neg))
f.close()

unknown = pd.read_csv('unknown.txt', sep="\t", engine="python", encoding = "utf-8")
unk = decompose(unknown.T.values[0],0)
with open('unk.txt', 'w') as f:
    f.write(str(unk))
f.close()

score = day_score(out1)
print(score)

chk = []
for word in pos:
    if word in neg:
        chk.append(word)

for word in neg:
    if word in pos:
        chk.append(word)

chk = list(set(chk))

with open('chk.txt', 'w') as f:
    f.write(str(chk))
f.close()

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