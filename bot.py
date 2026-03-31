import yfinance as yf
import asyncio
from telegram import Bot
import os

# 원혁님의 정보를 여기에 직접 입력하세요
TOKEN = '원혁님의_텔레그램_봇_토큰'
CHAT_ID = '원혁님의_텔레그램_채팅_ID'

async def send_alert():
    try:
        # 1. 환율 데이터 가져오기 (yfinance)
        ticker = yf.Ticker("USDKRW=X")
        data = ticker.history(period="1d")
        
        if data.empty:
            print("데이터를 가져오지 못했습니다.")
            return
            
        rate = data['Close'].iloc[-1]
        
        # 2. 메시지 구성
        message = f"🔔 [자산 실시간 알림]\n💵 현재 환율: {rate:.2f}원"
        
        if rate > 1530:
            message += "\n⚠️ 환율이 1,530원을 돌파했습니다! 대응이 필요할 수 있습니다."
        
        # 3. 텔레그램 전송
        bot = Bot(token=TOKEN)
        await bot.send_message(chat_id=CHAT_ID, text=message)
        print(f"✅ 알림 전송 완료: {rate:.2f}원")
        
    except Exception as e:
        print(f"❌ 에러 발생: {e}")

if __name__ == "__main__":
    asyncio.run(send_alert())
