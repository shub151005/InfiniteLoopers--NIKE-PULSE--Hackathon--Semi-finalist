from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from prophet import Prophet
import warnings

# 1. SETUP: Ignore math warnings and initialize the AI Senses
warnings.filterwarnings('ignore')
app = FastAPI()
analyzer = SentimentIntensityAnalyzer()

# 2. SECURITY: Allow React to talk to this Python server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
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
            "score": f"{score:+.2f}",
            "status": "🔥 HIGH HYPE" if score > 0.2 else "😐 NEUTRAL"
        })
    return {"leaderboard": leaderboard}

@app.get("/api/allocation")
def get_live_allocation():
    """Runs the Facebook Prophet Brain LIVE on 112,000 records"""
    print("🔮 Running Live Prophet Forecast...")
    
    # A. Load Sales Data
    df_sales = pd.read_csv('mock_sales.csv')
    df_sales['ds'] = pd.to_datetime(df_sales['ds'])
    
    # B. Filter for Bandra (Our Demo Target)
    geo_data = df_sales[df_sales['sub_region'] == 'Bandra'][['ds', 'y']].groupby('ds').sum().reset_index()
    
    # C. Train Prophet (The "Brain" part)
    m = Prophet(weekly_seasonality=True, daily_seasonality=False, yearly_seasonality=False)
    m.fit(geo_data)
    
    # D. Predict Tomorrow
    future = m.make_future_dataframe(periods=1)
    forecast = m.predict(future)
    baseline = int(forecast.iloc[-1]['yhat'])
    
    # E. Calculate Multiplier from Social Data
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

@app.get("/api/shield")
def get_shield_stats():
    # Simulated Live Telemetry
    return {
        "total_requests": 1540,
        "bots_blocked": 1512,
        "humans_verified": 28,
        "recent_blocks": [{"id": "bot_99", "location": "Mumbai", "reason": "Non-Human Latency"}]
    }

import os
import uvicorn

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
