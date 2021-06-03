class sack:
    def __init__(self,data1,capacity,fractional=1):
        self.data=data1
        #self.data_save=data
        #print(self.data_save)
        self.bagcapacity=capacity
        self.fractional=fractional
    
    def get_max_profit(self,data):
        # argument dictionary
        # return key of max profit
        return max(data, key =lambda item:item[0])
    def get_min_weight(self,data):
        # argument dictionary
        # return key of max profit
        return min(data, key =lambda item:item[1])
        
    def max_profit(self):
        total_profit=[]
        data=self.data[:]
        bagcapacity=self.bagcapacity
        fractional =self.fractional
        if fractional:
            while(bagcapacity>0 and len(data)!=0): 
                max_profit,weight=self.get_max_profit(data)
                
                if bagcapacity <weight:
                    rate=bagcapacity/weight
                    total_profit.append(max_profit*rate)
                    bagcapacity=0
                else:
                  total_profit.append(max_profit)
                  bagcapacity-=weight
                ## delete
                index=data.index([max_profit,weight])
                del data[index]
                #print(self.data)
                #print(reham)
    
            return sum(total_profit)
        else:
            while(bagcapacity>0 and len(data)!=0): 
                  max_profit,weight=self.get_max_profit(data)
                  
                  if bagcapacity <weight:
                      bagcapacity=0
                  else:
                    total_profit.append(max_profit)
                    bagcapacity-=weight
                  ## delete
                  index=data.index([max_profit,weight])
                  del data[index]
                  #print(data)
    
            return sum(total_profit)
        
    def min_weight(self):
        total_profit=[]
        data=self.data[:]
        #print(data)
        bagcapacity=self.bagcapacity
        fractional =self.fractional
        #print(self.data_save)
        if fractional:
              while(bagcapacity>0 and len(data)!=0): 
                      max_profit,weight=self.get_min_weight(data)
                      
                      if bagcapacity <weight:
                          rate=bagcapacity/weight
                          total_profit.append(max_profit*rate)
                          bagcapacity=0
                      else:
                        total_profit.append(max_profit)
                        bagcapacity-=weight
                      ## delete
                      index=data.index([max_profit,weight])
                      del data[index]
                      #print(data)
              return sum(total_profit)
        else:
             while(bagcapacity>0 and len(data)!=0): 
                    max_profit,weight=self.get_min_weight(data)
                    
                    if bagcapacity <weight:
                        bagcapacity=0
                    else:
                      total_profit.append(max_profit)
                      bagcapacity-=weight
                    ## delete
                    index=data.index([max_profit,weight])
                    del data[index]
                    #print(data)
             return sum(total_profit)
             
    def profitperweight(self):
        pro_w=[]
        total_profit=[]
        data=self.data[:]
        bagcapacity=self.bagcapacity
        fractional =self.fractional
        #self.data=self.data_save
        for i in data:
              pro_w.append(i[0]/i[1])
        if fractional:
            
            #print(pro_w)
            while(bagcapacity>0 and len(data)!=0 ):
                place=pro_w.index(max(pro_w))
              
                max_profit,weight=data[place]
                if bagcapacity <weight:
                    rate=bagcapacity/weight
                    total_profit.append(max_profit*rate)
                    bagcapacity=0
                else:
                    total_profit.append(max_profit)
                    bagcapacity-=weight
                ## delete
                index=data.index([max_profit,weight])
                del data[index]
                del pro_w[place]
            return sum(total_profit)
        else:
          while(bagcapacity>0 and len(pro_w)!=0 ):
                place=pro_w.index(max(pro_w))
                
                max_profit,weight=data[place]
                #print(place)
                if bagcapacity <weight:
                    bagcapacity=0
                else:
                    total_profit.append(max_profit)
                    bagcapacity-=weight
                ## delete
                index=data.index([max_profit,weight])
                del data[index]
                del pro_w[place]
          return sum(total_profit)





def main():
    # enter profits
    # weights
    # data
    # fractional or I/O
    # method (mp,mw,pw,all)
    # maxweight
    profits=list(map(int,input("Enter Profits separated by spaces: ").split()))
    weights=list(map(int,input("Enter Weights separated by spaces: ").split()))
    fractionalornot=int(input("Choose Fractional=1 or I/O=0: "))
    method=int(input("Choose method for max profit = 1 , min Weight = 2, profit per weight = 3 ,all=4: "))
    capacity=float(input("Write your capacity constraint: "))
    # create data
    data=[]
    if len(profits)!=len(weights):
        print("Not a valid input profit and weights have different lengths")
        return
    for i in range(len(profits)):
        data.append([profits[i],weights[i]])
    # create the bag object
    #print(data)
    # pass to it the data , fractional,capacity
    bag=sack(data,capacity,fractionalornot)
    ## inside the code i delete the data we must save it in somewhere ## problem
    if method==1:
        print("Max Profit: ",bag.max_profit())
    elif method==2:
        print("Min Weight: ",bag.min_weight())
    elif method == 3:
        print("Max Profit/Weight: ",bag.profitperweight())
    else:
         print("Max Profit: ",bag.max_profit())
         print("Min Weight: ",bag.min_weight())
         print("Max Profit/Weight: ",bag.profitperweight())
        
    
c=1
while(c!=0):
    main()
    c=int(input("enter 0 to close the program and 1 to continue: "))
        

