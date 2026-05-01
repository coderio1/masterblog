import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

POSTS_FILE = 'data/posts.json'


# ---------- Helpers for JSON storage ----------

def load_posts():
    """Read all blog posts from the JSON file and return them as a list."""
    with open(POSTS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_posts(posts):
    """Write the given list of posts back to the JSON file."""
    with open(POSTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(posts, f, indent=4, ensure_ascii=False)


def fetch_post_by_id(post_id):
    """Return the post dict with the given id, or None if not found."""
    posts = load_posts()
    for post in posts:
        if post['id'] == post_id:
            return post
    return None


# ---------- Routes ----------

@app.route('/')
def index():
    blog_posts = load_posts()
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        posts = load_posts()

        # Generate a new unique id (max existing id + 1, or 1 if list is empty)
        new_id = max((post['id'] for post in posts), default=0) + 1

        new_post = {
            'id': new_id,
            'author': request.form.get('author'),
            'title': request.form.get('title'),
            'content': request.form.get('content')
        }
        posts.append(new_post)
        save_posts(posts)

        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/delete/<int:post_id>')
def delete(post_id):
    posts = load_posts()
    # Keep every post except the one with the matching id
    posts = [post for post in posts if post['id'] != post_id]
    save_posts(posts)
    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    post = fetch_post_by_id(post_id)
    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        posts = load_posts()
        for p in posts:
            if p['id'] == post_id:
                p['author'] = request.form.get('author')
                p['title'] = request.form.get('title')
                p['content'] = request.form.get('content')
                break
        save_posts(posts)
        return redirect(url_for('index'))

    # GET request: show the form pre-filled with current values
    return render_template('update.html', post=post)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
