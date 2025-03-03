from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/configArchive/import', methods=['POST'])
def import_config():
    return jsonify({"status": "success", "message": "Config imported successfully"})

@app.route('/configArchive/export', methods=['GET'])
def export_config():
    return jsonify({"status": "success", "message": "Config exported successfully"})

@app.route('/time/current', methods=['GET'])
def get_current_time():
    return jsonify({"status": "success", "time": "2025-02-20T12:00:00Z"})

@app.route('/data/user', methods=['GET'])
def get_user():
    return jsonify({"status": "success", "user": {"id": 1, "name": "John Doe", "email": "john.doe@example.com"}})

@app.route('/data/posts', methods=['GET'])
def get_posts():
    return jsonify({"status": "success", "posts": [{"id": 1, "title": "First Post", "content": "This is a sample post."}]})

@app.route('/data/comments', methods=['GET'])
def get_comments():
    return jsonify({"status": "success", "comments": [{"id": 1, "post_id": 1, "content": "Great post!"}]})

@app.route('/data/likes', methods=['GET'])
def get_likes():
    print("get like is callinggg")
    return jsonify({"status": "success", "likes": [{"id": 1, "post_id": 1, "user_id": 1}]})

@app.route('/data/notifications', methods=['GET'])
def get_notifications():
    return jsonify({"status": "success", "notifications": [{"id": 1, "message": "You have a new comment!"}]})

if __name__ == '__main__':
    app.run(debug=True,port=8000)
