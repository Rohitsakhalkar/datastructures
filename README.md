# Data Structures in Python

   A collection of fundamental data structures implemented from scratch in Python.

   The goal of this project is to understand how common data structures work internally by implementing their core operations, handling edge cases, writing tests, and packaging the implementations as a reusable Python package.

## Implemented Data Structures
- Doubly Linked List
- Singly Linked List
- Stack
- Queue
- Binary Search Tree

## What I Practiced

This project goes beyond simply implementing append(), pop(), or insert().

While building these structures, I practiced:

- Object-oriented programming
- Type hints
- Generic data structures
- Iterators
- Recursion
- Tree traversal
- Searching and deletion
- Edge-case handling
- Exception handling
- Unit testing with pytest
- Python package structure
- Git and GitHub workflow
- Documentation

## Project Structure
```
DataStructure/
│
├── DataStructure/
│   ├── __init__.py
│   │
│   ├── LinkedList/
│   │   ├── __init__.py
│   │   ├── node.py
│   │   └── linked_list.py
│   │
│   ├── DoublyLinkedList/
│   │   ├── __init__.py
│   │   ├── node.py
│   │   └── doubly_linked_list.py
│   │
│   ├── Stack/
│   │   ├── __init__.py
│   │   ├── stack.py
|   |   └── node.py 
│   │
│   ├── Queue/
│   │   ├── __init__.py
│   │   └── queue.py
|   |   └── node.py 
│   │
│   └── BinarySearchTree/
│       ├── __init__.py
│       ├── node.py
│       └── binary_search_tree.py
│
├── tests/
│
├── pyproject.toml
└── README.md
```
The exact structure may change as the project grows.

## Singly Linked List

A linear data structure where each node stores a value and a reference to the next node.

- Core concepts
- Node-based storage
- Sequential traversal
- Insertion and removal
- Searching
- Iteration

## Doubly Linked List

A linked list where each node maintains references to both the next and previous nodes.

- Core concepts
- Forward traversal
- Reverse traversal
- Insertion
- Removal
- Index-based access
- Iterators
- Reversing the list

## Stack

A Last-In, First-Out (LIFO) data structure.
```
Push
 ↓
┌───┐
│ C │ ← Top
├───┤
│ B │
├───┤
│ A │
└───┘
```

### Typical operations:

- push()
- pop()
- peek()
- is_empty()

## Queue

A First-In, First-Out (FIFO) data structure.
```
Front          Rear
  ↓             ↓
┌───┬───┬───┬───┐
│ A │ B │ C │ D │
└───┴───┴───┴───┘
  ↑
Remove

                  ↑
                 Add

```

### Typical operations:

- enqueue()
- dequeue()
- peek()
- is_empty()

## Binary Search Tree

A binary tree where values smaller than a node are placed in the left subtree and larger values are placed in the right subtree.

### Implemented functionality includes:

- Insertion
- Deletion
- Searching
- Minimum value
- Maximum value
- Height
- Tree traversal
- Breadth-first traversal
- Clearing
- Membership testing
- Iteration
- Traversals
- Inorder
- Preorder
- Postorder
- Breadth-first search

For example, inorder traversal of a BST produces values in sorted order.
 
## Complexity

The implementations are intended to provide practical understanding of the time and space trade-offs involved in different data structures.

Some operations depend on the structure's current shape and state.

For example, a balanced BST can provide approximately:

Search     O(log n)
Insert     O(log n)
Delete     O(log n)

while a highly unbalanced BST can degrade to:

Search     O(n)
Insert     O(n)
Delete     O(n)

## Testing

Tests are written using pytest.

Run the test suite with:

python -m pytest

### The tests cover normal operations as well as edge cases such as:

- Empty structures
- Single-element structures
- Invalid indexes
- Removing elements
- Searching for missing values
- Tree deletion cases
- Boundary conditions

## Installation

Clone the repository:

``` bash
git Clone <respository-url>
```
Move into the project:

``` bash
cd datastructures
```

Create a virtual environment:

```bash
python -m venv .venv
```
Activate it.

Windows:
```bash
.venv\Scripts\Activate.ps1
```
Install dependencies

```bash
pip install -r requirements.txt
```

## Running Tests
```bash
python -m pytest tests
```

## Usage

### Example:

from DataStructure import ...

Individual data structures can then be imported and used according to their respective implementations.

See the source code and tests for detailed examples.

## Purpose

This project was created as a hands-on way to learn data structures rather than only studying their theory.

Instead of treating data structures as something to memorize, I wanted to understand:

How would I actually build one?

That meant dealing with references, edge cases, recursion, iteration, errors, testing, and package organization.

## Future Work

More data structures and algorithms will be added as I continue learning.

### Planned additions include:

- Hash Table
- Heap / Priority Queue
- Graph
- Trie
- More algorithms
- Improved documentation
- Performance comparisons

## Technologies

- Python
- pytest
- Git
- GitHub

## Implementations and Source Code

Each data structure has its own module, with separate node and implementation files where applicable.

| Data Structure | Implementation | Tests |
|---|---|---|
| Stack | [stack/stack.py](stack/stack.py) | [test_stack.py](tests/test_stack.py) |
| Queue | [queue/queue.py](queue/queue.py) | [test_queue.py](tests/test_queue.py) |
| Singly Linked List | [singlylinkedlist/singly_linked_list.py](singlylinkedlist/singly_linked_list.py) | [test_singlylinkedlist.py](tests/test_singlylinkedlist.py) |
| Doubly Linked List | [doublylinkedlist/doubly_linked_list.py](doublylinkedlist/doubly_linked_list.py) | [test_doublylinkedlist.py](tests/test_doublylinkedlist.py) |
| Binary Search Tree | [binarysearchtree/binary_search_tree.py](binarysearchtree/binary_search_tree.py) | [test_binarysearchtree.py](tests/test_binarysearchtree.py) |

## Engineering Work

- Implemented five fundamental data structures using Python classes and node-based structures.
- Wrote core operations for insertion, deletion, searching, indexing, and traversal.
- Used recursion to implement Binary Search Tree operations and tree traversals.
- Implemented Python special methods such as `__len__`, `__iter__`, `__contains__`, and `__repr__`.
- Added pytest test suites for the individual implementations.
- Configured project packaging using `pyproject.toml` and setuptools.


## Note

This project is primarily a learning project focused on understanding implementation details and software engineering practices.

It is not intended to replace Python's highly optimized built-in data structures.

## License

This project is  for learning and educational purpose

# Built by Sakhalkar, in search of meaning.
