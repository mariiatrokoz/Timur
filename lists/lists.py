#source: https://www.w3resource.com/python-exercises/list-advanced/index.php 

#1. + Write a Python function to reverse a list at a specific location.

def reverse_list(list):

    reversed_list = list[::-1]

    return reversed_list


#2. +- Write a Python function to find the length of the longest (increasing) sub-sequence in a list.

def find_length(list):

    longest_sub_seq = list[0]
    for subsequence in list:
        if longest_sub_seq < subsequence:
            longest_sub_seq = subsequence

    return len(longest_sub_seq)


#3. Write a Python function that finds all the permutations of the members of a list.

def find_all_permutations(list):

    ###

    return number_of_permutations


#4.+- Write a Python function to find the kth smallest element in a list

def find_smallest_element(list):

    smallest_element = list[0]

    for current_element in list:

        if smallest_element > current_element:
            smallest_element = current_element

    return smallest_element


#5. + Write a Python function to find the kth largest element in a list.

def find_largest_element(list):

    largest_element = list[0]

    for current_element in list:

        if current_element > largest_element:
            largest_element = current_element

    return largest_element


#6. Write a Python function to check if a list is a palindrome or not. Return true otherwise false.

#7. Write a Python a function to find the union and intersection of two lists.

#8. Write a Python function to remove duplicates from a list while preserving the order.

#9. Write a Python a function to find the maximum sum sub-sequence in a list. Return the maximum value.

#10. Write a Python a function to find the minimum sum sub-sequence in a list. Return the sub-sequence.

#11. Write a Python function to find the longest common sub-sequence in two lists.

#12. Write a Python program to find the first non-repeated element in a list.

#13. Write a Python a function to implement a LRU cache.

#Discards the least recently used items first. This algorithm requires keeping track of what was used when, which is expensive if one wants to make sure the algorithm always discards the least recently used item. General implementations of this technique require keeping "age bits" for cache-lines and track the "Least Recently Used" cache-line based on age-bits. In such an implementation, every time a cache-line is used, the age of all other cache-lines changes. LRU is actually a family of caching algorithms with members including 2Q by Theodore Johnson and Dennis Shasha, and LRU/K by Pat O'Neil, Betty O'Neil and Gerhard Weikum.

#14. Write a Python function to sort a list of dictionaries based on values of a key.

#15. Write a Python program to find all the pairs in a list whose sum is equal to a given value.

my_list = [5,98,4,34,5,76,78,4]

#print(reverse_list(my_list))
#print(find_length(my_list))
#print(find_all_permutations(my_list))
#print(find_smallest_element(my_list))
print(find_largest_element(my_list))
