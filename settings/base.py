from starlette.config import Config
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

config = Config('.env')
DATA_DIRECTORY = config('DATA_DIRECTORY')
FAKE_EMAIL = config('FAKE_EMAIL')
FAKE_PASSWORD = config('FAKE_PASSWORD')

