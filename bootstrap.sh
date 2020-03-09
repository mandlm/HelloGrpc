python3 -m grpc_tools.protoc -I protos --python_out=python-server --grpc_python_out=python-server protos/hello.proto
python3 -m grpc_tools.protoc -I protos --python_out=python-client --grpc_python_out=python-client protos/hello.proto

