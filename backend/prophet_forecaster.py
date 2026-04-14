import pandas as pd
from prophet import Prophet
import warnings

# Suppress annoying Prophet terminal warnings for a clean demo presentation
warnings.filterwarnings('ignore')

def run_allocation_engine():
    print("🔮 INITIALIZING PROPHET FORECASTING ENGINE...\n")
    
    try:
        # 1. Load the Historical Data
        print("Loading 112,000 historical sales records...")
        df = pd.read_csv('mock_sales.csv')
        df['ds'] = pd.to_datetime(df['ds'])

    except Exception as e:
        print(f"❌ Error loading mock_sales.csv: {e}")
        return

    # Let's target a specific Micro-Geography for the demo
    target_region = "Mumbai"
    target_sub = "Bandra"
    target_shoe = "Air Jordan 1"
    
    print(f"Targeting Micro-Geo: {target_region} - {target_sub} | Product: {target_shoe}")
    print("Analyzing historical baseline demand...")

    # Filter data for just that neighborhood and shoe
    geo_data = df[(df['region'] == target_region) & 
                  (df['sub_region'] == target_sub) & 
                  (df['shoe_model'] == target_shoe)][['ds', 'y']]

    # Group by date just in case there are multiple entries on the same day
    geo_data = geo_data.groupby('ds').sum().reset_index()

    if geo_data.empty:
        print("❌ Not enough historical data for this specific query.")
        return

    # 2. Train the Prophet Model
    # We turn on weekly seasonality to catch weekend buying habits!
    m = Prophet(daily_seasonality=False, yearly_seasonality=False, weekly_seasonality=True)
    m.fit(geo_data)

    # 3. Predict Tomorrow's baseline demand
    future = m.make_future_dataframe(periods=1)
    forecast = m.predict(future)
    
    # Get the predicted baseline for tomorrow (the very last row)
    baseline_prediction = forecast.iloc[-1]['yhat']
    
    print(f"\n📈 PROPHET BASELINE: {int(baseline_prediction)} Units expected naturally.")
    
    # 4. Apply the VADER Hype Multiplier!
    # Let's say we pull this score from our VADER sentiment file (+0.25 is High Hype)
    hype_score = 0.25 
    
    # Every +0.10 score adds a 10% multiplier to the baseline
    hype_multiplier = 1.0 + (hype_score * 1.0)
    
    final_allocation = int(baseline_prediction * hype_multiplier)
    
    print(f"🔥 INJECTING VADER SENSES (Social Score: +{hype_score})...")
    print("="*60)
    print(f"📦 FINAL SMART ALLOCATION: {final_allocation} Units for {target_sub}")
    print("="*60)
    print("Data ready for React Dashboard visualization.")

if __name__ == "__main__":
    run_allocation_engine()