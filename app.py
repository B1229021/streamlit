import streamlit as st
import pymysql

# 讀取 secrets
db_config = st.secrets["mysql"]

# 建立連線
conn = pymysql.connect(
    host=db_config["mysql_host"],
    port=int(db_config["mysql_port"]),
    user=db_config["mysql_user"],
    password=db_config["mysql_password"],
    db=db_config["mysql_db"]
)

# 撈資料
with conn.cursor() as cursor:
    cursor.execute("SELECT * FROM your_table_name")  # 替換成你要查的 table
    rows = cursor.fetchall()

# 顯示在網頁
st.write("資料庫內容")
st.dataframe(rows)