function [pred11] = loco_i(Data)
const=50;
[row,col]=size(Data);
pred1=zeros(row+1,col+1);
pred11=zeros(row+1,col+1);

pred1(1,:)=const*ones(1,col+1);
pred1(2:row+1,1)=const*ones(row,1);

pred1(2:row+1,2:col+1)=Data;

for i=2:row+1
  for j=2:col+1    
        if(pred1(i-1,j-1)>=max(pred1(i,j-1),pred1(i-1,j)))
        pred11(i,j)=min(pred1(i,j-1),pred1(i-1,j));
        elseif(pred1(i-1,j-1)<=min(pred1(i,j-1),pred1(i-1,j)))
        pred11(i,j)=max(pred1(i,j-1),pred1(i-1,j));        
        else
        pred11(i,j)=pred1(i,j-1)+pred1(i-1,j)-pred1(i-1,j-1);            
        end
  end
end

pred11=pred11(2:row+1,2:col+1);
pred11=int64(pred11);
pred11=double(pred11);