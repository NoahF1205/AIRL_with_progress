# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from kortex_driver/ReadAllMappingsRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import kortex_driver.msg

class ReadAllMappingsRequest(genpy.Message):
  _md5sum = "fa3403cd5897c9698bc0fdcb2a453fbc"
  _type = "kortex_driver/ReadAllMappingsRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """Empty input

================================================================================
MSG: kortex_driver/Empty
"""
  __slots__ = ['input']
  _slot_types = ['kortex_driver/Empty']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       input

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ReadAllMappingsRequest, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.input is None:
        self.input = kortex_driver.msg.Empty()
    else:
      self.input = kortex_driver.msg.Empty()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.input is None:
        self.input = kortex_driver.msg.Empty()
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.input is None:
        self.input = kortex_driver.msg.Empty()
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from kortex_driver/ReadAllMappingsResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import kortex_driver.msg

class ReadAllMappingsResponse(genpy.Message):
  _md5sum = "f318987fb4be88e1c786ff4d68235a14"
  _type = "kortex_driver/ReadAllMappingsResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """MappingList output

================================================================================
MSG: kortex_driver/MappingList

Mapping[] mappings
================================================================================
MSG: kortex_driver/Mapping

MappingHandle handle
string name
uint32 controller_identifier
MapGroupHandle active_map_group_handle
MapGroupHandle[] map_group_handles
MapHandle active_map_handle
MapHandle[] map_handles
string application_data
================================================================================
MSG: kortex_driver/MappingHandle

uint32 identifier
uint32 permission
================================================================================
MSG: kortex_driver/MapGroupHandle

uint32 identifier
uint32 permission
================================================================================
MSG: kortex_driver/MapHandle

uint32 identifier
uint32 permission"""
  __slots__ = ['output']
  _slot_types = ['kortex_driver/MappingList']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       output

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ReadAllMappingsResponse, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.output is None:
        self.output = kortex_driver.msg.MappingList()
    else:
      self.output = kortex_driver.msg.MappingList()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.output.mappings)
      buff.write(_struct_I.pack(length))
      for val1 in self.output.mappings:
        _v1 = val1.handle
        _x = _v1
        buff.write(_get_struct_2I().pack(_x.identifier, _x.permission))
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.controller_identifier
        buff.write(_get_struct_I().pack(_x))
        _v2 = val1.active_map_group_handle
        _x = _v2
        buff.write(_get_struct_2I().pack(_x.identifier, _x.permission))
        length = len(val1.map_group_handles)
        buff.write(_struct_I.pack(length))
        for val2 in val1.map_group_handles:
          _x = val2
          buff.write(_get_struct_2I().pack(_x.identifier, _x.permission))
        _v3 = val1.active_map_handle
        _x = _v3
        buff.write(_get_struct_2I().pack(_x.identifier, _x.permission))
        length = len(val1.map_handles)
        buff.write(_struct_I.pack(length))
        for val2 in val1.map_handles:
          _x = val2
          buff.write(_get_struct_2I().pack(_x.identifier, _x.permission))
        _x = val1.application_data
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.output is None:
        self.output = kortex_driver.msg.MappingList()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.output.mappings = []
      for i in range(0, length):
        val1 = kortex_driver.msg.Mapping()
        _v4 = val1.handle
        _x = _v4
        start = end
        end += 8
        (_x.identifier, _x.permission,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.name = str[start:end]
        start = end
        end += 4
        (val1.controller_identifier,) = _get_struct_I().unpack(str[start:end])
        _v5 = val1.active_map_group_handle
        _x = _v5
        start = end
        end += 8
        (_x.identifier, _x.permission,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.map_group_handles = []
        for i in range(0, length):
          val2 = kortex_driver.msg.MapGroupHandle()
          _x = val2
          start = end
          end += 8
          (_x.identifier, _x.permission,) = _get_struct_2I().unpack(str[start:end])
          val1.map_group_handles.append(val2)
        _v6 = val1.active_map_handle
        _x = _v6
        start = end
        end += 8
        (_x.identifier, _x.permission,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.map_handles = []
        for i in range(0, length):
          val2 = kortex_driver.msg.MapHandle()
          _x = val2
          start = end
          end += 8
          (_x.identifier, _x.permission,) = _get_struct_2I().unpack(str[start:end])
          val1.map_handles.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.application_data = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.application_data = str[start:end]
        self.output.mappings.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.output.mappings)
      buff.write(_struct_I.pack(length))
      for val1 in self.output.mappings:
        _v7 = val1.handle
        _x = _v7
        buff.write(_get_struct_2I().pack(_x.identifier, _x.permission))
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.controller_identifier
        buff.write(_get_struct_I().pack(_x))
        _v8 = val1.active_map_group_handle
        _x = _v8
        buff.write(_get_struct_2I().pack(_x.identifier, _x.permission))
        length = len(val1.map_group_handles)
        buff.write(_struct_I.pack(length))
        for val2 in val1.map_group_handles:
          _x = val2
          buff.write(_get_struct_2I().pack(_x.identifier, _x.permission))
        _v9 = val1.active_map_handle
        _x = _v9
        buff.write(_get_struct_2I().pack(_x.identifier, _x.permission))
        length = len(val1.map_handles)
        buff.write(_struct_I.pack(length))
        for val2 in val1.map_handles:
          _x = val2
          buff.write(_get_struct_2I().pack(_x.identifier, _x.permission))
        _x = val1.application_data
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.output is None:
        self.output = kortex_driver.msg.MappingList()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.output.mappings = []
      for i in range(0, length):
        val1 = kortex_driver.msg.Mapping()
        _v10 = val1.handle
        _x = _v10
        start = end
        end += 8
        (_x.identifier, _x.permission,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.name = str[start:end]
        start = end
        end += 4
        (val1.controller_identifier,) = _get_struct_I().unpack(str[start:end])
        _v11 = val1.active_map_group_handle
        _x = _v11
        start = end
        end += 8
        (_x.identifier, _x.permission,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.map_group_handles = []
        for i in range(0, length):
          val2 = kortex_driver.msg.MapGroupHandle()
          _x = val2
          start = end
          end += 8
          (_x.identifier, _x.permission,) = _get_struct_2I().unpack(str[start:end])
          val1.map_group_handles.append(val2)
        _v12 = val1.active_map_handle
        _x = _v12
        start = end
        end += 8
        (_x.identifier, _x.permission,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.map_handles = []
        for i in range(0, length):
          val2 = kortex_driver.msg.MapHandle()
          _x = val2
          start = end
          end += 8
          (_x.identifier, _x.permission,) = _get_struct_2I().unpack(str[start:end])
          val1.map_handles.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.application_data = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.application_data = str[start:end]
        self.output.mappings.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
class ReadAllMappings(object):
  _type          = 'kortex_driver/ReadAllMappings'
  _md5sum = 'b5feb1f35cacb5c11e26808022e25f5c'
  _request_class  = ReadAllMappingsRequest
  _response_class = ReadAllMappingsResponse