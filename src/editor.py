import streamlit as st


def render_editor():
    """Renders the editor for neural network diagram"""
    _check_session_info()
    _render_layer_controls()

    for i, layer in enumerate(st.session_state.layers):
        with st.expander(f"Layer {i + 1}", expanded=True):
            c1, c2, c3, c4 = st.columns(4)

            st.session_state.layers[i]["type"] = c1.selectbox(
                "Type",
                ["Linear", "Conv2d", "Flatten"],
                index=0,
                key=f"type_{i}",
                accept_new_options=True,
                help="If none of the predefined layers is suitable, you can simply add new one."
            )
            st.session_state.layers[i]["shape"] = c2.text_input(
                "Size", value=layer["shape"], key=f"shape_{i}"
            )
            st.session_state.layers[i]["text"] = c3.text_input(
                "Additional parameters", value=layer["text"], key=f"text_{i}"
            )
            st.session_state.layers[i]["activation"] = c4.text_input(
                "Input activation",
                value=layer["activation"],
                key=f"activation_{i}",
            )


def _render_layer_controls():
    """Renders buttons that add/remove layers"""
    st.markdown("## Layer controls")
    left_col, right_col = st.columns(2)
    with right_col:
        if st.button("Add layer"):
            st.session_state.layers.append(
                {
                    "type": "Conv2D",
                    "text": "",
                    "shape": " ",
                    "activation": "ReLU"
                    if len(st.session_state.layers) > 0
                    else "None",
                }
            )
    with left_col:
        if st.button("Remove last"):
            if len(st.session_state.layers) > 0:
                st.session_state.layers.pop()


def render_additional_controls():
    """Renders additional controls for the editor"""
    st.markdown("## Additional controls")
    st.session_state.diagram_style = st.selectbox(
        label="Diagram style", options=["Academia", "Modern"], index=0
    )
    c1, c2 = st.columns(2)
    with c1:
        st.session_state.outgoing = st.toggle("Render outgoing edge?")
    with c2:
        st.session_state.outgoing_text = st.text_input(
            label="Outgoing text", value="Output"
        )


def _check_session_info():
    """Ensures layers are present in current session"""
    if "layers" not in st.session_state:
        st.session_state.layers = []
    if "outgoing" not in st.session_state:
        st.session_state.outgoing = False
    if "outgoing_text" not in st.session_state:
        st.session_state.outgoing_text = "Output"
    if "diagram_style" not in st.session_state:
        st.session_state.diagram_style = "Academia"
