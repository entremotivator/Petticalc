import streamlit as st
from fpdf import FPDF

# Set up the default gratuity percentage
default_percentage = 15

# Title and description
st.title("Pretti Plates Calculator")
st.write(
    """
    **Welcome to Pretti Plates Calculator!**

    Whether you're dining solo or with friends, calculating your gratuity should be hassle-free.
    Simply enter the total amount of your bill, adjust the gratuity percentage if needed, 
    and we’ll instantly show you the calculated tip and the total amount to pay. You can even 
    download the summary as a PDF for your records or to share with others.
    """
)

# Input fields for total amount and tip percentage
cash_total = st.number_input("Enter your Cash Total ($):", min_value=0.0, format="%.2f")
tip_percentage = st.slider("Adjust Gratuity Percentage (%)", min_value=0, max_value=100, value=default_percentage)

# Calculate the tip amount and total amount with tip
tip_amount = cash_total * (tip_percentage / 100)
total_with_tip = cash_total + tip_amount

# Display the calculated amounts
st.write(f"**Calculated Tip Amount:** ${tip_amount:.2f}")
st.write(f"**Total Amount (Including Tip):** ${total_with_tip:.2f}")

# Option to download the details as a PDF
if st.button("Download Summary as PDF"):
    pdf = FPDF()
    pdf.add_page()
    
    # Add title
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Pretti Plates Gratuity Summary", ln=True, align="C")
    
    # Add content
    pdf.set_font("Arial", size=12)
    pdf.ln(10)  # New line
    pdf.cell(200, 10, f"Cash Total: ${cash_total:.2f}", ln=True)
    pdf.cell(200, 10, f"Gratuity Percentage: {tip_percentage}%", ln=True)
    pdf.cell(200, 10, f"Tip Amount: ${tip_amount:.2f}", ln=True)
    pdf.cell(200, 10, f"Total with Tip: ${total_with_tip:.2f}", ln=True)
    
    # Save the PDF to a file
    pdf_output = "Pretti_Plates_Gratuity_Summary.pdf"
    pdf.output(pdf_output)
    
    # Provide the PDF for download
    with open(pdf_output, "rb") as f:
        st.download_button(
            label="Download your Gratuity Summary PDF",
            data=f,
            file_name=pdf_output,
            mime="application/pdf",
        )
