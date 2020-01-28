#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *hare = list;
	listint_t *tort = list;

	do
	{
			if (hare->next == NULL || hare->next->next == NULL)
			{
					return (0);
			}
			
			tort = tort->next;
			hare = hare->next->next;
	}while(hare != tort);

	return (1);
}
