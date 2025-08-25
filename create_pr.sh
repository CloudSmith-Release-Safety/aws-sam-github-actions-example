#!/bin/bash

# Script to create pull request for Lambda concurrency improvements

echo "Creating pull request for Lambda concurrency improvements..."

# Navigate to repository directory
cd "$(dirname "$0")"

# Create a new branch for the changes
git checkout -b feature/lambda-concurrency-improvements

# Add all changes
git add .

# Commit changes
git commit -m "Modify Lambda functions to handle increased concurrent executions

- Updated SAM template with concurrency settings (100 concurrent executions)
- Upgraded runtime from Python 3.8 to 3.9 for better performance
- Added memory allocation (256MB) and timeout (30s) configurations
- Optimized Lambda function code for high concurrency:
  - Added error handling and input validation
  - Moved environment variables to global scope for reuse
  - Reduced logging overhead for better performance
- Added comprehensive documentation for concurrency improvements"

# Push the branch
git push origin feature/lambda-concurrency-improvements

echo "Branch created and pushed. You can now create a pull request on GitHub."
echo "Branch name: feature/lambda-concurrency-improvements"
echo ""
echo "Pull Request Title: Modify Lambda functions to handle increased concurrent executions"
echo ""
echo "Pull Request Description:"
echo "This PR implements improvements to handle increased concurrent Lambda executions:"
echo "- Reserved concurrency limit of 100 per function"
echo "- Runtime upgrade to Python 3.9"
echo "- Memory and timeout optimizations"
echo "- Enhanced error handling and performance optimizations"
echo "- Comprehensive documentation of changes"
