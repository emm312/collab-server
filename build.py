#!/usr/bin/python3
import os
import subprocess
import sys

if sys.argv.__contains__("--release"):
    CMAKE_BUILD_TYPE = "Release"
else:
    CMAKE_BUILD_TYPE = "Debug"

# Wait not export the compile commands in the cmake file then just soft link/move them after running the script
# You know how cmake can expor t compile_command.json
# yeah ik


# o yea i forgor

subprocess.run(["mkdir", "build"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

os.system("cd build && conan install .. --build missing")

# I added compile commands export into the cmake file itself
# I can actually import asio in main.cpp
os.system("cd build && cmake .. -DCMAKE_BUILD_TYPE={CMAKE_BUILD_TYPE} -DCMAKE_EXPORT_COMPILE_COMMANDS=1")
os.system("ln -sf build/compile_commands.json .")

os.system(f"cd build && cmake --build .")

if sys.argv.__contains__("--run"):
    os.system(f"./build/bin/collab-server")
