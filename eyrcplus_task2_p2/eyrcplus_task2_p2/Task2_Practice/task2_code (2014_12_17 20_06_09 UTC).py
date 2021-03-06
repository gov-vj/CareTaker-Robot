import numpy as np
import cv2

#Teams can add other helper functions
#which can be added here

class EyantaHeap:
    size=0
    class Entry:
        def __init__(self,rc,dis,prc):
            self.rc=rc
            self.dis=dis
            self.prc=prc
    heap=[]
    def insert(self,row,col,dis,prow,pcol):
        rc=(row*10)+col
        prc=(prow*10)+pcol
        self.heap[0]=self.Entry(rc,dis+1,prc)
        i=self.size
        self.size+=1
        while i>0 and self.heap[(i-1)/2].dis>self.heap[i].dis:
            self.exchange(i,(i-1)/2)
            i=(i-1)/2

    def exchange(self,i,j):
        temp=self.heap[j]
        self.heap[j]=self.heap[i]
        self.heap[i]=temp

    def removeMin():
        return self.remove(0)

    def remove(index):
        c=0
        ans=self.heap[index].dis,self.heap[index].rc,self.heap[index].prc
        self.exchange(size-1,index)
        self.size-=1
        while self.size>(2*index)+1:
            if self.size>(2*index)+2:
              if self.heap[index].dis>self.heap[(2*index)+1].dis||self.heap[index].dis>self.heap[(2*index)+2].dis:
                  if self.heap[(2*index)+1].dis>self.heap[(2*index)+2].dis:
                      
        
class Track:
    def __init__(self,prow,pcol,dis,in_setA):
        self.prow=prow
        self.pcol=pcol
        self.dis=dis
        self.in_setA=in_setA

track=[]
heap=EyantraHeap()
    
def play(img):
    '''
    img-- a single test image as input argument
    route_length  -- returns the single integer specifying the route length
    '''
    #add your code here
    red=[4,4]           #img 5
    green=[9,9]
    brc=[01,08,22,23,24,14,28,29,26,36,46,47,41,42,52,62,74,64,65,66,81,82,78,79,86,96] 
    for i in range(10):
        tempList=[]
        for j in range(10):
            tempList.append(10*i+j)
        track.append(tempList)
    for i in range(10):
        for j in range(10):
            track[i][j]=Track(0,0,0,False)
    row=red[0]
    col=red[1]
    track[row][col].in_setA=True
    insertInHeap(row,col,0)
    return route_length, route_path

insertinHeap(row,col,dis):
    if (row+1)<=9:
        temp=(row+1)*10+col
        if not((temp in brc) or track[row+1][col].in_setA):
            


if __name__ == "__main__":
    #code for checking output for single image
    img = cv2.imread('test_images/test_image1.png')
    route_length, route_path = play(img)
    print "route length = ", route_length
    print "route path   = ", route_path
    #code for checking output for all images
    route_length_list = []
    route_path_list   = []
    for file_number in range(1,6):
        file_name = "test_images/test_image"+str(file_number)+".png"
        pic = cv2.imread(file_name)
        route_length, route_path = play(pic)
        route_length_list.append(route_length)
        route_path_list.append(route_path)
    print route_length_list
    print route_path_list
