import os

class Config:
    SQLACHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'mysql+pymysql://username:password@localhost:3306/nome_do_banco'
    )