# Problem Set 4A
# Name: Alberto Bolanos
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    permutations_list = []
    if len(sequence) == 1:
        permutations_list.append(sequence)
    else:
        permutations_list.extend(get_permutations(sequence[1:]))
        permutations_list *= len(sequence)
        for item in range(len(permutations_list.copy())):
            permutations_list[item] = permutations_list[item][:item] + sequence[0] + permutations_list[item][item:]
    return permutations_list

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    test_input1 = 'a'
    print("Input:", test_input1)
    print("Expected Output:", ['a'])
    print("Actual Output:", get_permutations(test_input1))

    test_input2 = 'ab'
    print("Input:", test_input2)
    print("Expected Output:", ['ab', 'ba'])
    print("Actual Output:", get_permutations(test_input2))

    test_input3 = 'abc'
    print("Input:", test_input3)
    print("Expected Output:", ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print("Actual Output:", get_permutations(test_input3))

