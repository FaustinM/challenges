// HBM/CTB november 2022
// Using exceptions
// Lab8 program to complete

/**
 * Part 1
 * Exercice 1
 * 1. True
 * 2. True
 * 3. True
 * 4. False
 * 5. False
 * 6. True
 * 7. True
 * 
 * Exercice 2
 * i = 4 and d = 2
 * 
 * Exercice 3
 * Hello 15 Ibrahim 23
 * Bye 15 Celeste 10
 * Hi 15 15 Dong
 * 
 * Erreur du compilateur
*/


#include <iostream>
#include <string>
#include <stdexcept>
using namespace std;

float operation(char op, float a, float b);

int main() {
  char op; // requested operation
  float a,b;
  float res;
  a=5,b=2; // here we put different values for tests

  op = '*'; //-- testing multiplication
  cout << a << op << b << endl;
  res =  operation(op,a,b);
  cout <<"resultat " << a << op << b <<"="<<res << endl;

  op = '+';  //-- testing addition
  cout << a << op << b << endl;
  res =  operation(op,a,b);
  cout <<"resultat " << a << op << b <<"="<<res << endl;

  op = '-';  //-- testing soustraction
  cout << a << op << b << endl;
  res =  operation(op,a,b);
  cout <<"resultat " << a << op << b <<"="<<res << endl;

  op = '/';  //-- testing division
  cout << a << op << b << endl;
  res =  operation(op,a,b);
  cout <<"resultat " << a << op << b <<"="<<res << endl;

  b = 0;
  try {
    res = operation(op, a, b);
    cout << "resultat " << a << op << b << " = " << res << endl;
  } catch (string e) {
    cerr << e << endl;
  }
  return 0;
}


float operation(char op, float a, float b)  {
  float res;
  switch(op){
  case '/':
    if (b == 0) throw("division impossible");
    res = a/b;
    break;
  case '+':
    res = a+b;
    break;
  case '*':
    res = a*b;
    break;
  case '-':
    res = a-b;
    break;
  default:
    throw("operation unknown");
  }
  return res;
}
