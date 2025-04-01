#include <string>
#include <vector>

using namespace std;

int solution(int n) {
  int answer = 0;

  for (int i = 1; i <= n; i++) {
    if (!(n % i)) answer += i;
  }

  return answer;
} 

// n이 최대 3000이므로 1~n 까지 반복문 돌려서 단순 비교
