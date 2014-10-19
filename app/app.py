import os
from flask import (
    Flask,
    request,
    render_template,
    send_file,
)

from vk_friends_miner.miner import get_gml

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        uid = int(request.form['uid'].strip())
        return send_file(get_gml(uid), as_attachment=True, attachment_filename='%s.gml' % uid)
    else:
        return 'Error'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

