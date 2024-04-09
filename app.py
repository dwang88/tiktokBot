from flask import Flask, request, render_template
import praw

app = Flask(__name__)

reddit = praw.Reddit(client_id='_cpjlH1l7PKcgC2nEPvUog',
                     client_secret='j2u7ssnhKIqqg879o_2fkYlSaRSqwQ',
                     user_agent='reddit popular post bot by u/dwang7')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_most_upvoted_post', methods=['POST'])
def get_most_upvoted_post():
    subreddit_link = request.form['subreddit_link']
    
    try:
        subreddit = reddit.subreddit(subreddit_link)
        top_post = next(subreddit.top(limit=1, time_filter='all'))
        
        top_post_title = top_post.title
        top_post_url = top_post.url
        top_post_upvotes = top_post.score
    except Exception as e:
        return f"Error: {str(e)}"
    
    return render_template('top_post.html', title=top_post_title, url=top_post_url, upvotes=top_post_upvotes)

if __name__ == '__main__':
    app.run(debug=True)
