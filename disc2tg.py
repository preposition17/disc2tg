import html

from discord_selfbot import SelfBot
from telebot import TeleBot

from config import (
    DISCORD_TOKEN,
    DISCORD_GUILD_ID
)
from config import (
    TELEGRAM_TOKEN,
    TELEGRAM_CHAT_ID
)

from config import DEBUG

from utils import (
    format_text,
    bold,
    code,
    text_wrap,
    get_exclude_channels
)


ds_bot = SelfBot(DISCORD_TOKEN)
tg_bot = TeleBot(TELEGRAM_TOKEN)

exclude_channels = get_exclude_channels()
# Че смотришь


@ds_bot.message_handler
def test_handler(message):
    if message.guild_id == DISCORD_GUILD_ID:
        if DEBUG:
            print(f"{message.author.fullname} {message.text}\n"
                  f"--------------------------------------------------------\n"
                  f"{message.guild.name}: {message.channel.name}\n"
                  f"--------------------------------------------------------\n"
                  f"{message.raw}\n")
            print()

        if message.channel_id in exclude_channels: return
        tg_bot.send_message(TELEGRAM_CHAT_ID,
                            f"{bold(html.escape(message.channel.name))}\n"
                            f"{bold(html.escape(message.author.fullname))}\n"
                            f"{code('——————————————————————')}\n"
                            f"{code(html.escape(message.text))}",
                            parse_mode='html'
                            )


if __name__ == '__main__':
    ds_bot.run(debug=False)
