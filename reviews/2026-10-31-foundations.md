# Foundations, infrastructure and exchanges: fact-check, 31 October 2026

Checker and substantive corrections/additions: **GPT-6-Astra high**. This was an independent checking pass over existing drafts, followed by verification of the corrected text. Original `written_by: Unknown` credits were preserved; these are edits, not complete rewrites. No human-review credit was added.

Attribution evidence: the supervising agent verified the authenticated current runtime session `01a1921e-8156-76e1-a4cb-5e96899f237e`, whose latest `turn_context` (`01a19233-2efd-7993-916a-66c3ed4bde63`) records `model: gpt-6-astra`, `effort: high`. This worker was spawned with full-history inheritance and no override; the tool contract guarantees inherited model and effort. The session evidence is local at `/Users/sirodoht/.codex/sessions/2026/10/31/rollout-2026-10-31T13-20-35-01a1921e-8156-76e1-a4cb-5e96899f237e.jsonl`. Historical writer identity remains unknown.

## Method and scope

Read AGENTS.md and POLICY.md. Checked the lead, infobox, every factual body paragraph, and timelines against live opened sources, not model recollection. All final references listed below were opened and their relevant content read on 31 October 2026; redirects to the publisher's current document were accepted only after checking the destination. Footnote identifiers below map to the exact article references and claim groups. Tables without per-cell citations repeat sourced body/lead claims. Navigation-only See also links are not factual assertions.

Searched for major developments through the check date for all nine subjects, including EIP-7702/current account documentation, rollup stages and 2026 L2Beat changes, bridge standards/CCTP updates, oracle/data-feed changes, Chainlink Q3 2026, MetaMask 2026 reorganisation/security notices, Coinbase 2026 acquisitions/security, and Binance October 2026 incident updates. These are a snapshot through the date, not a guarantee that an undisclosed event does not exist. Circle's legacy-CCTP deprecation notices did not change the version-neutral burn/mint description. Speculative market forecasts, promotional size rankings, and unrelated token-price changes were excluded.

The dated, ongoing Binance incident remains explicitly preliminary. MetaMask's incident and separation plan are attributed to dated announcements rather than presented as completed resolutions. Coinbase's Amplitude impact is explicitly limited to the disclosure available by 31 October.

## Source-access limitations and resolutions

- MetaMask's former recovery and alerts URLs produced JavaScript redirects. Replaced them with readable official pages, then rechecked the relevant text.
- Binance's global 2019 announcement URL failed; the official en-PH copy opened and supports the same dated disclosure.
- Wormhole's original Medium incident post could not be retrieved (403). Used CertiK's published firsthand transaction/code analysis; also consulted Elliptic's incident analysis. No inaccessible Wormhole reference was retained.
- Coinbase's original support X statement returned 403. Amplitude's trust page opened but did not expose the referenced incident update. Used separately published CoinDesk and Decrypt reports quoting the company, with clear attribution and no unsourced technical cause or user count. Decrypt identifies Stephen Graves as editor. Neither inaccessible primary was retained as a supporting reference.

## cryptocurrency-wallet

Result: final factual text verified; `ai-fact-checked`, checked 2026-10-31.

Changes: Added EIP-7702 account delegation so the account taxonomy does not imply all externally owned accounts remain code-free. Preserved BIP-39 assignment and ERC-20 proposal dates.

Coverage: bitcoin: wallet component separation, hardware/offline signing and verification; ethereum/accounts: interfaces, account authority and network state; bip39: assignment date, randomness, optional passphrases and deterministic seed; erc20: allowances and transferFrom; custody: hosted versus user-controlled keys; delegation: account context, batching, sponsorship and delegated authority.

Opened retained references:

- `bitcoin` — Bitcoin developer documentation. *Wallets*. <https://developer.bitcoin.org/devguide/wallets.html>
- `ethereum` — ethereum.org. *Ethereum wallets*. <https://ethereum.org/en/wallets/>
- `accounts` — ethereum.org. *Ethereum accounts*. <https://ethereum.org/en/developers/docs/accounts/>
- `bip39` — Bitcoin Improvement Proposals. *BIP-39: Mnemonic code for generating deterministic keys*. <https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki>
- `erc20` — Vogelsteller, F. and Buterin, V. (2015). *ERC-20: Token Standard*. <https://eips.ethereum.org/EIPS/eip-20>
- `custody` — MetaMask. *What is a self-custodial wallet?* <https://support.metamask.io/start/metamask-is-a-self-custodial-wallet>
- `delegation` — Ethereum Improvement Proposals. *EIP-7702: Set Code for EOAs*. <https://eips.ethereum.org/EIPS/eip-7702>

## smart-contract

Result: final factual text verified; `ai-fact-checked`, checked 2026-10-31.

Changes: Added EIP-7702 delegation and its security implications alongside conventional contract permissions and proxies.

Coverage: intro/accounts: code, state, EVM, deployment gas, composability and permissions; erc20: interface and allowances; proxy: ERC-1967 date, implementation/beacon/admin storage and delegate execution; security: reentrancy, public visibility of private state and compiler/platform risks; oracles: external data; frontier: launch date; delegation: EOA code delegation and account context.

Opened retained references:

- `intro` — ethereum.org. *Introduction to smart contracts*. <https://ethereum.org/en/developers/docs/smart-contracts/>
- `erc20` — Vogelsteller, F. and Buterin, V. (2015). *ERC-20: Token Standard*. <https://eips.ethereum.org/EIPS/eip-20>
- `accounts` — ethereum.org. *Ethereum accounts*. <https://ethereum.org/en/developers/docs/accounts/>
- `proxy` — Palladino, S., Giordano, F. and Croubois, H. (2019). *ERC-1967: Proxy Storage Slots*. <https://eips.ethereum.org/EIPS/eip-1967>
- `security` — Solidity documentation. *Security considerations*. <https://docs.soliditylang.org/en/latest/security-considerations.html>
- `oracles` — ethereum.org. *Oracles*. <https://ethereum.org/en/developers/docs/oracles/>
- `frontier` — Ethereum Foundation (30 July 2015). *Ethereum launches*. <https://blog.ethereum.org/2015/07/30/ethereum-launches>
- `delegation` — Ethereum Improvement Proposals. *EIP-7702: Set Code for EOAs*. <https://eips.ethereum.org/EIPS/eip-7702>

## rollup

Result: final factual text verified; `ai-fact-checked`, checked 2026-10-31.

Changes: Clarified optimistic versus validity verification in the infobox and attached calldata/blob publication to the full rollup documentation. Kept decentralisation stages separate from assurance against bugs.

Coverage: optimistic/zk: execution, commitments, publication, challenges, proof verification, canonical withdrawal timing, sequencer confirmations and public data; blobs: EIP-4844 creation date, separate blob gas/data and temporary availability; stages: June 2023 introduction, decentralisation scope, exit/upgrade/council risks and explicit bug-security limitation.

Opened retained references:

- `optimistic` — ethereum.org. *Optimistic rollups*. <https://ethereum.org/en/developers/docs/scaling/optimistic-rollups/>
- `zk` — ethereum.org. *Zero-knowledge rollups*. <https://ethereum.org/en/developers/docs/scaling/zk-rollups/>
- `blobs` — Buterin, V. et al. (2022). *EIP-4844: Shard Blob Transactions*. <https://eips.ethereum.org/EIPS/eip-4844>
- `stages` — L2Beat. *Stages framework*. <https://l2beat.com/stages>

## blockchain-bridge

Result: final factual text verified; `ai-fact-checked`, checked 2026-10-31.

Changes: Corrected ERC-5164 from an implied established standard to a proposal currently at Last Call. Replaced a generic Wormhole summary with firsthand transaction analysis identifying the verification failure and 120,000 unbacked wrapped ETH.

Coverage: intro: bridging uses, wrapped assets and custody/redemption assumptions, trust spectrum and failure categories; cctp: native USDC burn/mint rather than wrapped liquidity claims; messages: source/sender identifiers, replay prevention and current Last Call status; stages: withdrawal and upgrade powers; wormhole: date, forged message/fake account verification bypass, minted amount and Ethereum redemptions.

Opened retained references:

- `intro` — ethereum.org. *Introduction to blockchain bridges*. <https://ethereum.org/en/bridges/>
- `cctp` — Circle. *Cross-Chain Transfer Protocol*. <https://developers.circle.com/cctp>
- `messages` — Ethereum Improvement Proposals. *ERC-5164: Cross-Chain Execution*. <https://eips.ethereum.org/EIPS/eip-5164>
- `stages` — L2Beat. *Stages framework*. <https://l2beat.com/stages>
- `wormhole` — CertiK (1 August 2022). *Wormhole bridge exploit incident analysis*. <https://www.certik.com/blog/1kDYgyBcisoD2EqiBpHE5l-wormhole-bridge-exploit-incident-analysis>

## blockchain-oracle

Result: final factual text verified; `ai-fact-checked`, checked 2026-10-31.

Changes: Qualified multiple-source aggregation: some Chainlink feeds use a single underlying provider, even where multiple oracle nodes participate.

Coverage: intro: deterministic execution and external-truth limitation; feeds: price data and collateral/settlement use; uniswap: cumulative prices, observations, TWAP and manipulation cost; quality: single sources, liquidity/concentration and wrapped/bridged price divergence; sequencer: outage detection, post-recovery grace periods and application checks.

Opened retained references:

- `intro` — ethereum.org. *Oracles*. <https://ethereum.org/en/developers/docs/oracles/>
- `feeds` — Chainlink. *Data Feeds*. <https://docs.chain.link/data-feeds>
- `uniswap` — Uniswap. *Uniswap v2 oracles*. <https://docs.uniswap.org/contracts/v2/concepts/core-concepts/oracles>
- `quality` — Chainlink. *Selecting quality data feeds*. <https://docs.chain.link/data-feeds/selecting-data-feeds>
- `sequencer` — Chainlink. *L2 sequencer uptime feeds*. <https://docs.chain.link/data-feeds/l2-sequencer-feeds>

## chainlink

Result: final factual text verified; `ai-fact-checked`, checked 2026-10-31.

Changes: Changed the Ethereum infobox row to the directly documented ERC-677 standard. Added the dated Q3 2026 report of CCIP 2.0 and CRE to avoid leaving the project at its 2019 launch.

Coverage: paper: 4 September 2017, Ellis/Juels/Nazarov and original onchain/offchain architecture; launch: Ethereum mainnet announcement 30 May 2019; feeds: report types, aggregation and application use; ocr: observation exchange, aggregate signatures, quorum, transmissions and fallback; token: LINK, ERC-677 and payment abstraction; quality: feed/integration risks; q3: 21 October 2026 review, CCIP 2.0 live in Q3 and institutional CRE workflows.

Opened retained references:

- `paper` — Ellis, S., Juels, A. and Nazarov, S. (4 September 2017). *ChainLink: a decentralized oracle network*. <https://research.chain.link/whitepaper-v1.pdf>
- `launch` — Nazarov, S. (30 May 2019). *Chainlink: connected consensus on Ethereum*. <https://chain.link/blog/chainlink-connected-consensus-on-ethereum>
- `feeds` — Chainlink. *Data Feeds*. <https://docs.chain.link/data-feeds>
- `ocr` — Chainlink. *Offchain Reporting*. <https://docs.chain.link/architecture-overview/off-chain-reporting>
- `token` — Chainlink. *LINK token contracts*. <https://docs.chain.link/resources/link-token-contracts>
- `quality` — Chainlink. *Selecting quality data feeds*. <https://docs.chain.link/data-feeds/selecting-data-feeds>
- `q3` — Chainlink (21 October 2026). *Chainlink quarterly review: Q3, 2026*. <https://chain.link/blog/quarterly-review-q3-2026>

## metamask

Result: final factual text verified; `ai-fact-checked`, checked 2026-10-31.

Changes: Updated two redirected help references to readable current pages. Changed developer wording to original developer and added the September 2026 announced corporate separation. Added the September/October 2026 infrastructure incident, retaining the company attribution and preliminary nature.

Coverage: origins/history: Davis/Finlay, browser work, July 2016 extension and Consensys origins; connect: extension/mobile EVM/Solana connection and QR/deep links; custody/recovery: self-custody, phrase/device password and split encrypted social-login recovery; alerts: URL/chain/request sharing, excluded secrets and optional transaction continuation; support: April 2023 disclosure, approximately 7,000, affected submission dates and wallet distinction; reorganisation: 9 September plan, same company rebranding/new Consensys and expected year-end completion; infrastructure: 30 September notice/1 October update, validators, investigation and no indicated wallet/fund impact.

Opened retained references:

- `origins` — MetaMask (14 July 2022). *How did MetaMask come to life? The origin story, revealed*. <https://metamask.io/news/how-did-metamask-come-to-life-the-origin-story-revealed>
- `history` — Consensys. *Eight years of evolution: the history of Ethereum and Consensys*. <https://consensys.com/blog/eight-years-of-evolution-the-history-of-ethereum-and-consensys>
- `connect` — MetaMask. *MetaMask Connect*. <https://docs.metamask.io/metamask-connect/>
- `custody` — MetaMask. *What is a self-custodial wallet?* <https://support.metamask.io/start/metamask-is-a-self-custodial-wallet>
- `recovery` — MetaMask. *User guide: Secret Recovery Phrase, password, and private keys*. <https://support.metamask.io/start/user-guide-secret-recovery-phrase-password-and-private-keys/>
- `alerts` — MetaMask. *How to manage security alerts to protect your wallet*. <https://support.metamask.io/configure/wallet/security-alerts/>
- `support` — Consensys (14 April 2023). *FAQ: customer support data security incident*. <https://consensys.com/blog/faq-customer-support-data-security-incident>
- `reorganisation` — Consensys (9 September 2026). *Consensys Software Inc. to become two independent companies*. <https://consensys.com/blog/consensys-software-inc-to-become-two-independent-companies-metamask-the-consumer-platform-and-consensys-the-protocols-and-institutional-infrastructure-company>
- `infrastructure` — MetaMask (1 October 2026, including 30 September notice). *User update*. <https://metamask.com/news/user-update>

## coinbase

Result: final factual text verified; `ai-fact-checked`, checked 2026-10-31.

Changes: Added completed Deribit acquisition and October 2026 integration. Added the newly reported Amplitude customer-contact-data incident with two reputable publishers, attribution, UTC publication date and no invented affected-user count.

Coverage: yc/listing: founders, Bitbank, summer 2012, hosted wallet, Nasdaq date/ticker; about/wallets: products and custody distinctions; base: 23 February 2023 announcement and OP Stack; circle: August 2023 issuance/governance, stake and reserve-income relationship; sec: dismissal date and non-merits rationale; incident: May 2025 bribed support access, excluded keys/passwords, ransom refusal and reimbursement promise; deribit/integration: 14 August 2025 close and 1 October 2026 account/position/balance migration; amplitude/amplitude-decrypt: attributed contact-data exposure, no indicated Coinbase-system/funds compromise and no published count.

Opened retained references:

- `yc` — Y Combinator (14 April 2021). *Coinbase from YC to IPO*. <https://www.ycombinator.com/blog/coinbase-from-yc-to-ipo>
- `listing` — Armstrong, B. (14 April 2021). *COIN — it's only the beginning*. <https://www.coinbase.com/en-gb/blog/coin-its-only-the-beginning>
- `about` — Coinbase. *About Coinbase*. <https://www.coinbase.com/about>
- `wallets` — ethereum.org. *Ethereum wallets*. <https://ethereum.org/en/wallets/>
- `base` — Coinbase (23 February 2023). *Introducing Base*. <https://www.coinbase.com/blog/introducing-base>
- `circle` — Circle and Coinbase (21 August 2023). *Ushering in the next chapter for USDC*. <https://www.circle.com/blog/ushering-in-the-next-chapter-for-usdc>
- `sec` — SEC (27 February 2025). *SEC announces dismissal of civil enforcement action against Coinbase*. <https://www.sec.gov/newsroom/press-releases/2025-47>
- `incident` — Coinbase (15 May 2025). *Protecting our customers — standing up to extortionists*. <https://www.coinbase.com/blog/protecting-our-customers-standing-up-to-extortionists>
- `deribit` — Coinbase (14 August 2025). *Deribit joins Coinbase: unlocking the future of global crypto derivatives*. <https://investor.coinbase.com/news/news-details/2025/Deribit-Joins-Coinbase-Unlocking-the-Future-of-Global-Crypto-Derivatives/>
- `integration` — Coinbase (updated 2 October 2026). *Coinbase International Exchange and Deribit are coming together: what you need to know*. <https://help.coinbase.com/en/international-exchange/deribit/what-you-need-to-know>
- `amplitude` — Godbole, O. (28 October 2026 UTC). *Coinbase says user funds are safe after third-party vendor exposes customer contact info*. CoinDesk. <https://www.coindesk.com/tech/2026/10/28/coinbase-says-customer-funds-are-safe-after-third-party-vendor-exposes-customer-contact-info>
- `amplitude-decrypt` — Decrypt (28 October 2026). *Coinbase customer data hit in analytics vendor breach, funds not impacted*. Edited by Stephen Graves. <https://decrypt.co/382009/coinbase-customer-data-hit-in-analytics-vendor-breach-funds-not-impacted>

## binance

Result: final factual text verified; `ai-fact-checked`, checked 2026-10-31.

Changes: Changed founder list to nonexhaustive because the current company page also credits Heina Chen. Added FCA permissions cancellation in May 2023. Corrected 2019 other-information exposure from definite to potential and replaced the inaccessible regional URL with the working publisher copy. Rechecked the October 2026 theft as preliminary company reporting.

Coverage: about/us: July 2017, founders, October 2026 co-CEOs and Binance.US/BAM September 2019 technology relationship; fca: June/August 2021 restrictions and 30 May 2023 cancellation; doj: guilty pleas, offences, penalties and monitor; sec/pardon: May 2025 discretionary civil dismissal and 21 October 2025 signed clemency warrant; 2019: 7,000 BTC, credentials, suspension and SAFU; bridge: 2 million BNB, forged proof and chain halt; incident: 29 October 20:05 UTC, approximate $6.3bn, frozen ~$3bn, set-aside >$6.34bn, expanded investigation/no key-leak evidence and service status in update #2.

Opened retained references:

- `about` — Binance. *About*. Accessed 31 October 2026. <https://www.binance.com/en/about>
- `us` — Binance.US (3 June 2026). *About Binance.US*. <https://support.binance.us/en/articles/9842963-about-binance-us>
- `fca` — Financial Conduct Authority (26 June 2021; subsequently updated). *Consumer warning on Binance Markets Limited and the Binance Group*. <https://www.fca.org.uk/news/news-stories/consumer-warning-binance-markets-limited-and-binance-group>
- `doj` — US Department of Justice (21 November 2023). *United States v. Changpeng Zhao*. <https://www.justice.gov/criminal/case/united-states-v-changpeng-zhao>
- `sec` — SEC (29 May 2025). *Litigation release 26316*. <https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26316>
- `pardon` — US Department of Justice (21 October 2025). *Executive grant of clemency: Changpeng Zhao*. <https://www.justice.gov/pardon/media/1416576/dl>
- `2019` — Binance (7 May 2019; subsequently updated). *Binance security breach update*. <https://www.binance.com/en-PH/support/announcement/detail/360028031711>
- `bridge` — BNB Chain (7 October 2022). *BNB Chain ecosystem update*. <https://www.bnbchain.org/en/blog/bnb-chain-ecosystem-update>
- `incident` — Binance (30 October 2026). *Security incident update #2*. <https://www.binance.com/en/support/announcement/detail/d3306d9dca5243548c813b605e1d1751>

## Final verification

Re-read all nine complete articles after the edits and compared each correction/addition to the live evidence. No unsupported final factual claim was identified. Programmatic citation audit passed for all nine: every marker defined and every definition used. All original writer credits remain unchanged. `git diff --check` passed.

The supervising agent reviewed the integrated diffs and is responsible for the required combined static build and `scripts/check.py` after all agents finish. This worker did not run concurrent builds in shared `dist`; the final site-wide build/check result must be recorded by the supervisor before delivery. No deployment or commit was made.
