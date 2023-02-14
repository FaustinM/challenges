#include <iostream>
#include <string>
#include "math_utils.cpp"

using namespace std;

int main() {
    int nbDividor = 0;
    int maxDivisor = 0;
    int i = 0;
    // TODO : Optimiser la gestion des diviseurs en sachant que si k divise n alors les diviseurs de k divise n
    while (nbDividor < 5){
        int nb = genTriangularNumber(i);
        vector<long long> divisors = listDivisors(nb);
        nbDividor = divisors.size();
        if (maxDivisor < nbDividor) maxDivisor = nbDividor;
        cout << i << " et " << maxDivisor << endl;
        i++;
    }
    cout << "Gen : " << i << " => " << genTriangularNumber(12375) << endl;
    return 0;
}
