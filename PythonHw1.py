str_type = 'string'
int_type = 1212
float_type = 12.5
b_type = bytes(255)
lst_type = ['kotik1', 'kotik2', 'kotik3']
tuple_type = (str_type, int_type, float_type)
set_type = set([1, 2, 3, 4])
fset_type = frozenset([5, 6, 7, 8])
dict_type = {'key1': 12,
             'key2': 'dict',
             'key3': 'type'}
print(type(str_type), str_type)
print(type(int_type), int_type)
print(type(float_type), float_type)
print(type(b_type), b_type)
print(type(tuple_type), tuple_type)
print(type(set_type), set_type)
print(type(fset_type), fset_type)
print(type(dict_type), dict_type)

a = 'absd'
b = 'ferg'
c = str(25)
print(a + b)
print(a, b, c)
print(a + b + c)
