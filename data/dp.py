import aiosqlite

DB_NAME = "nickname_bot.db"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS nicknames (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                nickname TEXT
            );
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                is_human BOOLEAN DEFAULT 1,
                gender TEXT DEFAULT NULL
            );
        """)
        await db.commit()

async def add_nickname(user_id: int, nickname: str):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT INTO nicknames (user_id, nickname) VALUES (?, ?)",
            (user_id, nickname)
        )
        await db.commit()

async def get_nicknames(user_id: int):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(
            "SELECT nickname FROM nicknames WHERE user_id = ?",
            (user_id,)
        )
        rows = await cursor.fetchall()
        return [row[0] for row in rows]

async def set_user_human(user_id: int, is_human: bool):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            INSERT INTO users (user_id, is_human)
            VALUES (?, ?)
            ON CONFLICT(user_id) DO UPDATE SET is_human = excluded.is_human
        """, (user_id, is_human))
        await db.commit()
