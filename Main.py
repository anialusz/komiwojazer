import pygame
import pygame.freetype
import random
import copy
import math 
import sys

from City import City

shortestPath = []
numberOfCities = 10
screen_width = 1080
screen_height = 720
white = (255, 255, 255)
yellow = (255, 255, 0)
violet = (136, 78, 160)
backgroundColor = (0, 0, 0)

def main() :
    citiesList = []
    citiesOrder = []
    programFinished = False
    run = True
    numberOfCheckedPaths = 0
    shortestDistance = 1.7976931348623157e+308 

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height)) 
    font = pygame.freetype.Font("Montserrat-Regular.ttf", 24)
    
    generateCitiesLocation(citiesList, citiesOrder) 

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill(backgroundColor)

        if (programFinished == False) :
            citiesList = applyNewCitesOrderToCitiesList(citiesList, citiesOrder)

            currentDistance = calculateDistanceBetweenAllCities(citiesList) 
            shortestDistance = checkIfShortestPath(shortestDistance, currentDistance, citiesList)
            numberOfCheckedPaths += 1
            font.render_to(screen, (10, 10), "Current shortest path length: " + str(round(shortestDistance, 2)), white)
            font.render_to(screen, (10, 50), "Progress of checked paths: " + str(round(((numberOfCheckedPaths/math.factorial(len(citiesOrder) - 1)) * 100), 2)) + "%", white)

            drawCitiesLocations(pygame, screen, citiesList)
            drawCurrentCheckOrder(pygame, screen, citiesList)
            drawCurrentShortestPath(pygame, screen, shortestPath, citiesList)

            citiesOrder, programFinished = createNextPermutationOfCitiesList(citiesOrder, programFinished)

            pygame.display.update()

def drawCitiesLocations(pygame, screen, citiesList) :
    for n in range (1, len(citiesList)) :
        pygame.draw.circle(screen, white, (citiesList[n].x, citiesList[n].y), 4)
    pygame.draw.circle(screen, yellow, (citiesList[0].x, citiesList[0].y), 4)

def drawCurrentCheckOrder(pygame, screen, citiesList) :
    for n in range (len(citiesList) - 1) :
        pygame.draw.line(screen, white, (citiesList[n].x, citiesList[n].y), (citiesList[n + 1].x, citiesList[n + 1].y))
    pygame.draw.line(screen, white, (citiesList[0].x, citiesList[0].y), (citiesList[len(citiesList) - 1].x, citiesList[len(citiesList) - 1].y))

def drawCurrentShortestPath(pygame, screen, shortestPath, citiesList) :
    for n in range (len(shortestPath) - 1) :
        pygame.draw.line(screen, violet, (shortestPath[n].x, shortestPath[n].y), (shortestPath[n + 1].x, shortestPath[n + 1].y), 3)
    pygame.draw.line(screen, violet, (shortestPath[0].x, shortestPath[0].y), (shortestPath[len(citiesList) -1].x, shortestPath[len(citiesList) - 1].y), 3)

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

def applyNewCitesOrderToCitiesList(citiesList, citiesOrder) :
    newCityList = []
    for n in citiesOrder :
        newCityList.append(citiesList[n])
    
    return newCityList

def generateCitiesLocation(citiesList, citiesOrder) :
    screenOffset = 70
    for cityNumber in range (numberOfCities) :
        x = random.randint(screenOffset, screen_width - screenOffset)
        y = random.randint(screenOffset, screen_height - screenOffset)
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

def checkIfShortestPath(savedShortestPath, currentPath, citiesList) :
    if (currentPath < savedShortestPath) :
        global shortestPath 
        shortestPath = copy.deepcopy(citiesList)
        return currentPath
    else:
        return savedShortestPath

def swap(cities_list, i, j) :
    temp = cities_list[i]
    cities_list[i] = cities_list[j]
    cities_list[j] = temp

main()