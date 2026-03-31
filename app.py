from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # add code here to fetch the job posts from a file
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # We will fill this in the next step
        pass
    return render_template('add.html')


@app.route('/delete/<int:post_id>')
def delete(post_id):
    # Find the blog post with the given id and remove it from the list
    # Redirect back to the home page

    @app.route('/update/<int:post_id>', methods=['GET', 'POST'])
    def update(post_id):
        # Fetch the blog posts from the JSON file
        post = fetch_post_by_id(post_id)
        if post is None:
            # Post not found
            return "Post not found", 404

        if request.method == 'POST':
        # Update the post in the JSON file
        # Redirect back to index

        # Else, it's a GET request
        # So display the update.html page
        return render_template('update.html', post=post)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
