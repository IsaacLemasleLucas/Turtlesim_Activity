# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target turtlesim_interfaces::turtlesim_interfaces
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${turtlesim_interfaces_TARGETS}.
if(turtlesim_interfaces_TARGETS AND NOT TARGET turtlesim_interfaces::turtlesim_interfaces)
  add_library(turtlesim_interfaces::turtlesim_interfaces INTERFACE IMPORTED)
  set_target_properties(turtlesim_interfaces::turtlesim_interfaces PROPERTIES
    INTERFACE_LINK_LIBRARIES "${turtlesim_interfaces_TARGETS}")
endif()
