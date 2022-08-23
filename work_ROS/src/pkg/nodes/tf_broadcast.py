#!/usr/bin/env python3
import rospy
import tf2_ros
import geometry_msgs.msg
import math

def handle_planet_pose (astro, parent, raio_astro, tempo):

    br = tf2_ros.TransformBroadcaster() #instanciando para publicar (boradcast)
    t = geometry_msgs.msg.TransformStamped() #instanciando a mensgame que vai ser utilizada
    #prenchendo a mensagem
    t.header.stamp = rospy.Time.now() 
    t.header.frame_id = parent
    t.child_frame_id = astro

    #instanciando as datas da msg
    t.transform.translation.x = raio_astro * math.sin(tempo)
    t.transform.translation.y = raio_astro * math.cos(tempo)
    t.transform.translation.z = 0.0
    t.transform.rotation.x = 0
    t.transform.rotation.y = 0
    t.transform.rotation.z = 0
    t.transform.rotation.w = 1

    br.sendTransform(t)
    rate.sleep()

if __name__ == '__main__':
    rospy.init_node('star_position', anonymous=True) #iniciar o nó
    rate = rospy.Rate(100) #definir a velocidade das publicações
    astro = rospy.get_param ("solar_system") #acessar o documento yaml que contém os parâmetros
    while not rospy.is_shutdown():
        x = rospy.Time.now().to_sec() # pegar o tempo do ros
        for frame in astro: # chamar a função com um frame de cada vez (usa-se para adicionar mais frames)
            handle_planet_pose (frame["astro"], frame["parent"], frame["raio_astro"], x*frame["velocidade"])