# Independent review: accounts, cryptography, interoperability, and consensus

Date: 2026-10-31
Checker and corrective writing pass: `gpt-6-astra high`

This pass did not author the submitted drafts. The seven original
`written_by: GPT-6-Astra high` fields are preserved. The checker identity
was verified from current session `turn_context` metadata (`model` =
`gpt-6-astra`, `effort` = `high`), independently confirmed by the coordinating
agent. The application name and automated approval-review model were not
used as attribution evidence.

All seven final articles were checked against live sources, including their
leads, infoboxes, body paragraphs, dates, named parties, and reference
metadata. All 33 unique retained reference URLs opened successfully through
the web tool. Redirecting ethereum.org `/en/` URLs resolve to the matching
current documentation. Existing text and every substantive correction were
reviewed against the sources before setting `status: ai-fact-checked`,
`checked: 2026-10-31`, and `checked_by: gpt-6-astra high`.

## Coverage and corrections

| Article | Claim coverage and live source evidence | Corrections and final disposition |
|---|---|---|
| `account-abstraction.md` | ERC-4337 specification: operation flow and payment model. EIP-7702: delegation lifecycle, example capabilities, and security considerations. Ethereum account-abstraction and Pectra pages: policy examples and activation. | Core draft supported. Added the material 2026 EIP-8141 development, explicitly Draft and prospective; checked its abstract/status against the specification and Hegotá timing against Ethereum's live roadmap. |
| `multisignature-wallet.md` | BIP 11: threshold semantics and history; BIP 16: script-hash spending; BIP 174: portable partial signing. Safe account/module documentation: contract authority and extensions. Sygnia's investigation: incident claims. | Qualified single-key resistance to thresholds greater than one. Replaced the BlockSec-only incident citation with the engaged forensic investigator's report and revised the passage to the report's specific findings. |
| `safe.md` | Safe history, account concepts, modules, guards, and token page cover names, dates, governance, and contract behaviour. Project history and product claims remain attributed. Sygnia supports the incident account. | Strengthened incident sourcing and distinguished interface manipulation from an unsupported allegation of a core-contract vulnerability. Added the 15 October 2026 Aegis announcement with explicit project attribution and its stated scope limit. |
| `zero-knowledge-proof.md` | Ethereum's overview: terminology, properties, membership example. Original Groth and STARK paper abstracts: authorship, dates, construction claims. Ethereum rollup documentation: execution, public data, and privacy distinction. | Added the versioned Arkworks implementation source to explicitly establish the later “Groth16” name's connection to the 2016 paper. No numerical cryptographic-performance generalisations were introduced. |
| `inter-blockchain-communication.md` | IBC Classic page, Interchain Developer Academy, ICS-20 specification and pseudocode, and Cosmos's technical Eureka walkthrough cover the entire original article. | Added attributed 2026 developments from the project's current history. Kept Classic architecture distinct from v2 and Eureka. Did not import promotional adoption counts or the project's blanket security claims. |
| `proof-of-work.md` | Bitcoin white paper, Bitcoin Developer Guide block-chain/mining chapters, and Ethereum Merge documentation cover history, mechanism, settlement limits, economics, and Ethereum's transition. | Corrected an overbroad distinction between shares and blocks: a share can meet the network target. Removed the unsupported cross-protocol hashing/adjustment generalisation. |
| `proof-of-stake.md` | Ethereum PoS, weak-subjectivity, pooled-staking, and Merge documentation cover consensus duties, penalties, trust, pool risks, and the transition. | Replaced an unconditional statement about all conflicting finalised histories with the documentation's attributed economic-finality explanation. Other claims supported; no obsolete fixed validator maximum was present. |

## Opened retained references

The following lists are the article reference sets actually opened and
inspected. Repeated sources were checked for their use in each article.

- Account abstraction: [ERC-4337](https://eips.ethereum.org/EIPS/eip-4337), [EIP-7702](https://eips.ethereum.org/EIPS/eip-7702), [account-abstraction roadmap](https://ethereum.org/roadmap/account-abstraction/), [Pectra](https://ethereum.org/roadmap/pectra/), [EIP-8141](https://eips.ethereum.org/EIPS/eip-8141), [upgrade roadmap](https://ethereum.org/roadmap/).
- Multisignature wallet: [BIP 11](https://bips.dev/11/), [BIP 16](https://bips.dev/16/), [BIP 174](https://bips.dev/174/), [Safe account concepts](https://docs.safe.global/advanced/smart-account-concepts), [Safe modules](https://docs.safe.global/advanced/smart-account-modules), [Sygnia investigation](https://www.sygnia.co/blog/sygnia-investigation-bybit-hack/).
- Safe: [history](https://safefoundation.org/blog/history-of-safe), [account concepts](https://docs.safe.global/advanced/smart-account-concepts), [modules](https://docs.safe.global/advanced/smart-account-modules), [guards](https://docs.safe.global/advanced/smart-account-guards), [token](https://safefoundation.org/token), [Sygnia investigation](https://www.sygnia.co/blog/sygnia-investigation-bybit-hack/), [Aegis announcement](https://safefoundation.org/blog/safenet-aegis-live).
- Zero-knowledge proof: [overview](https://ethereum.org/zero-knowledge-proofs/), [Groth paper](https://eprint.iacr.org/2016/260), [STARK paper](https://eprint.iacr.org/2018/046), [rollups](https://ethereum.org/developers/docs/scaling/zk-rollups/), [Arkworks 0.6.0 source](https://docs.rs/ark-groth16/0.6.0/src/ark_groth16/lib.rs.html).
- IBC: [Classic](https://ibcprotocol.dev/how-ibc-classic-works), [clients](https://ida.interchain.io/academy/3-ibc/4-clients), [ICS-20](https://github.com/cosmos/ibc/tree/main/spec/app/ics-020-fungible-token-transfer), [Eureka](https://cosmos.network/blog/ibc-eureka-technical-walkthrough), [project history](https://ibcprotocol.dev/about).
- Proof of work: [Bitcoin white paper](https://bitcoin.org/bitcoin.pdf), [block-chain guide](https://developer.bitcoin.org/devguide/block_chain.html), [mining guide](https://developer.bitcoin.org/devguide/mining.html), [Merge](https://ethereum.org/en/roadmap/merge/).
- Proof of stake: [PoS](https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/), [weak subjectivity](https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/weak-subjectivity/), [pools](https://ethereum.org/en/staking/pools/), [Merge](https://ethereum.org/en/roadmap/merge/).

## Freshness search and limitations

Searched for changes through 31 October 2026 across Ethereum's protocol and
research documentation, Safe announcements and investigation reports,
IBC/Cosmos project publications, and Bitcoin protocol material. Searches
included account abstraction/EIP-8141, Safe/Safenet releases, Bybit
investigation updates, IBC v2/Eureka development, proof-of-stake/finality
upgrades, proof-of-work changes, and zero-knowledge research. Material
findings affecting these articles are incorporated above.

Supplementary opened evidence included [NCC Group's Bybit analysis](https://www.nccgroup.com/research/in-depth-technical-analysis-of-the-bybit-hack/),
the original [BlockSec analysis](https://blocksec.com/blog/bybit-1-5-b-hack-in-depth-analysis-of-the-malicious-safe-wallet-upgrade-attack),
[Safe's current publication index](https://safefoundation.org/blog), and
[Ethereum's active research overview](https://ethereum.org/community/research/).
Search-only results were not used as retained claim evidence.

This is an editorial source check, not a contract audit or a cryptographic
proof verification. The published paper abstracts directly support the
limited construction claims retained; no claim is made to have formally
verified the mathematics. Project roadmaps are plans, and project release
or adoption claims are not independent measurements. No assertion of
comprehensive protection, guaranteed investment outcomes, or exhaustive
coverage of every implementation is made. No retained reference was
inaccessible and no unresolved factual blocker remains.

## Final validation

After corrections, re-read the final text against the sources and checked
all factual paragraphs for footnotes, infobox entries for cited body
coverage, and footnote markers/definitions for exact agreement. All seven
passed the repository's `build.validate` metadata function and a scoped
paragraph/reference consistency check using the repository's existing
virtual environment. System `python3` initially lacked `markdown`; rerunning
with that virtual environment resolved this without dependency changes.

The coordinating agent is responsible for the required complete static
build and `scripts/check.py` before publication. This subtask did not write
shared build output, commit, push, or modify the index/catalogue. No
automation, attribution-recovery logic, or migration code was changed.

Integration: normalized checker display credit to `GPT-6-Astra high` to
match the same verified model/effort elsewhere; no change to identity or
check date. Restored a blank line below Safe’s References heading.
