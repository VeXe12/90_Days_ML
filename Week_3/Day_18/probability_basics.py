import random

def simulate_law_of_large_numbers(num_trials):
    """
    Simulates coin flips to demonstrate how empirical probability 
    converges to theoretical probability (0.5) as N increases.
    """
    print(f"\n--- Simulating {num_trials} Coin Flips ---")
    
    heads_count = 0
    
    # Checkpoints to log progress
    checkpoints = {10, 100, 1000, 10000, 100000, 1000000}
    
    for i in range(1, num_trials + 1):
        # Simulate flip: 1 = Heads, 0 = Tails
        flip = random.randint(0, 1)
        heads_count += flip
        
        if i in checkpoints:
            probability = heads_count / i
            error = abs(probability - 0.5)
            print(f"Trials: {i:<7} | Heads Ratio: {probability:.5f} | Error: {error:.5f}")

def bayes_theorem_calculator(p_h, p_e_given_h, p_e_given_not_h):
    """
    Calculates P(H|E) using Bayes' Theorem.
    
    Args:
        p_h: Prior probability of Hypothesis H (e.g., probability of having the disease)
        p_e_given_h: Probability of Evidence E given H is true (Sensitivity/True Positive Rate)
        p_e_given_not_h: Probability of Evidence E given H is false (False Positive Rate)
    
    Returns:
        Posterior probability P(H|E)
    """
    # 1. Calculate P(Not H)
    p_not_h = 1 - p_h
    
    # 2. Calculate Total Probability of Evidence P(E)
    # P(E) = P(E|H)*P(H) + P(E|~H)*P(~H)
    p_e = (p_e_given_h * p_h) + (p_e_given_not_h * p_not_h)
    
    # 3. Apply Bayes' Rule: P(H|E) = P(E|H) * P(H) / P(E)
    p_h_given_e = (p_e_given_h * p_h) / p_e
    
    return p_h_given_e

# ==========================================
# EXECUTION
# ==========================================
if __name__ == "__main__":
    # PART 1: The Law of Large Numbers
    # Watch how the "Error" shrinks as Trials increase.
    # This explains why ML models need MORE data to reduce variance.
    simulate_law_of_large_numbers(100000)

    # PART 2: Bayes' Theorem (The Medical Diagnostic Problem)
    # Scenario:
    # - A rare disease affects 1% of the population (Prior: 0.01).
    # - The test is 99% accurate for sick people (Sensitivity: 0.99).
    # - The test has a 5% False Positive rate for healthy people (False Positive: 0.05).
    
    print(f"\n--- Bayes' Theorem: Medical Test Scenario ---")
    prob_disease = 0.01          # P(Disease)
    sensitivity = 0.99           # P(Positive | Disease)
    false_positive_rate = 0.05   # P(Positive | No Disease)

    posterior = bayes_theorem_calculator(prob_disease, sensitivity, false_positive_rate)
    
    print(f"Prior Belief P(Disease): {prob_disease * 100}%")
    print(f"Evidence: The test came back POSITIVE.")
    print(f"Updated Belief P(Disease | Positive): {posterior:.4f} ({posterior*100:.2f}%)")
    
    print("\nInsight: Even with a 99% accurate test, the probability is low (16%) because the disease is so rare.")
    print("This counter-intuitive result is why machines use Bayes instead of gut feeling.")
