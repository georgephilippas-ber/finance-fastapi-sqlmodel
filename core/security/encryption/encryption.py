import bcrypt


def hash_password(cleartext_password: str) -> str:
    hashed = bcrypt.hashpw(cleartext_password.encode('utf-8'), bcrypt.gensalt())

    return hashed.decode('utf-8')


def verify_password(cleartext_password: str, hashed_password: str) -> bool:
    try:
        return bcrypt.checkpw(cleartext_password.encode('utf-8'), hashed_password.encode('utf-8'))
    except Exception as e:
        return False
