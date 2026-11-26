---
title: Cardano (blockchain)
ticker: ADA
category: Layer 1
status: draft
updated: 2026-11-26
written_by: claude-haiku-5-5 (high effort)
---

**Cardano** is a proof-of-stake blockchain platform whose documentation describes it as a network on which users buy and sell ADA.[^1][^3] Its consensus protocol, Ouroboros, was introduced in a 2016 academic paper,[^2] and its native smart contract language, Plutus, is a Turing-complete language written in Haskell.[^3] Cardano's documentation says its development has produced a chain with zero outages, a self-description that this draft has not independently verified.[^1] This draft draws on project documentation, an academic paper, a Cardano.org news post and one exchange blog, and has not been fact-checked.[^4][^5]

## Infobox

| Field | Detail |
|---|---|
| Type | Proof-of-stake blockchain platform (self-described)[^1] |
| Ticker | ADA[^5] |
| Consensus | Ouroboros, a proof-of-stake protocol[^2][^1] |
| Smart contracts | Plutus, a Turing-complete language written in Haskell[^3] |
| Accounting model | Extended UTXO (EUTXO)[^3] |
| Development phases | Byron, Shelley, Goguen, Basho, Voltaire[^1] |
| Governance | On-chain; Plomin hard fork enacted 2025-01-29[^4] |
| Organisations listed by Cardano.org | Cardano Foundation, EMURGO, Input Output, Intersect, PRAGMA[^4] |

## History

Cardano's documentation says the Byron phase set the foundation for development, allowing users to buy and sell ada on a proof-of-stake network.[^1] Initially the ledger was a federated network in which block production and transaction validation were maintained by “the founding entities”. The Byron era also saw the delivery of the Daedalus and Yoroi wallets and a block explorer.[^1]

The mainnet underwent a hard fork in late July 2020 to switch from the Byron ledger rules to the Shelley ledger rules.[^1] The Shelley phase moved block production toward a distributed community of stake pool operators.[^1]

The Goguen phase focused on decentralised application building, smart contract support and custom token issuance. Its features were introduced in steps, each with a separate hard fork: Allegra added token locking, Mary added native multi-asset tokens, and Alonzo added smart contract support.[^1]

The Basho phase focuses on scalability and interoperability.[^1] The Babbage ledger era, also called Vasil, added reference inputs, inline datums and reference scripts.[^1]

## Technology

### Ouroboros consensus

The 2016 paper by Aggelos Kiayias, Alexander Russell, Bernardo David and Roman Oliynykov describes Ouroboros as “the first blockchain protocol based on proof of stake with rigorous security guarantees”.[^2] The authors state that its security properties are comparable to those of the Bitcoin protocol, and they claim that a proposed reward mechanism makes honest behaviour an approximate Nash equilibrium, neutralising attacks such as selfish mining.[^2] These are the authors' claims.

Cardano's documentation notes that consensus features have historically carried the name Ouroboros.[^1] The Shelley era used a transitional Praos protocol (TPraos) to move away from Ouroboros BFT, and the Babbage era replaced TPraos with Praos.[^1]

### Plutus and smart contracts

Plutus is described by Cardano's documentation as the native smart contract language for Cardano. It is Turing-complete, written in Haskell, and Plutus smart contracts are effectively Haskell programs.[^3] Developers write validators in Haskell, which are compiled into Plutus Core by a GHC plug-in called Plutus Tx. On-chain and off-chain code are based on the same language.[^3] The documentation states that it is essential to know the basics of Haskell to use Plutus.[^3]

Cardano uses an extended UTXO model (EUTXO). Output addresses can contain complex logic that decides which transactions may unlock them, and all outputs can carry custom data. The documentation says that whether a transaction validates depends only on the transaction and its inputs, so validity can be checked off-chain.[^3]

The documentation says that, in contrast to Ethereum, Plutus supports user-defined fungible and non-fungible tokens natively, without an accompanying smart contract. This comparison is the documentation's own.[^3]

## Governance

The Voltaire phase gives the community the ability to vote on network development updates, technical improvements and project funding.[^1] The Conway ledger era, part of Voltaire, includes two hard forks: Chang introduced the initial governance framework, and Plomin completed the governance feature set, including delegated representatives (DReps), treasury withdrawals and governance actions under CIP-1694.[^1]

On 29 January 2025, Cardano transitioned to community governance with the Plomin hard fork, approved by stake pool operators and the interim constitutional committee.[^4] Ada holders can propose and vote on governance actions directly or through DReps. Staking rewards continue, but withdrawing them requires delegation to a DRep or selecting a predefined option.[^4]

A Cardano.org news post credited to Intersect describes Plomin as “the first community-driven hard fork in blockchain history”. This is the post's own description and has not been checked against independent coverage.[^4]

The documentation says that two further eras are planned. Dijkstra will focus on Plutus v4, consensus and ledger integration, and Conway refactors for transition. Euler's full scope is still to be determined.[^1]

## Timeline

| Date | Event |
|---|---|
| 2016-09-14 | The Ouroboros paper is received by the IACR Cryptology ePrint Archive.[^2] |
| 2019-07-20 | The ePrint record shows the last of eight revisions.[^2] |
| 2020-07 | The mainnet hard fork switches from the Byron to the Shelley ledger rules.[^1] |
| 2023-02-14 | The Valentine (SECP) intra-era hard fork adds Plutus built-ins for ECDSA and Schnorr signatures.[^1] |
| 2025-01-29 | The Plomin hard fork is enacted, completing the governance feature set.[^4] |

## References

[^1]: [Development phases and eras | Cardano Docs](https://docs.cardano.org/about-cardano/evolution/eras-and-phases)
[^2]: [Ouroboros: A Provably Secure Proof-of-Stake Blockchain Protocol](https://eprint.iacr.org/2016/889)
[^3]: [Plutus | Cardano Docs](https://docs.cardano.org/developer-resources/smart-contracts/plutus)
[^4]: [Chang upgrade completed - Plomin hard fork achieved! | Cardano](https://cardano.org/news/2025-01-30-chang-upgrade-completed/)
[^5]: [What Actually Happened with the Cardano Exploit? - Bitfinex blog](https://blog.bitfinex.com/education/what-actually-happened-with-the-cardano-exploit/)
