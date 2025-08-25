import streamlit as st
import pymysql

db_config = st.secrets["mysql"]

try:
    conn = pymysql.connect(
        host=db_config["mysql_host"],
        port=int(db_config["mysql_port"]),
        user=db_config["mysql_user"],
        password=db_config["mysql_password"],
        db=db_config["mysql_db"]
    )
    st.success("資料庫連線成功！")
except Exception as e:
    st.error(f"資料庫連線失敗：{e}")
    st.stop()

table_name = "user"  # <--- 這裡要換成你真的有的 table

try:
    with conn.cursor() as cursor:
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        st.write("資料庫內容")
        st.dataframe(rows)
except Exception as e:
    st.error(f"查詢失敗：{e}")