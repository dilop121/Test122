from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
import logging

# Set up logging to monitor bot's activity
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to handle when a new member joins the group
def new_member(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        # This is a simple notification when a new member joins
        context.bot.send_message(
            chat_id=update.message.chat_id,
            text=f"New member {member.full_name} joined the group."
        )

# Function to detect video chat invitations and reactions
def handle_video_chat(update: Update, context: CallbackContext):
    # If a message contains a video chat invitation
    if update.message.video_chat_started:
        context.bot.send_message(
            chat_id=update.message.chat_id,
            text="A video chat has started!"
        )

    # For members joining the video chat (this might not work directly for all video chat events)
    if update.message.video_chat_participant_joined:
        context.bot.send_message(
            chat_id=update.message.chat_id,
            text=f"{update.message.video_chat_participant_joined} has joined the video chat."
        )

# Main function to run the bot
def main():
    # Use your own bot token here
    bot_token = '7581811310:AAFV_hoOlzbrctAxaz_0eQtwk9oTttGR9N8'
    
    updater = Updater(token=bot_token, use_context=True)
    dp = updater.dispatcher

    # Handlers for new member and video chat messages
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, new_member))
    dp.add_handler(MessageHandler(Filters.video_chat, handle_video_chat))

    # Start polling for messages
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
