#include <iostream>
#include <string>
#include "math_utils.cpp"

using namespace std;

vector<string> digits = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
                            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};
vector<string> power_10 = {"twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};

string getDigits(int x) {
    return digits[x-1];
}

string getNumber(int x) {
    if (x < 20) return getDigits(x);
    else {
        return power_10[(x/10)-2] + "-" + getDigits(x%10);
    }
}

string getHundred(int x) {
    string str = getDigits(x/100) + " hundred";
    if(x%100 != 0){
        str = str + " and " + getNumber(x%100);
    }
    return str;
}

size_t countWithoutEspace(string x){
    size_t count = 0;
    for (int i = 0; i < x.size(); i++){
        if (x[i] !='-' && x[i] !=' ') count++;
    }
    return count;
}

int main() {
    size_t count = 0;
    for (int i = 0; i < 1000; i++){
        if (i < 100){
            count = count + countWithoutEspace(getNumber(i));
        } else count = count + countWithoutEspace(getHundred(i));
    }
    count = count + countWithoutEspace("one thousand");
    cout << count << endl;
    return 0;
}
