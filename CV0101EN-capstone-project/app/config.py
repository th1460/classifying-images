import os
class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    UPLOAD_FOLDER = "image-file"
    CSRF_ENABLED = True
    DEBUG = False
    
    # Enter your API Key and Custom Classifier ID below
    API_KEY = "L6DZhWQtIWBviXbyS8KoGyqpZKm-snN23dWOehx_1wQA"
    CLASSIFIER_ID = "DefaultCustomModel_1328834208"
