# 단어 갯수 세기
def count_words(text):
    # 텍스트에서 명사만 추출하는 함수
    out = mecab.morphs(text)

    word_counts = {}

    for word in out:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

from eunjeon import Mecab
mecab = Mecab()
text = "아침에 눈을 뜨는 순간부터 감사함을 찾았습니다. 잠을 푹 자서 피로가 말끔히 풀린 건강한 몸으로 일어날 수 있음에 감사합니다. 덕분에 하루종일 기분이 좋았습니다. 이런 좋은 감정을 유지한 나에게 감사합니다."
# 텍스트를 형태소 단위로 나누는 함수. 파라미터의 norm은 문장을 정규화, stem은 각 단어에서 어간을 추출
out1 = mecab.morphs(text)
# 텍스트에서 명사만 추출하는 함수
out2 = mecab.nouns(text)
# 각 품사를 태깅하는 함수. 텍스트를 형태소 단위로 나눈 후 나뉘어진 형태소를 해당하는 품사와 함께 리스트화.
# 파라미터에는 norm, stem, join(나눠진 형태소와 품사를 형태소/품사 형태로 리스트화)
out3 = mecab.pos(text)
print('morphs',out1)
print('nouns',out2)
print('pos',out3)
print()

out4 = count_words(text)
print('word count', out4)