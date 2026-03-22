#include <iostream>
#include <chrono>
#include <vector>

using namespace std;
using namespace std::chrono;

int main() {
    int n;
    cout << "Enter n for Series: ";
    cin >> n;

    auto start = high_resolution_clock::now();

    unsigned long long a = 0, b = 1;
    cout << "Series: ";
    for (int i = 0; i <= n; i++) {
        cout << a << " ";
        unsigned long long next = a + b;
        a = b;
        b = next;
    }

    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<nanoseconds>(stop - start);

    cout << "\nExecution Speed: " << duration.count() << " ns" << endl;
    return 0;
}