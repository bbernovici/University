%Bogdan Bernovici
%Ex 2

%Am folosit Piecewise linear contrast stretching pentru problema aceasta
img = imread('tren.png');
imgGrey=rgb2gray(img);
figure,image(imgGrey),colormap(gray(256))

%Aici m-am jucat cu valorile pentru a elimina acel gri extrem
t1=20;
alpha=10;
t2=60;
beta=70;

[l,c]=size(imgGrey);
img_n=zeros(l,c);

%Am aplicat formula gasita in al doilea curs
for i=1:l
  for j=1:c
     u=imgGrey(i,j);
     if u<t1
        v=(alpha/t1)*u;
     end
     if u > t1 && u<t2
        v=alpha+((beta-alpha)/t2-t1)*(u-t1);
     else
        v=beta+((alpha-1-beta)/(alpha-1-t2))*(u-t2);
     end 
     img_n(i,j)=v;
 end
end

figure,image(img_n),colormap(gray(256))