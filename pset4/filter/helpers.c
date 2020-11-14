#include "helpers.h"
#include "math.h"
#include "stdlib.h"
#include "stdio.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    //accessing all the pixels
    for (int i = 0 ; i < height ; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // taking the average of r,g,b
            float averagecolor = ((float) image[i][j].rgbtRed + (float) image[i][j].rgbtGreen + (float) image[i][j].rgbtBlue) / 3;
            //printf("%f,%f",averagecolor, round(averagecolor));
            //changing with new values
            image[i][j].rgbtRed = round(averagecolor);
            image[i][j].rgbtGreen = round(averagecolor);
            image[i][j].rgbtBlue = round(averagecolor);

        }

    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    //usual accesing all the pixels
    for (int i = 0 ; i < height ; i++)
    {
        for (int j = 0 ; j < width ; j++)
        {
            // sapia effect
            float sapiared = (((float) image[i][j].rgbtRed * 393 / 1000) + ((float) image[i][j].rgbtGreen * 769 / 1000) +
                              ((float) image[i][j].rgbtBlue * 189 / 1000));
            float sapiagreen = (((float) image[i][j].rgbtRed * 349 / 1000) + ((float) image[i][j].rgbtGreen * 686 /1000) +
                                ((float) image[i][j].rgbtBlue * 168 / 1000));
            float sapiablue = (((float) image[i][j].rgbtRed * 272 / 1000) + ((float) image[i][j].rgbtGreen * 534 / 1000) +
                               ((float) image[i][j].rgbtBlue * 131 / 1000));
            // These if's for preventing not the exceed unsigned chars byte limit
            if (sapiared > 255)
            {
                image[i][j].rgbtRed = 255;
            }

            else
            {
                image[i][j].rgbtRed = round(sapiared);
            }

            if (sapiagreen > 255)
            {
                image[i][j].rgbtGreen = 255;
            }

            else
            {
                image[i][j].rgbtGreen = round(sapiagreen);
            }

            if (sapiablue > 255)
            {
                image[i][j].rgbtBlue = 255;
            }

            else
            {
                image[i][j].rgbtBlue = round(sapiablue);
            }
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE emptyglass[height][width];

    for (int i = 0 ; i < height ; i++)
    {
        for (int j = 0; j < width; j++)
        {
            emptyglass[i][j].rgbtRed = image[i][width - 1 - j].rgbtRed;
            emptyglass[i][j].rgbtGreen = image[i][width - 1 - j].rgbtGreen;
            emptyglass[i][j].rgbtBlue = image[i][width - 1 - j].rgbtBlue;

            //image[i][j].rgbtRed = image[i][width - 1].rgbtRed;
            //image[i][j].rgbtGreen = image[i][width - 1].rgbtGreen;
            //image[i][j].rgbtBlue = image[i][width - 1].rgbtBlue;



        }
        for (int j = 0; j < width ; j++)
        {
            image[i][j].rgbtRed = emptyglass[i][j].rgbtRed;
            image[i][j].rgbtGreen = emptyglass[i][j].rgbtGreen;
            image[i][j].rgbtBlue = emptyglass[i][j].rgbtBlue;
        }
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 1; i < height - 1 ; i++)
    {
        for (int j = 1 ; j < width - 1 ; j++)
        {
            if (i < 1 || j < 1 || i + 1 == width || j + 1 == height)
            {
                continue;
            }
            float a = ((float)image[i][j].rgbtRed +
                       (float) image[i][j + 1].rgbtRed +
                       (float) image[i][j - 1].rgbtRed +
                       (float) image[i + 1][j].rgbtRed +
                       (float) image[i - 1][j].rgbtRed +
                       (float) image[i - 1][j - 1].rgbtRed +
                       (float) image[i + 1][j + 1].rgbtRed +
                       (float) image[i - 1][j + 1].rgbtRed +
                       (float) image[i + 1][j - 1].rgbtRed) / 9;

            float b = ((float) image[i][j].rgbtBlue +
                       (float) image[i][j + 1].rgbtBlue +
                       (float) image[i][j - 1].rgbtBlue +
                       (float) image[i + 1][j].rgbtBlue +
                       (float) image[i - 1][j].rgbtBlue +
                       (float) image[i - 1][j - 1].rgbtBlue +
                       (float) image[i + 1][j + 1].rgbtBlue +
                       (float) image[i - 1][j + 1].rgbtBlue +
                       (float) image[i + 1][j - 1].rgbtBlue) / 9;

            float c = ((float) image[i][j].rgbtGreen +
                       (float) image[i][j + 1].rgbtGreen +
                       (float) image[i][j - 1].rgbtGreen +
                       (float) image[i + 1][j].rgbtGreen +
                       (float) image[i - 1][j].rgbtGreen +
                       (float) image[i - 1][j - 1].rgbtGreen +
                       (float) image[i + 1][j + 1].rgbtGreen +
                       (float) image[i - 1][j + 1].rgbtGreen +
                       (float) image[i + 1][j - 1].rgbtGreen) / 9;

            image[i][j].rgbtRed = round(a);
            image[i][j].rgbtBlue = round(b);
            image[i][j].rgbtGreen = round(c);
        }
    }
    return;
}
