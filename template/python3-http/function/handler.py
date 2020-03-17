from nmt.nmt import nmt

def translate():
   return "tranlated"



def handle(event, context):
    return {
        "statusCode": 200,
        "body": translate()
    }
