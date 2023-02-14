#include "BigInt.hpp"
#include "math_utils.cpp"

BigInt big_factoriel(long long int n) {
    if(n==2) return 2;
    if(n<=1) return 1;
    return big_factoriel(n-1)*n;
}

long long int big_sumDigit(BigInt a){
    int sum = 0;
    /* while (a > 0){
        cout << a << " et " << sum << endl;
        sum = sum + (int)a%10;
        a = a/10;
        a = trunc(a);
    } */
    string aAsString = a.to_string();
    for (int i = 0; i < aAsString.size()-7; i++) sum = sum + convertCharToInt(aAsString[i]);
    return sum;
}