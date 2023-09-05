import streamlit as st

# Constants based on research (replace with actual values)
STONE_COST_PER_TON = 189  # Replace with the actual cost per ton of stone
LABOR_COST_PER_SQUARE_METER = 200  # £200 per square meter
LABOR_COST_PER_HOUR = 32  # £25 per hour

# Function to calculate tonnage of stone required
def calculate_stone_tonnage(length, height):
    wall_area = length * height
    stone_density = 1.6
    stone_tonnage = wall_area * stone_density
    return stone_tonnage

# Function to estimate the cost of stone
def estimate_stone_cost(tonnage):
    return tonnage * STONE_COST_PER_TON

# Function to estimate the cost of labor based on square meter rate
def estimate_labor_cost_per_square_meter(length, height):
    wall_area = length * height
    labor_cost = wall_area * LABOR_COST_PER_SQUARE_METER
    return labor_cost

# Function to estimate the cost of labor based on hourly rate
def estimate_labor_cost_per_hour(length, height):
    labor_hours = length * height * 8  # Assuming 8 hours of labor per square meter
    labor_cost = labor_hours * LABOR_COST_PER_HOUR
    return labor_cost

# Streamlit app
st.title("Dry Stone Wall Calculator")
st.header("Estimate the Cost of Building a Dry Stone Wall")

# Sidebar with user inputs
st.sidebar.title("Wall Dimensions")
height = st.sidebar.number_input("Height (meters):", min_value=0.1, value=1.0, step=0.1)
length = st.sidebar.number_input("Length (meters):", min_value=1.0, value=10.0, step=1.0)

st.image("https://github.com/ConnorInnit/ASD/raw/main/assets/62507982/662debea-d3f4-448c-bf68-7ffda2db04a2.jpg", 
          caption="Card Logo", use_column_width=True)

# Calculate values
stone_tonnage = calculate_stone_tonnage(length, height)
stone_cost = estimate_stone_cost(stone_tonnage)
labor_cost_per_square_meter = estimate_labor_cost_per_square_meter(length, height)
labor_cost_per_hour = estimate_labor_cost_per_hour(length, height)

# Display the results in the main content area
st.subheader("Results")
st.write(f"Tonnage of stone required: {stone_tonnage:.2f} tonnes")
st.write(f"Estimated cost of stone: £{stone_cost:.2f}")
st.write(f"Estimated cost of labor per square meter: £{labor_cost_per_square_meter:.2f}")
st.write(f"Estimated cost of labor per hour: £{labor_cost_per_hour:.2f}")

# Add some explanations and a link to more information
st.markdown("### Additional Information")
st.write("Dry stone walls are a traditional and sustainable construction technique.")
st.write("For more information, check out [Dry Stone Wall Association of Great Britain (DSWA)](https://www.dswa.org.uk/).")
