city_name = "Istanbul, Turkey"
populations = [[1927,1950,2000,2017],[691000,983000,8831800,15029231]]

def change(past, present):
  change = present - past
  return change

def percent_growth(pastPop, presentPop):
  percentage = (change(pastPop, presentPop)/pastPop) * 100
  return percentage

def annual_growth (pastYear, pastPop, presentYear, presentPop):
  percent = percent_growth(pastPop, presentPop)
  years = change(pastYear, presentYear)
  annual = percent / years
  return annual

percent_gr = percent_growth(populations[1][0], populations[1][3])
print(percent_gr)

annual_grtot = annual_growth(populations[0][0],populations[1][0], populations[0][3], populations[1][3])


annual_gr1 = annual_growth(populations[0][0],populations[1][0], populations[0][1], populations[1][1])

annual_gr2 = annual_growth(populations[0][1],populations[1][1], populations[0][2], populations[1][2])

annual_gr3 = annual_growth(populations[0][2],populations[1][2], populations[0][3], populations[1][3])

print("The population growth of Turkey appears to be slowing down after its high period of growth in the late 90's. Using a few data points from between", populations[0][0], "and", populations[0][3], "we have found the annual population growth between different periods of time.")
print("It is clear that Turkey's population has increased between", populations[0][0], "and", populations[0][3], "based solely on the country's population during those two years", populations[1][0], "and", populations[1][3], "respectively. Taking the average annual population growth rate between these two years gives a growth of", annual_grtot, "However, the average doesn't give the full picture. If you take smaller pictures of this growth. We chose the years of", populations[0][0], ",", populations[0][1], ",", populations[0][2], ",and", populations[0][3], "The population growth between each of these years becomes more clear:", annual_gr1, ",", annual_gr2, ",", annual_gr3, ". This shows that there are less new people in the country compared to the amount that are already there. Any positive value indicates an increase, so this only indicates a slow in the country's positive growth that hasn't even reduced below the levels from the early 90's.")
