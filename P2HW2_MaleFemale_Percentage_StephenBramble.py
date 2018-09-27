#Ask user for number of males
#Ask user for number of females
#Add the numbers together
#Divide the numbers based on respective gender
#Show the respective percentages



Male = int (input("Enter the number of males in your class:"))

Female = int (input("Enter the number of females in your class:"))

TOC = Male + Female

MalePer = Male/TOC

FemalePer = Female/TOC

print ("The percentage of males is:",format (MalePer, ".0%"),("The Percentage of females is:"),format (FemalePer, ".0%"), sep="\t")

input ("Press any key to terminate:")
