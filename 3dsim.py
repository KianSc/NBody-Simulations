import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

#Plot Setup
plt.style.use('dark_background')
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(projection='3d')
ax.set_xlim(-100,100)
ax.set_ylim(-100,100)
ax.set_zlim(-100,100)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.set_title('3D N-Body Simulation',fontdict={'fontname': 'Times New Roman', 'fontsize': 50})

#Simulation Char
N = 200
G = 10
m = 100.0
rad = 10
dt = 0.025
epsilon = rad/2
t = np.linspace(0,100,1000)
pos = np.random.uniform(low=-100.0, high=100.0, size=(N, 3))
mass = np.full((N), m)
pos_0 = pos

#Forces
def get_forces(pos, mass, G=G, epsilon = epsilon):
    dif_tensor = pos[None, :, :] - pos[:, None, :]
    dif_mag = np.linalg.norm(dif_tensor, axis=2) #N, N
    dif_mag[dif_mag < epsilon] = epsilon 
    m_prod = mass[:, None] * mass[None, :] #N, N
    force_mag = (G*m_prod)/(dif_mag**3)
    force_vectors = force_mag[:,:, None] * dif_tensor #N, N, 3
    net_force = np.sum(force_vectors, axis = 1) #N, 3

    return net_force

#Particle Spawn
scat = ax.scatter(pos[:,0], pos[:,1], pos[:,2], s=2*rad, alpha = 0.8, color = 'white') 

def update(frame):
    global pos_0, pos

    a = get_forces(pos, mass)/mass[:, None]

    #Verlet integrator
    pos_current = pos.copy()
    pos = 2*pos_current - pos_0 + a*(dt**2)
    pos_0 = pos_current

    scat._offsets3d = (pos[:,0], pos[:,1], pos[:,2])

    return scat,

world = FuncAnimation(
    fig = fig,
    func = update,
    frames = len(t),
    interval = 12,
)

plt.show()
