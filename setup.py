from setuptools import find_packages, setup

package_name = 'hw3_2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='stephenlinux',
    maintainer_email='stephenlinux@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'pub = hw3_2.publisher_function32:main',
                'sub = hw3_2.subscriber_function32:main'            
        ],
    },
)
