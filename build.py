#!/usr/bin/python3
import os
import subprocess
import sys

if sys.argv.__contains__("--release"):
    CMAKE_BUILD_TYPE = "Release"
else:
    CMAKE_BUILD_TYPE = "Debug"

subprocess.run(["mkdir", "build"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if os.path.exists("build/conan.lock") == False:
    os.system("cd build && conan install ..")

os.system("cd build && cmake .. -DCMAKE_BUILD_TYPE={CMAKE_BUILD_TYPE}")

os.system(f"cd build && cmake --build .")

if sys.argv.__contains__("--run"):
    os.system(f"./build/bin/collab-server")
