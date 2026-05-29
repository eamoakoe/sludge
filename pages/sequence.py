import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

from utils.loader_sequence import build_edges

st.title("🔗 Design Sequence & Dependencies")

edges = build_edges()

G = nx.DiGraph()
G.add_edges_from(edges)

# ---- Draw Graph ----
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G)

nx.draw(
    G, pos,
    with_labels=True,
    node_size=3000,
    node_color="lightblue",
    font_size=8,
)

st.pyplot(plt)

# ---- Critical Path Logic ----
try:
    path = nx.dag_longest_path(G)
    st.subheader("🚨 Critical Path")
    st.write(" → ".join(path))
except:
    st.warning("Graph must be acyclic")
