from News import News
import pandas as pd

if __name__ == '__main__':
    news = News()

    data = []

    for x in range(1, 50):  
        digitalTimes = news.digitalTimes(x)

        for category, texts in digitalTimes.items():
            for text in texts:  
                data.append([category, text])

    df = pd.DataFrame(data, columns=["Category", "Article"])

    df = df[~df["Article"].str.startswith("입력")]

    remove_words = ["정치", "경제", "사회", "국제", "피플"]
    df = df[~df["Article"].isin(remove_words)]  # ✅ "Category" 필터링

    df = df[~df["Article"].str.contains(r"\[.*?\]에게 고견을 듣는다\.", na=False, regex=True)]
    
    hotclick_rows = df[df["Article"].str.contains("이 시간 핫클릭", na=False)].index.tolist()

    for start_idx in hotclick_rows: 
        df = df.drop(df.index[df.index.get_loc(start_idx):df.index.get_loc(start_idx) + 10], errors="ignore")

    # ✅ CSV 파일로 저장 (UTF-8 인코딩)
    df.to_csv("news_data.csv", index=False, encoding="utf-8-sig")

    print("✅ 필터링된 뉴스 데이터가 'news_data.csv' 파일로 저장되었습니다!")
