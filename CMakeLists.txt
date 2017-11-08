cmake_minimum_required(VERSION 2.8.3)
project(wm_trajectory_manager)
SET(CMAKE_CXX_STANDARD 11)
add_definitions(-std=c++11)
find_package(Boost REQUIRED COMPONENTS system)
find_package(catkin REQUIRED COMPONENTS
        roscpp
        trajectory_msgs
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
        roscpp
        trajectory_msgs
)

include_directories(
        ${catkin_INCLUDE_DIRS}
)

# add_executable( ${PROJECT_NAME}
#         src/wm_frame_to_box.cpp
#         )

# add_dependencies(${PROJECT_NAME} ${catkin_EXPORTED_TARGETS})

## Specify libraries to link a library or executable target against
# target_link_libraries(${PROJECT_NAME} ${catkin_LIBRARIES})
