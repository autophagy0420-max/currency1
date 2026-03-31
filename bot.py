import yfinance as yf
import asyncio
from telegram import Bot

# 1단계에서 받은 정보들을 여기에 넣으세요
TOKEN = '8773453459:AAEj9ALMpp9noyNdLj0WUmpvG_QBtACDQGE'
CHAT_ID = '1759062545'

async def send_alert():
    bot = Bot(token=TOKEN)
    
    # 환율 데이터 가져오기
    ticker = yf.Ticker("USDKRW=X")
    data = ticker.history(period="1d")
    rate = data['Close'].iloc[-1]
    
    message = f"🔔 [자산 알림]\n💵 현재 환율: {rate:.2f}원"
    
    if rate > 1530:
        message += "\n⚠️ 환율이 매우 높습니다! 대응이 필요할 수 있습니다."
    
    await bot.send_message(chat_id=CHAT_ID, text=message)
    print(f"✅ 알림 전송 완료: {rate:.2f}원")

if __name__ == "__main__":
    asyncio.run(send_alert())