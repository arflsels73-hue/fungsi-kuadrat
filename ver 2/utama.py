import streamlit as st
import math

# Pengaturan dasar halaman agar lebih lebar
st.set_page_config(
    page_title="Fungsi Kuadrat",
    page_icon="✨",
    layout="wide"
)

# --- FUNGSI BANTUAN UNTUK FORMAT RUMUS ---
def format_persamaan(a, b, c):
    """Fungsi untuk membuat rumus matematika terlihat rapi"""
    term_a = f"{a:g}x^2" if a not in [1, -1] else ("x^2" if a == 1 else "-x^2")

    term_b = ""
    if b > 0: term_b = f" + {b:g}x" if b != 1 else " + x"
    elif b < 0: term_b = f" - {abs(b):g}x" if b != -1 else " - x"

    term_c = ""
    if c > 0: term_c = f" + {c:g}"
    elif c < 0: term_c = f" - {abs(c):g}"

    return f"f(x) = {term_a}{term_b}{term_c}"

# --- SIDEBAR (MENU SAMPING) ---
with st.sidebar:
    st.header("⚙️ Pengaturan Nilai")
    st.markdown("Geser atau ketik koefisien fungsi kuadrat:")

    a = st.number_input("Nilai a (x²)", value=1.0, step=1.0, format="%.1f")
    b = st.number_input("Nilai b (x)", value=-2.0, step=1.0, format="%.1f")
    c = st.number_input("Nilai c (konstanta)", value=-3.0, step=1.0, format="%.1f")

    st.divider()
    st.caption("Dibuat untuk Tugas Sekolah 🎓")

if a == 0:
    st.error("⚠️ Nilai 'a' tidak boleh 0. Jika 0, maka ini bukan persamaan kuadrat, melainkan garis lurus.")
    st.stop()

# --- PERHITUNGAN MATEMATIKA ---
D = (b**2) - (4 * a * c)
xp = -b / (2 * a)
yp = -D / (4 * a)

# Menentukan akar-akar
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    akar_text = f"X₁= {x1:.2f} | X₂= {x2:.2f}"
    jenis_akar = "2 Titik Potong (Akar Berbeda)"
elif D == 0:
    x1 = -b / (2 * a)
    akar_text = f"X = {x1:.2f}"
    jenis_akar = "1 Titik Potong (Akar Kembar)"
else:
    akar_text = "Tidak Ada"
    jenis_akar = "Imajiner (Tidak memotong Sumbu X)"

# Arah kurva
arah_kurva = "Ke Atas 📈" if a > 0 else "Ke Bawah 📉"
sifat_puncak = "Titik Minimum" if a > 0 else "Titik Maksimum"

# --- TAMPILAN UTAMA ---
st.title("✨ Kalkulator Fungsi Kuadrat")
st.markdown("Menganalisis properti dan grafik dari fungsi kuadrat secara instan.")

# Menampilkan Rumus Dinamis yang rapi di tengah
rumus = format_persamaan(a, b, c)
st.latex(rumus)

# Membuat Tab
tab1, tab2 = st.tabs(["📊 Visualisasi Grafik", "📝 Analisis Detail"])

with tab1:
    st.markdown("### Kurva Fungsi")

    # Membuat titik koordinat untuk grafik
    data_x, data_y = [], []
    for i in range(-150, 151):
        x = xp + (i * 0.1)
        y = (a * x**2) + (b * x) + c
        data_x.append(x)
        data_y.append(y)

    chart_data = {"Sumbu X": data_x, "Kurva f(x)": data_y}
    st.line_chart(chart_data, x="Sumbu X", y="Kurva f(x)", color="#8b5cf6") # Warna ungu modern

with tab2:
    st.markdown("### Karakteristik Grafik")

    # Baris Pertama Metrik
    col1, col2, col3 = st.columns(3)
    col1.metric("Arah Terbuka", arah_kurva)
    col2.metric("Titik Potong Sumbu Y", f"(0, {c:g})")
    col3.metric("Diskriminan (D)", f"{D:g}", delta=jenis_akar, delta_color="off")

    st.divider()

    # Baris Kedua Metrik (Titik Puncak)
    st.markdown(f"### {sifat_puncak} (Puncak Parabola)")
    col4, col5, col6 = st.columns(3)
    col4.metric("Sumbu Simetri (Xp)", f"{xp:.2f}")
    col5.metric("Nilai Optimum (Yp)", f"{yp:.2f}")
    col6.metric("Koordinat Puncak", f"({xp:.2f}, {yp:.2f})")

    # Kotak Informasi Akar
    if D >= 0:
        st.success(f"**Akar-akar (Titik potong Sumbu X):** {akar_text}")
    else:
        st.warning("**Akar-akar:** Grafik mengambang dan tidak menyentuh Sumbu X (Akar Imajiner).")
        
