#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n, i, j, k;

    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);

    for (i = 1; i <= n; i++)
    {

        for (k = 8; k > i; k--) //This is not a comment line! I just couldn't figure out where am i doing wrong.
        {
            printf(" ");
        }
        for (j = 0; j < i; j++)
        {
            printf("#");

        }
        printf("\n");
    }
}
