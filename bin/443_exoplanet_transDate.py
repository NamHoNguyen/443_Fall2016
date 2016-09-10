import numpy as np

data = np.loadtxt('input/443_exoplanet.csv')
T = data[:,0]
T0 = data[:,1]
RA = data[:,2]
Dec = data[:,3]

# Midnight Sept 8, 16 and Oct 7, 16 at Stony Brook
Tmin = 2457640.67
Tmax = 2457669.67

#print data
rdj = []

for i in range(len(T)):
    index = 0
    while T0[i] < (Tmax-T[i]):
        T0[i] += T[i]
        # time at Stony Brook (EDT) - 4 hours behind UTC
        time = 24.*(T0[i]%1.)-4
        # Constrain mid-transit time from 10pm to 3am
        if (T0[i] > Tmin) and (time>=10) and (time<=15):
            if index == 0:
                print 'Row number: ',i+5
                index += 1
            #print T0[i]
            if len(rdj) == 0:
                rdj = np.array([RA[i],Dec[i],T0[i],i+5])
            else:
                rdj = np.vstack([rdj,[RA[i],Dec[i],T0[i],i+5]])

np.savetxt('output/rdj.csv',rdj)
