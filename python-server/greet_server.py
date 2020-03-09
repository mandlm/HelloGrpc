#!/usr/bin/env python3

import grpc

import hello_pb2
import hello_pb2_grpc

from concurrent import futures

import time

class GreetServer(hello_pb2_grpc.HelloServiceServicer):
    def greet(self, request, context):
        print(f"received \"{request.message}\"")
        return hello_pb2.GreetReply(message="Hello back")
    

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_HelloServiceServicer_to_server(GreetServer(), server)
    server.add_insecure_port("[::]:50505")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    print("serving...")
    serve()
