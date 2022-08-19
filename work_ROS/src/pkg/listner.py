#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64
from math import sqrt

class Listner():
    def __init__(self):
        rospy.init_node('listner', anonymous=True)
        rospy.Subscriber('velocidade', Twist, self.callback)
        self.pub_linear = rospy.Publisher('modulo_linear', Float64, queue_size=10) #publicando em um tópico
        self.pub_angular = rospy.Publisher('modulo_angular', Float64, queue_size=10) #publicando em outro tópico
        
    def callback(self, msg):
        x_linear, y_linear, z_linear, x_angular, y_angular, z_angular = msg.linear.x, msg.linear.y, msg.linear.z, msg.angular.x, msg.angular.y, msg.angular.z
        modulo_linear = sqrt((x_linear**2)+(y_linear**2)+(z_linear**2))
        modulo_angular = sqrt((x_angular**2)+(y_angular**2)+(z_angular**2))
        f_linear = Float64()
        f_angular = Float64()
        f_linear.data = modulo_linear
        f_angular.data = modulo_angular
        rospy.loginfo(modulo_linear)
        rospy.loginfo(modulo_angular) #sei que nao precisa ficar printando isso na tela, mas da pra printar os dois juntos?
        self.pub_linear.publish(f_linear)
        self.pub_angular.publish(f_angular)
        
if __name__ == '__main__':
    l = Listner()
    rospy.spin()
        