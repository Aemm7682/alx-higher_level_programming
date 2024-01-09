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
	listint_t *end = *head;

	if (head == NULL || *head == NULL)
		return (1);
	if (end == NULL)
		return (1);
	if (is_palindrome(&(end->next)) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
