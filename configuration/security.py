PASSWORD_MINIMUM_LENGTH = 4
PASSWORD_MAXIMUM_LENGTH = 128

JSON_WEB_TOKEN_SECRET_KEY: str = 'bb07c2d34569be2cdf090daf5ae58daec3c998265d8685820288d620c3b279d2'
JSON_WEB_TOKEN_EXPIRATION_TIME_MINUTES: int = 60

API_SECURITY_ENABLED: bool = False

# def generate_secret_key():
#     import secrets
#
#     return secrets.token_hex(32)
#

if __name__ == '__main__':
    pass
