print("Step 1: Script started")

import pandas as pd
print("Step 2: Pandas imported")

df = pd.read_csv("uk_population_data.csv")
print("Step 3: CSV loaded")
df = pd.read_csv("uk_population_data.csv")
print("Step 4: Data processed")
print("Step 5: Charts created")
print("Step 6: HTML generated")
# -----------------------------
# KPIs CALCULATION
# -----------------------------
total_population = int(df["Population"].sum())
total_births = int(df["Births"].sum())
total_deaths = int(df["Deaths"].sum())
total_migration = int(df["Migration"].sum())

growth_rate = round(((total_births - total_deaths + total_migration) / total_population) * 100, 2)

# -----------------------------
# COLOR THEME
# -----------------------------
colors = ["#1ABC9C", "#2C3E50", "#F1C40F", "#E74C3C"]

# -----------------------------
# CHARTS
# -----------------------------

# Donut Chart (Population by Region)
donut_fig = px.pie(
    df,
    names="Region",
    values="Population",
    hole=0.5,
    color_discrete_sequence=colors
)

donut_fig.update_layout(
    paper_bgcolor="white",
    plot_bgcolor="white",
    margin=dict(t=20, b=20, l=20, r=20)
)

donut_chart = pio.to_html(donut_fig, full_html=False)

# Bar Chart
bar_fig = px.bar(
    df,
    x="Region",
    y="Population",
    color="Region",
    color_discrete_sequence=colors
)

bar_fig.update_layout(
    paper_bgcolor="white",
    plot_bgcolor="white",
    showlegend=False
)

bar_chart = pio.to_html(bar_fig, full_html=False)

# Line Chart (Over Time)
line_fig = px.line(
    df,
    x="Year",
    y="Population",
    color="Region",
    color_discrete_sequence=colors
)

line_fig.update_layout(
    paper_bgcolor="white",
    plot_bgcolor="white"
)

line_chart = pio.to_html(line_fig, full_html=False)

# -----------------------------
# HTML TEMPLATE
# -----------------------------
html = f"""
<html>
<head>
<title>UK Population Dashboard</title>

<style>
body {{
    background-color: #F4F4F4;
    font-family: 'Segoe UI', Arial;
    margin: 0;
}}

.dashboard {{
    padding: 20px;
}}

/* KPI CARDS */
.card {{
    background: white;
    border-radius: 8px;
    padding: 15px;
    margin: 10px;
    width: 18%;
    display: inline-block;
    box-shadow: 0 2px 6px rgba(0,0,0,0.08);
}}

.card h3 {{
    font-size: 14px;
    color: #777;
    margin: 0;
}}

.card h1 {{
    font-size: 26px;
    color: #333;
    margin: 5px 0;
}}

/* SECTIONS */
.section-title {{
    font-size: 18px;
    margin: 20px 10px 10px;
    font-weight: bold;
    color: #333;
}}

.chart-box {{
    background: white;
    border-radius: 8px;
    padding: 15px;
    margin: 10px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.08);
}}
</style>

</head>

<body>

<div class="dashboard">

    <!-- KPI CARDS -->
    <div>
        <div class="card">
            <h3>Total Population</h3>
            <h1>{total_population:,}</h1>
        </div>

        <div class="card">
            <h3>Births</h3>
            <h1>{total_births:,}</h1>
        </div>

        <div class="card">
            <h3>Deaths</h3>
            <h1>{total_deaths:,}</h1>
        </div>

        <div class="card">
            <h3>Migration</h3>
            <h1>{total_migration:,}</h1>
        </div>

        <div class="card">
            <h3>Growth Rate</h3>
            <h1>{growth_rate}%</h1>
        </div>
    </div>

    <!-- DONUT -->
    <div class="section-title">Population Distribution</div>
    <div class="chart-box">
        {donut_chart}
    </div>

    <!-- BAR -->
    <div class="section-title">Population by Region</div>
    <div class="chart-box">
        {bar_chart}
    </div>

    <!-- LINE -->
    <div class="section-title">Population Over Time</div>
    <div class="chart-box">
        {line_chart}
    </div>

</div>

</body>
</html>
"""

# -----------------------------
# SAVE FILE
# -----------------------------
with open("dashboard.html", "w") as f:
    f.write(html)

print("Dashboard created successfully: dashboard.html")