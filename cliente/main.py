# Configurador CLI
# Descripción: Configurador de la interfaz de línea de comandos para el cliente
import argparse
import contextlib
import grpc
import logging
import grpc

import _credentials
import auth_pb2_grpc
import auth_pb2

# My serverd
LOGGER = logging.getLogger(__name__)

dir_local = "http://0.0.0.0:3041/"
deamon = grpc.insecure_channel(dir_local)

def run():
    print("Will try to greet world ...")
    with grpc.insecure_channel("localhost:3041") as channel:
        stub = auth_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(auth_pb2.HelloRequest(name="you"))
    print("Greeter client received: " + response.message)

if __name__ == "__main__":
    run()