import plotly.express as px

pivot = df.pivot_table(
    index="discipline",
    columns="phase",
    values="risk_score",
    aggfunc="mean"
)

fig = px.imshow(pivot, text_auto=True)

st.plotly_chart(fig, use_container_width=True)