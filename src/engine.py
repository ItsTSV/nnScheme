import streamlit as st
import graphviz


def render_schema():
    """Renders the graphviz neural network"""
    dot = _process_layers()

    st.markdown("## Export Options")
    _render_export(dot)

    st.markdown("## Neural Network Scheme")
    st.graphviz_chart(dot)


def _process_layers():
    """Converts layer information from session state into graphviz format"""
    layers = st.session_state.layers
    node_style, edge_color = _get_style_settings()

    dot = graphviz.Digraph(format="svg")
    dot.attr(rankdir="LR", nodesep="0.5", ranksep="1.0")
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

    if st.session_state.outgoing and layers:
        dot.node("output_end", label=" ", shape="none", width="0", height="0")
        dot.edge(f"n{len(layers) - 1}", "output_end", label=st.session_state.outgoing_text)

    return dot



def _render_export(dot):
    """Renders export options for scheme"""
    c1, c2 = st.columns(2)

    try:
        svg_data = dot.pipe(format='svg').decode('utf-8')
        c1.download_button(
            label="📥 Download SVG (Vector)",
            data=svg_data,
            file_name="nn_architecture.svg",
            mime="image/svg+xml",
            help="Best for web or editing in Illustrator/Inkscape"
        )
    except Exception as e:
        c1.error("SVG export requires 'Graphviz' installed on your system OS.")

    try:
        pdf_data = dot.pipe(format='pdf')
        c2.download_button(
            label="📥 Download PDF (LaTeX ready)",
            data=pdf_data,
            file_name="nn_architecture.pdf",
            mime="application/pdf",
            help="Best for LaTeX documents (retains vector quality)"
        )
    except Exception as e:
        c2.error("PDF export requires 'Graphviz' installed on your system OS.")


def _get_style_settings() -> tuple[dict, str]:
    """Returns style settings based on the selected diagram style"""
    edge_color = "black"
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
    if st.session_state.diagram_style == "Modern":
        edge_color = "#4A90E2"
        node_style.update({
            "color": "#4A90E2",
            "fillcolor": "#E6F0FA",
            "style": "filled,bold",
        })
    return node_style, edge_color
