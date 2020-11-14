#include <stdio.h>
#include <math.h>

int main (void)
{
    int b = 3;
    int c = 4;
    int h = 5;

    int a = (h + b + c) /3;

    b = round(a);
    h = round(a);
    c = round(a);
    printf("%i%i%i", b,h,c);
}