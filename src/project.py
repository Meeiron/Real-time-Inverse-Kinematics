import pygame
import numpy as np
import time
import math

WIDTH, HEIGHT = 1200, 900
FPS = 60

WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
BLUE = (50, 100, 255)
RED = (255, 80, 80)
GREEN = (80, 255, 80)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("IK Comparison: CCD vs FABRIK")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)

# แขน 4 ข้อ
lengths = [100, 100, 80, 60]
base_pos = np.array([WIDTH // 2, HEIGHT // 2], dtype=float)


def distance(a, b):
    return np.linalg.norm(a - b)


def forward_kinematics(base, angles, lengths):
    joints = [base.copy()]
    angle_sum = 0

    for i in range(len(lengths)):
        angle_sum += angles[i]
        x = joints[-1][0] + lengths[i] * math.cos(angle_sum)
        y = joints[-1][1] + lengths[i] * math.sin(angle_sum)
        joints.append(np.array([x, y]))

    return joints


def ccd_ik(base, lengths, target, max_iter=30, threshold=5):
    angles = [0.0] * len(lengths)

    start = time.perf_counter()

    for iteration in range(max_iter):
        joints = forward_kinematics(base, angles, lengths)
        end_effector = joints[-1]

        if distance(end_effector, target) < threshold:
            break

        for i in reversed(range(len(angles))):
            joints = forward_kinematics(base, angles, lengths)
            joint = joints[i]
            end_effector = joints[-1]

            to_end = end_effector - joint
            to_target = target - joint

            angle1 = math.atan2(to_end[1], to_end[0])
            angle2 = math.atan2(to_target[1], to_target[0])

            angles[i] += angle2 - angle1

    runtime = (time.perf_counter() - start) * 1000
    joints = forward_kinematics(base, angles, lengths)
    error = distance(joints[-1], target)

    return joints, runtime, iteration + 1, error


def fabrik_ik(base, lengths, target, max_iter=30, threshold=5):
    points = [base.copy()]

    for l in lengths:
        points.append(points[-1] + np.array([l, 0], dtype=float))

    total_length = sum(lengths)

    start = time.perf_counter()

    iterations_used = 0   # <-- เพิ่มบรรทัดนี้

    if distance(base, target) > total_length:
        direction = (target - base) / distance(base, target)

        for i in range(1, len(points)):
            points[i] = points[i - 1] + direction * lengths[i - 1]

        iterations_used = 1   # <-- เพิ่มบรรทัดนี้

    else:
        original_base = base.copy()

        for iteration in range(max_iter):
            # backward
            points[-1] = target.copy()

            for i in reversed(range(len(points) - 1)):
                r = distance(points[i + 1], points[i])
                lam = lengths[i] / r
                points[i] = (1 - lam) * points[i + 1] + lam * points[i]

            # forward
            points[0] = original_base.copy()

            for i in range(len(points) - 1):
                r = distance(points[i + 1], points[i])
                lam = lengths[i] / r
                points[i + 1] = (1 - lam) * points[i] + lam * points[i + 1]

            iterations_used = iteration + 1   # <-- เพิ่มบรรทัดนี้

            if distance(points[-1], target) < threshold:
                break

    runtime = (time.perf_counter() - start) * 1000
    error = distance(points[-1], target)

    return points, runtime, iterations_used, error


def draw_arm(joints, color):
    for i in range(len(joints) - 1):
        pygame.draw.line(
            screen,
            color,
            joints[i].astype(int),
            joints[i + 1].astype(int),
            5
        )
        pygame.draw.circle(screen, BLACK, joints[i].astype(int), 8)

    pygame.draw.circle(screen, BLACK, joints[-1].astype(int), 8)


running = True
use_fabrik = False

while running:
    clock.tick(FPS)

    target = np.array(pygame.mouse.get_pos(), dtype=float)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                use_fabrik = not use_fabrik

    screen.fill(WHITE)

    if use_fabrik:
        joints, runtime, iters, error = fabrik_ik(base_pos, lengths, target)
        method = "FABRIK (Proposed)"
        color = GREEN
    else:
        joints, runtime, iters, error = ccd_ik(base_pos, lengths, target)
        method = "CCD (Baseline)"
        color = BLUE

    draw_arm(joints, color)

    pygame.draw.circle(screen, RED, target.astype(int), 10)

    texts = [
        f"Method: {method}",
        f"Runtime: {runtime:.4f} ms",
        f"Iterations: {iters}",
        f"Error: {error:.2f}",
        "Press SPACE to switch method"
    ]

    for i, txt in enumerate(texts):
        surface = font.render(txt, True, BLACK)
        screen.blit(surface, (20, 20 + i * 30))

    pygame.display.flip()

pygame.quit()