#include <iostream>
#include <string>
#include <cmath>
#include "math_utils.cpp"

using namespace std;

int main() {
    for (int a = 3; a < 1000; a++)
        for (int b = a; b < 1000; b++) {
            float c = sqrt(a*a+b*b);
            if (a+b+c == 1000) {
                cout << "Solution : " << a*b*c << endl;
                return 0;
            }
        }
}
