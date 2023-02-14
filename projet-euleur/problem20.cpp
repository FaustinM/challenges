#include <iostream>
#include <string>
#include "math_big_int.cpp"

using namespace std;

int main() {
    // TODO : Implémenter BigInt
    cout << big_sumDigit(big_factoriel(100)) << endl;
    // cout << "La solution est " << to_string(factoriel_iter(10)) << endl;
    return 0;
}
