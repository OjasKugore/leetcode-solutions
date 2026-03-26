int maxArea(int* height, int heightSize) 
{
    int left = 0, right = heightSize - 1, max_area = 0, curr_area = 0;

    while (left<right)
    {
        if (height[left]<height[right])
        {
            curr_area = height[left] * (right - left);
            left++;
        }
        else
        {
            curr_area = height[right] * (right - left);
            right--;
        }
        if (max_area<curr_area)
        {
            max_area = curr_area;
        }
    }

    return max_area;
}
