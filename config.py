import os

class Config(object):
    BOT_TOKEN = os.environ.get("8753755010:AAHjR-nD3AUXKOPzsBxO82eRud7pfzK0jt8")
    API_ID = int(os.environ.get("28854523"))
    API_HASH = os.environ.get("3ec8779aa2109cfa00fd6146146a065c")
    AUTH_USER = os.environ.get('1018181607', '8753755010').split('1018181607')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "Sujeet™"#Here You Can Change with Your Name  or any custom name or title you prefer
