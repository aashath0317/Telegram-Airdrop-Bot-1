# --------------------------------------------- #
# Plugin Name           : TelegramAirdropBot    #
# Author Name           : fabston               #
# File Name             : config.py             #
# --------------------------------------------- #

# Enable / disable the airdrop
airdrop_live = True

# Telegram
api_token = (
    "5040431760:AAHkLJcv1meMiaVwG4zR10jpBnF2Q753TPk"  # More: https://core.telegram.org/bots#3-how-do-i-create-a-bot
)

host = "c2ptech-airdrob.herokuapp.com"  # ip/host where the bot is running

log_channel = -1001355597767  # Channel ID. Example: -1001355597767
admins = []  # Telegram User ID's. Admins are able to execute command "/airdroplist"
airdrop_cap = 100  # Max airdrop submissions that are being accepted
wallet_changes = 3  # How often a user is allowed to change their wallet address

# MySQL Database
mysql_host = "ec2-18-206-112-235.compute-1.amazonaws.com"
mysql_db = "d9q7c9dr2ii8jp"
mysql_user = "lipavcgjefwzhr"
mysql_pw = "f2939a013e3d1da4fc49d970136db3c164266f68b330aa501af4a861aeed339e"

texts = {
    "start_1": "Hi {} and welcome to our Airdrop!\n\nGet started by clicking the button below.\n\n",
    "start_2": "Hi {},\n\nYour address has been added to the airdrop list!\n\n",
    "start_captcha": "Hi {},\n\n",
    "airdrop_start": "The airdrop didn't start yet.",
    "airdrop_address": "Type in your address:",
    "airdrop_max_cap": "ℹ️ The airdrop reached its max cap.",
    "airdrop_walletused": "⚠️ That address has already been used. Use a different one.",
    "airdrop_confirmation": "✅ Your address has been added to airdrop list.",
    "airdrop_wallet_update": "✅ Your address has been updated.",
}
