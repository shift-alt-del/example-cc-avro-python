# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/sr.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11protobuf/sr.proto\x12\x08tutorial\"\xdb\x01\n\x06Person\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12,\n\x06phones\x18\x04 \x03(\x0b\x32\x1c.tutorial.Person.PhoneNumber\x1aM\n\x0bPhoneNumber\x12\x0e\n\x06number\x18\x01 \x01(\t\x12.\n\x04type\x18\x02 \x01(\x0e\x32\x1a.tutorial.Person.PhoneType:\x04HOME\"+\n\tPhoneType\x12\n\n\x06MOBILE\x10\x00\x12\x08\n\x04HOME\x10\x01\x12\x08\n\x04WORK\x10\x02')



_PERSON = DESCRIPTOR.message_types_by_name['Person']
_PERSON_PHONENUMBER = _PERSON.nested_types_by_name['PhoneNumber']
_PERSON_PHONETYPE = _PERSON.enum_types_by_name['PhoneType']
Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), {

  'PhoneNumber' : _reflection.GeneratedProtocolMessageType('PhoneNumber', (_message.Message,), {
    'DESCRIPTOR' : _PERSON_PHONENUMBER,
    '__module__' : 'protobuf.sr_pb2'
    # @@protoc_insertion_point(class_scope:tutorial.Person.PhoneNumber)
    })
  ,
  'DESCRIPTOR' : _PERSON,
  '__module__' : 'protobuf.sr_pb2'
  # @@protoc_insertion_point(class_scope:tutorial.Person)
  })
_sym_db.RegisterMessage(Person)
_sym_db.RegisterMessage(Person.PhoneNumber)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PERSON._serialized_start=32
  _PERSON._serialized_end=251
  _PERSON_PHONENUMBER._serialized_start=129
  _PERSON_PHONENUMBER._serialized_end=206
  _PERSON_PHONETYPE._serialized_start=208
  _PERSON_PHONETYPE._serialized_end=251
# @@protoc_insertion_point(module_scope)
