// Djikstra ?

#include <iostream>
#include <string>
#include "math_utils.cpp"
#include <fstream>
#include <vector>

using namespace std;

unsigned int max_value(vector<vector<int>> v, size_t y, size_t x){
    if(y >= v.size()-1) return v[y][x];
    else {
        unsigned int left = v[y][x]+max_value(v, y+1, x);
        unsigned int right = v[y][x]+max_value(v, y+1, x+1);
        if (left >= right) return left;
        else return right;
    }
}

int main() {
    ifstream EulerFile("input/problem22-trie.txt");

    vector<long long> lines;

    string line;
    while (getline(EulerFile, line)) {
        long long value = 0;
        for (int i = 0; i < line.size(); i++){
            value = value + (int)(line[i] - 'A')+1;
        }
        lines.push_back(value*(lines.size()+1));
    }
    cout << sumList(lines) << endl;
    EulerFile.close();

    return 0;
}