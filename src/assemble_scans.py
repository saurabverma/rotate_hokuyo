#!/usr/bin/env python

# Load lib
import rospy 
from laser_assembler.srv import AssembleScans2
from sensor_msgs.msg import PointCloud2

if __name__ == '__main__':

	# Initialize node, service and publisher
	rospy.init_node("assemble_scans_to_cloud")
	rospy.wait_for_service("assemble_scans2")
	assemble_scans = rospy.ServiceProxy('assemble_scans2', AssembleScans2)
	pub = rospy.Publisher ("/laser_pointcloud", PointCloud2, queue_size=1)

	# Set rate
	if rospy.has_param('~rate'):
		rate = rospy.get_param('~rate')
	else:
		rate = 1.0
	r = rospy.Rate(rate)

	# Publish cloud periodically
	begin_time = rospy.Time(0, 0)
	while not rospy.is_shutdown():
		try:
			end_time = rospy.get_rostime() # get data upto now
			resp = assemble_scans(begin_time, end_time)
			begin_time = rospy.get_rostime() # start new period for data collection now
			rospy.logdebug("Got cloud with %u points" % len(resp.cloud.data))
			pub.publish (resp.cloud)
		except rospy.ServiceException as e:
			rospy.logerror("Service call failed: %s" % e)
		r.sleep()
