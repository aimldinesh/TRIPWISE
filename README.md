<p align="center">
  <img src="https://img.shields.io/github/last-commit/aimldinesh/TripWise" alt="Last Commit Badge">
  <img src="https://img.shields.io/badge/LLM-LLaMA_3.3_70B_versatile-blueviolet" alt="Model Badge">
  <img src="https://img.shields.io/badge/deployed-GCP-green" alt="Deployment Badge">
  <img src="https://img.shields.io/badge/Made%20with-Streamlit-orange" alt="Streamlit Badge">
  <img src="https://img.shields.io/badge/Docker-Containerized-blue" alt="Docker Badge">
  <img src="https://img.shields.io/badge/Kubernetes-Minikube-326ce5" alt="Kubernetes Badge">
  <img src="https://img.shields.io/badge/Monitoring-ELK%20Stack-yellow" alt="Monitoring Badge">
</p>

<div align="center">

# 🌍 TripWise: Your Smart Travel Companion

**TripWise** is an intelligent AI-powered travel itinerary planner built using **LLaMA-3.3-70B**, **Streamlit**, and **LangChain**.  
It leverages user inputs like destination, travel dates, and interests to generate personalized itineraries in real-time.

</div>

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
│   │   └── itinerary_chain.py    # Itinerary chain logic
│   ├── config/
│   │   └── config.py             # Load API keys and .env settings
│   ├── utils/
│   │   ├── logger.py             # Logging
│   │   └── custom_exception.py   # Exception handling with traceback info
│
├── filebeat.yaml              # Filebeat config for log shipping
├── logstash.yaml              # Logstash pipeline config
├── elasticsearch.yaml         # Elasticsearch deployment
├── kibana.yaml                # Kibana UI setup
│
└── logs/
    └── log_<date>.log         # generated log files
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
Follow these steps to set up and run **TripWise** locally:

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
pip install -e . or pip install -r requirements.txt
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
The app will be available at: http://localhost:8501

---

## ✅ Docker Run (Optional)
```bash
# Build Docker image
docker build -t tripwise-app .

# Run the container
docker run -p 8501:8501 tripwise-app
```
---

## 📊 Monitoring Setup (ELK Stack)
- Filebeat → Collects logs from app container
- Logstash → Filters & transforms logs
- Elasticsearch → Stores log data
- Kibana → Visualizes logs in dashboard
All components are deployed using Kubernetes under the logging namespace.

---
## ☸️ Screenshots
### 📸 Application Screenshots  

| App Running on VM | Destination Cities & Interests | Cities Itinerary |
|-------------------|--------------------------------|------------------|
| <img src="https://github.com/aimldinesh/TRIPWISE/blob/main/Screenshots/app_images/1.app_running_on_VM.PNG" width="250"/> | <img src="https://github.com/aimldinesh/TRIPWISE/blob/main/Screenshots/app_images/2.Destination_cities_and_intrests.PNG" width="250"/> | <img src="https://github.com/aimldinesh/TRIPWISE/blob/main/Screenshots/app_images/3.Destinition_cities_and_interests_itineary.png" width="250"/> |

| Destination States & Interests | States Itinerary |
|--------------------------------|------------------|
| <img src="https://github.com/aimldinesh/TRIPWISE/blob/main/Screenshots/app_images/4.Destinition_states_and_interests.png" width="250"/> | <img src="https://github.com/aimldinesh/TRIPWISE/blob/main/Screenshots/app_images/5.Desitinition_states_and_interset_itineary.PNG" width="250"/> |

### ⚙️ Setup & Running Screenshots

| Elasticsearch Setup | Logstash + Filebeat Setup | Detailed Filebeat Setup |
|----------------------|----------------------------|---------------------------|
| <img src="https://github.com/aimldinesh/TRIPWISE/blob/main/Screenshots/setup_and_running/1.elastics_search_setup.PNG" width="250"/> | <img src="https://github.com/aimldinesh/TRIPWISE/blob/main/Screenshots/setup_and_running/2.logstash_and_filebeat_setup.PNG" width="250"/> | <img src="https://github.com/aimldinesh/TRIPWISE/blob/main/Screenshots/setup_and_running/3.filebeat_setup_2.PNG" width="250"/> |

| Streamlit App running  on GCP VM | Kibana Running on GCP VM |
|--------------------------|----------------------------|
| <img src="https://github.com/aimldinesh/TRIPWISE/blob/main/Screenshots/setup_and_running/4.Streamlit_app_running_on_gcp_vm.PNG" width="250"/> | <img src="https://github.com/aimldinesh/TRIPWISE/blob/main/Screenshots/setup_and_running/5.kibana_running_on_gcp_vm.PNG" width="250"/> |

### 📊 Kibana Screenshots

| Kibana Home | Stack Management |
|-------------|------------------|
| <img src="https://github.com/aimldinesh/TRIPWISE/blob/main/Screenshots/kibana/1.Kibana%20Home.PNG" width="250" /> | <img src="https://github.com/aimldinesh/TRIPWISE/blob/main/Screenshots/kibana/2.Kibana%20Stack%20Management.PNG" width="250" /> |

| Index Pattern Creation | Index Pattern Fields |
|------------------------|------------------------|
| <img src="https://github.com/aimldinesh/TRIPWISE/blob/main/Screenshots/kibana/3.Index%20Pattern%20Creation).PNG" width="250" /> | <img src="https://github.com/aimldinesh/TRIPWISE/blob/main/Screenshots/kibana/4.Index%20Pattern%20Fields.PNG" width="250" /> |

| Discover Logs Overview | Detailed Logs View | Visualization |
|-------------------------|---------------------|----------------|
| <img src="https://github.com/aimldinesh/TRIPWISE/blob/main/Screenshots/kibana/5.Kibana%20Discover%20Logs%20Overview.PNG" width="250" /> | <img src="https://github.com/aimldinesh/TRIPWISE/blob/main/Screenshots/kibana/6.Kibana%20Discover%20Detailed%20Logs.PNG" width="250" /> | <img src="https://github.com/aimldinesh/TRIPWISE/blob/main/Screenshots/kibana/7.Kibana_visualize.PNG" width="250" /> |

---
## 🤝 Contributors
- [Dinesh Chaudhary](https://github.com/aimldinesh)
