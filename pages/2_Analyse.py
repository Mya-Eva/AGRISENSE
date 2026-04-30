import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import plotly.graph_objects as go
import sys
import os

# Add parent directory to path to import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.theme import apply_theme, plotly_dark_layout

st.set_page_config(page_title="Analyse — AgroStat Pro", page_icon="📊", layout="wide")
apply_theme("analyse")

st.title("Analyse des Données")
st.markdown(
    '<p style="color:#8b949e;line-height:1.7;max-width:640px;">'
    "Visualisez vos rendements, consommations et performances agricoles en temps réel."
    "</p>",
    unsafe_allow_html=True
)

def load_data():
    with sqlite3.connect('agri_data.db') as conn:
        try:
            return pd.read_sql_query("SELECT * FROM production", conn)
        except:
            return pd.DataFrame()

df = load_data()

if not df.empty:
    # --- KPIs et Résumés ---
    st.markdown('<p class="agri-section-label" style="margin-top:2rem;">Indicateurs Clés</p>', unsafe_allow_html=True)
    
    kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4, gap="small")
    
    with kpi_col1:
        st.metric("Nombre de récoltes", len(df), delta=None)
    
    with kpi_col2:
        avg_rendement = df['rendement'].mean()
        st.metric("Rendement moyen (kg/ha)", f"{avg_rendement:.1f}")
    
    with kpi_col3:
        avg_engrais = df['engrais'].mean()
        st.metric("Engrais moyen (kg)", f"{avg_engrais:.1f}")
    
    with kpi_col4:
        avg_eau = df['eau'].mean()
        st.metric("Eau moyenne (m³)", f"{avg_eau:.1f}")
    
    st.divider()
    
    # --- Filtres ---
    st.markdown("### Filtres")
    filter_col1, filter_col2 = st.columns(2, gap="large")
    
    with filter_col1:
        cultures_disponibles = df['culture'].unique().tolist()
        culture_filtre = st.multiselect("Filtrer par culture", cultures_disponibles, default=cultures_disponibles)
        df_filtered = df[df['culture'].isin(culture_filtre)]
    
    with filter_col2:
        st.write("")  # Espace vide pour alignement
        st.write("")
        if st.button("Réinitialiser les filtres"):
            st.rerun()
    
    st.divider()
    
    # --- Visualisations ---
    st.markdown('<p class="agri-section-label">Visualisations</p>', unsafe_allow_html=True)
    
    viz_col1, viz_col2 = st.columns(2, gap="large")
    
    # Graphique 1: Rendement par culture
    with viz_col1:
        if not df_filtered.empty:
            rendement_par_culture = df_filtered.groupby('culture')['rendement'].mean().reset_index()
            fig1 = px.bar(rendement_par_culture, x='culture', y='rendement',
                         title="Rendement moyen par culture (kg/ha)",
                         labels={'culture': 'Culture', 'rendement': 'Rendement (kg/ha)'},
                         color='rendement', color_continuous_scale='Greens')
            fig1.update_layout(plotly_dark_layout(showlegend=False, height=400))
            st.plotly_chart(fig1, use_container_width=True)
    
    # Graphique 2: Distribution des cultures
    with viz_col2:
        if not df_filtered.empty:
            culture_count = df_filtered['culture'].value_counts().reset_index()
            culture_count.columns = ['culture', 'count']
            fig2 = px.pie(culture_count, names='culture', values='count',
                         title="Distribution des récoltes par culture",
                         color_discrete_sequence=["#3fb950", "#2ea043", "#1b5e20", "#58a6ff", "#f0883e"])
            fig2.update_layout(plotly_dark_layout(height=400))
            st.plotly_chart(fig2, use_container_width=True)
    
    # Graphique 3: Évolution temporelle
    st.markdown('<p class="agri-section-label" style="margin-top:2rem;">Tendances Temporelles</p>', unsafe_allow_html=True)
    
    if not df_filtered.empty:
        df_filtered['date'] = pd.to_datetime(df_filtered['date'])
        df_sorted = df_filtered.sort_values('date')
        
        fig3 = go.Figure()
        for culture in df_sorted['culture'].unique():
            culture_data = df_sorted[df_sorted['culture'] == culture]
            fig3.add_trace(go.Scatter(x=culture_data['date'], y=culture_data['rendement'],
                                     mode='lines+markers', name=culture))
        fig3.update_layout(plotly_dark_layout(
            title="Évolution du rendement dans le temps",
            xaxis_title="Date",
            yaxis_title="Rendement (kg/ha)",
            height=400
        ))
        st.plotly_chart(fig3, use_container_width=True)
    
    st.divider()
    
    # --- Tableau détaillé ---
    st.markdown('<p class="agri-section-label">Données Brutes</p>', unsafe_allow_html=True)
    
    if st.checkbox("Afficher le tableau complet des données"):
        st.dataframe(df_filtered, use_container_width=True, hide_index=True)
    
    st.divider()
    
    # --- Statistiques ---
    st.markdown('<p class="agri-section-label">Statistiques Détaillées</p>', unsafe_allow_html=True)
    
    stats_col1, stats_col2 = st.columns(2, gap="large")
    
    with stats_col1:
        st.markdown("**Rendement (kg/ha)**")
        st.markdown(f"- Minimum : {df_filtered['rendement'].min():.2f}")
        st.markdown(f"- Maximum : {df_filtered['rendement'].max():.2f}")
        st.markdown(f"- Médiane : {df_filtered['rendement'].median():.2f}")
        st.markdown(f"- Écart-type : {df_filtered['rendement'].std():.2f}")
    
    with stats_col2:
        st.markdown("**Consommation d'eau (m³)**")
        st.markdown(f"- Minimum : {df_filtered['eau'].min():.2f}")
        st.markdown(f"- Maximum : {df_filtered['eau'].max():.2f}")
        st.markdown(f"- Médiane : {df_filtered['eau'].median():.2f}")
        st.markdown(f"- Écart-type : {df_filtered['eau'].std():.2f}")

else:
    st.markdown("""
    <div class="agri-empty">
    <h3 style="margin-top:0;">Aucune donnée disponible</h3>
    <p>Commencez par <strong>enregistrer vos premières données</strong> dans la section Collecte pour voir vos analyses apparaître ici.</p>
    </div>
    """, unsafe_allow_html=True)
