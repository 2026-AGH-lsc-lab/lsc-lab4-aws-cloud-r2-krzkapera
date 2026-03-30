import matplotlib.pyplot as plt
import numpy as np

SECONDS_IN_MONTH = 30 * 24 * 60 * 60
LAMBDA_COST_FACTOR = 0.0000009500015
FARGATE_MONTHLY = 17.77
EC2_MONTHLY = 14.98

rps_range = np.linspace(0, 100, 500)
monthly_requests = rps_range * SECONDS_IN_MONTH
lambda_monthly = monthly_requests * LAMBDA_COST_FACTOR

break_even_rps = FARGATE_MONTHLY / (SECONDS_IN_MONTH * LAMBDA_COST_FACTOR)

plt.figure(figsize=(12, 7))
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["axes.axisbelow"] = True

plt.plot(
    rps_range,
    lambda_monthly,
    label="Lambda (on-demand)",
    color="#ff9900",
    linewidth=2.5,
)
plt.axhline(
    y=FARGATE_MONTHLY,
    label=f"Fargate (always-on) = ${FARGATE_MONTHLY}/mo",
    color="#38761d",
    linestyle="--",
    linewidth=2.5,
)
plt.axhline(
    y=EC2_MONTHLY,
    label=f"EC2 t3.small (always-on) = ${EC2_MONTHLY}/mo",
    color="#2f3b43",
    linestyle="-.",
    linewidth=2.5,
)

plt.axvline(x=break_even_rps, color="red", linestyle=":", alpha=0.6, linewidth=1)
plt.scatter([break_even_rps], [FARGATE_MONTHLY], color="red", zorder=5)

plt.annotate(
    f"Break-even: {break_even_rps:.2f} RPS",
    xy=(break_even_rps, FARGATE_MONTHLY),
    xytext=(break_even_rps + 10, FARGATE_MONTHLY + 5),
    arrowprops=dict(arrowstyle="->", color="red"),
    color="red",
    fontweight="bold",
    fontsize=11,
)

plt.title("Figure 2: Monthly Cost vs. Request Rate", fontsize=14, pad=15)
plt.xlabel("Average Requests Per Second (RPS)", fontsize=12)
plt.ylabel("Monthly Cost (USD)", fontsize=12)
plt.legend(loc="upper left", frameon=True, fontsize=11)
plt.grid(True, linestyle="-", alpha=0.2)
plt.xlim(0, 100)
plt.ylim(0, 220)

plt.tight_layout()
plt.savefig("results/figures/fig2_cost_vs_rps.png", dpi=300)
print(f"Figure 2 generated successfully. Break-even at {break_even_rps:.2f} RPS.")
