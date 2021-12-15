# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: subscription.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="subscription.proto",
    package="",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x12subscription.proto"G\n\x19\x43reateSubscriptionRequest\x12\x11\n\tis_active\x18\x01 \x01(\x08\x12\x17\n\x0f\x65xpiration_date\x18\x02 \x01(\t"%\n\x17ReadSubscriptionRequest\x12\n\n\x02id\x18\x01 \x01(\x05")\n\x1a\x43reateSubscriptionResponse\x12\x0b\n\x03msg\x18\x01 \x01(\t"R\n\x18ReadSubscriptionResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\tis_active\x18\x02 \x01(\x08\x12\x17\n\x0f\x65xpiration_date\x18\x03 \x01(\t2\xaa\x01\n\x0cSubscription\x12O\n\x12\x43reateSubscription\x12\x1a.CreateSubscriptionRequest\x1a\x1b.CreateSubscriptionResponse"\x00\x12I\n\x10ReadSubscription\x12\x18.ReadSubscriptionRequest\x1a\x19.ReadSubscriptionResponse"\x00\x62\x06proto3',
)


_CREATESUBSCRIPTIONREQUEST = _descriptor.Descriptor(
    name="CreateSubscriptionRequest",
    full_name="CreateSubscriptionRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="is_active",
            full_name="CreateSubscriptionRequest.is_active",
            index=0,
            number=1,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="expiration_date",
            full_name="CreateSubscriptionRequest.expiration_date",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=22,
    serialized_end=93,
)


_READSUBSCRIPTIONREQUEST = _descriptor.Descriptor(
    name="ReadSubscriptionRequest",
    full_name="ReadSubscriptionRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="ReadSubscriptionRequest.id",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=95,
    serialized_end=132,
)


_CREATESUBSCRIPTIONRESPONSE = _descriptor.Descriptor(
    name="CreateSubscriptionResponse",
    full_name="CreateSubscriptionResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg",
            full_name="CreateSubscriptionResponse.msg",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=134,
    serialized_end=175,
)


_READSUBSCRIPTIONRESPONSE = _descriptor.Descriptor(
    name="ReadSubscriptionResponse",
    full_name="ReadSubscriptionResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="ReadSubscriptionResponse.id",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="is_active",
            full_name="ReadSubscriptionResponse.is_active",
            index=1,
            number=2,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="expiration_date",
            full_name="ReadSubscriptionResponse.expiration_date",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=177,
    serialized_end=259,
)

DESCRIPTOR.message_types_by_name[
    "CreateSubscriptionRequest"
] = _CREATESUBSCRIPTIONREQUEST
DESCRIPTOR.message_types_by_name["ReadSubscriptionRequest"] = _READSUBSCRIPTIONREQUEST
DESCRIPTOR.message_types_by_name[
    "CreateSubscriptionResponse"
] = _CREATESUBSCRIPTIONRESPONSE
DESCRIPTOR.message_types_by_name["ReadSubscriptionResponse"] = _READSUBSCRIPTIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateSubscriptionRequest = _reflection.GeneratedProtocolMessageType(
    "CreateSubscriptionRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATESUBSCRIPTIONREQUEST,
        "__module__": "subscription_pb2"
        # @@protoc_insertion_point(class_scope:CreateSubscriptionRequest)
    },
)
_sym_db.RegisterMessage(CreateSubscriptionRequest)

ReadSubscriptionRequest = _reflection.GeneratedProtocolMessageType(
    "ReadSubscriptionRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _READSUBSCRIPTIONREQUEST,
        "__module__": "subscription_pb2"
        # @@protoc_insertion_point(class_scope:ReadSubscriptionRequest)
    },
)
_sym_db.RegisterMessage(ReadSubscriptionRequest)

CreateSubscriptionResponse = _reflection.GeneratedProtocolMessageType(
    "CreateSubscriptionResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATESUBSCRIPTIONRESPONSE,
        "__module__": "subscription_pb2"
        # @@protoc_insertion_point(class_scope:CreateSubscriptionResponse)
    },
)
_sym_db.RegisterMessage(CreateSubscriptionResponse)

ReadSubscriptionResponse = _reflection.GeneratedProtocolMessageType(
    "ReadSubscriptionResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _READSUBSCRIPTIONRESPONSE,
        "__module__": "subscription_pb2"
        # @@protoc_insertion_point(class_scope:ReadSubscriptionResponse)
    },
)
_sym_db.RegisterMessage(ReadSubscriptionResponse)


_SUBSCRIPTION = _descriptor.ServiceDescriptor(
    name="Subscription",
    full_name="Subscription",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=262,
    serialized_end=432,
    methods=[
        _descriptor.MethodDescriptor(
            name="CreateSubscription",
            full_name="Subscription.CreateSubscription",
            index=0,
            containing_service=None,
            input_type=_CREATESUBSCRIPTIONREQUEST,
            output_type=_CREATESUBSCRIPTIONRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="ReadSubscription",
            full_name="Subscription.ReadSubscription",
            index=1,
            containing_service=None,
            input_type=_READSUBSCRIPTIONREQUEST,
            output_type=_READSUBSCRIPTIONRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_SUBSCRIPTION)

DESCRIPTOR.services_by_name["Subscription"] = _SUBSCRIPTION

# @@protoc_insertion_point(module_scope)
