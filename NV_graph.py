import numpy as np
import matplotlib.pylab as plt
Sol=np.genfromtxt('advection.txt')
times=np.zeros(5)
index=Sol[:,0]==times[0]
s='Tiempo= '+str(times[0])+'s'
plt.plot(Sol[index,1],Sol[index,2],label=s)
for i in range(1,5):
    rand=np.random.random_integers(0,len(Sol[:,0]))
    if(Sol[rand,0]in times):
        rand=np.random.random_integers(0,len(Sol[:,0]))
    else:
        times[i]=Sol[rand,0]
        index=Sol[:,0]==times[i]
        s='Tiempo= '+str(times[i])+'s'
        plt.plot(Sol[index,1],Sol[index,2],label=s)
plt.legend()
plt.xlabel('Posición')
plt.ylabel('Amplitud')
plt.title("solución ecuació de advección")
plt.savefig('escalon.png')
