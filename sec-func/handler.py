import json


def hello(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully! second function",
        "input": event,
    }
    print("sec-fun")
    return {"statusCode": 200, "body": json.dumps(body)}

