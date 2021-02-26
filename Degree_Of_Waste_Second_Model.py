X = int(input("input width of cube side:"))
R = int(input("input width of sheet:"))



#Now looking at idealising which orientation

# Begins with converting width of each square in template into unique measurement
# measure width R in terms of no. of boxes that fit its width. 

R1 = R/X




X1 =3
X2 =4



# Calculates number of boxes left after the maximum of each template has been
# cut i.e if the width is 5 boxes the vertical template will have 1 template cut
# And so a single box left
V1 = R1 % X1

V2 = R1 % X2



# Here we see whichever template would have more wasted boxes is disregarded
# and the other template used
if (3*X)>R:
    print("The cardboard sheet is not wide enough for one box of this size")
    K = 4*V1
    # Note that the K value is just so that the function below works and
    # tells us that 100% of cardboard is wasted
    

elif V1 > V2:
    print("Use vertical template")
    K = 3*V2
    
    
elif V2 > V1:

    print("Use Horizontal template")
    K=4*V1
    
    
else:
    print("Use Horizontal template")
    K =4 * V1


# =============================================================================
# Next stage is to workout based on which template is used what the overall percentage of waste is
# K is equivalent to wasted boxes, F is total percent of material wasted per row of boxes cut
# 
# NoT is number of templates

#This calculates the percentage of wasted cardboard overall with this template
# =============================================================================
NoT = R1//X1
F = (K+(6*NoT))/((NoT*12)+K)




print("proportion of Wasted Cardboard:" , F)


# Program will crash with string inputs
