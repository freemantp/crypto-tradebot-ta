#!/bin/sh
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./common.proto

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./isalive.proto

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./privateService.proto

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./publicService.proto