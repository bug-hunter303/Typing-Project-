def calculations(original, user , elapsed_time):
    match_count = 0
    min_length = min(len(original), len(user))

    for i in range(min_length):
        if user[i] == original[i]:
            match_count += 1
    
    total_char = len(original)
    character_accuracy_percentage = round((match_count/total_char) * 100,2)

    correct_words = 0
    original_words = original.split()
    user_words = user.split()
    for i in range(len(original_words)):
        if i < len(user_words):
            if original_words[i] == user_words[i]:
                correct_words += 1
    
    wpm = int((correct_words/elapsed_time) * 60)

    return {
        "accuracy": character_accuracy_percentage,
        "wpm":wpm,
        "elapsed_time": elapsed_time,
        "correct_words": correct_words,

    }
