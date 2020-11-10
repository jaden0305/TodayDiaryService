import pandas as pd
import numpy as np
import random
from analysis import TextAnalysis

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
out = a.text_analysis()
emotion = out['feel'][0][0]

data = pd.read_csv('C:/Users/multicampus/Desktop/response.csv', encoding='CP949')

choice = random.choice(data[emotion])
print(choice)