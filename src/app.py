import streamlit as st
from engine import render_schema
from editor import render_editor, render_additional_controls


st.set_page_config(
    page_title="nnScheme",
    layout="wide",
)

left_col, right_col = st.columns(2)
with left_col:
    render_editor()
with right_col:
    render_additional_controls()
    render_schema()
