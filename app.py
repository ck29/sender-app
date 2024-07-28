from flask import Flask, send_file, Response, request
import os

app=Flask(__name__)

@app.route('/download/file', methods=['GET'])
def get_file():

    filename = request.args.get('filename')

    directory = 'files'
    file_path = os.path.join(directory, filename)

    try:
        response =  send_file(file_path, as_attachment=False)
        response.headers.set('Content-Type', 'application/octet-stream')
        return response
    except Exception as w:
        return Response(str(w), status=404)

if __name__ == 'main':
    print("Started.")
    app.run(debug=True)
    print("exited.")