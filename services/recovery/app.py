import os
import random
import hashlib
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/recovery/dry_run')
def dry_run_recovery():
    rcd = request.args.get('data', default='none', type=str)
    md5 = hashlib.md5(str(random.getrandbits(256)).encode('utf-8'))

    return jsonify(
        status='recovered',
        rcd=rcd,
        recovered_hash= md5.hexdigest()
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')