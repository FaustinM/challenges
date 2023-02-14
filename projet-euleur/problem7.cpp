// g++ ./problem7.cpp -o problem7 && ./problem7

#include <iostream>
#include "math_utils.cpp"

using namespace std;

int main() {
    int count = 2;
    int currentNumber = 3;
    while (count < 10001) {
        currentNumber = currentNumber + 2;
        if (isPrimeNumber(currentNumber)) {
            count++;
        }
    }
    cout << "La solution est " << currentNumber;
    return 0;
}