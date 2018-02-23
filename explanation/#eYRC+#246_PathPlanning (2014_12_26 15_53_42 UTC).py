import numpy as np
import cv2

#Teams can add other helper functions
#which can be added here

class EyantraHeap:       #heap class for finding min value
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
        
class Track:        #for storing path length and previous value of nodes
    def __init__(self,prow=0,pcol=0,dis=0,in_setA=False):
        self.prow=prow
        self.pcol=pcol
        self.dis=dis
        self.in_setA=in_setA

track=[]
Eheap=EyantraHeap()
brc=[]
#black block

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
    red=[]           #red block, red=[row,col]
    green=[]         #green block, green=[row,col]
    ## for green coordinates
    param1 = [0,5,0]
    param2 = [80,255,255]
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower = np.array(param1)
    upper = np.array(param2)
    mask  = cv2.inRange(hsv, lower, upper)
    res   = cv2.bitwise_and(img, img, mask= mask)

    i =0
    gray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,127,255,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    M = cv2.moments(contours[i])
    cxg = int(M['m10']/M['m00'])/40
    cyg = int(M['m01']/M['m00'])/40
    green.append(cyg);
    green.append(cxg);

    ##for red
    for i in range(11):  ## drawing white lines to separate the contours of red and black
        cv2.line(img,(0,(40*i)),(400,(40*i)),(255,255,255),3)
        cv2.line(img,((40*i) ,0),((40*i) ,400),(255,255,255),3)
    blur1 = cv2.GaussianBlur(img,(3,5),0)
    param1r = [0,10,0]
    param2r = [55,255,255]
    hsv = cv2.cvtColor(blur1,cv2.COLOR_BGR2HSV)
    lowerr = np.array(param1r)   
    upperr = np.array(param2r)
    mask  = cv2.inRange(hsv, lowerr, upperr)
    resr   = cv2.bitwise_and(blur1, blur1, mask= mask)

    i =0
    gray = cv2.cvtColor(resr,cv2.COLOR_BGR2GRAY)
    retr,threshr = cv2.threshold(gray,127,255,0)
    contoursr, hierarchyr = cv2.findContours(threshr,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img,contoursr,i,(255,255,255),80)
    M = cv2.moments(contoursr[i])
    cx = int(M['m10']/M['m00'])/40      ## cx and cy are normalized by dividing by 40
    cy = int(M['m01']/M['m00'])/40     
    red.append(cy);
    red.append(cx);

    ##for black
    param1b = [0,0,0]
    param2b = [80,255,255]
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lowerb = np.array(param1b)     
    upperb = np.array(param2b)
    mask  = cv2.inRange(hsv, lowerb, upperb)
    resb   = cv2.bitwise_and(img, img, mask= mask)
    gray = cv2.cvtColor(resb,cv2.COLOR_BGR2GRAY)
    retb,threshb = cv2.threshold(gray,127,255,0)
    contoursb, hierarchyb = cv2.findContours(threshb,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
  
    #number of contours of black is len(contoursb)-1
    for i in range(1,len(contoursb)):
            M = cv2.moments(contoursb[i])
            cxb=int(M['m10']/M['m00'])/40
            cyb=int(M['m01']/M['m00'])/40
            cyxb=(10*cyb)+cxb;
            brc.append(cyxb);
            
    #we use dijikstra algo
    for i in range(10):   #making 10 by 10 tempList equivalent to image
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
    route_length=track[row][col].dis
    leng=route_length-1
    route_path=[]
    for i in range(leng+1):
        route_path.append(0)
    route_path[leng]=(col+1,row+1)
    while red[0]!=row or red[1]!=col:
        prow=track[row][col].prow
        pcol=track[row][col].pcol
        row=prow
        col=pcol
        leng-=1
        if leng>=0:
            route_path[leng]=(col+1,row+1)
    while len(track)!=0:
        track.pop()
    while len(brc)!=0:
        brc.pop()
    while len(Eheap.heap)!=0:
        Eheap.heap.pop()
    return route_length, route_path
            


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
