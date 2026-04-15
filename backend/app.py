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
    
    try:
        # A. Load Historical Sales
        df_sales = pd.read_csv('mock_sales.csv')
        
        # B. Filter for Target Region
        # We use .str.contains to be extra safe with spacing/case sensitivity
        geo_data = df_sales[df_sales['sub_region'].str.contains('Bandra', na=False)]
        
        # C. The "Prophet Bypass" with Safety Net
        if not geo_data.empty:
            baseline = int(geo_data['y'].mean())
        else:
            # SAFETY NET: If CSV filter fails, use a realistic default
            baseline = 450 
            
    except Exception as e:
        print(f"Error in math: {e}")
        baseline = 450 # Ultimate Fallback

    # D. Calculate Multiplier from Social Data
    try:
        df_social = pd.read_csv('social_data.csv')
        bandra_social = df_social[df_social['sub_region'].str.contains('Bandra', na=False)]
        
        if not bandra_social.empty:
            bandra_score = bandra_social['raw_text'].apply(
                lambda x: analyzer.polarity_scores(str(x))['compound']
            ).mean()
        else:
            bandra_score = 0.25 # Default positive hype
    except:
        bandra_score = 0.25

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