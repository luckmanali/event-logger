# Event Logger: A Simple Scalable and Secure Event Logging API

Event Logger is a logging API built with FastAPI and deployed on AWS Lambda using the AWS API Gateway. 
The purpose of this API is to receive events from a client application and store them in an AWS S3 bucket.

## Table of Contents

- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Testing](#testing)
- [Deployment](#deployment)

## Project Overview

The Event Logger project consists of the following main files:

- `main.py`: The FastAPI application with the `/events` endpoint that logs events to an S3 bucket.
- `jwt_utils.py`: Utility functions for creating and decoding JWT tokens.
- `dependencies.py`: FastAPI dependency to authenticate the client app using a JWT token.
- `template.yaml`: AWS SAM template for deploying the FastAPI app to AWS Lambda and API Gateway.
- `requirements.txt`: Lists the required packages for the project.

## Requirements

- Python 3.8+
- boto3
- fastapi
- mangum
- python-dotenv
- uvicorn
- httpx
- pytest
- PyJWT

## Installation

1. Clone the repository:
    
```bash
git clone https://github.com/luckmanali/event-logger.git
```


2. Navigate to the project directory and create a virtual environment:
        
```bash
cd event-logger
python -m venv venv
```

3. Activate the virtual environment:
- For Windows:
  ```
  venv\Scripts\activate
  ```
- For macOS and Linux:
  ```
  source venv/bin/activate
  ```

4. Install the required dependencies:
    
```bash
pip install -r requirements.txt
```


## Configuration

1. Create a `.env` file in the project directory and add the following environment variables:

```env
AWS_ACCESS_KEY_ID=<your_aws_access_key_id>
AWS_SECRET_ACCESS_KEY=<your_aws_secret_access_key>
AWS_S3_BUCKET=<your_aws_s3_bucket_name>
APP_SECRET=<your_app_secret>
```


2. Replace `<your_aws_access_key_id>`, `<your_aws_secret_access_key>`, `<your_aws_s3_bucket_name>`, and `<your_app_secret>` with your actual AWS credentials and chosen secret for your application.


## Usage

1. To run the API locally, use the following command:

```bash
uvicorn main:app --reload
```


2. By default, the API will be available at `http://127.0.0.1:8000`.

3. To log an event, send a POST request to the `/events` endpoint with the following payload:

```json
{
  "event_type": "example_event",
  "event_data": {
    "key1": "value1",
    "key2": "value2"
  }
}
```

Make sure to include the Authorization header with the Bearer token as well.

## Testing

To run the tests, use the following command:

```bash
pytests
```

## Deployment

To deploy your Event Logger project to AWS Lambda and API Gateway using AWS SAM (Serverless Application Model), follow these detailed instructions:

### Prerequisites:

1. Install the [AWS CLI](https://aws.amazon.com/cli/).
2. Install the [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html).
3. Make sure you have configured your AWS credentials by running `aws configure`.

### Deployment Steps:

1. Open a terminal and navigate to your project's root directory.

2. Run the following command to build the AWS SAM application:
    
```bash
sam build
```


This command packages your application and uses your existing `template.yaml` file. It also creates a `.aws-sam` folder with the build artifacts.

3. Deploy the application using the AWS SAM CLI:

```bash
sam deploy --guided
```


This command will prompt you to enter the following information:

- **Stack Name:** Enter a name for the AWS CloudFormation stack that will be created for your application. For example, `event-logger-stack`.
- **AWS Region:** Choose the AWS region where you want to deploy your application. For example, `us-east-1`.
- **Confirm changes before deploy:** Type `Y` to review and confirm changes before deployment.
- **Allow SAM CLI IAM role creation:** Type `Y` to allow AWS SAM CLI to create the necessary IAM roles.
- **Save arguments to samconfig.toml:** Type `Y` to save your settings in a `samconfig.toml` file, which will be used for future deployments.

4. The deployment process will start, and you can monitor its progress in the terminal. Once the deployment is complete, you'll see an output similar to this:

```output
CloudFormation outputs from deployed stack
----------------------------------------------------------------------------------------------
Outputs                                                                                       
----------------------------------------------------------------------------------------------
Key                 APIGatewayURL                                                             
Description         The URL for the API Gateway                                              
Value               https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/Prod/             
----------------------------------------------------------------------------------------------
```


5. Copy the `APIGatewayURL` value (e.g., `https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/Prod/`). This is the base URL of your deployed API.

6. Update your client application to send requests to the deployed API Gateway URL.

Your Event Logger project is now deployed to AWS Lambda and API Gateway.


## License

This project is licensed under the terms of the MIT license. 

You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the project, subject to the following conditions:

- You must include a copy of the license in all copies or substantial portions of the project.
- You must give credit to the original author(s) of the project.

For more information, please refer to the [LICENSE](LICENSE) file.
