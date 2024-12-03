from wordfreq import word_frequency

def is_frequent_word(word, frequency_threshold):
    """
    Checks the frequency of a word in common English writing.

    Args:
        word (str): The word to check.
        frequency_threshold (float): Minimum acceptable frequency.

    Returns:
        bool: True if the word's frequency is above the threshold, False otherwise.
    """
    frequency = word_frequency(word, 'en')
    return frequency >= frequency_threshold

def find_matching_words(word_list, large_words_set, common_names_set, num_letters, frequency_threshold, apply_filters):
    """
    Identifies words that start and end with the same sequence of letters,
    ensuring no duplicates. Filtering options include frequency thresholds 
    and exclusion of common names.

    Args:
        word_list (list): List of words to search through.
        large_words_set (set): Set of valid English words.
        common_names_set (set): Set of common names to exclude (if filters enabled).
        num_letters (int): Number of letters to match at the beginning and end.
        frequency_threshold (float): Minimum acceptable frequency (if filters enabled).
        apply_filters (bool): Whether to apply filters for frequency and common names.

    Yields:
        str: Matching words.
    """
    min_word_length = num_letters + 1  # Ensure the word is long enough
    seen_words = set()  # Track seen words to eliminate duplicates

    for word in word_list:
        # Normalize word to lowercase to prevent case-sensitive duplicates
        word = word.lower()

        # Skip if the word has already been processed
        if word in seen_words:
            continue

        # Check word length
        if len(word) >= min_word_length:
            # Compare the first and last parts of the word
            first_part = word[:num_letters]
            last_part = word[-num_letters:]

            if first_part == last_part:
                if not apply_filters or (
                    word.isalpha() and
                    word in large_words_set and
                    is_frequent_word(word, frequency_threshold) and
                    word not in common_names_set
                ):
                    seen_words.add(word)  # Mark the word as seen
                    yield word  # Yield the unique matching word
