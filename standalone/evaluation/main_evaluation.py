from database.database import Database
from manager.user.user_manager import UserManager

if __name__ == '__main__':
    db = Database()

    with db.create_session() as session:
        user_manager = UserManager(session)

        print(user_manager.verify_and_retrieve("root", "root!1A"))
