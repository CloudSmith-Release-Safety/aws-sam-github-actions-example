import json
import os
from datetime import datetime

def lambda_handler(event, context):
    print(event)
    # Get calculation parameters from input
    first = event['input']['first']
    second = event['input']['second']
    third = event['input']['third']
    result = event['input']['result']
    
    print(f"FIRST: {first}, SECOND: {second}, THIRD: {third}")
    
    # Perform calculation
    result = int(result) + int(second)
    
    print(f"RESULT: {result}")
    
    # Enhanced response with metadata
    response = {
        "first": first,
        "second": second,
        "third": third,
        "result": int(result),
        "metadata": {
            "timestamp": datetime.now().isoformat(),
            "region": os.environ.get('AWS_REGION', 'unknown'),
            "calculation_type": "addition"
        }
    }
    
    event['input'] = response
    return event['input']

