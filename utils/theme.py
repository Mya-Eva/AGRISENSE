import streamlit as st

# ── Color palette ──────────────────────────────────────────────────────────
BG       = "#0d1117"
SURFACE  = "#161b22"
BORDER   = "#21262d"
BORDER2  = "#30363d"
GREEN    = "#3fb950"
GREEN_HV = "#2ea043"
TEXT     = "#e6edf3"
MUTED    = "#8b949e"

# ── CSS ────────────────────────────────────────────────────────────────────
_CSS = f"""
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* ── hide default chrome ── */
#MainMenu {{ visibility: hidden !important; }}
footer {{ visibility: hidden !important; }}
header[data-testid="stHeader"] {{ display: none !important; }}
[data-testid="stDecoration"] {{ display: none !important; }}
[data-testid="stSidebarNav"] {{ display: none !important; }}

/* ── base ── */
html, body, .stApp {{
    font-family: 'Inter', sans-serif;
    background-color: {BG} !important;
    color: {TEXT};
}}
.main {{ background-color: {BG} !important; }}
section.main > div.block-container {{
    background-color: {BG};
    padding-top: 80px;
    max-width: 1200px;
}}

/* ── typography ── */
h1, h2, h3, h4, h5, h6,
p, span, li, label,
.stMarkdown p, .stMarkdown li {{
    font-family: 'Inter', sans-serif !important;
    color: {TEXT} !important;
}}
h1 {{ font-size: 2rem !important; font-weight: 800 !important; letter-spacing: -0.5px; }}
h2 {{ font-size: 1.5rem !important; font-weight: 700 !important; }}
h3 {{ font-size: 1.15rem !important; font-weight: 600 !important; }}

/* ── top navbar ── */
.agri-nav {{
    position: fixed;
    top: 0; left: 0; right: 0;
    z-index: 9999;
    height: 62px;
    background: {SURFACE};
    border-bottom: 1px solid {BORDER};
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 2.5rem;
}}
.agri-nav-brand {{
    font-size: 1.05rem;
    font-weight: 800;
    color: {GREEN};
    letter-spacing: 1px;
    text-decoration: none;
}}
.agri-nav-brand em {{ color: {TEXT}; font-style: normal; }}
.agri-nav-links {{ display: flex; align-items: center; gap: 4px; }}
.agri-nav-link {{
    color: {MUTED};
    text-decoration: none;
    font-size: 0.88rem;
    font-weight: 500;
    padding: 6px 14px;
    border-radius: 6px;
    transition: color .18s, background .18s;
}}
.agri-nav-link:hover {{ color: {TEXT}; background: {BORDER}; }}
.agri-nav-link.active {{ color: {GREEN}; background: rgba(63,185,80,.1); }}

/* ── sidebar (mobile nav) ── */
section[data-testid="stSidebar"] {{
    background-color: {SURFACE} !important;
    border-right: 1px solid {BORDER} !important;
}}
.sb-brand {{
    display: block;
    font-size: 1.05rem;
    font-weight: 800;
    color: {GREEN} !important;
    letter-spacing: 1px;
    margin-bottom: 1.75rem;
}}
.sb-label {{
    font-size: 0.7rem;
    font-weight: 600;
    color: {MUTED} !important;
    text-transform: uppercase;
    letter-spacing: .1em;
    margin-bottom: .4rem;
}}
.sb-link {{
    display: block;
    color: {MUTED} !important;
    text-decoration: none;
    font-size: 0.9rem;
    font-weight: 500;
    padding: 9px 12px;
    border-radius: 8px;
    margin-bottom: 2px;
    transition: color .18s, background .18s;
}}
.sb-link:hover {{ color: {TEXT} !important; background: {BORDER}; }}
.sb-link.active {{ color: {GREEN} !important; background: rgba(63,185,80,.1); }}

/* ── desktop: hide sidebar ── */
@media (min-width: 769px) {{
    section[data-testid="stSidebar"],
    [data-testid="stSidebarCollapsedControl"] {{
        display: none !important;
    }}
    section.main > div.block-container {{
        padding-left: 2.5rem !important;
        padding-right: 2.5rem !important;
    }}
}}

/* ── mobile: hide top navbar ── */
@media (max-width: 768px) {{
    .agri-nav {{ display: none !important; }}
    section.main > div.block-container {{ padding-top: 1rem; }}
}}

/* ── buttons ── */
.stButton > button,
[data-testid="stFormSubmitButton"] > button {{
    background-color: {GREEN} !important;
    color: #0d1117 !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 8px !important;
    transition: background .18s, box-shadow .18s, transform .15s !important;
    font-size: 0.88rem !important;
}}
.stButton > button:hover,
[data-testid="stFormSubmitButton"] > button:hover {{
    background-color: {GREEN_HV} !important;
    box-shadow: 0 4px 14px rgba(63,185,80,.35) !important;
    transform: translateY(-1px) !important;
}}

/* ── inputs ── */
[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input,
[data-testid="stTextArea"] textarea,
[data-testid="stDateInput"] input {{
    background-color: {BORDER} !important;
    color: {TEXT} !important;
    border: 1px solid {BORDER2} !important;
    border-radius: 8px !important;
    font-family: 'Inter', sans-serif !important;
}}
[data-testid="stTextInput"] input:focus,
[data-testid="stNumberInput"] input:focus {{
    border-color: {GREEN} !important;
    box-shadow: 0 0 0 3px rgba(63,185,80,.15) !important;
}}
[data-testid="stSelectbox"] > div > div {{
    background-color: {BORDER} !important;
    color: {TEXT} !important;
    border: 1px solid {BORDER2} !important;
    border-radius: 8px !important;
}}
[data-testid="stMultiSelect"] > div {{
    background-color: {BORDER} !important;
    border: 1px solid {BORDER2} !important;
    border-radius: 8px !important;
}}

/* ── metrics ── */
[data-testid="stMetric"] {{
    background: {SURFACE};
    border: 1px solid {BORDER};
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
}}
[data-testid="stMetricLabel"] p {{
    color: {MUTED} !important;
    font-size: 0.78rem !important;
    text-transform: uppercase;
    letter-spacing: .05em;
}}
[data-testid="stMetricValue"] {{
    color: {TEXT} !important;
    font-weight: 700 !important;
}}

/* ── form container ── */
[data-testid="stForm"] {{
    background: {SURFACE};
    border: 1px solid {BORDER};
    border-radius: 16px;
    padding: 2rem;
}}

/* ── expander ── */
[data-testid="stExpander"] {{
    background: {SURFACE};
    border: 1px solid {BORDER} !important;
    border-radius: 12px;
}}

/* ── divider ── */
hr {{ border-color: {BORDER} !important; }}

/* ── dataframe ── */
[data-testid="stDataFrame"] {{
    border: 1px solid {BORDER};
    border-radius: 12px;
    overflow: hidden;
}}

/* ── info/success alert ── */
[data-testid="stAlert"] {{ border-radius: 10px; }}

/* ── checkbox ── */
[data-testid="stCheckbox"] label {{ color: {TEXT} !important; }}

/* ── feature card ── */
.agri-card {{
    background: {SURFACE};
    border: 1px solid {BORDER};
    border-radius: 14px;
    padding: 1.75rem;
    transition: border-color .2s, box-shadow .2s;
}}
.agri-card:hover {{
    border-color: {GREEN};
    box-shadow: 0 4px 24px rgba(63,185,80,.1);
}}
.agri-card-title {{
    font-size: 0.85rem;
    font-weight: 700;
    color: {GREEN};
    text-transform: uppercase;
    letter-spacing: .08em;
    margin-bottom: .5rem;
}}
.agri-card-body {{ color: {MUTED}; font-size: 0.9rem; line-height: 1.6; }}

/* ── info banner ── */
.agri-banner {{
    background: rgba(63,185,80,.08);
    border-left: 3px solid {GREEN};
    border-radius: 8px;
    padding: 1rem 1.25rem;
    margin-bottom: 1.5rem;
    color: {TEXT};
    font-size: 0.9rem;
}}

/* ── section label ── */
.agri-section-label {{
    font-size: 0.72rem;
    font-weight: 700;
    color: {GREEN};
    text-transform: uppercase;
    letter-spacing: .12em;
    margin-bottom: .75rem;
}}

/* ── empty state ── */
.agri-empty {{
    background: {SURFACE};
    border: 2px dashed {BORDER2};
    border-radius: 14px;
    padding: 3.5rem;
    text-align: center;
    color: {MUTED};
}}
.agri-empty h3 {{ color: {TEXT} !important; font-size: 1.2rem !important; }}
"""


def _navbar(current_page: str) -> str:
    def cls(page): return "active" if current_page == page else ""
    return f"""
<nav class="agri-nav">
  <a href="/" target="_self" class="agri-nav-brand">AGRI<em>SENSE</em></a>
  <div class="agri-nav-links">
    <a href="/" target="_self"          class="agri-nav-link {cls('home')}">Accueil</a>
    <a href="/Collecte" target="_self" class="agri-nav-link {cls('collecte')}">Collecte</a>
    <a href="/Analyse" target="_self" class="agri-nav-link {cls('analyse')}">Analyse</a>
  </div>
</nav>
"""


def _sidebar_nav(current_page: str):
    def cls(page): return "active" if current_page == page else ""
    with st.sidebar:
        st.markdown(f"""
<span class="sb-brand">AGRISENSE</span>
<p class="sb-label">Navigation</p>
<a href="/" target="_self"          class="sb-link {cls('home')}">Accueil</a>
<a href="/Collecte" target="_self" class="sb-link {cls('collecte')}">Collecte</a>
<a href="/Analyse" target="_self"  class="sb-link {cls('analyse')}">Analyse</a>
""", unsafe_allow_html=True)


def apply_theme(current_page: str = "home"):
    """Inject global dark theme, top navbar, and mobile sidebar nav.

    Args:
        current_page: one of "home" | "collecte" | "analyse"
    """
    st.markdown(f"<style>{_CSS}</style>", unsafe_allow_html=True)
    st.markdown(_navbar(current_page), unsafe_allow_html=True)
    _sidebar_nav(current_page)


def plotly_dark_layout(**kwargs) -> dict:
    """Return a dark-themed Plotly layout dict, merging any extra kwargs."""
    base = dict(
        paper_bgcolor=SURFACE,
        plot_bgcolor=SURFACE,
        font=dict(family="Inter, sans-serif", color=TEXT, size=12),
        xaxis=dict(gridcolor=BORDER, linecolor=BORDER2, tickcolor=BORDER2, tickfont=dict(color=MUTED)),
        yaxis=dict(gridcolor=BORDER, linecolor=BORDER2, tickcolor=BORDER2, tickfont=dict(color=MUTED)),
        title_font=dict(color=TEXT, size=14, family="Inter, sans-serif"),
        margin=dict(l=16, r=16, t=48, b=16),
        colorway=[GREEN, "#58a6ff", "#f0883e", "#bc8cff", "#ff7b72", "#79c0ff"],
    )
    base.update(kwargs)
    return base
