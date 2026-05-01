# MasterBlog

A simple Flask blog application where you can create, read, update, delete, and like blog posts. Posts are stored in a local JSON file.

## Requirements

- Python 3.x
- Flask

## Setup

1. Clone or download the project.
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate      # macOS/Linux
   .venv\Scripts\activate         # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the App

```bash
python app.py
```

Then open your browser and go to: [http://localhost:5000](http://localhost:5000)

## Usage

### View Posts
The home page (`/`) displays all blog posts with their title, author, content, and like count.

### Add a Post
Click **Add New Post** on the home page. Fill in the author, title, and content fields, then click **Submit**.

### Update a Post
Click **Update** on any post. Edit the fields and click **Submit** to save changes.

### Delete a Post
Click **Delete** on any post and confirm the prompt. The post is permanently removed.

### Like a Post
Click the **❤ like** button on any post to increment its like count by 1.

## Project Structure

```
3_29-MasterBlog-Flask/
├── app.py              # Flask application and routes
├── requirements.txt    # Python dependencies
├── data/
│   └── posts.json      # Blog post storage
├── static/
│   └── style.css       # Stylesheet
└── templates/
    ├── index.html      # Home page
    ├── add.html        # Add post form
    └── update.html     # Update post form
```