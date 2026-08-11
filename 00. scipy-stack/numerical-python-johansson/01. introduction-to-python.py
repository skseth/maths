# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
# Rich output display using IPython.display

from IPython.display import display, Image, HTML, Math, Latex, Markdown, Code, Pretty

# %%
import ipywidgets as widgets
import pandas as pd
from IPython.display import HTML, Math, display

display(HTML("<h2>Rich Output Display using IPython.display</h2>"))

# 1. Create a styled HTML Table using Pandas
df = pd.DataFrame(
    {
        "Model": ["GPT-4o", "Claude 3.5 Sonnet", "Gemini 1.5 Pro"],
        "Score": [0.88, 0.92, 0.86],
        "Status": ["Active", "Active", "Testing"],
    }
)

# Apply CSS styling (gradient background bars based on data values)
styled_table = df.style.background_gradient(cmap="Blues", subset=["Score"])

# 2. Create a mathematical equation
math_equation = Math(r"f(x) = \sigma(W^T x + b) = \frac{1}{1 + e^{-(W^T x + b)}}")

# 3. Create an interactive UI element
ui_slider = widgets.IntSlider(
    value=88, min=0, max=100, description="Threshold:", color="blue"
)

# --- THE POWER OF DISPLAY ---
# print() would fail completely here, showing raw text code or memory addresses.
# display() renders all three into their native, rich interactive visual forms.

display(HTML("<h3>1. Rich Data Table Output</h3>"))
display(styled_table)

display(HTML("<h3>2. High-Quality Math Notation</h3>"))
display(math_equation)

display(HTML("<h3>3. Live Interactive Widget</h3>"))
display(ui_slider)


# %%
Image(url="http://python.org/images/python-logo.gif")

# %%
Markdown("# Some markdown text with **bold** and *italic* formatting.\n## And more headings\n- Bullet 1\n- Bullet 2\n\n[Link to Python](https://www.python.org)")

# %%
from IPython.display import Pretty, display
from IPython.lib.pretty import pretty # This function converts the object to text

complex_data = {
    "user": {"id": 1024, "name": "Alex", "roles": ["admin", "developer"]},
    "metrics": {"session_time": 3600, "actions": ["click", "scroll", "submit"]},
    "status": "active"
}

# 1. Convert the dictionary into a pretty-formatted text string
formatted_text = pretty(complex_data, max_width=40)

# 2. Pass that text string into the Pretty display class
display(Pretty(formatted_text))

