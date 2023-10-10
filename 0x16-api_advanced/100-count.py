#!/usr/bin/python3
"""Task 3: Count it!"""
import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """Queries the Reddit API and returns the count of words in
    word_list in the titles of all the hot posts
    of the subreddit"""

    info = requests.get("https://www.reddit.com/r/{}/hot.json"
                        .format(subreddit),
                        params={"after": after},
                        headers={"User-Agent": "My-User-Agent"},
                        allow_redirects=False)
    if info.status_code != 200:
        return None

    hot_articles = [child.get("data").get("title")
                    for child in info.json()
                    .get("data")
                    .get("children")]
    if not hot_articles:
        return None

    word_list = list(dict.fromkeys(word_list))

    if word_count == {}:
        word_count = {word: 0 for word in word_list}

    for title in hot_articles:
        split_words = title.split(' ')
        for word in word_list:
            for s_word in split_words:
                if s_word.lower() == word.lower():
                    word_count[word] += 1

    if not info.json().get("data").get("after"):
        sorted_counts = sorted(word_count.items(), key=lambda kv: kv[0])
        sorted_counts = sorted(word_count.items(),
                               key=lambda kv: kv[1], reverse=True)
        [print('{}: {}'.format(k, v)) for k, v in sorted_counts if v != 0]
    else:
        return count_words(subreddit, word_list, word_count,
                           info.json().get("data").get("after"))
