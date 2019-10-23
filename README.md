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
        Sliding Window: <br/> The Sliding Window pattern is used to perform a required operation on a specific window size of a given array or linked list
        <br/><br/>
        <ul>
            <li> Maximum subarray of size 'K' (easy) </li>
            <li> Longest substring with ‘K’ distinct characters (medium) </li>
            <li> String anagrams (hard) </li>
        </ul> 
        <br/><br/>
    </li>
    <li>
        Two pointers or Iterators: <br/> Two Pointers is a pattern where two pointers iterate through the data structure in tandem until one or both of the pointers hit a certain condition
        <br/><br/>
        <ul>
            <li> Squaring a sorted array (easy) </li>
            <li> Triplets that sum to zero (medium) </li>
            <li> Comparing strings that contain backspace (medium) </li>
        </ul>
        <br/><br/>
    </li>
    <li>
        Fast and Slow pointers: <br/> The Fast and Slow pointer approach, also known as the Hare & Tortoise algorithm, is a pointer algorithm that uses two pointers which move through the array (or sequence/linked list) at different speeds. This approach is quite useful when dealing with cyclic linked lists or arrays.
        <br/><br/>
        <ul>
            <li> Linked list cycle (easy) </li>
            <li> Palindrome linked list (medium) </li>
            <li> Cycle in circular array (hard) </li>
        </ul>
        <br/><br/>
    </li>
    <li>
        Merge Interval: <br/> The Merge Intervals pattern is an efficient technique to deal with overlapping intervals. The pattern works like this: Given two intervals (‘a’ and ‘b’), there will be six different ways the two intervals can relate to each other.
        <br/><br/>
        <ul>
            <li> Intervals Intersection (medium) </li>
            <li> Maximum CPU load (hard) </li>
        </ul>
        <br/><br/>
    </li>
    <li>
        Cyclic sort: <br/> This pattern describes an interesting approach to deal with problems involving arrays containing numbers in a given range. The Cyclic Sort pattern iterates over the array one number at a time, and if the current number you are iterating is not at the correct index, you swap it with the number at its correct index
        <br/><br/>
        <ul>
            <li> Find the Missing Number (easy) </li>
            <li> Find the Smallest Missing Positive Number (medium) </li>
        </ul>
        <br/><br/>
    </li>
</ol>