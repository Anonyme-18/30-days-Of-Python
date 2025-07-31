concat_1 = "Thirty " + "Days " + "python"
concat_2 = "Coding" + " For" + " All"

company = "Coding For All"

print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

first_word_removed = company[7:]
print(first_word_removed)

print('Coding' in company)
print(company.find('Coding'))
print(company.index('Coding'))

print(company.replace('Coding', 'Python'))

phrase = 'Python for Everyone'
print(phrase.replace('Everyone', 'All'))

print(company.split())

tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech_companies.split(","))

print(company[0])
print(company[-1])
print(company[10])

phrase1 = "Python For Everyone"
words1 = phrase1.split()
acronym1 = words1[0][0] + words1[1][0] + words1[2][0]
print(acronym1)

words2 = company.split()
acronym2 = words2[0][0] + words2[1][0] + words2[2][0]
print(acronym2)

print(company.index('C'))
print(company.index('F'))

sentence = "Coding For All People"
print(sentence.rfind('l'))

sentence2 = 'You cannot end a sentence with because because because is a conjunction'
print(sentence2.find('because'))
print(sentence2.rindex('because'))

start = sentence2.find('because')
end = sentence2.rindex('because') + len('because')
print(sentence2[start:end])

print(company.startswith('Coding'))
print(company.endswith('coding'))

spaced_string = ' Coding For All '
print(spaced_string.strip())

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = ' # '.join(libraries)
print(joined_libraries)


print("I am enjoying this challenge.\nI just wonder what is next.")
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinlande\tHelsinki")

radius = 10 
area = 3.14 * radius ** 2 
print(f'The area of a circle with radius {radius} is {area} meters square.')

eight= 8
six= 6

print(f'{eight} - {six} = {eight+six}')
print(f'{eight} - {six} = {eight-six}')
print('%d * %d = %d' %(eight,six,eight*six))
print("{} / {} =  {:.2f}".format(eight, six, eight/six))
print(f'{eight} % {six} = {eight%six}')
print("{} // {} =  {}".format(eight, six, eight//six))
print('%d ** %d = %d'%(eight,six,eight**six))
