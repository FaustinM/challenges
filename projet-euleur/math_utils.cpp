#include<vector>
#include<unordered_map>
#include<cmath>
#include<string>

using namespace std;

bool isPrimeNumber(long long n) {
    if (n == 2 || n == 1) return true;
    for (long long i = 3; i < n; i+=2){
        if (n % i == 0){
            return false;
        }
    }
    return true;
}

long long genTriangularNumber(long long n) {
    return (n*(n+1))/2;
}

unsigned __int128 factoriel(unsigned __int128 n) {
    if(n==2) return 2;
    if(n<=1) return 1;
    return factoriel(n-1)*n;
}

// string bigIntToString(unsigned __uint256 num) {
//     string str;
//     do {
//         int digit = num % 10;
//         str = to_string(digit) + str;
//         num = (num - digit) / 10;
//     } while (num != 0);
//     return str;
// };

long double factoriel_iter(long long n) {
    long double prod = 1;
    long int p10 = 0;
    for (long long int i = n; i > 1; i--){
        long long int toMult = i;
        while (toMult%10==0){
            toMult = toMult/10;
            p10++;
        }
        prod = prod*toMult;
    }
    return prod;
}

vector<long long> listDivisors(long long n){
    vector<long long> divisors = {1};
    for (long long i = 2; i < n; i++) {
        if (n % i == 0) divisors.push_back(i);
    }
    return divisors;
}

long long sumList(vector<long long> n){
    long long s = 0;
    for (int i = 0; i < n.size(); i++) s = s + n[i];
    return s;
}

int quicksort_part(vector<long long> &n, int premier, int dernier, int pivot){
    swap(n[pivot], n[dernier]);
    int j = premier;
    for (int i = premier; i < dernier; i++){
        if (n[i] <= n[dernier]){
            swap(n[i], n[j]);
            j = j + 1;
        }
    }

    swap(n[dernier], n[j]);
    return j;
}

void quicksort(vector<long long> &n, int premier, int dernier){
    if (premier < dernier){
        int pivot = premier;
        pivot = quicksort_part(n, premier, dernier, pivot);
        quicksort(n, premier, pivot-1);
        quicksort(n, pivot+1, dernier);
    }
}

void quicksort(vector<long long> &n) {
    quicksort(n, 0, n.size()-1);
}

int convertCharToInt(char c){
    return c - '0';
}

long long strToInt(string s){
    long long n = 0;
    for(int i = 0; i < s.size(); i++) {
        n = n + (convertCharToInt(s[i])*(pow(10, s.size()-(i+1))));
    }
    return n;
}

double strToDouble(string s){
    double n = 0;
    for(int i = 0; i < s.size(); i++) {
        n = n + (convertCharToInt(s[i])*(pow(10, s.size()-(i+1))));
    }
    return n;
}

unsigned long long sumDigit(double a){
    unsigned long long sum = 0;
    /* while (a > 0){
        cout << a << " et " << sum << endl;
        sum = sum + (int)a%10;
        a = a/10;
        a = trunc(a);
    } */
    string aAsString = to_string(a);
    for (int i = 0; i < aAsString.size()-7; i++) sum = sum + convertCharToInt(aAsString[i]);
    return sum;
}

unsigned int lengthCollaz(unsigned int i, const unordered_map<unsigned int, unsigned int> &cache){
    if (cache.find(i) != cache.end()) return cache.at(i);
    if (i == 1) return 1;
    i = i%2==0 ? i/2 : 3*i+1;
    return 1+lengthCollaz(i, cache);
}

unsigned int lengthCollaz(unsigned int i){
    unordered_map<unsigned int, unsigned int> cache = {};
    return lengthCollaz(i, cache);
}

/*
vector<int> findNPrimeNumber(long long n) {
    vector<bool> isPrimeVectors = vector(n, true)
}*/