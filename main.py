import nltk
from tqdm import tqdm
from data_loader import load_large_english_dict, load_common_names
from filters import find_matching_words

nltk.download("words")

def remove_duplicates_from_list(word_list):
    """
    Removes duplicates from the final list by converting it to a set and back to a sorted list.

    Args:
        word_list (list): List of words to deduplicate and sort.

    Returns:
        list: Deduplicated and alphabetically sorted list of words.
    """
    deduplicated_words = sorted(set(word_list))  # Remove duplicates and sort
    print(f"Total words after final deduplication and sorting: {len(deduplicated_words)}")
    return deduplicated_words

def main():
    print("Enter the number of letters to match at the beginning and end of the word: ", end="")
    try:
        num_letters = int(input())
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    print("Do you want to include unusual words, names, or places? (y/n): ", end="")
    apply_filters_input = input().strip().lower()
    apply_filters = apply_filters_input == "n"

    frequency_threshold = None
    if apply_filters:
        print("Use the default frequency threshold (0.00000001)? (y/n): ", end="")
        use_default = input().strip().lower()
        if use_default == "y":
            frequency_threshold = 0.00000001
        elif use_default == "n":
            print("Enter your custom frequency threshold: ", end="")
            try:
                frequency_threshold = float(input())
            except ValueError:
                print("Invalid input. Using default threshold (0.00000001).")
                frequency_threshold = 0.00000001
        else:
            print("Invalid choice. Using default threshold (0.00000001).")
            frequency_threshold = 0.00000001

    print("Running program...")

    # Load word list
    all_words = nltk.corpus.words.words()

    # Load additional datasets
    large_words_set = load_large_english_dict()
    common_names_set = load_common_names() if apply_filters else set()

    # Process words
    results = list(
        tqdm(
            find_matching_words(
                all_words,
                large_words_set,
                common_names_set,
                num_letters,
                frequency_threshold,
                apply_filters,
            ),
            desc="Processing words",
            total=len(all_words),
        )
    )

    # Remove duplicates and sort the final results
    results = remove_duplicates_from_list(results)

    if results:
        print(f"Words that start and end with the same {num_letters} letters:")
        print(", ".join(results))
    else:
        print(f"No words found that start and end with the same {num_letters} letters.")

    print(f"\nTotal matching words found: {len(results)}")

if __name__ == "__main__":
    main()