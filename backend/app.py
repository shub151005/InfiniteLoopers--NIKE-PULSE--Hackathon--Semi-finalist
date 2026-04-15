from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import warnings

# 1. SETUP: Ignore math warnings and initialize the AI Senses
warnings.filterwarnings('ignore')
app = FastAPI()
analyzer = SentimentIntensityAnalyzer()

# The CORS Permission Slip
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from ANY website (perfect for the hackathon demo)
    allow_credentials=True,
    allow_methods=["*"],  # Allows GET, POST, etc.
    allow_headers=["*"],
)

@app.get("/api/hype")
def get_live_hype():
    """Reads social_data.csv and calculates the leaderboard LIVE"""
    print("🧠 Analyzing Social Hype Live...")
    df = pd.read_csv('social_data.csv')
    
    # Calculate sentiment score for every single row
    df['score'] = df['raw_text'].apply(lambda x: analyzer.polarity_scores(str(x))['compound'])
    
    # Group by neighborhood and get the average
    rankings = df.groupby(['region', 'sub_region'])['score'].mean().sort_values(ascending=False).head(4)
    
    leaderboard = []
    for i, ((reg, sub), score) in enumerate(rankings.items(), 1):
        leaderboard.append({
            "rank": i,
            "region": f"{reg} - {sub}",
            "score": f"{score:.2f} Hype"
        })
    return leaderboard

@app.get("/api/shield")
def get_shield_stats():
    # Simulated Live Telemetry
    return {
        "status": "Active",
        "bots_blocked": 1402,
        "threat_level": "Low"
    }

@app.get("/api/allocation")
def get_live_allocation():
    """Bypass Protocol: Lightweight Statistical Baseline + Live Hype"""
    print("🔮 Running Allocation Matrix (Lightweight Mode)...")
    
    # A. Load Historical Sales
    df_sales = pd.read_csv('mock_sales.csv')
    
    # B. Filter for Target Region (Bandra)
    geo_data = df_sales[(df_sales['region'] == 'India') & (df_sales['sub_region'] == 'Bandra')][['ds', 'y']].groupby('ds').sum().reset_index()
    
    # C. The "Prophet Bypass" (Statistical Moving Average)
    # Instead of compiling C++, we use a 7-day historical average to generate the baseline.
    geo_data = geo_data.sort_values('ds')
    if len(geo_data) >= 7:
        baseline = int(geo_data['y'].tail(7).mean())
    else:
        baseline = int(geo_data['y'].mean()) # Fallback
    
    # D. Calculate Multiplier from Social Data (VADER is still working!)
    df_social = pd.read_csv('social_data.csv')
    bandra_score = df_social[df_social['sub_region'] == 'Bandra']['raw_text'].apply(
        lambda x: analyzer.polarity_scores(str(x))['compound']
    ).mean()
    
    multiplier = 1.0 + (bandra_score * 1.0)
    final = int(baseline * multiplier)
    
    return {
        "target_region": "Mumbai - Bandra",
        "shoe_model": "Air Jordan 1",
        "baseline_prediction": baseline,
        "hype_multiplier": round(multiplier, 2),
        "final_approved_allocation": final,
        "delta": f"+{final - baseline} Pairs"
    }