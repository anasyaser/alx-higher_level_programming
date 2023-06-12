#include <listobject.h>
#include <object.h>
#include <stdio.h>
#include <stdlib.h>
#include <python.h>


void print_python_list_info(PyObject *p)
{
	printf("[*] size of the Python List = %d\n", sizeof(p));

}
