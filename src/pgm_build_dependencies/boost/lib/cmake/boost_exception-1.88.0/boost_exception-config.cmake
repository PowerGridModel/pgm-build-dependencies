# Generated by Boost 1.88.0

if(TARGET Boost::exception)
  return()
endif()

if(Boost_VERBOSE OR Boost_DEBUG)
  message(STATUS "Found boost_exception ${boost_exception_VERSION} at ${boost_exception_DIR}")
endif()

mark_as_advanced(boost_exception_DIR)

# Compute the include and library directories relative to this file.

get_filename_component(_BOOST_CMAKEDIR "${CMAKE_CURRENT_LIST_DIR}/../" REALPATH)

# If the computed and the original directories are symlink-equivalent, use original
if(EXISTS "/home/linuxbrew/.linuxbrew/Cellar/boost/1.88.0/lib/cmake")
  get_filename_component(_BOOST_CMAKEDIR_ORIGINAL "/home/linuxbrew/.linuxbrew/Cellar/boost/1.88.0/lib/cmake" REALPATH)
  if(_BOOST_CMAKEDIR STREQUAL _BOOST_CMAKEDIR_ORIGINAL)
    set(_BOOST_CMAKEDIR "/home/linuxbrew/.linuxbrew/Cellar/boost/1.88.0/lib/cmake")
  endif()
  unset(_BOOST_CMAKEDIR_ORIGINAL)
endif()

get_filename_component(_BOOST_INCLUDEDIR "${_BOOST_CMAKEDIR}/../../include/" ABSOLUTE)

add_library(Boost::exception INTERFACE IMPORTED)

set_target_properties(Boost::exception PROPERTIES
  INTERFACE_INCLUDE_DIRECTORIES "${_BOOST_INCLUDEDIR}"
)

unset(_BOOST_INCLUDEDIR)
unset(_BOOST_CMAKEDIR)
