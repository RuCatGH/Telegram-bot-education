import sqlite3
import os

# Определение текущего рабочего каталога
current_dir = os.getcwd()

# Получение абсолютного пути к базе данных
database_path = os.path.join(current_dir, "database.db")
conn = sqlite3.connect(database_path)
# Создание курсора
cursor = conn.cursor()


def check_or_update_category(user_id: int, category_user: str) -> bool:
    # Выполняем запрос на выборку данных для пользователя с указанным ID
    cursor.execute("SELECT user_id, category FROM users WHERE user_id=?", (user_id,))
    result = cursor.fetchone()
    if result is not None and len(result) >= 2:
        existing_category = result[1]
        # Обновление категории, если не совпадает с выбранной
        if existing_category != category_user:
            cursor.execute("UPDATE users SET category=? WHERE user_id=?", (category_user, user_id))
            conn.commit()
        return True
    # Добавляем пользователя, если нет в бд
    else:
        cursor.execute("INSERT INTO users (user_id, category) VALUES (?, ?)", (user_id, category_user))
        conn.commit()
        return False


# Получение id и category
def get_all_id_and_categories() -> list[(int, str)]:
    cursor.execute("SELECT user_id, category FROM users")
    results = cursor.fetchall()
    return results
