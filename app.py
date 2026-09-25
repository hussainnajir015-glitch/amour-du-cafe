"""
Amour Du Cafè — Static Café Website
====================================
A warm, cozy, production-ready Streamlit website for a café.
Deployed on Streamlit Community Cloud.

Author : Amour Du Cafè
Stack  : Streamlit (no backend, no database)
"""

from datetime import date, time
from typing import Dict, List, Tuple

import streamlit as st
import streamlit.components.v1 as components

# ---------------------------------------------------------------------------
# 1. PAGE CONFIGURATION  (must be the first Streamlit call)
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Amour Du Cafè — Brewed with Love",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------------------------
# 2. GLOBAL STYLES  (single optimized <style> block)
#    - Google Fonts: Playfair Display (headings) + Poppins (body)
#    - Hides Streamlit chrome (menu, footer, header)
#    - Design tokens as CSS variables for consistency
#    - Mobile media query < 768px
# ---------------------------------------------------------------------------
GLOBAL_CSS = """
<style>
/* ---------- Google Fonts ---------- */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&family=Poppins:wght@300;400;500;600&display=swap');

/* ---------- Design Tokens ---------- */
:root {
    --espresso:      #2B1A12;
    --coffee:        #3E2723;
    --mocha:         #5D4037;
    --latte:         #8D6E63;
    --cream:         #F5E6D3;
    --cream-light:   #FAF3E8;
    --terracotta:    #C97B5A;
    --sage:          #7C8A6A;
    --gold:          #D4A056;
    --text-dark:     #2B1A12;
    --text-muted:    #6B564D;
    --shadow-sm:     0 3px 10px rgba(43, 26, 18, 0.08);
    --shadow-md:     0 8px 24px rgba(43, 26, 18, 0.12);
    --shadow-lg:     0 16px 40px rgba(43, 26, 18, 0.18);
    --radius-sm:     10px;
    --radius-md:     16px;
    --radius-lg:     24px;
    --radius-pill:   999px;
    --transition:    all 0.35s cubic-bezier(0.25, 0.8, 0.25, 1);
}

/* ---------- Hide Streamlit chrome ---------- */
#MainMenu { visibility: hidden; }
footer    { visibility: hidden; }
header    { visibility: hidden; }
[data-testid="stToolbar"]        { display: none; }
[data-testid="stDecoration"]     { display: none; }
[data-testid="stStatusWidget"]   { display: none; }
[data-testid="stHeader"]         { display: none; }

/* ---------- Base / Body ---------- */
html, body, [class*="css"] {
    font-family: 'Poppins', -apple-system, BlinkMacSystemFont, sans-serif;
    color: var(--text-dark);
}
.stApp {
    background:
        radial-gradient(circle at 15% 10%, rgba(201, 123, 90, 0.06), transparent 45%),
        radial-gradient(circle at 85% 90%, rgba(124, 138, 106, 0.06), transparent 45%),
        linear-gradient(135deg, #FAF3E8 0%, #F5E6D3 100%);
    background-attachment: fixed;
}
.block-container {
    padding-top: 1.2rem;
    padding-bottom: 2rem;
    max-width: 1280px;
}

/* ---------- Typography ---------- */
h1, h2, h3, h4 {
    font-family: 'Playfair Display', Georgia, serif;
    color: var(--coffee);
    letter-spacing: 0.3px;
}
p, span, div, label {
    font-family: 'Poppins', sans-serif;
}

/* ---------- Hero ---------- */
.hero {
    position: relative;
    background: linear-gradient(135deg, var(--coffee) 0%, var(--espresso) 100%);
    background-size: cover;
    background-position: center;
    padding: 80px 40px;
    border-radius: var(--radius-lg);
    text-align: center;
    margin-bottom: 40px;
    overflow: hidden;
    box-shadow: var(--shadow-lg);
}
.hero::before {
    content: "";
    position: absolute;
    top: -50%; left: -50%;
    width: 200%; height: 200%;
    background:
        radial-gradient(circle at 30% 40%, rgba(212, 160, 86, 0.18), transparent 40%),
        radial-gradient(circle at 70% 70%, rgba(201, 123, 90, 0.15), transparent 40%);
    animation: float 14s ease-in-out infinite;
}
@keyframes float {
    0%, 100% { transform: translate(0, 0) rotate(0deg); }
    50%      { transform: translate(-15px, -20px) rotate(3deg); }
}
.hero-content { position: relative; z-index: 2; }

/* Hero logo (optional) */
.hero-logo {
    display: block;
    max-width: 130px;
    max-height: 130px;
    width: auto;
    height: auto;
    margin: 0 auto 18px auto;
    filter: drop-shadow(0 6px 18px rgba(0, 0, 0, 0.45));
    animation: logoFade 1.2s ease-out;
}
.hero-logo-fallback {
    display: block;
    font-size: 3.2rem;
    margin-bottom: 10px;
}
@keyframes logoFade {
    from { opacity: 0; transform: translateY(-10px); }
    to   { opacity: 1; transform: translateY(0); }
}

.hero h1 {
    color: var(--cream);
    font-size: clamp(2.4rem, 5.5vw, 4.2rem);
    margin: 0;
    letter-spacing: 3px;
    text-shadow: 2px 4px 14px rgba(0, 0, 0, 0.55);
    font-weight: 700;
}
.hero .divider {
    width: 80px; height: 2px;
    background: linear-gradient(90deg, transparent, var(--gold), transparent);
    margin: 22px auto;
}
.hero p {
    color: #E8D9C7;
    font-size: clamp(1rem, 1.6vw, 1.35rem);
    font-style: italic;
    font-family: 'Playfair Display', serif;
    margin: 0;
    letter-spacing: 1px;
}
.hero .badge {
    display: inline-block;
    margin-top: 26px;
    padding: 8px 22px;
    border: 1px solid rgba(212, 160, 86, 0.6);
    border-radius: var(--radius-pill);
    color: var(--gold);
    font-size: 0.85rem;
    letter-spacing: 2px;
    text-transform: uppercase;
}

/* ---------- Section Header ---------- */
.section-header {
    text-align: center;
    margin: 55px 0 30px 0;
    position: relative;
}
.section-header h2 {
    font-size: clamp(1.6rem, 3vw, 2.4rem);
    margin: 0;
    display: inline-block;
    position: relative;
    padding-bottom: 14px;
}
.section-header h2::after {
    content: "";
    position: absolute;
    bottom: 0; left: 50%;
    transform: translateX(-50%);
    width: 60px; height: 3px;
    background: linear-gradient(90deg, var(--terracotta), var(--gold));
    border-radius: 3px;
}
.section-header .subtitle {
    display: block;
    color: var(--text-muted);
    font-size: 0.95rem;
    margin-top: 12px;
    letter-spacing: 1px;
    font-style: italic;
}

/* ---------- Cards (Info, Menu, Review) ---------- */
.card {
    background: #FFFFFF;
    border-radius: var(--radius-md);
    padding: 28px;
    box-shadow: var(--shadow-sm);
    transition: var(--transition);
    height: 100%;
    border: 1px solid rgba(141, 110, 99, 0.08);
}
.card:hover {
    transform: translateY(-6px);
    box-shadow: var(--shadow-md);
}
.card h3, .card h4 {
    color: var(--coffee);
    margin-top: 0;
    margin-bottom: 12px;
}
.card p { color: var(--text-muted); line-height: 1.7; }

/* Menu card */
.menu-card {
    background: #FFFFFF;
    border-radius: var(--radius-md);
    padding: 22px 24px;
    margin-bottom: 16px;
    box-shadow: var(--shadow-sm);
    border-left: 4px solid var(--latte);
    transition: var(--transition);
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 16px;
}
.menu-card:hover {
    transform: translateX(6px);
    border-left-color: var(--terracotta);
    box-shadow: var(--shadow-md);
}
.menu-card .menu-info h4 {
    margin: 0 0 4px 0;
    font-size: 1.15rem;
    color: var(--coffee);
}
.menu-card .menu-info p {
    margin: 0;
    font-size: 0.92rem;
    color: var(--text-muted);
}
.menu-card .price {
    font-family: 'Playfair Display', serif;
    font-weight: 700;
    font-size: 1.25rem;
    color: var(--terracotta);
    white-space: nowrap;
}

/* Info box (About) */
.info-box {
    background: linear-gradient(180deg, #FFFFFF 0%, var(--cream-light) 100%);
    padding: 34px;
    border-radius: var(--radius-md);
    box-shadow: var(--shadow-sm);
    height: 100%;
    border-top: 4px solid var(--sage);
    transition: var(--transition);
}
.info-box:hover { box-shadow: var(--shadow-md); }
.info-box h3 {
    color: var(--coffee);
    font-size: 1.4rem;
    margin-top: 0;
    margin-bottom: 16px;
}

/* Review card */
.review-card {
    background: #FFFFFF;
    padding: 24px;
    border-radius: var(--radius-md);
    box-shadow: var(--shadow-sm);
    margin-bottom: 16px;
    border-left: 4px solid var(--gold);
    transition: var(--transition);
}
.review-card:hover {
    transform: translateY(-3px);
    box-shadow: var(--shadow-md);
}
.review-card .reviewer {
    margin: 0;
    color: var(--coffee);
    font-family: 'Playfair Display', serif;
    font-size: 1.1rem;
}
.review-card .stars {
    color: var(--gold);
    font-size: 1.1rem;
    margin: 6px 0 10px 0;
    letter-spacing: 2px;
}
.review-card .review-text {
    color: var(--text-muted);
    margin: 0;
    font-style: italic;
    line-height: 1.65;
}

/* Signature specials card */
.special-card {
    background: linear-gradient(160deg, #FFFFFF 0%, var(--cream-light) 100%);
    padding: 30px 24px;
    border-radius: var(--radius-md);
    text-align: center;
    box-shadow: var(--shadow-sm);
    border-top: 4px solid var(--terracotta);
    transition: var(--transition);
    height: 100%;
}
.special-card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: var(--shadow-lg);
}
.special-card .icon {
    font-size: 2.4rem;
    display: block;
    margin-bottom: 12px;
}
.special-card h3 {
    margin: 0 0 10px 0;
    color: var(--coffee);
    font-size: 1.25rem;
}
.special-card p {
    color: var(--text-muted);
    font-size: 0.92rem;
    margin: 0 0 14px 0;
    line-height: 1.6;
}
.special-card .price {
    font-family: 'Playfair Display', serif;
    font-weight: 700;
    color: var(--terracotta);
    font-size: 1.15rem;
}

/* ---------- Gallery Tile (SMALLER + CENTERED) ---------- */
.gallery-tile {
    position: relative;
    aspect-ratio: 1 / 1;            /* square */
    width: 100%;                    /* fill its column */
    max-width: 300px;               /* medium cap — prevents giant tiles */
    margin: 0 auto 8px auto;        /* centred + a bit of bottom gap */
    border-radius: var(--radius-md);
    overflow: hidden;
    box-shadow: var(--shadow-sm);
    transition: var(--transition);
    display: flex;
    align-items: flex-end;
    justify-content: flex-start;
    padding: 16px;
    color: #FFF;
    cursor: pointer;
    background-size: cover;
    background-position: center;
}
.gallery-tile::after {
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(180deg, transparent 40%, rgba(0,0,0,0.7) 100%);
    z-index: 1;
}
.gallery-tile:hover {
    transform: scale(1.04);
    box-shadow: var(--shadow-lg);
}
.gallery-tile span {
    position: relative;
    z-index: 2;
    font-family: 'Playfair Display', serif;
    font-weight: 600;
    font-size: 0.95rem;
    letter-spacing: 0.5px;
    text-shadow: 1px 1px 6px rgba(0,0,0,0.7);
}

/* Gradient fallback tiles */
.grad-1 { background: linear-gradient(135deg, #C97B5A, #8D6E63); }
.grad-2 { background: linear-gradient(135deg, #7C8A6A, #5D4037); }
.grad-3 { background: linear-gradient(135deg, #D4A056, #C97B5A); }
.grad-4 { background: linear-gradient(135deg, #3E2723, #8D6E63); }
.grad-5 { background: linear-gradient(135deg, #8D6E63, #D4A056); }
.grad-6 { background: linear-gradient(135deg, #5D4037, #7C8A6A); }

/* ---------- Buttons ---------- */
.stButton > button {
    background: linear-gradient(135deg, var(--mocha), var(--terracotta));
    color: #FFFFFF;
    border: none;
    padding: 12px 28px;
    border-radius: var(--radius-pill);
    font-family: 'Poppins', sans-serif;
    font-weight: 500;
    font-size: 0.95rem;
    letter-spacing: 0.5px;
    transition: var(--transition);
    box-shadow: 0 4px 14px rgba(141, 110, 99, 0.28);
    width: 100%;
}
.stButton > button:hover {
    background: linear-gradient(135deg, var(--coffee), var(--mocha));
    transform: translateY(-2px);
    box-shadow: 0 8px 22px rgba(62, 39, 35, 0.35);
    color: #FFFFFF;
}
.stButton > button:focus:not(:active) {
    color: #FFFFFF;
    border-color: transparent;
}

/* ---------- Form Inputs ---------- */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div > div {
    border-radius: var(--radius-sm) !important;
    border: 1px solid rgba(141, 110, 99, 0.25) !important;
    background: #FFFFFF !important;
    font-family: 'Poppins', sans-serif !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: var(--terracotta) !important;
    box-shadow: 0 0 0 2px rgba(201, 123, 90, 0.15) !important;
}

/* ---------- Tabs ---------- */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    border-bottom: 1px solid rgba(141, 110, 99, 0.2);
    padding-bottom: 6px;
    justify-content: center;
}
.stTabs [data-baseweb="tab"] {
    background: transparent;
    border-radius: var(--radius-pill);
    padding: 8px 20px;
    font-family: 'Poppins', sans-serif;
    font-weight: 500;
    color: var(--text-muted);
    transition: var(--transition);
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, var(--mocha), var(--terracotta)) !important;
    color: #FFFFFF !important;
}
.stTabs [data-baseweb="tab-highlight"] { background: transparent; }

/* ---------- Divider / Expander ---------- */
hr { border-color: rgba(141, 110, 99, 0.18); }
.streamlit-expanderHeader {
    font-family: 'Poppins', sans-serif;
    font-weight: 500;
    color: var(--coffee);
}

/* ---------- Footer ---------- */
.footer {
    background: linear-gradient(135deg, var(--coffee), var(--espresso));
    color: #D7CCC8;
    padding: 44px 30px 32px 30px;
    border-radius: var(--radius-lg);
    text-align: center;
    margin-top: 60px;
    box-shadow: var(--shadow-md);
}
.footer h3 {
    color: var(--cream);
    font-size: 1.7rem;
    margin: 0 0 8px 0;
    letter-spacing: 2px;
}
.footer .tagline {
    font-style: italic;
    color: #C9B7A6;
    margin: 0 0 24px 0;
    font-family: 'Playfair Display', serif;
}
.footer .socials {
    display: flex;
    justify-content: center;
    gap: 18px;
    flex-wrap: wrap;
    margin-bottom: 24px;
}
.footer .socials a {
    color: var(--cream);
    text-decoration: none;
    padding: 8px 18px;
    border: 1px solid rgba(245, 230, 211, 0.25);
    border-radius: var(--radius-pill);
    font-size: 0.88rem;
    transition: var(--transition);
}
.footer .socials a:hover {
    background: rgba(212, 160, 86, 0.2);
    border-color: var(--gold);
    color: var(--gold);
    transform: translateY(-2px);
}
.footer .copyright {
    font-size: 0.82rem;
    color: #A8968A;
    margin: 0;
    letter-spacing: 0.5px;
}

/* ---------- Newsletter box ---------- */
.newsletter-box {
    background: linear-gradient(135deg, #FFFFFF, var(--cream-light));
    border: 1px dashed var(--latte);
    border-radius: var(--radius-md);
    padding: 26px;
    text-align: center;
    margin-top: 30px;
}
.newsletter-box h3 {
    margin: 0 0 6px 0;
    color: var(--coffee);
    font-size: 1.2rem;
}
.newsletter-box p {
    color: var(--text-muted);
    font-size: 0.9rem;
    margin: 0 0 16px 0;
}

/* ---------- Map wrapper ---------- */
.map-wrap {
    border-radius: var(--radius-md);
    overflow: hidden;
    box-shadow: var(--shadow-sm);
    border: 3px solid #FFFFFF;
}

/* ---------- Mobile Responsiveness ---------- */
@media (max-width: 768px) {
    .block-container { padding-left: 1rem; padding-right: 1rem; }
    .hero { padding: 50px 22px; border-radius: var(--radius-md); }
    .hero h1 { letter-spacing: 1.5px; }
    .section-header { margin: 38px 0 22px 0; }
    .card, .info-box, .special-card { padding: 22px; }
    .menu-card {
        flex-direction: column;
        align-items: flex-start;
        gap: 6px;
        padding: 18px;
    }
    .menu-card .price { align-self: flex-end; }
    .footer { padding: 32px 20px 24px 20px; }
    .stButton > button { padding: 11px 20px; font-size: 0.9rem; }
    .stTabs [data-baseweb="tab"] { padding: 7px 14px; font-size: 0.85rem; }

    /* Gallery goes full-width square on phones */
       .gallery-tile {
        max-width: 100%;
        aspect-ratio: 1 / 1;
        padding: 14px;
        margin-bottom: 6px;
    }
}
</style>
"""

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# 3. STATIC DATA  (cached — never re-computed across reruns)
# ---------------------------------------------------------------------------
@st.cache_data(show_spinner=False)
def get_menu_data() -> Dict[str, List[Tuple[str, str, float]]]:
    """Return the full café menu grouped by category."""
    return {
        "Coffee": [
            ("Espresso", "Bold and pure", 200.00),
            ("Cappuccino", "Classic Italian style", 250.00),
            ("Café Latte", "Smooth and creamy", 200.00),
            ("Café Amour", "Signature with rose & vanilla", 200.50),
            ("Mocha Passion", "Chocolate espresso delight", 250.75),
            ("Flat White", "Velvety microfoam", 240.50),
            ("Iced Americano", "Refreshing and bold", 240.00),
            ("Iced Rose Latte", "Floral and cool", 250.25),
            ("Cold Brew", "Slow-steeped perfection", 240.75),
            ("Frappé Amour", "Blended coffee bliss", 250.95),
        ],
        "Tea & Others": [
            ("Earl Grey", "Classic bergamot", 75.50),
            ("Chamomile Dream", "Calming herbal blend", 80.75),
            ("Matcha Latte", "Japanese ceremonial grade", 15.50),
            ("Chai Latte", "Spiced and warming", 40.75),
            ("Hot Chocolate", "Belgian chocolate", 140.50),
            ("Fresh Orange Juice", "Freshly squeezed", 140.00),
        ],
        "Pastries": [
            ("Butter Croissant", "Flaky and golden", 300.50),
            ("Pain au Chocolat", "Chocolate filled", 345.00),
            ("Blueberry Muffin", "Bursting with berries", 50.75),
            ("Cinnamon Roll", "Warm and gooey", 240.25),
            ("Almond Danish", "Toasted almonds", 240.00),
        ],
        "Desserts": [
            ("Tiramisu", "Classic Italian", 60.50),
            ("Crème Brûlée", "French elegance", 160.75),
            ("Chocolate Lava Cake", "Warm molten center", 170.00),
            ("Cheesecake", "New York style", 260.25),
            ("Macarons (3 pcs)", "Assorted flavors", 15.50),
        ],
    }


@st.cache_data(show_spinner=False)
def get_signature_specials() -> List[Dict[str, str]]:
    """Return the three signature specials shown on the Home page."""
    return [
        {
            "icon": "💕",
            "name": "Café Amour",
            "desc": "Our signature espresso with a hint of vanilla and rose.",
            "price": "NPR 250.50",
        },
        {
            "icon": "🌹",
            "name": "Rose Latte",
            "desc": "Silky latte infused with organic rose petals.",
            "price": "NPR 300.00",
        },
        {
            "icon": "🍫",
            "name": "Mocha Passion",
            "desc": "Rich dark chocolate blended with premium espresso.",
            "price": "NPR 250.75",
        },
    ]


import base64
from pathlib import Path

IMAGES_DIR = Path(__file__).parent / "images"


@st.cache_data(show_spinner=False)
def img_to_base64(filename: str) -> str:
    """Load a local image from images/ and return it as a base64 data URI."""
    path = IMAGES_DIR / filename
    if not path.exists():
        return ""
    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    ext = path.suffix.lower().lstrip(".")
    mime = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "webp": "webp"}.get(ext, "jpeg")
    return f"data:image/{mime};base64,{encoded}"


@st.cache_data(show_spinner=False)
def get_gallery_items() -> List[Dict[str, str]]:
    """
    Gallery tiles.
    Each 'filename' must match a file inside the images/ folder.
    If a file is missing, the tile falls back to its gradient.
    """
    return [
        {"label": "Cozy Corners",  "filename": "gallery_1.jpg", "grad": "grad-1"},
        {"label": "Artisan Brews", "filename": "gallery_2.jpg", "grad": "grad-2"},
        {"label": "Sweet Bites",   "filename": "gallery_3.jpg", "grad": "grad-3"},
        {"label": "Morning Light", "filename": "gallery_4.jpg", "grad": "grad-4"},
        {"label": "Evening Vibes", "filename": "gallery_5.jpg", "grad": "grad-5"},
        {"label": "Our Baristas",  "filename": "gallery_6.jpg", "grad": "grad-6"},
    ]

@st.cache_data(show_spinner=False)
def get_seed_reviews() -> List[Dict[str, object]]:
    """Initial (seed) reviews shown on first load."""
    return [
        {"name": "Ajim Miya.",    "rating": 5, "text": "The best coffee I've ever had! The ambiance is magical."},
        {"name": "Sabir Hussain.", "rating": 5, "text": "Rose Latte is a masterpiece. Highly recommend!"},
        {"name": "Najir Hussain.", "rating": 5, "text": "Cozy place, lovely staff. Perfect for a date."},
    ]


# ---------------------------------------------------------------------------
# 4. SESSION STATE  (for page navigation and reviews)
# ---------------------------------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "reviews" not in st.session_state:
    st.session_state.reviews = list(get_seed_reviews())


# ---------------------------------------------------------------------------
# 5. REUSABLE UI HELPERS
# ---------------------------------------------------------------------------
def section_header(title: str, subtitle: str = "") -> None:
    """Render a centred section header with an optional subtitle."""
    sub_html = f'<span class="subtitle">{subtitle}</span>' if subtitle else ""
    st.markdown(
        f'<div class="section-header"><h2>{title}</h2>{sub_html}</div>',
        unsafe_allow_html=True,
    )


def render_hero() -> None:
    """Render the top hero banner (with logo image)."""
    logo_uri = img_to_base64("logo.jpg")  # change to "logo.jpg" if needed
    logo_html = (
        f'<img src="{logo_uri}" class="hero-logo" alt="Amour Du Cafè logo">'
        if logo_uri
        else '<span class="hero-logo-fallback">☕</span>'
    )
    st.markdown(
        f"""
        <div class="hero">
            <div class="hero-content">
                {logo_html}
                <h1>Amour Du Cafè</h1>
                <div class="divider"></div>
                <p>Where every cup tells a story of love and passion</p>
                <span class="badge">Est. with love · Damauli, Nepal</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_navbar() -> None:
    """Render the top navigation row (Home / Menu / Reviews / Contact)."""
    nav_items = [
        ("🏠  Home",    "Home"),
        ("📋  Menu",    "Menu"),
        ("⭐  Reviews", "Reviews"),
        ("📍  Contact", "Contact"),
    ]
    cols = st.columns(len(nav_items))
    for col, (label, key) in zip(cols, nav_items):
        with col:
            if st.button(label, key=f"nav_{key}", use_container_width=True):
                st.session_state.page = key
                st.rerun()


def render_gallery_tile(item: Dict[str, str]) -> None:
    """Render one gallery tile — uses local photo if it exists, else gradient."""
    data_uri = img_to_base64(item["filename"]) if item.get("filename") else ""
    if data_uri:
        style = f"background-image: url('{data_uri}');"
        css_class = "gallery-tile"
    else:
        style = ""
        css_class = f"gallery-tile {item.get('grad', 'grad-1')}"
    st.markdown(
        f'<div class="{css_class}" style="{style}"><span>{item["label"]}</span></div>',
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# 6. PAGE RENDERERS
# ---------------------------------------------------------------------------
def render_home() -> None:
    """Home page: About + Why Choose Us + Signature Specials + Gallery."""
    section_header("Welcome to Amour Du Cafè", "A love letter to the art of coffee")

    # --- About / Why Choose Us ---
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown(
            """
            <div class="info-box">
                <h3>Our Story</h3>
                <p>Nestled in the heart of Damauli, <b>Amour Du Cafè</b> is more than just a
                coffee shop — it's a love letter to the art of coffee making.</p>
                <p>Every bean is hand-picked, every roast is perfected, and every cup is
                brewed with <b>amour</b> (love).</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class="info-box">
                <h3>Why Choose Us?</h3>
                <p>🌱 &nbsp; Ethically sourced premium beans<br>
                   👨‍🍳 &nbsp; Expert baristas &amp; artisan brewing<br>
                   🏡 &nbsp; Cozy, romantic ambiance<br>
                   🍰 &nbsp; Freshly baked pastries daily<br>
                   🎵 &nbsp; Live acoustic evenings</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # --- Signature Specials ---
    section_header("Signature Specials", "Handcrafted favourites our guests love")
    specials = get_signature_specials()
    cols = st.columns(len(specials), gap="large")
    for col, item in zip(cols, specials):
        with col:
            st.markdown(
                f"""
                <div class="special-card">
                    <span class="icon">{item['icon']}</span>
                    <h3>{item['name']}</h3>
                    <p>{item['desc']}</p>
                    <span class="price">{item['price']}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

     # --- Gallery ---
    section_header("From Our Café", "A glimpse into our world")
    gallery = get_gallery_items()

    # 3-column grid, capped width so tiles stay medium-sized
    _, center_col, _ = st.columns([1, 4, 1])
    with center_col:
        for row_start in range(0, len(gallery), 3):
            cols = st.columns(3, gap="medium")
            for col, item in zip(cols, gallery[row_start : row_start + 3]):
                with col:
                    render_gallery_tile(item)


def render_menu() -> None:
    """Menu page: search + tabbed categories."""
    section_header("Our Menu", "Crafted with care, served with love")

    search = st.text_input(
        "🔍  Search for a dish or drink…",
        placeholder="e.g. latte, croissant, matcha",
        label_visibility="collapsed",
    )

    menu = get_menu_data()
    tabs = st.tabs([f"{icon}  {name}" for icon, name in [
        ("☕", "Coffee"), ("🍵", "Tea & Others"), ("🥐", "Pastries"), ("🍰", "Desserts"),
    ]])

    for tab, category in zip(tabs, menu.keys()):
        with tab:
            items = menu[category]
            if search:
                q = search.lower().strip()
                items = [i for i in items if q in i[0].lower() or q in i[1].lower()]

            if not items:
                st.info("No items match your search. Try a different keyword.")
                continue

            # Two-column responsive grid of menu cards
            left, right = st.columns(2, gap="medium")
            for idx, (name, desc, price) in enumerate(items):
                target = left if idx % 2 == 0 else right
                with target:
                    st.markdown(
                        f"""
                        <div class="menu-card">
                            <div class="menu-info">
                                <h4>{name}</h4>
                                <p>{desc}</p>
                            </div>
                            <span class="price">NPR {price:.2f}</span>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )


def render_reviews() -> None:
    """Reviews page: display + submit."""
    section_header("Customer Reviews", "What our guests are saying")

    for review in st.session_state.reviews:
        stars = "★" * int(review["rating"]) + "☆" * (5 - int(review["rating"]))
        st.markdown(
            f"""
            <div class="review-card">
                <p class="reviewer">{review['name']}</p>
                <p class="stars">{stars}</p>
                <p class="review-text">“{review['text']}”</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)
    section_header("Leave Your Review", "We'd love to hear from you")

    with st.form("review_form", clear_on_submit=True):
        col1, col2 = st.columns([2, 1])
        with col1:
            r_name = st.text_input("Your Name*", placeholder="Jane Doe")
        with col2:
            r_rating = st.slider("Rating", 1, 5, 5)

        r_text = st.text_area("Your Review*", placeholder="Tell us about your visit…")
        submitted = st.form_submit_button("Submit Review ⭐")

        if submitted:
            if r_name.strip() and r_text.strip():
                st.session_state.reviews.insert(
                    0,
                    {"name": r_name.strip(), "rating": int(r_rating), "text": r_text.strip()},
                )
                st.success("Thank you for your review! 💕")
                st.rerun()
            else:
                st.error("Please fill in all fields before submitting.")


def render_contact() -> None:
    """Contact page: location, hours, contact info, map, and message form."""
    section_header("Visit Us", "We'd love to see you at Amour Du Cafè")

    # --- Location + Hours | Contact + Socials ---
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown(
            """
            <div class="info-box">
                <h3>📍 Our Location</h3>
                <p>Vyas-02 Damauli<br>Tanahun, Nepal</p>
                <h3 style="margin-top:22px;">🕐 Opening Hours</h3>
                <p>Monday – Friday &nbsp; 7:00 AM – 10:00 PM<br>
                   Saturday &nbsp; 8:00 AM – 11:00 PM<br>
                   Sunday &nbsp; 8:00 AM – 9:00 PM</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class="info-box">
                <h3>📞 Get in Touch</h3>
                <p><b>Phone:</b> +977 971-2062918<br>
                   <b>Email:</b> amourducafe324@gmail.com</p>
                <h3 style="margin-top:22px;">Follow Us</h3>
                <p>📷 Instagram: @amourducafe<br>
                   📘 Facebook: Amour Du Café</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

      # --- Embedded Map (AM PRIME Barista Training Academy, Damauli) ---
    section_header("Find Us on the Map")
    st.markdown('<div class="map-wrap">', unsafe_allow_html=True)
    components.html(
        """
        <iframe
            src="https://www.google.com/maps?q=AM+PRIME+Barista+Training+Academy+Damauli+Tanahun+Nepal&output=embed"
            width="100%" height="380" style="border:0;" loading="lazy"
            referrerpolicy="no-referrer-when-downgrade">
        </iframe>
        """,
        height=400,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # --- Contact Form ---
    section_header("Send Us a Message", "We usually reply within a day")
    with st.form("contact_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Your Name")
        with col2:
            email = st.text_input("Your Email")

        subject = st.selectbox(
            "Subject",
            ["General Inquiry", "Feedback", "Catering", "Collaboration", "Other"],
        )
        message = st.text_area("Your Message")

        submitted = st.form_submit_button("Send Message ✉️")
        if submitted:
            if name.strip() and email.strip() and message.strip():
                st.success(f"Thank you, {name.strip()}! We'll get back to you soon. 💕")
                st.balloons()
            else:
                st.error("Please fill in all required fields.")


# ---------------------------------------------------------------------------
# 7. MAIN ROUTER
# ---------------------------------------------------------------------------
render_hero()
render_navbar()

# Small spacer between nav and page content
st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

PAGES = {
    "Home": render_home,
    "Menu": render_menu,
    "Reviews": render_reviews,
    "Contact": render_contact,
}
PAGES.get(st.session_state.page, render_home)()


# ---------------------------------------------------------------------------
# 8. NEWSLETTER + FOOTER  (shown on every page)
# ---------------------------------------------------------------------------
with st.expander("📧  Subscribe to our Newsletter"):
    st.markdown(
        '<div class="newsletter-box">'
        "<h3>Stay in the loop</h3>"
        "<p>Get seasonal menus, events, and little love notes — straight to your inbox.</p>"
        "</div>",
        unsafe_allow_html=True,
    )
    with st.form("newsletter", clear_on_submit=True):
        col1, col2 = st.columns([3, 1])
        with col1:
            nl_email = st.text_input(
                "Email",
                label_visibility="collapsed",
                placeholder="your@email.com",
            )
        with col2:
            sub = st.form_submit_button("Subscribe")
        if sub:
            if nl_email.strip() and "@" in nl_email:
                st.success("Subscribed! Welcome to the Amour Du Cafè family 💕")
            else:
                st.error("Please enter a valid email address.")


st.markdown(
    """
    <div class="footer">
        <h3>☕ Amour Du Cafè</h3>
        <p class="tagline">Brewed with love, served with passion</p>
             <div class="socials">
            <a href="https://www.facebook.com/share/1J9L545gMd/?mibextid=wwXIfr
" target="_blank">📷 Instagram</a>
            <a href="https://www.facebook.com/share/1J9L545gMd/?mibextid=wwXIfr
" target="_blank">📘 Facebook</a>
            <a href="mailto:amourducafe324@gmail.com">✉️ Email</a>
        </div>
        <p class="copyright">© 2025 Amour Du Cafè · All rights reserved · Made with ❤️ in Nepal</p>
    </div>
    """,
    unsafe_allow_html=True,
)