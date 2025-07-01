import numpy as np
import matplotlib.pyplot as plt

def center_of_gravity(x):
    '''
    Find the center of gravity of a vector, x.
    If x=[x0,x1,...,xn], then return
    c = (0*x0 + 1*x1 + 2*x2 + ... + n*xn) / sum(x)
    '''
    indices = np.arange(len(x))
    c = np.dot(indices, x) / np.sum(x)
    return c

def matched_identity(x):
    '''
    Create an identity matrix that has the same number of rows as x has elements.
    '''
    I = np.eye(len(x))
    return I

def sine_and_cosine(t_start, t_end, t_steps):
    '''
    Create a time axis, and compute its cosine and sine.
    '''
    t = np.linspace(t_start, t_end, t_steps)
    x = np.cos(t)
    y = np.sin(t)
    return t, x, y

# ===============================
# 以下是用于验证功能的测试代码
# ===============================

# 1. 测试 center_of_gravity
x = np.array([1, 2, 3, 4])
cog = center_of_gravity(x)
print("Center of gravity:", cog)

# 2. 测试 matched_identity
identity = matched_identity(x)
print("Matched identity matrix:\n", identity)

# 3. 测试 sine_and_cosine 并画图
t, cos_t, sin_t = sine_and_cosine(0, 2 * np.pi, 200)

plt.figure(figsize=(10, 4))
plt.plot(t, cos_t, label='cos(t)', color='blue')
plt.plot(t, sin_t, label='sin(t)', color='red')
plt.title('Cosine and Sine Functions')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
