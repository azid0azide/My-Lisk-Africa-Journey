
import matplotlib.pyplot as plt

# --- Fee Comparison Chart (Ethereum vs Lisk) ---

blockchains_fee = ['Ethereum', 'Lisk']
fees_usd = [0.056, 0.0000000022]

plt.figure(figsize=(10, 6))
bars = plt.bar(blockchains_fee, fees_usd, color=['#627eea', '#00aaff'])

for bar, fee in zip(bars, fees_usd):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() * 1.05,
             f"${fee:.10f}", ha='center', fontsize=12)

plt.title('Transaction Fee Comparison: Ethereum vs Lisk', fontsize=16)
plt.ylabel('Fee (USD)', fontsize=12)
plt.yscale('log')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()

# --- TPS and Finality Charts (Ethereum, Bitcoin, Lisk) ---

blockchains_perf = ['Ethereum', 'Bitcoin', 'Lisk']
tps = [30, 7, 25]
finality_seconds = [780, 3600, 30]  # Ethereum ~13 mins, Bitcoin ~60 mins, Lisk ~30 secs

fig, ax = plt.subplots(1, 2, figsize=(14, 6))

bars1 = ax[0].bar(blockchains_perf, tps, color=['#627eea', '#f7931a', '#00aaff'])
ax[0].set_title('Max Transactions Per Second (TPS)', fontsize=14)
ax[0].set_ylabel('TPS', fontsize=12)
for bar, value in zip(bars1, tps):
    ax[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, f"{value}", ha='center', fontsize=11)

bars2 = ax[1].bar(blockchains_perf, finality_seconds, color=['#627eea', '#f7931a', '#00aaff'])
ax[1].set_title('Time to Finality (seconds)', fontsize=14)
ax[1].set_ylabel('Seconds', fontsize=12)
ax[1].set_yscale('log')
for bar, value in zip(bars2, finality_seconds):
    ax[1].text(bar.get_x() + bar.get_width()/2, value * 1.1, f"{value}s", ha='center', fontsize=11)

plt.tight_layout()
plt.show()
