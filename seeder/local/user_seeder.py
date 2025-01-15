from configuration.seed import USERS
from manager.user.user_manager import UserManager


class UserSeeder:
    _user_manager: UserManager

    def __init__(self, user_manager: UserManager):
        self._user_manager = user_manager

    def seed(self):
        print('SEEDING - User', end='')
        for user_ in USERS:
            self._user_manager.persist(user_)
        print(' - Done')
