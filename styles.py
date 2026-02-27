# ─────────────────────────────────────────────────────
# styles.py — All CSS for SwarmScholar AI
# Edit colors, fonts, sizes here only!
# ─────────────────────────────────────────────────────

# def get_styles():
#     return """
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');

# *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

# html, body, .stApp {
#     font-family: 'Poppins', sans-serif !important;
#     background: #F8FAFC !important;
# }

# /* ── Hide Streamlit chrome ── */
# .stApp > header                  { display: none !important; }
# [data-testid="stHeader"]         { display: none !important; height: 0 !important; }
# [data-testid="stToolbar"]        { display: none !important; }
# [data-testid="collapsedControl"] { display: none !important; }
# section[data-testid="stSidebar"] { display: none !important; }
# footer                           { display: none !important; }

# .block-container {
#     padding: 0 !important;
#     margin: 0 !important;
#     max-width: 100% !important;
# }

# /* ── Base button reset ── */
# div.stButton > button {
#     font-family: 'Poppins', sans-serif !important;
#     font-weight: 600 !important;
#     border: none !important;
#     cursor: pointer !important;
#     transition: all 0.2s ease !important;
# }
# div.stButton > button:focus {
#     outline: none !important;
#     box-shadow: none !important;
# }

# /* ── Blue CTA button (hero + bottom) ── */
# .btn-blue div.stButton > button {
#     background: #3B82F6 !important;
#     color: #FFFFFF !important;
#     font-size: 15px !important;
#     font-weight: 700 !important;
#     padding: 14px 0 !important;
#     border-radius: 12px !important;
#     width: 100% !important;
#     box-shadow: 0 4px 20px rgba(59,130,246,0.4) !important;
# }
# .btn-blue div.stButton > button:hover {
#     background: #2563EB !important;
#     box-shadow: 0 6px 28px rgba(59,130,246,0.5) !important;
#     transform: translateY(-1px) !important;
# }

# /* ── Dark Analyse button ── */
# .btn-dark div.stButton > button {
#     background: #1E293B !important;
#     color: #F8FAFC !important;
#     font-size: 15px !important;
#     font-weight: 700 !important;
#     padding: 14px 0 !important;
#     border-radius: 12px !important;
#     width: 100% !important;
#     margin-top: 6px !important;
# }
# .btn-dark div.stButton > button:hover {
#     background: #0F172A !important;
#     transform: translateY(-1px) !important;
# }

# /* ── Ghost back button ── */
# .btn-ghost div.stButton > button {
#     background: transparent !important;
#     color: #64748B !important;
#     border: 1.5px solid #CBD5E1 !important;
#     font-size: 13px !important;
#     font-weight: 500 !important;
#     padding: 8px 20px !important;
#     border-radius: 10px !important;
# }
# .btn-ghost div.stButton > button:hover {
#     border-color: #3B82F6 !important;
#     color: #3B82F6 !important;
#     transform: none !important;
#     box-shadow: none !important;
# }

# /* ── Text input ── */
# .stTextInput > div > div > input {
#     font-family: 'Poppins', sans-serif !important;
#     font-size: 15px !important;
#     border: 2px solid #CBD5E1 !important;
#     border-radius: 12px !important;
#     padding: 14px 18px !important;
#     background: #FFFFFF !important;
#     color: #1E293B !important;
# }
# .stTextInput > div > div > input:focus {
#     border-color: #3B82F6 !important;
#     box-shadow: 0 0 0 3px rgba(59,130,246,0.12) !important;
# }
# .stTextInput > div > div > input::placeholder { color: #94A3B8 !important; }
# .stTextInput > label {
#     font-family: 'Poppins', sans-serif !important;
#     font-size: 13px !important;
#     font-weight: 600 !important;
#     color: #475569 !important;
# }

# /* ── Download button ── */
# .stDownloadButton > button {
#     font-family: 'Poppins', sans-serif !important;
#     background: #1E293B !important;
#     color: #F8FAFC !important;
#     font-weight: 600 !important;
#     font-size: 14px !important;
#     border-radius: 10px !important;
#     border: none !important;
#     padding: 12px 28px !important;
# }

# /* ── Spinner ── */
# .stSpinner > div { border-top-color: #3B82F6 !important; }
# </style>
# """