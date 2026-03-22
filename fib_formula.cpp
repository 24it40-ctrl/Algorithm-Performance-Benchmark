#include <iostream>
#include <cmath>
#include <chrono>

using namespace std;
using namespace std::chrono;

int main() {
    int n;
    cout << "Enter n (Formula): ";
    cin >> n;

    auto start = high_resolution_clock::now();

    // Binet's Formula logic
    double root5 = sqrt(5);
    double phi = (1 + root5) / 2;
    long long result = round(pow(phi, n) / root5);

    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<nanoseconds>(stop - start);

    cout << "Formula Result: " << result << endl;
    cout << "Time: " << duration.count() << " ns" << endl;
    return 0;
}