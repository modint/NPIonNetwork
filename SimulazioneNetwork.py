import networkx as nx
import EoN
import matplotlib.pyplot as plt

N= 10**4#numero di individui nella popolazione considerata

kF = 19 ##numero di contatti medi nella popolazione (fonte: Mossong et al)
kC=5 #numero di contatti con misure di distanziamento sociale

I0= 0.001 #frazione popolazione infettata al tempo zero

beta= 0.4 #transmission rate
gamma=1.0 #recovery rate
betaC=0.3 #transmission rate con mascherine etc

GL=nx.barabasi_albert_graph(N, kF)  #crea Grafo Albert Barabasi hp no restrizioni
GC=nx.barabasi_albert_graph(N, kC) #idem ma grado diminuisce per restrizioni


#simulazione sui due network di diffusione contagio modello SIR con ic I0
#La simulazione è fatta con Gillespie_SIR (si veda documentazione EoN). Esistono alternative come fast_SIR
t, S, I, R= EoN.Gillespie_SIR(GL, beta, gamma, rho=I0)
t1, S1, I1, R1= EoN.Gillespie_SIR(GC, beta, gamma, rho=I0)
t2, S2, I2, R2= EoN.Gillespie_SIR(GL, betaC, gamma, rho=I0)
t3, S3, I3, R3= EoN.Gillespie_SIR(GC, betaC, gamma, rho=I0)

#grafico della simulazione

plt.plot(t, I, label="Dinamica libera del virus")
plt.plot(t1, I1, label= "Con distanziamento")
plt.plot(t2, I2, label= "Con dispositivi di protezione")
plt.plot(t3, I3, label= "Con dispositivi di protezione e distanziamento")
plt.xlabel("$tempo$")
plt.ylabel("$Infetti$")
plt.legend()
plt.show()

