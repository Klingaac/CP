### 3.py

#include <iostream>

#int main() {
    #unsigned long long 
prev = 0; curr = 1; next;
    #std::cin >> 
n = int(input());

if (n <= 1):
    curr = n;
else:
    for i in range(n-1):# (int i = 2; i <= n; ++i) {
            next = prev + curr;
            prev = curr;
            curr = next;
        

#std::cout << 
print(curr)# << '\n';
    #return 0;
