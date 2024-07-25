from starlette.config import Config



config = Config('.env')
DATA_DIRECTORY = config('DATA_DIRECTORY')
SECRET_KEY = config('SECRET_KEY')

