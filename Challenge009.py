#----------* CHALLENGE 9 *----------
#Write a program that will ask for a number of days and then will show how many hours, minutes and seconds are in that number of days.

#youAsk =  int(input("Write a number of days: "))

#hoursInDay = 24
#minutesInHour = 60
#secinMinute = 60

#minutesInDay = minutesInHour * 24
#secInDay = secinMinute * minutesInDay

#print("Theres are",hoursInDay * youAsk,"hours,",minutesInDay * youAsk,"minutes and",secInDay * youAsk,"seconds." )


days = int(input("Enter the number of days: "))
hours = days*24
minutes = hours*60
seconds = minutes*60

print("In", days,"days there are...",hours,"hours",minutes,"minutes",seconds,"seconds.")