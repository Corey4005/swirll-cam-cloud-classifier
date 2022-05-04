# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detection/protos/model.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos import center_net_pb2 as object__detection_dot_protos_dot_center__net__pb2
from protos import faster_rcnn_pb2 as object__detection_dot_protos_dot_faster__rcnn__pb2
from protos import ssd_pb2 as object__detection_dot_protos_dot_ssd__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='object_detection/protos/model.proto',
  package='object_detection.protos',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n#object_detection/protos/model.proto\x12\x17object_detection.protos\x1a(object_detection/protos/center_net.proto\x1a)object_detection/protos/faster_rcnn.proto\x1a!object_detection/protos/ssd.proto\"\x86\x02\n\x0e\x44\x65tectionModel\x12:\n\x0b\x66\x61ster_rcnn\x18\x01 \x01(\x0b\x32#.object_detection.protos.FasterRcnnH\x00\x12+\n\x03ssd\x18\x02 \x01(\x0b\x32\x1c.object_detection.protos.SsdH\x00\x12H\n\x12\x65xperimental_model\x18\x03 \x01(\x0b\x32*.object_detection.protos.ExperimentalModelH\x00\x12\x38\n\ncenter_net\x18\x04 \x01(\x0b\x32\".object_detection.protos.CenterNetH\x00\x42\x07\n\x05model\"!\n\x11\x45xperimentalModel\x12\x0c\n\x04name\x18\x01 \x01(\t')
  ,
  dependencies=[object__detection_dot_protos_dot_center__net__pb2.DESCRIPTOR,object__detection_dot_protos_dot_faster__rcnn__pb2.DESCRIPTOR,object__detection_dot_protos_dot_ssd__pb2.DESCRIPTOR,])




_DETECTIONMODEL = _descriptor.Descriptor(
  name='DetectionModel',
  full_name='object_detection.protos.DetectionModel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='faster_rcnn', full_name='object_detection.protos.DetectionModel.faster_rcnn', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ssd', full_name='object_detection.protos.DetectionModel.ssd', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='experimental_model', full_name='object_detection.protos.DetectionModel.experimental_model', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='center_net', full_name='object_detection.protos.DetectionModel.center_net', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='model', full_name='object_detection.protos.DetectionModel.model',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=185,
  serialized_end=447,
)


_EXPERIMENTALMODEL = _descriptor.Descriptor(
  name='ExperimentalModel',
  full_name='object_detection.protos.ExperimentalModel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='object_detection.protos.ExperimentalModel.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=449,
  serialized_end=482,
)

_DETECTIONMODEL.fields_by_name['faster_rcnn'].message_type = object__detection_dot_protos_dot_faster__rcnn__pb2._FASTERRCNN
_DETECTIONMODEL.fields_by_name['ssd'].message_type = object__detection_dot_protos_dot_ssd__pb2._SSD
_DETECTIONMODEL.fields_by_name['experimental_model'].message_type = _EXPERIMENTALMODEL
_DETECTIONMODEL.fields_by_name['center_net'].message_type = object__detection_dot_protos_dot_center__net__pb2._CENTERNET
_DETECTIONMODEL.oneofs_by_name['model'].fields.append(
  _DETECTIONMODEL.fields_by_name['faster_rcnn'])
_DETECTIONMODEL.fields_by_name['faster_rcnn'].containing_oneof = _DETECTIONMODEL.oneofs_by_name['model']
_DETECTIONMODEL.oneofs_by_name['model'].fields.append(
  _DETECTIONMODEL.fields_by_name['ssd'])
_DETECTIONMODEL.fields_by_name['ssd'].containing_oneof = _DETECTIONMODEL.oneofs_by_name['model']
_DETECTIONMODEL.oneofs_by_name['model'].fields.append(
  _DETECTIONMODEL.fields_by_name['experimental_model'])
_DETECTIONMODEL.fields_by_name['experimental_model'].containing_oneof = _DETECTIONMODEL.oneofs_by_name['model']
_DETECTIONMODEL.oneofs_by_name['model'].fields.append(
  _DETECTIONMODEL.fields_by_name['center_net'])
_DETECTIONMODEL.fields_by_name['center_net'].containing_oneof = _DETECTIONMODEL.oneofs_by_name['model']
DESCRIPTOR.message_types_by_name['DetectionModel'] = _DETECTIONMODEL
DESCRIPTOR.message_types_by_name['ExperimentalModel'] = _EXPERIMENTALMODEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DetectionModel = _reflection.GeneratedProtocolMessageType('DetectionModel', (_message.Message,), {
  'DESCRIPTOR' : _DETECTIONMODEL,
  '__module__' : 'object_detection.protos.model_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.DetectionModel)
  })
_sym_db.RegisterMessage(DetectionModel)

ExperimentalModel = _reflection.GeneratedProtocolMessageType('ExperimentalModel', (_message.Message,), {
  'DESCRIPTOR' : _EXPERIMENTALMODEL,
  '__module__' : 'object_detection.protos.model_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.ExperimentalModel)
  })
_sym_db.RegisterMessage(ExperimentalModel)


# @@protoc_insertion_point(module_scope)
