from flask import Flask, request, render_template
import praw
import random

app = Flask(__name__)

# Initialize Reddit API
reddit = praw.Reddit(client_id='_cpjlH1l7PKcgC2nEPvUog',
                     client_secret='j2u7ssnhKIqqg879o_2fkYlSaRSqwQ',
                     user_agent='reddit popular post bot by u/dwang7')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_most_upvoted_post', methods=['POST'])
def get_most_upvoted_post():
    subreddit_url = request.form['subreddit_url']
    
    try:
        # Extract subreddit name from the URL
        subreddit_name = subreddit_url.split('/r/')[-1].split('/')[0]
        
        # Fetch information about the top post from the specified subreddit
        subreddit = reddit.subreddit(subreddit_name)
        
        # Fetch the top post within the past day
        top_post = next(subreddit.top(limit=1, time_filter='day'))
        
        # Get information about the top post
        top_post_title = top_post.title
        top_post_url = top_post.url
        top_post_upvotes = top_post.score
        top_post_subreddit = top_post.subreddit.display_name
        top_post_author = top_post.author.name
        subreddit_icon_url = subreddit.icon_img
        num_comments = top_post.num_comments
        post_time = random.randint(1, 23)
        comment_time = random.randint(post_time, post_time)

        
        # Fetch the top 7 comments of the top post
        top_comments = []
        for comment in top_post.comments[:7]:
            if isinstance(comment, praw.models.Comment):
                comment_info = {
                    'text': comment.body,
                    'username': comment.author.name,
                    'avatar_url': comment.author.icon_img,
                    'upvotes': comment.score
                }
                top_comments.append(comment_info)
        
        # Render a template with the information about the top post and top comments
        return render_template('top_post.html', title=top_post_title, url=top_post_url, upvotes=top_post_upvotes, 
                               subreddit=top_post_subreddit, author=top_post_author, icon=subreddit_icon_url, 
                               comments=num_comments, posttime=post_time, top_comments=top_comments, 
                               commenttime=comment_time)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
