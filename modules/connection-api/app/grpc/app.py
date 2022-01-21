from  concurrent import futures
import time
import grpc
import connection_pb2
import connection_pb2_grpc
from connection import ConnectionServicer
_ONE_DAY_IN_SECONDS = 60 * 60 * 24

def grpc_server():
    # Initialize gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    connection_pb2_grpc.add_ConnectionServiceServicer_to_server(ConnectionServicer(), server)


    print("Server starting on port 5005...")
    server.add_insecure_port("[::]:5005")
    server.start()
    # Keep thread alive
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
if __name__ == '__main__':
    grpc_server()