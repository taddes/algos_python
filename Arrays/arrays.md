# Arrays
* Excellent for structures that require addition or removal of items at the end of a given array. Still efficient, but less so for shift based additions or removals at existing indexes.

## Methods
* **add()**
  * O(1) / constant time complexity - Operation if adding to end of array

* **insert(item, index) / unshift(item, index)**
  * O(n) / linear complexity - If every item has to be shifted for the value to be inserted

* **pop()**
  * O(1) / constant time complexity - Fast operation if item at end of array.

* **remove(index)**
  * O(n) / linear complexity - If remove one item, you have to shift other items to fill removed item.