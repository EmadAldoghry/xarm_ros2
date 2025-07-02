import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'my_xarm6_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Install launch files
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        # Install config files
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
        # Install URDF files
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
        # Install SRDF files
        (os.path.join('share', package_name, 'srdf'), glob('srdf/*')),
        # Install mesh files
        (os.path.join('share', package_name, 'meshes/visual'), glob('meshes/visual/*')),
        (os.path.join('share', package_name, 'meshes/collision'), glob('meshes/collision/*')),
        (os.path.join('share', package_name, 'meshes/end_tool/visual'), glob('meshes/end_tool/visual/*')),
        (os.path.join('share', package_name, 'meshes/end_tool/collision'), glob('meshes/end_tool/collision/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aldoghry',
    maintainer_email='aldoghry@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
