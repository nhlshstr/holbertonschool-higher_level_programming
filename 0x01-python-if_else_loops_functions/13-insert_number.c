#include "lists.h"
/**
 *
 *
 *
 */
listint_t*insert_node(listint_t **head, int number)
{
		listint_t *tmp = *head;
		listint_t *newnode = malloc(sizeof(listint_t));

		if (newnode == NULL)
		{
				return (NULL);
		}

		if (head == NULL)
		{
				free(newnode);
				return (NULL);
		}

		newnode->n = number;

		if (newnode->n <= tmp->n)
		{
				newnode->next = tmp;
				*head = newnode;
				return (newnode);
		}

		while(tmp->next != NULL)
		{
				if (number <= tmp->next->n)
				{
						newnode->next = tmp->next;
						tmp->next = newnode;
						return (newnode);
				}

				tmp = tmp->next;
		}

		tmp->next = newnode;
		newnode->next = NULL;
		return (newnode);
}
