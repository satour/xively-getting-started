# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: control.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))

if sys.version_info[0]<3:

  from .google_py2.protobuf import descriptor as _descriptor
  from .google_py2.protobuf import message as _message
  from .google_py2.protobuf import reflection as _reflection
  from .google_py2.protobuf import symbol_database as _symbol_database
  from .google_py2.protobuf import descriptor_pb2

else :

  from .google_py3.protobuf import descriptor as _descriptor
  from .google_py3.protobuf import message as _message
  from .google_py3.protobuf import reflection as _reflection
  from .google_py3.protobuf import symbol_database as _symbol_database
  from .google_py3.protobuf import descriptor_pb2


# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='control.proto',
  package='control',
  serialized_pb=_b('\n\rcontrol.proto\x12\x07\x63ontrol\"1\n\x07Message\x12\n\n\x02id\x18\x02 \x02(\x05\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='control.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='control.Message.id', index=0,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='control.Message.name', index=1,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='control.Message.data', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=75,
)

DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'control_pb2'
  # @@protoc_insertion_point(class_scope:control.Message)
  ))
_sym_db.RegisterMessage(Message)


# @@protoc_insertion_point(module_scope)
