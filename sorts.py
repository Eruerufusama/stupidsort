# Oppgave 1
# What does this list..:
# [1900, 100, 900, 700, 300, 1000, 1300, 1500, 800, 1200]
# ...look like after 3 passes of Bubble Sort? 
#
# One pass:
# [100, 900, 700, 300, 1000, 1300, 1500, 800, 1200, 1900]
#
# Two passes:
# [100, 700, 300, 900, 1000, 1300, 800, 1200, 1500, 1900]
#
# Three passes:
# [100, 300, 700, 900, 1000, 800, 1200, 1300, 1500, 1900]
#
# Answer: B

# Oppgave 2
# Answer: C     O(n log n)

# Oppgave 3
from random import choice, randint
import asyncio


def main():
    unsorted_array = [
        ("James Bond", 131.2),
        ("Lord of the Rings", 91.5),
        ("Harry Potter", 148.0),
        ("The Dark Knight Rises", 112.9),
        ("Space Jam", 87.1)
        ]

    sort_and_print(unsorted_array, sleepsort, 1)

def sort_and_print(unsorted, sorting_algorithm, index=None):
    sorted_array = master_sort(unsorted, sorting_algorithm, index)

    title, budget = sorted_array[-1]
    print(f"The movie with the largest budget is '{title}', which had a budget of {budget} million dollars.")

# Helper functions below.
def master_sort(unsorted, sorting_algorithm, index=None):
    """Sorts an array of elements. If every element is itself an iterable, it can use a specified index to sort by.
    
    Arguments:
        unsorted {iterable} -- An unsorted array.
    
    Keyword Arguments:
        index {int} -- Index for every element in array (default: {None})
        sort_algorithm {function} -- Selects which sorting-algorithm to use when sorting. (default: {sleepsort})
    
    Raises:
        MissingSortingIndexError: Index was expected, but was not provided.
        IndexOutOfBoundsError: Index provided was out of bounds for the elements in the unsorted array.
    
    Returns:
        list -- A sorted version of the list.
    """
    # Validates whether or not the elements in the array are iterables.
    if hasattr(unsorted[0], "__iter__") and type(unsorted[0]) is not str:
        # Runs if elements were iterables, yet no index was provided.
        if index == None:
            raise MissingSortingIndexError("Each element in the array was an iterable, but no index was provided.")
        # Runs if index was out of bounds of the element-iterable.
        elif index > len(unsorted[0]):
            raise IndexOutOfBoundsError(f"length of each element was {len(unsorted[0])}, but the provided index as {index}.")

        else:
            # To restore elements to their respective datatype later.
            datatype = type(unsorted[0])
            
            # Re-creates the list with 'ArrayElements' instead of tuples/lists/etc.
            unsorted = [ArrayElement(element, index) for element in unsorted]

    sorted_list = sorting_algorithm(unsorted)

    # Re-creates the list with tuples instead of 'ArrayElements'.
    return [datatype(element.array) for element in sorted_list]

def slowsort(array, i=0, j=None): 
    """Sorts a list in ascending order based on the principles of 'multiply and surrender'.
        Average big O: O(Ω(n(log(n)/(2+n))))
    
    Arguments:
        li {list} -- Must be a mutable array, forcing nonfunctional programming - The new paradigm within programming where nothing is immutable.
        i {int} -- The first index to be sorted.
        j {int} -- The last index to be sorted.
    
    Returns:
        list -- Sorted list in ascending order.
    """
    if j is None:
        j = len(array)-1
    if i >= j:
        return array

    ij = int((i+j) / 2)
    
    slowsort(array, i, ij)
    slowsort(array, ij+1, j)

    if array[j] < array[ij]:
        array[j], array[ij] = array[ij], array[j]
    
    return slowsort(array, i, j-1)

def bogosort(unsorted):
    """A sorting algorithm for lucky people. Scramples the array randomly until it is.
        Best case O:    O(1)
        Average case O: O((n+1)!)
        Worst case O:   O(∞)
    
    Arguments:
        unsorted {iter} -- An unsorted array.
    
    Returns:
        list -- Returns a sorted list. Maybe. The worst case on this algorithm is actually infinite, so it may well never finish.
    """
    while True:
        array = unsorted.copy()
        # Create new randomly sorted array.
        perhaps_sorted = []
        while len(array) > 0:
            i = randint(0, len(array)-1)
            perhaps_sorted.append(array[i])
            array.pop(i)
        
        # Check if it's sorted.
        for i, current_element in enumerate(perhaps_sorted):
            if i > 0:
                if previous_element > current_element:
                    break
            previous_element = current_element
            if i == len(perhaps_sorted)-1:
                return perhaps_sorted

def recursive_bogosort(unsorted):
    """
    A sorting algorithm for lucky people.
    Sorts a list in ascending order, using the undisputed best-case champion of the sorting-field: Bogosort, implimented recursively.
    Takes an unsorted array, randomizes it, checks if it's sorted. If it isn't, repeats the process until it is.

    Best case big O:    O(1)
    Average case big O: O((n+1)!)
    Worst case big O:   O(∞)
    
    Arguments:
        li {list} -- an unsorted list.
    
    Returns:
        list -- Either a sorted list in ascending order, or an unsorted list.
    """
    new_list = []
    try:
        while len(unsorted) > 0:
            i = randint(0, len(unsorted)-1)
            new_list.append(unsorted[i])
            unsorted.pop(i)
        for i, current_element in enumerate(new_list):
            if i == 0:
                previous_element = current_element
            else:
                if previous_element > current_element:
                    return recursive_bogosort(new_list)
                previous_element = current_element

        return new_list
    except RecursionError:
        print("Unfortunately, the sorting was unsuccessful. Returning current state of list:")
        return unsorted

# TO BE IMPLIMENTED



    


# TO BE IMPLIMENTED
def bayessort(unsorted):
    """Impliments a naive bayes classifier that is trained to sort lists.
        Big O: No idea...
    
    Arguments:
        li {list} -- Unsorted list.
    """
    pass #TODO

def sleepsort(unsorted, speed=0.00000000001):
    """Sorts an unsorted array <A> by asynchronously appending <e> after sleeping for <e> * speed seconds.
        Big O: Good question...

    Arguments:
        unsorted {iterable} -- An iterable of int/float
    
    Keyword Arguments:
        speed {float} -- Selects performance of algorithm. Lower = Faster, but too low values makes it unreliable. (default: {1.0})
    
    Returns:
        [list] -- Sorted list.
    """
    async def sleep_coroutine(value, destination, speed):
        await asyncio.sleep(value * speed)
        destination.append(value)

    coroutines = set()
    sorted_list = []
    for element in unsorted:
        coroutines.add(sleep_coroutine(element, sorted_list, speed))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(coroutines))
    return sorted_list

class ArrayElement:
    def __init__(self, array, i):
        self.array = array
        self.value = self.array[i]

    # Equal
    def __eq__(self, other):
        return self.value == other

    # Greater than
    def __gt__(self, other):
        return self.value > other

    # Less than
    def __lt__(self, other):
        return self.value < other

    # Not equal
    def __ne__(self, other):
        return self.value != other

    # Less than
    def __le__(self, other):
        return self.value <= other

    # Greater than
    def __ge__(self, other):
        return self.value >= other
    
    # Multiply
    def __mul__(self, other):
        return self.value * other

class MissingSortingIndexError(Exception):
    pass
class IndexOutOfBoundsError(Exception):
    pass

if __name__ == "__main__":
    main()