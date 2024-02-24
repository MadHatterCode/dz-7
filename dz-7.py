example_list = [0, 1, 0, 12, 3]
# example_list = [1, 0, 13, 0, 0, 0, 5]
# example_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]


for i, num in enumerate(example_list):
    if num == 0:
        el = example_list.pop(i)
        example_list.append(el)
print(example_list)

# i = 0
# for j in range(len(example_list)):
#     if example_list[j] != 0:
#         example_list[i], example_list[j] = example_list[j], example_list[i]
#         i += 1
# print(example_list)
