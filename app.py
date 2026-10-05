import os
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Sai Krishna Neti | Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Strip ALL Streamlit chrome so the iframe fills the screen edge-to-edge
st.markdown("""
<style>
#MainMenu, footer, header,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"] { display: none !important; }
.block-container,
[data-testid="stMainBlockContainer"],
[data-testid="stAppViewBlockContainer"] {
    padding: 0 !important;
    padding-top: 0 !important;
    margin: 0 !important;
    max-width: 100% !important;
}
[data-testid="stMain"] { padding-top: 0 !important; }
[data-testid="stVerticalBlock"] { gap: 0 !important; }
.stApp > div { padding-top: 0 !important; margin-top: 0 !important; }
.element-container { margin: 0 !important; padding: 0 !important; }
section[data-testid="stSidebar"] { display: none !important; }
.stApp { background: #05050f !important; }
iframe { display: block !important; border: none !important; margin-top: 0 !important; }
</style>
<script>
window.addEventListener('load', function() {
    window.scrollTo(0, 0);
    setTimeout(function() { window.scrollTo(0, 0); }, 100);
    setTimeout(function() { window.scrollTo(0, 0); }, 500);
});
</script>
""", unsafe_allow_html=True)

html_path = os.path.join(os.path.dirname(__file__), "index.html")
with open(html_path, "r", encoding="utf-8") as f:
    HTML = f.read()

components.html(HTML, height=6000, scrolling=True)
