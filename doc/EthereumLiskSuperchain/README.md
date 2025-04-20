# Ethereum, Lisk and the Superchain

## A comparison of Ethereum, Bitcoin and Lisk's Architectures

| Feature | Ethereum | Bitcoin | Lisk |
| :--: | :--: | :--: | :--: |
| Consensus Mechanism | Proof of Stake (Ethereum 2.0 / Casper) | Proof of Work (SHA-256) | Delegated Proof of Stake (DPoS) |
| Time-to-Finality | ~13–15 minutes (safe finality via checkpoints) | ~60 minutes (6 block confirmations) | ~10–20 seconds (block time), faster finality |
| Fraud Proof System | Optimistic Rollups (external layer), zk-rollups in L2 | None natively; full node verification | None native; relies on trusted delegates |
| Transaction Cost (Simple Transfer) | ~$0.20–$1.50 (varies with gas fees) | ~$0.20–$1.00 (depends on fee market) | 0.001 LSK ($0.002) |
| Max Transactions per Second (TPS) | ~15–30 TPS (base layer), 1,000s via rollups | ~7 TPS (base layer) | ~25 TPS (can increase with optimizations) |

## Comparison of Transactions

So, I took 2 transactions, one from Etherscan and another from Lisk's Blockscout Explorer and I'll study them. Here are the hashes:

1. **0xdca3bf4ff39b81dbb197e7cb71d16b5e55677e56f4c558c47e074613a4faa411** from Eherscan
2. **0xe4c56f244d932780008afc57bf26a463e4cf83c2414b3d9dc346e9080ecf78e4** from Lisk's BE



### 1. Why does the Ethereum transaction cost more gas?

These 2 were successful transactions on these blockchains and the Etherscan one costed 0.83323233 Gwei while the Lisk BE one costed 0.001301318 Gwei.

There are two main reasons:

#### Ethereum has a more complex and congested ecosystem:

Ethereum is general-purpose, supporting dApps, DeFi, NFTs, etc. To handle security, consensus, and contract execution, it uses a more robust virtual machine (EVM). The base gas cost is higher, and competition for block space drives it up.

#### Lisk has a more lightweight and purpose-specific design

Lisk is optimized for speed and simplicity, with fewer operations per transaction. It uses static fees for most actions, which are very low compared to Ethereum’s dynamic gas pricing.

> So even for a simple value transfer, Ethereum needs more processing to validate, update state, and include in a block. Lisk just runs a lightweight validation and includes it faster with lower system requirements.

### 2. How did Gas Price impact total fees in USD?

#### Ethereum Transaction

**Gas Used:** ~21,000 (standard for a transfer)

**Gas Price:** 0.83323233 Gwei = 0.00000000083323233 ETH

$$Total Fee (in ETH) = Gas Used × Gas Price: 21,000 × 0.00000000083323233 = 0.000017497 ETH$$

$$If ETH = $3,200 (approx), then: 0.000017497 ETH × 3200 = **$0.056**$$

#### Lisk Transaction

Fee: 0.001301318 Gwei = 0.000000001301318 LSK

Lisk doesn't use dynamic gas, so this is just the flat fee.

$$If LSK = $1.70 (approx), then: 0.000000001301318 × 1.70 = **$0.0000000022**$$

#### Final Comparison in USD

| Blockchain | Total Fee (USD) | Fee Model |
| :--: | :--: | :--: |
| Ethereum | ~$0.056 | Gas-based (dynamic) |
| Lisk | ~$0.0000000022 | Flat/static fee |