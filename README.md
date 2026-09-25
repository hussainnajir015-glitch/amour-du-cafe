# ☕ Amour Du Cafè

A warm, cozy, production-ready **static café website** built with **Streamlit**.
No backend, no database — just beautiful HTML/CSS rendered through Streamlit.

---

## ✨ Features

- **Hero banner** with animated gradient, café name, tagline, and CTA badge
- **Home** — Our Story, Why Choose Us, Signature Specials, Gallery grid
- **Menu** — searchable, tabbed categories (Coffee, Tea, Pastries, Desserts) with card layout
- **Reviews** — read and submit guest reviews (session-scoped)
- **Contact** — location, hours, phone/email, embedded OpenStreetMap, and message form
- **Newsletter** — subscription form (client-side confirmation)
- **Fully responsive** — custom media queries for < 768px

---

## 🎨 Design

| Token         | Value     |
| ------------- | --------- |
| Espresso      | `#2B1A12` |
| Coffee        | `#3E2723` |
| Mocha         | `#5D4037` |
| Terracotta    | `#C97B5A` |
| Cream         | `#F5E6D3` |
| Sage          | `#7C8A6A` |
| Gold          | `#D4A056` |

Fonts: **Playfair Display** (headings) · **Poppins** (body), loaded from Google Fonts.

---

## 🚀 Deploying to Streamlit Community Cloud

1. **Push your code to GitHub**
   ```bash
   git init
   git add app.py README.md
   git commit -m "Initial commit — Amour Du Cafè"
   git branch -M main
   git remote add origin https://github.com/<your-username>/amour-du-cafe.git
   git push -u origin main