from News import News

if __name__ == '__main__':
    news = News()
    digitalTimes = news.digitalTimes(1)
    
    # 결과 출력
    for category, texts in digitalTimes.items():
        print(f"\n🔹 Category {category}:")
        print(texts)