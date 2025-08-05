<p align="center">
  <img src="https://img.shields.io/github/last-commit/aimldinesh/TripWise" alt="Last Commit Badge">
  <img src="https://img.shields.io/badge/LLM-LLaMA_3.3_70B_versatile-blueviolet" alt="Model Badge">
  <img src="https://img.shields.io/badge/deployed-GCP-green" alt="Deployment Badge">
  <img src="https://img.shields.io/badge/Made%20with-Streamlit-orange" alt="Streamlit Badge">
  <img src="https://img.shields.io/badge/Docker-Containerized-blue" alt="Docker Badge">
  <img src="https://img.shields.io/badge/Kubernetes-Minikube-326ce5" alt="Kubernetes Badge">
  <img src="https://img.shields.io/badge/Monitoring-ELK%20Stack-yellow" alt="Monitoring Badge">
</p>

# 🌍 TripWise: Your Smart Travel Companion

**TripWise** is an intelligent AI-powered travel itinerary planner built using **LLaMA-3.3-70B**, **Streamlit**, and **LangChain**. It leverages user inputs like destination, travel dates, and interests to generate personalized itineraries in real-time.

---

## 📌 Features

- 🧠 LLM-powered travel planning with LLaMA-3.3-70B
- 🗺️ Personalized itineraries based on user input
- ⚡ Fast generation via Groq API
- 🎯 Minimal and responsive UI with Streamlit
- 🚀 Fully containerized with Docker & deployed on GCP VM via Kubernetes (Minikube)
- 📈 Real-time monitoring using Filebeat, Logstash, Elasticsearch & Kibana

---

## 🔁 Project Architecture & Workflow

```mermaid
graph TD

    %% ========== SECTION HEADERS ==========
    A0["🔧 1. Development Phase"]:::header
    B0["🚀 2. Deployment Phase"]:::header
    C0["📊 3. Monitoring Phase"]:::header
    D0["🗂️ Version Control"]:::header

    %% ========== DEVELOPMENT ==========
    A0 --> A1["🖥️ Streamlit UI"]
    A1 -->|HTTP Requests| A2["🧠 Travel Planner"]
    A2 --> A3["🔗 Itinerary Chain Logic"]
    A3 --> A4["⚙️ Configuration Service"]
    A4 -->|🔐 Env Vars / Secrets| A2

    %% ========== DEPLOYMENT ==========
    B0 --> B1["📄 Dockerfile"]
    B1 --> B2["🏗️ Build Container Image"]
    B2 --> B3["📦 Push to Registry"]
    B3 --> B4["☸️ Kubernetes (Minikube)"]
    B4 --> B5["🌐 GCP VM Instance"]

    %% ========== MONITORING ==========
    C0 --> C1["📥 Filebeat"]
    B5 -->|📤 Logs| C1
    C1 --> C2["🛠️ Logstash"]
    C2 --> C3["📚 Elasticsearch"]
    C3 --> C4["📈 Kibana Dashboards"]

    %% ========== VERSION CONTROL ==========
    D0 --> D1["🐙 GitHub"]
    D1 -->|⚙️ CI/CD| B5

    %% ========== CONNECTIONS ==========
    A1 -.->|🧪 Dev Testing| B4
    A2 -.->|🧪 Dev Testing| B4
    A3 -.->|🧪 Dev Testing| B4

    %% ========== STYLE ==========
    classDef header fill:#ffffff,stroke:#222222,stroke-width:2px,font-size:16px,color:#000;
    class A0,B0,C0,D0 header;
```
---
## 🧠 Tech Stack

| Layer              | Tools Used                                                   |
|-------------------|---------------------------------------------------------------|
| LLM Backend        | [LLaMA 3.3 70B - Versatile (via Groq API)]                   |
| App Framework      | Streamlit                                                    |
| LangChain Modules  | `langchain`, `langchain_community`, `langchain_groq`         |
| Deployment         | Docker, Kubernetes (Minikube), GCP VM                        |
| Monitoring         | Filebeat, Logstash, Elasticsearch, Kibana                    |

---
## 🧱 Project Structure
```bash
TripWise/
│
├── app.py                      # Streamlit main app
├── requirements.txt            # Python dependencies
├── setup.py                    # Package setup
├── .env                        # Environment variables
├── Dockerfile                  # Docker image definition
├── k8s-deployment.yaml         # Kubernetes deployment
│
├── src/
│   ├── core/
│   │   └── planner.py            # TravelPlanner logic using LLM
│   ├── chains/
│   │   └── itinerary_chain.py    # Itinerary chain logic & prompt construction
│   ├── config/
│   │   └── config.py             # Load API keys and .env settings
│   ├── utils/
│   │   ├── logger.py             # Logging with daily log rotation
│   │   └── custom_exception.py   # Exception handling with traceback info
│
├── filebeat.yaml              # Filebeat config for log shipping
├── logstash.yaml              # Logstash pipeline config
├── elasticsearch.yaml         # Elasticsearch deployment
├── kibana.yaml                # Kibana UI setup
│
└── logs/
    └── log_<date>.log         # Auto-generated log files
```
---
## ⚙️ Setup Instructions
### ✅ Prerequisites
Make sure you have the following installed and configured before starting:
- 🐍 Python 3.10+
- 🐳 Docker
- ☸️ Minikube (for Kubernetes deployment)
- ☁️ GCP VM Instance (for cloud hosting)
- 🔑 Groq API Key (LLaMA 3.3 70B model)
--- 
## 🚀 How to Run Locally
Follow these steps to set up and run **NexPick** locally:

### 1. Clone the Repository

```bash
git clone https://github.com/aimldinesh/TripWise.git
cd TripWise
```
### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install Dependencies
```bash
pip install -e .
```
### 4. Set Environment Variables
Create a .env file in the root directory and add your secrets like:
```bash
GROQ_API_KEY = " " 
```
### 5. Run the App
```bash
streamlit run app.py
```
The app will be available at:
---

## ✅ Docker Run (Optional)
```bash
# Build Docker image
docker build -t tripwise-app .

# Run the container
docker run -p 8501:8501 tripwise-app
```
---
## ☸️ Complete Deployment Setup

---
## 📊 Monitoring Setup (ELK Stack)
- Filebeat → Collects logs from app container
- Logstash → Filters & transforms logs
- Elasticsearch → Stores log data
- Kibana → Visualizes logs in dashboard
All components are deployed using Kubernetes under the logging namespace.

---
## 📸 Sample Output
---
## 🛠️ Future Improvements

