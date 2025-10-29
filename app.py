import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Kaggle Data Explorer (Titanic)")

uploaded_file = st.file_uploader("Загрузите CSV-файл", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📊 Предпросмотр данных")
    st.dataframe(df.head())

    numeric_cols = df.select_dtypes('number').columns
    col = st.selectbox("Выберите числовой столбец:", numeric_cols)

    st.write("📈 Основные статистики:")
    st.write(df[col].describe())

    fig, ax = plt.subplots()
    sns.histplot(df[col], bins=20, kde=True, ax=ax)
    st.pyplot(fig)

    min_val, max_val = st.slider(
        "Фильтр по диапазону",
        float(df[col].min()),
        float(df[col].max()),
        (float(df[col].min()), float(df[col].max()))
    )

    filtered = df[(df[col] >= min_val) & (df[col] <= max_val)]
    st.write(f"🧾 Отфильтровано {len(filtered)} строк")
    st.dataframe(filtered)
