import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
    """
    Modulo operation Lambda function
    Calculates remainder of division with enhanced logging and validation
    """
    
    try:
        # Parse request body
        if 'body' in event:
            body = json.loads(event['body']) if isinstance(event['body'], str) else event['body']
        else:
            body = event
            
        # Extract operands
        dividend = body.get('dividend')
        divisor = body.get('divisor')
        
        # Validate inputs
        if dividend is None or divisor is None:
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'error': 'Missing required parameters: dividend and divisor'
                })
            }
        
        # Convert to numbers
        try:
            dividend = float(dividend)
            divisor = float(divisor)
        except (ValueError, TypeError):
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'error': 'Invalid number format'
                })
            }
        
        # Check for division by zero
        if divisor == 0:
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'error': 'Division by zero is not allowed'
                })
            }
        
        # Perform modulo operation
        result = dividend % divisor
        
        # Log operation for audit trail
        operation_log = {
            'operation': 'modulo',
            'dividend': dividend,
            'divisor': divisor,
            'result': result,
            'timestamp': datetime.utcnow().isoformat(),
            'request_id': context.aws_request_id if context else 'local'
        }
        
        # Store operation in CloudWatch Logs
        print(f"OPERATION_LOG: {json.dumps(operation_log)}")
        
        # Enhanced response with metadata
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'result': result,
                'operation': 'modulo',
                'dividend': dividend,
                'divisor': divisor,
                'timestamp': operation_log['timestamp'],
                'request_id': operation_log['request_id']
            })
        }
        
    except Exception as e:
        error_log = {
            'error': str(e),
            'operation': 'modulo',
            'timestamp': datetime.utcnow().isoformat(),
            'request_id': context.aws_request_id if context else 'local'
        }
        print(f"ERROR_LOG: {json.dumps(error_log)}")
        
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': 'Internal server error during modulo operation'
            })
        }
