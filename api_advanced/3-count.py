#!/usr/bin/python3

import praw
import re

def count_words(subreddit, word_list):
  """
  Queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords.

  Args:
    subreddit: The name of the subreddit to query.
    word_list: A list of keywords to count.

  Returns:
    None.
  """

  reddit = praw.Reddit(client_id="YOUR_CLIENT_ID",
                       client_secret="YOUR_CLIENT_SECRET",
                       user_agent="YOUR_USER_AGENT")

  hot_articles = reddit.subreddit(subreddit).hot(limit=100)

  word_counts = {}
  for article in hot_articles:
    title = article.title
    for word in word_list:
      word = word.lower()
      match = re.search(rf"\b{word}\b", title)
      if match:
        word_counts[word] = word_counts.get(word, 0) + 1

  sorted_word_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

  for word, count in sorted_word_counts:
    print(f"{word}: {count}")


if __name__ == "__main__":
  count_words("programming", ["python", "javascript", "java"])

