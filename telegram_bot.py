import requests

def send_to_user(message, bot_token, admin_id): 
    # message = "hello from your telegram bot"
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={admin_id}&text={message}"
    requests.get(url) # this sends the message
