import json
import os
import requests

SLACK_URL = os.environ.get("SLACK_URL", "")

def lambda_handler(event, context):
    if event['action'] == 'opened':
        # Construct the payload
        payload = f"{{\'text\':\'Issue Created: {event['issue']['html_url']}\'}}"

        # Send the payload
        r = requests.post(SLACK_URL, data=payload)

        # Return the response
        return {
            "statusCode": r.status_code,
            "body": r.text
        }
