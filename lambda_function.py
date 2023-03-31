import json
import os
import requests

SLACK_URL = os.environ.get("SLACK_URL", "")

def lambda_handler(event, context):
    # Parse the event
    body_str = event.get("body", "{}")
    body_str = body_str if body_str else "{}"
    body_obj = json.loads(body_str)
    
    # Construct the payload
    payload = f"{{\'text\':\'Issue Created: {body_obj.get('issue', {}).get('url', '')}\'}}"

    # Send the payload
    r = requests.post(SLACK_URL, data=payload)

    # Return the response
    return {
        "statusCode": r.status_code,
        "body": r.text
    }
