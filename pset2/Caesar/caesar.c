#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <stdlib.h>


int main(int argc, string argv[])
{

    if (argc == 2)
    {
        //printf("Success!\n");
        //printf("%s\n", argv[1]);
        //printf("\n");

        int key = atoi(argv[1]);
        //printf ("%i", key);


        string word = get_string("plaintext: ");
        //printf("word is :%s\n", word);
        int len = strlen(word);
        //printf("length is:%i\n", len);

        printf("ciphertext: ");
        for(int i = 0 ; i < len ; i++)
        {
            if (islower(word[i]))
                printf("%c", (word[i] - 'a' + key) % 26 + 'a');
            else if (isupper(word[i]))
                printf("%c", (word[i] - 'A' + key) % 26 + 'A');
            else
                printf("%c", word[i]);

            /* ASCII TABLE ATTEMP
            if ((int) word[i] < 78 && (int) word[i] > 64 )
            {
            //-
                printf("%c", (int) word[i] - key);
            }
            if ((int) word[i] > 77 && (int) word[i] < 91 )
            {
                printf("%c", (int) word[i] + key);
            }
            if ((int) word[i] < 110 && (int) word[i] > 96 )
            {
                printf("%c", (int) word[i] + key);
            }
            if ((int) word[i] > 109 && (int) word[i] < 123 )
            {
                //-
                printf("%c", (int) word[i] - key);
            }
            if (word[i] == '.' || word[i] == '?' || word[i] == '!' || word[i] == ',' || word[i] == ' ')
            {
             printf("%c", word[i]);
            }*/

        }
        printf("\n");
    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

}