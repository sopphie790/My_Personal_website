import streamlit as st

st.set_page_config(page_title="Contact", page_icon="📬")

st.title("📬 Contact Me")

name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Your Message")

if st.button("Send Message"):
    if name and email and message:
        st.success("✅ Message sent successfully!")
    else:
        st.error("⚠ Please fill in all fields.")

st.markdown("---")
st.subheader("🌐 Social Links")
st.write("GitHub: https://github.com/")
st.write("Facebook: https://facebook.com/")