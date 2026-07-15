import psycopg2

try:
    conn = psycopg2.connect(
        dbname="supporttech_ai",
        user="willhager",
        host="localhost",
        port=5432
    )
    cursor = conn.cursor()
    print("Connected to supporttech_ai database")
except Exception as e:
    print(f"Database connection failed: {e}")
    conn = None
    cursor = None

cursor = conn.cursor()

def save_conversation(conv_id: str):
    cursor.execute("INSERT INTO conversations (conv_id) VALUES (%s) ON CONFLICT (conv_id) DO NOTHING", (conv_id,))
    conn.commit()

def save_message(conv_id: str, role: str, content: str):
    cursor.execute(
        "SELECT COUNT(*) FROM messages WHERE conv_id = %s",
        (conv_id,)
    )
    message_count = cursor.fetchone()[0]

    cursor.execute(
        "INSERT INTO messages (conv_id, role, content, message_order) VALUES (%s, %s, %s, %s) RETURNING message_id",
        (conv_id, role, content, message_count + 1)
    )
    message_id = cursor.fetchone()[0]
    conn.commit()
    return message_id

def get_conversation_history(conv_id: str):
    cursor.execute(
        "SELECT role, content FROM messages WHERE conv_id = %s ORDER BY message_order ASC",
        (conv_id,)
    )
    return cursor.fetchall()

def save_evaluation(conv_id: str, message_id: int, score: int, feedback: str, user_message: str, qwen_response: str):
    cursor.execute(
        "INSERT INTO evaluations (conv_id, message_id, score, feedback) VALUES (%s, %s, %s, %s, %s, %s)",
        (conv_id, message_id, score, feedback, user_message, qwen_response)
    )
    conn.commit()

def save_title(conv_id: str, title: str):
    cursor.execute(
        "UPDATE conversations SET title = %s WHERE conv_id = %s",
        (title, conv_id)
    )
    conn.commit()

def fetch_sidebar_conv_names():
    cursor.execute("SELECT conv_id, title FROM conversations ORDER BY created_at DESC")
    return cursor.fetchall()

def delete_conversation(conv_id: str):
    cursor.execute("DELETE FROM conversations WHERE conv_id = %s", (conv_id,))
    conn.commit()