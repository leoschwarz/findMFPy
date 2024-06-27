cmake_minimum_required(VERSION 3.15...3.26)
project(${SKBUILD_PROJECT_NAME} LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 14)

set(PYBIND11_FINDPYTHON ON)
find_package(pybind11 CONFIG REQUIRED)

# TODO it did not work with static linking because on my machine apparently i
# only have a dynamic library of zstd , which is required by boost
# set(Boost_USE_STATIC_LIBS OFF)
#
# find_package( Boost REQUIRED COMPONENTS date_time filesystem system iostreams
# thread regex program_options unit_test_framework) if(Boost_FOUND)
# include_directories(${Boost_INCLUDE_DIRS}) endif()

# include_directories( ${CMAKE_SOURCE_DIR}/vendor/boost/libs/date_time/include
# ${CMAKE_SOURCE_DIR}/vendor/boost/libs/filesystem/include
# ${CMAKE_SOURCE_DIR}/vendor/boost/libs/system/include
# ${CMAKE_SOURCE_DIR}/vendor/boost/libs/iostreams/include
# ${CMAKE_SOURCE_DIR}/vendor/boost/libs/thread/include
# ${CMAKE_SOURCE_DIR}/vendor/boost/libs/regex/include
# ${CMAKE_SOURCE_DIR}/vendor/boost/libs/program_options/include # TODO maybe
# optional ${CMAKE_SOURCE_DIR}/vendor/boost/libs/unit_test_framework/include
# addde while trying to make it work
# ${CMAKE_SOURCE_DIR}/vendor/boost/libs/config/include
# ${CMAKE_SOURCE_DIR}/vendor/boost/libs/bind/include
# ${CMAKE_SOURCE_DIR}/vendor/boost/libs/range/include
# ${CMAKE_SOURCE_DIR}/vendor/boost/libs/assert/include
# ${CMAKE_SOURCE_DIR}/vendor/boost/libs/preprocessor/include
# ${CMAKE_SOURCE_DIR}/vendor/boost/libs/assign/include
# ${CMAKE_SOURCE_DIR}/vendor/boost/libs/detail/include
# ${CMAKE_SOURCE_DIR}/vendor/boost/libs/mpl/include
# ${CMAKE_SOURCE_DIR}/vendor/boost/libs/move/include
# ${CMAKE_SOURCE_DIR}/vendor/boost/libs/concept_check/include
#
# ${CMAKE_SOURCE_DIR}/vendor/boost/libs/iterator/include
# ${CMAKE_SOURCE_DIR}/vendor/boost/libs/static_assert/include
# ${CMAKE_SOURCE_DIR}/vendor/boost/libs/type_traits/include
# ${CMAKE_SOURCE_DIR}/vendor/boost-core/include)

# list all boost libs and add them all to the include directories by globbing
set(BOOST_LIBS
    accumulators
    algorithm
    align
    any
    array
    asio
    assert
    assign
    atomic
    beast
    bimap
    bind
    callable_traits
    charconv
    chrono
    circular_buffer
    cobalt
    compat
    compatibility
    compute
    concept_check
    config
    container
    container_hash
    context
    contract
    conversion
    convert
    core
    coroutine
    coroutine2
    crc
    date_time
    describe
    detail
    dll
    dynamic_bitset
    endian
    exception
    fiber
    filesystem
    flyweight
    foreach
    format
    function
    function_types
    functional
    fusion
    geometry
    gil
    graph
    graph_parallel
    hana
    headers
    heap
    histogram
    hof
    icl
    index.html
    integer
    interprocess
    intrusive
    io
    iostreams
    iterator
    json
    lambda
    lambda2
    leaf
    lexical_cast
    libraries.htm
    local_function
    locale
    lockfree
    log
    logic
    maintainers.txt
    math
    metaparse
    move
    mp11
    mpi
    mpl
    msm
    multi_array
    multi_index
    multiprecision
    mysql
    nowide
    numeric/conversion
    optional
    outcome
    parameter
    parameter_python
    pfr
    phoenix
    platform_maintainers.txt
    poly_collection
    polygon
    pool
    predef
    preprocessor
    process
    program_options
    property_map
    property_map_parallel
    property_tree
    proto
    ptr_container
    python
    qvm
    random
    range
    ratio
    rational
    redis
    regex
    safe_numerics
    scope
    scope_exit
    serialization
    signals2
    smart_ptr
    sort
    spirit
    stacktrace
    statechart
    static_assert
    static_string
    stl_interfaces
    system
    test
    thread
    throw_exception
    timer
    tokenizer
    tti
    tuple
    type_erasure
    type_index
    type_traits
    typeof
    units
    unordered
    url
    utility
    uuid
    variant
    variant2
    vmd
    wave
    winapi
    xpressive
    yap)
foreach(lib ${BOOST_LIBS})
  include_directories(${CMAKE_SOURCE_DIR}/vendor/boost/libs/${lib}/include)
endforeach()

# foreach (file(${CMAKE_SOURCE_DIR}/vendor/boost/libs/*) if (IS_DIRECTORY
# ${file}) include_directories(${file}/include) endif() endforeach()

include_directories(${CMAKE_SOURCE_DIR}/vendor/findMFBase/include)

# find_package(ZSTD REQUIRED) if(ZSTD_FOUND)
# include_directories(${ZSTD_INCLUDE_DIRS}) endif()

pybind11_add_module(_core MODULE src/main.cpp)
# target_link_libraries(_core PRIVATE ${Boost_LIBRARIES})
# target_link_libraries(_core PRIVATE ${ZSTD_LIBRARIES})
install(TARGETS _core DESTINATION ${SKBUILD_PROJECT_NAME})

# Add the subdirectory for the findMFBase project
# add_subdirectory(vendor/findMFBase) Link the findMFBase library to the _core
# module target_link_libraries(_core PRIVATE findMFBase)
