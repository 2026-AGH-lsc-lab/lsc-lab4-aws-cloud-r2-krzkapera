import matplotlib.pyplot as plt
import numpy as np

zip_avg_warm_h = 38.75
zip_cold_rtt = 837.13
zip_warm_rtt = 57.75
zip_init = 571.53
zip_cold_h = 37.64

cont_avg_warm_h = 74.38
cont_cold_rtt = 719.71
cont_warm_rtt = 23.32
cont_init = 560.87
cont_cold_h = 85.12

labels = [
    "Lambda Zip\n(Cold Start)",
    "Lambda Container\n(Cold Start)",
    "Lambda Zip\n(Warm)",
    "Lambda Container\n(Warm)",
]

rtts = [zip_cold_rtt, cont_cold_rtt, zip_warm_rtt, cont_warm_rtt]
inits = [zip_init, cont_init, 0, 0]
handlers = [zip_cold_h, cont_cold_h, zip_avg_warm_h, cont_avg_warm_h]

x = np.arange(len(labels))
width = 0.6

fig, ax = plt.subplots(figsize=(12, 7))

p1 = ax.bar(x, rtts, width, label="Network RTT", color="#5b9bd5")
p2 = ax.bar(x, inits, width, bottom=rtts, label="Init Duration", color="#ffc000")
p3 = ax.bar(
    x,
    handlers,
    width,
    bottom=np.array(rtts) + np.array(inits),
    label="Handler Duration",
    color="#70ad47",
)

totals = np.array(rtts) + np.array(inits) + np.array(handlers)
for i, total in enumerate(totals):
    ax.text(
        i,
        total + 10,
        f"{int(total)}ms",
        ha="center",
        va="bottom",
        fontweight="bold",
        fontsize=12,
    )

    ax.text(
        i,
        rtts[i] / 2,
        f"{int(rtts[i])}ms",
        ha="center",
        va="center",
        color="black",
        fontweight="bold",
        fontsize=10,
    )

    if inits[i] > 0:
        ax.text(
            i,
            rtts[i] + inits[i] / 2,
            f"{int(inits[i])}ms",
            ha="center",
            va="center",
            color="black",
            fontweight="bold",
            fontsize=10,
        )

    ax.text(
        i,
        rtts[i] + inits[i] + handlers[i] / 2,
        f"{int(handlers[i])}ms",
        ha="center",
        va="center",
        color="black",
        fontweight="bold",
        fontsize=10,
    )

ax.set_ylabel("Latency (ms)", fontsize=12)
ax.set_title("Figure 1: Lambda Latency Decomposition (Scenario A)", fontsize=14, pad=20)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=11)
ax.legend(loc="upper right", frameon=True)
ax.grid(axis="y", linestyle="-", alpha=0.3)
ax.set_ylim(0, 1600)

plt.tight_layout()
plt.savefig("results/figures/latency_decomposition.png", dpi=300)
print("Figure 1 updated with finalized values.")
