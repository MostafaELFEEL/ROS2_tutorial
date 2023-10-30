# ROS2_tutorial
# ROS 2 Tutorial Environment Setup

This repository contains instructions for setting up your environment for a ROS 2 tutorial. Follow these steps to get started.

## Prerequisites

Before you begin, make sure you have the following prerequisites installed:

- [ROS 2](https://docs.ros.org/en/humble/Installation.html)
- A Linux-based operating system (ROS 2 is primarily supported on Ubuntu)

## Getting Started

1. **Create a Directory**: Open your terminal and create a directory for your ROS 2 tutorial. You can name it whatever you like. In this example, we'll call it `ros2_tutorial`.

   ```bash
   mkdir ros2_tutorial
   cd ros2_tutorial

2. **Download the Repository**:
   ```bash
   https://github.com/MostafaELFEEL/ROS2_tutorial.git
3. **Building the packages**:
   ```bash
   colcon build

4. **Sourcing Workspace in .bashrc**:
   ```bash
   gedit ~/.bashrc
   ```

   **Paste the following line in bashrc**:
   ```bashrc
   source ~/ros2_tutorial/install/setup.bash

   



