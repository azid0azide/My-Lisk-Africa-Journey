# Introduction to Blockchain Technology

## Hello there!

So, I joined the Lisk Africa Builder's Bootcamp and I was so excited because I'll learn what exactly the Blockchain is and finally be a Crypto Bro! This is awesome since through the Bootcamp, you get to learn how to build Smart Contracts and dApps, among other awesome projects, possible, on chain. I hope you'll find this Series insightful and maybe it shall help you also learn new things along this Journey we've found ourselves in. Cheers! :beers:

## What is Blockchain?

Simply put, it's a mesh of libraries of blacked out record books that are locked down but still anyone can view or access them at any place. Ooof! I know but the smarter, nerdier definition is:

> ***"This refers to a decentralized, digitally distributed, public ledger that records transactions and exists on a network of multiple nodes in a secure and transparent manner."***

Since it's distributed and decentralized, there is no need for the common Middle man...

<div align="center">
	<img src="./assets/middleman.gif" style="width: 30px;height: 40px" alt="Martin Kessler's Middleman" />
</div>

## This is what's awesome about Blockchain...

### 1. It's **decentralized**

This means instead of being controlled by a single entity, every participant on the chain maintains it's integrity. Basically, you can't censor it nor does it have a single point of failure.

### 2. It's **distributed**

This means every node contains a copy (replica) of the transactions made on the chain. Data isn't easily changed nor is it lost on the chain.

### 3. It's **immutable**

Once a transaction is on the chain, it's very difficult, if not impossible, to modify or delete it.

### 4. It's **transparent**

All transactions are publicly visible on the chain, enhancing trust. The participants involved in a spacific transaction can view more details though.

### 5. It's **secure**

Cryptography is used to secure transcations and enhance their authenticity, preventing fraud, forgery and tampering.

## Is it just a fancy way of calling a database?

No. Dont't be a tool! Here's what's different between it and what you get from your SQL:

| Feature | Blockchain | Traditional Database |
| :--: | :--: | :--: |
| Control | Decentralized and no single authority | Centralized and managed by a single root user |
| Data Storage | Distributed across nodes | Stored on central servers |
| Security | Cryptography & Consensus protocols | Access control & authentication |
| Immutability | Data can't be changed once recorded | Data can be modified or deleted |
| Transperency | Public ledger that's open for verification | Restricted access with controlled visibility |

## I'm convinced. How does it work?

There's 3 fundamental components of a Blockchain:

1. **The block**: A collection of transactions recorded on the blockchain
2. **The transcation**: These are veriified by  the participant nodes before added onto a block
3. **The chain**: The blocks are linked together by cryptographic hashes, that are free from forgery.

More on the security, there is the **consensus mechanism**. This ensures that all transactions on a chain are verified and agreed upon bu he network. The commont types are:

1. **Proof of Work (PoW)**: This was used by the prime blockchain, Bitcoin. This involved having the nodes (miners) solve complex mathematical puzzles to validate transactions.

<div align="center">
	<img src="./assets/bitcoin.gif" style="width: 160px;height: 90px" alt="Bitcoin to the Moon" />
</div>

2. **Proof of Stake (PoS)**: Transaction validatora are chosen based on the ammount of crypto they hold and stake. There exists a **Delegated PoS (DPoS)** that where network participants vote for delegates who then validate transactions and create new blocks.

<div align="center">
	<img src="./assets/spongebob-money.gif" style="width: 100px;height: 90px" alt="Spongebob Mooney!" />
</div>

3. **Proof of Authority (PoA)**: This is where a small, pre-approved group of validators, known as "authorities," are responsible for verifying transactions and creating new blocks.

<div align="center">
	<img src="./assets/authoritah.gif" style="width: 160px;height: 90px" alt="Respect my Authoritaj!" />
</div>

Each of the consensus protocols above maintain the **Byzantine Fault Tolerance (BFT)** i.e. a characteristic of a system's ability to function correctly and reach consensus even when some of its components fail or act maliciously.

### By the way, what he heck are Nodes and Miners?

A **node** is a computer that stores a copyt of the blockchain and calidate transactions while **miners**, mostly in ablockchain that uses PoW, or **validators**, in one that iuses PoS, are sesponsible for verifying  transactions and adding new blocks on tthe chain. The might be referre to as either *full*, when they enforce the rules of the blochain or *light*, when they rely on full nodes for information. 

### Can you hav e a "private" Blockchain?

Yes, of course, meanie! These are useally implemented by enterprises and here are the differences between them and public Blockchains:

| Feature | Public Blockchain | Private Blockchain |
| :--: | :--: | :--: | 
| Access | Open to everyone | Restricted to specific participants |
| Control | Decentralized | Centralized |
| Security | Through consensus mechanisms | Controlled by a single organization |
| Offering | Transperency and Decentralization | Efficiency and controlled access |
| Examples | Ethereum, Bitcoin | Hyperledger, Corda, Ripple |

## Now that I know what the blockhain is, what can I make with it or on it?

There are these programs known as **Smart contracts** i.e. sel-executing algorithms stored on the chain that automatically execute transactions when predefined conditions are met and **Decentalized Applications (dApps)** i.e. blockchain-based apps that operate without a central authority, that you cn build. Tey are applied in the following areas:

1.  **Decentralized finance (DeFi)**: for lending, borrowing and trading without need for traditional banks e.g. Aave, Uniswap and Compound
2. **NFT Marketplaces**: Non-fungible tokens (NFTs) are unique digital identifier recorded on a blockchain, acting as a digital certificate of ownership for a specific asset.  There places where one may exchange them for crypto e.g. OpenSea, Fondation, Rarible.
3. **Gaming and the Metaverse**: These are play to earn games and virtual economies e.g Axie Infinity
4. **Supply chain and Logistics**: Ensures that shipping or manufacturing is transparent an trackable e.g. VeChain.

### I'm a Scientist. How can I use Blockchain in Science and Research?

Blockchain Tech is most definitely applicable in this field in the following ways:

1. **Enhanced Data transperency and Security**: Data can be signed and made available on a blockchain that is immutable and tamper-proof. This can ensure the reproducibility and authenticity of the data.
2. **Streamlined Peer review**: Researchers collaborating and sharing their work openly and securely can be the way to go. Also the whole Peer review process can be tracked and transparent.
3. **Research Funding and tracking**: Crowdfunding and collaborative research by clearly defining ownership and contributions as well as tracking it securely and transperently.

## That's great and all. What are some challenges blockchain faces?

### 1. Scalability issues

Whan a network gets congested and larger, slower transaction speeds and high fees can result from this happening. This is solved currently by **Layer 2 solutions**e.g. Optimism and ZK-Rollups, that process transactions off-chain to improve speed and **Sharding**, where the blockchain is split into smaller parts to handle more transactions in parallel. [^1]

[^1]: It should be noted that these are patchworks and not permanent.

### 2. Energy consumption by PoW

Need for high computing power led to server farms and mines that consume a lot of electricity. Some even can cause literal blackouts and instability in the electric grids of a town. This is solved currently by PoS and **Green blockchains** like Algorand and Tezos that use energy-efficient mechanisms.

### 3. Regulatory and Legalities

Governments struggle with regulating decentralized systems leading to uncertainity in business decisions and controlling the users and participants of the chain. **Decentralized identity** comes as a solution hat ensures compliance while ensuring user privacy.

## Whoa! That's a lot of info!

I know. I hope that this is a great intro to Blockchain and it will maybe spark interest in you to learn more about it.
