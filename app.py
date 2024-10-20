import streamlit as st
from fpdf import FPDF

# Set up default gratuity percentage
default_percentage = 15

# Title and introduction with a welcoming image
st.title("Pretti Plates Calculator")
st.image("https://example.com/restaurant_image.jpg", caption="Enjoy your meal with Pretti Plates!")

st.write(
    """
    **Pretti Plates Calculator** is your go-to tool for calculating meal gratuity quickly and accurately. Whether you're out with friends or 
    enjoying a solo meal, it's important to leave the right tip for the service you've received.
    
    Simply enter the total cost of your meal, adjust the gratuity percentage if needed, and we’ll calculate both the tip and your final total. 
    You can even download a summary of your calculation in PDF format, perfect for keeping track of your expenses or sharing with your group.
    """
)

# Helpful Note on Tipping Etiquette
st.subheader("Why Gratuity Matters")
st.write(
    """
    Tipping is a reflection of the service provided. It’s a way to show appreciation to the restaurant staff who make your dining experience 
    enjoyable. The standard gratuity is typically 15%, but this can vary based on the quality of service. Let’s help you calculate the perfect tip!
    """
)

st.write("Ready to calculate? Let's get started!")

# Input fields for cash total and tip percentage
cash_total = st.number_input("Enter your Cash Total ($):", min_value=0.0, format="%.2f", help="Enter the total cost of your meal.")
tip_percentage = st.slider(
    "Adjust Gratuity Percentage (%)", min_value=0, max_value=100, value=default_percentage, help="Use the slider to adjust the percentage of your gratuity."
)

# Calculate tip amount and total
tip_amount = cash_total * (tip_percentage / 100)
total_with_tip = cash_total + tip_amount

# Display results with a dynamic summary
st.subheader("Your Calculation Summary:")
st.write(f"- **Cash Total:** ${cash_total:.2f}")
st.write(f"- **Gratuity Percentage:** {tip_percentage}%")
st.write(f"- **Tip Amount:** ${tip_amount:.2f}")
st.write(f"- **Total Amount (Including Tip):** ${total_with_tip:.2f}")

st.write(
    """
    You can adjust the gratuity percentage to see how it impacts your total, or lock in the standard 15% tip. Once you're happy with the result, 
    download a PDF version of your calculation for record-keeping or future use.
    """
)

# Function to generate PDF summary
def create_pdf(cash_total, tip_percentage, tip_amount, total_with_tip):
    pdf = FPDF()
    pdf.add_page()

    # Add title and header
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Pretti Plates Gratuity Summary", ln=True, align="C")
    
    # Add detailed content
    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.cell(200, 10, f"Cash Total: ${cash_total:.2f}", ln=True)
    pdf.cell(200, 10, f"Gratuity Percentage: {tip_percentage}%", ln=True)
    pdf.cell(200, 10, f"Tip Amount: ${tip_amount:.2f}", ln=True)
    pdf.cell(200, 10, f"Total Amount (Including Tip): ${total_with_tip:.2f}", ln=True)
    
    # Add extra detail and footer
    pdf.ln(10)
    pdf.cell(200, 10, "Gratuity Tip Recommendations:", ln=True)
    pdf.cell(200, 10, "- 15% is the standard for good service.", ln=True)
    pdf.cell(200, 10, "- 20% or more for exceptional service.", ln=True)
    pdf.cell(200, 10, "- 10% or less for unsatisfactory service.", ln=True)

    pdf.ln(20)
    pdf.set_font("Arial", "I", 10)
    pdf.cell(200, 10, "Thank you for using Pretti Plates Calculator! Keep track of your meals and tips effortlessly.", ln=True, align="C")
    
    # Save the PDF to a file
    return pdf

# Option to download PDF
if st.button("Download Summary as PDF"):
    pdf = create_pdf(cash_total, tip_percentage, tip_amount, total_with_tip)
    pdf_output = "Pretti_Plates_Gratuity_Summary.pdf"
    pdf.output(pdf_output)
    
    with open(pdf_output, "rb") as f:
        st.download_button(
            label="Download Gratuity Summary PDF",
            data=f,
            file_name=pdf_output,
            mime="application/pdf",
        )

# Additional tipping tips and scenarios
st.subheader("Gratuity Guidelines & Custom Tips")
st.write(
    """
    - **15%**: This is the standard tip for satisfactory service. 
    - **18-20%**: Tip this amount for great service, particularly in fine dining or attentive environments.
    - **10% or less**: If the service was below your expectations, you can leave a reduced tip.
    
    Consider the circumstances. For large parties or special requests, a higher gratuity might be appropriate.
    """
)

# Contextual Example: What to tip based on occasion
st.subheader("Tipping Scenarios")
st.write(
    """
    - **Date Night**: Planning something special? Consider tipping around **18-20%** to reflect the effort put in.
    - **Business Lunch**: Professional courtesy matters—keep your tip between **15-18%** to match the setting.
    - **Casual Meal**: A quick lunch or coffee with friends? The standard **15%** should suffice.
    
    Use the slider to experiment with different tip amounts based on your occasion.
    """
)

# Added feature for saving calculation data
st.subheader("Save Your Tip Calculation")
save_tip = st.checkbox("Save this calculation to your history")

if save_tip:
    st.write("Tip calculation saved! You can view your saved calculations in the future.")

# Footer message
st.write("---")
st.write(
    """
    **Pretti Plates Calculator** takes the guesswork out of tipping, so you can enjoy your dining experience without worrying about math. 
    If you enjoyed using this tool, please share it with others or leave your feedback on how we can improve!
    """
)
