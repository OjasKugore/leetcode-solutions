int maxSubArray(int* nums, int numsSize) 
{
    int runningsum = 0, max = nums[0];
    for (int i = 0; i < numsSize; i++)
    {
        runningsum += nums[i];
        if (runningsum > max)
        {
            max = runningsum;
        }
        
        if (runningsum < 0)
        {
            runningsum = 0;
        }
        
    }
    return max;
}
