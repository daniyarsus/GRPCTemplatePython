# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: text_processor.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14text_processor.proto\"\x1b\n\x0bTextRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\"&\n\x0cTextResponse\x12\x16\n\x0eprocessed_text\x18\x01 \x01(\t2;\n\rTextProcessor\x12*\n\x0bProcessText\x12\x0c.TextRequest\x1a\r.TextResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'text_processor_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TEXTREQUEST']._serialized_start=24
  _globals['_TEXTREQUEST']._serialized_end=51
  _globals['_TEXTRESPONSE']._serialized_start=53
  _globals['_TEXTRESPONSE']._serialized_end=91
  _globals['_TEXTPROCESSOR']._serialized_start=93
  _globals['_TEXTPROCESSOR']._serialized_end=152
# @@protoc_insertion_point(module_scope)
