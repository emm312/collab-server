#!/usr/bin/python3
import os
import subprocess
import sys

if sys.argv.__contains__("--release"):
    CMAKE_BUILD_TYPE = "Release"
else:
    CMAKE_BUILD_TYPE = "Debug"

subprocess.run(["mkdir", "build"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

os.system("cd build && conan install .. --build missing")

os.system("cd build && cmake .. -DCMAKE_BUILD_TYPE={CMAKE_BUILD_TYPE} -DCMAKE_EXPORT_COMPILE_COMMANDS=1")
os.system("ln -sf build/compile_commands.json .")

os.system(f"cd build && cmake --build .")

if sys.argv.__contains__("--run"):
    os.system(f"./build/bin/collab-server")
