le = [2,4,6,8,10]
lo = [2,4,6,8]


def file(name):
    """converts a txt to a list of numbers"""
    words = "C:/python27/" + name+".txt"
    doc= open(words)
    lis =[]
    for i in doc:
        lis.append(float(i))
    return lis


def mean(l):
    '''calculates the mean of a list of numbers '''
    sums = 0
    for i in l:
        sums += float(i)
    means = sums/len(l)
    return means

def sd(l):
    '''calculates the standard deviation of a list of numbers '''
    m = mean(l)
    x = []
    for i in l:
        x.append((i-m)**2)
    sums = 0
    for i in x:
        sums+=i
    v = sums/(len(l)-1)
    sd = v**(0.5)
    return sd

def median(l):
    '''calculates the median of a list of numbers '''
    l.sort()
    half = len(l)/2
    if len(l)%2==0:
        median = ( l[(half-1)] + l[half])/2.0
        #print half-1, half
    else:
        median = l[half]
        #print int(half) 
    return median

def iqr(l):
    '''calulates the stats and returns the interquartile range of a list of numbers '''
    l.sort()
    iq3 = []
    iq1 =[]
    
    if len(l)%2!=0:
        middle = len(l)/2
        #print middle
        for i in range(len(l)):
            if i < middle:
                iq1.append(l[i])
                
            elif i > middle:
                iq3.append(l[i])
        iq1.append(l[middle])
        iq3.append(l[middle])
        
    else:
        middle1 = len(l)/2 -1
        middle2 = len(l)/2
        #print middle1, middle2
        for i in range(len(l)):
            if i <= middle1:
                iq1.append(l[i])
            elif i>=middle2:
                iq3.append(l[i])
   
    print "min", "iq1", "median", "mean", "iq3", "max"
    print l[0], median(iq1), median(l),mean(l), median(iq3), l[-1]
    return median(iq3) - median(iq1)
nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn    
def z(l):
    '''calculates the zscores of a list of numbers '''
    meanz = mean(l)
    zscores = []
    for i in l:
        zscore = (i-meanz)/sd(l)
        zscores.append(zscore)
    return zscores

choc = [1,2,3,4,5,6,7,8,9,10,11]
hap = [1,2,3,4,5,6,7,8,9,10]
        
def r(x,y):
    '''calculates the regression of a list of numbers '''
    zscoresx =z(x)
    zscoresy = z(y)
    
    zscoresxofy = []
    for i in range(len(x)):
        zscoresxofy.append(zscoresx[i]*zscoresy[i])
    
    return sum(zscoresxofy)/(len(x)-1)



def listmaker(thelist, value, freq):
    '''This creates a list with values aappearing freq times'''
    counter = 0
    while counter < freq:
        thelist.append(value)
        counter += 1
    print done

  
