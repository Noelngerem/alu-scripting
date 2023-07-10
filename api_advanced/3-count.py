import requests

def count_words(subreddit, word_list, after=None, count_dict=None):
    if count_dict is None:
        count_dict = {}
    
    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        
        for post in posts:
            title = post['data']['title']
            lowercase_title = title.lower()
            
            for word in word_list:
                lowercase_word = word.lower()
                
                if lowercase_word in lowercase_title:
                    if lowercase_word in count_dict:
                        count_dict[lowercase_word] += lowercase_title.count(lowercase_word)
                    else:
                        count_dict[lowercase_word] = lowercase_title.count(lowercase_word)
        
        after = data['data']['after']
        
        if after is not None:
            return count_words(subreddit, word_list, after, count_dict)
    
    sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
    
    for word, count in sorted_counts:
        print(f"{word}: {count}")

count_words("python", ["python", "javascript", "java"])
