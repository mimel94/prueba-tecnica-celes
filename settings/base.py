from starlette.config import Config


config = Config('.env')
DATA_DIRECTORY = config('DATA_DIRECTORY', default='')
SECRET_KEY = config('SECRET_KEY', default='')
