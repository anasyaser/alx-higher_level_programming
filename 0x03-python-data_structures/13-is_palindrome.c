#include "lists.h"

/**
 * linked_list_length - get length of linked list
 * @head: pointer to head of linked list
 * Return: (int) length of linked list\
 */

int linked_list_length(listint_t *head)
{
	unsigned int cnt = 0;

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
		head = head->next;

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
	listint_t *begin = *head;
	listint_t *last;

	if (length == 1 || length == 0)
		return (1);
	while (middle)
	{
		last = get_nth_node(*head, length - 1);
		if (begin->n != last->n)
			return (0);
		begin = begin->next;
		length--;
		middle--;
	}
	return (1);
}
