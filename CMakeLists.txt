cmake_minimum_required(VERSION 3.15...3.26)
project(${SKBUILD_PROJECT_NAME} LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 14)

set(PYBIND11_FINDPYTHON ON)
find_package(pybind11 CONFIG REQUIRED)

set(boost_download_url
    "https://archives.boost.io/release/1.86.0/source/boost_1_86_0.tar.bz2")
set(boost_download_sha256
    "1bed88e40401b2cb7a1f76d4bab499e352fa4d0c5f31c0dbae64e24d34d7513b")

# Download and unpack boost if not available
set(boost_root "${CMAKE_BINARY_DIR}/vendor/boost")
set(boost_tar "${CMAKE_BINARY_DIR}/boost.tar.bz2")
file(MAKE_DIRECTORY "${boost_root}")
file(
  DOWNLOAD ${boost_download_url} ${boost_tar}
  EXPECTED_HASH SHA256=${boost_download_sha256}
  SHOW_PROGRESS)
if(NOT EXISTS ${boost_root}/README.md)
  message(STATUS "Extracting Boost...")
  execute_process(COMMAND tar xjf ${boost_tar} --strip-components=1
                  WORKING_DIRECTORY ${boost_root})
endif()

include_directories(${boost_root})
include_directories(${CMAKE_SOURCE_DIR}/vendor/findMFBase/include)

pybind11_add_module(_core MODULE src/main.cpp)
install(TARGETS _core DESTINATION ${SKBUILD_PROJECT_NAME})
