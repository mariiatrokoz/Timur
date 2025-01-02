#include <unistd.h>
#include <stdio.h>


#define BUFFER_SIZE 128

int	main()
{
	FILE *file = NULL;
	char buffer[128];
	
	file = fopen("hello.txt", "r");

	if (file == NULL)
	{
		printf("Error reading file");
		return (1);
	}

	int new_line_counter = 0;
	
	while (fgets(buffer, BUFFER_SIZE, file) != NULL) {
		
		int i = 0;

		while (buffer[i] != '\0') {
			
			if (buffer[i] == '\n')
			{
				new_line_counter++;
			}
			i++;
		}
	}
	
	printf("Total line count: %d\n", new_line_counter);
	
	fclose(file); 
}
