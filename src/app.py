from flask import Flask
import pcstats
import json

app = Flask(__name__)

@app.route('/stats')
def stats():
    return json.dumps(pcstats.getStats())
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")