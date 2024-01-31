
# ROS2 Keyboard Publisher

A ROS package for publishing keyboard input as `std_msgs/String` messages.

## Overview

This ROS package provides a simple keyboard publisher node that reads user keyboard input and publishes it as a string message (`std_msgs/String`). It can be useful for controlling ROS robots or triggering certain actions based on keyboard input.

## Installation

1. Navigate to your desired workspace directory (e.g., ros2_ws)

```bash
cd home/ros/ros2_ws/src
```

2. Clone the repository into your ROS workspace:

   ```bash
   git clone https://github.com/dhanushshettigar/ros2_key_pub.git
   ```
3. Build the package with colcon

```bash
colcon build --symlink-install
```

4. Source the setup.bash file
```bash
source install/setup.bash
```

## Usage

Run the keyboard publisher node:

```bash
ros2 run ros2_key_pub key_pub keyboard_input
```
Replace `keyboard_input` with the desired topic name.

### Controlling the Node

Press keys on your keyboard, and the node will publish the pressed key as a `std_msgs/String message`.

To terminate the node, press the `q` key.

### Print the data going through a Topic

You can listen to topic directly from the terminal

```bash
ros2 topic echo /keyboard_input
```
