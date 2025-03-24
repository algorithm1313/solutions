#include <bits/stdc++.h>

using namespace std;

int solution(string s) {
  int answer = atoi(s.c_str());

  return answer;
}

// atoi 'ASCII to integer'의 약자로 const char*를 int로 변환
// s.c_str()는 string s를 const char*로 변환
//
// atoi(s.c_str())는 int로 변환 가능하면 정수를 반환하고 변환 불가능하면 0 반환
// 추가로 stoi(s)도 가능
// 음수의 경우 알아서 변환해준다