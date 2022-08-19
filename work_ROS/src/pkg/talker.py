#!/usr/bin/env python3




import rospy
from geometry_msgs.msg import Twist #importando o tipo de mensagem que será utilizado
import random

class Talker:
    def __init__(self):
        rospy.init_node('vel', anonymous=True) #inicializa o nó, tem que ter no programa
        self.pub = rospy.Publisher('velocidade', Twist, queue_size = 10) #se inscreve em um tópico (o publisher publica em um tópico)
        self.list = list(range(100))

    def velocidade(self):
        rate = rospy.Rate(5)
        while not rospy.is_shutdown():
            v = Twist()
            v.linear.x = random.choice(self.list) #Declarando as variáveis de velocidade 
            v.linear.y = random.choice(self.list)
            v.linear.z = random.choice(self.list)
            v.angular.x = random.choice(self.list)
            v.angular.y = random.choice(self.list)
            v.angular.z = random.choice(self.list)
            rospy.loginfo(v)
            self.pub.publish(v)
            rate.sleep() #respeitar o rate definido anteriormente

if __name__ == '__main__':
    try:
        t = Talker()
        t.velocidade()
    except rospy.ROSInterruptException:
        pass
    
