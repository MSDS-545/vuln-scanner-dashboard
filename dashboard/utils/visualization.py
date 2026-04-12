import plotly.express as px

def severity_chart(df):

    return px.histogram(df, x="severity")