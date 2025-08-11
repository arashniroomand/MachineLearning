import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
@st.cache_data
def load_data():
    return sns.load_dataset('titanic')

df = load_data()
numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
cat_cols = df.select_dtypes(exclude=['number']).columns.tolist()

# ====================================
# CONSTANT UI ELEMENTS (won't rerun)
# ====================================
st.set_page_config(layout="wide")

# Custom CSS for persistent elements
st.markdown("""
<style>
.title-box {
    padding: 10px;
    border-radius: 5px;
    margin: 10px 0;
    font-weight: bold;
    text-align: center;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.persistent {
    position: relative;
    z-index: 999;
}
</style>
""", unsafe_allow_html=True)

# Persistent title
with st.container():
    st.markdown('<div class="title-box persistent" style="background-color:#3498db;color:white">TITANIC DATASET EXPLORER</div>', 
                unsafe_allow_html=True)

# Persistent column display
with st.container():
    cols = st.columns(5)
    colors = ["#73afdb", "#83b196", '#9b59b6', '#f1c40f', "#677673"]
    for i, col in enumerate(df.columns[:5]):
        cols[i%5].markdown(f'<div class="title-box" style="background-color:{colors[i]};color:white">{col}</div>', 
                          unsafe_allow_html=True)
    for i, col in enumerate(df.columns[5:10]):
        cols[i%5].markdown(f'<div class="title-box" style="background-color:{colors[i]};color:white">{col}</div>', 
                          unsafe_allow_html=True)
    for i, col in enumerate(df.columns[10:]):
        cols[i%5].markdown(f'<div class="title-box" style="background-color:{colors[i]};color:white">{col}</div>', 
                          unsafe_allow_html=True)

# ====================================
# INTERACTIVE SECTIONS (tab-based)
# ====================================
tab1, tab2 = st.tabs(["🔍 Data Explorer", "📊 Custom Plots"])

with tab1:
    # Sample data with button trigger
    with st.form("sample_form"):
        sample_size = st.slider("Select sample size", 1, len(df), 5)
        submitted = st.form_submit_button("🔎 Load Samples")
    
    if submitted:
        st.write(f"Showing {sample_size} random samples:")
        st.dataframe(df.sample(sample_size))

# ====================================
# ADDITIONAL FEATURES
# ====================================
with st.sidebar:
    st.header("Dataset Info")
    st.write(f"Total Rows: {len(df)}")
    st.write(f"Columns: {len(df.columns)}")
    
    if st.checkbox("Show Column Descriptions"):
        st.markdown("""
        - **survived**: 0=No, 1=Yes
        - **pclass**: Ticket class (1=1st, 2=2nd, 3=3rd)
        - **fare**: Passenger fare in £
        - **embarked**: Port (C=Cherbourg, Q=Queenstown, S=Southampton)
        """)
    
    if st.checkbox("Show Full Data"):
        st.dataframe(df)  # Using native Streamlit dataframe instead of AgGrid