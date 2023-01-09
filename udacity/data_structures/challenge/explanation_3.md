huffman_encoding:
I have used a dictionary to hold the frequency of each character.
As changing a using a dict is a O(1) operation, the performance is great.
Also, used the queue.PriorityQueue class for the requested priority queue from build-in Python libs. It uses a min-heap under the hoods,
then it's very fast to add new elements (O(Log N)).
The whole function has Linear (O(N)) time complexity, as it grows as bigger is the data to encode.

huffman_decoding:
Used a list to hold the data and recursive function to decode.
Function is O(Log N)

