from math import sqrt

def similaridadeCosseno(rating1, rating2):
    somaXY = 0
    moduloX = 0
    moduloY = 0

    for key in rating1:
        moduloX += rating1[key] ** 2
    for key in rating2:
        moduloY += rating2[key] ** 2

    for key in rating1:
        if key in rating2:
            somaXY += rating1[key] * rating2[key]
    similaridade = somaXY/(sqrt(moduloX) * sqrt(moduloY)),8
    return similaridade


def calculatePearson(ratingsList, rating1, rating2):
    n = 0
    Sxy = 0
    Sx = 0
    Sy = 0

    Sx2 = 0 # somatorio x²
    Sy2 = 0
    for key in ratingsList:
        n += 1
        Sxy += rating1[key] * rating2[key]
        Sx += rating1[key]
        Sy += rating2[key]

        Sx2 += (rating1[key] ** 2)
        Sy2 += (rating2[key] ** 2)


    numerador = Sxy - (Sx * Sy)/n
    denominador = sqrt(Sx2 - (Sx**2)/n) * sqrt(Sy2 - (Sy**2)/n)

    if denominador == 0 or n == 0:
        return 0

    valorPearson = numerador/denominador
    return valorPearson


def pearsonCorrelation(rating1, rating2):
    ratingsList = []
    for key in rating1:
        if key in rating2:
            ratingsList.append(key)
    return calculatePearson(ratingsList, rating1, rating2)


def manhattan(rating1, rating2):
    """Computes the Manhattan distance. Both rating1 and rating2 are dictionaries
       of the form {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}"""
    distance = 0
    commonRatings = False
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key])
            commonRatings = True
    if commonRatings:
        return distance
    else:
        return -1  # Indicates no ratings in common

def distanciaEuclidiana(rating1, rating2):
    distance = 0
    commonRatings = False
    for key in rating1:
        if key in rating2:
            distance += (rating1[key] - rating2[key])**2
            commonRatings = True
    if commonRatings:
        return sqrt(distance)
    else:
        return -1

def distanciaMinkowski(rating1, rating2, r):
    distance = 0
    commonRatings = False
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key]) ** r
            commonRatings = True
    if commonRatings:
        return distance**(1/r)
    else:
        return -1

def computeNearestNeighbor(username, users):
    """creates a sorted list of users based on their distance to username"""
    distances = []
    for user in users: # para cada usuário da lista de usuários
        if user != username:
            distance = similaridadeCosseno(users[user], users[username])  # calcule a distância
            distances.append((distance, user))
    # sort based on distance -- closest first
    distances.sort()
    return distances  # retorna uma lista ordenada contendo todos os usuários e suas distâncias para o usuário a quem se quer recomendar

def recommend(username, users):
    """Give list of recommendations"""
    # first find nearest neighbor
    nearest = computeNearestNeighbor(username, users)[0][1]  # vizinho mais próximo

    recommendations = []
    # now find bands neighbor rated that user didn't
    neighborRatings = users[nearest]  # avaliações do vizinho
    userRatings = users[username]  # avaliações do usuário
    for artist in neighborRatings: # para cada conteúdo que foi avaliado pelo vizinho
        if not artist in userRatings:  # se este conteúdo não foi avaliado pelo usuário, recomende-o
            recommendations.append((artist, neighborRatings[artist]))
    # using the fn sorted for variety - sort is more efficient
    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)  # retorne a lista com o conteúdo que foi recomendado
