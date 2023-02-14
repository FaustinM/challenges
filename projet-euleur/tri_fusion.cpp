#include <iostream>
#include <string>
#include "math_utils.cpp"

using namespace std;

/*
entrée : un tableau T
sortie : une permutation triée de T
fonction triFusion(T[1, …, n])
      si n ≤ 1
              renvoyer T
      sinon
              renvoyer fusion(triFusion(T[1, …, n/2]), triFusion(T[n/2 + 1, …, n]))

entrée : deux tableaux triés A et B
sortie : un tableau trié qui contient exactement les éléments des tableaux A et B
fonction fusion(A[1, …, a], B[1, …, b])
      si A est le tableau vide
              renvoyer B
      si B est le tableau vide
              renvoyer A
      si A[1] ≤ B[1]
              renvoyer A[1] + fusion(A[2, …, a], B)
      sinon
              renvoyer B[1] + fusion(A, B[2, …, b])

*/

void print_v(const vector<int> &a){
    for (int i = 0; i < a.size(); i++){
        cout << a[i] << " ";
    }
    cout << endl;
}

vector<int> push_head(const vector<int>& a, int v){
    vector<int> r;
    r.push_back(v);
    for (size_t i = 0; i < a.size(); i++)
        r.push_back(a[i]);
    return r;
}

vector<int> remove_f(const vector<int>& a){
    vector<int> r;
    for (size_t i = 1; i < a.size(); i++)
        r.push_back(a[i]);
    return r;
}

vector<int> fusion(vector<int> a, vector<int> b){
    if (a.size() == 0)
        return b;
    if (b.size() == 0)
        return a;
    if (a[0] <= b[0]) {
        return push_head(fusion(remove_f(a), b), a[0]);
    }
    else {
        return push_head(fusion(remove_f(b), a), b[0]);
    }
}

vector<int> triFusion(vector<int> t){
    if (t.size() <= 1) return t;
    else {
        vector<int> fHalf;
        for (size_t i = 0; i <= (t.size()-1)/2; i++)
            fHalf.push_back(t[i]);
        
        vector<int> sHalf;
        for (size_t i = (t.size()/2); i < t.size(); i++)
            sHalf.push_back(t[i]);

        vector<int> triFHalf = triFusion(fHalf);
        vector<int> triSHalf = triFusion(sHalf);
        return fusion(triFHalf, triSHalf);
    }
}

int main() {
    vector<int> v = {6, 1, 2, 5, 4, 7, 3};

    //print_v(fusion({7}, {3}));

    vector<int> sortedV = triFusion(v);
    print_v(sortedV);
    return 0;
}
