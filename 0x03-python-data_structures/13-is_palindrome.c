#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
#include <stdio.h>

/**
 * len_list - finds length of list
 *
 * @head: pointer to linked list head
 *
 * Return: length of linked list
 */
int len_list(listint_t **head)
{
	listint_t *copy;
	int len;

	copy = *head;
	len = 0;
	while (copy->next)
	{
		len++;
		copy = copy->next;
	}
	len++;

	return (len);
}


/**
 * is_palindrome - checks whether linked list is a palindrome
 *
 * @head: head of linked list
 *
 * Return: 1 if True 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *copy, *iter_copy;
	int len, i, x, a, b;

	len = len_list(head);
	copy = *head;

	if (*head == NULL)
	{
		return (1);
	}

	i = 0;
	while (i < len)
	{
		x = 0;
		iter_copy = copy;
		a = copy->n;
		while (x < len - 2 * i - 1)
		{
			iter_copy = iter_copy->next;
			x++;
		}

		b = iter_copy->n;
		if (a != b)
			return (0);

		copy = copy->next;
		i++;
	}
	return (1);
}
