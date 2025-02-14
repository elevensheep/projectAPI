from bs4 import BeautifulSoup
import requests

class News:
    
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0"}
    
    def get(self, url):
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()  
            response.encoding = response.apparent_encoding
            return BeautifulSoup(response.text, "html.parser")
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Error fetching {url}: {e}")
            return None
    
    def parse(self, soup):
        if not soup:
            return []
        
        span_tags = soup.find_all("span")
        texts = [span.text.strip() for span in span_tags if span.text.strip()]
        
        return texts
    
    # 신문사 : 중앙, 조선, 국민, ytn, 동아, 디지털타임즈, jtbc, mbc, 뉴시스, 서울신문

    
    def joongang(self, pageNum):
        pass
    def chosun(self, pageNum):
        pass
    def kmlb(self, pageNum):
        pass
    def ytn(self, pageNum):
        pass
    def donga(self, pageNum):
        pass
    def digitalTimes(self, pageNum):
        # section_num : 정치 : 2400, 경제 : 3200, 산업 : 2200, ict : 2000, 금융 : 3100, 부동산 : 3500, 국제 : 2300, 사회 : 3700
        categorys = [2400, 3200, 2200, 2000, 3100, 3500, 2300, 3700]
        results = {}

        for category in categorys:
            url = f'https://www.dt.co.kr/section.html?section_num={category}&cpage={pageNum}'
            soup = self.get(url)
            texts = self.parse(soup)
            
            results[category] = texts 
        
        return results
    def jtbc(self, pageNum):
        pass
    def mbc(self, pageNum):
        pass
    def newsis(self, pageNum):
        pass
    def seoul(self, pageNum):
        pass
    


