 # Infinite-Loopers_Hackathon_SemiFinal

 👟 NIKE PULSE: AI-Driven Supply Chain Intelligence
 Bridging the gap between human desire and global logistics.

![Nike Pulse Header](https://img.shields.io/badge/Status-Live%20Demo-00f2fe?style=for-the-badge)
![Tech Stack](https://img.shields.io/badge/Stack-Python%20%7C%20React%20%7C%20Prophet%20%7C%20Vite-ff8c00?style=for-the-badge)



🌩️ THE PROBLEM: THE "SILENT" SELL-OUT
In the world of limited-edition sneakers, demand isn't a straight line—it’s a lightning strike. 

Traditional logistics systems are **reactive**. They look at what sold last week to decide what to ship next week. But by the time a sales spike shows up in the database, the shoes are already sold out, the fans are disappointed, and the scalper bots have won. 

**Nike Pulse** bridges this "Data Gap" by turning social media noise into actionable logistics signals before the first pair even leaves the warehouse.

---

## 🏗️ SYSTEM ARCHITECTURE
Nike Pulse operates as a **Tri-Layer Intelligence Stack**, built with a **Blade Runner 2049** aesthetic for high-intensity data visualization.

### 🛡️ Layer 1: The Biometric Shield (Security)
* **Tech:** Behavioral Latency Analysis.
* **Function:** Detects non-human interaction patterns to intercept automated scalper bots. 
* **Impact:** Prioritizes inventory for verified human customers, maintaining brand integrity.

### 📡 Layer 2: The VADER Senses (Perception)
* **Tech:** VADER Sentiment Analysis (NLP).
* **Function:** Scrapes and analyzes localized social sentiment live. 
* **Impact:** Calculates a "Hype Score" that acts as a leading indicator for demand surges in sub-regions like **Bandra** or **Howrah**.

### 🔮 Layer 3: The Prophet Brain (Prediction)
* **Tech:** Facebook Prophet (Time-Series Machine Learning).
* **Function:** Ingests **112,000+ historical records** to establish a baseline and applies the Hype Multiplier.
* **Impact:** Automates proactive stock allocation (e.g., boosting inventory by +15% based on real-time hype).

---

## 📂 DATA ENGINE & STRUCTURE
The system is powered by live-processed datasets included in this repository:

* **`mock_sales.csv`**: 112,000+ records of historical time-series data (`ds`, `y`, `region`, `sub_region`).
* **`social_data.csv`**: Real-time geolocated social sentiment strings used for the VADER NLP engine.
* **`data.json`**: Structured snapshot for rapid UI telemetry.

---

## 🚀 HOW TO RUN THE ENGINE

To replicate the Nike Pulse Command Center, you must run both the "Brain" and the "Face" simultaneously.

### 1. Initialize the AI Brain (Backend)
```bash
# Install core ML and API dependencies
pip install fastapi uvicorn pandas prophet vaderSentiment

# Start the FastAPI server
python -m uvicorn app:app --reload
```

### 2. Launch the Dashboard (Frontend)
```bash
# Navigate to the dashboard directory
cd pulse-dashboard

# Install React dependencies
npm install axios lucide-react

# Start the development server
npm run dev
```
**Access:** Navigate to `http://localhost:5173` to initialize the live data pipeline.

---

## 🛠️ TROUBLESHOOTING THE INSTALL
If the `prophet` library fails to install, your system may lack the necessary C++ compiler.

**Quick Fixes:**
1.  **Dependency first:** Run `pip install pystan` before installing prophet.
2.  **Conda users:** Use `conda install -c conda-forge fbprophet`.
3.  **File Paths:** Ensure all `.csv` files are in the same directory as `app.py`.
