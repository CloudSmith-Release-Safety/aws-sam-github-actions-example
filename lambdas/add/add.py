import json
import os
from datetime import datetime

# Global variables for reuse across invocations
REGION = os.environ.get('AWS_REGION', 'unknown')

def lambda_handler(event, context):
    try:
        input_data = event.get('input', {})
        first = input_data.get('first')
        second = input_data.get('second') 
        third = input_data.get('third')
        result = input_data.get('result')
        
        result = int(result) + int(second)
        
        response = {
            "first": first,
            "second": second,
            "third": third,
            "result": result
        }
        
        event['input'] = response
        return event['input']
        
    except Exception as e:
        return {
            "error": str(e),
            "statusCode": 500
        }
