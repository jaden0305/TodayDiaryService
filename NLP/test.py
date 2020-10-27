# from wordcloud import WordCloud, STOPWORDS
from eunjeon import Mecab
# import matplotlib.pyplot as plt
import pandas as pd
# 한글 폰트 패스로 지정
# import matplotlib.font_manager as fm
# import re
# import collections

class TextAnalysis:
    mecab = Mecab()
    tag = ['VCP', 'VCN', 'NNG', 'IC', 'MAG', 'VA', 'VV', 'XR']
    stopwords=['의','가','이','은','들','는','좀','꽤','주','잘','걍','과','도','를','으로','자','에','와','한','하','다','있']
    minus_discard_list = ['웃음', '남부럽', '탄복', '가슴', '기분', '개', '자식', '기집', '터지', '되', '오르', '만족', '속', '유쾌', '의심', '끼치', '치', '안정', '느끼']
    def __init__(self, text):
        self.text = text
    def set_update(self, set_a, set_b):
        set_a.update(set_b)
        return set_a
    @classmethod
    def decompose(cls, ls):
        word_list = []
        for word in ls:
            if word[1] in cls.tag and word[0] not in cls.stopwords:
                word_list.append(word[0])
        
        return set(word_list)
    @classmethod
    def get_pos(cls):
        pos = open('pos.txt', "r").read().split('\n')
        pos.pop()
        return pos
    
    @classmethod
    def get_neg(cls):
        neg = open('neg.txt', "r").read().split('\n')
        neg.pop()
        return neg
    @classmethod
    def get_horror(cls):
        h = pd.read_csv('공포.txt', encoding='UTF-8', names=['word'], sep='\n')
        horror = cls.decompose(cls.mecab.pos(' '.join(h.T.values[0])))
        for word in cls.minus_discard_list:
            horror.discard(word)
        return horror
    
    @classmethod
    def get_delight(cls):
        d = pd.read_csv('기쁨.txt', encoding='UTF-8', names=['word'], sep='\n')
        delight = cls.decompose(cls.mecab.pos(' '.join(d.T.values[0])))
        delight.discard('보')
        delight.discard('좋')
        return delight
    @classmethod
    def get_surprise(cls):
        s = pd.read_csv('놀람.txt', encoding='UTF-8', names=['word'], sep='\n')
        surprise = cls.decompose(cls.mecab.pos(' '.join(s.T.values[0])))
        surprise.discard('금')
        return surprise
    @classmethod
    def get_angry(cls):
        a = pd.read_csv('분노.txt', encoding='UTF-8', names=['word'], sep='\n')
        angry = cls.decompose(cls.mecab.pos(' '.join(a.T.values[0])))
        for word in cls.minus_discard_list:
            angry.discard(word)
        return angry
    @classmethod
    def get_sad(cls):
        s = pd.read_csv('슬픔.txt', encoding='UTF-8', names=['word'], sep='\n')
        sad = cls.decompose(cls.mecab.pos(' '.join(s.T.values[0])))
        sad.add('싫')
        for word in cls.minus_discard_list:
            sad.discard(word)
        return sad
    @classmethod
    def get_boring(cls):
        b = pd.read_csv('지루함.txt', encoding='UTF-8', names=['word'], sep='\n')
        boring = cls.decompose(cls.mecab.pos(' '.join(b.T.values[0])))
        return boring
    @classmethod
    def get_happy(cls):
        h = pd.read_csv('행복.txt', encoding='UTF-8', names=['word'], sep='\n')
        happy = cls.decompose(cls.mecab.pos(' '.join(h.T.values[0])))
        happy.discard('기분')
        happy.discard('속')
        return happy
    @classmethod
    def get_minus2(cls):
        down2 = pd.read_csv('down2.txt', encoding='UTF-8', names=['word'], sep='\n')
        minus2 = cls.decompose(cls.mecab.pos(' '.join(down2.T.values[0])))
        for word in cls.minus_discard_list:
            minus2.discard(word)
        return minus2
    @classmethod
    def get_minus3(cls):
        down3 = pd.read_csv('down3.txt', encoding='UTF-8', names=['word'], sep='\n')
        minus3 = cls.decompose(cls.mecab.pos(' '.join(down3.T.values[0])))
        minus3.add('싫')
        for word in cls.minus_discard_list:
            minus3.discard(word)
        return minus3
    def count_words(self):
        # 텍스트에서 명사만 추출하는 함수
        out = self.mecab.nouns(self.text)
        word_counts = {}
        for word in out:
            word_counts[word] = word_counts.get(word, 0) + 1
        
        sorted_word_counts = sorted(word_counts.items(), key=lambda x : x[1], reverse=True)
        
        for i in range(len(sorted_word_counts)):
            keyword = sorted_word_counts[i][0]
            if keyword in self.get_pos():
                sorted_word_counts[i] = list(sorted_word_counts[i])
                sorted_word_counts[i].append(1)
            elif keyword in self.set_update(self.get_delight(), self.get_happy()):
                sorted_word_counts[i] = list(sorted_word_counts[i])
                sorted_word_counts[i].append(1)
            elif keyword in self.get_neg():
                sorted_word_counts[i] = list(sorted_word_counts[i])
                sorted_word_counts[i].append(-1)
            elif keyword in self.set_update(self.get_minus2(), self.get_minus3()):
                sorted_word_counts[i] = list(sorted_word_counts[i])
                sorted_word_counts[i].append(-1)
            else:
                sorted_word_counts[i] = list(sorted_word_counts[i])
                sorted_word_counts[i].append(0)
        
        return sorted_word_counts
    def day_score(self):
        text = self.mecab.pos(self.text)
        cnt = 0
        score = 0
        p = []
        n = []
        txt = self.decompose(text)
        feel = {}
        for word in txt:
            if word in self.get_delight():
                score += 2
                cnt += 2
                feel['delight'] = feel.get('delight',0) + 1    
            elif word in self.get_happy():
                score += 3
                cnt += 3
                feel['happy'] = feel.get('happy',0) + 1    
            elif word in self.get_minus2():
                score -= 2
                cnt += 2
                if word in self.get_horror():
                    feel['horror'] = feel.get('horror',0) + 1    
                elif word in self.get_angry():
                    feel['angry'] = feel.get('angry',0) + 1    
                elif word in self.get_sad():
                    feel['sad'] = feel.get('sad',0) + 1    
            elif word in self.get_minus3():
                score -= 3
                cnt += 3
                if word in self.get_horror():
                    feel['horror'] = feel.get('horror',0) + 1    
                elif word in self.get_angry():
                    feel['angry'] = feel.get('angry',0) + 1
                elif word in self.get_sad():
                    feel['sad'] = feel.get('sad',0) + 1    
            elif word in self.get_pos():
                score += 1
                cnt += 1
                p.append(word)
            elif word in self.get_neg():
                score -= 1
                cnt += 1
                n.append(word)
        return score/cnt, feel
    def text_analysis(self):
        # 일일 감정점수
        score, feel = self.day_score()
        print(score, feel)
        # 일일 감정분류
        sorted_feel = sorted(feel.items(), key=lambda item:item[1], reverse=True)
        if len(sorted_feel) == 0:
            sorted_feel = [('boring', 0)]
        print(sorted_feel)
        # 단어 갯수 (wordcloud용)\
        # print('word count', self.count_words())
        word_count = self.count_words()
        print(word_count)
        return {
            "score": score,
            "feel": sorted_feel,
            "word_cound": word_count
        }
if __name__ == "__main__":
    text = open('text.txt','r').read()
    a = TextAnalysis(text)
    a.text_analysis()


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