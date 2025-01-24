from sqlite3 import Connection, connect, IntegrityError
from typing import Optional

from configuration.database import SESSION_DATABASE_FILENAME


class SessionManager:
    _sqlite_filename: str

    def __init__(self, sqlite_filename: str = SESSION_DATABASE_FILENAME):
        self._sqlite_filename = sqlite_filename

        with self.get_connection() as _connection:
            _connection.execute("""
            CREATE TABLE IF NOT EXISTS session (
                session_id TEXT NOT NULL,
                entry_key TEXT NOT NULL,
                value TEXT,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                session_closed BOOLEAN DEFAULT FALSE,
                PRIMARY KEY (session_id, entry_key)
            );
            """)

    def get_connection(self) -> Connection:
        return connect(self._sqlite_filename)

    def close_session(self, session_id: str) -> bool:
        with self.get_connection() as _connection:
            try:
                _connection.execute("""
                    UPDATE session SET session_closed = TRUE WHERE session_id = ?;
                """, (session_id,))

                return True
            except IntegrityError:
                return False

    def add(self, session_id: str, entry_key: str, value: str) -> bool:
        with self.get_connection() as _connection:
            try:
                _connection.execute("""
                    INSERT INTO session (session_id, entry_key, value)
                    VALUES (?, ?, ?)
                    ON CONFLICT(session_id, entry_key)
                    DO UPDATE SET value = excluded.value;
                """, (session_id, entry_key, value))

                return True
            except IntegrityError:
                return False

    def get(self, session_id: str, entry_key: str) -> Optional[str]:
        with self.get_connection() as _connection:
            try:
                cursor_ = _connection.execute("""
                    SELECT value FROM session WHERE session_id = ? AND entry_key = ?;
                """, (session_id, entry_key))

                query_result_ = cursor_.fetchone()

                return query_result_[0]
            except (IntegrityError, TypeError, IndexError) as e:
                return None


if __name__ == '__main__':
    session_manager = SessionManager()
    session_manager.add("george", "state", "one and a half")

    print(session_manager.get("george", "state"))
