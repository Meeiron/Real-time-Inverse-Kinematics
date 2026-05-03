# Real-time Inverse Kinematics Comparison using CCD and Enhanced FABRIK

## Course
Computer Animation Term Project  
Department of Computer Engineering, Chulalongkorn University

## Author
Theerut Suwanrada

---

## Project Title
Real-time Inverse Kinematics Comparison using CCD and Enhanced FABRIK

---

## Problem
This project studies the inverse kinematics (IK) problem for real-time interactive computer animation.

Given a fixed base joint, multiple connected arm segments, and a target position, the objective is to compute the joint configuration such that the end-effector reaches the target as accurately and efficiently as possible.

The main focus is on comparing convergence speed, runtime performance, and positional accuracy between two IK methods.

---

## Approach

### Baseline
**Cyclic Coordinate Descent (CCD)**

CCD solves IK by iteratively rotating each joint from the end-effector toward the base until the target is reached.

Main characteristics:
- simple implementation
- angle-based iterative solver
- may require many iterations
- slower for longer chains

---

### Proposed
**Enhanced FABRIK (Forward And Backward Reaching Inverse Kinematics)**

The proposed method uses FABRIK with additional improvements:

- **Early stopping**  
  terminates iteration when error is below threshold

- **Unreachable target clamping**  
  directly stretches the chain toward unreachable targets

These improvements reduce unnecessary iterations and improve real-time responsiveness.

---

## Results

### Speedup
The proposed method achieves approximately:

- **2.9× speedup** for 3 joints
- **3.1× speedup** for 5 joints
- **3.1× speedup** for 10 joints

---

### Stability Improvement
The proposed method reduces average positional error from:

- CCD: **3.8 px**
- Proposed: **1.2 px**

This corresponds to approximately:

- **68% error reduction**

---

## Visualization / Demo
The project includes a real-time interactive 2D demo.

Features:
- articulated arm follows mouse cursor
- switch between CCD and FABRIK
- display runtime, iterations, and error
- real-time visual comparison

Press **SPACE** to switch methods.

---

## How to Run

### Install dependencies
```bash
pip install pygame numpy
