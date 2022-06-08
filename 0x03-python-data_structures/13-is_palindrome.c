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
	int len, *list, i;

	listint_t *copy;

	if (*head == NULL)
	{
		return (1);
	}

	copy = *head;
	len = len_list(head);

	list = malloc(len * sizeof(int));
	copy = *head;
	i = 0;
	while (copy->next)
	{
		list[i] = copy->n;
		copy = copy->next;
		i++;
	}
	list[i] = copy->n;

	i = 0;
	while (i < len)
	{
		if (list[i] != list[len - i - 1])
		{
			free(list);
			return (0);
		}
		i++;
	}
	free(list);
	return (1);
}
