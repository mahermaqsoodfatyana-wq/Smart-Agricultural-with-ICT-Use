import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="ICT in Smart Agriculture",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 ICT in Smart Agriculture")
st.subheader("Crop Input & Cost Calculator")

st.markdown("""
This application helps farmers estimate:

✅ Seed Requirement

✅ Fertilizer Requirement

✅ Spray Requirement

✅ Estimated Total Cost

based on crop type and land area (acres).
""")

# Crop Data
crop_data = {
    "Wheat": {
        "seed": 50,
        "fertilizer": 100,
        "spray": 2,
        "seed_cost": 180,
        "fertilizer_cost": 120,
        "spray_cost": 1500
    },
    "Rice": {
        "seed": 35,
        "fertilizer": 120,
        "spray": 3,
        "seed_cost": 220,
        "fertilizer_cost": 120,
        "spray_cost": 1500
    },
    "Cotton": {
        "seed": 10,
        "fertilizer": 150,
        "spray": 5,
        "seed_cost": 1200,
        "fertilizer_cost": 120,
        "spray_cost": 1500
    },
    "Maize": {
        "seed": 12,
        "fertilizer": 130,
        "spray": 2,
        "seed_cost": 900,
        "fertilizer_cost": 120,
        "spray_cost": 1500
    }
}

crop = st.selectbox(
    "Select Crop",
    list(crop_data.keys())
)

acres = st.number_input(
    "Enter Land Area (Acres)",
    min_value=1.0,
    value=1.0,
    step=0.5
)

data = crop_data[crop]

# Calculations
total_seed = data["seed"] * acres
total_fertilizer = data["fertilizer"] * acres
total_spray = data["spray"] * acres

seed_cost = total_seed * data["seed_cost"]
fertilizer_cost = total_fertilizer * data["fertilizer_cost"]
spray_cost = total_spray * data["spray_cost"]

total_cost = seed_cost + fertilizer_cost + spray_cost

st.header("📊 Results")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Seeds Required", f"{total_seed:.1f} kg")

with col2:
    st.metric("Fertilizer Required", f"{total_fertilizer:.1f} kg")

with col3:
    st.metric("Spray Required", f"{total_spray:.1f} L")

st.subheader("💰 Estimated Cost")

st.write(f"🌱 Seed Cost: PKR {seed_cost:,.0f}")
st.write(f"🧪 Fertilizer Cost: PKR {fertilizer_cost:,.0f}")
st.write(f"🚜 Spray Cost: PKR {spray_cost:,.0f}")

st.success(f"Total Estimated Cost: PKR {total_cost:,.0f}")

# Summary Table
summary = pd.DataFrame({
    "Item": ["Seeds", "Fertilizer", "Spray"],
    "Required": [
        f"{total_seed:.1f} kg",
        f"{total_fertilizer:.1f} kg",
        f"{total_spray:.1f} L"
    ]
})

st.subheader("Input Summary")
st.table(summary)

st.bar_chart({
    "Seeds Cost": seed_cost,
    "Fertilizer Cost": fertilizer_cost,
    "Spray Cost": spray_cost
})

st.header("👨‍💻 Project Team")

st.markdown("""
1. Maqsood Ahmad (25ME142)

2. M. Abdullah (25ME162)

3. M. Haseeb (54)

4. Azmat u Allah (25ME198)

5. Syed Sabih Gillani (25ME226)
""")

st.info("ICT in Smart Agriculture Project using Streamlit")
