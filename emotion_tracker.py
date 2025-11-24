import datetime

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


def detect_emotions(text):
    text = text.lower()

    emotions = {
        "Happy": ["happy", "great", "good", "excited", "joy", "awesome", "positive"],
        "Sad": ["sad", "down", "unhappy", "depressed", "cry", "lonely"],
        "Angry": ["angry", "annoyed", "irritated", "frustrated", "mad", "furious"],
        "Anxious": ["worried", "nervous", "anxious", "stress", "overthinking", "panic"],
        "Confused": ["confused", "lost", "uncertain", "don’t know", "unsure"],
        "Tired": ["tired", "exhausted", "sleepy", "fatigue", "drained"],
    }

    scores = {emotion: 0 for emotion in emotions}

    for emotion, keywords in emotions.items():
        for word in keywords:
            if word in text:
                scores[emotion] += 1

    if all(score == 0 for score in scores.values()):
        return [("Unknown", 0)]

    sorted_emotions = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [(emotion, score) for emotion, score in sorted_emotions if score > 0]


def reflection_message(emotion):
    messages = {
        "Happy": "You're feeling positive! That’s great—moments like these matter.",
        "Sad": "It's okay to feel sad sometimes. Your feelings are valid.",
        "Angry": "Anger usually points to something important. You’re not wrong to feel this.",
        "Anxious": "Anxiety is your mind trying to protect you. You’re doing your best.",
        "Confused": "Confusion means you're in the middle of understanding something.",
        "Tired": "Your body and mind might be asking for rest. Listen when you can.",
        "Unknown": "I can’t identify the exact emotion, but I'm here to reflect with you."
    }
    return messages.get(emotion, messages["Unknown"])


def suggestions(emotion):
    tips = {
        "Happy": [
            "Write down what made you happy—to revisit later.",
            "Share your positive energy with someone close.",
            "Celebrate the small wins."
        ],
        "Sad": [
            "Try journaling your thoughts for 5 minutes.",
            "Go for a slow walk to reset your mind.",
            "Talk to someone you trust—it helps lighten the feeling."
        ],
        "Angry": [
            "Try the 4-7-8 breathing technique.",
            "Release energy through a walk or stretching.",
            "Write your thoughts and read them after 10 minutes."
        ],
        "Anxious": [
            "Try grounding: Look around and name 5 things you see.",
            "Take 5 slow breaths to calm your nervous system.",
            "Write down your biggest worry and challenge it logically."
        ],
        "Confused": [
            "Break your thoughts into smaller parts.",
            "Explain the situation to yourself in writing.",
            "Step away for 5 minutes and return with fresh clarity."
        ],
        "Tired": [
            "Drink some water and stretch lightly.",
            "Take a power nap if possible.",
            "Reduce screen time for a bit to refresh."
        ],
        "Unknown": [
            "Try noting what’s on your mind right now.",
            "Take 3 deep breaths.",
            "Do something comforting like music or warm tea."
        ]
    }
    return tips.get(emotion, tips["Unknown"])


def save_log(text, primary_emotion):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("emotion_log.txt", "a") as f:
        f.write(f"[{now}] Feeling: {text} | Emotion: {primary_emotion}\n")


def main():
    print(Colors.BOLD + Colors.OKBLUE + "\n✨ Advanced Emotion Reflector ✨" + Colors.ENDC)
    user_text = input("How are you feeling today?\n> ")

    detected = detect_emotions(user_text)

    # Primary Emotion
    primary_emotion, score = detected[0]

    print("\n" + Colors.BOLD + "Detected Emotions (Ranked):" + Colors.ENDC)
    for emotion, score in detected:
        print(f" - {emotion} (score: {score})")

    print("\n" + Colors.OKGREEN + "Reflection:" + Colors.ENDC)
    print(reflection_message(primary_emotion))

    print("\n" + Colors.WARNING + "✨ Suggested Actions:" + Colors.ENDC)
    for tip in suggestions(primary_emotion):
        print("-", tip)

    save = input("\nDo you want to save this entry? (yes/no): ")
    if save.lower() == "yes":
        save_log(user_text, primary_emotion)
        print(Colors.OKBLUE + "Your entry has been saved!" + Colors.ENDC)

    print("\nThank you for sharing. 💛")


main()