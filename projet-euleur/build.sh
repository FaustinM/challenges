#!/bin/bash
g++ -ggdb -std=c++11 ./$1.cpp -o bin/$1 && echo "Fin du build" && time ./bin/$1