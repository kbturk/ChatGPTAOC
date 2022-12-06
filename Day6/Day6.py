#part 1
def find_start_of_packet_marker(data):
  # Initialize a queue of length 4 to hold the last four characters received
  queue = []
  
  # Loop through the characters in the data
  for i, c in enumerate(data):
    # Add the current character to the queue
    queue.append(c)
    
    # If the queue has more than 4 elements, remove the first element
    if len(queue) > 4:
      queue.pop(0)
      
    # If the queue has 4 elements and all of them are different, return the
    # index of the current character plus 1 (to account for 0-based indexing)
    if len(queue) == 4 and len(set(queue)) == 4:
      return i + 1
      
  # If no start-of-packet marker was found, return -1
  return -1

  
# Test the function with the examples from the problem statement
data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
print(find_start_of_packet_marker(data))  # should print 7

data = "bvwbjplbgvbhsrlpgdmjqwftvncz"
print(find_start_of_packet_marker(data))  # should print 5

data = "nppdvjthqldpwncqszvftbrmjlhg"
print(find_start_of_packet_marker(data))  # should print 6

data = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
print(find_start_of_packet_marker(data))  # should print 10

data = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
print(find_start_of_packet_marker(data))  # should print 11

#part 2
def find_start_of_message_marker(data):
  # Initialize a queue of length 14 to hold the last 14 characters received
  queue = []
  
  # Loop through the characters in the data
  for i, c in enumerate(data):
    # Add the current character to the queue
    queue.append(c)
    
    # If the queue has more than 14 elements, remove the first element
    if len(queue) > 14:
      queue.pop(0)
      
    # If the queue has 14 elements and all of them are different, return the
    # index of the current character plus 1 (to account for 0-based indexing)
    if len(queue) == 14 and len(set(queue)) == 14:
      return i + 1
      
  # If no start-of-message marker was found, return -1
  return -1
  
# Test the function with the examples from the problem statement
data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
print(find_start_of_message_marker(data))  # should print 19

data = "bvwbjplbgvbhsrlpgdmjqwftvncz"
print(find_start_of_message_marker(data))  # should print 23

data = "nppdvjthqldpwncqszvftbrmjlhg"
print(find_start_of_message_marker(data))  # should print 23

data = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
print(find_start_of_message_marker(data))  # should print 29

data = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
print(find_start_of_message_marker(data))  # should print 26
