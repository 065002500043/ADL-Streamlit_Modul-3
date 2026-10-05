import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul aplikasi
st.title("Streamlit Simple App")

# Menambahkan navigasi di sidebar
page = st.sidebar.radio("Pilih halaman", ["Dataset", "Visualisasi"])

# Halaman Dataset
if page == "Dataset":
    st.header("Halaman Dataset")

    # Membaca file CSV
    df = pd.read_csv("pddikti_example.csv")

    # Menampilkan dataset
    st.dataframe(df)

# Halaman Visualisasi
elif page == "Visualisasi":
    st.header("Halaman Visualisasi")

    # Membaca file CSV
    data = pd.read_csv("pddikti_example.csv")

    # Filter berdasarkan universitas
    selected_university = st.selectbox(
        "Pilih Universitas",
        data["universitas"].unique()
    )

    filtered_data = data[data["universitas"] == selected_university]

    # Membuat visualisasi
    fig, ax = plt.subplots(figsize=(12, 6))

    for prog_studi in filtered_data["program_studi"].unique():
        subset = filtered_data[
            filtered_data["program_studi"] == prog_studi
        ]

        # Urutkan data berdasarkan id
        subset = subset.sort_values(by="id", ascending=False)

        ax.plot(
            subset["semester"],
            subset["jumlah"],
            label=prog_studi
        )

    ax.set_title(
        f"Visualisasi Data untuk {selected_university}"
    )
    ax.set_xlabel("Semester")
    ax.set_ylabel("Jumlah")
    ax.tick_params(axis="x", rotation=90)
    ax.legend()

    # Menampilkan grafik
    st.pyplot(fig)