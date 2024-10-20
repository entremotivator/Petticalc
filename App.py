import streamlit as st

# Set up the default gratuity percentage
default_percentage = 15

# Title and description
st.title("Gratuity (Tip) Calculator")
st.write("Enter the cash total and adjust the gratuity percentage as needed.")

# Input fields for total amount and tip percentage
cash_total = st.number_input("Cash Total ($):", min_value=0.0, format="%.2f")
tip_percentage = st.slider("Gratuity Percentage (%)", min_value=0, max_value=100, value=default_percentage)

# Calculate the tip amount and total amount with tip
tip_amount = cash_total * (tip_percentage / 100)
total_with_tip = cash_total + tip_amount

# Display the calculated amounts
st.write(f"**Tip Amount:** ${tip_amount:.2f}")
st.write(f"**Total with Tip:** ${total_with_tip:.2f}")
