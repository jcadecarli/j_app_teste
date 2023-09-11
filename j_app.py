import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap

# Set the title and description of your app
st.title("Faster 2D Wave Animation with Color Change")
st.write("This app displays an animated 2D wave with color change.")

# Create a Matplotlib figure and axis
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 100)
y = np.linspace(0, 2 * np.pi, 100)
X, Y = np.meshgrid(x, y)
wave = np.sin(X + Y)

# Create a colormap that changes colors
cmap = ListedColormap(["blue", "cyan", "lime", "yellow", "red"])

# Create an empty plot for the wave animation
im = ax.imshow(wave, cmap=cmap, origin="lower", extent=[0, 2 * np.pi, 0, 2 * np.pi])

# Set labels and title for the plot
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Faster 2D Wave Animation with Color Change")

# Function to update the wave animation
def update(frame):
    wave = np.sin(X + Y - frame / 5.0)
    im.set_array(wave)
    return im,

# Create an animation
ani = FuncAnimation(fig, update, frames=range(100), blit=True, interval=50)  # Faster animation (interval=50)

# Create a Streamlit figure to display the animation
st.pyplot(fig)

# Add a timer for 10 minutes (600 seconds)
st.text("This animation will run for 10 minutes (600 seconds).")
