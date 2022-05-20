import os


class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://grace:simakush@localhost/simablog'

    SQLALCHEMY_DATABASE_URI = 'postgres://knlzjntoipebhz:df79385a36c28d2b94247f41c7925dd7e1779d8c5a7c0c3d8cadd74315f31888@ec2-3-231-82-226.compute-1.amazonaws.com:5432/dd49uubfm86359'

    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
     uri = os.getenv("DATABASE_URL")  
     if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)

        
     SQLALCHEMY_DATABASE_URI=uri

  

class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
