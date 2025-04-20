#include <bits/stdc++.h>
using namespace std;

vector<int> solution(int brown, int yellow) {
  vector<int> answer;
  int mx = 0;
  int sum = brown + yellow;

  for (int i = 3; i <= sqrt(sum); i++) {
    if (sum % i == 0 && (i - 2) * (sum / i - 2) == yellow) {
      mx = i;
    }
  }

  answer.push_back(sum / mx);
  answer.push_back(mx);

  return answer;
}