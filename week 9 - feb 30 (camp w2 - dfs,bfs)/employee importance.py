# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

from typing import List


class Solution:
    importance = 0
    dic = {}
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        for i in employees:
            self.dic[i.id] = i
        def recursion(employee):
            self.importance += employee.importance
            if not employee.subordinates:
                return employee.importance
            for i in employee.subordinates:
                employee = self.dic[i]
                recursion(employee)
            return self.importance
        recursion(self.dic[id])
        return self.importance
                
            
        
            
            
        