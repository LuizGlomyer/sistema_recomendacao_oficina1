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
    denominador = sqrt(moduloX) * sqrt(moduloY)

    if denominador == 0:
        return 0
    similaridade = somaXY / denominador
    return similaridade


def calculatePearson(ratingsList, rating1, rating2):
    n = 0
    Sxy = 0
    Sx = 0
    Sy = 0

    Sx2 = 0  # somatorio x²
    Sy2 = 0
    for key in ratingsList:
        n += 1
        Sxy += rating1[key] * rating2[key]
        Sx += rating1[key]
        Sy += rating2[key]

        Sx2 += (rating1[key] ** 2)
        Sy2 += (rating2[key] ** 2)

    if n == 0:
        return 0

    numerador = Sxy - (Sx * Sy) / n
    denominador = sqrt(Sx2 - (Sx ** 2) / n) * sqrt(Sy2 - (Sy ** 2) / n)
    if denominador == 0:
        return 0

    valorPearson = numerador / denominador
    if valorPearson > 1:
        valorPearson = int(valorPearson)
    elif valorPearson < -1:
        valorPearson = int(valorPearson)
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
            distance += (rating1[key] - rating2[key]) ** 2
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
        return distance ** (1 / r)
    else:
        return -1


def computeNearestNeighbor(username, users, algoritmo):
    distances = []
    for user in users:  # para cada usuário da lista de usuários
        if user[2] != username:
            a = user[2]  # var de teste
            b = username
            if algoritmo == "manhattan":
                distance = manhattan(a, b)
                distances.append((distance, user))
            elif algoritmo == "distanciaEuclidiana":
                distance = distanciaEuclidiana(a, b)
                distances.append((distance, user))
            elif algoritmo == "pearson":
                distance = pearsonCorrelation(a, b)
                distances.append((distance, user))
            elif algoritmo == "cosseno":
                # CUIDADO, no cosseno os valores devem estar ordenados em ordem crescente, nos outros algoritmos em ordem decrescente
                distance = similaridadeCosseno(a, b)
                distances.append((distance, user))

    distances.sort()
    if algoritmo == 'manhattan':
        distances = list(filter(lambda d: d[0] != -1, distances))
    elif algoritmo == 'distanciaEuclidiana':
        distances = list(filter(lambda d: d[0] != -1, distances))
    elif algoritmo == 'pearson':
        distances = list(filter(lambda d: d[0] != 0, distances))
        distances.reverse()
    elif algoritmo == 'cosseno':
        distances.reverse()
        distances = list(filter(lambda d: d[0] != 0, distances))

    for rating in distances:
        print(rating[0])
    return distances   #retorna uma lista ordenada contendo todos os usuários e suas distâncias para o usuário a quem se quer recomendar


def recommend(username, users, algoritmo):
    nearest = computeNearestNeighbor(username[2], users, algoritmo)  # vizinhos mais próximos, retorna uma tupla com o grau de similaridade [0] e o usuário a que se refere [1]
    recommendations = []
    while len(recommendations) < 5:  #mínimo de 5 recomendações
        for usuario in nearest:
            avaliacoes = list(usuario[1][2].items()) # convertendo dict em lista
            avaliacoes.sort(key=lambda a: a[1], reverse=True) # diz para ordenar em ordem decrescente com base no segundo elemento da lista
            for avaliacao in avaliacoes:
                if len(recommendations) < 5 and avaliacao[1] >= 7 and avaliacao[0] not in username[2]:
                    recommendations.append(avaliacao)
            #print(recommendations)

        break  # não conseguimos encher 5 recomendações, saímos do while

    return sorted(recommendations, key=lambda artistTuple: artistTuple[1],
                  reverse=True)  # retorne a lista com o conteúdo que foi recomendado
