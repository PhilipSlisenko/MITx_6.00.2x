###########################
# 6.00.2x Problem Set 1: Space Cows 

from pset1.ps1_partition import get_partitions
from collections import namedtuple
#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def cast_to_sorted_list_of_named_tuples(cows):
    Cow = namedtuple('Cow', 'name weight')
    cows = [Cow(*cow) for cow in cows.items()]
    cows_sorted = sorted(cows, key=lambda cow: cow.weight)
    return cows_sorted

def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cows_sorted = cast_to_sorted_list_of_named_tuples(cows)
    def gen_trip(cows_sorted, limit):
        aboarded_weight = 0
        aboarded_cows = list()
        while aboarded_weight < limit and cows_sorted and cows_sorted[0].weight + aboarded_weight <= limit:
            for i, cow in reversed(list(enumerate(cows_sorted))):
                    if cow.weight + aboarded_weight <= limit:
                        cow_to_board = cows_sorted.pop(i)
                        break
            aboarded_weight += cow_to_board.weight
            aboarded_cows.append(cow_to_board.name)
        return aboarded_cows
    trips = list()
    while cows_sorted:
        trips.append(gen_trip(cows_sorted, limit))
    return trips



# Problem 2
def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    for permut_option in get_partitions(cows.items()):
        legit_option = True
        for trip in permut_option:
            trip_weight = 0
            for cow in trip:
                trip_weight += cow[1]
            if trip_weight > limit:
                legit_option = False
                break
        if legit_option:
            return [[cow[0] for cow in trip] for trip in permut_option]
        

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    import time
    start = time.time()
    greedy_cow_transport(
        {'Abby': 38, 'Willow': 35, 'Dottie': 85, 'Daisy': 50, 'Coco': 10, 'Buttercup': 72, 'Betsy': 65, 'Rose': 50,
         'Lilly': 24, 'Patches': 12}, 100)
    end = time.time()
    greedy_time = end - start
    start = time.time()
    brute_force_cow_transport(
        {'Abby': 38, 'Willow': 35, 'Dottie': 85, 'Daisy': 50, 'Coco': 10, 'Buttercup': 72, 'Betsy': 65, 'Rose': 50,
         'Lilly': 24, 'Patches': 12}, 100)
    end = time.time()
    brute_time = end - start
    print("Greedy: {}\nBrute: {}".format(greedy_time, brute_time))


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
print(cows)
#print(cast_to_sorted_list_of_named_tuples(cows))
#print(greedy_cow_transport({'Abby': 38, 'Willow': 35, 'Dottie': 85, 'Daisy': 50, 'Coco': 10, 'Buttercup': 72, 'Betsy': 65, 'Rose': 50, 'Lilly': 24, 'Patches': 12}, 100))
#print(brute_force_cow_transport({'Milkshake': 40, 'Miss Bella': 25, 'MooMoo': 50, 'Lotus': 40, 'Horns': 25, 'Boo': 20}, 100))
compare_cow_transport_algorithms()

