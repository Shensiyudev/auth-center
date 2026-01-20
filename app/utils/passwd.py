import logging

from passlib.exc import UnknownHashError
from passlib.context import CryptContext

logger = logging.getLogger('app')


class PasswordManager:

    pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

    @classmethod
    def encrypt(cls, password: str) -> str:
        return cls.pwd_context.hash(password)

    @classmethod
    def verify(cls, plain_password: str, encrypted_password: str) -> bool:
        try:
            status = cls.pwd_context.verify(plain_password, encrypted_password)
            return status
        except UnknownHashError as e:
            logger.error(e)
            return False


if __name__ == '__main__':
    print(PasswordManager.encrypt('123456'))
