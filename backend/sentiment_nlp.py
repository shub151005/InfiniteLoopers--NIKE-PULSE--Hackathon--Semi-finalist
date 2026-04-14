import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_social_hype():
    analyzer = SentimentIntensityAnalyzer()
    print("🧠 INITIALIZING VADER NLP SENSES...")
    print("Reading 2,000 social media data points...\n")

    # Dictionary to store all scores for each sub-region
    sub_region_scores = {}

    try:
        with open('social_data.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                region = row.get('region', 'Unknown').strip()
                sub_region = row.get('sub_region', 'Unknown').strip()
                text = row.get('raw_text', '').strip()

                if not text:
                    continue

                # VADER calculates a 'compound' score from -1.0 (extreme negative) to 1.0 (extreme positive)
                score = analyzer.polarity_scores(text)['compound']

                # Group the scores by neighborhood
                loc_key = f"{region} - {sub_region}"
                if loc_key not in sub_region_scores:
                    sub_region_scores[loc_key] = []
                
                sub_region_scores[loc_key].append(score)

    except FileNotFoundError:
        print("❌ Error: Could not find 'social_data.csv'. Make sure it is in the same folder!")
        return

    # Calculate averages and sort them from Highest Hype to Lowest Hype
    ranked_regions = []
    for loc, scores in sub_region_scores.items():
        avg_score = sum(scores) / len(scores)
        post_count = len(scores)
        ranked_regions.append((loc, avg_score, post_count))
    
    # Sort the list based on the average score (descending order)
    ranked_regions.sort(key=lambda x: x[1], reverse=True)

    print("📊 LOCALIZED HYPE LEADERBOARD ([-1.0 to +1.0])")
    print("="*65)
    print(f"{'STATUS'.ljust(12)} | {'NEIGHBORHOOD'.ljust(25)} | {'SCORE'.ljust(6)} | {'DATA POINTS'}")
    print("-" * 65)
    
    for loc, avg_score, count in ranked_regions:
        # Dashboard formatting based on the score thresholds
        if avg_score > 0.2:
            status = "🔥 HIGH HYPE "
        elif avg_score < -0.1:
            status = "📉 NEGATIVE  "
        else:
            status = "😐 NEUTRAL   "
            
        print(f"{status} | {loc.ljust(25)} | {avg_score:>+5.2f} | ({count} posts)")
        
    print("="*65)
    print("Routing ranked hype data to Prophet AI...\n")

if __name__ == "__main__":
    analyze_social_hype()