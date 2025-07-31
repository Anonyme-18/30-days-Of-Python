it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

age = [22, 19, 24, 25, 26, 24, 25, 24]


#length of it companies
print("We have", len(it_companies), "IT companies.\n")

#Adding twitter 
it_companies.add("Twitter")
print(it_companies, "\n")

#insertion of multiple it companies
it_companies.update(['Samsung', 'Huawei', 'infosys'])
print(it_companies, "\n")

#removing item from it_companies
it_companies.remove("Facebook")
print(it_companies, "\n")

#difference between remove and discard
print("The both methods allow to delete an item on sets. The difference is: when the item is not find, remove method returns an error but discard method doesn't return error\n")


#Joining A and B
joined_sets=A.update(B)
print(joined_sets, "\n")


#intersection
print(A.intersection(B), "\n")

print("Is A subset of B?", A.issubset(A), "\n")

print("Are A and B disjoint sets ?:", A.isdisjoint(B), "\n")

print("The symetric difference between A and B is: ", A.symmetric_difference(B), "\n")

del A
del B

#converting off age to sets
age_sets= set(age)

#comparating of age list and ages sets
print("The age list length is: ", len(age), ", and the length of age sets is: ", len(age_sets), "\n")

#A string is an immutable, ordered sequence of characters enclosed in quotes (" " or ' '), meaning its content cannot be changed after creation and characters are stored in a specific order. A list is a mutable, ordered collection of elements enclosed in square brackets ([]), meaning you can modify, add, or remove items, and duplicates are allowed. A tuple is an immutable, ordered collection of elements enclosed in parentheses (()), which means its content cannot be changed after creation, but it can contain duplicates and keeps the order of elements. A set is a mutable, unordered collection of unique elements enclosed in curly braces ({}), meaning it does not allow duplicates, does not keep a fixed order, and its elements cannot be accessed by index.

sentence= "I am a teacher and I love to inspire and teach people"

all_words= sentence.split()

unique_words= set(all_words)

print("Unique words are :", unique_words, "\n")
print("We have :", len(all_words), " words" , " and ", len(unique_words), " unique words in the sentence\n")


















