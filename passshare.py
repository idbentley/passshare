from flask import Flask, render_template, g, request
import pymongo

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html') 

"""@app.route('/register')
def register():
    if request.method == "POST":
        jira_uname = request.cookies.get('auth_user', None)
        public_key = request.args.get('public_key', None)
        if jira_uname and public_key:
            user = g.db.find_one({_id: jira_uname})
            if not user:
                user = {'_id': jira_uname}
                g.db.insert(user)
                user = g.db.find_one({_id: jira_uname})
            g.db.update({_id: jira_uname}, {
                '$addToSet': {
                    'public_keys': public_key
                },
                '$set': {
                    'current_key': public_key
                }})
        else:
            abort(400)"""


if __name__ == '__main__':
    #g.db = pymongo.MongoClient()
    app.debug = True
    app.run()