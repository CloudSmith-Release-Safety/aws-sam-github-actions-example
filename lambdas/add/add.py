import json
import os
from datetime import datetime
import boto3
from pydantic import BaseModel, ValidationError
from typing import Optional

# Global variables for connection reuse
REGION = os.environ.get('AWS_REGION', 'unknown')

class CalculationInput(BaseModel):
    first: int
    second: int
    third: int
    result: Optional[int] = None

class CalculationResponse(BaseModel):
    first: int
    second: int
    third: int
    result: int
    metadata: dict

def lambda_handler(event, context):
    try:
        # Validate input using Pydantic
        input_data = event.get('input', {})
        calc_input = CalculationInput(**input_data)
        
        # Perform calculation
        result = (calc_input.result or 0) + calc_input.second
        
        # Enhanced response with metadata using Pydantic
        response = CalculationResponse(
            first=calc_input.first,
            second=calc_input.second,
            third=calc_input.third,
            result=result,
            metadata={
                "timestamp": datetime.now().isoformat(),
                "region": REGION,
                "calculation_type": "addition",
                "function_version": context.function_version if context else "unknown"
            }
        )
        
        event['input'] = response.dict()
        return event['input']
        
    except ValidationError as e:
        return {
            "error": f"Invalid input format: {e}",
            "statusCode": 400
        }
    except Exception as e:
        return {
            "error": str(e),
            "statusCode": 500
        }

