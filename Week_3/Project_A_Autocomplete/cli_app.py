import os
from autocomplete_engine import AutocompleteEngine

def load_sample_corpus():
    """
    Returns a larger text corpus to make predictions more interesting.
    In a real-world app, you would read from a massive text file or database.
    """
    return """
    Machine learning is a subfield of artificial intelligence. 
    Machine code is understood by computers. 
    Machine learning engineers build predictive models. 
    Artificial intelligence is transforming software engineering.
    Software engineers write clean code.
    Machine learning algorithms require large amounts of data.
    Data science relies heavily on statistics and probability.
    Artificial neural networks mimic the human brain.
    Deep learning is a subset of machine learning.
    Software engineering practices ensure reliable systems.
    """

def run_cli():
    print("Initializing Autocomplete Engine...")
    engine = AutocompleteEngine()
    
    corpus = load_sample_corpus()
    engine.train(corpus)
    
    print("\n=================================================")
    print("🚀 Autocomplete CLI Online [Phase 2 Project]")
    print("Type a sentence. The engine will use the previous word")
    print("as the 'state' and the current word as the 'prefix'.")
    print("Type 'EXIT' to quit.")
    print("=================================================\n")
    
    while True:
        try:
            # Get user input
            user_input = input(">> ").strip().lower()
            
            if user_input == 'exit':
                print("Shutting down engine... Goodbye!")
                break
            if not user_input:
                continue
                
            # Tokenize the input to find context and prefix
            words = user_input.split()
            
            if len(words) == 1:
                context = ""  # No history, essentially a Unigram model
                prefix = words
            else:
                context = words[-2] # The word immediately preceding the current typing
                prefix = words[-1]  # The word currently being typed
            
            # Query the engine
            suggestions = engine.suggest(context, prefix)
            
            # Apply Decision Theory: Maximize Expected Utility by showing Top 3
            if suggestions:
                print(f"   [Predictions for '{prefix}' following '{context} भी']: ")
                # Display only the top 3 most probable suggestions
                for word, prob in suggestions[:3]:
                    # If prob is 0.0, it means it's mathematically possible via Trie, 
                    # but never seen together in Markov Chain.
                    print(f"   -> {word:<15} (Confidence: {prob:.2%})")
            else:
                print(f"   [No suggestions found in vocabulary for '{prefix}']")
                
        except KeyboardInterrupt:
            print("\nShutting down engine... Goodbye!")
            break

# ==========================================
# EXECUTION
# ==========================================
if __name__ == "__main__":
    run_cli()