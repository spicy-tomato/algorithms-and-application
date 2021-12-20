import random

class PSO:
    def __init__(self,a,b,c,d,s):
        self._a = a
        self._b = b
        self._c = c
        self._d = d
        self._s = s

        self.vel = [[],[],[],[]]
        self.newSwarm = [[],[],[],[]]
        self.localSwarm = [[],[],[],[]]

        self.newFitness = []           #fit moi
        self.localFitness = []          #fit cu

        self.gb = []                  #toan cuc
        self.pb = [[],[],[],[]]       #cuc bo

    def khoitao(self):
        for item in range(0,4):
            for i in range(0,4):
                self.vel[item].insert(i,random.uniform(1,21))
                self.localSwarm[item].insert(i,random.randrange(1,21))

        self.pb = list(self.localSwarm)

    def khoitaofit(self):
        for item in range(0,4):
            T = self._a*self.localSwarm[item][0] + self._b*self.localSwarm[item][1] + self._c*self.localSwarm[item][2] + self._d*self.localSwarm[item][3]
            self.localFitness.insert(item,abs(T-self._s))

    def timFit(self):
        self.newFitness = []
        for item in range(0,4):
            T = self._a*self.newSwarm[item][0] + self._b*self.newSwarm[item][1] + self._c*self.newSwarm[item][2] + self._d*self.newSwarm[item][3]
            self.newFitness.insert(item,abs(T-self._s))

    def updateBetterFitSwarm(self):
        for item in range(0,4):
            if(self.localFitness[item]>self.newFitness[item]):
                self.localFitness[item] = self.newFitness[item]
                self.localSwarm[item] = list(self.newSwarm[item])
                self.pb[item] = self.newSwarm[item]

    def timGb(self):
        for item in range(0,4):
            if(self.localFitness[item]==min(self.localFitness)):
                self.gb = self.localSwarm[item]

    def updateParticle(self):
        self.newSwarm = [[],[],[],[]]

        for item in range(0,4):
            for i in range(0,4):
                w = 0.7
                c1 = c2 = 1.5
                r1 = random.uniform(-1,1)
                r2 = random.uniform(-1,1)
                x = self.localSwarm[item][i]
                Pb = self.pb[item][i]
                Gb = self.gb[i]
                self.vel[item][i] = w * self.vel[item][i] + c1*r1*(Pb-x) + c2*r2*(Gb-x)
                self.newSwarm[item].insert(i,round(x + self.vel[item][i],0))

                while((0<=self.newSwarm[item][i]<=20)==False):          # bien nam ngoai pvi [0,20]
                    r1 = random.uniform(-1,1)
                    r2 = random.uniform(-1,1)
                    self.vel[item][i] = w * self.vel[item][i] + c1*r1*(Pb-x) + c2*r2*(Gb-x)
                    self.newSwarm[item][i] = x + self.vel[item][i]


    def main(self):
        self.khoitao()
        self.khoitaofit()
        self.timGb()

        while( 0 not in self.localFitness):
            self.updateParticle()
            self.timFit()
            self.updateBetterFitSwarm()
        self.timGb()
        print(self.gb)

a = PSO(3,2,1,1,34)
a.main()


