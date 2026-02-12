# nnScheme
Simplistic tool for creating block diagrams of neural networks, originally created to visualize reinforcement learning models.
Written in Python, Streamlit and Graphviz.

### Features
- [x] UI for creating and editing block diagrams w/ real-time preview
- [x] Styling options for academic and modern aesthetics
- [x] Export to .png and .svg
- [x] Linear layers & all activations
- [ ] Other layers, such as convolutional, normalization etc.

### Usage
Desktop:
1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `streamlit run src/app.py`
> In order to export, Graphviz needs to be installed and added to PATH.

Server:
1.  [It just works](https://nnscheme.streamlit.app/)

