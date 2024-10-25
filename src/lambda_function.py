import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello World, I am Github Actions, Updated at 5:35 PM')
    }



# Step 1: Create a Lambda Function in your AWS Account and note down the Function ARN
# Step 2: Create a GitHub Repository and push your source code to your GitHub repository
# Step 3: Create an Action in your repository and add the following block of code in 
# to your GitHub Actions .yaml file
# Step 4:Push the code and you should be seeing the code that you pushed on your 
# AWS Lambda Console.