This package is designed for a Hokuyo facing vertically up (instead of forward) and being rotated by a Dynamixel motor. This is useful if the we have to map the ceiling of a unique structure using a Hokuyo laser scaner. Note that a slip ring might be need because the scaner is assumed to rotate continuously.

The motor speed is defined in 'dynamixel_rotate_config.yaml' file. To start the system, run 'start_rotate_hokuyo.launch' whereas to stop the motor rotation, run 'stop_rotate.launch' (after stoping the former launch file). Remember to update the motor ID and connection ports for both Dynamixel and Hokuyo to be setup in the 'config' and 'launch' files.

There are a total of 3 coordinate frames considered here. One is that of the base (slip_ring - static and base frame) {x-forward, y-left, z-up}. Next is that of sensor static postion (hokuyo_sensor - static) which is placed at a certain vertical distance from the slip ring but instead of looking forward, this is facing up {x-up, y-right, z-forward}. Finally, the rotating frame (laser) w.r.t. /hokuyo_sensor about x-axis {x-up, y,z-rotating in horizontal plane}.



Note that this package 'rotate_hokuyo' (https://github.com/saurabverma/rotate_hokuyo.git) is dependent on following packages:

1. Dynamixel
```bash
sudo apt install ros-kinetic-dynamixel-motor
```

2. Hokuyo
```bash
sudo apt install ros-kinetic-urg-node
```

3. Laser assembler
```bash
sudo apt install ros-kinetic-laser-assembler
```
