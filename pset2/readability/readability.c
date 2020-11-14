#include <stdio.h>
#include <math.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    //string input = get_string("Text: ");
    //string input = "There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.";
    string input = get_string("Text: ");

    int numberofletters, numberofwords, numberofsentences;
    numberofletters = 0;
    numberofwords = 0;
    numberofsentences =0;

    for(int i=0 ; i < strlen(input) ; i++)
    {
        if (isalpha(input[i]))

            numberofletters++;

        if (input[i] == ' ')

            numberofwords++;

        if ((input[i] == '.') || (input[i] == '!') || (input[i] == '?'))

            numberofsentences++;


    //printf("i is=%i  nol=%i\n",i ,numberofletters);
    //YARIN BURAYA DIKKATprintf("i is=%i  nol=%i\n",i ,numberofwords + 1);
    //printf("i is=%i  nol=%i\n",i ,numberofsentences);
    }
    numberofwords = numberofwords + 1;
    float L = (numberofletters / (float) numberofwords) * 100;
    float S = (numberofsentences / (float) numberofwords) * 100;
    int final = round(0.0588 * L - 0.296 * S - 15.8);
    //printf("%i", final);
    if (final < 1)
        printf("Before Grade 1\n");
    else if (final >= 16)
        printf("Grade 16+\n");
    else
        printf("Grade %i\n", final);



}

