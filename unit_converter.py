import streamlit as st
from pint import UnitRegistry

ureg = UnitRegistry()
Q_ = ureg.Quantity

unit_categories = {
    "Length": ["metre", "kilometre", "mile", "yard", "foot", "inch", "centimetre"],
    "Mass": ["kilogram", "gram", "pound", "ounce", "ton"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Time": ["second", "minute", "hour", "day"],
    "Speed": ["meter/second", "kilometer/hour", "mile/hour"],
    "Area": ["square meter", "square kilometer", "square mile", "acre", "hectare"],
    "Volume": ["liter", "milliliter", "gallon", "cubic meter"],
}

st.set_page_config(page_title="Unit Converter", layout="centered")
st.title("🔄 Google-Style Unit Converter")

category = st.selectbox("Select a category", list(unit_categories.keys()))
units = unit_categories[category]

col1, col2 = st.columns(2)

with col1:
    value = st.number_input("", min_value=0.0, value=1.0, format="%.6f", key="input_value")
    from_unit = st.selectbox("", units, key="from_unit")

with col2:
    to_unit = st.selectbox("", units, key="to_unit")

try:
    quantity = Q_(value, from_unit)
    converted = quantity.to(to_unit)
    result = converted.magnitude

    with col2:
        st.markdown(
            f"<h2 style='margin-top: 10px;'>{result:.6f}</h2>",
            unsafe_allow_html=True
        )

    st.markdown(
        f"<span style='background-color: #fff3cd; padding: 6px 12px; border-radius: 6px; font-weight: bold;'>Formula</span> multiply the value of <b>{from_unit}</b> by <b>{(result / value) if value != 0 else 0:.6f}</b> to get <b>{to_unit}</b>",
        unsafe_allow_html=True
    )

except Exception as e:
    st.error(f"Conversion error: {e}")