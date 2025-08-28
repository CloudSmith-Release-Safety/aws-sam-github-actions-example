import json
import boto3
import uuid
from datetime import datetime

def lambda_handler(event, context):
    """
    User Profile Lambda function
    Handles user profile updates with validation and storage
    """
    
    try:
        # Parse request
        http_method = event.get('httpMethod', 'POST')
        path_parameters = event.get('pathParameters') or {}
        user_id = path_parameters.get('userId')
        
        if 'body' in event:
            body = json.loads(event['body']) if isinstance(event['body'], str) else event['body']
        else:
            body = event
            
        # Handle different HTTP methods
        if http_method == 'GET':
            return get_user_profile(user_id)
        elif http_method == 'PUT':
            return update_user_profile(user_id, body)
        elif http_method == 'POST':
            return create_user_profile(body)
        else:
            return {
                'statusCode': 405,
                'body': json.dumps({'error': 'Method not allowed'})
            }
            
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal server error'})
        }

def get_user_profile(user_id):
    """Get user profile by ID"""
    if not user_id:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'User ID is required'})
        }
    
    # Simulate profile retrieval
    profile = {
        'userId': user_id,
        'name': f'User {user_id}',
        'email': f'user{user_id}@example.com',
        'lastUpdated': datetime.utcnow().isoformat()
    }
    
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(profile)
    }

def create_user_profile(body):
    """Create new user profile"""
    name = body.get('name')
    email = body.get('email')
    
    if not name or not email:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Name and email are required'})
        }
    
    user_id = str(uuid.uuid4())
    profile = {
        'userId': user_id,
        'name': name,
        'email': email,
        'createdAt': datetime.utcnow().isoformat(),
        'lastUpdated': datetime.utcnow().isoformat()
    }
    
    return {
        'statusCode': 201,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(profile)
    }

def update_user_profile(user_id, body):
    """Update existing user profile"""
    if not user_id:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'User ID is required'})
        }
    
    name = body.get('name')
    email = body.get('email')
    
    if not name and not email:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'At least one field (name or email) is required'})
        }
    
    # Simulate profile update
    profile = {
        'userId': user_id,
        'name': name or f'User {user_id}',
        'email': email or f'user{user_id}@example.com',
        'lastUpdated': datetime.utcnow().isoformat()
    }
    
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(profile)
    }
