int maxProfit(int* prices, int pricesSize) 
{
    int max = 0, min_price = prices[0], diff = 0;

    for ( int i = 0; i < pricesSize; i++)
    {
        if (prices[i]< min_price)
        {
            min_price = prices[i];
        }

        diff = prices[i] - min_price;

        if (diff > max)
        {
            max = diff;
        }
    } 
    return max;
}
