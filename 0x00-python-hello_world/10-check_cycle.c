#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * check_cycle - check if one cycle done
 * @list: pointer to check list
 * Return: 1 if one cycle and 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list, *slow = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
