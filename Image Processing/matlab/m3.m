%Bogdan Bernovici
%Ex 3


matrix = [
    [3*sqrt(2)/2, 3*sqrt(2)/2, 20]
    [-sqrt(2)/6, sqrt(2)/6, 10]
    [0, 0, 1]]

x0 = matrix(1,3)

y0 = matrix(2,3)

beta = sqrt(matrix(2,1)^2 + matrix(2,2)^2) % rezultat: 1/3

alfa = (beta/matrix(2,1)) * (matrix(1,2) - matrix(2,2)) % rezultat -48/18

angle = -atan(matrix(2,1)/matrix(2,2))




