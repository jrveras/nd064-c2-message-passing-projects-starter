import sys
import grpc
import connection_pb2
import connection_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = connection_pb2_grpc.ConnectionServiceStub(channel)

argv = sys.argv[1:]

contact=connection_pb2.Contact(
    person_id = int(argv[0]),
    start_date = argv[1],
    end_date = argv[2],
    meters = int(argv[3])
)

response = stub.GetList(contact)
print(response)