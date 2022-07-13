# lexicographically dictioanry sort

my_string = ["Hello", "this", "is", "example", "how", "to", "sort", "strings"]


def sort_string(my_string):
	return sorted(sorted(my_string), key=str.upper)

print(sort_string(my_string))

def lexicographi_sort(s):
    return sorted(sorted(s), key=str.upper)

print(lexicographi_sort(my_string))