from flask import Flask
app = Flask(__name__)
from nmt.nmt import nmt
import argparse
import subprocess
import os
import sys
from waitress import serve



#@app.route('/', defaults={'path': ''}, methods=['GET', 'PUT', 'POST', 'PATCH', 'DELETE'])
#@app.route('/<path:path>', methods=['GET', 'PUT', 'POST', 'PATCH', 'DELETE'])
@app.route('/')
def handle():
    command = "cd nmt && python -m nmt.nmt \
    --out_dir=./nmt/tmp/nmt_model \
    --inference_input_file=./nmt/tmp/my_infer_file.vi \
    --inference_output_file=./nmt/tmp/nmt_model/output_infer && cd .."
    command_list = [i for i in command.split(" ") if i]
    f = open("./nmt/nmt/tmp/my_infer_file.vi", "w")
    f.write(app.config["argument"])
    f.close()
    #command_list = [i for i in command.split(" ") if i]

    #subprocess.Popen(command_list)
    os.system(command)
    f = open("./nmt/nmt/tmp/nmt_model/output_infer", "r")
    content = f.read()
    f.close()
    print("============line26=============")
    return content



def create_app(argument):
    app.config['argument'] = argument
    return app

if __name__ == '__main__':
    argument = sys.stdin.read()
    app = create_app(argument)
    serve(app, host='0.0.0.0', port=5000)
    #app.run()
