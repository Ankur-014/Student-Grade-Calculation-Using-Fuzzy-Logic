# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 01:03:21 2019

@author: Salim Shadman Ankur
         Roll :1507014
"""

#INPUT CRISP VALUE
CLASS, time, classtest = list(map(float, input("Enter the marks of classes, times, classtests: ").split(" ")))


#Taking the graph point of x axis

#VARIABLE "CLASS"

fclass = [0, 0, 0.20, 0.30] #FEW
aclass = [0.20, 0.30, 0.45, 0.55] #AVERAGE
hclass = [0.45, 0.55, 0.70, 0.80] #HIGH
vhclass = [0.70, 0.80, 1, 1] #VERY HIGH

#VARIABLE "TIME"

ltime = [0,0, 0.20, 0.40] #LOW
atime = [0.20, 0.40, 0.60, 0.80] #AVERAGE
latime = [0.60, 0.80, 1, 1] #LARGE

#VARIABLE "CLASS TEST"

vlctest = [0,0,0.15,0.25] #VERY LOW
lctest = [0.15, 0.25, 0.35, 0.45] #LOW
acltest = [0.35, 0.45, 0.55, 0.65] #AVERAGE
hctest = [0.55, 0.65, 0.75, 0.85] #HIGH
vhctest = [0.75, 0.85,1,1] #VERY HIGH

#FUZZIFICATION OF INPUT VARIABLE

val_class = [] 
val_time = []
val_ctest = []


def fuzzify_class_val(x):
    if x > fclass[3]:
        val_class.append(0) #0
    elif x < fclass[0]:
        val_class.append(0) #0
    elif x>=fclass[0] and x<=fclass[1]:
        temp = (x-fclass[0])/(fclass[1]-fclass[0]) #(x-a)/(b-a)
        val_class.append(temp)
    elif x>=fclass[1] and x<=fclass[2]:
        val_class.append(1) #1
    elif x>=fclass[2] and x<=fclass[3]:
        temp = (fclass[3]-x)/(fclass[3]-fclass[2]) #(d-x)/(d-c)
        val_class.append(temp)

    if x > aclass[3]:
        val_class.append(0)
    elif x < aclass[0]:
        val_class.append(0)
    elif x>=aclass[0] and x<=aclass[1]:
        temp = (x-aclass[0])/(aclass[1]-aclass[0])
        val_class.append(temp)
    elif x>=aclass[1] and x<=aclass[2]:
        val_class.append(1)
    elif x>=aclass[2] and x<=aclass[3]:
        temp = (aclass[3]-x)/(aclass[3]-aclass[2])
        val_class.append(temp)

    if x > hclass[3]:
        val_class.append(0)
    elif x < hclass[0]:
        val_class.append(0)
    elif x>=hclass[0] and x<=hclass[1]:
        temp = (x-hclass[0])/(hclass[1]-hclass[0])
        val_class.append(temp)
    elif x>=hclass[1] and x<=hclass[2]:
        val_class.append(1)
    elif x>=hclass[2] and x<=hclass[3]:
        temp = (hclass[3]-x)/(hclass[3]-hclass[2])
        val_class.append(temp)

    if x > vhclass[3]:
        val_class.append(0)
    elif x < vhclass[0]:
        val_class.append(0)
    elif x>=vhclass[0] and x<=vhclass[1]:
        temp = (x-vhclass[0])/(vhclass[1]-vhclass[0])
        val_class.append(temp)
    elif x>=vhclass[1] and x<=vhclass[2]:
        val_class.append(1)
    elif x>=vhclass[2] and x<=vhclass[3]:
        temp = (vhclass[3]-x)/(vhclass[3]-vhclass[2])
        val_class.append(temp)


def fuzzify_time_val(x):
    if x > ltime[3]:
        val_time.append(0)
    elif x < ltime[0]:
        val_time.append(0)
    elif x >= ltime[0] and x <= ltime[1]:
        temp = (x - ltime[0]) / (ltime[1] - ltime[0])
        val_time.append(temp)
    elif x >= ltime[1] and x <= ltime[2]:
        val_time.append(1)
    elif x >= ltime[2] and x <= ltime[3]:
        temp = (ltime[3] - x) / (ltime[3] - ltime[2])
        val_time.append(temp)

    if x > atime[3]:
        val_time.append(0)
    elif x < atime[0]:
        val_time.append(0)
    elif x >= atime[0] and x <= atime[1]:
        temp = (x - atime[0]) / (atime[1] - atime[0])
        val_time.append(temp)
    elif x >= atime[1] and x <= atime[2]:
        val_time.append(1)
    elif x >= atime[2] and x <= atime[3]:
        temp = (atime[3] - x) / (atime[3] - atime[2])
        val_time.append(temp)

    if x > latime[3]:
        val_time.append(0)
    elif x < latime[0]:
        val_time.append(0)
    elif x >= latime[0] and x <= latime[1]:
        temp = (x - latime[0]) / (latime[1] - latime[0])
        val_time.append(temp)
    elif x >= latime[1] and x <= latime[2]:
        val_time.append(1)
    elif x >= latime[2] and x <= latime[3]:
        temp = (latime[3] - x) / (latime[3] - latime[2])
        val_time.append(temp)


def fuzzify_classtest_val(x):
    if x > vlctest[3]:
        val_ctest.append(0)
    elif x < vlctest[0]:
        val_ctest.append(0)
    elif x >= vlctest[0] and x <= vlctest[1]:
        temp = (x - vlctest[0]) / (vlctest[1] - vlctest[0])
        val_ctest.append(temp)
    elif x >= vlctest[1] and x <= vlctest[2]:
        val_ctest.append(1)
    elif x >= vlctest[2] and x <= vlctest[3]:
        temp = (vlctest[3] - x) / (vlctest[3] - vlctest[2])
        val_ctest.append(temp)

    if x > lctest[3]:
        val_ctest.append(0)
    elif x < lctest[0]:
        val_ctest.append(0)
    elif x >= lctest[0] and x <= lctest[1]:
        temp = (x - lctest[0]) / (lctest[1] - lctest[0])
        val_ctest.append(temp)
    elif x >= lctest[1] and x <= lctest[2]:
        val_ctest.append(1)
    elif x >= lctest[2] and x <= lctest[3]:
        temp = (lctest[3] - x) / (lctest[3] - lctest[2])
        val_ctest.append(temp)

    if x > acltest[3]:
        val_ctest.append(0)
    elif x < acltest[0]:
        val_ctest.append(0)
    elif x >= acltest[0] and x <= acltest[1]:
        temp = (x - acltest[0]) / (acltest[1] - acltest[0])
        val_ctest.append(temp)
    elif x >= acltest[1] and x <= acltest[2]:
        val_ctest.append(1)
    elif x >= acltest[2] and x <= acltest[3]:
        temp = (acltest[3] - x) / (acltest[3] - acltest[2])
        val_ctest.append(temp)

    if x > hctest[3]:
        val_ctest.append(0)
    elif x < hctest[0]:
        val_ctest.append(0)
    elif x >= hctest[0] and x <= hctest[1]:
        temp = (x - hctest[0]) / (hctest[1] - hctest[0])
        val_ctest.append(temp)
    elif x >= hctest[1] and x <= hctest[2]:
        val_ctest.append(1)
    elif x >= hctest[2] and x <= hctest[3]:
        temp = (hctest[3] - x) / (hctest[3] - hctest[2])
        val_ctest.append(temp)

    if x > vhctest[3]:
        val_ctest.append(0)
    elif x < vhctest[0]:
        val_ctest.append(0)
    elif x >= vhctest[0] and x <= vhctest[1]:
        temp = (x - vhctest[0]) / (vhctest[1] - vhctest[0])
        val_ctest.append(temp)
    elif x >= vhctest[1] and x <= vhctest[2]:
        val_ctest.append(1)
    elif x >= vhctest[2] and x <= vhctest[3]:
        temp = (vhctest[3] - x) / (vhctest[3] - vhctest[2])
        val_ctest.append(temp)


fuzzify_class_val(CLASS)
fuzzify_time_val(time)
fuzzify_classtest_val(classtest)

#ASSESSMENT

vl = [] #VERY LOW
l = [] #LOW
a = [] #AVERAGE
h = [] #HIGH
vh = [] #VERY HIGH

#FUZZY RULES EVALUATION

vl.append(min(val_class[0],min(val_time[0],val_ctest[0])))
vl.append(min(val_class[0],min(val_time[0],val_ctest[1])))
vl.append(min(val_class[0],min(val_time[0],val_ctest[2])))
l.append(min(val_class[0],min(val_time[0],val_ctest[3])))
l.append(min(val_class[0],min(val_time[0],val_ctest[4])))
vl.append(min(val_class[0],min(val_time[1],val_ctest[0])))
vl.append(min(val_class[0],min(val_time[1],val_ctest[1])))
l.append(min(val_class[0],min(val_time[1],val_ctest[2])))
a.append(min(val_class[0],min(val_time[1],val_ctest[3])))
h.append(min(val_class[0],min(val_time[1],val_ctest[4])))
vl.append(min(val_class[0],min(val_time[2],val_ctest[0])))
vl.append(min(val_class[0],min(val_time[2],val_ctest[1])))
l.append(min(val_class[0],min(val_time[2],val_ctest[2])))
a.append(min(val_class[0],min(val_time[2],val_ctest[3])))
h.append(min(val_class[0],min(val_time[2],val_ctest[4])))


vl.append(min(val_class[1],min(val_time[0],val_ctest[0])))
vl.append(min(val_class[1],min(val_time[0],val_ctest[1])))
l.append(min(val_class[1],min(val_time[0],val_ctest[2])))
a.append(min(val_class[1],min(val_time[0],val_ctest[3])))
h.append(min(val_class[1],min(val_time[0],val_ctest[4])))
vl.append(min(val_class[1],min(val_time[1],val_ctest[0])))
vl.append(min(val_class[1],min(val_time[1],val_ctest[1])))
l.append(min(val_class[1],min(val_time[1],val_ctest[2])))
a.append(min(val_class[1],min(val_time[1],val_ctest[3])))
h.append(min(val_class[1],min(val_time[1],val_ctest[4])))
vl.append(min(val_class[1],min(val_time[2],val_ctest[0])))
vl.append(min(val_class[1],min(val_time[2],val_ctest[1])))
l.append(min(val_class[1],min(val_time[2],val_ctest[2])))
a.append(min(val_class[1],min(val_time[2],val_ctest[3])))
h.append(min(val_class[1],min(val_time[2],val_ctest[4])))


vl.append(min(val_class[2],min(val_time[0],val_ctest[0])))
l.append(min(val_class[2],min(val_time[0],val_ctest[1])))
a.append(min(val_class[2],min(val_time[0],val_ctest[2])))
h.append(min(val_class[2],min(val_time[0],val_ctest[3])))
vh.append(min(val_class[2],min(val_time[0],val_ctest[4])))
vl.append(min(val_class[2],min(val_time[1],val_ctest[0])))
l.append(min(val_class[2],min(val_time[1],val_ctest[1])))
a.append(min(val_class[2],min(val_time[1],val_ctest[2])))
h.append(min(val_class[2],min(val_time[1],val_ctest[3])))
vh.append(min(val_class[2],min(val_time[1],val_ctest[4])))
vl.append(min(val_class[2],min(val_time[2],val_ctest[0])))
l.append(min(val_class[2],min(val_time[2],val_ctest[1])))
a.append(min(val_class[2],min(val_time[2],val_ctest[2])))
h.append(min(val_class[2],min(val_time[2],val_ctest[3])))
vh.append(min(val_class[2],min(val_time[2],val_ctest[4])))


l.append(min(val_class[3],min(val_time[0],val_ctest[0])))
a.append(min(val_class[3],min(val_time[0],val_ctest[1])))
h.append(min(val_class[3],min(val_time[0],val_ctest[2])))
h.append(min(val_class[3],min(val_time[0],val_ctest[3])))
vh.append(min(val_class[3],min(val_time[0],val_ctest[4])))
l.append(min(val_class[3],min(val_time[1],val_ctest[0])))
a.append(min(val_class[3],min(val_time[1],val_ctest[1])))
h.append(min(val_class[3],min(val_time[1],val_ctest[2])))
h.append(min(val_class[3],min(val_time[1],val_ctest[3])))
vh.append(min(val_class[3],min(val_time[1],val_ctest[4])))
l.append(min(val_class[3],min(val_time[2],val_ctest[0])))
a.append(min(val_class[3],min(val_time[2],val_ctest[1])))
h.append(min(val_class[3],min(val_time[2],val_ctest[2])))
vh.append(min(val_class[3],min(val_time[2],val_ctest[3])))
vh.append(min(val_class[3],min(val_time[2],val_ctest[4])))

#FUZZY RULES AGGREGATION

max_vl = max(vl)
max_l = max(l)
max_a = max(a)
max_h = max(h)
max_vh = max(vh)

#DEFUZZIFICATION

cog = max_vl*(0.0+0.05+0.1+0.15)
cog+= max_l*(0.2+0.25+0.3+0.35+0.4)
cog+= max_a*(0.45+0.5+0.55+0.6)
cog+= max_h*(0.65+0.70+0.75+0.8)
cog+= max_vh*(0.85+0.9+0.95+1)

cog/= ((max_vl*4)+(max_l*5)+(max_a*4)+(max_h*4)+(max_vh*4))
print("Student Assesment:",cog) #CRISP VALUE

#INPUT CRISP VALUE
part1, part2 = list(map(float, input("Enter the marks of part1, part2: ").split(" ")))


#Taking the graph point of x axis

#VARIABLE "PART1"

vlpart1 = [0, 0, 0.02, 0.18] #VERY LOW
lpart1 = [0.02, 0.18, 0.22, 0.38] #LOW
apart1 = [0.22, 0.38, 0.42, 0.58] #AVERAGE
hpart1 = [0.42, 0.58, 0.62, 0.78] #HIGH
vhpart1 = [0.62, 0.78, 0.82, 0.98] #VERY HIGH
vvhpart1 = [0.82, 0.98, 1, 1] #VERY VERY HIGH

#VARIABLE "PART2"

vlpart2 = [0, 0, 0.02, 0.18] #VERY LOW
lpart2 = [0.02, 0.18, 0.22, 0.38] #LOW
apart2 = [0.22, 0.38, 0.42, 0.58] #AVERAGE
hpart2 = [0.42, 0.58, 0.62, 0.78] #HIGH
vhpart2 = [0.62, 0.78, 0.82, 0.98] #VERY HIGH
vvhpart2 = [0.82, 0.98, 1, 1] #VERY VERY HIGH


#FUZZIFICATION OF INPUT VARIABLE

val_part1 = [] 
val_part2 = []

def fuzzify_part1_val(x):
    if x > vlpart1[3]:
        val_part1.append(0) #0
    elif x < vlpart1[0]:
        val_part1.append(0) #0
    elif x>=vlpart1[0] and x<=vlpart1[1]:
        temp = (x-vlpart1[0])/(vlpart1[1]-vlpart1[0]) #(x-a)/(b-a)
        val_part1.append(temp)
    elif x>=vlpart1[1] and x<=vlpart1[2]:
        val_part1.append(1) #1
    elif x>=vlpart1[2] and x<=vlpart1[3]:
        temp = (vlpart1[3]-x)/(vlpart1[3]-vlpart1[2]) #(d-x)/(d-c)
        val_part1.append(temp)
    
    if x > lpart1[3]:
        val_part1.append(0) #0
    elif x < lpart1[0]:
        val_part1.append(0) #0
    elif x>=lpart1[0] and x<=lpart1[1]:
        temp = (x-lpart1[0])/(lpart1[1]-lpart1[0]) #(x-a)/(b-a)
        val_part1.append(temp)
    elif x>=lpart1[1] and x<=lpart1[2]:
        val_part1.append(1) #1
    elif x>=lpart1[2] and x<=lpart1[3]:
        temp = (lpart1[3]-x)/(lpart1[3]-lpart1[2]) #(d-x)/(d-c)
        val_part1.append(temp)
        
    if x > apart1[3]:
        val_part1.append(0) #0
    elif x < apart1[0]:
        val_part1.append(0) #0
    elif x>=apart1[0] and x<=apart1[1]:
        temp = (x-apart1[0])/(apart1[1]-apart1[0]) #(x-a)/(b-a)
        val_part1.append(temp)
    elif x>=apart1[1] and x<=apart1[2]:
        val_part1.append(1) #1
    elif x>=apart1[2] and x<=apart1[3]:
        temp = (apart1[3]-x)/(apart1[3]-apart1[2]) #(d-x)/(d-c)
        val_part1.append(temp)
        
    if x > hpart1[3]:
        val_part1.append(0) #0
    elif x < hpart1[0]:
        val_part1.append(0) #0
    elif x>=hpart1[0] and x<=hpart1[1]:
        temp = (x-hpart1[0])/(hpart1[1]-hpart1[0]) #(x-a)/(b-a)
        val_part1.append(temp)
    elif x>=hpart1[1] and x<=hpart1[2]:
        val_part1.append(1) #1
    elif x>=hpart1[2] and x<=hpart1[3]:
        temp = (hpart1[3]-x)/(hpart1[3]-hpart1[2]) #(d-x)/(d-c)
        val_part1.append(temp)
        
    if x > vhpart1[3]:
        val_part1.append(0) #0
    elif x < vhpart1[0]:
        val_part1.append(0) #0
    elif x>=vhpart1[0] and x<=vhpart1[1]:
        temp = (x-vhpart1[0])/(vhpart1[1]-vhpart1[0]) #(x-a)/(b-a)
        val_part1.append(temp)
    elif x>=vhpart1[1] and x<=vhpart1[2]:
        val_part1.append(1) #1
    elif x>=vhpart1[2] and x<=vhpart1[3]:
        temp = (vhpart1[3]-x)/(vhpart1[3]-vhpart1[2]) #(d-x)/(d-c)
        val_part1.append(temp)
        
    if x > vvhpart1[3]:
        val_part1.append(0) #0
    elif x < vvhpart1[0]:
        val_part1.append(0) #0
    elif x>=vvhpart1[0] and x<=vvhpart1[1]:
        temp = (x-vvhpart1[0])/(vvhpart1[1]-vvhpart1[0]) #(x-a)/(b-a)
        val_part1.append(temp)
    elif x>=vvhpart1[1] and x<=vvhpart1[2]:
        val_part1.append(1) #1
    elif x>=vvhpart1[2] and x<=vvhpart1[3]:
        temp = (vvhpart1[3]-x)/(vvhpart1[3]-vvhpart1[2]) #(d-x)/(d-c)
        val_part1.append(temp)
    
    
def fuzzify_part2_val(x):
    if x > vlpart2[3]:
        val_part2.append(0) #0
    elif x < vlpart2[0]:
        val_part2.append(0) #0
    elif x>=vlpart2[0] and x<=vlpart2[1]:
        temp = (x-vlpart2[0])/(vlpart2[1]-vlpart2[0]) #(x-a)/(b-a)
        val_part2.append(temp)
    elif x>=vlpart2[1] and x<=vlpart2[2]:
        val_part2.append(1) #1
    elif x>=vlpart2[2] and x<=vlpart2[3]:
        temp = (vlpart2[3]-x)/(vlpart2[3]-vlpart2[2]) #(d-x)/(d-c)
        val_part2.append(temp)
    
    if x > lpart2[3]:
        val_part2.append(0) #0
    elif x < lpart2[0]:
        val_part2.append(0) #0
    elif x>=lpart2[0] and x<=lpart2[1]:
        temp = (x-lpart2[0])/(lpart2[1]-lpart2[0]) #(x-a)/(b-a)
        val_part2.append(temp)
    elif x>=lpart2[1] and x<=lpart2[2]:
        val_part2.append(1) #1
    elif x>=lpart2[2] and x<=lpart2[3]:
        temp = (lpart2[3]-x)/(lpart2[3]-lpart2[2]) #(d-x)/(d-c)
        val_part2.append(temp)
        
    if x > apart2[3]:
        val_part2.append(0) #0
    elif x < apart2[0]:
        val_part2.append(0) #0
    elif x>=apart2[0] and x<=apart2[1]:
        temp = (x-apart2[0])/(apart2[1]-apart2[0]) #(x-a)/(b-a)
        val_part2.append(temp)
    elif x>=apart2[1] and x<=apart2[2]:
        val_part2.append(1) #1
    elif x>=apart2[2] and x<=apart2[3]:
        temp = (apart2[3]-x)/(apart2[3]-apart2[2]) #(d-x)/(d-c)
        val_part2.append(temp)
        
    if x > hpart2[3]:
        val_part2.append(0) #0
    elif x < hpart2[0]:
        val_part2.append(0) #0
    elif x>=hpart2[0] and x<=hpart2[1]:
        temp = (x-hpart2[0])/(hpart2[1]-hpart2[0]) #(x-a)/(b-a)
        val_part2.append(temp)
    elif x>=hpart2[1] and x<=hpart2[2]:
        val_part2.append(1) #1
    elif x>=hpart2[2] and x<=hpart2[3]:
        temp = (hpart2[3]-x)/(hpart2[3]-hpart2[2]) #(d-x)/(d-c)
        val_part2.append(temp)
        
    if x > vhpart2[3]:
        val_part2.append(0) #0
    elif x < vhpart2[0]:
        val_part2.append(0) #0
    elif x>=vhpart2[0] and x<=vhpart2[1]:
        temp = (x-vhpart2[0])/(vhpart2[1]-vhpart2[0]) #(x-a)/(b-a)
        val_part2.append(temp)
    elif x>=vhpart2[1] and x<=vhpart2[2]:
        val_part2.append(1) #1
    elif x>=vhpart2[2] and x<=vhpart2[3]:
        temp = (vhpart2[3]-x)/(vhpart2[3]-vhpart2[2]) #(d-x)/(d-c)
        val_part2.append(temp)
        
    if x > vvhpart2[3]:
        val_part2.append(0) #0
    elif x < vvhpart2[0]:
        val_part2.append(0) #0
    elif x>=vvhpart2[0] and x<=vvhpart2[1]:
        temp = (x-vvhpart2[0])/(vvhpart2[1]-vvhpart2[0]) #(x-a)/(b-a)
        val_part2.append(temp)
    elif x>=vvhpart2[1] and x<=vvhpart2[2]:
        val_part2.append(1) #1
    elif x>=vvhpart2[2] and x<=vvhpart2[3]:
        temp = (vvhpart2[3]-x)/(vvhpart2[3]-vvhpart2[2]) #(d-x)/(d-c)
        val_part2.append(temp)
    
fuzzify_part1_val(part1)
fuzzify_part2_val(part2)

#ASSESSMENT

vl1 = [] #VERY LOW
l1 = [] #LOW
a1 = [] #AVERAGE
h1 = [] #HIGH
vh1 = [] #VERY HIGH
vvh1 = [] #VERY VERY HIGH

#FUZZY RULES EVALUATION

vl1.append(min(val_part1[0],val_part2[0]))
vl1.append(min(val_part1[0],val_part2[1]))
l1.append(min(val_part1[0],val_part2[2]))
l1.append(min(val_part1[0],val_part2[3]))
a1.append(min(val_part1[0],val_part2[4]))
h1.append(min(val_part1[0],val_part2[5]))


vl1.append(min(val_part1[1],val_part2[0]))
l1.append(min(val_part1[1],val_part2[1]))
l1.append(min(val_part1[1],val_part2[2]))
a1.append(min(val_part1[1],val_part2[3]))
a1.append(min(val_part1[1],val_part2[4]))
h1.append(min(val_part1[1],val_part2[5]))

l1.append(min(val_part1[2],val_part2[0]))
l1.append(min(val_part1[2],val_part2[1]))
a1.append(min(val_part1[2],val_part2[2]))
h1.append(min(val_part1[2],val_part2[3]))
h1.append(min(val_part1[2],val_part2[4]))
vh1.append(min(val_part1[2],val_part2[5]))

l1.append(min(val_part1[3],val_part2[0]))
a1.append(min(val_part1[3],val_part2[1]))
h1.append(min(val_part1[3],val_part2[2]))
h1.append(min(val_part1[3],val_part2[3]))
vh1.append(min(val_part1[3],val_part2[4]))
vvh1.append(min(val_part1[3],val_part2[5]))

a1.append(min(val_part1[4],val_part2[0]))
h1.append(min(val_part1[4],val_part2[1]))
h1.append(min(val_part1[4],val_part2[2]))
vh1.append(min(val_part1[4],val_part2[3]))
vh1.append(min(val_part1[4],val_part2[4]))
vvh1.append(min(val_part1[4],val_part2[5]))

a1.append(min(val_part1[5],val_part2[0]))
h1.append(min(val_part1[5],val_part2[1]))
vh1.append(min(val_part1[5],val_part2[2]))
vh1.append(min(val_part1[5],val_part2[3]))
vvh1.append(min(val_part1[5],val_part2[4]))
vvh1.append(min(val_part1[5],val_part2[5]))



#FUZZY RULES AGGREGATION

max_vl1 = max(vl1)
max_l1 = max(l1)
max_a1 = max(a1)
max_h1 = max(h1)
max_vh1 = max(vh1)
max_vvh1 = max(vvh1)

#DEFUZZIFICATION

cog1 = max_vl1*(0.0+0.05+0.1)
cog1+= max_l1*(0.15+0.2)
cog1+= max_a1*(0.25+0.3+0.35+0.4)
cog1+= max_h1*(0.45+0.5+0.55+0.6)
cog1+= max_vh1*(0.65+0.7+0.75+0.8)
cog1+= max_vvh1*(0.85+0.9+0.95+1)

cog1/= ((max_vl1*3)+(max_l1*2)+(max_a1*4)+(max_h1*4)+(max_vh1*4)+(max_vvh1*4))
print("Paper Assesment:",cog1) #CRISP VALUE


#GRADE CALCULATION

marks = (cog1*0.7)+(cog*0.3)
grade = marks*100

if grade>=80.0:
    print("A+")
elif grade<80.0 and grade >=75.0:
    print("A")
elif grade<75.0 and grade >=70.0:
    print("A-")
elif grade<70.0 and grade >=65.0:
    print("B+")
elif grade<65.0 and grade >=60.0:
    print("B")
elif grade<60.0 and grade >=55.0:
    print("B-")
elif grade<55.0 and grade >=50.0:
    print("C+")
elif grade<50.0 and grade >=45.0:
    print("C")
elif grade<45.0 and grade >=40.0:
    print("D")
else:
    print("F")
    














