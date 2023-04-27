# Modify merge sort algorithm
def merge_sort(items):
    n = len(items)
    temporary_storage = [None] * n
    size_of_subsections = 1

    while size_of_subsections < n:
        for i in range(0, n, size_of_subsections * 2):
            i1_start, i1_end = i, min(i + size_of_subsections, n)
            i2_start, i2_end = i1_end, min(i1_end + size_of_subsections, n)
            sections = (i1_start, i1_end), (i2_start, i2_end)
            merge(items, sections, temporary_storage, key=len)
        size_of_subsections *= 2

    print(items)


def merge(items, sections, temporary_storage, key):
    (start_1, end_1), (start_2, end_2) = sections
    i_1 = start_1
    i_2 = start_2
    i_t = 0

    while i_1 < end_1 or i_2 < end_2:
        if i_1 < end_1 and i_2 < end_2:
            if key(items[i_1]) > key(items[i_2]):
                temporary_storage[i_t] = items[i_1]
                i_1 += 1

            else:  # the_list[i_2] >= items[i_1]
                temporary_storage[i_t] = items[i_2]
                i_2 += 1
            i_t += 1

        elif i_1 > end_1:
            for i in range(i_1, end_1):
                temporary_storage[i_t] = items[i_1]
                i_1 += 1
                i_t += 1

        else:  # i_2 < end_2
            for i in range(i_2, end_2):
                temporary_storage[i_t] = items[i_2]
                i_2 += 1
                i_t += 1

    for i in range(i_t):
        items[start_1 + i] = temporary_storage[i]


# Create three string lists
fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango",
          "nectarine", "orange"]
countries = ["Afghanistan", "Brazil", "Canada", "Denmark", "Estonia", "Finland", "Greece", "Honduras", "Iceland",
             "Jamaica", "Kenya", "Lebanon", "Mauritius", "Nepal", "Oman", "Pakistan", "Qatar", "Russia", "Sweden",
             "Tanzania"]
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "gray", "black", "white"]

merge_sort(fruits)
print(fruits)
print("\n")
merge_sort(countries)
print(countries)
print("\n")
merge_sort(colors)
print(colors)
