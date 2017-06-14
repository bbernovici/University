%Bogdan Bernovici
%Ex 5

%Metoda prin care folosesc functia built-in din Matlab pentru median
img = zeros(9);
for i=4:6
    for j=4:6
        img(i,j) = 30;
    end
end

img_median = medfilt2(img) %rezultatul

%Metoda facuta de mine fara medfilt2
img_median_second = img;
%folosesc un window de 3x3 pe care il sortez mai tarziu si iau medianul
win = zeros(1,9)
[l,c] = size(img);
for i=2:l-1
    for j=2:c-1
        %adun toti vecinii
        win(1) = img(j-1, i-1);
        win(2) = img(j, i-1);
        win(3) = img(j+1, i-1);
        win(4) = img(j-1, i);
        win(5) = img(j, i);
        win(6) = img(j+1, i);
        win(7) = img(j-1, i+1);
        win(8) = img(j, i+1);
        win(9) = img(j+1, i+1);
        
        win = sort(win); %functia de sortare
        img_median_second(i,j) = win(5);
    end
end
img_median_second %rezultatul

%Metoda pentru average filter
img_average = img;
%folosesc un window de 3x3 pe care il sortez mai tarziu si iau averageul
win = zeros(1,9);
[l,c] = size(img);
for i=2:l-1
    for j=2:c-1
        %adun toti vecinii
        win(1) = img(j-1, i-1);
        win(2) = img(j, i-1);
        win(3) = img(j+1, i-1);
        win(4) = img(j-1, i);
        win(5) = img(j, i);
        win(6) = img(j+1, i);
        win(7) = img(j-1, i+1);
        win(8) = img(j, i+1);
        win(9) = img(j+1, i+1);
        
        avg = mean(win) %functia de average pt window
        img_average(i,j) = avg;
    end
end
img_average %rezultatul

figure, image(img), colormap(gray(256)) %initiala
figure, image(img_median_second), colormap(gray(256)) %median
figure, image(img_average), colormap(gray(256)) %average