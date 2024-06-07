# Ejercicio 2.
y = (0.10**2 - 0.05**2)**0.5
Q = [
    [2E-6,-0.05,0,0],
    [-8E-6,0,y,0],
    [12E-6,0.05,0,0],
]
Ef(0,0,0,Q)
# -36 + 9.6

em.plotEf(Ef, Q, dx=0.15, figsize=(6,6), density=1.5, title='Líneas de campo prob. 11.9')

print("E =",np.round(np.array(Ef(-0.0895,-0.0081,0,Q))/1000000, decimals=2)," x10^6 C")

print("E =",np.round(np.array(Ef(-0.085804565,0.05,0,Q))/1000000, decimals=0)," x10^6 C")