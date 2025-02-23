import sqlite3

# データベース接続（ファイルがなければ新規作成）
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# テーブル作成
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
''')

# データ挿入
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 30))

# 変更を保存
conn.commit()

# データ取得
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# 結果を表示
for row in rows:
    print(row)

# 接続を閉じる
conn.close()
