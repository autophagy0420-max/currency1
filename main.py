import yfinance as yf
import time

def get_realtime_data():
    print("🚀 실시간 자산 데이터 분석을 시작합니다...")
    
    # 1. 환율 가져오기
    ticker = yf.Ticker("USDKRW=X")
    data = ticker.history(period="1d")
    current_rate = data['Close'].iloc[-1]
    

    print("\n" + "="*35)
    print(f"💵 현재 원/달러 환율: {current_rate:.2f}원")
    print("="*35)
    
    # 상황에 맞춘 간단한 조언
    if current_rate > 1500:
        print("⚠️ 환율이 1,500원을 넘었습니다. 달러 추가 매수는 신중하세요!")
    
    # ($114k) 대비 분석 (BTC 2개 보유 기준)
 

if __name__ == "__main__":
    get_realtime_data()