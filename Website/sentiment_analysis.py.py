def classify_sentiment(sentence):
    positive_words = ["good", "great", "excellent", "happy", "joy", "love", "wonderful", "fantastic", "awesome", "amazing",
                  "beautiful", "delightful", "positive", "cheerful", "pleasure", "satisfying", "admire", "adore",
                  "brilliant", "charming", "fabulous", "glorious", "grateful", "lovely", "optimistic", "perfect",
                  "pleasant", "splendid", "terrific", "vibrant", "blessed", "blissful", "content", "ecstatic", "elated",
                  "euphoric", "graceful", "jovial", "magnificent", "radiant", "sunny", "upbeat", "victorious",
                  "wondrous", "zestful", "affectionate", "captivating", "celebratory", "divine", "enchanting", "fun",
                  "harmonious", "inspiring", "incredible", "invigorating", "magical", "mesmerizing", "optimistic",
                  "passionate", "refreshing", "rejuvenating", "satisfying", "serene", "spirited", "tranquil",
                  "uplifting", "wholesome", "admirable", "bountiful", "buoyant", "charismatic", "creative", "dazzling",
                  "exhilarating", "fulfilling", "glamorous", "innovative", "jubilant", "majestic", "miraculous",
                  "nurturing", "playful", "resplendent", "stunning", "thrilling", "vivacious", "zesty", "angelic",
                  "bubbly", "carefree", "colorful", "dynamic", "effervescent", "exuberant", "festive", "gleeful",
                  "heartwarming", "idyllic", "lively", "merry", "picturesque", "radiant", "splendorous", "uplifting"]

    negative_words = ["bad", "awful", "terrible", "horrible", "unhappy", "sad", "depressed", "miserable", "gloomy", "dismal",
                  "bleak", "disheartened", "disappointed", "unpleasant", "unfortunate", "inferior", "ugly", "dreadful",
                  "abominable", "atrocious", "appalling", "dire", "distressing", "pitiful", "gloomy", "dreary",
                  "melancholy", "woeful", "forlorn", "sorrowful", "heartbreaking", "tragic", "regretful", "grieving",
                  "anguished", "tormented", "wretched", "despondent", "downhearted", "dejected", "defeated", "despairing",
                  "hopeless", "pessimistic", "dismayed", "discouraged", "disconsolate", "dispirited", "demoralized",
                  "broken", "crestfallen", "crushed", "sullen", "glum", "morose", "blue", "grief-stricken", "woeful",
                  "anguished", "mournful", "piteous", "plaintive", "sorrowful", "tearful", "desolate", "isolated",
                  "lonely", "neglected", "rejected", "heartbroken", "alienated", "betrayed", "disowned", "forsaken",
                  "jilted", "bereft", "devastated", "disconsolate", "homeless", "destitute", "abandoned", "deprived",
                  "distressed", "excluded", "forgotten", "unwanted", "worthless", "humiliated", "rejected", "defeated",
                  "despised", "ridiculed", "shunned", "victimized", "unloved", "unappreciated", "underappreciated"]

    sarcasm_words = ["yeah", "right", "sure", "obviously", "totally", "definitely", "clearly", "absolutely", "naturally",
                 "naturally", "certainly", "indeed", "no doubt", "as if", "whatever", "oh yeah", "great idea", "big surprise",
                 "oh sure", "fantastic", "wonderful", "excellent", "terrific", "brilliant", "genius", "outstanding",
                 "remarkable", "impressive", "awesome", "incredible", "amazing", "astounding", "phenomenal", "fantabulous",
                 "wonderful", "splendid", "fabulous", "marvelous", "stupendous", "tremendous", "fantastic", "extraordinary",
                 "mind-blowing", "jaw-dropping", "unbelievable", "mind-boggling", "unreal", "unrealistic", "impossible",
                 "unthinkable", "inconceivable", "preposterous", "ridiculous", "absurd", "crazy", "ludicrous", "mad"]

    # Convert sentence to lowercase for case-insensitive matching
    sentence_lower = sentence.lower()

    # Check if sentence contains positive, negative, or sarcastic words
    positive_count = sum(1 for word in positive_words if word in sentence_lower)
    negative_count = sum(1 for word in negative_words if word in sentence_lower)
    sarcasm_count = sum(1 for word in sarcasm_words if word in sentence_lower)

    # Determine sentiment based on counts
    if positive_count > negative_count and sarcasm_count == 0:
        return "Positive"
    elif negative_count > positive_count and sarcasm_count == 0:
        return "Negative"
    elif sarcasm_count > 0:
        return "Sarcasm"
    else:
        return "Neutral"

def main():
    print("Welcome to the Sentiment Analysis tool!")
    while True:
        user_input = input("Enter a sentence (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Exiting...")
            break
        sentiment = classify_sentiment(user_input)
        print(f"The sentiment of \"{user_input}\" is: {sentiment}")

if __name__ == "__main__":
    main()


