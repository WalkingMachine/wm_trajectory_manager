#!/usr/bin/env python
# coding=utf-8

import rospy
# from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import wm_trajectory_manager.srv
import os

class trajectory_manager:
    def __init__(self, node_name):
        rospy.init_node(node_name)
        service_save = rospy.Service('save_trajectory', wm_trajectory_manager.srv.save_trajectory, self.save)
        service_run = rospy.Service('run_trajectory', wm_trajectory_manager.srv.run_trajectory, self.run)
        self.controller = "sara_arm_trajectory_controller"
    def save(self, srv):
        # srv = wm_trajectory_manager.srv.save_trajectory()
        file = open(srv.file, 'w+')
        file.write(str(srv.trajectory))
        print "service save"
        return []
    def run(self, srv):
        print "service run"
        command = "rostopic pub -f "+str(srv.file)+" /"+self.controller+"/Follow_trajectory/goal trajectory_msgs/JointTrajectory"
        print command
        os.system(command)
        return []

if __name__ == '__main__':

    try:
        trajectory_manager('trajectory_manager')

        rospy.spin()

    except rospy.ROSInterruptException:
        pass
