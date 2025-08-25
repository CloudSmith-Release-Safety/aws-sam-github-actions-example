
import json
import os
from datetime import datetime

# Global variables for connection reuse
REGION = os.environ.get('AWS_REGION', 'unknown')

def lambda_handler(event, context):
    try:
        # Handle nested input structure
        input_data = event.get('input', {}).get('input', event.get('input', {}))
        first = input_data.get('first')
        second = input_data.get('second')
        third = input_data.get('third')
        
        # Perform calculation
        result = int(first) * int(second) * int(third)
        
        # Optimized response
        response = {
            "first": first,
            "second": second,
            "third": third,
            "result": result,
            "metadata": {
                "timestamp": datetime.now().isoformat(),
                "region": REGION,
                "calculation_type": "multiplication"
            }
        }
        
        event['input'] = response
        return event['input']
        
    except Exception as e:
        return {
            "error": str(e),
            "statusCode": 500
        }
