#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>

#define CHUNK 512

int main(int argc,char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }

    FILE *card = fopen(argv[1],"r");

    if (card == NULL)
    {
        printf("Be sure to select correct file\n");
        return 1;
    }

    int image_count = 0;
    FILE *outputimg = NULL;
    bool jpgfound = false;
    typedef uint8_t BYTE;
    BYTE array[CHUNK];
    char file[8];

    while (fread(array,sizeof(array),1,card) == 1)
    {

        if(array[0] == 0xff && array[1] == 0xd8 && array[2] == 0xff && (array[3] & 0xf0) == 0xe0)
        {
            if (jpgfound == false)
            {
                sprintf(file, "%03i.jpg", image_count);
                image_count++;
                outputimg = fopen(file,"w");
                fwrite(array,sizeof(array),1,outputimg);
                jpgfound = true;

            }
            else if(jpgfound == true)
            {
                fclose(outputimg);
                sprintf(file, "%03i.jpg", image_count);
                image_count++;
                outputimg = fopen(file,"w");
                fwrite(array,sizeof(array),1,outputimg);
            }
        }
        else if(jpgfound == true)
        {
            fwrite(array,sizeof(array),1,outputimg);
        }

    }

    fclose(outputimg);
    fclose(card);
    return 0;

}
