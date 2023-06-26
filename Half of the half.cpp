#include <iostream>
#include <string>
using namespace std;

int main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        string sequence;
        cin >> sequence;
        int k = sequence.length() / 2;
        string first_half = sequence.substr(0, k);

        for (int j = 0; j < k; j += 2) {
            cout << first_half[j];
        }

        cout << endl;
    }

    return 0;
}
