from textblob import TextBlob

def get_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the sentiment polarity
    polarity = blob.sentiment.polarity
    
    # Determine the sentiment
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

if __name__ == '__main__':
    # Read input from the user
    user_input = input("Enter a sentence to analyze its sentiment: ")
    
    # Analyze the sentiment of the user's input
    sentiment = get_sentiment(user_input)
    
    # Display the result
    print(f"The sentiment of the text is: {sentiment}")