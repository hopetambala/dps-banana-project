import plotly.express as px
import plotly.express as px

gapminder = px.data.gapminder().query("continent=='Europe'")
fig = px.line_3d(gapminder, x="gdpPercap", y="pop", z="year", color='country')
fig.show()