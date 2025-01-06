
#include <stdio.h>





int	main()
{

	int prices[3] = {32, 33, 99};
	
	int length = sizeof(prices) / sizeof(int);
	for(int i = 0; i < length; i++)
	{
		int price = prices[i];

		printf("index: %d, value: %d\n", i, price);
	}



}
