#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - A function that runs an infinite while loop.
 *
 * Return: zero on exit.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}

	return (0);
}

/**
 * main - The function that creates zombie processes.
 * Return: EXIT_SUCCESS on successful execution.
 */

int main(void)
{
	pid_t pid;
	int index = 0;

	while (index < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
			index++;
		}
		else
		{
			exit(0);
		}
	}

	infinite_while();

	return (EXIT_SUCCESS);
}
