class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Dc418289!@localhost/advanced_e_commerce_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_TYPE= 'SimpleCache'
    DEBUG = True