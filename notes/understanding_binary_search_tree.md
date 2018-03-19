# Understanding Binary Search Trees

<table>
    <tr>
        <td><center>__Binary Search Trees__</center></td>
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
</table>

The weight that time complexity entails is closely related with the  importance to create a data structure at compile time, that is going to verify every operation of a compiled code. A clear example involves comparing two common structures such as:

<table>
    <tr>
        <td><center>__Sorted Arrays__</center></td>
        <td><center>__Linked Lists__</center></td>
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
</table>

Let's take a look about Facebook webpage, there are some users who are only going to search for other users, or they can also be curious about their friend's pictures; and other users, like me for example that enjoy mostly uploading pictures to share in facebook profile.

The previous examples are a few of the many actions possible in a webpage, where a data structure such as binary search tree, with predictable running time, can speed up the loading of the site.

A tree has nodes with enclosed data and a connection from a node to another node that represent the edges of the tree. So, the first head or root node has a reference to be identified, and from this node, all the rest of the nodes can be found or accessed through only one path. If a node has more than a unique way to be located, it is easy to say that this structure is not a tree.
