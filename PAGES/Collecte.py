import streamlit as st
import sqlite3
from datetime import datetime

st.set_page_config(page_title="Collecte - AgroStat Pro", page_icon="📝", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f4f7ff; }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #1b5e21;
        color: red;
        font-weight: 700;
        border: none;
        transition: 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #2e7d32;
    }
    .form-section {
        border: 1px solid #e2f0e9;
        border-radius: 16px;
        padding: 2rem;
        background: grey;
        box-shadow: 0 10px 30px rgba(15, 23, 42, 0.08);
    }
    .info-box {
        background: red;
        border-left: 5px solid #1b5e20;
        padding: 1.5rem;
        border-radius: 8px;
        margin-bottom: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📝 Collecte de Données")
st.markdown("Enregistrez vos informations de récolte, intrants et consommation d'eau pour chaque parcelle.")

st.markdown("""
<div class="info-box">
💡 <strong>Conseil :</strong> Plus vos données sont détaillées et régulièrement saisies, meilleures seront vos analyses!
</div>
""", unsafe_allow_html=True)

# --- Base de données ---
def save_data(date, culture, rendement, engrais, eau):
    with sqlite3.connect('agri_data.db') as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS production 
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, culture TEXT, rendement REAL, engrais REAL, eau REAL)''')
        c.execute("INSERT INTO production (date, culture, rendement, engrais, eau) VALUES (?,?,?,?,?)",
                  (date, culture, rendement, engrais, eau))
        conn.commit()

st.markdown('<div class="form-section">', unsafe_allow_html=True)

with st.form("data_form", clear_on_submit=True):
    st.markdown("### Formulaire de Saisie")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Informations générales**")
        date_input = st.date_input("📅 Date de récolte", value=datetime.today())
        culture_input = st.selectbox("🌾 Type de Culture", ["Maïs", "Riz", "Blé", "Cacao", "Café"])
    
    with col2:
        st.markdown("**Rendement et intrants**")
        rendement_input = st.number_input("📊 Rendement (kg/ha)", min_value=0.0, step=0.1)
        engrais_input = st.number_input("🧪 Quantité Engrais (kg)", min_value=0.0, step=0.1)
    
    st.markdown("**Gestion de l'eau**")
    eau_input = st.number_input("💧 Consommation Eau (m³)", min_value=0.0, step=0.1)
    
    st.divider()
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        submit = st.form_submit_button("✅ Sauvegarder les données", use_container_width=True)
    with col_btn2:
        st.form_submit_button("🔄 Réinitialiser", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

if submit:
    save_data(str(date_input), culture_input, rendement_input, engrais_input, eau_input)
    st.success("✨ Données enregistrées avec succès ! Vous pouvez consulter vos résultats dans l'onglet Analyse.")
    st.balloons()

# --- Aide ---
st.divider()
with st.expander("❓ Besoin d'aide avec ce formulaire?"):
    st.markdown("""
    **Champs expliqués :**
    - **Date de récolte** : La date exacte où vous avez récolté
    - **Type de Culture** : Sélectionnez parmi les 5 cultures disponibles
    - **Rendement** : La quantité récolée par hectare
    - **Quantité Engrais** : L'engrais utilisé en kg pour cette récolte
    - **Consommation Eau** : Le volume d'eau utilisé en mètres cubes
    """)
