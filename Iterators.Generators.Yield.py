nested_list = [
['a', 'b', 'c'],
['d', 'e', 'f', 'h', False],
[1, 2, None],
]

# Итератор

class FlatIterator:
    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.cursor = -1
        self.nest_cursor = 0
        self.list_len = len(self.nested_list)

    def __iter__(self):
        self.cursor += 1
        self.nest_cursor = 0
        return self

    def __next__(self):
        while self.cursor - self.list_len and self.nest_cursor == len(self.nested_list[self.cursor]):
          iter(self)
        if self.cursor == self.list_len:
          raise StopIteration
        self.nest_cursor += 1
        return self.nested_list[self.cursor][self.nest_cursor - 1]

for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)
print('----')


# Генератор

def flat_generator(nested_list):
    for values in nested_list:
        for value in values:
            yield value

list_values = list(flat_generator(nested_list))
print(list_values)
