# Algo
## Algorithm practice

It’s important for any engineer, even the senior ones, to brush up on their coding skills and algorithms. **Data structures and algorithms** are the bread and butter of software engineering.  Following are the topics that you should definitely master.

<ol> 
    <li>
        <strong>Trees:</strong> 
        <br/>This is most basic stuff 
        <br/><br/>
        <ul> 
            <li> Tree construction, conversion, traversal and manipulation algorithms </li>
            <li> Binary trees, BST and Trie question </li>
            <li> n-ary tree and one balanced version AVL or Red black tree </li>
            <li> Recursive vs Iterative approaches </li>
            <li> Serialization and Deserialization of trees </li>
            <li> Finding LCA (Least Common Ancestor) </li>
        </ul>
        <br/>
    </li>
    <li>
        <strong>Graphs:</strong>
        <br/><br/>
        <ul>
            <li> Relationships = Graphs. Graphs are most fundamental and flexible way of representing a relationship.</li>
            <li> Consider if a problem can be visualized and solved as a graph algorithm - distance, search, connectivity, cycle detection, etc </li>
            <li> Adjacency list vs Matrix </li>
            <li> Graph traversal algorithm - BFS and DFS. Computational complexity, tradeoffs and implementation </li>
            <li> Dijkstra and Prim </li>
            <li> Topologial sorting and cycle detection. alien dictionary problem </li>
            <li> Try and use STL(built in data structure) </li>
        </ul>
        <br/>
    </li>
    <li>
        <strong>Hash Table:</strong>
        <br/>This is most commonly used data structure and algorithm question.
        <br/><br/>
        <ul>
            <li> Reducing time complexity by using more space </li>
            <li> Time complexity insertion, deletion O(1) </li>
            <li> LRU Cache </li>
            <li> Hash Table vs BST which to choose and when </li>
            <li> Examples: Pair with sum 'K' & subarray with sum 0 </li>
        </ul>
        <br/>
    </li>
    <li>
        <strong>Arrays and Strings:</strong>
        <br/><br/>
        <ul>
            <li> array rotation, rearrangement and optimization problems </li>
            <li> palindrome, anagrams and parentheses </li>
            <li> subsequence and subarray problem </li>
            <li> Problems - 
                <ol>
                    <li> Minimum window substring </li>
                    <li> Maximum sum subarray </li>
                    <li> kth largest element </li>
                    <li> maximum subsequence sum such that no three are consecutive </li>
                </ol>
            </li>
        </ul>
        <br/>
    </li>
    <li>
        <strong>Recursion and Backtracking:</strong>
        <br/><br/>
        <ul>
            <li> Use recursion to find more elegant solutions to problems that can be solved iteratively </li>
            <li> examples word break and boggle </li>
        </ul>
        <br/>
    </li>
    <li>
        <strong>Memoization and greediness:</strong>
        <br/><br/>
        <ul>
            <li> practice dynamic programming especially tabulation</li>
            <li> LCS, LIS, Min cost path, 0-1 Knapsack, Palindrome partitioning</li>
            <li> Greedy algorithm - activity selection, maximize difference in circular array, k booking, fractional knapsack</li>
        </ul>
        <br/>
    </li>
    <li>
        <strong>Big-O Notation:</strong>
        <br/>This is absolutely a must- time and space complexity is asked almost in all interview question. How to optimize code for better time/space complexity.
        <br/><br/>
        <ul>
            <li> While practising, also perform analysis and add the time and space complexities of the written code</li>
            <li> Generally, to improve the speed of a program, we can choose to either use an appropriate data structure or algorithm, or to use more memory. It’s a classic space and time trade off. </li>
        </ul>
        <br/>
    </li>
    <li>
        <strong>Searching and sorting:</strong>
        <br/><br/>
        <ul>
            <li> Binary search. if array sorted then log(n) time complexity </li>
            <li> Merge sort vs Quick sort - Merge interval popular problem</li>
            <li> Merge sort is useful when combining lists without wasting memory/disk space</li>
            <li> Divide and conquer - median of two sorted arrays </li>
            <li> Be familiar with the common sorting functions and on what kind of input data they’re efficient on or not. Think about efficiency means in terms of runtime and space used. For example, in exceptional cases insertion sort or radix sort are much better than the generic QuickSort / MergeSort / HeapSort answers </li>
        </ul>
        <br/>
    </li>
    <li>
        <strong>Linked List:</strong>
        <br/><br/>
        <ul>
            <li> loop detection, cloning, flattening, union, intersection and basic manipulation</li>
            <li> circular and doubly linked list</li>
        </ul>
        <br/>
    </li>
    <li>
        <strong>Stacks and Queues:</strong>
        <br/><br/>
        <ul>
            <li> Implement stacks and queues using both arrays and linked list</li>
            <li> Queues using stacks, stacks using queues, k stacks in an array </li>
            <li> Popular stack problems - stock span, celebrity problem, balanced parenthesis, NGE, histogram problem</li>
        </ul>
        <br/>
    </li>
    <li>
        <strong>Heap:</strong>
        <br/>Use a heap anytime you want to keep track of a “top” or “min” in a list
        <br/><br/>
        <ul>
            <li> Understand priority queue</li>
            <li> Median of a stream of integers </li>
        </ul>
        <br/>
    </li>
    <li>
        <strong>Others:</strong>
        <br/><br/>
        <ul>
            <li> Famous classes of NP Complete problems - travelling salesman, knapsack</li>
            <li> Discrete math problems and probability </li>
            <li> Stack and heap memory management</li>
            <li> Object oriented design concepts </li>
            <li> OS concepts - process vs threads, concurrency, semaphores, locks, context switching, process scheduling</li>
            <li> bit manipulation</li>
        </ul>
    </li>
</ol>

## Patterns for coding interview and their associated sample questions 
<ol>
    <li> 
        <strong>Sliding Window:</strong> <br/> The Sliding Window pattern is used to perform a required operation on a specific window size of a given array or linked list
        <br/><br/>
        <ul>
            <li> Maximum subarray of size 'K' (easy) </li>
            <li> Longest substring with ‘K’ distinct characters (medium) </li>
            <li> String anagrams (hard) </li>
        </ul> 
        <br/><br/>
    </li>
    <li>
        <strong>Two pointers or Iterators:</strong> <br/> Two Pointers is a pattern where two pointers iterate through the data structure in tandem until one or both of the pointers hit a certain condition
        <br/><br/>
        <ul>
            <li> Squaring a sorted array (easy) </li>
            <li> Triplets that sum to zero (medium) </li>
            <li> Comparing strings that contain backspace (medium) </li>
        </ul>
        <br/><br/>
    </li>
    <li>
        <strong>Fast and Slow pointers:</strong> <br/> The Fast and Slow pointer approach, also known as the Hare & Tortoise algorithm, is a pointer algorithm that uses two pointers which move through the array (or sequence/linked list) at different speeds. This approach is quite useful when dealing with cyclic linked lists or arrays.
        <br/><br/>
        <ul>
            <li> Linked list cycle (easy) </li>
            <li> Palindrome linked list (medium) </li>
            <li> Cycle in circular array (hard) </li>
        </ul>
        <br/><br/>
    </li>
    <li>
        <strong>Merge Interval:</strong> <br/> The Merge Intervals pattern is an efficient technique to deal with overlapping intervals. The pattern works like this: Given two intervals (‘a’ and ‘b’), there will be six different ways the two intervals can relate to each other.
        <br/><br/>
        <ul>
            <li> Intervals Intersection (medium) </li>
            <li> Maximum CPU load (hard) </li>
        </ul>
        <br/><br/>
    </li>
    <li>
        <strong>Cyclic sort:</strong> <br/> This pattern describes an interesting approach to deal with problems involving arrays containing numbers in a given range. The Cyclic Sort pattern iterates over the array one number at a time, and if the current number you are iterating is not at the correct index, you swap it with the number at its correct index
        <br/><br/>
        <ul>
            <li> Find the Missing Number (easy) </li>
            <li> Find the Smallest Missing Positive Number (medium) </li>
        </ul>
        <br/><br/>
    </li>
    <li>
        <strong>In place reversal of linked list:</strong> <br/> This pattern reverses one node at a time starting with one variable (current) pointing to the head of the linked list, and one variable (previous) will point to the previous node that you have processed. In a lock-step manner, you will reverse the current node by pointing it to the previous before moving on to the next node. Also, you will update the variable “previous” to always point to the previous node that you have processed.
        <br/><br/>
        <ul>
            <li> Reverse a sub-list (medium) </li>
            <li> Reverse every k element sublist (medium) </li>
        </ul>
        <br/><br/>
    </li>
    <li>
        <strong>Tree BFS:</strong> <br/> The Tree BFS pattern works by pushing the root node to the queue and then continually iterating until the queue is empty. For each iteration, we remove the node at the head of the queue and “visit” that node. After removing each node from the queue, we also insert all of its children into the queue.
        <br/><br/>
        <ul>
            <li> Binary Tree level order traversal (easy) </li>
            <li> Zigzag traversal (medium) </li>
        </ul>
        <br/><br/>
    </li>
    <li>
        <strong>Tree DFS:</strong> <br/> The Tree DFS pattern works by starting at the root of the tree, if the node is not a leaf you need to do three things:
        <ol>
            <li> Decide whether to process the current node now (pre-order), or between processing two children (in-order) or after processing both children (post-order).</li>
            <li> Make two recursive calls for both the children of the current node to process them.</li>
        </ol>
        <br/>
        <ul>
            <li> Binary Tree level order traversal (easy) </li>
            <li> Zigzag traversal (medium) </li>
        </ul>
        <br/><br/>
    </li>
    <li>
        <strong>Two Heaps:</strong> <br/> This pattern uses two heaps; A Min Heap to find the smallest element and a Max Heap to find the biggest element. The pattern works by storing the first half of numbers in a Max Heap, this is because you want to find the largest number in the first half. You then store the second half of numbers in a Min Heap, as you want to find the smallest number in the second half. At any time, the median of the current list of numbers can be calculated from the top element of the two heaps.
        <br/><br/>
        <ul>
            <li> Find median of a number stream (medium) </li>
        </ul>
        <br/><br/>
    </li>
    <li>
        <strong>Subsets:</strong> <br/> The pattern looks like this: <br/>Given a set of [1, 5, 3]<br/>
        <ol> 
            <li> Start with an empty set: [[]] </li>
            <li> Add the first number (1) to all the existing subsets to create new subsets: [[], [1]]; </li>
            <li> Add the second number (5) to all the existing subsets: [[], [1], [5], [1,5]];</li>
            <li> Add the third number (3) to all the existing subsets: [[], [1], [5], [1,5], [3], [1,3], [5,3], [1,5,3]].</li>
        </ol>
        <br/>
        <ul>
            <li> Subsets with duplicates (easy) </li>
            <li> String permutation by changing case (medium) </li>
        </ul>
        <br/><br/>
    </li>
    <li>
        <strong>Modified binary search:</strong> <br/> This pattern describes an efficient way to handle all problems involving Binary Search.
        <br/>The patterns looks like this for an ascending order set:
        <ol>
            <li> First, find the middle of start and end. An easy way to find the middle would be: middle = (start + end) / 2. But this has a good chance of producing an integer overflow so it’s recommended that you represent the middle as: middle = start + (end — start) / 2 </li>
            <li> If the key is equal to the number at index middle then return middle </li>
            <li> If ‘key’ isn’t equal to the index middle:
                <ul>
                    <li> Check if key < arr[middle]. If it is reduce your search to end = middle — 1 </li>
                    <li> Check if key > arr[middle]. If it is reduce your search to start = middle + 1 </li>
                </ul>
            </li>
        </ol>
        <br/>
        <ul>
            <li> Order agnostic Binary Search (easy) </li>
            <li> Search in a sorted infinite array (medium) </li>
        </ul>
        <br/><br/>
    </li>
    <li>
        <strong>Top K Elements:</strong> <br/> The best data structure to keep track of ‘K’ elements is Heap. This pattern will make use of the Heap to solve multiple problems dealing with ‘K’ elements at a time from a set of given elements. The pattern looks like this:
        <ol>
            <li> Insert ‘K’ elements into the min-heap or max-heap based on the problem.</li>
            <li> Iterate through the remaining numbers and if you find one that is larger than what you have in the heap, then remove that number and insert the larger one. </li>
        </ol>
        <br/>
        <ul>
            <li> Top 'K' numbers (easy) </li>
            <li> Top 'K' frequent numbers (medium) </li>
        </ul>
        <br/><br/>
    </li>
    <li>
        <strong>K-way merge:</strong> <br/> The pattern looks like this:
        <ol>
            <li> Insert the first element of each array in a Min Heap.</li>
            <li> After this, take out the smallest (top) element from the heap and add it to the merged list.</li>
            <li> After removing the smallest element from the heap, insert the next element of the same list into the heap.</li>
            <li> Repeat steps 2 and 3 to populate the merged list in sorted order.
        </ol>
        <br/>
        <ul>
            <li> Merge K Sorted Lists (medium) </li>
            <li> K Pairs with large sums (hard) </li>
        </ul>
        <br/><br/>
    </li>
    <li>
        <strong>Topological sort:</strong> <br/> Topological Sort is used to find a linear ordering of elements that have dependencies on each other. For example, if event ‘B’ is dependent on event ‘A’, ‘A’ comes before ‘B’ in topological ordering.
        <br/><br/>
        <ul>
            <li> Task scheduling (medium) </li>
            <li> Minimum height of a tree </li>
        </ul>
        <br/><br/>
    </li>
</ol>