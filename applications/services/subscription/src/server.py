from utils.config import CONFIG
from concurrent import futures
from logic.protogen import customer_pb2_grpc, subscription_pb2_grpc
from routes.customer_routes import CustomerRouter
from routes.subscription_routes import SubscriptionRouter

import grpc

URL = f"{CONFIG['server']['host']}:{CONFIG['server']['port']}"
MAX_WORKERS = CONFIG["server"]["max_workers"]


def serve() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=MAX_WORKERS))
    customer_pb2_grpc.add_CustomerServicer_to_server(CustomerRouter(), server)
    subscription_pb2_grpc.add_SubscriptionServicer_to_server(
        SubscriptionRouter(), server
    )
    server.add_insecure_port(URL)
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
