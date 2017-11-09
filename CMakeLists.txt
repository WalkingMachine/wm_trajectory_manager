cmake_minimum_required(VERSION 2.8.3)
project(wm_trajectory_manager)
find_package(catkin REQUIRED COMPONENTS
        rospy
        trajectory_msgs
        message_generation
        )

add_service_files(
        DIRECTORY srv
        FILES
         run_trajectory.srv
         save_trajectory.srv
)

generate_messages(
        DEPENDENCIES trajectory_msgs
)

catkin_package(
        CATKIN_DEPENDS
        rospy
        trajectory_msgs
)

include_directories(
        ${catkin_INCLUDE_DIRS}
)

