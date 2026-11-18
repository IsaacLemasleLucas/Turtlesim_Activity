// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from turtlesim_interfaces:msg/TurtleArray.idl
// generated code does not contain a copyright notice

#ifndef TURTLESIM_INTERFACES__MSG__DETAIL__TURTLE_ARRAY__BUILDER_HPP_
#define TURTLESIM_INTERFACES__MSG__DETAIL__TURTLE_ARRAY__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "turtlesim_interfaces/msg/detail/turtle_array__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace turtlesim_interfaces
{

namespace msg
{

namespace builder
{

class Init_TurtleArray_array
{
public:
  Init_TurtleArray_array()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::turtlesim_interfaces::msg::TurtleArray array(::turtlesim_interfaces::msg::TurtleArray::_array_type arg)
  {
    msg_.array = std::move(arg);
    return std::move(msg_);
  }

private:
  ::turtlesim_interfaces::msg::TurtleArray msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::turtlesim_interfaces::msg::TurtleArray>()
{
  return turtlesim_interfaces::msg::builder::Init_TurtleArray_array();
}

}  // namespace turtlesim_interfaces

#endif  // TURTLESIM_INTERFACES__MSG__DETAIL__TURTLE_ARRAY__BUILDER_HPP_
