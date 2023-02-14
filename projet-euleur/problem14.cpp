#include <iostream>
#include <string>
#include <unordered_map>
#include "math_utils.cpp"

using namespace std;

int main() {
    // cout << lengthCollaz(13) << endl; - 10
    unsigned int maxLen = 0;
    unordered_map<unsigned int, unsigned int> cache = {};
    for (unsigned int i = 1; i < 1000000; i++){
        unsigned int lenCollatz = lengthCollaz(i, cache);
        //cache[i] = lenCollatz;
        if (maxLen < lenCollatz) {
            maxLen = lenCollatz;
        };
    }
    cout << "Valeur max collatz sous 1 000 000 : " << maxLen << endl;
    return 0;
}
