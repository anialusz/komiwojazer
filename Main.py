import pygame
import random
import copy

from City import City

cities = []
shortestPath = []
numberOfCities = 10
screen_width = 720
screen_height = 480


white = (255, 255, 255)
violet = (136, 78, 160)
background = (0, 0, 0)

def main() :
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height)) 
    FPS = 60
    generateCitiesLocation() 
    
    shortestDistance = 1641726468125

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill(background)

        currentDistance = calculateDistanceBetweenAllCities(cities) 
        shortestDistance = checkIfShortestPath(shortestDistance, currentDistance)

  ##      print(shortestDistance)
        for n in range (len(cities)) :
            pygame.draw.circle(screen, white, (cities[n].x, cities[n].y), 4)
        
        for n in range (len(cities) - 1) :
            pygame.draw.line(screen, white, (cities[n].x, cities[n].y), (cities[n + 1].x, cities[n + 1].y))

        for n in range (len(shortestPath) - 1) :
            pygame.draw.line(screen, violet, (shortestPath[n].x, shortestPath[n].y), (shortestPath[n + 1].x, shortestPath[n + 1].y), 3)

        pygame.display.update()

        i = random.randrange(0, numberOfCities)
        j = random.randrange(0, numberOfCities)
        swap(cities, i, j)

def generateCitiesLocation() :
    for city in range (numberOfCities) :
        x = random.randint(50, screen_width - 50)
        y = random.randint(50, screen_height - 50)
        createCity(x,y)

def createCity(x, y) :
    cities.append(City(x, y))


def calculateDistanceBetweenAllCities(cities_list) :
    distance = 0
    totalDistance = 0
    for n in range (len(cities_list) - 1) :
        distance = ((cities[n].x - cities[n + 1].x) ** 2 + (cities[n].y - cities[n + 1].y) ** 2) ** 0.5
        totalDistance += distance
    return totalDistance

def swap(cities_list, i, j) :
    temp = cities_list[i]
    cities_list[i] = cities_list[j]
    cities_list[j] = temp


def checkIfShortestPath(savedShortestPath, currentPath) :
    if (currentPath < savedShortestPath) :
        global shortestPath 
        shortestPath = copy.deepcopy(cities)
        print(currentPath)
        return currentPath
    else:
        return savedShortestPath


main()