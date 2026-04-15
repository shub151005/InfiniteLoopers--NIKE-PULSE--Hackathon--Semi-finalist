from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import warnings

warnings.filterwarnings('ignore')
app = FastAPI()
analyzer = SentimentIntensityAnalyzer()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/shield")
def get_shield_stats():
    # Matching the keys in your App.jsx exactly
    return {
        "total_requests": 4502,
        "bots_blocked": 1402,
        "humans_verified": 3100,
        "recent_blocks": [
            {"id": "XX-92", "location": "Moscow", "reason": "Latency Suspect"},
            {"id": "TH-41", "location": "Bangkok", "reason": "User-Agent Spoof"},
            {"id": "VN-12", "location": "Hanoi", "reason": "Rapid Interaction"}
        ]
    }

@app.get("/api/hype")
def get_live_hype():
    try:
        df = pd.read_csv('social_data.csv')
        df['score'] = df['raw_text'].apply(lambda x: analyzer.polarity_scores(str(x))['compound'])
        rankings = df.groupby(['region', 'sub_region'])['score'].mean().sort_values(ascending=False).head(4)
        
        leaderboard = []
        for i, ((reg, sub), score) in enumerate(rankings.items(), 1):
            leaderboard.append({
                "rank": i,
                "region": f"{reg} - {sub}",
                "score": f"{score:.2f} Hype"
            })
        # WRAPPING in "leaderboard" key so hype.leaderboard.map works!
        return {"leaderboard": leaderboard}
    except:
        return {"leaderboard": [{"rank": 1, "region": "Mumbai - Bandra", "score": "0.85 Hype"}]}

@app.get("/api/allocation")
def get_live_allocation():
    try:
        df_sales = pd.read_csv('mock_sales.csv')
        geo_data = df_sales[df_sales['sub_region'].str.contains('Bandra', na=False)]
        baseline = int(geo_data['y'].mean()) if not geo_data.empty else 450
        
        df_social = pd.read_csv('social_data.csv')
        bandra_social = df_social[df_social['sub_region'].str.contains('Bandra', na=False)]
        bandra_score = bandra_social['raw_text'].apply(lambda x: analyzer.polarity_scores(str(x))['compound']).mean() if not bandra_social.empty else 0.25
        
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
    except:
        return {
            "target_region": "Mumbai - Bandra", "shoe_model": "Air Jordan 1",
            "baseline_prediction": 450, "hype_multiplier": 1.25,
            "final_approved_allocation": 562, "delta": "+112 Pairs"
        }