# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: connection.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='connection.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x63onnection.proto\"e\n\x08Location\x12\x11\n\tperson_id\x18\x01 \x01(\x05\x12\x11\n\tlongitude\x18\x02 \x01(\t\x12\x10\n\x08latitude\x18\x03 \x01(\t\x12\x15\n\rcreation_time\x18\x04 \x01(\t\x12\n\n\x02id\x18\x05 \x01(\x05\"Q\n\x06Person\x12\x14\n\x0c\x63ompany_name\x18\x01 \x01(\t\x12\x11\n\tlast_name\x18\x02 \x01(\t\x12\x12\n\nfirst_name\x18\x03 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\x05\"I\n\x11\x43onnectionMessage\x12\x1b\n\x08location\x18\x01 \x01(\x0b\x32\t.Location\x12\x17\n\x06person\x18\x02 \x01(\x0b\x32\x07.Person\"@\n\x15\x43onnectionMessageList\x12\'\n\x0b\x63onnections\x18\x01 \x03(\x0b\x32\x12.ConnectionMessage\"R\n\x07\x43ontact\x12\x11\n\tperson_id\x18\x01 \x01(\x05\x12\x12\n\nstart_date\x18\x02 \x01(\t\x12\x10\n\x08\x65nd_date\x18\x03 \x01(\t\x12\x0e\n\x06meters\x18\x04 \x01(\x05\"\x07\n\x05\x45mpty2g\n\x11\x43onnectionService\x12%\n\x03Get\x12\x06.Empty\x1a\x16.ConnectionMessageList\x12+\n\x07GetList\x12\x08.Contact\x1a\x16.ConnectionMessageListb\x06proto3'
)




_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='person_id', full_name='Location.person_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='Location.longitude', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='Location.latitude', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creation_time', full_name='Location.creation_time', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='Location.id', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=20,
  serialized_end=121,
)


_PERSON = _descriptor.Descriptor(
  name='Person',
  full_name='Person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='company_name', full_name='Person.company_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='Person.last_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='Person.first_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='Person.id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=123,
  serialized_end=204,
)


_CONNECTIONMESSAGE = _descriptor.Descriptor(
  name='ConnectionMessage',
  full_name='ConnectionMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='location', full_name='ConnectionMessage.location', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='person', full_name='ConnectionMessage.person', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=206,
  serialized_end=279,
)


_CONNECTIONMESSAGELIST = _descriptor.Descriptor(
  name='ConnectionMessageList',
  full_name='ConnectionMessageList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='connections', full_name='ConnectionMessageList.connections', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=281,
  serialized_end=345,
)


_CONTACT = _descriptor.Descriptor(
  name='Contact',
  full_name='Contact',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='person_id', full_name='Contact.person_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_date', full_name='Contact.start_date', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_date', full_name='Contact.end_date', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='meters', full_name='Contact.meters', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=347,
  serialized_end=429,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=431,
  serialized_end=438,
)

_CONNECTIONMESSAGE.fields_by_name['location'].message_type = _LOCATION
_CONNECTIONMESSAGE.fields_by_name['person'].message_type = _PERSON
_CONNECTIONMESSAGELIST.fields_by_name['connections'].message_type = _CONNECTIONMESSAGE
DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
DESCRIPTOR.message_types_by_name['Person'] = _PERSON
DESCRIPTOR.message_types_by_name['ConnectionMessage'] = _CONNECTIONMESSAGE
DESCRIPTOR.message_types_by_name['ConnectionMessageList'] = _CONNECTIONMESSAGELIST
DESCRIPTOR.message_types_by_name['Contact'] = _CONTACT
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), {
  'DESCRIPTOR' : _LOCATION,
  '__module__' : 'connection_pb2'
  # @@protoc_insertion_point(class_scope:Location)
  })
_sym_db.RegisterMessage(Location)

Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), {
  'DESCRIPTOR' : _PERSON,
  '__module__' : 'connection_pb2'
  # @@protoc_insertion_point(class_scope:Person)
  })
_sym_db.RegisterMessage(Person)

ConnectionMessage = _reflection.GeneratedProtocolMessageType('ConnectionMessage', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTIONMESSAGE,
  '__module__' : 'connection_pb2'
  # @@protoc_insertion_point(class_scope:ConnectionMessage)
  })
_sym_db.RegisterMessage(ConnectionMessage)

ConnectionMessageList = _reflection.GeneratedProtocolMessageType('ConnectionMessageList', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTIONMESSAGELIST,
  '__module__' : 'connection_pb2'
  # @@protoc_insertion_point(class_scope:ConnectionMessageList)
  })
_sym_db.RegisterMessage(ConnectionMessageList)

Contact = _reflection.GeneratedProtocolMessageType('Contact', (_message.Message,), {
  'DESCRIPTOR' : _CONTACT,
  '__module__' : 'connection_pb2'
  # @@protoc_insertion_point(class_scope:Contact)
  })
_sym_db.RegisterMessage(Contact)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'connection_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)



_CONNECTIONSERVICE = _descriptor.ServiceDescriptor(
  name='ConnectionService',
  full_name='ConnectionService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=440,
  serialized_end=543,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='ConnectionService.Get',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_CONNECTIONMESSAGELIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetList',
    full_name='ConnectionService.GetList',
    index=1,
    containing_service=None,
    input_type=_CONTACT,
    output_type=_CONNECTIONMESSAGELIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONNECTIONSERVICE)

DESCRIPTOR.services_by_name['ConnectionService'] = _CONNECTIONSERVICE

# @@protoc_insertion_point(module_scope)
