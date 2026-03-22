from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    # ensure bcrypt limit
    safe_password = password.encode("utf-8")[:72]
    return pwd_context.hash(safe_password)


def verify_password(plain_password: str, hashed_password: str):
    safe_password = plain_password.encode("utf-8")[:72]
    return pwd_context.verify(safe_password, hashed_password)