# Product Review Summarizer

## Overview
The **Product Review Summarizer** is a web application that extracts key insights from product reviews using AI. It provides a summarized review along with the main **pros** and **cons**, making it easier for users to understand customer feedback quickly.

This project is built using:
- **FastAPI** (Backend API)
- **Streamlit** (Frontend UI)
- **Cohere AI** (Text summarization)

---

## 🚀 Features
- **Summarizes multiple product reviews** into a concise overview.
- **Extracts key advantages & disadvantages** from customer feedback.
- **User-friendly UI** with Streamlit.
- **FastAPI-powered backend** for handling review processing.
- **Uses Cohere's LLM** for natural language understanding.

---

## 📂 Project Structure
```
Project Root/
│── README.md          # Project documentation
│── frontend/          # Streamlit frontend
│   ├── app.py         # UI using Streamlit
│── src/               # Backend source code
│   ├── main.py        # FastAPI application
│   ├── cohere_utils.py # AI processing logic
│── content/           # Static assets (images, ...)
│── config/            # Configuration files (in future updates)
│── docker/            # Docker setup (in future updates)
│── docs/             # Documentation
    ├── requirements.txt #Required libraires to install
│── log/               # Logs
```

---

## 🛠️ Installation & Setup
### **1. Clone the Repository**
```bash
git clone https://github.com/Amirhossein-Mirzaei/Product-Reviews-Summarizer.git

cd Product-Review-Summarizer
```

### **2. Create & Activate Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```
### **2-1. Using Conda Environment (Recommended)**
If you use **Conda**, create and activate an environment:
```bash
conda create --name review-summarizer-EnvName python=3.11 -y
conda activate review-summarizer-EnvName
```

### **3. Install Dependencies**
```bash
pip install -r docs/requirements.txt
```

### **4. Run the Backend (FastAPI Server)**
```bash
cd src
uvicorn main:app --reload
```
FastAPI should now be running at: **http://127.0.0.1:8000**

### **5. Run the Frontend (Streamlit UI)**
```bash
cd frontend
streamlit run app.py
```
The UI should open in your browser.

---

## 🖥️ Usage
1. Enter your **Cohere API Key**.
2. Paste the product reviews into the text box.
3. Click on **Analyze** to generate the summary in persian.
4. View the **summary, pros, and cons** extracted from the reviews.

---

## ⚡ API Endpoints
### **Analyze Reviews**
**POST** `/analyze_reviews/`
#### Request Body:
```json
{
  "review_text": "User reviews here...",
  "cohere_api_key": "your-api-key"
}
```
#### Response:
```json
{
  "summary": "Concise summary of reviews...",
  "pros": "- Benefit 1\n- Benefit 2",
  "cons": "- Drawback 1\n- Drawback 2"
}
```

---

## 🛠️ Technologies Used
- **Python** (FastAPI, Streamlit, langchain)
- **Cohere API** (AI-powered text processing)
- **Requests** (HTTP requests handling)
- **Logging** (Debugging & error tracking)


---
# How to Get a Free Cohere API Key for Testing  

Cohere provides a free API key that you can use for testing your project. Follow these steps to get your API key:

## 1: Sign Up for Cohere  
1. Visit [Cohere's official website](https://cohere.com).  
2. Click on **"Sign up"**.  
3. Register in website.  

## 2: Access the API Key  
1. After signing up, go to the [Cohere Dashboard](https://dashboard.cohere.com/).  
2. Navigate to the **API Keys** section.  
3. You will see your **API key**.  

### Now You Can Use the API Key 

## Notes  
✅ The free-tier API key is great for testing.  
⚠️ Do not share your API key publicly to avoid unauthorized usage.  

---
## 👨‍💻 Author
Developed by **Amirhossein Mirzaei**
- [LinkedIn](https://www.linkedin.com/in/amirhossein-mirzaei/)




