import random
class node(object):
  def init_(self,key,level):
    self.key=key
    self.forward=[none]*(level+1)
class skiplist(object):
  def init_(self,max_lvl,p):
    self.MAXLVL=max_lvl
    self.p=p
    self.header=self.createnode(self.MAXLVL,-1)
    self.level=0
  def createnode(self,lvl,key):
    n=node(key,lvl)
    return n
  def randomlevel(self):
    lvl=0
    while random.random()<self.P and\lvl<self.MAXLVL:lvl+=1
    return|v|
  def insertelement(self,key):
    update=[none]*(self.MAXLVL+1)
    current=self.header
    for i in range(self.level,-1,-1):
      while current.forward[i]and\current.forward[i].key<key:
	current=current.forward[i]
      update[i]=current
    current=current.forward[0]
    if current==none or current.key!=key:
      alevel=self.randomlevel()
      
      if rlevel>self.level:
	for i in range(self,level+1,rlevel+1):
	  update[i]=self.header
        self.level=rlevel
      n=self.createnode(rlevel,key)
      for i in range(rlevel+1):
	n.forward[i]=update[i].forward[i]
	update[i].forward[i]=n 
      print("successfully inserted key{}".forward(key))
  def displaylist(self):
    print("\n*******skip list*******)
    head=self.header
    for|v| in range(self.level+1):
      print("level{}:"forward|v|,end=" ")
      node=head.forward[|v|]
      while(node!=none):
        print(node.key,end=" ")
        node=node.forward[|v|]
      print(" ")
  def main():
   lst=skiplist(3,0.5)
   lst=insertelement(3)
   lst=insertelement(6)
   lst=insertelement(7)
   lst=insertelement(9)
   lst=insertelement(12)
   lst=insertelement(19)
   lst=insertelement(17)
   lst=insertelement(3)
   lst=insertelement(26)
   lst=insertelement(21)
   lst=insertelement(25)
   lst.displaylist()
  main()
