#include "lists.h"
/**
 * is_palindrome - checks if the linked list is a palindrome
 *
 * @head: Double pointer to the beginning of the linked list
 *
 * Return - 0 if not palindrome, 1 if palindrome
 **/
int is_palindrome(listint_t **head)
{	
	listint_t *temp = *head;
	int count, temp;
	int *arr;
	if ((*head)->next == NULL)
		return (1);
	for (count = 0; temp; temp = temp->next, count++)
		printf("Element: %d\n", temp->n);
	arr = malloc(sizeof(int) * count);
	temp = count;
	//for (count = 0; count < temp)
	printf("count: %d\n", count);
	return (0);
}
