#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 *
 * @head: head of the linked list
 * @number: number to be added
 *
 * Return: returns address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new;

	current = *head;

	new = malloc(sizeof(listint_t));
	new->n = number;

	if (*head == NULL)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	if (current->n < number)
	{
		while (current->next != NULL && (current->next)->n < number)
			current = current->next;
	}

	new->next = current->next;
	current->next = new;

	return (new);
}
