#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    float cash;
    int a, b, c, d, e, f, g, h;
    do
    {
        cash = get_float("Change owed: ");
    }
    while (cash <= 0);

    int cent = cash * 100;

    if (true)
    {
        a = cent / 25;
        b = cent % 25;

        c = b / 10;
        d = b % 10;

        e = d / 5;
        f = d % 5;

        g = f / 1;
        h = f % 1;

    }
    int pennies = a + c + e + g;

    printf("%i\n", pennies);






}