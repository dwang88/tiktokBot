# How to run program

1. Deploy Python App 
```
python app.py
```

2. Invoke Web Request (replace 'AskReddit' with any subreddit eg. UCSD)

```
Invoke-WebRequest -Uri "http://127.0.0.1:5000/get_most_upvoted_post?subreddit_link=AskReddit" -Method GET
```