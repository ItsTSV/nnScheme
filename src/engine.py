import streamlit as st
import graphviz


def render_schema():
    """Renders the graphviz neural network"""
    st.markdown("## Neural Network Scheme")
    st.graphviz_chart(_process_layers())


def _process_layers():
    """Converts layer information from session state into graphviz format"""
    layers = st.session_state.layers

    dot = graphviz.Digraph(format="svg")
    dot.attr(rankdir="LR", nodesep="0.5", ranksep="1.0")
    node_style = {
        "shape": "box",
        "width": "1.5",
        "height": "3.5",
        "fixedsize": "true",
        "fontsize": "12",
        "margin": "0.15",
        "penwidth": "1.1",
        "color": "black",
        "style": "bold",
        "fillcolor": "white"
    }

    edge_color = "black"
    dot.attr("node", **node_style)
    dot.attr("edge", fontsize="11", penwidth="1.5", color=edge_color)

    for i, layer in enumerate(layers):
        layer_type = layer.get("type", "Layer")
        layer_size = layer.get("shape", "size")
        layer_comment = layer.get("text", "")
        layer_activation = layer.get("activation", "None")

        label = f"{layer_type.upper()}\l"
        label += f"({layer_size})\l"
        if layer_comment.strip():
            label += f"{layer_comment}\l"

        dot.node(f"n{i}", label=label)

        if i > 0:
            edge_label = f" {layer_activation} " if layer_activation != "None" else ""
            dot.edge(f"n{i - 1}", f"n{i}", label=edge_label, labelloc="t")

    return dot
