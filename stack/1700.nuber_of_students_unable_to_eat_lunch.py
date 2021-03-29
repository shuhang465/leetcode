class Solution:
#思路就是定位在student中sandwich[0]的元素，如果没有，就直接返回当前长度；
#如果找的话，就剔除当前元素进行重新排序
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        for sandwich in sandwiches:
            if sandwich in students:
                students.pop(students.index(sandwich))
            else:
                return len(students)       
        return 0 

        
