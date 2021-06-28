### Hashtables

Implement hash tables with hash, add, get, and contains functions.

### Approach and Efficiency

With a target key this has an O(1) time and space complexity.


### API

add() - This function's signature takes in two arguments (key, value) and has returns nothing. The purpose is to add a new key value pair to a hashtable by first calling a hash function on the key and then create a new instance of a Linked List if there is nothing at that index. If there is an existing item at that index then the key value pair will be appened to the linked list

get() - This function's signature is to take in one argument (key) and return the value associated with that key. It calls the hash function and then looks for the value at that key index. If none exists None is returned. If there is an existing linked list the function will traverse until it locates the appropriate key/value. If none exists None will be returned.

contains() This function's siganture is one argument(key) and returns True or False depensing if the hashable contans the passed in argument or now. 

hash() This function's siganture is one argument(key) and the return is a generated index number.
