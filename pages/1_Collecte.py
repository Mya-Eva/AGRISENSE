import streamlit as st
import sqlite3
from datetime import datetime
import sys
import os

# Add parent directory to path to import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.theme import apply_theme

st.set_page_config(page_title="Collecte — AgroStat Pro", page_icon="📝", layout="wide")
apply_theme("collecte")

st.title("Collecte de Données")
st.markdown(
    '<p style="color:#8b949e;line-height:1.7;max-width:640px;">'
    "Enregistrez vos informations de récolte, intrants et consommation d'eau pour chaque parcelle."
    "</p>",
    unsafe_allow_html=True
)

st.markdown("""
<div class="agri-banner">
<strong>Conseil :</strong> Plus vos données sont détaillées et régulièrement saisies, meilleures seront vos analyses.
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

with st.form("data_form", clear_on_submit=True):
    st.markdown('<p class="agri-section-label">Formulaire de Saisie</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("**Informations générales**")
        date_input = st.date_input("Date de récolte", value=datetime.today())
        culture_input = st.selectbox("Type de Culture", ["Maïs", "Riz", "Blé", "Cacao", "Café"])
    
    with col2:
        st.markdown("**Rendement et intrants**")
        rendement_input = st.number_input("Rendement (kg/ha)", min_value=0.0, step=0.1)
        engrais_input = st.number_input("Quantité Engrais (kg)", min_value=0.0, step=0.1)
    
    st.markdown("**Gestion de l'eau**")
    eau_input = st.number_input("Consommation Eau (m³)", min_value=0.0, step=0.1)
    
    st.divider()
    
    col_btn1, col_btn2 = st.columns(2, gap="medium")
    with col_btn1:
        submit = st.form_submit_button("Sauvegarder les données", use_container_width=True)
    with col_btn2:
        st.form_submit_button("Réinitialiser", use_container_width=True)

if submit:
    save_data(str(date_input), culture_input, rendement_input, engrais_input, eau_input)
    st.success("Données enregistrées avec succès ! Vous pouvez consulter vos résultats dans l'onglet Analyse.")
    st.balloons()

# --- Aide ---
st.divider()
with st.expander("Besoin d'aide avec ce formulaire ?"):
    st.markdown("""
    **Champs expliqués :**
    - **Date de récolte** : La date exacte où vous avez récolté.
    - **Type de Culture** : Sélectionnez parmi les 5 cultures disponibles.
    - **Rendement** : La quantité récoltée par hectare.
    - **Quantité Engrais** : L'engrais utilisé en kg pour cette récolte.
    - **Consommation Eau** : Le volume d'eau utilisé en mètres cubes.
    """)
