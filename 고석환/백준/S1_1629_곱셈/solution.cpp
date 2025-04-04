#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll A, B, C;

// ll go(ll a, ll b) {
//   if (b <= 1) return a % C;

//   ll ret = go(a, b / 2);

//   ret = ret * ret % C;

//   if (b % 2 == 1) {
//     ret = ret * a % C;
//   }

//   return ret;
// }

ll go(ll a, ll b) {
  if (b <= 1) return a % C;

  if (b % 2 == 1) {
    return go(a, b / 2) * go(a, b / 2) % C * a % C;
  }

  return go(a, b / 2) * go(a, b / 2) % C;
}

int main() {
  cin >> A >> B >> C;

  cout << go(A, B);

  return 0;
}