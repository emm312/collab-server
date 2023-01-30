cmake_minimum_required(VERSION 3.0)

if (NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Debug)
endif()

project(collab_server)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall")
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)


include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()


file(GLOB_RECURSE sources src/*.cpp include/*.h)

add_executable(collab-server ${sources})
target_include_directories(collab-server PUBLIC ${CONAN_LIBS})
target_include_directories(collab-server PUBLIC include)
