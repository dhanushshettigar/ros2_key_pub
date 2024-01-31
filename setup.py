from setuptools import find_packages, setup

package_name = 'ros2_key_pub'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Dhanush Shettigar',
    maintainer_email='dhanushshettigar90@gmail.com',
    description='A ROS package for publishing keyboard input.',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
           'key_pub = ros2_key_pub.key_pub:main'
        ],
    },
)
