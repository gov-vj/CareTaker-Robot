#####import numpy as np
#####import cv2

#Teams can add other helper functions
#which can be added here

class EyantraHeap:
    class Entry:
        def __init__(self,rc,dis,prc):   #record=rc,dis,prc
            self.rc=rc
            self.dis=dis
            self.prc=prc
    heap=[]
    def insert(self,row,col,dis,prow,pcol):
        rc=(row*10)+col
        prc=(prow*10)+pcol
        self.heap.append(self.Entry(rc,dis+1,prc))
        i=len(self.heap)-1
        while i>0 and self.heap[(i-1)/2].dis>self.heap[i].dis:
            self.exchange(i,(i-1)/2)
            i=(i-1)/2

    def exchange(self,i,j):
        temp=self.heap[j]
        self.heap[j]=self.heap[i]
        self.heap[i]=temp

    def removeMin(self):
        return self.remove(0)

    def remove(self,index):
        size=len(self.heap)
        ans=self.heap[index].dis,self.heap[index].rc,self.heap[index].prc
        self.exchange(size-1,index)
        self.heap.pop()
        size-=1
        while size>(2*index)+1:
            if size>(2*index)+2:
              if self.heap[index].dis>self.heap[(2*index)+1].dis or self.heap[index].dis>self.heap[(2*index)+2].dis:
                  if self.heap[(2*index)+1].dis>self.heap[(2*index)+2].dis:
                      c=(2*index)+2
                  else:
                      c=(2*index)+1
              else:
                  break
            else:
              if self.heap[index].dis>self.heap[(2*index)+1].dis:
                  c=(2*index)+1
              else:
                  break
            self.exchange(index,c)
            index=c
        return ans
        
class Track:
    def __init__(self,prow=0,pcol=0,dis=0,in_setA=False):
        self.prow=prow
        self.pcol=pcol
        self.dis=dis
        self.in_setA=in_setA

track=[]
Eheap=EyantraHeap()
brc=[1,8,22,23,24,14,28,29,26,36,46,47,41,42,52,62,74,64,65,66,81,82,78,79,86,96]
def insertInHeap(row,col,dis):
    if (row+1)<=9:
        temp=(row+1)*10+col
        if not((temp in brc) or track[row+1][col].in_setA):
            Eheap.insert(row+1,col,dis,row,col)
    if (row-1)>=0:
        temp=(row-1)*10+col
        if not((temp in brc) or track[row-1][col].in_setA):
            Eheap.insert(row-1,col,dis,row,col)
    if (col+1)<=9:
        temp=row*10+(col+1)
        if not((temp in brc) or track[row][col+1].in_setA):
            Eheap.insert(row,col+1,dis,row,col)
    if (col-1)>=0:
        temp=row*10+(col-1)
        if not((temp in brc) or track[row][col-1].in_setA):
            Eheap.insert(row,col-1,dis,row,col)

def play(img):
    '''
    img-- a single test image as input argument
    route_length  -- returns the single integer specifying the route length
    '''
    
    #add your code here
    red=[4,4]           #img 5
    green=[9,9] 
    for i in range(10):
        tempList=[]
        for j in range(10):
            tempList.append(Track())
        track.append(tempList)
    row=red[0]
    col=red[1]
    track[row][col].in_setA=True
    insertInHeap(row,col,0)
    while green[0]!=row or green[1]!=col:
        ans=Eheap.removeMin()
        dis=ans[0]
        row=ans[1]/10
        col=ans[1]%10
        prow=ans[2]/10
        pcol=ans[2]%10
        track[row][col].dis=dis
        track[row][col].prow=prow
        track[row][col].pcol=pcol
        if not track[row][col].in_setA:
            insertInHeap(row,col,dis)
            track[row][col].in_setA=True
    row=green[0]
    col=green[1]
    print "dist %d \n" %(track[row][col].dis)
    print "%d, %d" %(row,col)
    while red[0]!=row or red[1]!=col:
        prow=track[row][col].prow
        pcol=track[row][col].pcol
        row=prow
        col=pcol
        print "%d, %d" %(row,col)
#####    return route_length, route_path
            


if __name__ == "__main__":
    play(0)
    #code for checking output for single image
#    img = cv2.imread('test_images/test_image1.png')
#    route_length, route_path = play(img)
#    print "route length = ", route_length
#    print "route path   = ", route_path
    #code for checking output for all images
#    route_length_list = []
#    route_path_list   = []
#    for file_number in range(1,6):
#        file_name = "test_images/test_image"+str(file_number)+".png"
#        pic = cv2.imread(file_name)
#        route_length, route_path = play(pic)
#        route_length_list.append(route_length)
#        route_path_list.append(route_path)
#    print route_length_list
#    print route_path_list
