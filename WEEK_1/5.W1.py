def rem_dups(input_list):
    return list(set(input_list))

input_list = input("Enter a list of numbers separated by spaces: ").split()
input_list = [int(num) for num in input_list] 

result = rem_dups(input_list)
print(f"Original list: {input_list}")
print(f"List after removing duplicates: {result}")

