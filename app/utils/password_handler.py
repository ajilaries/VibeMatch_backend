from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    safe_password = password[:72]   # bcrypt limit
    return pwd_context.hash(safe_password)

def verify_password(password: str, hashed: str):
    return pwd_context.verify(password[:72], hashed)