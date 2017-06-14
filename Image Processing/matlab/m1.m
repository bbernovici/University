%Bogdan Bernovici
%Ex 1

% Se presupune ca imaginea noastra are 100 de pixeli, adica matrice de
% 10x10
img = zeros(10);

%punem background alb imaginii
for i=1:10
    for j=1:10
        img(i,j)= 255;
    end
end
 
%plasam primul obiect (35% de black)
for i=1:5
    for j=1:7
        img(i,j)= 0;
    end
end

%plasam al doilea obiect (10% de 60)
for i=6:7
    for j=1:5
        img(i,j)=60
    end
end

%plasam al treilea obiect (10% de 180)
for i=8:9
    for j=1:5
        img(i,j)=180
    end
end


%generarea histogramei
img = uint8(img); %in matlab matricea e double default, si imi trebuie int
histo = imhist(img);
figure, plot(histo)

%afisam imaginea din matrice pe un scale de 256
figure,image(img),colormap(gray(256));

