# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: customer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="customer.proto",
    package="",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x0e\x63ustomer.proto"c\n\x15\x43reateCustomerRequest\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x11\n\tlast_name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x14\n\x0cphone_number\x18\x04 \x01(\t"!\n\x13ReadCustomerRequest\x12\n\n\x02id\x18\x01 \x01(\x05"o\n\x15UpdateCustomerRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12\x14\n\x0cphone_number\x18\x05 \x01(\t"\x19\n\x17ReadCustomerListRequest"%\n\x16\x43reateCustomerResponse\x12\x0b\n\x03msg\x18\x01 \x01(\t"n\n\x14ReadCustomerResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12\x14\n\x0cphone_number\x18\x05 \x01(\t"%\n\x16UpdateCustomerResponse\x12\x0b\n\x03msg\x18\x01 \x01(\t"\xc5\x01\n\x18ReadCustomerListResponse\x12?\n\rcustomer_list\x18\x01 \x03(\x0b\x32(.ReadCustomerListResponse.CustomerObject\x1ah\n\x0e\x43ustomerObject\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12\x14\n\x0cphone_number\x18\x05 \x01(\t2\x9e\x02\n\x08\x43ustomer\x12\x43\n\x0e\x43reateCustomer\x12\x16.CreateCustomerRequest\x1a\x17.CreateCustomerResponse"\x00\x12=\n\x0cReadCustomer\x12\x14.ReadCustomerRequest\x1a\x15.ReadCustomerResponse"\x00\x12I\n\x10ReadCustomerList\x12\x18.ReadCustomerListRequest\x1a\x19.ReadCustomerListResponse"\x00\x12\x43\n\x0eUpdateCustomer\x12\x16.UpdateCustomerRequest\x1a\x17.UpdateCustomerResponse"\x00\x62\x06proto3',
)


_CREATECUSTOMERREQUEST = _descriptor.Descriptor(
    name="CreateCustomerRequest",
    full_name="CreateCustomerRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="first_name",
            full_name="CreateCustomerRequest.first_name",
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
        _descriptor.FieldDescriptor(
            name="last_name",
            full_name="CreateCustomerRequest.last_name",
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
        _descriptor.FieldDescriptor(
            name="email",
            full_name="CreateCustomerRequest.email",
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
        _descriptor.FieldDescriptor(
            name="phone_number",
            full_name="CreateCustomerRequest.phone_number",
            index=3,
            number=4,
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
    serialized_start=18,
    serialized_end=117,
)


_READCUSTOMERREQUEST = _descriptor.Descriptor(
    name="ReadCustomerRequest",
    full_name="ReadCustomerRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="ReadCustomerRequest.id",
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
    serialized_start=119,
    serialized_end=152,
)


_UPDATECUSTOMERREQUEST = _descriptor.Descriptor(
    name="UpdateCustomerRequest",
    full_name="UpdateCustomerRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="UpdateCustomerRequest.id",
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
            name="first_name",
            full_name="UpdateCustomerRequest.first_name",
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
        _descriptor.FieldDescriptor(
            name="last_name",
            full_name="UpdateCustomerRequest.last_name",
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
        _descriptor.FieldDescriptor(
            name="email",
            full_name="UpdateCustomerRequest.email",
            index=3,
            number=4,
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
        _descriptor.FieldDescriptor(
            name="phone_number",
            full_name="UpdateCustomerRequest.phone_number",
            index=4,
            number=5,
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
    serialized_start=154,
    serialized_end=265,
)


_READCUSTOMERLISTREQUEST = _descriptor.Descriptor(
    name="ReadCustomerListRequest",
    full_name="ReadCustomerListRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=267,
    serialized_end=292,
)


_CREATECUSTOMERRESPONSE = _descriptor.Descriptor(
    name="CreateCustomerResponse",
    full_name="CreateCustomerResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg",
            full_name="CreateCustomerResponse.msg",
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
    serialized_start=294,
    serialized_end=331,
)


_READCUSTOMERRESPONSE = _descriptor.Descriptor(
    name="ReadCustomerResponse",
    full_name="ReadCustomerResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="ReadCustomerResponse.id",
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
            name="first_name",
            full_name="ReadCustomerResponse.first_name",
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
        _descriptor.FieldDescriptor(
            name="last_name",
            full_name="ReadCustomerResponse.last_name",
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
        _descriptor.FieldDescriptor(
            name="email",
            full_name="ReadCustomerResponse.email",
            index=3,
            number=4,
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
        _descriptor.FieldDescriptor(
            name="phone_number",
            full_name="ReadCustomerResponse.phone_number",
            index=4,
            number=5,
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
    serialized_start=333,
    serialized_end=443,
)


_UPDATECUSTOMERRESPONSE = _descriptor.Descriptor(
    name="UpdateCustomerResponse",
    full_name="UpdateCustomerResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg",
            full_name="UpdateCustomerResponse.msg",
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
    serialized_start=445,
    serialized_end=482,
)


_READCUSTOMERLISTRESPONSE_CUSTOMEROBJECT = _descriptor.Descriptor(
    name="CustomerObject",
    full_name="ReadCustomerListResponse.CustomerObject",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="ReadCustomerListResponse.CustomerObject.id",
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
            name="first_name",
            full_name="ReadCustomerListResponse.CustomerObject.first_name",
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
        _descriptor.FieldDescriptor(
            name="last_name",
            full_name="ReadCustomerListResponse.CustomerObject.last_name",
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
        _descriptor.FieldDescriptor(
            name="email",
            full_name="ReadCustomerListResponse.CustomerObject.email",
            index=3,
            number=4,
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
        _descriptor.FieldDescriptor(
            name="phone_number",
            full_name="ReadCustomerListResponse.CustomerObject.phone_number",
            index=4,
            number=5,
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
    serialized_start=578,
    serialized_end=682,
)

_READCUSTOMERLISTRESPONSE = _descriptor.Descriptor(
    name="ReadCustomerListResponse",
    full_name="ReadCustomerListResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="customer_list",
            full_name="ReadCustomerListResponse.customer_list",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
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
    nested_types=[
        _READCUSTOMERLISTRESPONSE_CUSTOMEROBJECT,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=485,
    serialized_end=682,
)

_READCUSTOMERLISTRESPONSE_CUSTOMEROBJECT.containing_type = _READCUSTOMERLISTRESPONSE
_READCUSTOMERLISTRESPONSE.fields_by_name[
    "customer_list"
].message_type = _READCUSTOMERLISTRESPONSE_CUSTOMEROBJECT
DESCRIPTOR.message_types_by_name["CreateCustomerRequest"] = _CREATECUSTOMERREQUEST
DESCRIPTOR.message_types_by_name["ReadCustomerRequest"] = _READCUSTOMERREQUEST
DESCRIPTOR.message_types_by_name["UpdateCustomerRequest"] = _UPDATECUSTOMERREQUEST
DESCRIPTOR.message_types_by_name["ReadCustomerListRequest"] = _READCUSTOMERLISTREQUEST
DESCRIPTOR.message_types_by_name["CreateCustomerResponse"] = _CREATECUSTOMERRESPONSE
DESCRIPTOR.message_types_by_name["ReadCustomerResponse"] = _READCUSTOMERRESPONSE
DESCRIPTOR.message_types_by_name["UpdateCustomerResponse"] = _UPDATECUSTOMERRESPONSE
DESCRIPTOR.message_types_by_name["ReadCustomerListResponse"] = _READCUSTOMERLISTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateCustomerRequest = _reflection.GeneratedProtocolMessageType(
    "CreateCustomerRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATECUSTOMERREQUEST,
        "__module__": "customer_pb2"
        # @@protoc_insertion_point(class_scope:CreateCustomerRequest)
    },
)
_sym_db.RegisterMessage(CreateCustomerRequest)

ReadCustomerRequest = _reflection.GeneratedProtocolMessageType(
    "ReadCustomerRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _READCUSTOMERREQUEST,
        "__module__": "customer_pb2"
        # @@protoc_insertion_point(class_scope:ReadCustomerRequest)
    },
)
_sym_db.RegisterMessage(ReadCustomerRequest)

UpdateCustomerRequest = _reflection.GeneratedProtocolMessageType(
    "UpdateCustomerRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPDATECUSTOMERREQUEST,
        "__module__": "customer_pb2"
        # @@protoc_insertion_point(class_scope:UpdateCustomerRequest)
    },
)
_sym_db.RegisterMessage(UpdateCustomerRequest)

ReadCustomerListRequest = _reflection.GeneratedProtocolMessageType(
    "ReadCustomerListRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _READCUSTOMERLISTREQUEST,
        "__module__": "customer_pb2"
        # @@protoc_insertion_point(class_scope:ReadCustomerListRequest)
    },
)
_sym_db.RegisterMessage(ReadCustomerListRequest)

CreateCustomerResponse = _reflection.GeneratedProtocolMessageType(
    "CreateCustomerResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATECUSTOMERRESPONSE,
        "__module__": "customer_pb2"
        # @@protoc_insertion_point(class_scope:CreateCustomerResponse)
    },
)
_sym_db.RegisterMessage(CreateCustomerResponse)

ReadCustomerResponse = _reflection.GeneratedProtocolMessageType(
    "ReadCustomerResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _READCUSTOMERRESPONSE,
        "__module__": "customer_pb2"
        # @@protoc_insertion_point(class_scope:ReadCustomerResponse)
    },
)
_sym_db.RegisterMessage(ReadCustomerResponse)

UpdateCustomerResponse = _reflection.GeneratedProtocolMessageType(
    "UpdateCustomerResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPDATECUSTOMERRESPONSE,
        "__module__": "customer_pb2"
        # @@protoc_insertion_point(class_scope:UpdateCustomerResponse)
    },
)
_sym_db.RegisterMessage(UpdateCustomerResponse)

ReadCustomerListResponse = _reflection.GeneratedProtocolMessageType(
    "ReadCustomerListResponse",
    (_message.Message,),
    {
        "CustomerObject": _reflection.GeneratedProtocolMessageType(
            "CustomerObject",
            (_message.Message,),
            {
                "DESCRIPTOR": _READCUSTOMERLISTRESPONSE_CUSTOMEROBJECT,
                "__module__": "customer_pb2"
                # @@protoc_insertion_point(class_scope:ReadCustomerListResponse.CustomerObject)
            },
        ),
        "DESCRIPTOR": _READCUSTOMERLISTRESPONSE,
        "__module__": "customer_pb2"
        # @@protoc_insertion_point(class_scope:ReadCustomerListResponse)
    },
)
_sym_db.RegisterMessage(ReadCustomerListResponse)
_sym_db.RegisterMessage(ReadCustomerListResponse.CustomerObject)


_CUSTOMER = _descriptor.ServiceDescriptor(
    name="Customer",
    full_name="Customer",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=685,
    serialized_end=971,
    methods=[
        _descriptor.MethodDescriptor(
            name="CreateCustomer",
            full_name="Customer.CreateCustomer",
            index=0,
            containing_service=None,
            input_type=_CREATECUSTOMERREQUEST,
            output_type=_CREATECUSTOMERRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="ReadCustomer",
            full_name="Customer.ReadCustomer",
            index=1,
            containing_service=None,
            input_type=_READCUSTOMERREQUEST,
            output_type=_READCUSTOMERRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="ReadCustomerList",
            full_name="Customer.ReadCustomerList",
            index=2,
            containing_service=None,
            input_type=_READCUSTOMERLISTREQUEST,
            output_type=_READCUSTOMERLISTRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="UpdateCustomer",
            full_name="Customer.UpdateCustomer",
            index=3,
            containing_service=None,
            input_type=_UPDATECUSTOMERREQUEST,
            output_type=_UPDATECUSTOMERRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_CUSTOMER)

DESCRIPTOR.services_by_name["Customer"] = _CUSTOMER

# @@protoc_insertion_point(module_scope)
