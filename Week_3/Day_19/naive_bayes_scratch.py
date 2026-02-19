import math
from collections import defaultdict

class NaiveBayesClassifier:
    def __init__(self):
        self.vocab = set()
        self.class_counts = defaultdict(int)
        self.word_counts = defaultdict(lambda: defaultdict(int))
        self.total_words_per_class = defaultdict(int)
        self.total_docs = 0

    def tokenize(self, text):
        """Converts text to lowercase and splits into words."""
        return text.lower().split()

    def fit(self, X, y):
        """
        Trains the model (Maximum Likelihood Estimation).
        X: List of text strings.
        y: List of corresponding labels.
        """
        self.total_docs = len(X)
        
        for text, label in zip(X, y):
            self.class_counts[label] += 1
            words = self.tokenize(text)
            
            for word in words:
                self.vocab.add(word)
                self.word_counts[label][word] += 1
                self.total_words_per_class[label] += 1

    def predict(self, text):
        """Predicts the class of a new text string."""
        words = self.tokenize(text)
        best_class = None
        max_log_prob = float('-inf')

        # Calculate probability for each class
        for label in self.class_counts:
            # 1. Calculate the Log Prior: log(P(Class))
            # P(Class) = (Docs in Class) / (Total Docs)
            prior = self.class_counts[label] / self.total_docs
            log_prob = math.log(prior)

            # 2. Calculate the Log Likelihood: log(P(Word | Class))
            for word in words:
                # LAPLACE SMOOTHING: Add 1 to numerator, add vocab size to denominator
                # This prevents P(Word | Class) from ever being exactly 0
                word_count = self.word_counts[label][word]
                total_words = self.total_words_per_class[label]
                vocab_size = len(self.vocab)
                
                # P(Word | Class)
                likelihood = (word_count + 1) / (total_words + vocab_size)
                
                # Add log likelihoods (instead of multiplying raw probabilities)
                log_prob += math.log(likelihood)

            print(f"Log-Probability for '{label}': {log_prob:.4f}")

            # 3. Keep track of the class with the highest probability
            if log_prob > max_log_prob:
                max_log_prob = log_prob
                best_class = label

        return best_class

# ==========================================
# EXECUTION
# ==========================================
if __name__ == "__main__":
    # 1. A small training dataset
    X_train = [
        "the team won the championship game",
        "the quarterback threw a touchdown",
        "the election results are in",
        "the senator gave a speech today",
        "the president signed the new bill",
        "the player scored a goal"
    ]
    y_train = ["Sports", "Sports", "Politics", "Politics", "Politics", "Sports"]

    # 2. Initialize and Train
    nb = NaiveBayesClassifier()
    nb.fit(X_train, y_train)
    
    print(f"Training Complete. Vocabulary Size: {len(nb.vocab)} words\n")

    # 3. Test on a completely new headline
    # Notice that "won" and "game" lean Sports, but "the" and "a" are neutral.
    test_headline = "the team won a great game"
    
    print(f"Testing Headline: '{test_headline}'")
    prediction = nb.predict(test_headline)
    print(f"\nPrediction: ---> {prediction} <---")
