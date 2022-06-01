thisdict={
    "Brand":"ford",
    "Model" : "Mustang",
     "year":  1964
}
# thisdict["year"]=2020
# thisdict.update({"Model":"GT Mustang"})
# thisdict["Cost"]="150,000$"
# print(thisdict)
# del thisdict["Cost"]
# print("\n")
# print(thisdict)

# for s in thisdict:
#     print(s,":",thisdict[s])

# for x,y in thisdict.items():
#     print(x,y)

mydict=thisdict.copy()
# print(mydict)

thisdict["Colour"]="Black"
mydict["Colour"]="White"

print(mydict)
print("<><><><><><><>")
print(thisdict)