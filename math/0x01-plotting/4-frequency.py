#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

plt.hist(student_grades, bins=10, range=(0, 100), histtype='bar', ec='black')
plt.xlabel('Grades')
plt.ylabel('Number of Students')
plt.suptitle('Project A')
plt.yticks(np.arange(0, 30, 5))
plt.show()