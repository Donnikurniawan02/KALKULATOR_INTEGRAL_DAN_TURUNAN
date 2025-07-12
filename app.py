import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Simbol x global
x = sp.Symbol('x')

st.set_page_config(page_title="Kalkulator KalkulusX", layout="centered")

st.title("🧮 Kalkulator Integral & Turunan (KalkulusX)")
st.markdown("Masukkan fungsi aljabar satu variabel (misal: x**2 + 3*x).")

# Input fungsi
fungsi_input = st.text_input("Fungsi f(x) =", "x**2 + 3*x")

# Coba parsing fungsi
try:
    fungsi = sp.sympify(fungsi_input)
except (sp.SympifyError, TypeError):
    st.error("❌ Fungsi tidak valid. Periksa penulisannya.")
    st.stop()

# Pilihan operasi
operasi = st.radio("Pilih Operasi:", ["Turunan", "Integral"])

# Proses operasi simbolik
if operasi == "Turunan":
    hasil = sp.diff(fungsi, x)
    st.latex(f"f'(x) = {sp.latex(hasil)}")
else:
    hasil = sp.integrate(fungsi, x)
    st.latex(f"\\int f(x)\\,dx = {sp.latex(hasil)} + C")

# Evaluasi pada titik tertentu
st.subheader("📍 Evaluasi Numerik")
titik = st.number_input("Masukkan nilai x =", value=1.0)
evaluasi = hasil.subs(x, titik)
st.write(f"Hasil evaluasi pada x = {titik} adalah *{evaluasi}*")

# Visualisasi grafik
st.subheader("📈 Grafik Fungsi dan Hasil Operasi")
x_vals = np.linspace(-10, 10, 400)

# Konversi fungsi ke bentuk numerik
f_lambd = sp.lambdify(x, fungsi, modules=["numpy"])
h_lambd = sp.lambdify(x, hasil, modules=["numpy"])

# Plot
try:
    y_f = f_lambd(x_vals)
    y_h = h_lambd(x_vals)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x_vals, y_f, label='f(x)', color='blue')
    ax.plot(x_vals, y_h, label='Hasil Operasi', color='red')
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)
except Exception as e:
    st.error("❌ Tidak dapat menampilkan grafik untuk fungsi ini.")

st.markdown("---")
st.caption("🧑‍💻 Dibuat dengan Streamlit + SymPy + Matplotlib | @2025")
