#!/bin/bash

# Clean up previous builds
rm -rf lambda1.zip lambda2.zip shared_layer.zip

# Package shared layer
cd shared_layer
zip -r ../shared_layer.zip .
cd ..

# Package lambda1
cd lambda1
zip -r ../lambda1.zip .
cd ..

# Package lambda2
cd lambda2
zip -r ../lambda2.zip .
cd ..

# Deploy shared layer
aws lambda publish-layer-version --layer-name shared_layer --compatible-runtimes python3.11 --zip-file fileb://shared_layer.zip

# Deploy lambda1
aws lambda create-function --function-name lambda1 --runtime python3.8 --role your_lambda_role_arn --handler lambda1_function.lambda_handler --code S3Bucket=your_bucket_name,S3Key=lambda1.zip --layers your_shared_layer_arn

# Deploy lambda2
aws lambda create-function --function-name lambda2 --runtime python3.8 --role your_lambda_role_arn --handler lambda2_function.lambda_handler --code S3Bucket=your_bucket_name,S3Key=lambda2.zip --layers your_shared_layer_arn
