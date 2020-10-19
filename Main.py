import pygame
import pygame.freetype
import random
import copy
import math 

from City import City

shortestPath = []
numberOfCities = 10
screen_width = 1080
screen_height = 720
FPS = 60
white = (255, 255, 255)
yellow = (255, 255, 0)
violet = (136, 78, 160)
backgroundColor = (0, 0, 0)

def main() :
    cities = []
    citiesOrder = []
    newCitiesOrder = []
    programFinished = False
    run = True
    numberOfCheckedPaths = 0
    shortestDistance = 1.7976931348623157e+308 

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height)) 
    font = pygame.freetype.Font("Montserrat-Regular.ttf", 24)
    
    generateCitiesLocation(cities, citiesOrder) 

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill(backgroundColor)

        if (programFinished == False) :
            newCitiesOrder = applyNewCitesOrderToCitiesList(cities, citiesOrder)

            currentDistance = calculateDistanceBetweenAllCities(newCitiesOrder) 
            shortestDistance = checkIfShortestPath(shortestDistance, currentDistance, newCitiesOrder)
            numberOfCheckedPaths += 1
            font.render_to(screen, (10, 10), "Current shortest path length: " + str(round(shortestDistance, 2)), white)
            font.render_to(screen, (10, 50), "Progress of checked paths: " + str(round(((numberOfCheckedPaths/math.factorial(len(citiesOrder) - 1)) * 100), 2)) + "%", white)

            drawCitiesLocations(pygame, screen, newCitiesOrder)
            drawCurrentCheckOrder(pygame, screen, newCitiesOrder)
            drawCurrentShortestPath(pygame, screen, shortestPath, newCitiesOrder)

            citiesOrder, programFinished = createNextPermutationOfCitiesList(citiesOrder, programFinished)

            pygame.display.update()

def drawCitiesLocations(pygame, screen, newCitiesOrder) :
    for n in range (1, len(newCitiesOrder)) :
        pygame.draw.circle(screen, white, (newCitiesOrder[n].x, newCitiesOrder[n].y), 4)
    pygame.draw.circle(screen, yellow, (newCitiesOrder[0].x, newCitiesOrder[0].y), 4)

def drawCurrentCheckOrder(pygame, screen, newCitiesOrder) :
    for n in range (len(newCitiesOrder) - 1) :
        pygame.draw.line(screen, white, (newCitiesOrder[n].x, newCitiesOrder[n].y), (newCitiesOrder[n + 1].x, newCitiesOrder[n + 1].y))
    pygame.draw.line(screen, white, (newCitiesOrder[0].x, newCitiesOrder[0].y), (newCitiesOrder[len(newCitiesOrder) - 1].x, newCitiesOrder[len(newCitiesOrder) - 1].y))

def drawCurrentShortestPath(pygame, screen, shortestPath, newCitiesOrder) :
    for n in range (len(shortestPath) - 1) :
        pygame.draw.line(screen, violet, (shortestPath[n].x, shortestPath[n].y), (shortestPath[n + 1].x, shortestPath[n + 1].y), 3)
    pygame.draw.line(screen, violet, (shortestPath[0].x, shortestPath[0].y), (shortestPath[len(newCitiesOrder) -1].x, shortestPath[len(newCitiesOrder) - 1].y), 3)

def createNextPermutationOfCitiesList(citiesOrder, programFinished) :
    largestX = -1
    
    largestY = -1
    for n in range (1, len(citiesOrder) - 1) :
        if (citiesOrder[n] < citiesOrder[n + 1]) :
            largestX = n

    if (largestX == -1) : 
        programFinished = True

    for y in range ( largestX, len(citiesOrder)) :
        if (citiesOrder[largestX] < citiesOrder[y]) :
            largestY = y

    swap(citiesOrder, largestX, largestY)

    endArray = citiesOrder[largestX + 1: ]
    endArray.reverse()
    citiesOrder =  citiesOrder[0 : largestX + 1] + endArray

    return citiesOrder, programFinished

def applyNewCitesOrderToCitiesList(cities, citiesOrder) :
    newCityListOrder = []
    for n in citiesOrder :
        newCityListOrder.append(cities[n])
    
    return newCityListOrder

def generateCitiesLocation(citiesList, citiesOrder) :
    for cityNumber in range (numberOfCities) :
        x = random.randint(70, screen_width - 70)
        y = random.randint(70, screen_height - 70)
        createCity(citiesList, x, y)
        citiesOrder.append(cityNumber)

def createCity(citiesList, x, y) :
    citiesList.append(City(x, y))

def calculateDistanceBetweenAllCities(cities_list) :
    distance = 0
    totalDistance = 0
    for n in range (len(cities_list) - 1) :
        distance = ((cities_list[n].x - cities_list[n + 1].x) ** 2 + (cities_list[n].y - cities_list[n + 1].y) ** 2) ** 0.5
        totalDistance += distance
    returnRoute = ((cities_list[0].x - cities_list[len(cities_list) - 1].x) ** 2 + (cities_list[0].y - cities_list[len(cities_list) - 1].y) ** 2) ** 0.5
    totalDistance += returnRoute
    return totalDistance


def checkIfShortestPath(savedShortestPath, currentPath, newCitiesOrder) :
    if (currentPath < savedShortestPath) :
        global shortestPath 
        shortestPath = copy.deepcopy(newCitiesOrder)
        return currentPath
    else:
        return savedShortestPath

def swap(cities_list, i, j) :
    temp = cities_list[i]
    cities_list[i] = cities_list[j]
    cities_list[j] = temp

main()