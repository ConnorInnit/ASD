import streamlit as st

# Constants based on research (replace with actual values)
STONE_COST_PER_TON = 189  # Replace with the actual cost per ton of stone
LABOR_COST_PER_SQUARE_METER = 200  # £200 per square meter
LABOR_COST_PER_HOUR = 25  # £25 per hour

# Function to calculate tonnage of stone required
def calculate_stone_tonnage(length, height):
    # Calculate the area of the wall (length times height)
    wall_area = length * height
    # Research shows the density would be 1.6, therefore we assign stone density the value of 1.6 (ton)
    stone_density = 1.6
    # Calculate and assign the tonnage using multiplication of area and density, and convert to metric tons (tonnes).
    stone_tonnage = wall_area * stone_density
    return stone_tonnage

# Function to estimate the cost of stone
def estimate_stone_cost(tonnage):
    return tonnage * STONE_COST_PER_TON

# Function to estimate the cost of labor based on square meter rate
def estimate_labor_cost_per_square_meter(length, height):
    # Calculate the labor cost based on the wall area and the provided labor rate
    wall_area = length * height
    labor_cost = wall_area * LABOR_COST_PER_SQUARE_METER
    return labor_cost

# Function to estimate the cost of labor based on hourly rate
def estimate_labor_cost_per_hour(length, height):
    # Calculate the total labor hours required for the wall
    labor_hours = length * height * 8  # Assuming 8 hours of labor per square meter
    labor_cost = labor_hours * LABOR_COST_PER_HOUR
    return labor_cost

# Streamlit app
st.title("Dry Stone Wall Calculator")

# User inputs
height = st.number_input("Please enter the height of the wall in meters:")
length = st.number_input("Please enter the length of the wall in meters:")

# Calculate values
stone_tonnage = calculate_stone_tonnage(length, height)
stone_cost = estimate_stone_cost(stone_tonnage)
labor_cost_per_square_meter = estimate_labor_cost_per_square_meter(length, height)
labor_cost_per_hour = estimate_labor_cost_per_hour(length, height)

# Display the results
st.write(f"Tonnage of stone required: {stone_tonnage:.2f} tonnes")
st.write(f"Estimated cost of stone: £{stone_cost:.2f}")
st.write(f"Estimated cost of labor per square meter: £{labor_cost_per_square_meter:.2f}")
st.write(f"Estimated cost of labor per hour: £{labor_cost_per_hour:.2f}")
