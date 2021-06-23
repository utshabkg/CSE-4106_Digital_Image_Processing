function [pred11] = temporal_sptl2(D,c)
const=5;
[row,col]=size(D);
pred1=zeros(row+1,col+1);
pred11=zeros(row+1,col+1);

pred1(1,:)=const*ones(1,col+1);
pred1(2:row+1,1)=const*ones(row,1);

pred1(2:row+1,2:col+1)=D;

switch c

    case 1
        for i=2:row+1
            for j=2:col+1    
                pred11(i,j)=pred1(i-1,j);
            end
        end
    case 2
        for i=2:row+1
            for j=2:col+1    
                pred11(i,j)=pred1(i-1,j-1);
            end
        end
    case 3
        for i=2:row+1
            for j=2:col+1    
                pred11(i,j)=pred1(i,j-1);
            end
        end
 %(A+B)/2       
    case 4
        for i=2:row+1
            for j=2:col+1    
                pred11(i,j)=0.5*(pred1(i,j-1)+pred1(i-1,j));
            end
        end

%A+B-C
    case 5

        for i=2:row+1
            for j=2:col+1    
                pred11(i,j)=pred1(i,j-1)+pred1(i-1,j)-pred1(i-1,j-1);
            end
        end
        
%A+(B-C)/2
    case 6
         for i=2:row+1
            for j=2:col+1    
                pred11(i,j)=pred1(i,j-1)+((pred1(i-1,j)-pred1(i-1,j-1))*0.5);
            end
         end
         
%B+(A-C)/2
    case 7
          for i=2:row+1
            for j=2:col+1    
                pred11(i,j)=pred1(i-1,j)+((pred1(i,j-1)-pred1(i-1,j-1))*0.5);
            end
          end
          
 end
          
 

pred11=pred11(2:row+1,2:col+1);
pred11=D-fix(pred11);
pred11=double(pred11);
