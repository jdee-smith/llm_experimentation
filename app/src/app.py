import duckdb
import pandas as pd
import streamlit as st
from code_editor import code_editor

import sql

st.set_page_config(page_title="App")


@st.cache_resource
def db_connect():
    if "duck_conn" not in st.session_state:
        st.session_state["duck_conn"] = duckdb.connect("/db/scenarios.db")
    return st.session_state["duck_conn"]


def initialize_db(conn: duckdb.DuckDBPyConnection):
    for schema in ["Historical", "Baseline"]:
        conn.sql(f"CREATE SCHEMA IF NOT EXISTS {schema}")

    df = pd.read_csv("sample_data/sales.csv")
    conn.sql("CREATE TABLE IF NOT EXISTS Historical.RTS AS SELECT * FROM df")


def main():
    conn = db_connect()
    initialize_db(conn)
    create_side_bar(conn)
    create_page(conn)


def create_side_bar(conn: duckdb.DuckDBPyConnection):
    cur = conn.cursor()

    with st.sidebar:
        st.divider()

        table_list = ""
        cur.execute("show all tables")
        recs = cur.fetchall()

        if len(recs) > 0:
            st.markdown("# Database")

        for rec in recs:
            table_name = ".".join([rec[1], rec[2]])
            # table_name = rec[2]
            table_list += f"- {table_name}\n"
            cur.execute(f"describe {table_name}")

            for col in cur.fetchall():
                table_list += f"    - {col[0]} {col[1]}\n"

        st.markdown(table_list)


def create_page(conn: duckdb.DuckDBPyConnection):
    st.title("App :chart_with_upwards_trend:")
    st.divider()

    cur = conn.cursor()
    st.write("Write SQL in the box below.")
    st.write("Hit ctrl+enter to run the SQL.")
    res = code_editor(code=sql.example_sql, lang="sql", key="editor")

    for query in res["text"].split(";"):
        if query.strip() == "":
            continue

        try:
            cur.execute(query)
            df = cur.fetch_df()
            st.write(df)
        except Exception as e:
            st.error(e)

    if st.button("reset database"):
        st.cache_resource.clear()
        st.session_state["editor"]["text"] = ""
        st.rerun()


if __name__ == "__main__":
    main()
