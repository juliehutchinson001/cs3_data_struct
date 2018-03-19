# Understanding Binary Search Trees

<center><table>
    <tr>
        <td><center>Binary Search Trees</center></td>
    </tr>
    <tr>
        <td>Inserting new item: O(logN)</td>
    </tr>
    <tr>
        <td>Searching an item: O(logN)</td>
    </tr>
    <tr>
        <td>Removing an item: O(logN)</td>
    </tr>
</table></center>

The weight that time complexity entails is closely related with the  importance to create a data structure at compile time, that is going to verify every operation of a compiled code. A clear example involves comparing two common structures such as:

<center><table>
    <tr>
        <td><center>Sorted Arrays</center></td>
        <td><center>Linked Lists</center></td>
    </tr>
    <tr>
        <td>Insert new item: O(N)</td>
        <td>Insert new item: O(1)</td>
    </tr>
    <tr>
        <td>Search w binary search: O(logN)</td>
        <td>Search is sequential: O(N)</td>
    </tr>
    <tr>
        <td>Remove an item: O(N)</td>
        <td>Remove item by reference: O(1)</td>
    </tr>
</table></center>

Let's take a look about Facebook webpage, there are some users who are only going to search for other users, or they can also be curious about their friend's pictures; and other users, like me for example that enjoy mostly uploading pictures to share in facebook profile.

The previous examples are a few of the many actions possible in a webpage, where a data structure such as binary search tree, with predictable running time, can speed up the loading of the site.

A tree has nodes with enclosed data and a connection from a node to another node that represent the edges of the tree. So, the first head or root node has a reference to be identified, and from this node, all the rest of the nodes can be found or accessed through a unique path. If a node has more than one way to be located, this structure is not a tree.

![This is a tree](https://github.com/juliehutchinson001/cs3_data_struct/blob/master/notes/images/Tree.jpg "Example of a Tree")

Looking at the previous diagram, there are more characteristics that come with a tree. For example, the term <strong>child</strong> is used when referring a node that is connected to a <strong>parent node</strong>, and all the nodes that have no children, are called <strong>leaf nodes</strong>. Parent - children relationships are not independent from each other.

## Binary Search Trees (BST)

You might be thinking at this point, what is the relationship between a tree and a binary search tree? Well, the previous image was not just a tree, it can also be referred as a binary search tree because of several reasons. Each of the nodes have two children, meaning this types of trees can have at most two children nodes, where the left child will always be smaller than the parent node, and the right child will always be bigger, in quantity, than the parent node.

The most noticeable benefit of using a binary search tree is that on every decision taken (every iteration), to find an specific data, we discard half of the data from which we are searching --similar to a binary search, where time complexity is O(logN).

### BST Height
