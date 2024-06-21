cmake_minimum_required(VERSION 3.15...3.26)
project(${SKBUILD_PROJECT_NAME} LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 14)

set(PYBIND11_FINDPYTHON ON)
find_package(pybind11 CONFIG REQUIRED)

# TODO it did not work with static linking because on my machine apparently i
# only have a dynamic library of zstd , which is required by boost
set(Boost_USE_STATIC_LIBS OFF)

find_package(
  Boost REQUIRED
  COMPONENTS date_time
             filesystem
             system
             iostreams
             thread
             regex
             program_options
             unit_test_framework)
if(Boost_FOUND)
  include_directories(${Boost_INCLUDE_DIRS})
endif()
include_directories(${CMAKE_SOURCE_DIR}/vendor/findMFBase/include)

find_package(ZSTD REQUIRED)
if(ZSTD_FOUND)
  include_directories(${ZSTD_INCLUDE_DIRS})
endif()

pybind11_add_module(_core MODULE src/main.cpp)
target_link_libraries(_core PRIVATE ${Boost_LIBRARIES})
target_link_libraries(_core PRIVATE ${ZSTD_LIBRARIES})
install(TARGETS _core DESTINATION ${SKBUILD_PROJECT_NAME})

# Add the subdirectory for the findMFBase project
# add_subdirectory(vendor/findMFBase) Link the findMFBase library to the _core
# module target_link_libraries(_core PRIVATE findMFBase)
