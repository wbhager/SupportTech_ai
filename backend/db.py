import psycopg2

conn = psycopg2.connect(
    dbname = "supporttech_ai",
    user = "willhager",
    host = "localhost",
    port = 5432
)

cursor = conn.cursor()

def save_conversation(conv_id):
    cursor.execute("INSERT INTO conversations (conv_id) VALUES (%s) ON CONFLICT (conv_id) DO NOTHING", (conv_id,))
    conn.commit()

def save_message(conv_id, role, content):
    cursor.execute(
        "SELECT COUNT(*) FROM messages WHERE conv_id = %s",
        (conv_id,)
    )
    message_count = cursor.fetchone()[0]

    cursor.execute(
        "INSERT INTO messages (conv_id, role, content, message_order) VALUES (%s, %s, %s, %s)",
        (conv_id, role, content, message_count + 1)
    )
    conn.commit()

def get_conversation_history(conv_id):
    cursor.execute(
        "SELECT role, content FROM messages WHERE conv_id = %s ORDER BY message_order ASC",
        (conv_id,)
    )

