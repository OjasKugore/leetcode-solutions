int findMaxConsecutiveOnes(int* nums, int numsSize) 
{
    int counter = 0, max = 0;
    for (int i = 0; i < numsSize; i++)
    {
        if (nums[i] == 1)
        {
            counter++;
        }
        else
        {
            counter = 0;
        }

        if (counter > max)
        {
            max = counter;
        }
    }
    return max;
}
