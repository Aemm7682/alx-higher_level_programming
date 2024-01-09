#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * is_palindrome - function to check it is palindrome
 * @head: is the front of first node
 * Return: 1 on 0
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (aux_palind(head, *head));
}
/**
 * aux_palind - function to check it is palindrome
 * @head: head list
 * @end: end list
 * */
int aux_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (aux_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
