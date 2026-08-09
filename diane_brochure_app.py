#!/usr/bin/env python3
"""
Diane's Bathroom Remodel Brochure
DJM Project Pro's - Streamlit Version

Run with:
    streamlit run diane_brochure_app.py
"""

import streamlit as st
import os
from pathlib import Path

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Diane's Bathroom Options | DJM Project Pro's",
    page_icon="🛁",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------
# PATHS
# --------------------------------------------------
BASE = Path(__file__).parent
IMG_DIR = BASE / "diane-brochure"

OPTIONS = {
    "A": {
        "title": "Acrylic Shelves + Speckled Quartz",
        "file": "optA.jpg",
        "desc": "Practical & clean. Built-in shelving, grab bar ready, warm beige tones that complement your new countertop.",
        "features": [
            "Beige acrylic surround with deep shelves",
            "Cream tub + brushed nickel fixtures",
            "Speckled quartz counter + gold accents",
            "Easiest install & lowest maintenance"
        ]
    },
    "B": {
        "title": "White Marble + Chrome",
        "file": "optB.jpg",
        "desc": "Bright, modern, and timeless. Large-format marble look tile with black fixtures for a clean spa feel.",
        "features": [
            "White marble tile surround + niche",
            "Matte black fixtures",
            "White marble countertop + chrome",
            "Bright, high-end look"
        ]
    },
    "C": {
        "title": "Cream Subway + Gold",
        "file": "optC.jpg",
        "desc": "Warm traditional-modern. Soft cream tile, almond tub, brushed gold fixtures and fabric curtain.",
        "features": [
            "Cream subway tile walls",
            "Almond/beige tub + gold fixtures",
            "Light stone counter + gold hardware",
            "Warm, inviting atmosphere"
        ]
    },
    "D": {
        "title": "Sage Green Tile + Speckled",
        "file": "optD.jpg",
        "desc": "Fresh modern color. Soft sage vertical tile with black fixtures and glass panel.",
        "features": [
            "Sage green vertical tile",
            "Matte black fixtures + glass panel",
            "Speckled quartz counter + gold",
            "Trendy yet timeless"
        ]
    },
    "E": {
        "title": "Warm Taupe Stone + Niches",
        "file": "optE.jpg",
        "desc": "Spa-level. Large stone-look tile with multiple recessed LED niches for ample shelving.",
        "features": [
            "Warm taupe large-format tile",
            "Multiple LED recessed niches",
            "Brushed nickel fixtures",
            "Speckled quartz counter + gold"
        ]
    },
    "F": {
        "title": "Cream Subway + Clear Glass",
        "file": "optF.jpg",
        "desc": "Clean and bright. Classic cream subway with clear glass panel and matching brushed nickel.",
        "features": [
            "Cream subway tile",
            "Clear glass shower panel",
            "Brushed nickel fixtures (matched)",
            "Speckled quartz counter"
        ]
    }
}

# --------------------------------------------------
# CUSTOM CSS - DJM ORANGE/BLACK THEME
# --------------------------------------------------
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .stApp {
        background-color: #1a1a1a;
        color: #eee;
    }

    h1, h2, h3, h4 {
        color: #ffffff !important;
    }

    .djm-header {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
        border-bottom: 4px solid #E85D04;
        padding: 24px 20px 18px;
        text-align: center;
        margin-bottom: 8px;
    }
    .djm-logo {
        font-size: 28px;
        font-weight: 800;
        letter-spacing: 1px;
        color: #fff;
    }
    .djm-logo span {
        color: #E85D04;
    }
    .djm-tag {
        font-size: 13px;
        color: #aaa;
        margin-top: 4px;
    }

    .project-bar {
        background: #2d2d2d;
        padding: 12px 20px;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 28px;
        font-size: 14px;
        border-bottom: 1px solid #333;
        margin-bottom: 24px;
    }
    .project-bar strong {
        color: #E85D04;
    }

    .option-label {
        display: inline-block;
        background: #E85D04;
        color: #fff;
        font-size: 12px;
        font-weight: 700;
        padding: 3px 10px;
        border-radius: 4px;
        margin-bottom: 8px;
        letter-spacing: 0.5px;
    }

    .feature-list {
        list-style: none;
        padding-left: 0;
        font-size: 13.5px;
        color: #ccc;
    }
    .feature-list li {
        padding: 3px 0 3px 18px;
        position: relative;
    }
    .feature-list li::before {
        content: "✓";
        position: absolute;
        left: 0;
        color: #E85D04;
        font-weight: 700;
    }

    .stButton > button {
        background-color: transparent;
        border: 2px solid #E85D04;
        color: #E85D04;
        font-weight: 700;
        border-radius: 6px;
        width: 100%;
    }
    .stButton > button:hover {
        background-color: #E85D04;
        color: white;
        border-color: #E85D04;
    }

    .footer-box {
        background: #111;
        border-top: 3px solid #E85D04;
        padding: 28px 20px;
        text-align: center;
        margin-top: 40px;
    }
    .footer-box a {
        color: #E85D04;
        text-decoration: none;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown("""
<div class="djm-header">
    <div class="djm-logo">DJM <span>Project Pro's</span></div>
    <div class="djm-tag">Carbon County Home Improvement • Licensed & Insured</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="project-bar">
    <div><strong>Client:</strong> Diane</div>
    <div><strong>Address:</strong> 120 S Lincoln Ave, Walnutport PA</div>
    <div><strong>Scope:</strong> Tub Surround + Countertop + Fixtures</div>
</div>
""", unsafe_allow_html=True)

st.markdown("## Your Bathroom Remodel Options")
st.markdown(
    "<p style='color:#bbb; margin-bottom:24px;'>"
    "All designs keep your existing layout: tub on the left, vanity on the right "
    "(stopping before the toilet), toilet in the back-right corner, and your light brown tile floor."
    "</p>",
    unsafe_allow_html=True
)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "selected" not in st.session_state:
    st.session_state.selected = None

# --------------------------------------------------
# MAIN PREVIEW
# --------------------------------------------------
preview_key = st.session_state.selected or "A"
preview = OPTIONS[preview_key]
preview_path = IMG_DIR / preview["file"]

col_preview, col_info = st.columns([1.6, 1])

with col_preview:
    if preview_path.exists():
        st.image(str(preview_path), use_container_width=True, caption=f"Option {preview_key}")
    else:
        st.warning(f"Image not found: {preview['file']}")

with col_info:
    st.markdown(f"### Option {preview_key}")
    st.markdown(f"**{preview['title']}**")
    st.markdown(f"<p style='color:#bbb'>{preview['desc']}</p>", unsafe_allow_html=True)
    st.markdown("<ul class='feature-list'>" +
                "".join(f"<li>{f}</li>" for f in preview["features"]) +
                "</ul>", unsafe_allow_html=True)

    if st.button(f"Select Option {preview_key}", key=f"main_select_{preview_key}", type="primary"):
        st.session_state.selected = preview_key
        st.rerun()

st.markdown("---")
st.markdown("### All Options")

# 3-column grid
cols = st.columns(3)
for idx, (key, opt) in enumerate(OPTIONS.items()):
    with cols[idx % 3]:
        img_path = IMG_DIR / opt["file"]
        if img_path.exists():
            st.image(str(img_path), use_container_width=True)

        st.markdown(f"<span class='option-label'>OPTION {key}</span>", unsafe_allow_html=True)
        st.markdown(f"**{opt['title']}**")
        st.caption(opt["desc"][:90] + "…")

        btn_type = "primary" if st.session_state.selected == key else "secondary"
        if st.button(f"View / Select {key}", key=f"btn_{key}", type=btn_type):
            st.session_state.selected = key
            st.rerun()

# --------------------------------------------------
# SELECTION CONFIRMATION
# --------------------------------------------------
if st.session_state.selected:
    st.success(f"**Option {st.session_state.selected} selected** — {OPTIONS[st.session_state.selected]['title']}")
    st.info("Text or call Dylan to lock this option in and move to final pricing.")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("""
<div class="footer-box">
    <h3 style="color:#fff; margin-bottom:8px;">Ready to choose?</h3>
    <p style="color:#999;">Select an option above, then text or call to lock it in.</p>
    <p style="margin-top:14px; color:#eee;"><strong>Dylan Mabe</strong> • DJM Project Pro's</p>
    <p><a href="tel:2723945428">(272) 394-5428</a> &nbsp;|&nbsp; <a href="mailto:djmprojectpro@gmail.com">djmprojectpro@gmail.com</a></p>
    <p style="margin-top:10px; font-size:13px; color:#777;">Walnutport • Lehighton • Jim Thorpe • Carbon County PA</p>
</div>
""", unsafe_allow_html=True)
