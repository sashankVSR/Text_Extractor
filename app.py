import streamlit as st
from PIL import Image
import pytesseract

# Function to extract text from image using pytesseract
def extract_text_from_image(image):
    # Convert image to grayscale for better OCR accuracy
    gray_image = image.convert('L')
    text = pytesseract.image_to_string(gray_image)
    return text

# Streamlit app
def main():
    st.title("Image Text Extraction App")
    st.write("Upload an image, and this app will extract the text from it.")

    # Upload image
    uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # Open the uploaded image using PIL
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        st.write("")  # Add space
        
        # Extract text from image
        extracted_text = extract_text_from_image(image)
        
        # Show the extracted text
        st.subheader("Extracted Text:")
        st.write(extracted_text)

if __name__ == "__main__":
    main()
