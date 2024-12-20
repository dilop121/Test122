from telegram import Update
from telegram.ext import Application, MessageHandler, CallbackContext
from telegram.ext import filters
import logging

# Set up logging to monitor bot's activity
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to handle when a new member joins the group
async def new_member(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        # This is a simple notification when a new member joins
        await context.bot.send_message(
            chat_id=update.message.chat_id,
            text=f"New member {member.full_name} joined the group."
        )

# Function to detect video chat invitations and reactions
async def handle_video_chat(update: Update, context: CallbackContext):
    group_name = update.message.chat.title  # Get the group name

    # If a message contains a video chat invitation
    if update.message.video_chat_started:
        await context.bot.send_message(
            chat_id=update.message.chat_id,
            text=f"A video chat has started in {group_name}!"
        )

    # For members joining the video chat
    if update.message.video_chat_participant_joined:
        await context.bot.send_message(
            chat_id=update.message.chat_id,
            text=f"{update.message.video_chat_participant_joined} has joined the video chat in {group_name}."
        )

    # For video chat ending
    if update.message.video_chat_ended:
        await context.bot.send_message(
            chat_id=update.message.chat_id,
            text=f"The video chat has ended in {group_name}."
        )

# Main function to run the bot
async def main():
    # Use your own bot token here
    bot_token = '7581811310:AAFV_hoOlzbrctAxaz_0eQtwk9oTttGR9N8'
    
    # Create the Application instance
    application = Application.builder().token(bot_token).build()

    # Handlers for new member and video chat messages
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, new_member))
    application.add_handler(MessageHandler(filters.TEXT, handle_video_chat))  # Update this line

    # Start polling for messages
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
