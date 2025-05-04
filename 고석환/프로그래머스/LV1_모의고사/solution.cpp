#include <bits/stdc++.h>
using namespace std;

int check_ans(int arr[], size_t size, vector<int> &ans) {
  int ret = 0;

  for (int i = 0; i < ans.size(); i++) {
    if (ans[i] == arr[i % size]) {
      ret++;
    }
  }

  return ret;
}

vector<int> solution(vector<int> answers) {
  vector<int> answer;

  int mx = 0;
  vector<int> v;

  int a[] = {1, 2, 3, 4, 5};
  int b[] = {2, 1, 2, 3, 2, 4, 2, 5};
  int c[] = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

  int ret1 = check_ans(a, sizeof(a) / sizeof(a[0]), answers);
  int ret2 = check_ans(b, sizeof(b) / sizeof(b[0]), answers);
  int ret3 = check_ans(c, sizeof(c) / sizeof(c[0]), answers);

  v.push_back(ret1);
  v.push_back(ret2);
  v.push_back(ret3);

  for (int i = 0; i < 3; i++) {
    mx = max(v[i], mx);
  }

  for (int i = 0; i < 3; i++) {
    if (mx == v[i]) {
      answer.push_back(i + 1);
    }
  }

  return answer;
}