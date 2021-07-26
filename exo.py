
from threading import Thread, Condition
import time
import random
import sched, time
le_sched = sched.scheduler(time.time, time.sleep)

la_queue = []
memoire_partage=int(input("Entrer la taille de la memoire: "))
producteur=int(input("Entrer le nombre de producteur: "))
consommateur=int(input("Entrer le nombre de consommateur: "))

nb_pro=0
nb_cons=0
condition = Condition()

class Producteur(Thread):
    def run(self):
        numeros = range(10)
        global la_queue
    
        while True:
            def product(sc):

                condition.acquire()
                if len(la_queue) == memoire_partage:
                    condition.wait()
                    
                else:

                    num = random.choice(numeros)
                    la_queue.append(num)
                condition.notify()
                condition.release()
                time.sleep(random.random())

                le_sched.enter(2, 1, product, (sc,))
            le_sched.enter(2, 1, product, (le_sched,))
            le_sched.run()



class Consomateur(Thread):
    def run(self):
        global queue
        
        while True:
            def consomme(sc): 
                condition.acquire()
                if not la_queue:
                    condition.wait()
                num = la_queue.pop(0)
                condition.notify()
                condition.release()
                time.sleep(random.random())
                le_sched.enter(6, 1, consomme, (sc,))
            le_sched.enter(6, 1, consomme, (le_sched,))
            le_sched.run()


while nb_pro<producteur:
    Producteur().start()
    nb_pro=nb_pro+1

while nb_cons<consommateur:
    Consomateur().start()
    nb_cons=nb_cons+1

def print_la_queu(sc): 
    global la_queue
    print(la_queue)
    le_sched.enter(1, 1, print_la_queu, (sc,))
le_sched.enter(1, 1, print_la_queu, (le_sched,))
le_sched.run()