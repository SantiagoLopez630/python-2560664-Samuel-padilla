import random
vec=[]
for i in range(random.randint(10,25)):
        vec.insert(i,round(random.random()*100))
        for k in range(len(vec)):
            for j in range (i+1, len(vec)):
                if vec[k]>vec[j]:
                    aux=vec[k]
                    vec[k]=vec[j]
                    vec[j]=aux
                    print(vec[i])
                    print(vec[k])
                    print(vec[j])
                  