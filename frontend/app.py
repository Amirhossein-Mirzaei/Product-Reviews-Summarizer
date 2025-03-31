import streamlit as st
import requests
import time

# Create FastAPI endpoint
API_URL = "http://127.0.0.1:8000/analyze_reviews/"

# Streamlit UI Config
items_in_menu = {
    "About ": "https://www.linkedin.com/in/amirhossein-mirzaei/"
}

st.set_page_config(page_title="📋 خلاصه ساز کامنت محصولات", layout="centered", page_icon='../content/41.png', initial_sidebar_state='expanded', menu_items=items_in_menu)

st.session_state.language = 'fa'
st.session_state.direction = 'rtl'

# Apply RTL direction to the whole page


st.title("📋 خلاصه ساز :red[کامنت] محصولات")
st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500&display=swap');
        * {{font-family: 'Vazirmatn', sans-serif; direction: rtl;}}
        
    </style>
""", unsafe_allow_html=True)
# User input for API key
cohere_api_key = st.text_input("API خود را وارد کنید", type="password")

st.write("سلام، لطفا کامنت را در کادر زیر وارد کن تا بررسی شود")

# User input text here
review_text = st.text_area("متن کامنت(ها) رو در این قسمت وارد کنید", height=180)

if st.button("🔍 تحلیل کن"):
    if review_text.strip() and cohere_api_key.strip():
        progress_text = "در حال پردازش کامنت های ورودی هستیم ..."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.05)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        my_bar.empty()

        with st.spinner("خلاصه شما درحال پردازش است ..."):
            try:
                # Send request to FastAPI endpoint
                response = requests.post(API_URL, json={"review_text": review_text, "cohere_api_key": cohere_api_key})

                if response.status_code == 200:
                    data = response.json()

                    st.subheader("📝 خلاصه:")
                    st.info(data["summary"])
                    st.markdown("-----")
                    st.subheader("✅ مزایا:")
                    #st.success(data["pros"])
                    for i in data["pros"].split("\n"):
                        st.success(i, icon="✅")
                    st.markdown("-----")
                    st.subheader("❌ معایب:")
                    #st.error(data["cons"])
                    for i in data["cons"].split("\n"):
                        st.error(i, icon="❌")
                else:
                    st.error(f"🥲 متاسفانه خطایی رخ داده است: {response.status_code}")
            except requests.exceptions.RequestException as e:
                st.error(f"🚨 خطا در ارتباط با سرور: {e}")
    else:
        st.warning("🤔 لطفا متن و API Key را وارد کنید")
    
st.caption("👨‍💻 توسعه دهنده: [امیرحسین میرزایی](https://www.linkedin.com/in/amirhossein-mirzaei/)")
