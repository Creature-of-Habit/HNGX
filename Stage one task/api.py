from flask import Flask, jsonify, request
from datetime import datetime,timezone
app = Flask(__name__)

@app.route('/api')
def api():
    slack_name = request.args.get("slack_name",str)
    track = request.args.get("track",str)
    now = datetime.now(timezone.utc)
    utcnow = datetime.datetime.now(tz=datetime.timezone.utc)
    user_data ={
        "slack_name":"charliee",
        "current_day":now.strftime('%A'),
        "utc_time":utcnow,
        "track":"backend",
        "github_file_url":"",
        "github_repo_url":"",
        "status_code": 200
    }
    
    if (slack_name == user_data["slack_name"]) & ( track == user_data["track"]) :
        return jsonify(user_data), 200

if __name__ == "__main__":
    app.run(debug=True)