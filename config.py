import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6157850456:AAECSQKBOrjcmF_mI9ngnltvsHqjV7TBOEk")

    APP_ID = int(os.environ.get("APP_ID", 22894281))

    API_HASH = os.environ.get("API_HASH", "b59176de6ec96903b816d72c2ad4fff8")

    AUDIO_THUMBNAIL = os.environ.get("AUDIO_THUMBNAIL", "https://telegra.ph//file/6f7d35131f69951c74ee5.jpg")

    VIDEO_THUMBNAIL = os.environ.get("VIDEO_THUMBNAIL", "https://telegra.ph//file/6f7d35131f69951c74ee5.jpg")
    
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "adult_updates")
