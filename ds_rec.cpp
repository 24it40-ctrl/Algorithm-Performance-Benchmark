#include <iostream>
#include <string>
#include <chrono>
using namespace std;
using namespace std::chrono;

int solve(string n) {
    if (n.length() == 1) return n[0] - '0';
    long long sum = 0;
    for (char c : n) 
 sum += (c - '0');
    return solve(to_string(sum));
}
int main() {
    string n; cout << "Enter: "; cin >> n;
for (char c : n) {
if(!isdigit(c)) {
cout<<"Invalid input !"<<endl;
return 0;
}
}
    auto start = high_resolution_clock::now();
    int res = solve(n);
    auto end = high_resolution_clock::now();
    cout << "Res: " << res << " | Time: " << duration_cast<nanoseconds>(end-start).count() /1000000.0 << " ms" << endl;
    return 0;
}
