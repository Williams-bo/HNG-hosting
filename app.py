from flask import Flask, request, jsonify
import datetime
import pytz

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get current day of the week
    current_day = datetime.datetime.now(pytz.utc).strftime('%A')

    # Get current UTC time with validation of +/-2 hours
    current_time_utc = datetime.datetime.now(pytz.utc)
    current_time_utc_str = current_time_utc.strftime('%Y-%m-%dT%H:%M:%SZ')

    # GitHub file URL and repo URL
    github_file_url = "https://github.com/Williams-bo/HNG-hosting/blob/main/app.py"
    github_repo_url = "https://github.com/Williams-bo/HNG-hosting"

    # Construct the response JSON
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_time_utc_str,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
