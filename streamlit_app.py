import streamlit as st
from PIL import Image

# Constants based on research
STONE_COST_PER_TON = 189  # Cost per ton provided from research
LABOR_COST_PER_SQUARE_METER = 200  # Cost per square meter provided by research
LABOR_COST_PER_HOUR = 32  # Cost per hour provided from Research

# Function to calculate tonnage of stone required
def calculate_stone_tonnage(length, height):
    wall_area = length * height
    stone_density = 1.6
    stone_tonnage = wall_area * stone_density
    return stone_tonnage

# Function to calculate the cost of stone
def estimate_stone_cost(tonnage):
    return tonnage * STONE_COST_PER_TON

# Function to calculate the cost of labor based on square meter rate
def estimate_labor_cost_per_square_meter(length, height):
    wall_area = length * height
    labor_cost = wall_area * LABOR_COST_PER_SQUARE_METER
    return labor_cost

# Function to calculate the cost of labor based on hourly rate
def estimate_labor_cost_per_hour(length, height):
    labor_hours = length * height * 8  # Assuming 8 hours of labor per square meter
    labor_cost = labor_hours * LABOR_COST_PER_HOUR
    return labor_cost

# Streamlit app
st.set_page_config(
    page_title="Dry Stone Wall Calculator",  # Page title
    page_icon="🧱",  # Emoji for page icon
    layout="wide",  # Layout type
    initial_sidebar_state="expanded",
)

st.title("Dry Stone Wall Calculator")
st.header("Estimate the Cost of Building a Dry Stone Wall")
st.write("Please click the arrow on the left to type in your desired wall dimensions")

# Sidebar with user inputs
st.sidebar.title("Wall Dimensions")
height = st.sidebar.number_input("Height (meters):", min_value=0.1, value=1.0, step=0.1)
length = st.sidebar.number_input("Length (meters):", min_value=1.0, value=10.0, step=1.0)
st.sidebar.write("Please press enter to execute the calculation")

# UHI image displayed
st.image(
    "https://www.uhi.ac.uk/en/t4-media/one-web/university/admin-assets/img/logos/card-logo.jpg",
    caption="",
    use_column_width=True,
)

# Calculate values under header
stone_tonnage = calculate_stone_tonnage(length, height)
stone_cost = estimate_stone_cost(stone_tonnage)
labor_cost_per_square_meter = estimate_labor_cost_per_square_meter(length, height)
labor_cost_per_hour = estimate_labor_cost_per_hour(length, height)

# Display the results underneath UHI image
st.subheader("Results")
st.write(f"Tonnage of stone required: {stone_tonnage:.2f} tonnes")
st.write(f"Estimated cost of stone: £{stone_cost:.2f}")
st.write(f"Estimated total cost of labor based per square meter: £{labor_cost_per_square_meter:.2f}")
st.write(f"Estimated total cost of labor based on an hourly rate: £{labor_cost_per_hour:.2f}")

# Links and more information
st.markdown("##### Additional Information")
st.write("Dry stone walls are a traditional and sustainable construction technique.")
st.write("For more information, check out [Dry Stone Wall Association of Great Britain (DSWA)](https://www.dswa.org.uk/).")

st.markdown("#### Disclaimer")
st.write("Labour prices are based on an average range of different Stonemason rates throughout the UK; prices will vary depending on Stonemasons' experience.")
st.write("Stone prices are based on Sand Stone and Mixed Stone, with research conducted relevant to the UK current prices (2023).")
st.write("The calculations outputted by this calculator may not be 100% accurate; for a quote, check out [Register of DSWA Professional Wallers](https://www.dswa.org.uk/members/#:~:text=Professionals%20by%20location).")


