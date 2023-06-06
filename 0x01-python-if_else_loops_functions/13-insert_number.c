#include "lists.h"

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
