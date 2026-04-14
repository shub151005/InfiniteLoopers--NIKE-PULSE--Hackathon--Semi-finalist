import json
import math

def calculate_distance(p1, p2):
    """Calculates the Euclidean distance between two [X, Y] points."""
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def is_human_trajectory(trajectory, latency_ms):
    """
    The Core Logic: 
    1. Humans take time to click (> 200ms).
    2. Humans move in messy curves. Bots move in perfect straight lines.
    """
    # Rule 1: The Latency Check (Too fast = Bot)
    if latency_ms < 200:
        return False, "Failed Latency (Too Fast)"

    # Rule 2: The Linearity Check (Too straight = Bot)
    if len(trajectory) < 2:
        return False, "Invalid Trajectory"

    # Calculate the literal straight line from start to finish
    start_point = trajectory[0]
    end_point = trajectory[-1]
    straight_line_dist = calculate_distance(start_point, end_point)

    # Calculate the actual messy path the mouse took
    actual_path_dist = 0
    for i in range(len(trajectory) - 1):
        actual_path_dist += calculate_distance(trajectory[i], trajectory[i+1])

    # Prevent division by zero if they didn't move the mouse
    if actual_path_dist == 0:
        return False, "Zero Movement"

    # Linearity Ratio: 1.0 means a mathematically perfect straight line
    linearity_ratio = straight_line_dist / actual_path_dist

    # If the path is > 95% straight, it's a machine
    if linearity_ratio > 0.95:
        return False, "Failed Biometrics (Too Linear)"

    return True, "Passed (Human Curve)"

def run_shield_simulation():
    """Reads the JSON file and filters the traffic."""
    print("🛡️ INITIALIZING PULSE BIOMETRIC SHIELD...\n")
    
    try:
        with open('live_traffic.json', 'r') as file:
            # Load the entire JSON object
            payload = json.load(file)
            
            # Extract JUST the list of sessions from the "traffic" key
            traffic_data = payload.get("traffic", [])
            
    except FileNotFoundError:
        print("Error: Could not find 'live_traffic.json'. Make sure it is in the same folder!")
        return

    human_count = 0
    bot_count = 0
    verified_payloads = []

    for request in traffic_data:
        is_human, reason = is_human_trajectory(request['trajectory'], request['latency_ms'])
        
        # Adding Region and Sub-Region to the terminal output for the demo!
        loc = f"{request['region']} - {request['sub_region']}"
        
        if is_human:
            human_count += 1
            verified_payloads.append(request)
            print(f"✅ [CLEARED] {request['session_id']} | Loc: {loc} | Reason: {reason}")
        else:
            bot_count += 1
            print(f"❌ [BLOCKED] {request['session_id']} | Loc: {loc} | Reason: {reason}")

    print("\n" + "="*50)
    print("📊 SHIELD DIAGNOSTIC REPORT")
    print("="*50)
    print(f"Total Requests Processed : {len(traffic_data)}")
    print(f"Malicious Bots Dropped   : {bot_count}")
    print(f"Verified Human Signals   : {human_count}")
    print("="*50)
    print("Routing verified signals to Prophet AI...\n")

# Run the test when you execute the file
if __name__ == "__main__":
    run_shield_simulation()