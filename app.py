import streamlit as st

# Set the page title and icon
st.set_page_config(page_title="react-diff Waitlist ⏰", page_icon="✉️")

# Main page content (Waitlist Signup)
st.title("ReactDiff Waitlist ⏰")
st.write("Sign up to be the first to know when we launch! Enter your name and email address below to join our waitlist.")

# Input fields for name and email
name = st.text_input("Name:")
email = st.text_input ("Enter your email address:")

# Button to submit the information
if st.button("Join Waitlist"):
    if name and email:
        # Save the email and name (you could modify this to save to a database or file)
        with open("waitlist_emails.txt", "a") as f:
            f.write(f"{name}, {email}\n")
        st.success("Thank you! You've been added to the waitlist.")
    else:
        st.error("Please enter both your name and email address.")

st.write("---")
st.write("We respect your privacy 🔒 Please note that your information will only be used to notify you about recieving access to ReactDiff's inital launch.")

st.sidebar.subheader("Meet ReactDiff")
st.sidebar.write("""
   React-Diff is an AI software tool created for neuro-oncology research. The software applies machine learning (ML) to visualize tumor growth patterns using advanced reaction-diffusion models. 

Our Mission is to provide researchers with valuable insights towards understanding tumor heterogeneity and potential therapeutic interventions. 
                
""")
st.sidebar.subheader("Key Features")
st.sidebar.write("""
- Simulation Accuracy: Utilizes cutting-edge algorithms to simulate realistic tumor growth patterns.
- User-Friendly Interface: Designed with ease of use in mind, allowing both experts and beginners to explore simulations.
- Data Integration: Seamlessly integrates with existing datasets to provide detailed analysis and predictions.   

Stay tuned for more updates as we prepare to launch this innovative tool!                            
"""
     )