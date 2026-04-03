/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* rearrangeArray(int* nums, int numsSize, int* returnSize) 
{
    int* array = (int*)malloc(numsSize * sizeof(int));

    int even = 0, odd = 1;
//in even idices(0,2,4 there are pos)
    for ( int i = 0; i < numsSize; i++)
    {
        if (nums[i] > 0)
        {
            array[even] = nums[i];
            even+=2;
        }
        else
        {
            array[odd] = nums[i];
            odd+=2;
        }
    }
    *returnSize = numsSize;
    return array;
}
