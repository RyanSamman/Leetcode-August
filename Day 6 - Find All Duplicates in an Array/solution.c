#include <stdio.h>
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findDuplicates(int* nums, int numsSize, int* returnSize){
	// Allocate from 0 to numsSize
	// Integers in 'nums' guranteed to be from 1 <= i <= numsSize
    int *accArr = calloc(numsSize + 1, sizeof(int)); 
    *returnSize = 0;
    
    for (int i = 0; i < numsSize; i++) 
    {
        *(accArr + *(nums + i)) += 1;
        if (*(accArr + *(nums + i)) == 2) 
        {
            *returnSize += 1;
        }
    } 
    
    int *returnArr = calloc(*returnSize , sizeof(int));
    
    for (int i = 0, j = 0; i < numsSize + 1; i++) 
    {
        if (*(accArr + i) == 2) 
        {
            *(returnArr + j) = i;
            j++;
        }
    }
    
    return returnArr;
}