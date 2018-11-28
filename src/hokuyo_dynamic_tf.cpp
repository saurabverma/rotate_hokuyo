#include "ros/ros.h"
#include <dynamixel_msgs/JointState.h>
#include <tf/transform_broadcaster.h>

float motor_pos;

void scanCallback(const dynamixel_msgs::JointState::ConstPtr &motor_angle)
{
  motor_pos = motor_angle->current_pos;

  static tf::TransformBroadcaster br;
  tf::Transform transform;
  tf::Quaternion q;

  q.setRPY(motor_pos, 0, 0);
  // q.setRPY(0, 0, 0);
  transform.setRotation(q);
  br.sendTransform(tf::StampedTransform(transform, ros::Time::now(), "/hokuyo_sensor", "/laser"));
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "tilt_lidar");
  ros::NodeHandle n;
  ros::Subscriber mortor_sub = n.subscribe("/pan_controller/state", 1, scanCallback);
  ros::spin();
  return 0;
}
