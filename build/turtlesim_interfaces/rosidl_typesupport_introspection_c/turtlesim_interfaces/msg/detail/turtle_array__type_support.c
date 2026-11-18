// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from turtlesim_interfaces:msg/TurtleArray.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "turtlesim_interfaces/msg/detail/turtle_array__rosidl_typesupport_introspection_c.h"
#include "turtlesim_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "turtlesim_interfaces/msg/detail/turtle_array__functions.h"
#include "turtlesim_interfaces/msg/detail/turtle_array__struct.h"


// Include directives for member types
// Member `array`
#include "turtlesim_interfaces/msg/turtle.h"
// Member `array`
#include "turtlesim_interfaces/msg/detail/turtle__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void turtlesim_interfaces__msg__TurtleArray__rosidl_typesupport_introspection_c__TurtleArray_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  turtlesim_interfaces__msg__TurtleArray__init(message_memory);
}

void turtlesim_interfaces__msg__TurtleArray__rosidl_typesupport_introspection_c__TurtleArray_fini_function(void * message_memory)
{
  turtlesim_interfaces__msg__TurtleArray__fini(message_memory);
}

size_t turtlesim_interfaces__msg__TurtleArray__rosidl_typesupport_introspection_c__size_function__TurtleArray__array(
  const void * untyped_member)
{
  const turtlesim_interfaces__msg__Turtle__Sequence * member =
    (const turtlesim_interfaces__msg__Turtle__Sequence *)(untyped_member);
  return member->size;
}

const void * turtlesim_interfaces__msg__TurtleArray__rosidl_typesupport_introspection_c__get_const_function__TurtleArray__array(
  const void * untyped_member, size_t index)
{
  const turtlesim_interfaces__msg__Turtle__Sequence * member =
    (const turtlesim_interfaces__msg__Turtle__Sequence *)(untyped_member);
  return &member->data[index];
}

void * turtlesim_interfaces__msg__TurtleArray__rosidl_typesupport_introspection_c__get_function__TurtleArray__array(
  void * untyped_member, size_t index)
{
  turtlesim_interfaces__msg__Turtle__Sequence * member =
    (turtlesim_interfaces__msg__Turtle__Sequence *)(untyped_member);
  return &member->data[index];
}

void turtlesim_interfaces__msg__TurtleArray__rosidl_typesupport_introspection_c__fetch_function__TurtleArray__array(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const turtlesim_interfaces__msg__Turtle * item =
    ((const turtlesim_interfaces__msg__Turtle *)
    turtlesim_interfaces__msg__TurtleArray__rosidl_typesupport_introspection_c__get_const_function__TurtleArray__array(untyped_member, index));
  turtlesim_interfaces__msg__Turtle * value =
    (turtlesim_interfaces__msg__Turtle *)(untyped_value);
  *value = *item;
}

void turtlesim_interfaces__msg__TurtleArray__rosidl_typesupport_introspection_c__assign_function__TurtleArray__array(
  void * untyped_member, size_t index, const void * untyped_value)
{
  turtlesim_interfaces__msg__Turtle * item =
    ((turtlesim_interfaces__msg__Turtle *)
    turtlesim_interfaces__msg__TurtleArray__rosidl_typesupport_introspection_c__get_function__TurtleArray__array(untyped_member, index));
  const turtlesim_interfaces__msg__Turtle * value =
    (const turtlesim_interfaces__msg__Turtle *)(untyped_value);
  *item = *value;
}

bool turtlesim_interfaces__msg__TurtleArray__rosidl_typesupport_introspection_c__resize_function__TurtleArray__array(
  void * untyped_member, size_t size)
{
  turtlesim_interfaces__msg__Turtle__Sequence * member =
    (turtlesim_interfaces__msg__Turtle__Sequence *)(untyped_member);
  turtlesim_interfaces__msg__Turtle__Sequence__fini(member);
  return turtlesim_interfaces__msg__Turtle__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember turtlesim_interfaces__msg__TurtleArray__rosidl_typesupport_introspection_c__TurtleArray_message_member_array[1] = {
  {
    "array",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(turtlesim_interfaces__msg__TurtleArray, array),  // bytes offset in struct
    NULL,  // default value
    turtlesim_interfaces__msg__TurtleArray__rosidl_typesupport_introspection_c__size_function__TurtleArray__array,  // size() function pointer
    turtlesim_interfaces__msg__TurtleArray__rosidl_typesupport_introspection_c__get_const_function__TurtleArray__array,  // get_const(index) function pointer
    turtlesim_interfaces__msg__TurtleArray__rosidl_typesupport_introspection_c__get_function__TurtleArray__array,  // get(index) function pointer
    turtlesim_interfaces__msg__TurtleArray__rosidl_typesupport_introspection_c__fetch_function__TurtleArray__array,  // fetch(index, &value) function pointer
    turtlesim_interfaces__msg__TurtleArray__rosidl_typesupport_introspection_c__assign_function__TurtleArray__array,  // assign(index, value) function pointer
    turtlesim_interfaces__msg__TurtleArray__rosidl_typesupport_introspection_c__resize_function__TurtleArray__array  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers turtlesim_interfaces__msg__TurtleArray__rosidl_typesupport_introspection_c__TurtleArray_message_members = {
  "turtlesim_interfaces__msg",  // message namespace
  "TurtleArray",  // message name
  1,  // number of fields
  sizeof(turtlesim_interfaces__msg__TurtleArray),
  turtlesim_interfaces__msg__TurtleArray__rosidl_typesupport_introspection_c__TurtleArray_message_member_array,  // message members
  turtlesim_interfaces__msg__TurtleArray__rosidl_typesupport_introspection_c__TurtleArray_init_function,  // function to initialize message memory (memory has to be allocated)
  turtlesim_interfaces__msg__TurtleArray__rosidl_typesupport_introspection_c__TurtleArray_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t turtlesim_interfaces__msg__TurtleArray__rosidl_typesupport_introspection_c__TurtleArray_message_type_support_handle = {
  0,
  &turtlesim_interfaces__msg__TurtleArray__rosidl_typesupport_introspection_c__TurtleArray_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_turtlesim_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, turtlesim_interfaces, msg, TurtleArray)() {
  turtlesim_interfaces__msg__TurtleArray__rosidl_typesupport_introspection_c__TurtleArray_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, turtlesim_interfaces, msg, Turtle)();
  if (!turtlesim_interfaces__msg__TurtleArray__rosidl_typesupport_introspection_c__TurtleArray_message_type_support_handle.typesupport_identifier) {
    turtlesim_interfaces__msg__TurtleArray__rosidl_typesupport_introspection_c__TurtleArray_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &turtlesim_interfaces__msg__TurtleArray__rosidl_typesupport_introspection_c__TurtleArray_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
