import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Input values
voltages = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
currents = [
    -0.009853876338718169,
    -0.008475209798088187,
    -0.0072245173776401056,
    -0.006751143501730558,
    -0.005603237526474062,
    -0.004086589420575551,
    -0.0033089243380782325,
    -0.002166446055095717,
    -0.001691078317098001,
    -0.0009966642650292264,
    0.00011490184547573081,
]

# Compute resistance through linear regression
result = linregress(x=currents, y=voltages)
resistance = result.slope
bias = result.intercept
resistance_std = result.stderr
bias_std = result.intercept_stderr

# Convert resistance and error bar into plottable values
resistance_value_str, resistance_magnitude_str = f"{resistance:.2e}".split("e")
error_bar_str = f"{resistance_std / (10 ** int(resistance_magnitude_str)):.2f}"

# Useful parameters for clean plot
abscissa = np.arange(-10, 10)

min_v = min(voltages)
max_v = max(voltages)
amp_v = max_v - min_v
plot_x_limits = [min_v - 0.1 * amp_v, max_v + 0.1 * amp_v]

min_c = min(currents)
max_c = max(currents)
amp_c = max_c - min_c
plot_y_limits = [min_c - 0.1 * amp_c, max_c + 0.1 * amp_c]

# Plot the measurements
plt.errorbar(voltages, currents, yerr=5e-4 * np.ones(len(currents)), fmt="o")

# Plot the regression
plt.plot(abscissa, (abscissa - bias) / resistance, zorder=0)
plt.fill_between(
    abscissa,
    y1=(abscissa - bias + bias_std) / (resistance - resistance_std),
    y2=(abscissa - bias - bias_std) / (resistance + resistance_std),
    zorder=0,
    alpha=0.5,
    color="tab:orange",
)

# Configure display
plt.title(
    f"I-C curve of the resistor "
    f"(R = {resistance_value_str} "
    f"+/- {error_bar_str} "
    f"x 10^{resistance_magnitude_str})"
)
plt.xlabel("Voltage (V)")
plt.ylabel("Current (A)")
plt.xlim(plot_x_limits)
plt.ylim(plot_y_limits)

# Tell python to show the figure
plt.show()
