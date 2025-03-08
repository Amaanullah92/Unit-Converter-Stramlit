import streamlit as st
import emoji as em

st.title(em.emojize(":globe_showing_Americas: Welcome to Unit Converter App"))
st.markdown(em.emojize("#### This app converts units of length, temperature, time, and weight."))
st.write(em.emojize("📌 Select the Unit Type to Convert:"))

unit_type = st.selectbox(em.emojize("📂 Choose a Category:"), ["📏 Length", "🌡️ Temperature", "⏳ Time", "⚖️ Weight"])

def convert_units(category, value, units):
    if category == "📏 Length":
        if units == "Kilometers to miles":
            return value * 0.621371, "miles 🛣️"
        elif units == "Miles to kilometers":
            return value * 1.60934, "km 🚗"
        elif units == "Meters to feet":
            return value * 3.28084, "ft 📏"
        elif units == "Feet to meters":
            return value * 0.3048, "m 📐"

    elif category == "🌡️ Temperature":
        if units == "Celsius to Fahrenheit":
            return (value * 9/5) + 32, "°F 🔥"
        elif units == "Fahrenheit to Celsius":
            return (value - 32) * 5/9, "°C ❄️"
        elif units == "Celsius to Kelvin":
            return value + 273.15, "K 🧊"
        elif units == "Kelvin to Celsius":
            return value - 273.15, "°C 🌡️"
        elif units == "Fahrenheit to Kelvin":
            return (value - 32) * 5/9 + 273.15, "K 🌍"
        elif units == "Kelvin to Fahrenheit":
            return (value - 273.15) * 9/5 + 32, "°F 🔥"

    elif category == "⏳ Time":
        if units == "Seconds to minutes":
            return value / 60, "mins ⏱️"
        elif units == "Minutes to seconds":
            return value * 60, "secs ⏳"
        elif units == "Minutes to hours":
            return value / 60, "hrs ⌛"
        elif units == "Hours to minutes":
            return value * 60, "mins ⏲️"
        elif units == "Hours to days":
            return value / 24, "days 📅"
        elif units == "Days to hours":
            return value * 24, "hrs ⏰"

    elif category == "⚖️ Weight":
        if units == "Kilograms to pounds":
            return value * 2.20462, "lbs 🏋️"
        elif units == "Pounds to kilograms":
            return value * 0.453592, "kg ⚖️"

    return None, ""

if unit_type == "📏 Length":
    unit = st.selectbox(em.emojize("📏 Choose a unit to convert:"), ["Kilometers to miles", "Miles to kilometers", "Meters to feet", "Feet to meters"])
elif unit_type == "🌡️ Temperature":
    unit = st.selectbox(em.emojize("🌡️ Choose a unit to convert:"), ["Celsius to Fahrenheit", "Fahrenheit to Celsius", "Celsius to Kelvin", "Kelvin to Celsius", "Fahrenheit to Kelvin", "Kelvin to Fahrenheit"])
elif unit_type == "⏳ Time":
    unit = st.selectbox(em.emojize("⏳ Choose a unit to convert:"), ["Seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes", "Hours to days", "Days to hours"])
elif unit_type == "⚖️ Weight":
    unit = st.selectbox(em.emojize("⚖️ Choose a unit to convert:"), ["Kilograms to pounds", "Pounds to kilograms"])

value = st.number_input(em.emojize("🔢 Enter the value to convert:"))


if st.button(em.emojize("🔄 Convert")):
    result, unit_symbol = convert_units(unit_type, value, unit)
    if result is not None:
        st.success(em.emojize(f"✅ The converted value is {result:.2f} {unit_symbol}"))
    else:
        st.write(em.emojize("🔴 Please select a unit type and unit to convert."))