# sistema_recomendacao_oficina1

Sistema de recomendação de jogos. Com apoio de um dataset obtido na internet geramos uma lista de usuários e suas avaliações, aleatoriamente. Após isso aplicamos algoritmos como Distância de Manhattan/Euclidiana, Correlação de Pearson e Similaridade do Cosseno para inferirmos o usuário mais similar e apartir daí recomendarmos o jogo que mais se adequa ao usuário em questão. 

O algoritmo usado num sistema de recomendação depende da natureza dos dados. Como a lista de avaliações é uma matriz esparsa a melhor métrica é a Similaridade do Cosseno. Manhattan e Euclides dão uma acurácia mediana e Pearson não produz resultados satisfatórios. 

Datasets usados:
https://www.kaggle.com/gregorut/videogamesales
https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings/
