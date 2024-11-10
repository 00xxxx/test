import sqlite3

def login(user_input_username, user_input_password):
    # 데이터베이스 연결
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()

    # SQL 쿼리 작성 (취약한 방식)
    query = f"SELECT * FROM users WHERE username = '{user_input_username}' AND password = '{user_input_password}'"
    print(f"Executing query: {query}")

    # 쿼리 실행
    cursor.execute(query)
    result = cursor.fetchone()

    connection.close()

    if result:
        return "로그인 성공!"
    else:
        return "로그인 실패!"

# 예제 사용자 입력 (악의적인 입력)
username = "admin"
password = "' OR '1'='1"

print(login(username, password))