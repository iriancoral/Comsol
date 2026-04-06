import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 11,
    'axes.linewidth': 0.8,
    'grid.linewidth': 0.5,
    'grid.alpha': 0.4,
    'lines.linewidth': 1.5,
    'lines.markersize': 5,
})

# Steady-state T_min (t=3600s) from COMSOL data
p_values = [0.70, 0.80, 0.90, 0.95, 1.00, 1.10, 1.20, 1.30, 1.40, 1.50, 1.60, 1.70, 1.80, 1.90]
T_min_ss = [282.06, 284.00, 287.49, 289.85, 292.60, 294.45, 294.89, 295.02, 294.78, 294.50, 294.35, 293.85, 293.40, 293.12]

fig, ax = plt.subplots(figsize=(7, 4.5))

ax.plot(p_values, T_min_ss, 's-', color='#2c3e50', markerfacecolor='#2c3e50',
        markeredgecolor='#2c3e50', markersize=4, linewidth=1.4,
        label=r'Steady-state $T_{\mathrm{min}}$')

# Highlight optimum at p=1.3
opt_idx = p_values.index(1.3)
ax.plot(p_values[opt_idx], T_min_ss[opt_idx], 'D', color='#c0392b',
        markersize=7, zorder=5, markeredgecolor='#c0392b',
        label=r'Optimum: $p = 1.3$, $T_{\mathrm{min}} = 295.0\,\mathrm{K}$')

# Dew point line
ax.axhline(y=283.15, color='#7f8c8d', linestyle='--', linewidth=1.2,
           label=r'Dew point $T_{\mathrm{dew}} = 283.15\,\mathrm{K}$')

ax.set_xlabel('Chebyshev exponent $p$', fontsize=12)
ax.set_ylabel(r'Steady-state $T_{\mathrm{min}}$ (K)', fontsize=12)
ax.legend(fontsize=9.5, loc='lower right', framealpha=0.9, edgecolor='#cccccc')
ax.grid(True, which='both', linestyle='-', alpha=0.35)
ax.minorticks_on()
ax.grid(True, which='minor', linestyle=':', alpha=0.2)
ax.set_xlim(0.6, 2.0)
ax.set_ylim(280, 296.5)
ax.tick_params(labelsize=10)

plt.tight_layout()
plt.savefig(r'C:\Users\Irian\Desktop\Irian\Irian\Irian Claude\Scorro\Master\Jaar 2\Comsol\Final report\images\Plot of steady-state Tmin vs p, peak at p = 1.3.png', dpi=300, bbox_inches='tight')
plt.close()
print("Done!")
