#include <iostream>
#include <string>
#include "math_utils.cpp"

using namespace std;

int getCurrentDay(int month, int year){
    if (month == 1)
        if (year%400==0 || (year%4==0 && year%100!=0))
            return 29;
        else
            return 28;
    if (month == 7)
        return 31;
    if (month % 2 == 0)
        return 31;
    else
        return 30;
}

int main() {
    /*
        Lundi : 0
        Mardi : 1
        Mercredi : 2
        Jeudi : 3
        Vendredi : 4
        Samedi : 5
        Dimanche : 6
    */
    unsigned int nbJours = 0;
    unsigned int day = 1;
    for (int y = 1901; y < 2001; y++)
        for (int m = 0; m < 12; m++){
            if (day % 7 == 6)
                nbJours++;
            day = day + getCurrentDay(m, y);
        }
    cout << nbJours << endl;
    return 0;
}