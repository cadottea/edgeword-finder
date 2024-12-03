import os
import pickle
import urllib.request
import requests
import json

# Load configuration
with open("config.json", "r") as f:
    CONFIG = json.load(f)

def cache_data(filename, data=None):
    """
    Caches data to a file or loads it if it exists.

    Args:
        filename (str): Name of the cache file.
        data (any): Data to save. If None, loads the cached data.

    Returns:
        any: Cached data if it exists, otherwise None.
    """
    if data is None:
        if os.path.exists(filename):
            with open(filename, "rb") as f:
                return pickle.load(f)
        return None
    else:
        with open(filename, "wb") as f:
            pickle.dump(data, f)

def fetch_url(url):
    """
    Fetches the content of a URL with error handling.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: Content of the URL as a string, or None if an error occurs.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def load_large_english_dict():
    """
    Loads a large English dictionary, caching it locally for efficiency.

    Returns:
        set: A set of unique words from combined dictionaries.
    """
    cached_data = cache_data("words_cache.pkl")
    if cached_data:
        return cached_data

    urls = CONFIG["urls"]
    all_words = set()
    for url in urls:
        content = fetch_url(url)
        if content:
            words_list = content.splitlines()
            all_words.update([word.strip().lower() for word in words_list if len(word.strip()) >= 4])

    cache_data("words_cache.pkl", all_words)
    return all_words

def load_common_names():
    """
    Loads a list of common first names, caching it locally.

    Returns:
        set: A set of common names normalized to lowercase.
    """
    cached_data = cache_data("names_cache.pkl")
    if cached_data:
        return cached_data

    url = CONFIG["names_url"]
    content = fetch_url(url)
    if content:
        common_names = {name.strip().lower() for name in content.splitlines()}
        cache_data("names_cache.pkl", common_names)
        return common_names

    return set()