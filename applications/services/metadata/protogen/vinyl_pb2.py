# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/vinyl.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/vinyl.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12protos/vinyl.proto\"\x1a\n\x0cVinylRequest\x12\n\n\x02id\x18\x01 \x01(\t\":\n\rVinylResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06\x61rtist\x18\x02 \x01(\t\x12\r\n\x05genre\x18\x03 \x01(\t26\n\x05Vinyl\x12-\n\x0cgetVinylInfo\x12\r.VinylRequest\x1a\x0e.VinylResponseb\x06proto3'
)




_VINYLREQUEST = _descriptor.Descriptor(
  name='VinylRequest',
  full_name='VinylRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='VinylRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=48,
)


_VINYLRESPONSE = _descriptor.Descriptor(
  name='VinylResponse',
  full_name='VinylResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='VinylResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='artist', full_name='VinylResponse.artist', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='genre', full_name='VinylResponse.genre', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=108,
)

DESCRIPTOR.message_types_by_name['VinylRequest'] = _VINYLREQUEST
DESCRIPTOR.message_types_by_name['VinylResponse'] = _VINYLRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VinylRequest = _reflection.GeneratedProtocolMessageType('VinylRequest', (_message.Message,), {
  'DESCRIPTOR' : _VINYLREQUEST,
  '__module__' : 'protos.vinyl_pb2'
  # @@protoc_insertion_point(class_scope:VinylRequest)
  })
_sym_db.RegisterMessage(VinylRequest)

VinylResponse = _reflection.GeneratedProtocolMessageType('VinylResponse', (_message.Message,), {
  'DESCRIPTOR' : _VINYLRESPONSE,
  '__module__' : 'protos.vinyl_pb2'
  # @@protoc_insertion_point(class_scope:VinylResponse)
  })
_sym_db.RegisterMessage(VinylResponse)



_VINYL = _descriptor.ServiceDescriptor(
  name='Vinyl',
  full_name='Vinyl',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=110,
  serialized_end=164,
  methods=[
  _descriptor.MethodDescriptor(
    name='getVinylInfo',
    full_name='Vinyl.getVinylInfo',
    index=0,
    containing_service=None,
    input_type=_VINYLREQUEST,
    output_type=_VINYLRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_VINYL)

DESCRIPTOR.services_by_name['Vinyl'] = _VINYL

# @@protoc_insertion_point(module_scope)