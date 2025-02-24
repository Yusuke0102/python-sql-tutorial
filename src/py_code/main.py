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

user_input_name = "Alice'); DROP TABLE users; --"
sql = f"INSERT INTO users (name) VALUES ('{user_input_name}')"

try:
    # データ挿入（通常の安全な方法）
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 30))

    # SQLインジェクションの試行
    cursor.executescript(sql)  # `DROP TABLE users;` が実行される可能性あり

    # 変更を保存
    conn.commit()

    # テーブルが削除されたかどうかを確認
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    # 結果を表示
    for row in rows:
        print(row)

except sqlite3.OperationalError as e:
    # エラーが発生した場合、SQLインジェクションが成功した可能性がある
    if "no such table: users" in str(e):  
        print("🚨 SQLインジェクションが成功しました！`users` テーブルが削除されました！ 🚨")
    else:
        print("❌ 予期しないエラーが発生しました:", e)

# 接続を閉じる
conn.close()
