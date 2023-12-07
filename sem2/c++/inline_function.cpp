#include <iostream>

using namespace std;

// define an inline function to calculate the square of a number
inline int square(int x) {
    return x * x;
}

int main() {
    int num;
    cout << "Enter a number: ";
    cin >> num;

    // call the inline function
    int result = square(num);
    cout << "The square of " << num << " is " << result << endl;

    return 0;
}
