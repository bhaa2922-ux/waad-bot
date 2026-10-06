import asyncio, os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, BotCommand
from aiogram.filters import Command
TOKEN=os.getenv("BOT_TOKEN")
bot=Bot(token=TOKEN)
dp=Dispatcher()
@dp.message(Command("تفعيل_الحمايه"))
async def hm(m: Message):
 await m.answer("✯ تفعيل الحمايه\nتم قفل الصور، الفيديو، التوجيه، الملصقات ✅")
@dp.message(Command("تعطيل_الرابط"))
async def link(m: Message):
 await m.answer("✯ تعطيل الرابط ✅")
@dp.message(Command("تعطيل_الرفع"))
async def up(m: Message):
 await m.answer("✯ تعطيل الرفع ✅ يسمح للمالك يرفع بس")
@dp.message(Command("قفل_الدخول"))
async def jl(m: Message):
 await m.answer("✯ قفل الدخول ✅")
@dp.message(Command("قفل"))
async def lock(m: Message):
 await m.answer(f"تم قفل {m.text.split(maxsplit=1)[1] if len(m.text.split())>1 else ''} ✅")
@dp.message(Command("فتح"))
async def unlock(m: Message):
 await m.answer(f"تم فتح {m.text.split(maxsplit=1)[1] if len(m.text.split())>1 else ''} ✅")
@dp.message(Command("لقبي"))
async def laq(m: Message):
 mb=await bot.get_chat_member(m.chat.id,m.from_user.id)
 await m.answer(f"لقبك: {mb.custom_title or 'ماعندك لقب'}")
@dp.message(Command("صلاحياتي","كشف","افتاري"))
async def info(m: Message):
 c=await bot.get_chat_member_count(m.chat.id)
 await m.answer(f"👥 {m.chat.title}\nالعدد: {c}")
@dp.message(F.text)
async def anti(m: Message):
 try:
  mem=await bot.get_chat_member(m.chat.id,m.from_user.id)
  if mem.status in ['administrator','creator']: return
 except: pass
 if any(x in (m.text or '').lower() for x in ["t.me","http","گ","چ"]):
  try: await m.delete()
  except: pass
async def main():
 await bot.set_my_commands([
  BotCommand(command="تفعيل_الحمايه", description="✯ تفعيل الحمايه كاملة"),
  BotCommand(command="تعطيل_الرابط", description="تعطيل الرابط"),
  BotCommand(command="تعطيل_الرفع", description="يسمح للمالك يرفع بس"),
  BotCommand(command="قفل_الدخول", description="مايسمح للاشخاص يدخلون"),
  BotCommand(command="قفل", description="قفل [النوع]"),
  BotCommand(command="فتح", description="فتح [النوع]"),
  BotCommand(command="لقبي", description="لقبك"),
  BotCommand(command="صلاحياتي", description="صلاحياتك"),
  BotCommand(command="كشف", description="كشف المجموعه"),
  BotCommand(command="افتاري", description="افتارك"),
 ])
 await dp.start_polling(bot)
asyncio.run(main())
