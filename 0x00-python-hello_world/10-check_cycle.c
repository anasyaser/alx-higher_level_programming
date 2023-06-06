#include "lists.h"

/**
 * node_is_exist - check if node in existing arraylist
 *
 * @node: pointer to node to check
 * @nodes_list: array of nodes
 * Return: 1 if node exist else 0
 */

int node_is_exist(listint_t **nodes_list, listint_t *node)
{
	if (node == NULL)
		return (0);
	while (*nodes_list)
	{
		if (*nodes_list == node)
			return (1);
		nodes_list++;
	}
	return (0);
}

/**
 * check_cycle - check if Linked list has inner cycle
 *
 * @list: pointer to head of linked list
 * Return: (int) 0 if no cycle else 1
 */

int check_cycle(listint_t *list)
{

	listint_t **checked_nodes;
	unsigned int i = 0;
	unsigned int arr_size = 10;

	checked_nodes = malloc(arr_size * sizeof(listint_t *));
	if (checked_nodes == NULL)
	{
		printf("Error");
		return (1);
	}

	while (list != NULL)
	{
		checked_nodes[i] = list;
		list = list->next;

		if (node_is_exist(checked_nodes, list))
		{
			free(checked_nodes);
			return (1);
		}

		i++;
		if (i >= arr_size)
		{
			arr_size += 10;
			checked_nodes =	realloc(checked_nodes,
					arr_size * sizeof(listint_t *));
			if (checked_nodes == NULL)
			{
				printf("Error");
				return (1);
			}
		}
	}
	free(checked_nodes);
	return (0);
}
