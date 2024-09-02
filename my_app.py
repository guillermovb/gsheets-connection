import streamlit as st

st.subheader("📗 Google Sheets st.connection using Public URLs")

st.write("#### 1. Read public Google Worksheet as Pandas")

with st.echo():
    import streamlit as st

    from streamlit_gsheets import GSheetsConnection

    # Create a connection object.
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read()
    
    st.dataframe(df)
