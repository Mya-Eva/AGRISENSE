import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Analyse - AgroStat Pro", page_icon="📊", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #1b5e20;
        color: white;
        font-weight: 700;
        border: none;
        transition: 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #2e7d32;
    }
    .metric-card {
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 2rem;
        background: white;
        box-shadow: 0 10px 30px rgba(15, 23, 42, 0.08);
    }
    .empty-state {
        background: #f8fafc;
        border: 2px dashed #cbd5e1;
        border-radius: 12px;
        padding: 3rem;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Analyse des Données")
st.markdown("Visualisez vos rendements, consommations et performances agricoles en temps réel.")

def load_data():
    with sqlite3.connect('agri_data.db') as conn:
        try:
            return pd.read_sql_query("SELECT * FROM production", conn)
        except:
            return pd.DataFrame()

df = load_data()

if not df.empty:
    # --- KPIs et Résumés ---
    st.markdown("📈 Indicateurs Clés")
    
    kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)
    
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
    st.markdown("### 🔍 Filtres")
    filter_col1, filter_col2 = st.columns(2)
    
    with filter_col1:
        cultures_disponibles = df['culture'].unique().tolist()
        culture_filtre = st.multiselect("Filtrer par culture", cultures_disponibles, default=cultures_disponibles)
        df_filtered = df[df['culture'].isin(culture_filtre)]
    
    with filter_col2:
        st.write("")  # Espace vide pour alignement
        st.write("")
        if st.button("🔄 Réinitialiser les filtres"):
            st.rerun()
    
    st.divider()
    
    # --- Visualisations ---
    st.markdown("📊 Visualisations")
    
    viz_col1, viz_col2 = st.columns(2)
    
    # Graphique 1: Rendement par culture
    with viz_col1:
        if not df_filtered.empty:
            rendement_par_culture = df_filtered.groupby('culture')['rendement'].mean().reset_index()
            fig1 = px.bar(rendement_par_culture, x='culture', y='rendement',
                         title="Rendement moyen par culture (kg/ha)",
                         labels={'culture': 'Culture', 'rendement': 'Rendement (kg/ha)'},
                         color='rendement', color_continuous_scale='Greens')
            fig1.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig1, use_container_width=True)
    
    # Graphique 2: Distribution des cultures
    with viz_col2:
        if not df_filtered.empty:
            culture_count = df_filtered['culture'].value_counts().reset_index()
            culture_count.columns = ['culture', 'count']
            fig2 = px.pie(culture_count, names='culture', values='count',
                         title="Distribution des récoltes par culture",
                         color_discrete_sequence=px.colors.sequential.Greens)
            fig2.update_layout(height=400)
            st.plotly_chart(fig2, use_container_width=True)
    
    # Graphique 3: Évolution temporelle
    st.markdown("📈 Tendances Temporelles")
    
    if not df_filtered.empty:
        df_filtered['date'] = pd.to_datetime(df_filtered['date'])
        df_sorted = df_filtered.sort_values('date')
        
        fig3 = go.Figure()
        for culture in df_sorted['culture'].unique():
            culture_data = df_sorted[df_sorted['culture'] == culture]
            fig3.add_trace(go.Scatter(x=culture_data['date'], y=culture_data['rendement'],
                                     mode='lines+markers', name=culture))
        fig3.update_layout(title="Évolution du rendement dans le temps",
                          xaxis_title="Date",
                          yaxis_title="Rendement (kg/ha)",
                          height=400)
        st.plotly_chart(fig3, use_container_width=True)
    
    st.divider()
    
    # --- Tableau détaillé ---
    st.markdown("📋 Données Brutes")
    
    if st.checkbox("Afficher le tableau complet des données"):
        st.dataframe(df_filtered, use_container_width=True, hide_index=True)
    
    st.divider()
    
    # --- Statistiques ---
    st.markdown("📊 Statistiques Détaillées")
    
    stats_col1, stats_col2 = st.columns(2)
    
    with stats_col1:
        st.write("**Rendement (kg/ha)**")
        st.write(f"- Minimum : {df_filtered['rendement'].min():.2f}")
        st.write(f"- Maximum : {df_filtered['rendement'].max():.2f}")
        st.write(f"- Médiane : {df_filtered['rendement'].median():.2f}")
        st.write(f"- Écart-type : {df_filtered['rendement'].std():.2f}")
    
    with stats_col2:
        st.write("**Consommation d'eau (m³)**")
        st.write(f"- Minimum : {df_filtered['eau'].min():.2f}")
        st.write(f"- Maximum : {df_filtered['eau'].max():.2f}")
        st.write(f"- Médiane : {df_filtered['eau'].median():.2f}")
        st.write(f"- Écart-type : {df_filtered['eau'].std():.2f}")

else:
    st.markdown("""
    <div class="empty-state">
    <h3>📭 Aucune donnée disponible</h3>
    <p>Commencez par <strong>enregistrer vos premières données</strong> dans la section Collecte pour voir vos analyses apparaître ici.</p>
    </div>
    """, unsafe_allow_html=True)
