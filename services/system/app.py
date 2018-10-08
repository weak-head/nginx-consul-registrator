import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/system/status')
def system_status():

    # nginx gateway IP
    gw_ip = os.environ.get('GATEWAY_IP', None)

    recovery_service_status = 'disconnected'
    recovery_result = None

    try:
        # call recovery service with some arbitrary data
        req_url = 'http://{gw_ip}/recovery/dry_run?data={data}'
        response = requests.get(req_url.format(gw_ip=gw_ip, data='some_data'))

        if response.status_code == 200:
            recovery_result = response.json()
            recovery_service_status = 'connected'
    except:
        None

    return jsonify(
        gateway_ip = gw_ip,
        recovered_data = recovery_result,
        services = {
            'recovery': recovery_service_status
        }
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')