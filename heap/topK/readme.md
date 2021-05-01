topk问题：排在前k的元素，不要求顺序，适合用堆。    
最简单的做法就是用heapq.nlargest(k, heap)，但是对于（13,a)(13,b),也会排成（13，b)(13,a)，就是freq和word都是从大到小排的，所以这时候要用heapq.nsmallest,freq取负值。比如692.
692可以直接用heapq.nsmallest,也可以建成大顶堆之后pop出来k个。
