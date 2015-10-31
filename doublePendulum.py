# solve the two pendulums on a cart problem
import numpy as np
from scipy import sin, cos
from scipy.integrate import odeint
import matplotlib.pyplot as plt

class doublePendulum():
	"""Define the Pendulum class"""

	def __init__(self, input_para, time_info, init_cond):
		""" Model geometrical and mass input parameters """
		# Model information
		self.M1, self.M2, self.L1, self.L2, self.m1, self.m2, self.h1, self.h2, self.M, self.L = input_para
		# time information
		self.ts, self.te, self.tstep = time_info
		self.t = np.arange(self.ts, self.te, self.tstep)
		# Initial condition
		self.init_status = init_cond
		# generalized cooridinates
		self.x = self.init_status[0]
		self.th1 = self.init_status[1]
		self.th2 = self.init_status[2]

		self.dx = self.init_status[3]
		self.dth1 = self.init_status[4]
		self.dth2 = self.init_status[5]
		
		
	def equation(self, var, tim):
		"""Return the first derivative of the coordinates (totally 6 variables)"""
		g = 9.8

		self.x, self.th1, self.th2, self.dx, self.dth1, self.dth2 = var

		dx = self.dx
		dth1 = self.dth1
		dth2 = self.dth2

		#
		m11 = (self.M1 + self.m1 / 2.0) * self.L1 * cos(self.th1)
		m12 = (self.M1 + self.m1 / 3.0) * self.L1**2
		m13 = 0.0

		m21 = (self.M2 + self.m2 / 2.0) * self.L2 * cos(self.th2)
		m22 = 0.0
		m23 = (self.M2 + self.m2 / 3.0) * self.L2**2

		m31 = (self.M1 + self.M2 + self.m1 + self.m2 + self.M)
		m32 = m11
		m33 = m21

		b1 = -(self.M1 + self.m1 / 2.0) * self.L1 * g * sin(self.th1)
		b2 = -(self.M2 + self.m2 / 2.0) * self.L2 * g * sin(self.th2)
		b3 = (self.M1 + self.m1 / 2.0) * self.L1 * dth1**2 * sin(self.th1) \
		     +(self.M2 + self.m2 / 2.0) *self.L2 * dth2**2 * sin(self.th2)

		d2x, d2th1, d2th2 = np.linalg.solve([[m11, m12, m13], [m21, m22, m23], [m31, m32, m33]], [b1, b2, b3])

		return np.array([dx, dth1, dth2, d2x, d2th1, d2th2])

	"""
	def solve_ode(self):
		
		solu = odeint(self.equation, self.init_status, self.t)

		self.x = solu[:, 0]
		self.th1 = solu[:, 1]
		self.th2 = solu[:,2]

		# Convert the results from generalized coordinates to cartesian coordinates
		# Sphere A
		X1 = self.x + self.L1 * sin(self.th1)
		Y1 = self.h1 - self.L1 * cos(self.th1)
		# Sphere B
		X2 = self.x + self.L + self.L2 * sin(self.th2)
		Y2 = self.h2 - self.L2 * cos(self.th2)
		# Cart
		X = self.x + self.L / 2.0

		result = np.array([self.t, X1, Y1, X2, Y2, X, self.th1, self.th2])

		return result
	"""

	def solve_ode(self, t):
		""" Solve the system of the lagrange equtions describing the pendulum motion """
		solu = odeint(self.equation, self.init_status, t)

		self.x = solu[-1, 0]
		self.th1 = solu[-1, 1]
		self.th2 = solu[-1, 2]
		self.dx = solu[-1, 3]
		self.dth1 = solu[-1, 4]
		self.dth2 = solu[-1, 5]

		# Convert the results from generalized coordinates to cartesian coordinates
		# Sphere A
		X1 = self.x + self.L1 * sin(self.th1)
		Y1 = self.h1 - self.L1 * cos(self.th1)
		# Sphere B
		X2 = self.x + self.L + self.L2 * sin(self.th2)
		Y2 = self.h2 - self.L2 * cos(self.th2)
		# Cart
		X = self.x + self.L / 2.0

		result = np.array([t[-1], X1, Y1, X2, Y2, X, self.x, self.th1, self.th2, self.dx, self.dth1, self.dth2])

		return result


if __name__ == '__main__':
	# Model parameters
	M1 = 1000.0
	M2 = 1000.0
	L1 = 1.0
	L2 = 10.0
	m1 = 1.0
	m2 = 1.0
	h1 = 1.0
	h2 = 10.0
	M = 1.0
	L = 2.0
	input_para = np.array([M1, M2, L1, L2, m1, m2, h1, h2, M, L])

	# Time information
	ts = 0.0								# start time
	te = 1000.0								# end time
	tstep = 0.01								# time step
	time_info = np.array([ts, te, tstep])

	# Initial condition
	x0 = 0.0
	th10 = 1.0
	th20 = -0.0837
	dx0 = 0.0
	dth10 = 0.0
	dth20 = 0.0
	init_cond = np.array([x0, th10, th20, dx0, dth10, dth20])

	# Create pendulum instance
	pendulum = doublePendulum(input_para, time_info, init_cond)

	# Solve the ODE to get the trajectory of the pendulum
	result = pendulum.solve_ode()

	t = result[0, :]
	x1 = result[1, :]
	y1 = result[2, :]
	x2 = result[3, :]
	y2 = result[4, :]
	x = result[5, :]
	th1 = result[6, :]
	th2 = result[7, :]

	# Display the reuslts
	plt.plot(x1, y1,'r', x2, y2, 'b')
	#plt.plot(t, th1, 'r', t, th2, 'b')
	#plt.plot(t, x)
	plt.show()
	



			