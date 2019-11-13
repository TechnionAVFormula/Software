#!/usr/bin/env python
import sys
import json
import rospy
import sensor_msgs.point_cloud2 as pc2

class Lidar():
    def __init__(self, number_of_frames_to_record=1, scan_topic="/velodyne/pointcloud"):
        rospy.loginfo("Listening for lidar point clouds on %s", scan_topic)
        self.number_of_frames_to_record = number_of_frames_to_record
        self.scan_sub = rospy.Subscriber(scan_topic, pc2.PointCloud2, self.on_scan)
        self.recorded_lidar = {
            'time': 0,
            'frames': []
        }
        
    def on_scan(self, frame):
        rospy.loginfo("Got scan")
        new_frame = {}
        gen = pc2.read_points(frame, skip_nans=True, field_names=("x", "y", "z", "intensity", "ring"))
        new_frame['time'] = 0
        new_frame['points'] = map(lambda pt: {'x': pt[0], 'y': pt[1], 'z': pt[2], 'intensity': pt[3], 'ring': pt[4]}, gen)
        self.recorded_lidar.frames.apeend(new_frame)

        if len(self.recorded_lidar.frames) > self.number_of_frames_to_record:
            self.stop()

    def stop():
        rospy.loginfo("Stopping Lidar listener")
        self.scan_sub.unregister()
        print(json.dumps(self.recorded_lidar))


def main(number_of_frames_to_record):
    rospy.init_node('save_lidar_frames', anonymous=True)
    
    lidar = Lidar(number_of_frames_to_record)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        number_of_frames_to_record = 0
        if len(sys.argv) > 1:
            number_of_frames_to_record = int(sys.argv[1])
        main(number_of_frames_to_record)
    except rospy.ROSInterruptException:
        pass