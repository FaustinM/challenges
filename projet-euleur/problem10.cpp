// Crible d'Erathostène - https://fr.wikipedia.org/wiki/Crible_d%27%C3%89ratosth%C3%A8ne

#include <iostream>
#include <string>
#include "math_utils.cpp"

using namespace std;

int main() {
    int count = 2;
    int currentNumber = 3;
    long long sum = 5;
    while (currentNumber+1 < 2000000) {
        currentNumber = currentNumber + 2;
        if (isPrimeNumber(currentNumber)) {         
            sum = sum + currentNumber;
        }
    }
    cout << "La solution est " << sum;
    return 0;
}
