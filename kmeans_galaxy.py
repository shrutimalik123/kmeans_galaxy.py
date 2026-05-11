import random

def kmeans_galaxy_game():
    # 1. Dataset: Unlabeled "Space Objects"
    # Objects have (Brightness, Distance)
    print("--- 🌌 THE CLUSTER COMMANDER: k-MEANS GALAXY 🌌 ---")
    print("Mission: Group unlabeled space objects into distinct clusters.")
    print("Goal: Find the 'Centroids' that best represent your groups.")

    # 2. Hyperparameter: k (Number of Clusters)
    print("\n--- STEP 1: DEFINE k ---")
    print("How many types of objects do you think are in this sector? (k)")
    try:
        k = int(input("Enter k (e.g., 2 or 3): "))
    except ValueError:
        k = 2

    # 3. Initialization: Random Centroids
    print(f"\n--- 🖥️ INITIALIZING {k} CLUSTER CENTROIDS... ---")
    centroids = [{"b": random.randint(1, 10), "d": random.randint(1, 10)} for _ in range(k)]
    
    for i, c in enumerate(centroids):
        print(f"Centroid {i+1} starting position: Brightness={c['b']}, Distance={c['d']}")

    # 4. Simulation of Assignment and Update
    # In real k-Means, this repeats until the centroids stop moving[span_2](start_span)[span_2](end_span)[span_3](start_span)[span_3](end_span).
    print("\n--- 🛰️ ASSIGNING OBJECTS TO NEAREST CENTROID... ---")
    print("Algorithm: Calculating Euclidean Distance for every star and planet...")
    
    # Simulate a "Move" toward the mean of assigned points
    for i in range(len(centroids)):
        centroids[i]['b'] += random.randint(-1, 1) # Centroids drift to the 'center'
        centroids[i]['d'] += random.randint(-1, 1)

    # 5. Final Convergence
    print("\n--- ✨ CONVERGENCE REACHED ---")
    for i, c in enumerate(centroids):
        print(f"Final Category {i+1} Profile: Brightness Avg={c['b']}, Distance Avg={c['d']}")

    print("\nANALYSIS:")
    if k == 3:
        print("🏆 COSMIC EXPLORER: You found the distinct groups of Stars, Planets, and Nebulae!")
    else:
        print("📋 STABLE: You have grouped the data. Try a different 'k' to see if more patterns emerge.")

if __name__ == "__main__":
    kmeans_galaxy_game()
