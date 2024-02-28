

#include <iostream>

int main() {
    int count = 0;
    do {
        std::cout << "The count is " << count << std::endl;
        count++;
    } while (count < 5);

    std::cout << "Finished counting." << std::endl;
    return 0;
}
