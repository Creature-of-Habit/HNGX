from flask import Flask, request, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

@app.route('/api')
def api():
    slack_name = request.args.get("slack_name",str)
    track = request.args.get("track",str)
    now = datetime.now(timezone.utc)

    user_data ={
        "slack_name":"charliee",
        "current_day":now.strftime('%A'),
        "utc_time":now.strftime('%Y-%m-%dT%H:%M:%SZ'),
        "track":"backend",
        "github_file_url":"https://github.com/Creature-of-Habit/HNGX/blob/main/Stage%20one%20task/api.py",
        "github_repo_url":"https://github.com/Creature-of-Habit/HNGX.git",
        "status_code": 200
    }

    if (slack_name == user_data["slack_name"]) & ( track == user_data["track"]) :
        return jsonify(user_data), 200

if __name__ == "__main__":
    app.run(debug=True)