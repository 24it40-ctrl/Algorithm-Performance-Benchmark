
#include <iostream>
#include <string>
#include <chrono>
using namespace std;
using namespace std::chrono;

int main() {
    string n; cout << "Enter: "; cin >> n;
for (char c: n) {
if(!isdigit(c)){
cout<<"Invalid Input !"<<endl;
return 0;
}
}
    auto start = high_resolution_clock::now();
    long long s = 0;
    for (char c : n) s += (c - '0');
    int res = (s == 0) ? 0 : 1 + (s - 1) % 9;
    auto end = high_resolution_clock::now();
    cout << "Res: " << res << " | Time: " << duration_cast<nanoseconds>(end-start).count() /1000000.0 << " ms" << endl;
    return 0;
}
