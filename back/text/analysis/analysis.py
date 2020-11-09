import os
from collections import Counter

from eunjeon import Mecab
import pandas as pd

from django.conf import settings


class TextAnalysis:

    mecab = Mecab(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'NLP', 'mecab', 'mecab-ko-dic'))
    tag = ['VCP', 'VCN', 'NNG', 'IC', 'MAG', 'VA', 'VV', 'XR']
    stopwords=['의','가','이','은','들','는','좀','꽤','주','잘','걍','과','도','를','으로','자','에','와','한','하','다','있']
    minus_discard_list = ['웃음', '남부럽', '탄복', '가슴', '기분', '개', '자식', '기집', '터지', '되', '오르', '만족', '속', '유쾌', '의심', '끼치', '치', '안정', '느끼']

    pos = []
    neg = []
    horror = []
    delight = []
    surprise = []
    angry = []
    sad = []
    boring = []
    happy = []
    minus2 = []
    minus3 = []

    # def __init__(self, text):
    #     self.text = text
    def __init__(self, data):
        self.content = data['content']
        self.title = data['title']        
        self.emotions = [
            sticker['emotion']['name'] for sticker in data['stickers']
        ]

    @classmethod
    def decompose(cls, ls):

        word_list = []

        for word in ls:
            if '+' in word[1]:
                if word[1].split('+')[0] in cls.tag and word[0] not in cls.stopwords:
                    word_list.append(word[0])
            elif word[1] in cls.tag and word[0] not in cls.stopwords:
                word_list.append(word[0])
        
        return set(word_list)

    @classmethod
    def get_pos(cls):
        if cls.pos:
            return cls.pos
        pos = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pos.txt'), "r", encoding="cp949").read().split('\n')        
        pos.pop()

        cls.pos = pos
        return pos
    
    @classmethod
    def get_neg(cls):
        if cls.neg:
            return cls.neg
        neg = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'neg.txt'), "r", encoding="cp949").read().split('\n')

        neg.pop()

        cls.neg = neg
        return neg

    @classmethod
    def get_horror(cls):
        if cls.horror:
            return cls.horror
        h = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'horror.txt'), encoding='UTF-8', names=['word'], sep='\n')
        horror = cls.decompose(cls.mecab.pos(' '.join(h.T.values[0])))

        for word in cls.minus_discard_list:
            horror.discard(word)
        
        cls.horror = horror
        return horror
    
    @classmethod
    def get_delight(cls):
        if cls.delight:
            return cls.delight
        d = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'delight.txt'), encoding='UTF-8', names=['word'], sep='\n')
        delight = cls.decompose(cls.mecab.pos(' '.join(d.T.values[0])))
        delight.discard('보')
        delight.discard('좋')
        delight.discard('재미있')
        # print(delight)
        cls.delight = delight
        return delight

    @classmethod
    def get_surprise(cls):
        if cls.surprise:
            return cls.surprise
        s = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'surprise.txt'), encoding='UTF-8', names=['word'], sep='\n')
        surprise = cls.decompose(cls.mecab.pos(' '.join(s.T.values[0])))
        surprise.discard('금')

        cls.surprise = surprise
        return surprise

    @classmethod
    def get_angry(cls):
        if cls.angry:
            return cls.angry
        a = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'angry.txt'), encoding='UTF-8', names=['word'], sep='\n')
        angry = cls.decompose(cls.mecab.pos(' '.join(a.T.values[0])))

        for word in cls.minus_discard_list:
            angry.discard(word)
        
        cls.angry = angry
        return angry

    @classmethod
    def get_sad(cls):
        if cls.sad:
            return cls.sad
        s = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sad.txt'), encoding='UTF-8', names=['word'], sep='\n')
        sad = cls.decompose(cls.mecab.pos(' '.join(s.T.values[0])))
        sad.add('싫')

        for word in cls.minus_discard_list:
            sad.discard(word)
        
        cls.sad = sad
        return sad

    @classmethod
    def get_boring(cls):
        if cls.boring:
            return cls.boring
        b = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'boring.txt'), encoding='UTF-8', names=['word'], sep='\n')
        boring = cls.decompose(cls.mecab.pos(' '.join(b.T.values[0])))

        cls.boring = boring
        return boring

    @classmethod
    def get_happy(cls):
        if cls.happy:
            return cls.happy
        h = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'happy.txt'), encoding='UTF-8', names=['word'], sep='\n')
        happy = cls.decompose(cls.mecab.pos(' '.join(h.T.values[0])))
        happy.discard('기분')
        happy.discard('속')

        cls.happy = happy
        return happy

    @classmethod
    def get_minus2(cls):
        if cls.minus2:
            return cls.minus2
        down2 = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'down2.txt'), encoding='UTF-8', names=['word'], sep='\n')
        minus2 = cls.decompose(cls.mecab.pos(' '.join(down2.T.values[0])))

        for word in cls.minus_discard_list:
            minus2.discard(word)
        
        cls.minus2 = minus2
        return minus2

    @classmethod
    def get_minus3(cls):
        if cls.minus3:
            return cls.minus3
        down3 = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'down3.txt'), encoding='UTF-8', names=['word'], sep='\n')
        minus3 = cls.decompose(cls.mecab.pos(' '.join(down3.T.values[0])))
        minus3.add('싫')

        for word in cls.minus_discard_list:
            minus3.discard(word)
        
        cls.minus3 = minus3
        return minus3

    def count_words(self):
        # 텍스트에서 명사만 추출하는 함수
        out = self.mecab.nouns(self.content)
        out_title = self.mecab.nouns(self.title)
        out += out_title
        word_counts = Counter(out)
        
        sorted_word_counts = sorted(word_counts.items(), key=lambda x : x[1], reverse=True)
        
        for i in range(len(sorted_word_counts)):
            keyword = sorted_word_counts[i][0]
            if keyword in self.get_pos():
                sorted_word_counts[i] = list(sorted_word_counts[i])
                sorted_word_counts[i].append(1)
            elif keyword in self.get_delight():
                sorted_word_counts[i] = list(sorted_word_counts[i])
                sorted_word_counts[i].append(1)
            elif keyword in self.get_happy():
                sorted_word_counts[i] = list(sorted_word_counts[i])
                sorted_word_counts[i].append(1)
            elif keyword in self.get_neg():
                sorted_word_counts[i] = list(sorted_word_counts[i])
                sorted_word_counts[i].append(-1)
            elif keyword in self.get_minus2():
                sorted_word_counts[i] = list(sorted_word_counts[i])
                sorted_word_counts[i].append(-1)
            elif keyword in self.get_minus3():
                sorted_word_counts[i] = list(sorted_word_counts[i])
                sorted_word_counts[i].append(-1)
            else:
                sorted_word_counts[i] = list(sorted_word_counts[i])
                sorted_word_counts[i].append(0)
        
        return sorted_word_counts

    def calc_score(self, source, feel, cnt, score, p, n, is_title=False):
        additional_score = 0
        if is_title:
            additional_score = 1

        analyzed_source = self.mecab.pos(source)
        word_list = self.decompose(analyzed_source)
        for word in word_list:
            if word in self.get_delight():
                score += 2 + additional_score
                cnt += 2 + additional_score
                feel['delight'] = feel.get('delight',0) + 1 + additional_score  
            elif word in self.get_happy():
                score += 3 + additional_score
                cnt += 3 + additional_score
                feel['happy'] = feel.get('happy',0) + 1 + additional_score  
            elif word in self.get_minus2():
                score -= 2 + additional_score
                cnt += 2 + additional_score
                if word in self.get_horror():
                    feel['horror'] = feel.get('horror',0) + 1 + additional_score  
                elif word in self.get_angry():
                    feel['angry'] = feel.get('angry',0) + 1 + additional_score  
                elif word in self.get_sad():
                    feel['sad'] = feel.get('sad',0) + 1 + additional_score
            elif word in self.get_minus3():
                score -= 3 + additional_score
                cnt += 3 + additional_score
                if word in self.get_horror():
                    feel['horror'] = feel.get('horror',0) + 1 + additional_score
                elif word in self.get_angry():
                    feel['angry'] = feel.get('angry',0) + 1 + additional_score
                elif word in self.get_sad():
                    feel['sad'] = feel.get('sad',0) + 1 + additional_score  
            elif word in self.get_boring():
                feel['boring'] = feel.get('boring', 0) + 1 + additional_score
            elif word in self.get_surprise():
                feel['surprise'] = feel.get('surprise', 0) + 1 + additional_score
            elif word in self.get_pos():
                score += 1 + additional_score
                cnt += 1 + additional_score
                p.append(word)
            elif word in self.get_neg():
                score -= 1 + additional_score
                cnt += 1 + additional_score
                n.append(word)

    def day_score(self):
        cnt = 0
        score = 0
        p = []
        n = []

        feel = {}
        self.calc_score(self.content, feel, cnt, score, p, n, is_title=False)
        self.calc_score(self.title, feel, cnt, score, p, n, is_title=True)

        for emotion in self.emotions:
            if emotion:
                feel[emotion] = feel.get(emotion, 0) + 2 

        if cnt == 0:
            return cnt, feel
        return score/cnt, feel

    def text_analysis(self):
        # 일일 감정점수
        score, feel = self.day_score()

        # 일일 감정분류
        for key, value in feel.items():
            if score > 0:
                if key == 'horror' or key == 'angry' or key =='sad':
                    feel[key] = 0
            elif score < 0:
                if key == 'happy' or key == 'delight':
                    feel[key] = 0
                    
        sorted_feel = sorted(feel.items(), key=lambda item:item[1], reverse=True)
        if len(sorted_feel) == 0:
            sorted_feel = [('boring', 0)]

        # 단어 갯수 (wordcloud용)\
        # print('word count', self.count_words())
        word_count = self.count_words()

        return {
            "score": score,
            "feel": sorted_feel,
            "word_count": word_count
        }

if __name__ == "__main__":
    data = {
        'title' : '다행이다.',
        'content' : '''약도 아침/자기전으로 잘 챙겨먹고

        옛날보다 더 몸이 건강해진것같다

        지금 이 몸무게에 들어갈수 없었던 바지도 잘들어가고

        너무 좋다 그리고 과하게 살이 쪘을땐 뭐든지 짜증이 났는데

        별다른 이벤트가 없다면 그냥 그러려니 잘 넘긴다

        나 정말 다행이야

        어제는 사고싶은 옷들이 있어서 인터넷으로 옷을 주문했다

        그리고 돈을 아끼려고 많이 노력중이다

        나 잘할수 있다고 믿을래!''',
        'stickers' : [{'emotion': {'name': 'happy'}}, {'emotion': {'name':'delight'}}]
    }
    a = TextAnalysis(data)
    # print(a)
    a.text_analysis()
