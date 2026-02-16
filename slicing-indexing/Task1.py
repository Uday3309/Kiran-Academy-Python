
# -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
#  k   i   r   a   n     a  c  a  d  e  m  y
#  0   1   2   3   4  5  6  7  8  9  10 11 12
name="kiran academy"
divider="-"*(20)

print(f"{divider} 5 examples on Positive step size {divider}")

# O/P will be:kiran academy,ia cdm,r am,acm,nd
all_names=[name[0::1], name[1::2],name[2::3],name[3::4],name[4::5]]

for result in all_names:
    print(f"5 examples on Positive step size:{result}")

print(f"{divider} 5 examples on Negative step size {divider}")

# O/P will be:daca nar,yeaa,ma r,ear,dn
all_names=[name[-4:-12:-1], name[-1:-8:-2],name[-2::-3],name[-3::-4],name[-4::-5]]

for result in all_names:
    print(f"5 examples on Negative step size:{result}")

print(f"{divider} Start Negative, End Positive {divider}")

# O/P iwll be:kiran academy,iran,ran,krnaaey,ady
all_names=[name[-13::1], name[-12:-8:1], name[-11:-8:1], name[-13::2], name[-7::3]]

for result in all_names:
    print(f"Start Negative, End Positive:{result}")

print(f"{divider} Start Positive, End Negative {divider}")

# O/P will be:ymedaca narik,edac,narik,daca n,yeaa
all_names=[name[12::-1], name[10:6:-1], name[4::-1], name[9:3:-1], name[12:5:-2]]

for result in all_names:
    print(f"Start Positive, End Negative:{result}")

print(f"{divider} Start Negative, End Negative {divider}")

# O/P will be:k,narik,yea,d,daca nar
all_names=[name[-13::-1], name[-9::-1], name[-1:-6:-2], name[-4:-5:-1], name[-4:-12:-1]]

for result in all_names:
    print(f"Start Negative, End Negative:{result}")

print(f"{divider} Start Positive, End Positive {divider}")

# O/P will be:kiran academy,krn,ady,i,a
all_names=[name[0:13:1], name[0:5:2], name[6:13:3], name[1:5:4], name[6:9:5]]

for result in all_names:
    print(f"Start Positive, End Positive:{result}")



