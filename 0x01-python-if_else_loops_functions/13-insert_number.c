#include "lists.h"
#include <stdlib.h>
/**
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
	*new = malloc(sizeof(listint_t));

	if (!new)
		return(NULL);
	new->n = number;
	new-next = NULL;
	if (!node || new->n < node->n)
	{
		new->next = node;
		return (*head = new);
	}

