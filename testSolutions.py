print('Degree: ', graph.get_degree('1'))

# solutions at nossoHeuristics_GT

# gahuku.net / lambda = 0.5 / density 24.238095
solution.add_communities(
    [[16], [5, 14], [3, 4, 6, 7, 8, 11, 12], [9, 10, 13], [1, 2], [15]]
)

# signedZhao.net
com1 = numpy.array([0, 1, 3, 4, 5, 6, 7, 8, 9]) + 1
com2 = numpy.array([2, 15, 20, 21, 22, 23, 25, 26, 27, 28, 29]) + 1
com3 = numpy.array([10, 11, 12, 14, 16, 17, 18, 19]) + 1
com4 = numpy.array([13, 30, 31, 32, 33, 35, 36, 37, 38, 39]) + 1
com5 = numpy.array([24, 34, 48]) + 1
com6 = numpy.array([40, 41, 42, 43, 44, 45, 46, 47, 49]) + 1

x = [list(com1), list(com2), list(com3), list(
    com4), list(com5), list(com6)]
solution.add_communities(x)

# parlamento.net / lambda = 0.200000 / density 26.800000
solution.add_communities(
    [[10], [1, 3, 6, 8, 9], [2, 4, 5, 7]]
)

# parlamento.net / lambda = 0.500000 / density 24.238095
solution.add_communities(
    [[1,3,6,8,9],[10],[5],[7],[2,4]]
)

1-(-1)-2
1-(-1)-3
1-(-1)-4
1-(-1)-5
1-(1)-6
1-(-1)-7
1-(1)-8
1-(1)-9
1-(-1)-10
2-(-1)-3
2-(1)-4
2-(1)-5
2-(-1)-6
2-(1)-7
2-(-1)-8
2-(-1)-9
2-(1)-10
3-(-1)-4
3-(-1)-5
3-(1)-6
3-(-1)-7
3-(1)-8
3-(1)-9
3-(-1)-10
4-(1)-5
4-(-1)-6
4-(1)-7
4-(-1)-8
4-(-1)-9
4-(1)-1
5-(-1)-6
5-(1)-7
5-(-1)-8
5-(-1)-9
5-(-1)-10
6-(-1)-7
6-(1)-8
6-(1)-9
6-(-1)-10
7-(-1)-8
7-(-1)-9
7-(-1)-10
8-(1)-9
8-(-1)-10
9-(-1)-10


1-2
1-3
1-4
1-5
1-(1)-6
1-7
1-(1)-8
1-(1)-9
1-10
2-3
2-(1)-4
2-(1)-5
2-6
2-(1)-7
2-8
2-9
2-(1)-10
3-4
3-5
3-(1)-6
3-7
3-(1)-8
3-(1)-9
3-10
4-(1)-5
4-6
4-(1)-7
4-8
4-9
4-(1)-1
5-6
5-(1)-7
5-8
5-9
5-10
6-7
6-(1)-8
6-(1)-9
6-10
7-8
7-9
7-10
8-(1)-9
8-10
9-10

1-(0)-2
1-(0)-3
1-(0)-4
1-(0)-5
1-(1)-6
1-(0)-7
1-(1)-8
1-(1)-9
1-(0)-10
2-(0)-3
2-(1)-4
2-(1)-5
2-(0)-6
2-(1)-7
2-(0)-8
2-(0)-9
2-(1)-10
3-(0)-4
3-(0)-5
3-(1)-6
3-(0)-7
3-(1)-8
3-(1)-9
3-(0)-10
4-(1)-5
4-(0)-6
4-(1)-7
4-(0)-8
4-(0)-9
4-(1)-1
5-(0)-6
5-(1)-7
5-(0)-8
5-(0)-9
5-(0)-10
6-(0)-7
6-(1)-8
6-(1)-9
6-(0)-10
7-(0)-8
7-(0)-9
7-(0)-10
8-(1)-9
8-(0)-10
9-(0)-10

