from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def send_data():
    # Respond to Twine with some XML data
    xml_response = '''<?xml version="1.0" encoding="UTF-8"?>
    <response>
        <message>Hello, Twine!</message>
        <currency>100</currency>
    </response>'''
    response = make_response(xml_response)
    response.headers['Content-Type'] = 'application/xml'
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000)
