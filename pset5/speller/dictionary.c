// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <strings.h>


#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

//declaring word counting variable
int word_count = 0;

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    int n = hash(word);

    for(node *curser = table[n]; curser != NULL; curser = curser->next)
    {
        int a = strcasecmp(curser->word, word);
        if(a == 0)
            return true;
    }
    return false;
}

// Hashes word to a number


unsigned int hash(const char *word)
{
    /* ##################################################################
       ####    !!!!!! THE FOUNDER OF THIS FUNCTION IS DJIB2  !!!!!!. ####
       ##################################################################*/
    unsigned long hash = 5381;
    int c = *word;
    c = tolower(c);

    while (*word != 0)
    {
        hash = ((hash << 5) + hash) + c;
        c = *word++;
        c = tolower(c);

    }
    return hash % N;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    FILE *dict = fopen(dictionary, "r");
    if (dict == NULL)
    {
        return false;
    }

    char temporaryword[LENGTH + 1];
    while(fscanf(dict,"%s\n", temporaryword) != EOF)
    {

        node *temporarynode = malloc(sizeof(node));
        if (temporarynode == NULL){
            return false;
        }
        strcpy(temporarynode -> word, temporaryword);

        int n = hash(temporaryword);
        temporarynode ->next = NULL;
        table[n] = temporarynode;

        word_count++;
    }

    fclose(dict);
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    if(word_count > 0)
        return word_count;
    else
        return 0;

}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{

    for(int i = 0; i < N; i++)
    {
        node *temporary = table[i];

        while(temporary != NULL)
        {
            node * next = temporary->next;
            free(temporary);
            temporary = next;
        }
        table[i] = NULL;
    }

    return true;
}
