import streamlit as st

st.set_page_config(page_title="AgroStat Pro - Accueil", page_icon="🌾", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f4f7fb; }
    .stApp { color-scheme: light; }
    .card {
        border: 1px solid #e2e8f0;
        border-radius: 18px;
        padding: 2rem;
        background: yellow;
        box-shadow: 0 10px 30px rgba(15, 23, 42, 0.08);
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3.2em;
        background-color: #1b5e20;
        color: yellow;
        font-weight: 700;
        border: none;
        transition: 0.2s ease;
    }
    .stButton>button:hover {
        background-color: yellow;
    }
    .big-title {
        font-size: 2.9rem;
        line-height: 1.05;
        color: Green;
    }
    .feature-box {
        border: 1px solid #d1d5db;
        border-radius: 16px;
        padding: 1.5rem;
        background: grey;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌿 AgroStat Pro")
st.markdown('<div class="big-title">Transformez vos données agricoles en actions stratégiques.</div>', unsafe_allow_html=True)
st.write("Bienvenue sur votre tableau de bord agricole. Centralisez les saisies de récolte, suivez les performances et obtenez des insights instantanés.")

st.divider()

hero_col, image_col = st.columns([3, 2])

with hero_col:
    st.markdown("### Une plateforme complète pour la production agricole moderne")
    st.write("AgroStat Pro vous accompagne depuis la collecte terrain jusqu'à l'analyse des résultats grâce à une interface simple et professionnelle.")
    st.write("**Fonctionnalités clés :**")
    st.markdown("- Saisie rapide des données de récolte, engrais et eau\n- Visualisations dynamiques des rendements\n- Stockage local sécurisé via SQLite")

    card1, card2 = st.columns(2)
    with card1:
        st.markdown('<div class="feature-box">\n📝 Collecte de données\n<br>Enregistrez facilement toutes vos observations de récolte et intrants.\n</div>', unsafe_allow_html=True)
    with card2:
        st.markdown('<div class="feature-box">\n📊 Analyse des performances\n<br>Obtenez des graphiques clairs et des KPI utiles pour piloter vos cultures.\n</div>', unsafe_allow_html=True)

with image_col:
    st.image("https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&q=80&w=800", caption="Agriculture connectée et analytique")

st.markdown("---")

st.markdown("### 🚀 Commencez ici")
cta_col1, cta_col2 = st.columns(2)

with cta_col1:
    st.markdown("#### 📝 Enregistrement des informations")
    st.write("Saisissez toutes vos données de récolte et intrants pour structurer votre suivi agricole.")
    if st.button("Utiliser le menu a gauche pour naviguer <<", key="collecte_cta"):
        st.switch_page("1_Collecte")

with cta_col2:
    st.markdown("#### 📊 Visualisation et analyse")
    st.write("Consultez les résultats récapitulatifs et les tendances par culture.")
       

st.markdown("---")

st.markdown("### Pourquoi AgroStat Pro ?")
feature1, feature2, feature3 = st.columns(3)
feature1.markdown("**✅ Simplicité**\nUne interface claire pour des actions rapides.")
feature2.markdown("**✅ Fiabilité**\nVos données sont enregistrées localement et réutilisables immédiatement.")
feature3.markdown("**✅ Vision stratégique**\nDes indicateurs utiles pour comprendre vos résultats agricoles.")

st.markdown("---")

st.markdown("#### Besoin d'aide ?")
st.write("Utilisez les boutons ci-dessous pour accéder aux sections Collecte et Analyse.")