from apscheduler.schedulers.background import BackgroundScheduler
from .twilio_client import send_whatsapp_message
from .utils import get_random_prompt,all_users

scheduler = BackgroundScheduler()

def sechdule_daily_checks():
    for user in all_users():
        message = get_random_prompt()
        send_whatsapp_message(user, message)


scheduler.add_job(sechdule_daily_checks,'cron',hour=10) #every day at 10 am 
scheduler.start()

