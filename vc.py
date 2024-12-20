from telegram import Update
from telegram.ext import Application, MessageHandler, CallbackContext
from telegram.ext import filters
import logging
import asyncio

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

async def new_member(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        await context.bot.send_message(
            chat_id=update.message.chat_id,
            text=f"New member {member.full_name} joined the group."
        )

async def handle_video_chat(update: Update, context: CallbackContext):
    group_name = update.message.chat.title

    if update.message.video_chat_started:
        await context.bot.send_message(
            chat_id=update.message.chat_id,
            text=f"A video chat has started in {group_name}!"
        )

    if update.message.video_chat_participant_joined:
        await context.bot.send_message(
            chat_id=update.message.chat_id,
            text=f"{update.message.video_chat_participant_joined} has joined the video chat in {group_name}."
        )

    if update.message.video_chat_ended:
        await context.bot.send_message(
            chat_id=update.message.chat_id,
            text=f"The video chat has ended in {group_name}."
        )

async def main():
    bot_token = '7581811310:AAFV_hoOlzbrctAxaz_0eQtwk9oTttGR9N8'
    
    application = Application.builder().token(bot_token).build()

    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, new_member))
    application.add_handler(MessageHandler(filters.TEXT, handle_video_chat))

    await application.run_polling()

if __name__ == '__main__':
    try:
        import nest_asyncio
        nest_asyncio.apply()  # This is for environments that already have an event loop (e.g., Jupyter Notebooks)
        asyncio.run(main())
    except RuntimeError:
        # If an event loop is already running, just use await directly
        import sys
        loop = asyncio.get_event_loop()
        if loop.is_running():
            loop.create_task(main())
        else:
            asyncio.run(main())
