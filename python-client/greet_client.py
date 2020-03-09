#!/usr/bin/env python3

import grpc

import hello_pb2
import hello_pb2_grpc

channel = grpc.insecure_channel("localhost:50505")
stub = hello_pb2_grpc.HelloServiceStub(channel)

reply = stub.greet(hello_pb2.GreetRequest(message="Hello service"))

print(f"service replied \"{reply.message}\"")
