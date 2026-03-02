import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription

from launch_ros.actions import Node
import xacro

def generate_launch_description():
    robotXacroName='so101_new_calib'
    namePackage='so101_moveit2_description'
    modelFileRelativePath='model/so101_new_calib.xacro'
    pathModelFile=os.path.join(get_package_share_directory(namePackage),modelFileRelativePath)
    
    robotDescription=xacro.process_file(pathModelFile).toxml()
    
    nodeRobotStatePublisher=Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[
            {'robot_description': robotDescription, 'use_sim_time': True},
        ],
    )

    launchDescriptionObject=LaunchDescription()
    launchDescriptionObject.add_action(nodeRobotStatePublisher)
    
    return launchDescriptionObject