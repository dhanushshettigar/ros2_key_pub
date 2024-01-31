import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import sys
import termios
import tty

class KeyboardPublisher(Node):

    def __init__(self, topic_name):
        super().__init__('keyboard_pub')
        self.publisher_ = self.create_publisher(String, topic_name,10)
        self.key = None

    def get_key(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            self.key = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    def publish_key(self):
        self.get_key()
        if self.key:
            if self.key == 'q':
                self.get_logger().info('Terminating node...')
                sys.exit(0)
            else:
                self.get_logger().info(f'Key pressed: {self.key}')
                msg = String()
                msg.data = self.key
                self.publisher_.publish(msg)

def main(args=None):
    if args is None:
        args = sys.argv

    if len(args) != 2:
        print("Usage: ros2 run ros2_key_pub  <topic_name>")
        sys.exit(1)

    topic_name = args[1]
    
    rclpy.init(args=args)
    keyboard_publisher = KeyboardPublisher(topic_name)

    try:
        while rclpy.ok():
            keyboard_publisher.publish_key()
    except KeyboardInterrupt:
        pass
    finally:
        keyboard_publisher.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
