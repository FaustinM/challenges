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
    ifstream EulerFile("input/problem67.txt");

    vector<vector<int>> lines;

    string line;
    while (getline(EulerFile, line)) {
        vector<int> parsedLine;
        string subline = "";
        for (unsigned int i = 0; i < line.size(); i++){
            if(line[i] == ' '){
                parsedLine.push_back(strToInt(subline));
                subline = "";
            } else {
                subline.push_back(line[i]);
            }
        }
        parsedLine.push_back(strToInt(subline));
        lines.push_back(parsedLine);
    }
    cout << max_value(lines, 0, 0);
    EulerFile.close();

    return 0;
}