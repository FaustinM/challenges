#include <iostream>
#include <string>
#include "math_utils.cpp"

using namespace std;

vector<long long> v;

int main() {
    v.push_back(0);
    for (int i = 1; i < 10000; i++){
        v.push_back(sumList(listDivisors(i)));
    }

    size_t v_size = v.size();
    long long somme;
    for (int i = 0; i < v_size; i++){
        if(v[i] < v_size && v[v[i]] == i && v[i] != i){
            cout << "HEY" << endl;
            somme = somme+i;
        }
    }
    cout << somme << endl;
    return 0;
}
