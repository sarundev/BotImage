import os
from dotenv import load_dotenv
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, BotCommand

# Load environment variables from .env file
load_dotenv()

API_TOKEN = os.getenv('BOT_TOKEN')

if not API_TOKEN:
    raise ValueError("No BOT_TOKEN found. Please check your .env file.")

bot = telebot.TeleBot(API_TOKEN)

REGISTER_TEXT = (
    "🚀 ត្រៀមខ្លួនរីកចម្រើនជំនួញរបស់អ្នកហើយឬនៅ?\n\n"
    "📖 វគ្គសិក្សា៖ ជំនាញជំនួញ និងទីផ្សារ\n"
    "⏳ រយៈពេល៖ ៦ សប្តាហ៍\n"
    "🎥 ទម្រង់៖ មេរៀនជាវីដេអូ + ថ្នាក់សួរ-ឆ្លើយផ្សាយផ្ទាល់\n"
    "🏆 វិញ្ញាបនបត្រ៖ មាន នៅពេលបញ្ចប់វគ្គសិក្សា\n\n"
    "ដើម្បីចុះឈ្មោះ សូមទាក់ទងតាម /contact។"
)

LESSONS_TEXT = (
    "📚 មេរៀនក្នុងវគ្គសិក្សា៖\n\n"
    "១. មូលដ្ឋានគ្រឹះនៃជំនួញ\n"
    "២. យុទ្ធសាស្ត្រទីផ្សារ\n"
    "៣. ការកសាងម៉ាក (Branding)\n"
    "៤. ទីផ្សារឌីជីថល និងបណ្តាញសង្គម\n"
    "៥. ការលក់ និងការបិទកិច្ចព្រមព្រៀង\n"
    "៦. ការគ្រប់គ្រងហិរញ្ញវត្ថុ និងការរីកលូតលាស់\n\n"
    "មេរៀននីមួយៗមានវីដេអូ និងលំហាត់អនុវត្តន៍។"
)

SCHEDULES_TEXT = (
    "📅 កាលវិភាគថ្នាក់ផ្សាយផ្ទាល់៖\n\n"
    "🗓️ រៀងរាល់ថ្ងៃអង្គារ — ម៉ោង ៧ យប់ (សួរ-ឆ្លើយ)\n"
    "🗓️ រៀងរាល់ថ្ងៃសៅរ៍ — ម៉ោង ១០ ព្រឹក (សិក្ខាសាលា)\n\n"
    "តំណចូលរួមនឹងផ្ញើជូនមុនពេលចាប់ផ្តើម។"
)

FAQ_TEXT = (
    "❓ សំណួរញឹកញាប់៖\n\n"
    "🔹 តើខ្ញុំត្រូវមានបទពិសោធន៍ជាមុនទេ?\n"
    "→ ទេ! វគ្គនេះសមរម្យសម្រាប់អ្នកចាប់ផ្តើមដំបូង។\n\n"
    "🔹 តើខ្ញុំអាចមើលមេរៀនពេលណាក៏បាន?\n"
    "→ បាទ/ចាស វីដេអូអាចមើលបានគ្រប់ពេល។\n\n"
    "🔹 តើមានវិញ្ញាបនបត្រទេ?\n"
    "→ មាន នៅពេលអ្នកបញ្ចប់វគ្គសិក្សា។\n\n"
    "🔹 តើតម្លៃប៉ុន្មាន?\n"
    "→ សូមទាក់ទង /contact សម្រាប់ព័ត៌មានតម្លៃ។"
)

CONTACT_TEXT = (
    "📞 ទាក់ទងមកយើង៖\n\n"
    "✉️ Telegram៖ @YourSupport\n"
    "📧 អ៊ីមែល៖ support@example.com\n"
    "🕘 ម៉ោងធ្វើការ៖ ច័ន្ទ–សុក្រ ៨ព្រឹក–៥ល្ងាច\n\n"
    "ក្រុមការងារយើងរីករាយជួយឆ្លើយរាល់សំណួររបស់អ្នក!"
)

HELP_TEXT = (
    "💡 របៀបប្រើប្រាស់ Bot នេះ៖\n\n"
    "១. ចុចប៊ូតុងខាងក្រោម ឬប្រើ Command (ឧ. /lessons) ដើម្បីស្វែងរកព័ត៌មាន។\n"
    "២. បើអ្នកចង់ចាប់ផ្តើមឡើងវិញ សូមវាយ /start\n"
    "៣. បើមានបញ្ហា សូមទាក់ទងមកយើងតាម /contact។"
)

ABOUT_TEXT = (
    "🏢 អំពី BizGrow Academy Bot\n\n"
    "Bot នេះបង្កើតឡើងដើម្បីជួយសម្រួលដល់សិស្សានុសិស្សក្នុងការស្វែងរកមេរៀន មើលកាលវិភាគ និងទាក់ទងក្រុមការងារបានយ៉ាងឆាប់រហ័ស។\n"
    "យើងប្តេជ្ញាផ្តល់នូវចំណេះដឹងផ្នែកជំនួញនិងទីផ្សារដ៏ល្អបំផុតសម្រាប់អ្នក!"
)

STATS_TEXT = (
    "📊 ស្ថិតិវគ្គសិក្សា៖\n\n"
    "👨‍🎓 សិស្សដែលបានចុះឈ្មោះសរុប៖ ៥០០+ នាក់\n"
    "⏳ ម៉ោងសិក្សាសរុប៖ ២៤ ម៉ោង\n"
    "⚙️ (មុខងារតាមដានការសិក្សាផ្ទាល់ខ្លួន នឹងមានក្នុងពេលឆាប់ៗនេះ)"
)

FEEDBACK_TEXT = (
    "📝 ផ្ញើមតិយោបល់៖\n\n"
    "យើងស្វាគមន៍រាល់មតិយោបល់របស់អ្នកដើម្បីកែលម្អសេវាកម្មរបស់យើង។\n"
    "សូមផ្ញើមតិយោបល់របស់អ្នកដោយផ្ទាល់ទៅកាន់ /contact។"
)

# Set up the bot's command menu
bot.set_my_commands([
    BotCommand("start", "ចាប់ផ្តើម"),
    BotCommand("help", "របៀបប្រើ"),
    BotCommand("about", "អំពី Bot នេះ"),
    BotCommand("stats", "ស្ថិតិ"),
    BotCommand("feedback", "ផ្ញើមតិយោបល់")
])

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Create the custom reply keyboard
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    
    # Define buttons
    btn_enroll = KeyboardButton("✍️ ចុះឈ្មោះ")
    btn_lessons = KeyboardButton("📚 មេរៀន")
    btn_schedules = KeyboardButton("📅 ថ្នាក់ផ្សាយផ្ទាល់")
    btn_faq = KeyboardButton("❓ សំណួរញឹកញាប់")
    btn_contact = KeyboardButton("📞 ជំនួយ")
    
    # Add buttons to markup
    # Row 1
    markup.add(btn_enroll, btn_lessons)
    # Row 2
    markup.add(btn_schedules, btn_faq)
    # Row 3 (Full width)
    markup.add(btn_contact)

    # Welcome message text
    welcome_text = (
        "សូមស្វាគមន៍មកកាន់ BizGrow Academy! 🎓\n\n"
        "យើងជួយសហគ្រិន និងអ្នកជំនាញ ឲ្យពង្រីកផ្នែកជំនួញ និងទីផ្សារ — ចាប់ពីយុទ្ធសាស្ត្រ រហូតដល់ការលក់តាមអនឡាញ។\n\n"
        "📚 /lessons — មើលមេរៀនវគ្គសិក្សា\n"
        "✍️ /enroll — ចុះឈ្មោះចូលរៀន\n"
        "📅 /schedules — មើលថ្នាក់ផ្សាយផ្ទាល់\n"
        "❓ /faq — សំណួរញឹកញាប់\n"
        "📞 /contact — ទាក់ទងក្រុមការងារ\n\n"
        "សូមចុចប៊ូតុងខាងក្រោម ដើម្បីចាប់ផ្តើម។\n"
        "ប្រើ /off ដើម្បីផ្អាកការងារ។"
    )
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

# Handlers for inline commands
@bot.message_handler(commands=['register', 'enroll'])
def handle_register_command(message):
    bot.reply_to(message, REGISTER_TEXT)

@bot.message_handler(commands=['lessons'])
def handle_lessons_command(message):
    bot.reply_to(message, LESSONS_TEXT)

@bot.message_handler(commands=['schedules'])
def handle_schedules_command(message):
    bot.reply_to(message, SCHEDULES_TEXT)

@bot.message_handler(commands=['faq'])
def handle_faq_command(message):
    bot.reply_to(message, FAQ_TEXT)

@bot.message_handler(commands=['contact'])
def handle_contact_command(message):
    bot.reply_to(message, CONTACT_TEXT)

@bot.message_handler(commands=['help'])
def handle_help_command(message):
    bot.reply_to(message, HELP_TEXT)

@bot.message_handler(commands=['about'])
def handle_about_command(message):
    bot.reply_to(message, ABOUT_TEXT)

@bot.message_handler(commands=['stats'])
def handle_stats_command(message):
    bot.reply_to(message, STATS_TEXT)

@bot.message_handler(commands=['feedback'])
def handle_feedback_command(message):
    bot.reply_to(message, FEEDBACK_TEXT)

# Handlers for keyboard button presses
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    text = message.text
    if text == "✍️ ចុះឈ្មោះ":
        bot.reply_to(message, REGISTER_TEXT)
    elif text == "📚 មេរៀន":
        bot.reply_to(message, LESSONS_TEXT)
    elif text == "📅 ថ្នាក់ផ្សាយផ្ទាល់":
        bot.reply_to(message, SCHEDULES_TEXT)
    elif text == "❓ សំណួរញឹកញាប់":
        bot.reply_to(message, FAQ_TEXT)
    elif text == "📞 ជំនួយ":
        bot.reply_to(message, CONTACT_TEXT)

print("Bot is running...")
bot.infinity_polling()
