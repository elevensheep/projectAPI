import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize
from gensim.models import Word2Vec
from collections import defaultdict

nltk.download('punkt_tab')
# 한글 자연어처리를 위해 nltk 라이브러리의 한국어 지원을 추가
nltk.download('punkt')

# ✅ CSV 파일 불러오기
df = pd.read_csv("projectAPI/crowling/news_data.csv")

# ✅ 데이터 전처리: 한글 & 공백만 남기고 나머지 제거
def clean_text(text):
    text = re.sub(r"[^가-힣\s]", "", str(text))  # 한글과 공백만 남기기
    text = re.sub(r"\s+", " ", text).strip()  # 불필요한 공백 제거
    return text

df["Article"] = df["Article"].apply(clean_text)

# ✅ 카테고리별로 기사 문장을 리스트에 저장
category_sentences = defaultdict(list)

for _, row in df.iterrows():
    category = row["Category"]
    words = word_tokenize(row["Article"])  # 기사 내용을 단어 토큰화
    category_sentences[category].append(words)

# ✅ Word2Vec 모델 학습
category_models = {}

for category, sentences in category_sentences.items():
    if len(sentences) > 1:  # 학습할 데이터가 있는 경우만 진행
        model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)
        category_models[category] = model
        print(f"✅ {category} 카테고리 Word2Vec 모델 학습 완료!")

# ✅ 특정 카테고리의 단어 벡터 확인 (예: 'politics')
example_category = "politics"

if example_category in category_models:
    model = category_models[example_category]
    word = "시간"  # 예제 단어
    if word in model.wv:
        print(f"\n🔹 '{word}' 단어 벡터 (politics 카테고리):")
        print(model.wv[word])
    else:
        print(f"❌ '{word}' 단어가 모델에 없음.")

similar_words = model.wv.most_similar("시간", topn=10)
print("🔹 시간:", similar_words)
