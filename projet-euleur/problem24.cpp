#include <iostream>
#include <string>
#include <array>
#include "math_utils.cpp"

using namespace std;

vector<string> generateNumbers(string currentNumber = "", size_t len = 10, array<bool, 10> blacklist = { false }){
    vector<string> list;
    if (len != 0){
        for (int x = 0; x < 10; x++){
            if (!blacklist[x]){
                char currentChar = (char)((int)'0' + x);
                array<bool, 10> copyBlacklist = blacklist;
                copyBlacklist[x] = true;
                vector<string> subNumbers = generateNumbers(currentNumber+currentChar, len-1, copyBlacklist);

                for (int y = 0; y < subNumbers.size(); y++){
                    list.push_back(subNumbers[y]);
                }
            }
        };
    } else {
        list.push_back(currentNumber);
    }
    
    return list;
}

int main() {
    vector<string> numbers = generateNumbers();
    vector<long long> parsedNumber;
    cout << "Il y a " << numbers.size() << " nbr" << endl;
    for (size_t i = 0; i < numbers.size(); i++) {
        parsedNumber.push_back(strToInt(numbers[i]));
    }
    cout << "Il y a toujours " << parsedNumber.size() << " nbr" << endl;
    cout << parsedNumber[1000000-1] << endl;

    
    return 0;
}
