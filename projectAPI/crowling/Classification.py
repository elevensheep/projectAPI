from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from sentence_transformers import SentenceTransformer
from datasets import load_dataset
import numpy as np

class KNNClassifier:
    def __init__(self, n_neighbors=3):
        self.model = KNeighborsRegressor(n_neighbors=n_neighbors, metric="cosine")
    
    def fit(self, X, y):
        self.model.fit(X, y)
    
    def predict(self, X):
        return self.model.predict(X)
    
    def score(self, X, y):
        predictions = self.predict(X)
        return mean_squared_error(y, predictions)

if __name__ == "__main__":
    # SBERT 모델 로드
    model = SentenceTransformer("jhgan/ko-sroberta-multitask")
    
    # KorSTS 데이터셋 로드
    dataset = load_dataset("klue", "sts")
    
    # 학습 데이터 준비
    train_sentences1 = dataset["train"]["sentence1"][:1000]
    train_sentences2 = dataset["train"]["sentence2"][:1000]
    train_scores = dataset["train"]["labels"][:1000]
    
    # 문장 벡터 변환
    X_train = np.array([model.encode(s1) - model.encode(s2) for s1, s2 in zip(train_sentences1, train_sentences2)])
    y_train = np.array(train_scores)
    
    # 테스트 데이터 준비
    test_sentences1 = dataset["validation"]["sentence1"][:200]
    test_sentences2 = dataset["validation"]["sentence2"][:200]
    test_scores = dataset["validation"]["labels"][:200]
    
    X_test = np.array([model.encode(s1) - model.encode(s2) for s1, s2 in zip(test_sentences1, test_sentences2)])
    y_test = np.array(test_scores)
    
    # KNN 유사도 모델 학습
    knn = KNNClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)
    
    # 예측 및 MSE 계산
    predictions = knn.predict(X_test)
    mse = knn.score(X_test, y_test)
    
    print(f"Mean Squared Error: {mse:.4f}")
    
    # 예제 문장 유사도 예측
    test_example_1 = "나는 커피를 마신다."
    test_example_2 = "나는 아메리카노를 즐겨 마신다."
    test_vector = model.encode(test_example_1) - model.encode(test_example_2)
    predicted_score = knn.predict([test_vector])[0]
    print(f"Predicted Similarity Score between test sentences: {predicted_score:.2f}")
