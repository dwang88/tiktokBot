from flask import Flask, request
import praw

app = Flask(__name__)

# Configure Reddit API
reddit = praw.Reddit(client_id='_cpjlH1l7PKcgC2nEPvUog',
                     client_secret='j2u7ssnhKIqqg879o_2fkYlSaRSqwQ',
                     user_agent='reddit popular post bot by u/dwang7')

@app.route('/get_most_upvoted_post', methods=['GET'])
def get_most_upvoted_post():
    subreddit_link = request.args.get('subreddit_link')
    subreddit = reddit.subreddit(subreddit_link)
    top_post = next(subreddit.top(limit=1, time_filter='all'))
    return {
        'title': top_post.title,
        'url': top_post.url,
        'upvotes': top_post.score
    }

if __name__ == '__main__':
    app.run(debug=True)
