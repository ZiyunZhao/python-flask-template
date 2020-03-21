from nmt.nmt import nmt
import os


def translate():
    command = "cd nmt && python -m nmt.nmt \
    --out_dir=./nmt/tmp/nmt_model \
    --inference_input_file=./nmt/tmp/my_infer_file.vi \
    --inference_output_file=./nmt/tmp/nmt_model/output_infer && cd .."
    f = open("./nmt/nmt/tmp/my_infer_file.vi", "w")
    f.write("2")
    f.close()
    os.system(command)
    f = open("./nmt/nmt/tmp/nmt_model/output_infer", "r")
    content = f.read()
    f.close()
    return content


def handle(event, context):
    content = translate()
    return {
        "statusCode": 200,
        "body": content
    }

