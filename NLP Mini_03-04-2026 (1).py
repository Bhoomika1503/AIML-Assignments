import nltk
import random
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Download nltk data
nltk.download('punkt')

# ---------------- CHATBOT ---------------- #
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm fine!", "Doing good!", "Great!"],
    "your name": ["I am a chatbot.", "Call me ChatBot!"],
    "bye": ["Goodbye!", "See you later!"]
}

def chatbot():
    print("\nChatbot: Type 'bye' to exit")
    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("Chatbot: Goodbye!")
            break

        found = False
        for key in responses:
            if key in user_input:
                print("Chatbot:", random.choice(responses[key]))
                found = True
                break

        if not found:
            print("Chatbot: Sorry, I don't understand.")

# ---------------- FAKE NEWS DETECTOR ---------------- #
texts = [
    # REAL news
    "Government launches new health scheme",
    "India wins cricket match against Australia",
    "New education policy introduced",
    "Stock market reaches new high",
    "Scientists discover new vaccine",

    # FAKE news
    "Aliens landed in India yesterday",
    "Man becomes invisible after eating tablet",
    "Time travel machine invented in village",
    "Human can live without food for 1 year",
    "Magic pill makes you fly"
]

labels = [
    "real", "real", "real", "real", "real",
    "fake", "fake", "fake", "fake", "fake"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

def fake_news():
    user_input = input("\nEnter news: ")
    user_vec = vectorizer.transform([user_input])
    prediction = model.predict(user_vec)

    print("Prediction:", prediction[0])

# ---------------- KEYWORD EXTRACTOR ---------------- #
def keyword_extractor():
    text = input("\nEnter text: ")
    words = nltk.word_tokenize(text.lower())

    stopwords = ["the", "is", "and", "in", "to", "of", "a"]
    filtered = [word for word in words if word.isalnum() and word not in stopwords]

    freq = Counter(filtered)
    keywords = freq.most_common(5)

    print("Keywords:", keywords)

# ---------------- MAIN MENU ---------------- #
def main():
    while True:
        print("\n--- NLP MINI APP ---")
        print("1. Chatbot")
        print("2. Fake News Detector")
        print("3. Keyword Extractor")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            chatbot()
        elif choice == "2":
            fake_news()
        elif choice == "3":
            keyword_extractor()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()