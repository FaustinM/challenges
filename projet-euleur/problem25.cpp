#include <iostream>
#include <string>
#include "BigInt.hpp"
#include "math_utils.cpp"

using namespace std;

int main() {
    // TODO : Ca marche pas correctement
    BigInt target = big_pow10(1000); // 4782
    BigInt a(0), b(1);
    double i = 1;
    while (a < target){
        i++;
        a = b;
        b = a+b;
    }
    cout << i << endl;
    return 0;
}
