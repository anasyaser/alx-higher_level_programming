#include "lists.h"

/**
 * linked_list_length - get length of linked list
 *
 * @head: pointer to head of linked list
 * Return: (int) length of linked list
 */

int linked_list_length(listint_t *head)
{
	int cnt = 0;

	while (head)
	{
		head = head->next;
		cnt++;
	}
	return (cnt);

}

/**
 * get_nth_node - get nth node of linked list
 *
 * @head: pointer to head of linked list
 * @nth: required lenght (starting from 0 and assuming valid number)
 * Return: pointer to required node
 */

listint_t *get_nth_node(listint_t *head, int nth)
{
	while (nth--)
	{
		head = head->next;
	}

	return (head);
}


/**
 * is_palindrome - check if linked list is palindrome
 *
 * @head: pointer to head of linked list
 * Return: (int) 1 if it is palindrome else 0
 */

int is_palindrome(listint_t **head)
{
	int length = linked_list_length(*head);
	int middle = length / 2;
	listint_t *current = *head;
	int i = 0;
	int *node_values;

	if (length == 1 || length == 0)
		return (1);

	node_values = malloc(sizeof(int) * middle);
	if (node_values == NULL)
	{
		printf("hello\n");
		return (0);
	}


	while (current)
	{
		if (middle)
		{
			node_values[middle - 1] = current->n;
			middle--;
		} else if (node_values[i] != current->n)
		{
			free(node_values);
			return (0);
		} else
		{
			i++;
		}
		current = current->next;
	}
	free(node_values);
	return (1);
}
