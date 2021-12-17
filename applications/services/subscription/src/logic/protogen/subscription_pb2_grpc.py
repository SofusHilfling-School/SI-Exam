# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import logic.protogen.subscription_pb2 as subscription__pb2


class SubscriptionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateSubscription = channel.unary_unary(
            "/Subscription/CreateSubscription",
            request_serializer=subscription__pb2.CreateSubscriptionRequest.SerializeToString,
            response_deserializer=subscription__pb2.CreateSubscriptionResponse.FromString,
        )
        self.ReadSubscription = channel.unary_unary(
            "/Subscription/ReadSubscription",
            request_serializer=subscription__pb2.ReadSubscriptionRequest.SerializeToString,
            response_deserializer=subscription__pb2.ReadSubscriptionResponse.FromString,
        )
        self.ReadSubscriptionList = channel.unary_unary(
            "/Subscription/ReadSubscriptionList",
            request_serializer=subscription__pb2.ReadSubscriptionListRequest.SerializeToString,
            response_deserializer=subscription__pb2.ReadSubscriptionListResponse.FromString,
        )
        self.UpdateSubscription = channel.unary_unary(
            "/Subscription/UpdateSubscription",
            request_serializer=subscription__pb2.UpdateSubscriptionRequest.SerializeToString,
            response_deserializer=subscription__pb2.UpdateSubscriptionResponse.FromString,
        )
        self.DeleteSubscription = channel.unary_unary(
            "/Subscription/DeleteSubscription",
            request_serializer=subscription__pb2.DeleteSubscriptionRequest.SerializeToString,
            response_deserializer=subscription__pb2.DeleteSubscriptionResponse.FromString,
        )


class SubscriptionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateSubscription(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ReadSubscription(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ReadSubscriptionList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateSubscription(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteSubscription(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_SubscriptionServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CreateSubscription": grpc.unary_unary_rpc_method_handler(
            servicer.CreateSubscription,
            request_deserializer=subscription__pb2.CreateSubscriptionRequest.FromString,
            response_serializer=subscription__pb2.CreateSubscriptionResponse.SerializeToString,
        ),
        "ReadSubscription": grpc.unary_unary_rpc_method_handler(
            servicer.ReadSubscription,
            request_deserializer=subscription__pb2.ReadSubscriptionRequest.FromString,
            response_serializer=subscription__pb2.ReadSubscriptionResponse.SerializeToString,
        ),
        "ReadSubscriptionList": grpc.unary_unary_rpc_method_handler(
            servicer.ReadSubscriptionList,
            request_deserializer=subscription__pb2.ReadSubscriptionListRequest.FromString,
            response_serializer=subscription__pb2.ReadSubscriptionListResponse.SerializeToString,
        ),
        "UpdateSubscription": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateSubscription,
            request_deserializer=subscription__pb2.UpdateSubscriptionRequest.FromString,
            response_serializer=subscription__pb2.UpdateSubscriptionResponse.SerializeToString,
        ),
        "DeleteSubscription": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteSubscription,
            request_deserializer=subscription__pb2.DeleteSubscriptionRequest.FromString,
            response_serializer=subscription__pb2.DeleteSubscriptionResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "Subscription", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Subscription(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateSubscription(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Subscription/CreateSubscription",
            subscription__pb2.CreateSubscriptionRequest.SerializeToString,
            subscription__pb2.CreateSubscriptionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ReadSubscription(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Subscription/ReadSubscription",
            subscription__pb2.ReadSubscriptionRequest.SerializeToString,
            subscription__pb2.ReadSubscriptionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ReadSubscriptionList(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Subscription/ReadSubscriptionList",
            subscription__pb2.ReadSubscriptionListRequest.SerializeToString,
            subscription__pb2.ReadSubscriptionListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def UpdateSubscription(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Subscription/UpdateSubscription",
            subscription__pb2.UpdateSubscriptionRequest.SerializeToString,
            subscription__pb2.UpdateSubscriptionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def DeleteSubscription(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Subscription/DeleteSubscription",
            subscription__pb2.DeleteSubscriptionRequest.SerializeToString,
            subscription__pb2.DeleteSubscriptionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
