from typing import List


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
      self.persons = persons
      self.times = times
      self.winners = self.countVote(self.persons)
    
    def findTime(self,times:List[int],t:int):
      i = 0
      j = len(times)-1
      best = 0
      while i <= j:
        mid = i+(j-i)//2
        if times[mid] > t:
          j = mid-1
        elif times[mid] < t:
          best = mid
          i = mid+1
        else:
          return mid
      return best
    
    
    def countVote(self,persons:List[int]):
      dic = {}
      winner = {}
      maxvote = 0
      for i in range(len(persons)):
        if persons[i] in dic:
          dic[persons[i]]+=1
          if dic[persons[i]] >= maxvote:
            maxvote = dic[persons[i]]
            winner[i] = persons[i]
          else:
            winner[i] = winner[i-1]
        else:
          dic[persons[i]] = 1
          if 1 >= maxvote:
            maxvote = 1
            winner[i] = persons[i]
          else:
            winner[i] = winner[i-1] 
      return winner
      
    
    
    def q(self, t: int) -> int:
      time = self.findTime(self.times,t)
      # return self.countVote(self.persons[:time+1])
      return self.winners[time]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)