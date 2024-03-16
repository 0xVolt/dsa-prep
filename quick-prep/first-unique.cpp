#include <bits/stdc++.h>
using namespace std;


int getUnique(string input) {
    unordered_map<char, int> hashMap;

    for (char ch: input) {
        hashMap[ch]++;
    }

    char first;

    for (auto &pair: hashMap) {
        if (pair.second == 1) {
            first = pair.first;
        }
    }

    int index = input.find(first);

    if (index == string::npos) {
        return -1;
    } else {
        return index + 1;
    }
}


int main() {
    string input = "statistics";

    cout << getUnique(input);

    return 0;
}