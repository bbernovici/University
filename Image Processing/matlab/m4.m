%Bogdan Bernovici
%Ex 4

img = zeros(30,11);
for i=1:30
    for j=1:11
        img(i,j) = 255;
    end
end

%construirea imaginii A din figura
img(6,4) = 160;
img(7,4:5) = 160; 
img(8,3:6) = 160;
img(9,3:8) = 160;
img(10, 4:8) = 160;
img(11, 4:8) = 160;
img(12, 4:8) = 160;
img(13, 3:8) = 160;
img(14, 3:8) = 160;
img(15, 3:8) = 160;
img(16, 3:8) = 160;
img(17, 3:9) = 160;
img(18, 4) = 160; img(18, 6:7) = 160;
img(19, 4) = 160; img(19, 6:7) = 160;
img(20, 4) = 160; img(20, 6:7) = 160;
img(21, 6:7) = 160;
img(22, 7) = 160;
img(23, 7) = 160;

%construirea elementului structural B
struct = zeros(3);
for i=1:3
    for j=1:3
        struct(i,j) = 255;
    end
end
struct(1,2) = 160;
struct(2,1) = 160;
struct(3,2) = 160;
struct(2,3) = 160;
struct(2,2) = 200;
%functia de eroziune a imaginii A cu elementul structural B
img_eroded = img;
%adaug 1 rand pe abele parti laterale ale matricei
%img = padarray(img, [0, 1], 1)
[l,c] = size(img);
win = zeros(1,9);
for i=2:l-1
    for j=2:c-1
        
        %adun toti vecinii
        win(1) = img(i-1, j-1);
        win(2) = img(i, j-1);
        win(3) = img(i+1, j-1);
        win(4) = img(i-1, j);
        win(5) = img(i, j);
        win(6) = img(i+1, j);
        win(7) = img(i-1, j+1);
        win(8) = img(i, j+1);
        win(9) = img(i+1, j+1);
        
        %transorm din vector in matrice sa o pot compara mai tarziu
        win = reshape(win, [3,3]);
        %presupun ca elementul structural se potriveste
        ok = 1;
        for k=1:3
            for l=1:3
                %daca punctul de pe elem str este 160 atunci
                if struct(k,l) == 160
                    %daca punctul de pe fereastra ce coincide este diferit
                    if win(k,l) ~= 160
                        %elementul structural nu se potriveste, anulam tot
                        ok = 0;
                    end
                end
            end
        end
        
        %in cazul in care cele doua coincid atunci actualizam matricea
        %erodata
        if ok == 1 
            img_eroded(i,j) = 160;
        else 
            if img_eroded(i,j) == 160
                img_eroded(i,j) = 0; %aratam erodarea cu negru
            else 
                img_eroded(i,j) = 255;
            end
        end
    end
end
                    
figure, image(img), colormap(gray(256))
figure, image(struct), colormap(gray(256))
figure, image(img_eroded), colormap(gray(256))