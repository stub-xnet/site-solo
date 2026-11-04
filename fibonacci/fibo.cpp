
#include <iostream>
using namespace std;

int Fibo(int n)
{
    if (n == 1 || n == 2)
        return 1;
    return Fibo(n - 1) + Fibo(n - 2);
}

int main()
{
    int number;
    cin >> number;
    cout << Fibo(number) << endl;
    return 0;
}
