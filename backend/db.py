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
        "INSERT INTO messages (conv_id, role, content, message_order) VALUES (%s, %s, %s, %s)",
        (conv_id, role, content, COUNT(message_id))
    )
    conn.commit()

