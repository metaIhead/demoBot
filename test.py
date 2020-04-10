from flask import *
import os
import interactionDB

app = Flask(__name__)

@app.route("/send_message", methods=['POST'])
def bot_handler():
    print(request.json)
    return 'NOT WORD'

@app.route("/", methods=['GET'])
def get_response():
    return render_template('table.html',load={'info_status': interactionDB.read_all_users() })

if __name__ == "__main__":
    app.run(debug=True)
