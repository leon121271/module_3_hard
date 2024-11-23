data_structure = [[1,2,3],{'a':4, 'b':5},(6,{'cube':7, 'drum':8}),"Hello",((),[{(2, 'Urban', ('Urban2', 35))}])]
def calculate_structure_sum(data_structure):
    total_sum = 0
    def recursive_sum(element):
        nonlocal total_sum
        if isinstance(element, (list, tuple, set)):
            for item in element:
                recursive_sum(item)
        elif isinstance(element, dict):
            for key, value in element.items():
                recursive_sum(key)
                recursive_sum(value)
        elif isinstance(element, str):
            total_sum += len(element)
        elif isinstance(element, (int, float)):
            total_sum += element
    for item in data_structure:
        recursive_sum(item)
    return total_sum
result = calculate_structure_sum(data_structure)
print(result)