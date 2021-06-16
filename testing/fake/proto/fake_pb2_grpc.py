# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from testing.fake.proto import fake_pb2 as testing_dot_fake_dot_proto_dot_fake__pb2


class AgentManagerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Add = channel.unary_unary(
                '/gnmi.fake.AgentManager/Add',
                request_serializer=testing_dot_fake_dot_proto_dot_fake__pb2.Config.SerializeToString,
                response_deserializer=testing_dot_fake_dot_proto_dot_fake__pb2.Config.FromString,
                )
        self.Remove = channel.unary_unary(
                '/gnmi.fake.AgentManager/Remove',
                request_serializer=testing_dot_fake_dot_proto_dot_fake__pb2.Config.SerializeToString,
                response_deserializer=testing_dot_fake_dot_proto_dot_fake__pb2.Config.FromString,
                )
        self.Status = channel.unary_unary(
                '/gnmi.fake.AgentManager/Status',
                request_serializer=testing_dot_fake_dot_proto_dot_fake__pb2.Config.SerializeToString,
                response_deserializer=testing_dot_fake_dot_proto_dot_fake__pb2.Config.FromString,
                )


class AgentManagerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Add(self, request, context):
        """Add adds an agent to the server.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Remove(self, request, context):
        """Remove removes an agent from the server.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Status(self, request, context):
        """Status returns the current status of an agent on the server.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AgentManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Add': grpc.unary_unary_rpc_method_handler(
                    servicer.Add,
                    request_deserializer=testing_dot_fake_dot_proto_dot_fake__pb2.Config.FromString,
                    response_serializer=testing_dot_fake_dot_proto_dot_fake__pb2.Config.SerializeToString,
            ),
            'Remove': grpc.unary_unary_rpc_method_handler(
                    servicer.Remove,
                    request_deserializer=testing_dot_fake_dot_proto_dot_fake__pb2.Config.FromString,
                    response_serializer=testing_dot_fake_dot_proto_dot_fake__pb2.Config.SerializeToString,
            ),
            'Status': grpc.unary_unary_rpc_method_handler(
                    servicer.Status,
                    request_deserializer=testing_dot_fake_dot_proto_dot_fake__pb2.Config.FromString,
                    response_serializer=testing_dot_fake_dot_proto_dot_fake__pb2.Config.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gnmi.fake.AgentManager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AgentManager(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Add(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gnmi.fake.AgentManager/Add',
            testing_dot_fake_dot_proto_dot_fake__pb2.Config.SerializeToString,
            testing_dot_fake_dot_proto_dot_fake__pb2.Config.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Remove(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gnmi.fake.AgentManager/Remove',
            testing_dot_fake_dot_proto_dot_fake__pb2.Config.SerializeToString,
            testing_dot_fake_dot_proto_dot_fake__pb2.Config.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Status(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gnmi.fake.AgentManager/Status',
            testing_dot_fake_dot_proto_dot_fake__pb2.Config.SerializeToString,
            testing_dot_fake_dot_proto_dot_fake__pb2.Config.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)