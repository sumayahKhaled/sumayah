from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import random
import asyncio

# اكتب التوكن الخاص بالبوت هنا
TOKEN = '7976174930:AAE4Kk5-au527T_gBuekzkPAp_3vMkNpD1Q'

# تخزين أرقام التخمين لكل مستخدم
user_guesses = {}

# دالة البدء
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    random_number = random.randint(1, 10)
    user_guesses[user_id] = random_number
    await update.message.reply_text(
        "مرحباً! أنا بوت لعبة التخمين 🎮\nأفكر في رقم بين 1 و 10، حاول تخمينه!"
    )

# دالة التحقق من التخمين
async def guess(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in user_guesses:
        await update.message.reply_text("ابدأ اللعبة أولاً باستخدام الأمر /start!")
        return

    try:
        guess_number = int(update.message.text)
        correct_number = user_guesses[user_id]

        if guess_number == correct_number:
            await update.message.reply_text("🎉 أحسنت! لقد خمنت الرقم بشكل صحيح!")
            del user_guesses[user_id]  # حذف الرقم بعد الفوز
        else:
            await update.message.reply_text("❌ لم تخمن بشكل صحيح، حاول مرة أخرى!")
    except ValueError:
        await update.message.reply_text("الرجاء إرسال رقم صحيح بين 1 و 10.")

# تشغيل البوت
async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # إضافة معالجات الأوامر
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, guess))

    print("البوت يعمل... 🎮")
    await app.run_polling()

if __name__ == '__main__':
    asyncio.run(main())