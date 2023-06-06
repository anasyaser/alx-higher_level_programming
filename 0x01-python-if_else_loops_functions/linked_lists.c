#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n; /* number of nodes */

	current = h;
	n = 0;
	while (current != NULL)
	{
		printf("%i\n", current->n);
		current = current->next;
		n++;

	}

	return (n);

}

/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
			current = current->next;
		current->next = new;

	}

	return (new);

}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);

	}

}

/**
 * insert_node - insert node in sorted linked list
 * @head: pointer to head of linked list
 * @number: value of new node
 * Return: address of new node if success else null
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *cur = *head;
	listint_t *prev = cur;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	if (*head == NULL)
	{
		*head = new_node;
		new_node->next = NULL;
	}
	else
	{
		while (prev != NULL)
		{
			if (cur == NULL || number < cur->n)
			{
				new_node->next = cur;
				if(prev != NULL)
				{
					prev->next = new_node;
					break;
				}
			}
			prev = cur;
			cur = cur->next;
		}
	}
	return (new_node);
}
