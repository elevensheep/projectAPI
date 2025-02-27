from Classification import NewsWord2Vec
# ✅ 클래스 인스턴스 생성
news_model = NewsWord2Vec("projectAPI/crowling/news_data.csv")

# ✅ 데이터 로드 & 전처리
news_model.load_data()

# ✅ Word2Vec 학습
news_model.train_word2vec()

# ✅ 특정 단어 벡터 확인 (예: '시간' in 'politics' 카테고리)
word_vector = news_model.get_word_vector("politics", "시간")
print("🔹 '시간' 단어 벡터:", word_vector)

# ✅ 특정 단어와 유사한 단어 확인
similar_words = news_model.get_similar_words("politics", "시간", topn=10)
print("🔹 '시간'과 유사한 단어:", similar_words)
