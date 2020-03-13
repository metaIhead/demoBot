from flask import Flask ,request
app = Flask(__name__)

@app.route("/1128488996:AAHIwMHnJoq85VhgUMncZ9295HNmhTNPNH0", methods=['GET','POST'])
def hello():
    print(request.get_json)
    return "Hello World!"


# if __name__ == "__main__":
#     app.run(debug=True)




# https://api.telegram.org/bot1128488996:AAHIwMHnJoq85VhgUMncZ9295HNmhTNPNH0/setWebhook?url=https://bot-key.herokuapp.com/1128488996:AAHIwMHnJoq85VhgUMncZ9295HNmhTNPNH0


# https://api.telegram.org/bot1128488996:AAHIwMHnJoq85VhgUMncZ9295HNmhTNPNH0/deleteWebhook
