# 👟 NIKE PULSE: AI-Driven Supply Chain Intelligence
> **"Bridging the gap between human desire and global logistics."**

![Status](https://img.shields.io/badge/Status-Finals--Ready-00f2fe?style=for-the-badge)
![Deployment](https://img.shields.io/badge/Deployment-Live-ff8c00?style=for-the-badge)

---

## 🌩️ 1. PROBLEM STATEMENT & OBJECTIVE
In high-demand sneaker markets, consumer desire moves faster than data. [cite_start]Traditional logistics are **reactive**, resulting in the "Silent Sell-Out"—where stock is depleted by scalper bots before real fans can react, and inventory is often misallocated due to a lack of localized real-time insights[cite: 20].

**Objective:** To build a proactive intelligence layer that secures the queue against bots and uses social sentiment to optimize stock distribution before a drop occurs.

## ⚖️ 2. GAP ANALYSIS (Current vs. Proposed)
| Feature | Legacy Systems (Reactive) | Nike Pulse (Proactive) |
| :--- | :--- | :--- |
| **Demand Signal** | Past sales history & app clicks. | Real-time social sentiment (VADER NLP). |
| **Bot Defense** | Post-request filtering (causes crashes). | Pre-queue Biometric Shield (intercepts latency). |
| **Inventory** | Static allocation based on old trends. | Dynamic multipliers via Prophet AI forecasting. |

---

## 🏗️ 3. SYSTEM ARCHITECTURE
[cite_start]Nike Pulse operates as a **Tri-Layer Intelligence Stack**[cite: 22]:

1.  **Biometric Shield (`biometric_filter.py`)**: Intercepts inhuman click-latency to drop bots at the "front door."
2.  **VADER Senses (`sentiment_nlp.py`)**: Scrapes and scores localized social buzz to generate a "Hype Multiplier."
3.  **Prophet Brain (`prophet_forecaster.py`)**: Processes 112k+ records to calculate demand baselines and applies the Hype Multiplier for final routing.

---

## 🛠️ 4. TECHNOLOGY STACK
* **Frontend:** React.js, Vite, Lucide-React, Tailwind CSS[cite: 23].
* [cite_start]**Backend:** Python 3.8+, FastAPI, Uvicorn[cite: 23].
* [cite_start]**AI/ML:** Facebook Prophet, VADER Sentiment Analysis[cite: 23].
* **Data:** Pandas, NumPy, JSON telemetry[cite: 23].

---

## 📁 5. PROJECT STRUCTURE
```text
backend/
│   ├── app.py                  # FastAPI Gateway
│   ├── biometric_filter.py      # Bot mitigation logic
│   ├── prophet_forecaster.py    # Time-series ML model
│   ├── sentiment_nlp.py         # Social sentiment engine
│   ├── requirements.txt         # Python dependencies
│   ├── mock_sales.csv           # 112k+ historical records
│   ├── social_data.csv          # Localized social strings
│   └── live_traffic.json        # Real-time telemetry feed
└── pulse-dashboard/            # React/Vite Frontend

🚀 6. SETUP & EXECUTION STEPS 

Prerequisites
Python 3.8+ & Node.js (npm)

Backend Setup
cd backend

python -m venv venv

source venv/bin/activate (Mac/Linux) or venv\Scripts\activate (Windows)

pip install -r requirements.txt

python app.py (Runs on Port 8000)

Frontend Setup
cd pulse-dashboard

npm install

npm run dev (Runs on Port 5173)
