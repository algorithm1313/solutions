#include <bits/stdc++.h>
using namespace std;

int ret;
string s, delimeter;

int main() {
  getline(cin, s);
  getline(cin, delimeter);

  auto start = 0;
  auto end = s.find(delimeter);

  while (end != string::npos) {
    ret++;
    start = end + delimeter.size();
    end = s.find(delimeter, start);
  }

  cout << ret;
  return 0;
}