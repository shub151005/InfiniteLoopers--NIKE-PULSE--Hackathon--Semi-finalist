 # Infinite-Loopers_Hackathon_SemiFinal

 👟 NIKE PULSE: AI-Driven Supply Chain Intelligence
 Bridging the gap between human desire and global logistics.

![Nike Pulse Header](https://img.shields.io/badge/Status-Live%20Demo-00f2fe?style=for-the-badge)
![Tech Stack](https://img.shields.io/badge/Stack-Python%20%7C%20React%20%7C%20Prophet%20%7C%20Vite-ff8c00?style=for-the-badge)



🌩️ THE PROBLEM: THE "SILENT" SELL-OUT
In the world of limited-edition sneakers, demand isn't a straight line—it’s a lightning strike. 

Traditional logistics systems are **reactive**. They look at what sold last week to decide what to ship next week. But by the time a sales spike shows up in the database, the shoes are already sold out, the fans are disappointed, and the scalper bots have won. 

Nike Pulse bridges this "Data Gap" by turning social media noise into actionable logistics signals before the first pair even leaves the warehouse.

🏗️ SYSTEM ARCHITECTURE
Nike Pulse operates as a **Tri-Layer Intelligence Stack**, built with a **Blade Runner 2049** aesthetic for high-intensity data visualization.

🛡️ Layer 1: The Biometric Shield (Security)
* Tech:Behavioral Latency Analysis.
* unction:Detects non-human interaction patterns to intercept automated scalper bots. 
* Impact:Prioritizes inventory for verified human customers, maintaining brand integrity.

📡 Layer 2: The VADER Senses (Perception)
* Tech: VADER Sentiment Analysis (NLP).
* Function: Scrapes and analyzes localized social sentiment live. 
* Impact: Calculates a "Hype Score" that acts as a leading indicator for demand surges in sub-regions like **Bandra** or **Howrah**.

🔮 Layer 3: The Prophet Brain (Prediction)
* Tech: Facebook Prophet (Time-Series Machine Learning).
* Function: Ingests **112,000+ historical records** to establish a baseline and applies the Hype Multiplier.
* Impact: Automates proactive stock allocation (e.g., boosting inventory by +15% based on real-time hype).

 📂 DATA ENGINE & STRUCTURE
The system is powered by live-processed datasets included in this repository:
* mock_sales.csv: 112,000+ records of historical time-series data (`ds`, `y`, `region`, `sub_region`).
* social_data.csv: Real-time geolocated social sentiment strings used for the VADER NLP engine.
* data.json: Structured snapshot for rapid UI telemetry.


🚀 PROPER SETUP & INSTALLATION

To run Nike Pulse locally, you will need to initialize the backend AI engine and the frontend React dashboard. We highly recommend using a Python Virtual Environment to keep the machine learning dependencies clean.
Prerequisites
* Python 3.8+ installed on your system.
* Node.js & npm installed.
Step1 : Clone the Repository.
Step 2: Initialize the AI Brain (Backend)
It is best practice to run the ML models inside an isolated environment to prevent library conflicts.

A. Create and Activate Virtual Environment:
bash
 
B. Install Core API & Data Handling:
bash
pip install fastapi uvicorn pandas numpy

C. Install the Intelligence Models (Prophet & VADER):**
*Note: We install `pystan` first as it is the required C++ backend for Prophet.*
bash
pip install pystan
pip install prophet
pip install vaderSentiment


D. Start the Live Server:
bash
 The API will boot up on port 8000
python -m uvicorn app:app --reload

Step 3: Launch the Dashboard (Frontend)
Open a **second, separate terminal** and leave the Python backend running.

bash
 Navigate to the UI directory
cd pulse-dashboard

 Install React dependencies (Vite, Tailwind, Lucide Icons)
npm install

 Start the Blade Runner UI
npm run dev

🎯 Final Access:** Once both terminals are live, open your browser and navigate to `http://localhost:5173` to enter the command center.
why this version is a massive flex:
1. Virtual Environments (`venv`):** Adding this step proves you understand how real-world software is deployed. It protects the judges' computers from getting messy.
   2.Separated ML Installs: By explicitly separating `fastapi` from `prophet` and `vaderSentiment`, you are showing them exactly *where* the AI lives in the stack. 
3. The `pystan` note: Explaining *why* `pystan` is there (as a C++ backend for Prophet) shows you actually understand how the library works under the hood.

Access: Navigate to `http://localhost:5173` to initialize the live data pipeline.

---

🛠️ TROUBLESHOOTING THE INSTALL
If the `prophet` library fails to install, your system may lack the necessary C++ compiler.

Quick Fixes:
1.  Dependency first: Run `pip install pystan` before installing prophet.
2.  Conda users: Use `conda install -c conda-forge fbprophet`.
3.   Paths: Ensure all `.csv` files are in the same directory as `app.py`.
