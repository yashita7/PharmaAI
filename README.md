# PharmaAI
PharmaAI is an innovative AI-driven solution designed to assist pharmacists and healthcare professionals in analyzing and interpreting medical prescriptions with high accuracy and efficiency. PharmaAI automates the process of prescription analysis, reducing errors, and improving patient safety.

An **AI-powered assistant** that leverages **OCR, NLP, AI Agents, and Generative AI** to extract and analyze **medical prescriptions** with **context-aware intelligence**.  

## 🚀 Unique Features  
✅ **Multi-Agent AI System** – Uses **CrewAI** to coordinate AI agents for OCR and NLP tasks  
✅ **Generative AI-Powered Analysis** – Leverages **Gemini AI** for **intelligent medical interpretation**  
✅ **OCR with Deep Learning** – Extracts text from **handwritten & printed prescriptions**  
✅ **Structured NLP Insights** – Identifies **medicines & key medical terms**  
✅ **Streamlit UI for Accessibility** – User-friendly interface for pharmacists  

## 🏗️ AI Architecture  
1️⃣ **OCR Agent** → Extracts text from prescription images  
2️⃣ **NLP Agent** → Analyzes extracted text & identifies medicines  
3️⃣ **AI Reasoning Agent (CrewAI + Gemini AI)** → Provides structured insights  
4️⃣ **Streamlit Frontend** → Upload images & visualize AI-powered results  

## 🛠️ Tech Stack  
- **Python**  
- **EasyOCR** (for text extraction)  
- **spaCy** (for NLP-based medicine recognition)  
- **CrewAI** (for multi-agent AI coordination)  
- **Google Gemini AI** (for Generative AI-powered analysis)  
- **Streamlit** (for interactive UI)  

## 📦 Installation  
### 1️⃣ Clone the Repository  
git clone https://github.com/yashita7/PharmaAI.git

### 2️⃣ Create a Virtual Environment
-> python -m venv venv
-> source venv/bin/activate  # On macOS/Linux
-> venv\Scripts\activate     # On Windows

### 3️⃣ Install Dependencies
pip install -r requirements.txt

### 4️⃣ Set Up API Keys
Create a **.env file** and add your API key:
GEMINI_API_KEY=your_api_key_here

### 🎯 Usage
**Running the Assistant**
streamlit run frontend.py
1. Upload a prescription image.
2. AI extracts text & identifies medicines.
3. Generative AI provides structured analysis.

### Future Enhancements
-> 🚀 Integrate a chatbot for pharmacist queries
-> 🩺 Expand NLP to detect drug interactions
-> 📊 Generate prescription insights & summaries
