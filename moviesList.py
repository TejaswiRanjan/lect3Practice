#WAP to ask the user to enter names of their 3 favourite movies & store them into list

movies = []

movies1 = input("Enter the first favourite movie name : ")
movies2 = input("Enter the second favourite movie name : ")
movies3 = input("Enter the third favourite movie name : ")
movies.append(movies1)
movies.append(movies2)
movies.append(movies3)

print("The favourite movies are : ",movies)