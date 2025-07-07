import matplotlib.pyplot as plt
import numpy as np

# path_to_data = '../data/zetapi-iterates10000/run3/'
path_to_data = '../data/fortran-out/'
# path_to_data = './'
# Radii to plot
# nonuni_radii = [0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85]
# nonuni_radii = []
radii_res1 = np.arange(0.87, 0.88, 0.001)
# radii = np.append(nonuni_radii, uni_radii)
# radii_res1 = np.arange(0.87, 0.875, 0.001)
# radii_res2 = np.arange(0.86, 0.901, 0.01)
# radii_res1 = [0.89]
radii_res2 = []
# radii_res2 = [0.87, 0.88, 0.89]
# radii_res3 = np.linspace(0.85, 0.87, 2)
radii_res3 = []
radii = np.append(np.append(radii_res1, radii_res2), radii_res3)

Bc = 1.0/np.pi

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)
# Loop through each file, load the data and plot    
for i, r in enumerate(radii):
    filename = f"phase_portrait_r={r:.4f}_iter=1-500000.txt"
    # filename = f"phase_portrait_zeta_pi_r={r:.4f}_iter=1-500000.txt"
    
    # plt_filename = f"phase_portrait_zeta0_r={r:.4f}_iter=1-500000.png"
    # plt_filename = f"phase_portrait_zetapi_r={r:.4f}_iter=1-500000.png"
    # plt_filename = f"phase_portrait_fig1b_r={r:.4f}.png"
    # plt_filename = f"phase_portrait_fig1b_lcfs_v2.png" 
    plt_filename = f"phase_portrait_zeta0_combined_iter=1-500000_zoomin-v4.png"
    # plt_filename = f"phase_portrait_zetapi_combined_iter=1-500000.png"
    
    array = np.loadtxt(path_to_data + filename)
    psi_t_vals = array[:,0]
    theta_vals = array[:,1]
    x = np.sqrt(psi_t_vals/(np.pi * Bc)) * np.cos(theta_vals)
    y = np.sqrt(psi_t_vals/(np.pi * Bc)) * np.sin(theta_vals)
    
    # plt.figure()
    # fig = plt.figure(figsize=(10, 6))
    # ax = fig.add_subplot(1, 1, 1)
    ax.plot(x, y, '.', markersize=1, label=f"r={r:.4f}")

    # plt.xlim([-2,2])
    # plt.ylim([-2,2])
    ax.set_xlim([0.8675, 0.8775])
    ax.set_ylim([-0.05, 0.05])
    # ax.set_xlim([0.80, 1.30])
    # ax.set_ylim([0.10, 0.60])
    # plt.gca().set_aspect('equal')
    plt.legend(loc='upper right',fontsize=8)
    ax.grid('on') 
    # plt.show()
    # plt.savefig(path_to_data + plt_filename, bbox_inches='tight', dpi=200)
    # plt.close()
    
plt.savefig(path_to_data + plt_filename, bbox_inches='tight', dpi=300) 
print("Plots saved successfully.")


