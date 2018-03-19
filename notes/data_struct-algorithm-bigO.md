
# Data Structures, Algorithms and Time/Space Complexity

<table>
    <tr>
        <td>__Sorted Arrays__</td>
        <td>__Linked Lists__</td>
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

>- To insert a new item in the array, it is quite slow because the data in the array needs to be rearranged, that is the reason this process takes order N linear time Complexity.

>- If we wanted to insert a new item on a linked list, on the other hand, this process requires an algorithm that is fast because it only needs to update the references of the nodes, so it can be done on order 1 constant time complexity.
