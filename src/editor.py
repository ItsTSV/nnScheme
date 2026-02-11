import streamlit as st


def render_editor():
    """Renders the editor for neural network diagram"""
    _check_session_info()
    _render_layer_controls()

    for i, layer in enumerate(st.session_state.layers):
        with st.expander(f"Layer {i + 1}", expanded=True):
            c1, c2, c3, c4, c5 = st.columns(5)

            st.session_state.layers[i]["type"] = c1.selectbox(
                "Type", ["Linear", "Conv2d", "Flatten"], index=0, key=f"type_{i}"
            )
            st.session_state.layers[i]["text"] = c2.text_input(
                "Text", value=layer["text"], key=f"text_{i}"
            )
            st.session_state.layers[i]["shape"] = c3.text_input(
                "Size", value=layer["shape"], key=f"shape_{i}"
            )
            if st.session_state.layers[i]["type"] == "Conv2d":
                st.session_state.layers[i]["params"] = c4.text_input(
                    "Conv size", value=layer["params"], key=f"params_{i}"
                )
            st.session_state.layers[i]["activation"] = c5.text_input(
                "Input activation",
                value=layer["activation"],
                key=f"activation_{i}",
            )


def _render_layer_controls():
    """Renders buttons that add/remove layers"""
    st.markdown("## Layer Controls")
    left_col, right_col = st.columns(2)
    with right_col:
        if st.button("Add Layer"):
            st.session_state.layers.append(
                {
                    "type": "Conv2D",
                    "text": "",
                    "shape": "32",
                    "params": "",
                    "activation": "ReLU"
                    if len(st.session_state.layers) > 0
                    else "None",
                }
            )
    with left_col:
        if st.button("Remove Last"):
            if len(st.session_state.layers) > 0:
                st.session_state.layers.pop()


def _check_session_info():
    """Ensures layers are present in current session"""
    if "layers" not in st.session_state:
        st.session_state.layers = []
