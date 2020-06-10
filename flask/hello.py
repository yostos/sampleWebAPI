from flask import *

app = Flask(__name__)
# これがないと日本語が文字化けする。
app.config['JSON_AS_ASCII'] = False

@app.route("/api", methods=["POST"])
def api_return():
    try:
        print(request)
        userid = request.json['userid']
        print("Userid = {}".format(userid))
        user = {
                "id" : userid,
                "name" : "山田太郎",
                "gender" : "male",
                "age" : 29,
                "company" : "White Company"}
        return jsonify({"user":user})
    except:
        return """
            エラーが発生しました。
        """
@app.route("/", methods=["GET","POST"])
def hello_world():
    if request.method == "GET":
        return """
            <!DOCTYPE html>
            <html>
            <head>
              <title>Hello World!</title>
              <meta charset="utf-8">
              <meta name="viewport" content="width=device-width, initial-scale=1">
            </head>
            <body>
              <section>
                <p> Hello World! とかやってんじゃねーよ </p>
                <form action="/" method="POST">
                <label for="userid">User ID:</label>
                <input name="userid" name="userid" required minlength="10" size=10></input>
                </form>
              </section>
            </body>
            </html>
    """
    else:
        try:
            userid = str(request.form["userid"])
            user = {
                "id" : userid,
                "name" : "山田太郎",
                "gender" : "male",
                "age" : 29,
                "company" : "White Company"}
            return jsonify({"user":user})
        except:
            return """
                エラーが発生しました。
            """


