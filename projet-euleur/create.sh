#!/bin/bash
echo "#include <iostream>" >> $1.cpp
echo "#include <string>" >> $1.cpp
echo "#include \"math_utils.cpp\"" >> $1.cpp
echo "" >> $1.cpp
echo "using namespace std;" >> $1.cpp
echo "" >> $1.cpp
echo "int main() {" >> $1.cpp
echo "    return 0;" >> $1.cpp
echo "}" >> $1.cpp