"""
Amour Du Cafè — Premium Dark Café Website (v6 — Final with Video Tile)
=======================================================================
Dark theme · Page backgrounds · Animated counters · 74 menu items
Gallery video tile (Sweet Bites) · Deployed on Streamlit Community Cloud.
"""

from datetime import date, time
from typing import Dict, List, Tuple, Optional
import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

# ---------------------------------------------------------------------------
# 1. PAGE CONFIGURATION
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Amour Du Cafè — Brewed with Love",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------------------------
# 2. GLOBAL STYLES
# ---------------------------------------------------------------------------
GLOBAL_CSS = """
<style>
/* ---------- Google Fonts ---------- */
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Playfair+Display:wght@500;600;700;800&family=Poppins:wght@300;400;500;600;700&family=Italianno&display=swap');

/* ---------- DARK MODE LOCK ---------- */
:root { 
    color-scheme: dark only;
    forced-color-adjust: none;
}
@media (prefers-color-scheme: dark), (prefers-color-scheme: light) {
    html, body, .stApp {
        background-color: #0A0806 !important;
        color: #FFFFFF !important;
    }
}
[data-testid="stAppViewContainer"],
[data-testid="stHeader"],
[data-testid="stMain"],
[data-testid="stSidebar"],
section.main,
.main {
    background-color: transparent !important;
    color: #FFFFFF !important;
}
[data-testid="stMarkdownContainer"],
[data-testid="stMarkdownContainer"] *,
.stMarkdown, .stMarkdown *,
.stText, .stText *,
p, span, div, label, h1, h2, h3, h4, h5, h6 {
    color: #FFFFFF !important;
}
html { filter: none !important; -webkit-filter: none !important; }
[data-theme="light"], [data-theme="light"] body, [data-theme="light"] .stApp {
    background: #0A0806 !important;
    color: #FFFFFF !important;
}

/* ---------- Design Tokens ---------- */
:root {
    --black:         #0A0806;
    --black-soft:    #121010;
    --black-card:    #1A1614;
    --black-elev:    #221E1B;
    --border:        rgba(212, 160, 86, 0.18);
    --border-soft:   rgba(255, 255, 255, 0.06);
    --white:         #FFFFFF;
    --white-soft:    #F5F5F5;
    --white-muted:   #B8B0A8;
    --white-dim:     #8A8480;
    --gold:          #D4A056;
    --gold-light:    #E8C88A;
    --gold-glow:     rgba(212, 160, 86, 0.35);
    --terracotta:    #C97B5A;
    --terracotta-dk: #A85E3D;
    --sage:          #8FA07A;
    --shadow-sm:     0 4px 14px rgba(0, 0, 0, 0.4);
    --shadow-md:     0 10px 30px rgba(0, 0, 0, 0.5);
    --shadow-lg:     0 20px 50px rgba(0, 0, 0, 0.6);
    --shadow-xl:     0 30px 70px rgba(0, 0, 0, 0.7);
    --shadow-gold:   0 10px 40px rgba(212, 160, 86, 0.3);
    --radius-sm:     12px;
    --radius-md:     18px;
    --radius-lg:     28px;
    --radius-pill:   999px;
    --transition:    all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
}

/* ---------- Hide Streamlit chrome ---------- */
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
[data-testid="stHeader"] { display: none; }

/* ---------- Base ---------- */
html, body, [class*="css"] {
    font-family: 'Poppins', -apple-system, BlinkMacSystemFont, sans-serif;
    color: var(--white);
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}
.stApp {
    background: transparent !important;
    color: var(--white);
}
.block-container {
    padding-top: 1rem;
    padding-bottom: 2rem;
    max-width: 1320px;
}

/* ---------- Typography ---------- */
h1, h2, h3, h4 {
    font-family: 'Playfair Display', Georgia, serif;
    color: var(--white);
    letter-spacing: 0.3px;
    font-weight: 700;
}

/* ---------- Custom Coffee Cursor ---------- */
body, .stApp {
    cursor: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 26 26"><circle cx="13" cy="13" r="8" fill="%23D4A056" stroke="%230A0806" stroke-width="1.5"/><ellipse cx="13" cy="13" rx="3" ry="6" fill="%230A0806" opacity="0.6"/></svg>') 13 13, auto;
}
.stButton > button, a, .gallery-tile {
    cursor: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 30 30"><text y="22" font-size="20">☕</text></svg>') 15 15, pointer;
}

/* ---------- Scroll Progress Bar ---------- */
.scroll-progress {
    position: fixed;
    top: 0; left: 0;
    height: 3px;
    background: linear-gradient(90deg, var(--terracotta), var(--gold), var(--gold-light));
    z-index: 99999;
    width: 0%;
    box-shadow: 0 0 12px var(--gold-glow);
    transition: width 0.1s ease-out;
}

/* ---------- PAGE BACKGROUNDS ---------- */
.page-bg-home {
    position: fixed;
    top: 0; left: 0;
    width: 100vw; height: 100vh;
    z-index: -2;
    background:
        linear-gradient(160deg, rgba(10, 8, 6, 0.92) 0%, rgba(18, 16, 16, 0.88) 50%, rgba(10, 8, 6, 0.94) 100%),
        url('https://images.unsplash.com/photo-1447933601403-0c6688de566e?w=1920&q=80') center/cover fixed;
    pointer-events: none;
}
.page-bg-menu {
    position: fixed;
    top: 0; left: 0;
    width: 100vw; height: 100vh;
    z-index: -2;
    background:
        linear-gradient(160deg, rgba(10, 8, 6, 0.94) 0%, rgba(18, 16, 16, 0.90) 50%, rgba(10, 8, 6, 0.95) 100%),
        url('https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=1920&q=80') center/cover fixed;
    pointer-events: none;
}
.page-bg-reviews {
    position: fixed;
    top: 0; left: 0;
    width: 100vw; height: 100vh;
    z-index: -2;
    background:
        linear-gradient(160deg, rgba(10, 8, 6, 0.93) 0%, rgba(18, 16, 16, 0.90) 50%, rgba(10, 8, 6, 0.94) 100%),
        url('https://images.unsplash.com/photo-1521017432531-fbd92d768814?w=1920&q=80') center/cover fixed;
    pointer-events: none;
}
.page-bg-contact {
    position: fixed;
    top: 0; left: 0;
    width: 100vw; height: 100vh;
    z-index: -2;
    background:
        linear-gradient(160deg, rgba(10, 8, 6, 0.94) 0%, rgba(18, 16, 16, 0.90) 50%, rgba(10, 8, 6, 0.95) 100%),
        url('https://images.unsplash.com/photo-1554118811-1e0d58224f24?w=1920&q=80') center/cover fixed;
    pointer-events: none;
}

/* ---------- Hero ---------- */
.hero {
    position: relative;
    background:
        linear-gradient(135deg, rgba(10, 8, 6, 0.94) 0%, rgba(18, 16, 16, 0.90) 50%, rgba(10, 8, 6, 0.92) 100%),
        url('https://images.unsplash.com/photo-1447933601403-0c6688de566e?w=1600&q=80') center/cover;
    padding: 100px 40px 90px;
    border-radius: var(--radius-lg);
    text-align: center;
    margin-bottom: 30px;
    overflow: hidden;
    box-shadow: var(--shadow-xl);
    border: 1px solid var(--border);
}
.hero::before {
    content: "";
    position: absolute;
    top: -60%; left: -60%;
    width: 220%; height: 220%;
    background:
        radial-gradient(circle at 30% 40%, rgba(212, 160, 86, 0.25), transparent 45%),
        radial-gradient(circle at 70% 70%, rgba(201, 123, 90, 0.20), transparent 45%);
    animation: float 18s ease-in-out infinite;
    pointer-events: none;
}
@keyframes float {
    0%, 100% { transform: translate(0, 0) rotate(0deg); }
    33%      { transform: translate(-20px, -25px) rotate(4deg); }
    66%      { transform: translate(15px, -15px) rotate(-3deg); }
}
.hero-content { position: relative; z-index: 2; }
.hero-logo {
    display: block;
    max-width: 140px;
    max-height: 140px;
    margin: 0 auto 22px auto;
    border-radius: 50%;
    filter: drop-shadow(0 10px 30px rgba(212, 160, 86, 0.5));
    animation: logoFade 1.4s ease-out;
    border: 3px solid rgba(212, 160, 86, 0.5);
}
.hero-logo-fallback {
    display: block;
    font-size: 4rem;
    margin-bottom: 14px;
    filter: drop-shadow(0 8px 24px rgba(212, 160, 86, 0.5));
}
@keyframes logoFade {
    from { opacity: 0; transform: translateY(-20px) scale(0.95); }
    to   { opacity: 1; transform: translateY(0) scale(1); }
}
.hero .eyebrow {
    display: inline-block;
    color: var(--gold-light);
    font-size: 0.78rem;
    letter-spacing: 5px;
    text-transform: uppercase;
    margin-bottom: 12px;
    font-weight: 500;
}
.hero h1 {
    color: var(--white);
    font-size: clamp(2.6rem, 6vw, 5rem);
    margin: 0;
    letter-spacing: 4px;
    text-shadow: 0 4px 30px rgba(212, 160, 86, 0.4), 2px 6px 24px rgba(0, 0, 0, 0.8);
    font-weight: 800;
    line-height: 1.05;
}
.hero .script {
    font-family: 'Italianno', cursive;
    font-size: clamp(2rem, 4vw, 3.2rem);
    color: var(--gold-light);
    display: block;
    margin: -8px 0 4px 0;
    letter-spacing: 1px;
    text-shadow: 0 0 30px rgba(212, 160, 86, 0.6);
    line-height: 1;
}
.hero .divider {
    width: 120px; height: 2px;
    background: linear-gradient(90deg, transparent, var(--gold), var(--gold-light), var(--gold), transparent);
    margin: 26px auto;
    position: relative;
    box-shadow: 0 0 20px var(--gold-glow);
}
.hero .divider::before {
    content: "☕";
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    background: #0A0806;
    padding: 0 12px;
    font-size: 0.9rem;
    color: var(--gold);
}
.hero p {
    color: var(--white-soft);
    font-size: clamp(1rem, 1.6vw, 1.3rem);
    font-style: italic;
    font-family: 'Cormorant Garamond', serif;
    font-weight: 500;
    margin: 0 auto;
    letter-spacing: 1.5px;
    max-width: 640px;
    line-height: 1.6;
}
.hero .badge {
    display: inline-block;
    margin-top: 30px;
    padding: 10px 26px;
    border: 1px solid rgba(212, 160, 86, 0.55);
    border-radius: var(--radius-pill);
    color: var(--gold-light);
    font-size: 0.8rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    background: rgba(212, 160, 86, 0.10);
    backdrop-filter: blur(10px);
    font-weight: 500;
}

/* ---------- Section Header ---------- */
.section-header {
    text-align: center;
    margin: 65px 0 40px 0;
    position: relative;
}
.section-header .kicker {
    display: inline-block;
    font-family: 'Italianno', cursive;
    font-size: 1.8rem;
    color: var(--gold);
    margin-bottom: -6px;
    line-height: 1;
    text-shadow: 0 0 20px rgba(212, 160, 86, 0.4);
}
.section-header h2 {
    font-size: clamp(1.7rem, 3.2vw, 2.5rem);
    margin: 0;
    display: inline-block;
    position: relative;
    padding-bottom: 18px;
    font-weight: 700;
    color: var(--white);
}
.section-header h2::after {
    content: "";
    position: absolute;
    bottom: 0; left: 50%;
    transform: translateX(-50%);
    width: 70px; height: 3px;
    background: linear-gradient(90deg, var(--terracotta), var(--gold), var(--terracotta));
    border-radius: 3px;
    box-shadow: 0 0 16px var(--gold-glow);
}
.section-header .subtitle {
    display: block;
    color: var(--white-muted);
    font-size: 0.95rem;
    margin-top: 14px;
    letter-spacing: 1.5px;
    font-style: italic;
    font-family: 'Cormorant Garamond', serif;
    font-weight: 500;
}

/* ---------- Sub-category Headers ---------- */
.sub-category {
    margin: 22px 0 18px 0;
    padding-left: 14px;
    position: relative;
    border-left: 3px solid var(--gold);
}
.sub-category h3 {
    font-family: 'Playfair Display', serif;
    font-size: 1.35rem;
    color: var(--gold-light);
    margin: 0;
    letter-spacing: 1.5px;
    text-shadow: 0 0 16px rgba(212, 160, 86, 0.35);
    font-weight: 600;
}
.sub-category::after {
    content: "";
    position: absolute;
    bottom: -8px;
    left: 14px;
    width: 40px;
    height: 2px;
    background: linear-gradient(90deg, var(--gold), transparent);
}

/* ---------- Menu card ---------- */
.menu-card {
    background: linear-gradient(135deg, rgba(26, 22, 20, 0.85) 0%, rgba(34, 30, 27, 0.85) 100%);
    backdrop-filter: blur(12px);
    border-radius: var(--radius-md);
    padding: 22px 26px;
    margin-bottom: 16px;
    box-shadow: var(--shadow-sm);
    border-left: 4px solid var(--gold);
    transition: var(--transition);
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 16px;
    position: relative;
    overflow: hidden;
    border-top: 1px solid var(--border-soft);
    border-right: 1px solid var(--border-soft);
    border-bottom: 1px solid var(--border-soft);
}
.menu-card::before {
    content: "";
    position: absolute;
    top: 0; left: 0;
    width: 4px; height: 100%;
    background: linear-gradient(180deg, var(--gold), var(--terracotta));
    transform: scaleY(0);
    transform-origin: top;
    transition: transform 0.4s ease;
    box-shadow: 0 0 20px var(--gold-glow);
}
.menu-card:hover {
    transform: translateX(8px);
    box-shadow: var(--shadow-md);
    border-left-color: transparent;
}
.menu-card:hover::before { transform: scaleY(1); }
.menu-card .menu-info h4 {
    margin: 0 0 4px 0;
    font-size: 1.15rem;
    color: var(--white);
    font-weight: 600;
}
.menu-card .menu-info p {
    margin: 0;
    color: var(--white-muted);
    font-style: italic;
    font-family: 'Cormorant Garamond', serif;
    font-size: 1rem;
}
.menu-card .price {
    font-family: 'Playfair Display', serif;
    font-weight: 700;
    font-size: 1.2rem;
    color: var(--gold-light);
    white-space: nowrap;
    padding: 6px 14px;
    background: rgba(212, 160, 86, 0.10);
    border-radius: var(--radius-pill);
    border: 1px solid var(--border);
}
.menu-card .price.ask-us {
    color: var(--white-muted);
    font-size: 1rem;
    font-style: italic;
    background: rgba(184, 176, 168, 0.10);
    border-color: var(--border-soft);
}

/* ---------- Info box ---------- */
.info-box {
    background: linear-gradient(160deg, rgba(26, 22, 20, 0.88) 0%, rgba(34, 30, 27, 0.88) 100%);
    backdrop-filter: blur(12px);
    padding: 36px;
    border-radius: var(--radius-md);
    box-shadow: var(--shadow-sm);
    height: 100%;
    border-top: 4px solid var(--sage);
    transition: var(--transition);
    position: relative;
    overflow: hidden;
    border-left: 1px solid var(--border-soft);
    border-right: 1px solid var(--border-soft);
    border-bottom: 1px solid var(--border-soft);
}
.info-box::before {
    content: "";
    position: absolute;
    top: -50px; right: -50px;
    width: 140px; height: 140px;
    background: radial-gradient(circle, rgba(212, 160, 86, 0.10), transparent 70%);
    border-radius: 50%;
    pointer-events: none;
}
.info-box:hover {
    box-shadow: var(--shadow-md);
    transform: translateY(-4px);
    border-top-color: var(--gold);
}
.info-box h3 {
    color: var(--white);
    font-size: 1.45rem;
    margin-top: 0;
    margin-bottom: 18px;
    display: flex;
    align-items: center;
    gap: 10px;
}
.info-box p {
    color: var(--white-soft);
    font-size: 1rem;
    line-height: 1.85;
    margin: 0 0 14px 0;
}
.info-box p b { color: var(--gold-light); }

/* ---------- Review card ---------- */
.review-card {
    background: linear-gradient(135deg, rgba(26, 22, 20, 0.90) 0%, rgba(34, 30, 27, 0.90) 100%);
    backdrop-filter: blur(12px);
    padding: 28px;
    border-radius: var(--radius-md);
    box-shadow: var(--shadow-sm);
    margin-bottom: 18px;
    border-left: 4px solid var(--gold);
    transition: var(--transition);
    position: relative;
    border-top: 1px solid var(--border-soft);
    border-right: 1px solid var(--border-soft);
    border-bottom: 1px solid var(--border-soft);
}
.review-card::after {
    content: "\\201C";
    position: absolute;
    top: 10px; right: 24px;
    font-family: 'Playfair Display', serif;
    font-size: 5rem;
    color: rgba(212, 160, 86, 0.15);
    line-height: 1;
    pointer-events: none;
}
.review-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-md);
    border-left-color: var(--terracotta);
}
.review-card .reviewer {
    margin: 0;
    color: var(--white);
    font-family: 'Playfair Display', serif;
    font-size: 1.15rem;
    font-weight: 600;
}
.review-card .stars {
    color: var(--gold);
    font-size: 1.15rem;
    margin: 8px 0 12px 0;
    letter-spacing: 3px;
    text-shadow: 0 0 14px rgba(212, 160, 86, 0.5);
}
.review-card .review-text {
    color: var(--white-soft);
    margin: 0;
    font-style: italic;
    line-height: 1.7;
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.08rem;
    font-weight: 500;
}

/* ---------- Special card ---------- */
.special-card {
    background: linear-gradient(160deg, rgba(26, 22, 20, 0.88) 0%, rgba(34, 30, 27, 0.88) 100%);
    backdrop-filter: blur(12px);
    padding: 36px 26px;
    border-radius: var(--radius-md);
    text-align: center;
    box-shadow: var(--shadow-sm);
    border-top: 4px solid var(--terracotta);
    transition: var(--transition);
    height: 100%;
    position: relative;
    overflow: hidden;
    border-left: 1px solid var(--border-soft);
    border-right: 1px solid var(--border-soft);
    border-bottom: 1px solid var(--border-soft);
}
.special-card::before {
    content: "";
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: radial-gradient(circle at 50% 0%, rgba(212, 160, 86, 0.15), transparent 60%);
    pointer-events: none;
    opacity: 0;
    transition: opacity 0.4s ease;
}
.special-card:hover::before { opacity: 1; }
.special-card:hover {
    transform: translateY(-10px) scale(1.02);
    box-shadow: var(--shadow-lg), var(--shadow-gold);
    border-top-color: var(--gold);
}
.special-card .icon {
    font-size: 2.8rem;
    display: block;
    margin-bottom: 16px;
    filter: drop-shadow(0 4px 16px rgba(212, 160, 86, 0.5));
}
.special-card h3 {
    margin: 0 0 12px 0;
    color: var(--white);
    font-size: 1.3rem;
}
.special-card p {
    color: var(--white-muted);
    margin: 0 0 18px 0;
    line-height: 1.65;
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.05rem;
    font-weight: 500;
}
.special-card .price {
    font-family: 'Playfair Display', serif;
    font-weight: 700;
    color: var(--gold-light);
    font-size: 1.2rem;
    display: inline-block;
    padding: 6px 18px;
    background: rgba(212, 160, 86, 0.12);
    border-radius: var(--radius-pill);
    border: 1px solid var(--border);
}

/* ---------- Gallery Tile ---------- */
.gallery-tile {
    position: relative;
    aspect-ratio: 1 / 1;
    width: 100%;
    max-width: 320px;
    margin: 0 auto 8px auto;
    border-radius: var(--radius-md);
    overflow: hidden;
    box-shadow: var(--shadow-sm);
    transition: var(--transition);
    display: flex;
    align-items: flex-end;
    justify-content: flex-start;
    padding: 18px;
    color: #FFF;
    cursor: pointer;
    background-size: cover;
    background-position: center;
    border: 1px solid var(--border-soft);
}
.gallery-tile::after {
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(180deg, transparent 30%, rgba(10, 8, 6, 0.9) 100%);
    z-index: 1;
}
.gallery-tile:hover {
    transform: scale(1.05);
    box-shadow: var(--shadow-lg), var(--shadow-gold);
    border-color: var(--gold);
}
.gallery-tile span {
    position: relative;
    z-index: 2;
    font-family: 'Playfair Display', serif;
    font-weight: 600;
    font-size: 1rem;
    letter-spacing: 0.5px;
    text-shadow: 1px 2px 10px rgba(0,0,0,0.9);
    color: var(--white);
}

/* ---------- Video tile support ---------- */
.gallery-tile video {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    object-fit: cover;
    z-index: 0;
    border-radius: inherit;
}
.gallery-tile.has-video::after {
    background: linear-gradient(180deg, transparent 40%, rgba(10, 8, 6, 0.85) 100%);
}

.grad-1 { background: linear-gradient(135deg, #6B3A28, #2A1A12); }
.grad-2 { background: linear-gradient(135deg, #3E4A30, #1A1F14); }
.grad-3 { background: linear-gradient(135deg, #8C6A2E, #3A2410); }
.grad-4 { background: linear-gradient(135deg, #1F120B, #4A2820); }
.grad-5 { background: linear-gradient(135deg, #3A2418, #7A5028); }
.grad-6 { background: linear-gradient(135deg, #2A1A12, #3E4A30); }

/* ---------- Buttons ---------- */
.stButton > button {
    background: linear-gradient(135deg, rgba(34, 30, 27, 0.95), rgba(168, 94, 61, 0.95));
    color: #FFFFFF;
    border: 1px solid var(--border);
    padding: 12px 28px;
    border-radius: var(--radius-pill);
    font-family: 'Poppins', sans-serif;
    font-weight: 500;
    font-size: 0.92rem;
    letter-spacing: 0.8px;
    transition: var(--transition);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.5);
    width: 100%;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(8px);
}
.stButton > button::before {
    content: "";
    position: absolute;
    top: 0; left: -100%;
    width: 100%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(212, 160, 86, 0.25), transparent);
    transition: left 0.6s ease;
}
.stButton > button:hover::before { left: 100%; }
.stButton > button:hover {
    background: linear-gradient(135deg, var(--terracotta), var(--gold));
    transform: translateY(-3px);
    box-shadow: 0 10px 30px var(--gold-glow);
    color: #0A0806;
    border-color: var(--gold);
}
.stButton > button:focus:not(:active) {
    color: #FFFFFF;
    border-color: var(--gold);
}
.stButton > button p, .stButton > button span, .stButton > button div {
    color: inherit !important;
}

/* ---------- Form Inputs ---------- */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div > div {
    border-radius: var(--radius-sm) !important;
    border: 1px solid var(--border) !important;
    background: rgba(26, 22, 20, 0.85) !important;
    color: var(--white) !important;
    font-family: 'Poppins', sans-serif !important;
    backdrop-filter: blur(8px);
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: var(--gold) !important;
    box-shadow: 0 0 0 3px rgba(212, 160, 86, 0.20) !important;
}
.stTextInput > div > div > input::placeholder,
.stTextArea > div > div > textarea::placeholder {
    color: var(--white-dim) !important;
}
.stTextInput label, .stTextArea label, .stSelectbox label, .stSlider label {
    color: var(--white) !important;
}
.stSelectbox [data-baseweb="select"] > div {
    background: rgba(26, 22, 20, 0.85) !important;
    border-color: var(--border) !important;
    color: var(--white) !important;
}

/* ---------- Tabs ---------- */
.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
    border-bottom: 1px solid var(--border-soft);
    padding-bottom: 8px;
    justify-content: center;
    background: transparent;
    flex-wrap: wrap;
}
.stTabs [data-baseweb="tab"] {
    background: rgba(26, 22, 20, 0.7);
    backdrop-filter: blur(8px);
    border-radius: var(--radius-pill);
    padding: 10px 26px;
    font-family: 'Poppins', sans-serif;
    font-weight: 500;
    font-size: 0.95rem;
    color: var(--white-muted);
    transition: var(--transition);
    border: 1px solid var(--border-soft);
}
.stTabs [data-baseweb="tab"]:hover { color: var(--gold-light); }
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, var(--terracotta-dk), var(--gold)) !important;
    color: #0A0806 !important;
    box-shadow: 0 4px 20px var(--gold-glow);
    border-color: var(--gold);
}
.stTabs [data-baseweb="tab-highlight"] { background: transparent; }
.stTabs [data-baseweb="tab-panel"] { color: var(--white); }

/* ---------- Expander ---------- */
.streamlit-expanderHeader, [data-testid="stExpander"] summary {
    font-family: 'Poppins', sans-serif;
    font-weight: 500;
    color: var(--white) !important;
    background: rgba(26, 22, 20, 0.85) !important;
    border-radius: var(--radius-sm) !important;
}
[data-testid="stExpander"] {
    background: rgba(26, 22, 20, 0.85) !important;
    border: 1px solid var(--border-soft) !important;
    border-radius: var(--radius-md) !important;
    backdrop-filter: blur(10px);
}
[data-testid="stExpander"] * { color: var(--white); }

/* ---------- Alerts ---------- */
.stAlert {
    background: rgba(34, 30, 27, 0.9) !important;
    color: var(--white) !important;
    border-radius: var(--radius-sm) !important;
    backdrop-filter: blur(8px);
}
.stAlert * { color: var(--white) !important; }

hr { border-color: var(--border-soft); }

/* ---------- Footer ---------- */
.footer {
    background:
        linear-gradient(135deg, rgba(10, 8, 6, 0.97) 0%, rgba(18, 16, 16, 0.96) 100%),
        url('https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=1600&q=80') center/cover;
    color: var(--white-muted);
    padding: 60px 30px 40px 30px;
    border-radius: var(--radius-lg);
    text-align: center;
    margin-top: 70px;
    box-shadow: var(--shadow-lg);
    position: relative;
    overflow: hidden;
    border: 1px solid var(--border);
}
.footer::before {
    content: "";
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 3px;
    background: linear-gradient(90deg, transparent, var(--gold), var(--terracotta), var(--gold), transparent);
    box-shadow: 0 0 20px var(--gold-glow);
}
.footer h3 {
    color: var(--white);
    font-size: 2rem;
    margin: 0 0 10px 0;
    letter-spacing: 3px;
}
.footer .script {
    font-family: 'Italianno', cursive;
    font-size: 2.2rem;
    color: var(--gold-light);
    display: block;
    margin-bottom: 4px;
    text-shadow: 0 0 30px rgba(212, 160, 86, 0.5);
}
.footer .tagline {
    font-style: italic;
    color: var(--white-muted);
    margin: 0 0 30px 0;
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.15rem;
    font-weight: 500;
    letter-spacing: 1px;
}
.footer .socials {
    display: flex;
    justify-content: center;
    gap: 16px;
    flex-wrap: wrap;
    margin-bottom: 30px;
}
.footer .socials a {
    color: var(--white-soft);
    text-decoration: none;
    padding: 10px 22px;
    border: 1px solid var(--border);
    border-radius: var(--radius-pill);
    font-size: 0.88rem;
    transition: var(--transition);
    background: rgba(212, 160, 86, 0.06);
    backdrop-filter: blur(6px);
}
.footer .socials a:hover {
    background: rgba(212, 160, 86, 0.20);
    border-color: var(--gold);
    color: var(--gold-light);
    transform: translateY(-3px);
    box-shadow: var(--shadow-gold);
}
.footer .copyright {
    font-size: 0.82rem;
    color: var(--white-dim);
    margin: 0;
    letter-spacing: 0.8px;
}

/* ---------- Newsletter ---------- */
.newsletter-box {
    background: linear-gradient(135deg, rgba(26, 22, 20, 0.9), rgba(34, 30, 27, 0.9));
    border: 1.5px dashed var(--gold);
    border-radius: var(--radius-md);
    padding: 30px;
    text-align: center;
    margin-top: 24px;
    backdrop-filter: blur(8px);
}
.newsletter-box h3 {
    margin: 0 0 8px 0;
    color: var(--white);
    font-size: 1.3rem;
}
.newsletter-box p {
    color: var(--white-muted);
    margin: 0 0 16px 0;
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.05rem;
    font-weight: 500;
}

/* ---------- Map ---------- */
.map-wrap {
    border-radius: var(--radius-md);
    overflow: hidden;
    box-shadow: var(--shadow-md);
    border: 4px solid var(--black-elev);
    transition: var(--transition);
}
.map-wrap:hover { box-shadow: var(--shadow-lg), var(--shadow-gold); }

/* ---------- Stats bar ---------- */
.stats-bar {
    display: flex;
    justify-content: center;
    gap: 60px;
    flex-wrap: wrap;
    padding: 36px 24px;
    background: linear-gradient(135deg, rgba(26, 22, 20, 0.9) 0%, rgba(34, 30, 27, 0.9) 100%);
    backdrop-filter: blur(12px);
    border-radius: var(--radius-md);
    box-shadow: var(--shadow-sm);
    margin: 30px 0 10px 0;
    border: 1px solid var(--border);
}
.stat-item { text-align: center; min-width: 120px; }
.stat-item .num {
    display: block;
    font-family: 'Playfair Display', serif;
    font-size: 2.2rem;
    font-weight: 700;
    color: var(--gold-light);
    line-height: 1;
    margin-bottom: 6px;
    text-shadow: 0 0 24px rgba(212, 160, 86, 0.5);
}
.stat-item .lbl {
    font-size: 0.78rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--white-muted);
    font-weight: 500;
}

/* ---------- Marquee ---------- */
.marquee-strip {
    background: linear-gradient(90deg, rgba(26, 22, 20, 0.9), rgba(34, 30, 27, 0.9), rgba(26, 22, 20, 0.9));
    backdrop-filter: blur(8px);
    color: var(--gold-light);
    padding: 14px 0;
    border-radius: var(--radius-pill);
    overflow: hidden;
    margin: 40px 0 20px 0;
    box-shadow: var(--shadow-sm);
    white-space: nowrap;
    border: 1px solid var(--border);
}
.marquee-strip .inner {
    display: inline-block;
    animation: marquee 30s linear infinite;
    font-family: 'Playfair Display', serif;
    letter-spacing: 3px;
    font-size: 0.95rem;
    text-transform: uppercase;
}
.marquee-strip .inner span { margin: 0 30px; }
@keyframes marquee {
    0%   { transform: translateX(0); }
    100% { transform: translateX(-50%); }
}

/* ---------- Fade-in ---------- */
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
}
.main-content > * { animation: fadeInUp 0.6s ease-out; }

/* ---------- Slider ---------- */
.stSlider [data-baseweb="slider"] div[role="slider"] {
    background-color: var(--gold) !important;
    box-shadow: 0 0 12px var(--gold-glow);
}
.stSlider [data-baseweb="slider"] > div > div {
    background: var(--gold) !important;
}

/* ---------- Mobile ---------- */
@media (max-width: 768px) {
    .block-container { padding-left: 1rem; padding-right: 1rem; }
    .hero { padding: 60px 22px; border-radius: var(--radius-md); }
    .hero h1 { letter-spacing: 2px; }
    .section-header { margin: 42px 0 26px 0; }
    .card, .info-box, .special-card { padding: 24px; }
    .menu-card {
        flex-direction: column;
        align-items: flex-start;
        gap: 8px;
        padding: 18px;
    }
    .menu-card .price { align-self: flex-end; }
    .footer { padding: 40px 20px 30px 20px; }
    .stButton > button { padding: 11px 20px; font-size: 0.88rem; }
    .stTabs [data-baseweb="tab"] { padding: 7px 14px; font-size: 0.82rem; }
    .gallery-tile {
        max-width: 100%;
        aspect-ratio: 1 / 1;
        padding: 14px;
        margin-bottom: 6px;
    }
    .stats-bar { gap: 30px; padding: 28px 18px; }
    .stat-item .num { font-size: 1.8rem; }
}
</style>
"""

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# 3. SCROLL PROGRESS + ANIMATED COUNTERS
# ---------------------------------------------------------------------------
components.html(
    """
    <script>
    (function attachProgress() {
        const doc = window.parent.document;
        let bar = doc.querySelector('.scroll-progress');
        if (!bar) {
            bar = doc.createElement('div');
            bar.className = 'scroll-progress';
            doc.body.appendChild(bar);
        }
        const update = () => {
            const h = doc.documentElement;
            const top = h.scrollTop || doc.body.scrollTop;
            const sh = h.scrollHeight - h.clientHeight;
            const pct = sh > 0 ? (top / sh) * 100 : 0;
            bar.style.width = pct + '%';
        };
        doc.addEventListener('scroll', update, { passive: true });
        window.parent.addEventListener('scroll', update, { passive: true });
        update();
    })();

    function animateCounter(el) {
        if (el.dataset.done) return;
        el.dataset.done = 'true';
        const target = parseFloat(el.dataset.target) || 0;
        const suffix = el.dataset.suffix || '';
        const decimals = parseInt(el.dataset.decimals || '0');

        if (target < 10 && decimals > 0) {
            let current = 0;
            const steps = 40;
            const inc = target / steps;
            let i = 0;
            const timer = setInterval(() => {
                i++;
                current += inc;
                if (i >= steps) { current = target; clearInterval(timer); }
                el.textContent = current.toFixed(decimals) + suffix;
            }, 30);
            return;
        }

        let current = 0;
        const duration = 1500;
        const start = performance.now();
        const tick = (now) => {
            const t = Math.min((now - start) / duration, 1);
            const eased = 1 - Math.pow(1 - t, 3);
            current = target * eased;
            if (target >= 1000) {
                el.textContent = Math.floor(current).toLocaleString() + suffix;
            } else {
                el.textContent = Math.floor(current) + suffix;
            }
            if (t < 1) requestAnimationFrame(tick);
            else {
                el.textContent = (target >= 1000
                    ? Math.floor(target).toLocaleString()
                    : Math.floor(target)) + suffix;
            }
        };
        requestAnimationFrame(tick);
    }

    function scanAndAnimate() {
        const doc = window.parent.document;
        doc.querySelectorAll('.stat-item .num[data-target]').forEach((el) => {
            const rect = el.getBoundingClientRect();
            if (rect.top < window.parent.innerHeight && !el.dataset.done) {
                animateCounter(el);
            }
        });
    }

    const doc = window.parent.document;
    doc.addEventListener('scroll', scanAndAnimate, { passive: true });
    setTimeout(scanAndAnimate, 500);
    setTimeout(scanAndAnimate, 1200);
    setTimeout(scanAndAnimate, 2500);
    </script>
    """,
    height=0,
)


# ---------------------------------------------------------------------------
# 4. STATIC DATA
# ---------------------------------------------------------------------------
@st.cache_data(show_spinner=False)
def get_menu_data():
    return {
        "Appetizers": [
            ("Dynamite Chicken", "Crispy chicken in spicy dynamite sauce", 350.00),
            ("Dynamite Shrimps", "Juicy shrimp with creamy dynamite glaze", 650.00),
            ("French Fries", "Golden crispy fries", 200.00),
            ("Sausages (Chicken / Buff)", "Grilled sausages, your choice", 240.00),
        ],
        "Mo : Mo": [
            ("Steam Momo (Buff / Chicken)", "Classic steamed dumplings", 170.00),
            ("Fried Momo (Buff / Chicken)", "Golden pan-fried dumplings", 200.00),
            ("Chilly Momo (Buff / Chicken)", "Spicy tossed with peppers", 250.00),
            ("Jhol Momo (Buff / Chicken)", "In warm spiced soup broth", 200.00),
            ("Kothey Momo (Buff / Chicken)", "Pan-seared, juicy inside", 300.00),
        ],
        "Spicy Zone": [
            ("Ramen Bowl", "Hearty Japanese-style noodle bowl", 700.00),
            ("Hot & Spicy Wings (3 pcs)", "Fiery buffalo-glazed wings", 350.00),
            ("Hot & Spicy Wings (5 pcs)", "Fiery buffalo-glazed wings — large", 450.00),
        ],
        "Brunch": [
            ("Cheese Poached Egg", "Poached eggs with hollandaise & cheese", 300.00),
            ("Blueberry Smoothie Bowl", "Chilled berry bowl with toppings", 200.00),
            ("Croissant Chicken & Cheese", "Flaky croissant with chicken & cheese", 300.00),
            ("Strawberry Parfait", "Layered yogurt, berries & granola", 200.00),
        ],
        "Italian Corner": [
            ("Penne Alfredo", "Creamy white sauce pasta", 400.00),
            ("Penne Arrabiata", "Spicy tomato pasta", 300.00),
            ("Penne Pesto", "Basil pesto pasta", 450.00),
            ("Chicken Pizza", "Wood-fired with grilled chicken", 650.00),
            ("Veg Pizza", "Fresh garden vegetables", 600.00),
            ("Mixed Pizza", "Loaded with chicken & veggies", 800.00),
        ],
        "Sandwiches & Rolls": [
            ("Croque Monsieur", "Classic French grilled ham & cheese", 300.00),
            ("Mexican Chicken Wrap", "Zesty wrap with Mexican spices", 350.00),
            ("Chicken Roll", "Wrapped with tender chicken", 230.00),
            ("Egg Roll", "Crispy roll with egg filling", 200.00),
            ("Keema Roll", "Spiced minced meat roll", 220.00),
            ("Cheese Sandwich", "Grilled with melted cheese", 250.00),
        ],
        "Burger Joint": [
            ("Buff Smash Burger", "Juicy smashed buff patty", 300.00),
            ("Zinger Chicken Burger", "Crispy spicy chicken fillet", 300.00),
            ("Devil's Chicken Burger", "Fiery chicken burger", 450.00),
        ],
        "Espresso Based Drinks": [
            ("Espresso", "Bold and pure", 120.00),
            ("Americano", "Smooth black coffee", 150.00),
            ("Cafe Latte", "Smooth and creamy", 180.00),
            ("Cappuccino", "Classic Italian style", 180.00),
            ("Cortado", "Equal parts espresso & milk", 180.00),
            ("Cafe Mocha", "Chocolate espresso delight", 250.00),
            ("Flat White", "Velvety microfoam", 200.00),
        ],
        "Hot Flavored Drinks": [
            ("Flavored Cafe Latte", "Latte with your choice of flavor", 250.00),
            ("Latte Macchiato", "Layered milk & espresso", 230.00),
            ("Americano Royale", "Premium americano", 220.00),
            ("Tiramisu Latte", "Dessert-inspired latte", 300.00),
            ("Hot Chocolate", "Belgian chocolate", 180.00),
        ],
        "Amour's Signature": [
            ("Caramel Sticky Mocha", "Our signature caramel mocha", 300.00),
        ],
        "Iced Coffee": [
            ("Iced Americano", "Refreshing and bold", 150.00),
            ("Iced Latte", "Chilled smooth latte", 180.00),
            ("Iced Mocha", "Chilled chocolate espresso", 250.00),
            ("Iced Tiramisu Latte", "Dessert-inspired iced latte", 300.00),
            ("Iced Strawberry Latte", "Strawberry-infused iced latte", 250.00),
            ("Espresso Shakerato", "Shaken espresso over ice", 150.00),
        ],
        "Slow Bar — Nepali Specialty Coffee": [
            ("Washed", "Nepali washed process", 250.00),
            ("Honey", "Nepali honey process", 300.00),
            ("Natural", "Nepali natural process", 300.00),
            ("Anaerobic", "Nepali anaerobic fermentation", 300.00),
        ],
        "Slow Bar — Specialty Coffee Around The World": [
            ("Washed", "Washed process — international", 500.00),
            ("Honey", "Honey process — international", 550.00),
            ("Natural", "Natural process — international", 550.00),
            ("Anaerobic", "Anaerobic fermentation — international", 550.00),
        ],
        "Coffee Alternatives": [
            ("Peach Iced Tea", "Refreshing peach tea", 200.00),
            ("Lemon Iced Tea", "Zesty lemon iced tea", 200.00),
            ("Apple Iced Tea", "Crisp apple iced tea", 200.00),
            ("Hot Lemon With Honey", "Warm soothing classic", 100.00),
        ],
        "Mojitos": [
            ("Virgin Mojito", "Classic mint & lime", 200.00),
            ("Strawberry Mojito", "Sweet strawberry twist", 250.00),
            ("Passionfruit Mojito", "Tropical passionfruit", 280.00),
            ("Blue Lagoon Mojito", "Vibrant blue citrus", 250.00),
        ],
        "Smoothies": [
            ("Passion Mango Smoothie", "Tropical mango blend", None),
            ("Passion Breeze", "Refreshing fruit blend", None),
            ("Pina Colada", "Pineapple & coconut", None),
        ],
        "Matcha Menu": [
            ("Matcha Latte", "Japanese ceremonial grade", 200.00),
            ("Mango Matcha Latte", "Matcha with mango", 250.00),
            ("Strawberry Matcha", "Matcha with strawberry", 250.00),
            ("Coconut Matcha", "Matcha with coconut", 250.00),
            ("Spanish Matcha Latte", "Spanish-style matcha", 250.00),
        ],
    }


@st.cache_data(show_spinner=False)
def get_signature_specials() -> List[Dict[str, str]]:
    return [
        {"icon": "💕", "name": "Café Amour", "desc": "Our signature espresso with a hint of vanilla and rose.", "price": "NPR 250.50"},
        {"icon": "🌹", "name": "Rose Latte", "desc": "Silky latte infused with organic rose petals.", "price": "NPR 300.00"},
        {"icon": "🍫", "name": "Mocha Passion", "desc": "Rich dark chocolate blended with premium espresso.", "price": "NPR 250.75"},
    ]


IMAGES_DIR = Path(__file__).parent / "images"


@st.cache_data(show_spinner=False)
def img_to_base64(filename: str) -> str:
    path = IMAGES_DIR / filename
    if not path.exists():
        return ""
    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    ext = path.suffix.lower().lstrip(".")
    mime = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "webp": "webp"}.get(ext, "jpeg")
    return f"data:image/{mime};base64,{encoded}"


@st.cache_data(show_spinner=False)
def video_to_base64(filename: str) -> str:
    path = IMAGES_DIR / filename
    if not path.exists():
        return ""
    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    return f"data:video/mp4;base64,{encoded}"


@st.cache_data(show_spinner=False)
def get_gallery_items() -> List[Dict[str, str]]:
    return [
        {"label": "Cozy Corners",  "filename": "gallery_1.jpg", "grad": "grad-1", "type": "image"},
        {"label": "Artisan Brews", "filename": "gallery_2.jpg", "grad": "grad-2", "type": "image"},
        {"label": "Sweet Bites",   "filename": "sweetbites.mp4", "grad": "grad-3", "type": "video"},
        {"label": "Morning Light", "filename": "gallery_4.jpg", "grad": "grad-4", "type": "image"},
        {"label": "Evening Vibes", "filename": "gallery_5.jpg", "grad": "grad-5", "type": "image"},
        {"label": "Our Baristas",  "filename": "gallery_6.jpg", "grad": "grad-6", "type": "image"},
    ]


@st.cache_data(show_spinner=False)
def get_seed_reviews() -> List[Dict[str, object]]:
    return [
        {"name": "Ajim Miya.",    "rating": 5, "text": "The best coffee I've ever had! The ambiance is magical."},
        {"name": "Sabir Hussain.", "rating": 5, "text": "Rose Latte is a masterpiece. Highly recommend!"},
        {"name": "Najir Hussain.", "rating": 5, "text": "Cozy place, lovely staff. Perfect for a date."},
    ]


# ---------------------------------------------------------------------------
# 5. SESSION STATE
# ---------------------------------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "reviews" not in st.session_state:
    st.session_state.reviews = list(get_seed_reviews())


# ---------------------------------------------------------------------------
# 6. HELPERS
# ---------------------------------------------------------------------------
def set_page_background(page: str) -> None:
    bg_class_map = {
        "Home": "page-bg-home",
        "Menu": "page-bg-menu",
        "Reviews": "page-bg-reviews",
        "Contact": "page-bg-contact",
    }
    bg_class = bg_class_map.get(page, "page-bg-home")
    st.markdown(f'<div class="{bg_class}"></div>', unsafe_allow_html=True)


def section_header(title: str, subtitle: str = "", kicker: str = "") -> None:
    kicker_html = f'<span class="kicker">{kicker}</span>' if kicker else ""
    sub_html = f'<span class="subtitle">{subtitle}</span>' if subtitle else ""
    st.markdown(
        f'<div class="section-header">{kicker_html}<h2>{title}</h2>{sub_html}</div>',
        unsafe_allow_html=True,
    )


def render_hero() -> None:
    logo_uri = img_to_base64("logo.jpg")
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
                <span class="eyebrow">Est. with love · Damauli, Nepal</span>
                <span class="script">Welcome to</span>
                <h1>Amour Du Cafè</h1>
                <div class="divider"></div>
                <p>Where every cup tells a story of love and passion</p>
                <span class="badge">☕ Handcrafted Daily · 100% Arabica</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_navbar() -> None:
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
    is_video = item.get("type") == "video"

    if is_video:
        video_uri = video_to_base64(item["filename"]) if item.get("filename") else ""
        if video_uri:
            st.markdown(
                f'''
                <div class="gallery-tile has-video" style="position: relative;">
                    <video autoplay muted loop playsinline>
                        <source src="{video_uri}" type="video/mp4">
                    </video>
                    <span>{item["label"]}</span>
                </div>
                ''',
                unsafe_allow_html=True,
            )
        else:
            css_class = f"gallery-tile {item.get('grad', 'grad-3')}"
            st.markdown(
                f'<div class="{css_class}"><span>{item["label"]}</span></div>',
                unsafe_allow_html=True,
            )
        return

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
# 7. PAGE RENDERERS
# ---------------------------------------------------------------------------
def render_home() -> None:
    section_header("Welcome to Amour Du Cafè", "A love letter to the art of coffee", kicker="Our Story")

    st.markdown(
        """
        <div class="stats-bar">
            <div class="stat-item">
                <span class="num" data-target="7" data-suffix="+">7+</span>
                <span class="lbl">Years Brewing</span>
            </div>
            <div class="stat-item">
                <span class="num" data-target="25000" data-suffix="+">25,000+</span>
                <span class="lbl">Cups Served</span>
            </div>
            <div class="stat-item">
                <span class="num" data-target="74" data-suffix="+">74</span>
                <span class="lbl">Menu Items</span>
            </div>
            <div class="stat-item">
                <span class="num" data-target="4.9" data-suffix="★" data-decimals="1">4.9★</span>
                <span class="lbl">Guest Rating</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown(
            """
            <div class="info-box">
                <h3>☕ Our Story</h3>
                <p>Nestled in the heart of Damauli, <b>Amour Du Cafè</b> is more than just a
                coffee shop — it's a love letter to the art of coffee making.</p>
                <p>Every bean is hand-picked, every roast is perfected, and every cup is
                brewed with <b>amour</b> (love).</p>
                <p>We believe great coffee is an experience — one that warms the soul
                as much as it awakens the senses.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class="info-box">
                <h3>✨ Why Choose Us?</h3>
                <p>🌱 &nbsp; Ethically sourced premium beans<br>
                   👨‍🍳 &nbsp; Expert baristas &amp; artisan brewing<br>
                   🏡 &nbsp; Cozy, romantic ambiance<br>
                   🍰 &nbsp; Freshly baked pastries daily<br>
                   🎵 &nbsp; Live acoustic evenings</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="marquee-strip">
            <div class="inner">
                <span>☕ Freshly Roasted</span> ·
                <span>🌹 Rose Latte Special</span> ·
                <span>🥐 Baked Daily</span> ·
                <span>🎵 Live Music Fridays</span> ·
                <span>❤️ Made with Love</span> ·
                <span>☕ Freshly Roasted</span> ·
                <span>🌹 Rose Latte Special</span> ·
                <span>🥐 Baked Daily</span> ·
                <span>🎵 Live Music Fridays</span> ·
                <span>❤️ Made with Love</span> ·
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    section_header("Signature Specials", "Handcrafted favourites our guests love", kicker="Our Favourites")
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

    section_header("From Our Café", "A glimpse into our world", kicker="Gallery")
    gallery = get_gallery_items()
    _, center_col, _ = st.columns([1, 4, 1])
    with center_col:
        for row_start in range(0, len(gallery), 3):
            cols = st.columns(3, gap="medium")
            for col, item in zip(cols, gallery[row_start : row_start + 3]):
                with col:
                    render_gallery_tile(item)


def render_menu() -> None:
    section_header("Our Menu", "Crafted with care, served with love", kicker="Taste the Difference")

    search = st.text_input(
        "🔍  Search for a dish or drink…",
        placeholder="e.g. latte, momo, pizza, mojito",
        label_visibility="collapsed",
    )

    menu = get_menu_data()

    GROUPED_MENU = {
        "🍽️  Food": [
            "Appetizers", "Mo : Mo", "Spicy Zone", "Brunch",
            "Italian Corner", "Sandwiches & Rolls", "Burger Joint",
        ],
        "☕  Coffee": [
            "Espresso Based Drinks", "Hot Flavored Drinks", "Amour's Signature",
            "Iced Coffee", "Slow Bar — Nepali Specialty Coffee",
            "Slow Bar — Specialty Coffee Around The World",
        ],
        "🍹  Cold & More": [
            "Coffee Alternatives", "Mojitos", "Smoothies", "Matcha Menu",
        ],
    }

    tabs = st.tabs(list(GROUPED_MENU.keys()))

    for tab, (group_name, categories) in zip(tabs, GROUPED_MENU.items()):
        with tab:
            any_results = False

            for category in categories:
                items = menu.get(category, [])

                if search:
                    q = search.lower().strip()
                    items = [i for i in items if q in i[0].lower() or q in i[1].lower()]

                if not items:
                    continue

                any_results = True

                st.markdown(
                    f'<div class="sub-category"><h3>{category}</h3></div>',
                    unsafe_allow_html=True,
                )

                left, right = st.columns(2, gap="medium")
                for idx, (name, desc, price) in enumerate(items):
                    target = left if idx % 2 == 0 else right
                    if price is not None:
                        price_html = f'<span class="price">NPR {price:.2f}</span>'
                    else:
                        price_html = '<span class="price ask-us">Ask Us</span>'
                    with target:
                        st.markdown(
                            f"""
                            <div class="menu-card">
                                <div class="menu-info">
                                    <h4>{name}</h4>
                                    <p>{desc}</p>
                                </div>
                                {price_html}
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )

                st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

            if not any_results and search:
                st.info("No items match your search. Try a different keyword.")


def render_reviews() -> None:
    section_header("Customer Reviews", "What our guests are saying", kicker="Testimonials")

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
    section_header("Leave Your Review", "We'd love to hear from you", kicker="Share Your Experience")

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
                components.html(
                    """
                    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.0/dist/confetti.browser.min.js"></script>
                    <script>
                      confetti({ particleCount: 180, spread: 90, origin: { y: 0.6 },
                        colors: ['#D4A056','#C97B5A','#8FA07A','#E8C88A','#FFFFFF'] });
                    </script>
                    """,
                    height=0,
                )
                st.success("Thank you for your review! 💕")
                st.rerun()
            else:
                st.error("Please fill in all fields before submitting.")


def render_contact() -> None:
    section_header("Visit Us", "We'd love to see you at Amour Du Cafè", kicker="Get in Touch")

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

    section_header("Find Us on the Map", kicker="Location")
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

    section_header("Send Us a Message", "We usually reply within a day", kicker="Say Hello")
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
# 8. MAIN ROUTER
# ---------------------------------------------------------------------------
set_page_background(st.session_state.page)
render_hero()
render_navbar()

st.markdown("<div style='height:14px;'></div>", unsafe_allow_html=True)

PAGES = {
    "Home": render_home,
    "Menu": render_menu,
    "Reviews": render_reviews,
    "Contact": render_contact,
}
PAGES.get(st.session_state.page, render_home)()


# ---------------------------------------------------------------------------
# 9. NEWSLETTER + FOOTER
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
        <span class="script">Amour Du Cafè</span>
        <h3>☕ Brewed with Love</h3>
        <p class="tagline">Where every cup tells a story of love and passion</p>
        <div class="socials">
            <a href="https://www.instagram.com/amourducafe786" target="_blank">📷 Instagram</a>
            <a href="https://www.facebook.com/share/1J9L545gMd/" target="_blank">📘 Facebook</a>
            <a href="mailto:amourducafe324@gmail.com">✉️ Email</a>
        </div>
        <p class="copyright">© 2025 Amour Du Cafè · All rights reserved · Made with ❤️ in Nepal</p>
    </div>
    """,
    unsafe_allow_html=True,
)