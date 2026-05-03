# Real-time Inverse Kinematics: CCD vs FABRIK

This project presents a real-time comparison between two inverse kinematics (IK) algorithms: **Cyclic Coordinate Descent (CCD)** and **Forward And Backward Reaching Inverse Kinematics (FABRIK)** for 2D articulated arm animation.

The system is implemented in Python with an interactive visualization, allowing users to evaluate performance, convergence behavior, and motion quality in real time.

---

## 🔗 Repository

GitHub: https://github.com/Meeiron/Real-time-Inverse-Kinematics

---

## 📌 Project Overview

Inverse Kinematics (IK) is widely used in:

* Computer animation
* Game development
* Robotics simulation

This project focuses on comparing:

* Convergence speed
* Runtime performance
* Iteration count
* Stability in edge cases (e.g., unreachable targets)

---

## ⚙️ Features

* Real-time interactive IK simulation
* Mouse-controlled target position
* Switch between CCD and FABRIK
* Early stopping for faster convergence
* Unreachable target clamping
* Supports multiple chain lengths (e.g., 3, 5, 10 joints)

---

## 🧠 Methods

### CCD (Cyclic Coordinate Descent)

* Iteratively rotates joints from end-effector to base
* Simple and intuitive
* Easier to apply joint constraints

### FABRIK (Enhanced)

* Position-based approach (no angle rotation)
* Forward & backward passes
* Faster convergence
* More stable for real-time applications

Enhancements:

* Early stopping (threshold-based)
* Unreachable target clamping

---

## 📂 Project Structure

```bash
Real-time-Inverse-Kinematics/
│
├── src/                # Source code (main simulation logic)
│   ├── main.py
│   ├── ccd.py
│   ├── fabrik.py
│   └── utils.py
│
├── assets/             # (Optional) images / demo resources
│
├── results/            # Experiment results / screenshots
│
├── report/             # Final report (IEEE format)
│   └── IK_Report.pdf
│
├── slides/             # Presentation slides
│   └── IK_Presentation.pdf
│
└── README.md
```

---

## 📄 Included Files (Submission Materials)

This repository includes all materials submitted for the course project:

* 📘 **Final Report** (IEEE format)
* 📊 **Presentation Slides (PDF)**
* 🎥 **Demo (if included in repo or external link)**
* 💻 **Full Source Code (Python + Pygame)**

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install pygame numpy
```

### 2. Run the simulation

```bash
python src/main.py
```

### 3. Controls

* Move mouse → control target
* (Optional) Key press → switch IK method

---

## 📊 Results Summary

| Metric             | CCD         | FABRIK       |
| ------------------ | ----------- | ------------ |
| Iterations         | Higher      | Lower        |
| Runtime            | Slower      | Faster (~3×) |
| Stability          | Medium      | High         |
| Unreachable Target | Inefficient | Efficient    |

---

## ⚠️ Limitations

* Limited to 2D articulated chains
* No joint angle constraints
* No temporal smoothing
* FABRIK may produce ambiguous poses in some cases

---

## 🔄 When CCD Can Be Better

* Easier to enforce joint constraints
* More predictable behavior
* Better control over joint rotations
* Suitable for short kinematic chains

---

## 🚀 Future Work

* Extend to 3D IK systems
* Add joint constraints
* Integrate with Unreal Engine (Control Rig)
* Physics-based animation
* Motion smoothing

---

## 📚 Conclusion

FABRIK provides:

* Faster convergence
* Fewer iterations
* Better real-time performance

However, CCD remains useful in constraint-driven systems.

👉 There is **no universally best method** — the choice depends on application requirements.

---

## 👤 Author

**Theerut Suwanrada**
Computer Animation Term Project
