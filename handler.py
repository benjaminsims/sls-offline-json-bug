import json


def big_json(event, context):
    with open('random.json') as json_file:
        records = json.load(json_file)
    # Uncommenting this line will prevent the error occurring
    # records = records[0:10]
    body = json.dumps(records)
    return {"statusCode": 200, "body": body}
