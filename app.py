import streamlit as st
import plotly.graph_objects as go
import plotly.io as pio
import conda.cli

conda.cli.main('conda', 'install',  '-c', 'conda-forge', 'python-kaleido')

pio.kaleido.scope.chromium_args = (
        "--headless",
        "--no-sandbox",
        "--single-process",
        "--disable-gpu")
# Create a sample Plotly figure
fig = go.Figure(data=go.Scatter(x=[1, 2, 3, 4], y=[10, 11, 12, 13]))

fig.show()
output_filename = 'output.png'

# Use the save_as function to save the figure as an image
pio.write_image(fig, output_filename)
st.write('output saved')
with open("output.png", "rb") as file:
    btn = st.download_button(
            label="Download image",
            data=file,
            file_name="output.png",
            mime="image/png"
          )
