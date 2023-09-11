import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set the title and description of your app
st.title("Animated Cosine and Sine Functions")
st.write("This app displays animated cosine and sine functions.")

# Create a Matplotlib figure and axis
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 1000)
line_cos, = ax.plot(x, np.cos(x), label="Cosine")
line_sin, = ax.plot(x, np.sin(x), label="Sine")

# Set labels and title for the plot
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Animated Cosine and Sine Functions")
ax.legend()

# Function to update the plot for animation
def update(frame):
    x = np.linspace(frame / 100, frame / 100 + 2 * np.pi, 1000)
    line_cos.set_data(x, np.cos(x))
    line_sin.set_data(x, np.sin(x))
    return line_cos, line_sin

# Create an animation
ani = FuncAnimation(fig, update, frames=range(1000), blit=True, interval=100)

# Display the Matplotlib animation using Streamlit
st.pyplot(fig)

# Add a timer for 10 minutes
st.text("This animation will run for 10 minutes.")
