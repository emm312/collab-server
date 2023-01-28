.PHONY: build run

run: build
	./build/bin/collab-server

build:
	-mkdir build
	cd build && conan install ..
	cd build && cmake ..
	cd build && cmake --build .