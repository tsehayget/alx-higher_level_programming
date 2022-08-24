#include "lists.h"

/**
 * check_cycle - checks if linked list is a circle
 * @list: imports the linked list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list;

	for (; head != NULL; head = head->next)
	{
		for (list = head->next; list != NULL; list = list->next)
		{
			if (list == head)
				return(1);
			;
		}
	}
	return (0);
}
