import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Kisi-Kisi Generator", layout="wide")

st.title("📚 Kisi-Kisi Indikator Generator")
st.write("Paste soal dan level kognitif (C1, C2, C3...) sesuai urutan.")

soal_input = st.text_area("📥 Paste Soal (satu soal per baris)", height=200)
level_input = st.text_area("📊 Paste Level Kognitif (satu level per baris)", height=150)

if st.button("🚀 Generate Indikator"):

    soal_list = [s.strip() for s in soal_input.split("\n") if s.strip()]
    level_list = [l.strip() for l in level_input.split("\n") if l.strip()]

    if len(soal_list) != len(level_list):
        st.error("⚠ Jumlah soal dan level tidak sama!")
    else:
        indikator = []

        for i, level in enumerate(level_list):
            if level.upper() == "C1":
                teks = f"Siswa mampu menyebutkan informasi pada soal nomor {i+1}."
            elif level.upper() == "C2":
                teks = f"Siswa mampu menjelaskan konsep pada soal nomor {i+1}."
            elif level.upper() == "C3":
                teks = f"Siswa mampu menerapkan konsep pada soal nomor {i+1}."
            else:
                teks = f"Siswa mampu menyesuaikan indikator pada soal nomor {i+1}."

            indikator.append(teks)

        df = pd.DataFrame({
            "No": range(1, len(indikator)+1),
            "Level": level_list,
            "Indikator": indikator
        })

        st.success("✅ Indikator berhasil dibuat!")
        st.dataframe(df)

        output = BytesIO()
        df.to_excel(output, index=False, engine='openpyxl')
        output.seek(0)

        st.download_button(
            label="⬇ Download Excel",
            data=output,
            file_name="kisi_kisi_indikator.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
