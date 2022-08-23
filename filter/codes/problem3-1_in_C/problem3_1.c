#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    int k = 20;
    double x[] = {1.0, 2.0, 3.0, 4.0, 2.0, 1.0};
    double y[k];
    for (int i=0; i<k; i++){
        y[i] = 0;
    } 
    y[0] = x[0];
    y[1] = -0.5 * y[0] + x[1];
    for (int n=0; n<k-1; n++)
    {
        if (n < 6){
            y[n] = -0.5 * y[n - 1] + x[n] + x[n - 2];
        }
        else if (n > 5 && n < 8){
            y[n] = -0.5 * y[n - 1] + x[n - 2];
        }
        else{
            y[n] = -0.5 * y[n - 1];
        }
    }

    for (int i=0; i<k; i++)
    {
        printf("%lf ", y[i]);
    }

    FILE *fptr;

    fptr = fopen("arr_x.txt","w");   
    
    if(fptr == NULL)
    {
      printf("Error!");   
      exit(1);             
    }
    for (int i=0; i<k; i++)
    {
        fprintf(fptr, "%lf ", y[i]);
    }

    return 0;
}
