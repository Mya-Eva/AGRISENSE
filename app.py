import streamlit as st
from utils.theme import apply_theme

st.set_page_config(page_title="AgroStat Pro — Accueil", page_icon="🌿", layout="wide")
apply_theme("home")

# ── Hero ───────────────────────────────────────────────────────────────────
st.markdown('<p class="agri-section-label">Plateforme agricole</p>', unsafe_allow_html=True)
st.title("Transformez vos données agricoles en actions stratégiques")
st.markdown(
    '<p style="color:#8b949e;font-size:1.05rem;max-width:640px;line-height:1.7;">'
    "Centralisez vos saisies de récolte, suivez les performances et obtenez "
    "des insights instantanés grâce à un tableau de bord conçu pour l'agriculture moderne."
    "</p>",
    unsafe_allow_html=True,
)

st.divider()

# ── Main columns ───────────────────────────────────────────────────────────
hero_col, image_col = st.columns([3, 2], gap="large")

with hero_col:
    st.markdown("### Une plateforme complète pour la production agricole moderne")
    st.markdown(
        '<p style="color:#8b949e;line-height:1.7;">'
        "AgroStat Pro vous accompagne depuis la collecte terrain jusqu'à l'analyse "
        "des résultats grâce à une interface simple et professionnelle."
        "</p>",
        unsafe_allow_html=True,
    )

    card1, card2 = st.columns(2, gap="medium")
    with card1:
        st.markdown(
            '<div class="agri-card">'
            '<p class="agri-card-title">Collecte de données</p>'
            '<p class="agri-card-body">Enregistrez facilement toutes vos observations de récolte et intrants.</p>'
            "</div>",
            unsafe_allow_html=True,
        )
    with card2:
        st.markdown(
            '<div class="agri-card">'
            '<p class="agri-card-title">Analyse des performances</p>'
            '<p class="agri-card-body">Obtenez des graphiques clairs et des KPI utiles pour piloter vos cultures.</p>'
            "</div>",
            unsafe_allow_html=True,
        )

with image_col:
    st.image(
        "https://www.shutterstock.com/image-photo/chocolate-cacao-tree-farm-green-600nw-2256239597.jpg",
        caption="Agriculture connectée et analytique",
        use_container_width=True,
    )

st.divider()

# ── CTA ────────────────────────────────────────────────────────────────────
st.markdown("### Commencez ici")
cta_col1, cta_col2 = st.columns(2, gap="large")

with cta_col1:
    st.markdown("#### Enregistrement des données")
    st.markdown(
        '<p style="color:#8b949e;line-height:1.7;">'
        "Saisissez toutes vos données de récolte et intrants pour structurer votre suivi agricole."
        "</p>",
        unsafe_allow_html=True,
    )
    if st.button("Aller vers la Collecte", key="cta_collecte"):
        st.switch_page("pages/1_Collecte.py")

with cta_col2:
    st.markdown("#### Visualisation et analyse")
    st.markdown(
        '<p style="color:#8b949e;line-height:1.7;">'
        "Consultez les résultats récapitulatifs et les tendances par culture."
        "</p>",
        unsafe_allow_html=True,
    )
    if st.button("Aller vers l'Analyse", key="cta_analyse"):
        st.switch_page("pages/2_Analyse.py")

st.divider()

# ── Features ───────────────────────────────────────────────────────────────
st.markdown("### Pourquoi AgroStat Pro ?")
f1, f2, f3 = st.columns(3, gap="medium")

with f1:
    st.markdown(
        '<div class="agri-card">'
        '<p class="agri-card-title">Simplicité</p>'
        '<p class="agri-card-body">Une interface claire pour des actions rapides, sans courbe d\'apprentissage.</p>'
        "</div>",
        unsafe_allow_html=True,
    )
with f2:
    st.markdown(
        '<div class="agri-card">'
        '<p class="agri-card-title">Fiabilité</p>'
        '<p class="agri-card-body">Vos données sont enregistrées localement et réutilisables immédiatement.</p>'
        "</div>",
        unsafe_allow_html=True,
    )
with f3:
    st.markdown(
        '<div class="agri-card">'
        '<p class="agri-card-title">Vision stratégique</p>'
        '<p class="agri-card-body">Des indicateurs utiles pour comprendre et améliorer vos résultats agricoles.</p>'
        "</div>",
        unsafe_allow_html=True,
    )

st.divider()

st.markdown("#### Besoin d'aide ?")
st.markdown(
    '<p style="color:#8b949e;">Utilisez la navigation en haut de page pour accéder aux sections Collecte et Analyse.</p>',
    unsafe_allow_html=True,
)
