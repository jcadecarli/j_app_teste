import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.write("Aqui é P&D, Carvalho!")
# Set the title and description of your app
st.title("Cosine Function Chart App")
st.write("This app displays a chart of the cosine function.")

# Define the range of x values
x = np.linspace(0, 2 * np.pi, 100)

# Calculate the corresponding y values using the cosine function
y = np.cos(x)

# Create a Matplotlib figure and plot the cosine function
fig, ax = plt.subplots()
ax.plot(x, y)

# Set labels and title for the plot
ax.set_xlabel("x")
ax.set_ylabel("y = cos(x)")
ax.set_title("Cosine Function")

# Display the Matplotlib plot using Streamlit
st.pyplot(fig)


