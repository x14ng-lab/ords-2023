import plotly.graph_objects as go

def line_chart (df):
    """
    Generating a line chart for GP workforce trend

    Args:
        df (pandas.DataFrame): a dataframe containing GP workforce infomation by gender
    """
    #Data Preparation for plotting
    GP_workforce_all = df[df["Gender"]=="All"]
    GP_workforce_m = df[df["Gender"]=="Female"]
    GP_workforce_f = df[df["Gender"]=="Male"]
    GP_workforce_NR = df[df["Gender"]=="Not recorded"]
    fig = go.Figure()
    #Line chart for All Gender
    fig.add_trace(go.Scatter(x = GP_workforce_all["Year"], y=GP_workforce_all["Number of Workforce"], name="Total", line=dict(color="black"))) 
    #Line chart for Male
    fig.add_trace(go.Scatter(x = GP_workforce_m["Year"], y=GP_workforce_m["Number of Workforce"],name="Male", line=dict(color="blue")))
    #Line chart for Female
    fig.add_trace(go.Scatter(x = GP_workforce_f["Year"], y=GP_workforce_f["Number of Workforce"],name="Female", line=dict(color="red")))
    #Line chart for Not Recorded
    fig.add_trace(go.Scatter(x = GP_workforce_NR["Year"], y=GP_workforce_NR["Number of Workforce"],name="Not Recorded", line=dict(color="#D3D3D3", dash='dash')))
    fig.add_vline(x=6, line_dash="dot", annotation_text = "Oldest Year in Prevalence Data", line_color="gray")
    fig.update_layout(height=850, width=900, title="Number of GP Workforce Over Time", xaxis_title="Year", yaxis_title="Number of Workforce", xaxis=dict(tickmode="array",tickvals=GP_workforce_all["Year"].values))
    fig.show()