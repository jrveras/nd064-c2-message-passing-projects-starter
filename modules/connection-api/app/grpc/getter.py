import grpc
import connection_pb2
import connection_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = connection_pb2_grpc.ConnectionServiceStub(channel)

response = stub.Get(connection_pb2.Empty())
print(response)