#include <iostream>
#include <chrono>

using namespace std;
using namespace std::chrono;

// सर, यह फंक्शन रिकर्शन का इस्तेमाल करता है
long long fibRecursive(int n) {
    if (n <= 1) return n;
    return fibRecursive(n - 1) + fibRecursive(n - 2);
}

int main() {
    int n;
    cout << "Enter n: ";
    if (!(cin >> n) || n < 0) {
        cout << "Invalid Input!" << endl;
        return 1;
    }

    auto start = high_resolution_clock::now();
    long long result = fibRecursive(n);
    auto stop = high_resolution_clock::now();

    auto duration = duration_cast<nanoseconds>(stop - start);

    cout << "Result: " << result << endl;
    cout << "Time Taken: " << duration.count() << " ns" << endl;
    return 0;
}