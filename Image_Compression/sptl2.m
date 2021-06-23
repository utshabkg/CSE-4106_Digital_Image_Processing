function [pred11] = sptl2(D)
const=10;
[row,col]=size(D);
pred1=zeros(row+1,col+1);
pred11=zeros(row+1,col+1);

pred1(1,:)=const*ones(1,col+1);
pred1(2:row+1,1)=const*ones(row,1);

pred1(2:row+1,2:col+1)=D;

for i=2:row+1
  for j=2:col+1    
        pred11(i,j)=0.5*(pred1(i,j-1)+pred1(i-1,j));
  end
end

pred11=pred11(2:row+1,2:col+1);
pred11=D-fix(pred11);



