---
title: Base
ticker: —
category: Layer 2
status: ai-fact-checked
checked: 2026-10-30
checked_by: Opus 5.5 High
updated: 2026-10-30
---

# Base

**Base** is a layer 2 network on [Ethereum](ethereum.md) developed and
operated by Coinbase, the US cryptocurrency exchange. It processes
transactions off Ethereum, posts the data back to it, and uses ETH to pay
for gas. Base was announced in February 2023 and opened to the public in
August 2023. It was built on Optimism's OP Stack and was part of the
Optimism Superchain until February 2026, when Base said it would move to
its own software stack. As of October 2026 Base has no network token,
although Coinbase has said it is exploring one.[^theblock-launch][^theblock-token][^theblock-unified]

| | |
|---|---|
| Type | Rollup on Ethereum |
| Developer | Coinbase |
| Creator | Jesse Pollak |
| Announced | 2023-02-23 (testnet) |
| Mainnet | 2023-08-09 (public) |
| Chain ID | 8453[^base-network] |
| Gas token | ETH |
| Network token | None (as of October 2026) |
| Software | OP Stack (2023–2026); base/base (from 2026) |
| Sequencer | Single centralised sequencer |
| Proof system | TEE and ZK multi-proofs (since 2026-05-28) |
| Withdrawal window | 5 days with one proof; 1 day with two |
| Data availability | Ethereum (blobs) |
| L2Beat stage | Stage 1 |
| Live data | [L2Beat](https://l2beat.com/scaling/projects/base), [DefiLlama](https://defillama.com/chain/Base), [BaseScan](https://basescan.org) |

## History

### Announcement

Coinbase unveiled Base at the ETHDenver conference on 23 February 2023,
launching a testnet at the same time. Base was built on the OP Stack, an
open-source framework for layer 2 networks created by Optimism, and
Coinbase said it would join Optimism as a core developer of the OP Stack.
Jesse Pollak, then Coinbase's senior director of engineering, said Base
would not have a token: "These networks don't need tokens to be
successful." Coinbase Ventures announced a Base Ecosystem Fund to invest
in early-stage projects building on the network.[^theblock-launch]

Pollak had joined Coinbase in 2017 and is described in press coverage as
the creator of Base.[^coindesk-pollak] By mid-2023 he was described as
the lead for Base and head of protocols at Coinbase.[^techcrunch-mainnet]

### Launch and Onchain Summer

The testnet ran from late February to mid-July 2023, when Base opened its
mainnet to developers only. The network opened to the public on 9 August
2023, alongside "Onchain Summer", a month of promotions in which Coinbase
and more than 50 brands, platforms and creators, including Coca-Cola and
Atari, released NFTs and other projects on Base.[^techcrunch-mainnet]

During the developer-only phase, users bridged funds to Base before its
official opening. Much of the early trading volume came from BALD, a
memecoin that rose and then collapsed. Pollak called the activity an
unplanned result of an open, permissionless network.[^techcrunch-mainnet]

Friend.tech, a social app linked to Twitter in which users trade "shares"
in other users' accounts, launched on Base in August 2023.
Decrypt reported that on 20 August 2023 Base processed more than 900,000
transactions, nearly double the daily totals of Arbitrum and Optimism at
the time.[^decrypt-friendtech]

### Agreement with Optimism

Under an agreement announced in August 2023, Base could earn up to 118
million OP tokens over six years. In return, Base would contribute to the
Optimism Collective the greater of 2.5% of its total sequencer revenue or
15% of its profit after the cost of posting data to Ethereum. According
to The Block, the agreement was part of a "shared commitment to
the rules for upgrades and sequencing of OP Chains", with upgrades
decided by Optimism governance.[^theblock-op-grant][^base-superchain] Base's voting power
in Optimism governance was capped at 9%.[^base-superchain][^op-forum]

According to DL News, Base contributed 8,387 ETH to the Collective over
the course of the partnership, about 41% of the Collective's lifetime
revenue.[^dlnews-op]

### Blobs and growth

Ethereum's Dencun upgrade, scheduled for 13 March 2024, introduced blobs
(EIP-4844), and Base adopted them through its Ecotone upgrade on 14 March
2024, saying it would support them from "day 1". Blobs gave
rollups a separate, cheaper way to post data to Ethereum, and Base had
predicted fee reductions of 10 to 100 times.[^theblock-4844][^base-upgrades]
The Defiant reported that fees on the leading layer 2s that adopted
blobs fell by between 50% and 98%.[^defiant-dencun] Research by Galaxy found that in the 150
days after the upgrade Base spent more on blobs than any other rollup, and
that the combined margins of Base, OP Mainnet and Arbitrum rose
sharply. It also found that Base's transaction failure rate peaked at
21%, which it attributed largely to bots.[^galaxy-dencun]

Coinbase launched Smart Wallet on 5 June 2024. The wallet replaced
recovery phrases with passkeys, could be created with a fingerprint, Face
ID or a hardware key, and let developers sponsor users' gas fees. Its
launch opened that year's Onchain Summer campaign.[^decrypt-smartwallet]

### Decentralisation steps

At launch, proposing and challenging Base's state was permissioned. In
August 2023 Pollak acknowledged that "the current systems' upgradability
and challenging authorizations are still permissioned".[^theblock-permissionless]
Base deployed permissionless fault proofs on mainnet on 30 October 2024,
allowing anyone to challenge invalid withdrawal claims.[^base-faultproofs] On 29 April 2025 Base
said it had reached Stage 1 in the rollup decentralisation framework
proposed by Vitalik Buterin, after adding a Security Council of 10 independent entities. Upgrades
required 75% agreement among the council, Base and Optimism.[^theblock-stage1]

### Content coins and the Base App

On 16 April 2025 Base's official X account posted "Base is for everyone"
and then said it had "coined it" on Zora, a platform that turns posts into
tradable tokens. The token's price surged and then fell about 90% within
minutes. Coinbase said that "Base did not launch a token, this is not an
official Base token, and Base did not sell this token". Pollak described
it as a "content coin" rather than a memecoin.[^dlnews-coin][^decrypt-coin]

On 16 July 2025 Coinbase renamed Coinbase Wallet the Base App and
relaunched it as what it called an "everything app". It combined a social
feed built on the Farcaster protocol, posts tokenised through Zora,
trading, mini-apps, USDC payments and XMTP messaging. Accounts were
created as smart wallets called Base Accounts. Coinbase also described
Base as three parts: Base Chain, Base Build for developers, and the Base
App.[^theblock-baseapp]

On 9 February 2026 the Base App removed its Farcaster-powered feed, and
Coinbase began winding down its creator rewards programme.
Pollak said that "the app needs to have one primary focus, and that thing
is trading".[^theblock-talk] In a podcast interview reported on 3 March
2026, Coinbase chief executive Brian Armstrong said that the app's social features "didn't quite
work".[^theblock-socialfi] In July 2026 he said that content
coins "didn't work" and that Base had pivoted away from them early in the
year, while defending its focus on AI agents.[^defiant-armstrong][^cryptonews-armstrong]
On 15 July 2026 Pollak handed leadership of the app to Jordan "Cobie" Fish
to focus on the Base chain, saying its social bets, including creator
coins, had "disintegrated completely".[^theblock-cobie] On 10 September
2026 Coinbase renamed the Base App back to Coinbase Wallet, describing it
as a multichain trading app.[^theblock-wallet]

### Token exploration

At the BaseCamp conference on 15 September 2025, Pollak said Base was
"beginning to explore" a network token, reversing Coinbase's earlier
position. Armstrong confirmed this on X but said there were no definitive
plans. At the same event Pollak announced a bridge between Base and
[Solana](solana.md).[^theblock-token] In November 2025 Pollak launched a
personal memecoin, JESSE, which drew criticism from users who said bots
had taken much of the supply. A Base spokesperson said the company stood
behind the project.[^coindesk-pollak] As of October 2026 no Base network
token has been launched.

### Unified stack

On 18 February 2026 Base announced that it would move to "a unified,
Base-operated stack" in a single repository, base/base, built on
open-source components such as Reth.[^base-unified] Base said the code for components
such as the sequencer had been owned by several teams across several
repositories, creating coordination overhead. It said it would remain
compatible with the OP Stack specification in the short term, would
replace Optimism on its Security Council with an independent signer, and
would require node operators to run base/base releases. It remained a
customer of Optimism's "OP Enterprise" service.[^base-unified][^theblock-unified][^dlnews-op]
Base's head of product, Wilson Cusack, said the change would give it
"our own spec, code, and infra". Base planned six hard forks a year and
set a target of 1 gigagas per second.[^base-unified][^decrypt-unified]

An Optimism spokesperson said it was "grateful for our three-year
partnership with Base". OP Labs chief executive Jing Wang wrote that the
move "is a hit to near-term onchain revenues".[^dlnews-op] On the
Optimism governance forum, the Optimism Foundation said the Superchain
revenue share "will not continue", that Base was not entitled to the
unvested portion of its OP grant, and that the 9% voting cap still
applied.[^op-forum]

### Independent upgrades

Base's first independent upgrade, Azul, activated on mainnet on 28 May
2026. It replaced optimistic fault proofs with a multi-proof system and
made base-reth-node the only execution client.[^base-upgrades][^base-azul][^theblock-azul]
Beryl followed on 25 June 2026. It introduced B20, a token standard
compatible with ERC-20 but implemented as a native precompile inside the
node, and shortened the single-proof withdrawal window from seven days to
five.[^base-beryl] On 24 August 2026 tokenised stocks issued by Coinbase
and built on B20 went live on Base for users outside the US.[^base-stocks] Cobalt, activated on 30 September 2026, extended B20,
added "validity transactions" that are included only if specified
onchain conditions hold, and moved verification of TEE signer
registrations fully onchain.[^base-cobalt] As of October 2026 the next
upgrade, Denim, was targeted for November 2026, and a further upgrade,
Everest, had no date.[^base-upgrades]

## Technology

### Transaction flow

A single centralised sequencer run by Base orders transactions. Base runs five
sequencer instances coordinated by op-conductor, but only the leader
produces blocks, and L2Beat notes that the replicas "do not create
independent operators or censorship resistance". Blocks are sealed every
two seconds, and Flashblocks give preconfirmations about every 200
milliseconds, which the protocol does not enforce. Transaction data is
posted to Ethereum as blobs.[^l2beat]

Users can bypass the sequencer by submitting a transaction to a contract
on Ethereum. If it is not included, it can be forced into the chain after
up to 12 hours.[^l2beat]

### Proving

Under the Azul design, each proposed checkpoint of Base's state is
submitted to an AggregateVerifier contract on Ethereum, which accepts one
or two proofs. The usual first proof comes from provers running in AWS
Nitro enclaves, a trusted execution environment (TEE), which re-execute
blocks and sign the result. Zero-knowledge (ZK) provers can be run by
anyone and can back a proposal or dispute an invalid one.[^base-azul]
Permissionless ZK proofs can override TEE proofs if the two
conflict.[^theblock-azul] A proposal with a single proof can be finalised
after five days, and one with both after one day.[^base-beryl]

L2Beat classifies Base as Stage 1 and states that users can exit in the
presence of a malicious operator even if the Security Council
disappears. It notes that contracts can be upgraded with no delay, so
users have no window to exit before an unwanted upgrade, and that the
Security Council's powers are not limited to provable bugs, which keeps
Base from Stage 2.[^l2beat]

## Governance

Base has no token governance. Contract upgrades require the approval of a
two-of-two multisig made up of the Base Coordinator Multisig (three of
six signers) and the Base Security Council (eight of 11). A separate
three-of-12 multisig can change some system parameters and pause
withdrawals for up to three months.[^l2beat] Before February 2026,
Optimism was one of the parties whose approval upgrades
required.[^theblock-stage1][^theblock-unified]

## Incidents and controversies

- **Centralisation.** At launch critics argued that Coinbase's sole
  control of the sequencer made Base centralised, and Gnosis founder Martin
  Köppelmann pointed to Base's lack of fraud proofs, saying the Coinbase
  team would need to provide more details about measures that might reduce
  Coinbase's control. Pollak said that Coinbase
  "cannot unilaterally upgrade contracts or land invalid output
  proposals".[^theblock-permissionless] As of October 2026 the sequencer is
  still centralised, and L2Beat rates it as having no real-time
  censorship resistance beyond the 12-hour forced-inclusion
  path.[^l2beat]
- **Sequencer fees (February 2025).** Onchain observers noted that Base's
  sequencer fee revenue was being sent to the Coinbase exchange, and
  critics, including Sonic Labs co-founder Andre Cronje, questioned whether
  Base was aligned with Ethereum. A Base strategy team member said the ETH was held
  by Coinbase for "security and auditing purposes".[^theblock-fees]
- **"Base is for everyone" (April 2025).** DL News reported that onchain
  records showed a few buyers bought early and sold at a profit.
  Blockchain developer Suhail Kakar called it "deeply disappointing", while Base defended it
  as an experiment in public.[^dlnews-coin][^decrypt-coin]
- **Sequencer outage (August 2025).** On 5 August 2025 block production
  stopped for 33 minutes after the active sequencer fell behind and
  automatic failover chose a replacement that was still being provisioned.
  Engineers moved block production to a healthy sequencer by hand.[^theblock-outage]
- **Block production outages (June 2026).** On 25 June 2026 the chain
  halted for 116 minutes, and on 26 June for 20 minutes. Base said a bug
  in the sequencer's block-building logic let stale state persist after a
  failed transaction, producing a block that other nodes rejected. A
  separate bug slowed recovery. Base said "all funds on Base were
  safe".[^base-postmortem][^theblock-june]
- **Departure from the Superchain.** Base's move to its own stack ended
  its revenue share with the Optimism Collective. A participant in the
  Optimism governance forum asked whether the original agreements had allowed this and
  why it had not been disclosed. The Foundation replied that Base's
  participation was "never a given".[^op-forum]

## Timeline

| Date | Event |
|---|---|
| 2023-02-23 | Base announced at ETHDenver; testnet launches |
| 2023-07 | Mainnet opens to developers |
| 2023-08-09 | Mainnet opens to the public; Onchain Summer begins |
| 2023-08 | Friend.tech launches on Base |
| 2023-08-24 | Revenue-share agreement with Optimism announced |
| 2024-03-14 | Ecotone upgrade: blob support |
| 2024-06-05 | Coinbase Smart Wallet launches |
| 2024-10-30 | Permissionless fault proofs on mainnet |
| 2025-02 | Criticism of sequencer fees sent to Coinbase |
| 2025-04-16 | "Base is for everyone" content coin |
| 2025-04-29 | Base reaches Stage 1 |
| 2025-07-16 | Coinbase Wallet renamed Base App |
| 2025-08-05 | 33-minute sequencer outage |
| 2025-09-15 | Base says it is exploring a network token |
| 2026-02-09 | Base App drops social feed to focus on trading |
| 2026-02-18 | Base announces move to its own stack |
| 2026-05-28 | Azul upgrade: TEE and ZK multi-proofs |
| 2026-06-25 | Beryl upgrade: B20 tokens; 116-minute outage |
| 2026-06-26 | 20-minute outage |
| 2026-07 | Armstrong says content coins "didn't work" |
| 2026-07-15 | Pollak hands Base App leadership to Cobie |
| 2026-08-24 | Coinbase tokenised stocks launch on Base |
| 2026-09-10 | Base App renamed back to Coinbase Wallet |
| 2026-09-30 | Cobalt upgrade |

## See also

- [Ethereum](ethereum.md)
- [Optimism](optimism.md)
- [Arbitrum](arbitrum.md)
- [USDC](usdc.md)
- [Solana](solana.md)

## References

[^theblock-launch]: The Block (2023). *Coinbase unveils its Ethereum Layer 2 network that won't have a token*. <https://www.theblock.co/post/214183/mmcsweeney@theblock.co>
[^theblock-token]: The Block (2025). *Coinbase-incubated Base network 'beginning to explore' native token, creator Jesse Pollak says*. <https://www.theblock.co/post/370668/coinbase-incubated-base-network-beginning-to-explore-native-token-creator-jesse-pollak-says>
[^theblock-unified]: The Block (2026). *Coinbase-incubated Base network to ditch Optimism for 'unified solution'*. <https://www.theblock.co/post/390380>
[^coindesk-pollak]: CoinDesk (2025). *Most Influential: Jesse Pollak*. <https://www.coindesk.com/tech/2025/12/12/most-influential-jesse-pollak>
[^techcrunch-mainnet]: TechCrunch (2023). *Coinbase's blockchain Base to launch to the public next week*. <https://techcrunch.com/2023/08/03/coinbases-blockchain-base-to-launch-to-the-public-next-week/>
[^decrypt-friendtech]: Decrypt (2023). *Base network sees activity soar past Arbitrum, Optimism amid Friend.tech frenzy*. <https://decrypt.co/153133/base-network-sees-activity-soar-past-arbitrum-optimism-friend-tech-frenzy>
[^theblock-op-grant]: The Block (2023). *Base set to receive 118M OP tokens over six years in governance agreement*. <https://www.theblock.co/post/247532/base-optimism-revenue>
[^op-forum]: Optimism governance forum (2026). *Base, the Superchain, and Governance: Questions That Merit Answers*. <https://gov.optimism.io/t/base-the-superchain-and-governance-questions-that-merit-answers/10612>
[^dlnews-op]: DL News (2026). *Optimism token price plunges 25% as Coinbase cuts off DAO from millions in revenue*. <https://www.dlnews.com/articles/defi/optimism-token-price-plunges-as-base-leaves-superchain/>
[^theblock-4844]: The Block (2024). *Base says it will support EIP-4844 from 'day 1' following Dencun upgrade*. <https://www.theblock.co/post/281258/base-to-support-eip-4844-from-day-1-following-dencun-upgrade>
[^base-upgrades]: Base documentation. *Upgrades overview*. <https://docs.base.org/upgrades/overview>
[^defiant-dencun]: The Defiant (2024). *Transaction fees on layer 2 plummet post Dencun*. <https://thedefiant.io/news/cefi/transaction-fees-on-layer-2-plummet-post-dencun>
[^galaxy-dencun]: Pokorny, Z., Galaxy Research (2024). *150 days after Dencun*. <https://www.galaxy.com/insights/research/ethereum-150-days-after-dencun>
[^decrypt-smartwallet]: Decrypt (2024). *Coinbase debuts Smart Wallet, gunning to bring 1 billion users to crypto*. <https://decrypt.co/233925/coinbase-debuts-smart-wallet-gunning-to-bring-1-billion-users-to-crypto>
[^theblock-permissionless]: The Block (2023). *Base is 'permissionless,' says Coinbase's Jesse Pollak*. <https://www.theblock.co/post/244629/coinbase-base-jesse-pollak>
[^theblock-stage1]: The Block (2025). *Base reaches 'stage 1' in Ethereum rollup decentralization with fault proofs and security council*. <https://www.theblock.co/amp/post/352320/base-stage-1>
[^dlnews-coin]: DL News (2025). *Coinbase distances itself from 'deeply disappointing' Base memecoin*. <https://dlnews.com/articles/defi/coinbase-distances-itself-from-base-memecoin-made-on-zora/>
[^decrypt-coin]: Decrypt (2025). *Coinbase's Base promotes unofficial meme coin—traders ape in and get rekt*. <https://decrypt.co/315204/coinbases-base-promotes-unofficial-meme-coin-traders-ape-get-rekt>
[^theblock-baseapp]: The Block (2025). *Coinbase unveils Base App, rebrands wallet as all-in-one social and trading platform*. <https://www.theblock.co/post/362713/coinbase-unveils-base-app-rebrands-wallet-as-all-in-one-social-and-trading-platform>
[^theblock-talk]: The Block (2026). *Base App removes Farcaster-powered Talk feed to sharpen focus on onchain trading*. <https://www.theblock.co/post/389191>
[^cryptonews-armstrong]: crypto.news (2026). *Coinbase CEO admits Base 'messed up' on content coins*. <https://crypto.news/coinbase-ceo-admits-base-messed-up-on-content-coins/>
[^defiant-armstrong]: The Defiant (2026). *Coinbase CEO says Base's content coins 'didn't work'*. <https://thedefiant.io/news/blockchains/coinbase-ceo-says-base-s-content-coins-didn-t-work>
[^decrypt-unified]: Decrypt (2026). *Coinbase-backed Ethereum network Base to dump Optimism tech as potential token looms*. <https://decrypt.co/358469/coinbase-ethereum-network-base-dump-optimism-tech-potential-token-looms>
[^base-azul]: Base documentation. *Azul: proofs*. <https://docs.base.org/upgrades/azul/proofs>
[^theblock-azul]: The Block (2026). *Coinbase-incubated Base launches Azul testnet upgrade with multiproofs to advance decentralization*. <https://www.theblock.co/post/398421/coinbase-incubated-base-launches-azul-testnet-upgrade-with-multiproofs-to-advance-decentralization>
[^base-beryl]: Base documentation. *Beryl overview*. <https://docs.base.org/base-chain/specs/upgrades/beryl/overview.md>
[^base-cobalt]: Base documentation. *Cobalt overview*. <https://docs.base.org/base-chain/specs/upgrades/cobalt/overview.md>
[^l2beat]: L2Beat. *Base*. <https://l2beat.com/scaling/projects/base>
[^theblock-fees]: The Block (2025). *Base defends moving sequencer fees to Coinbase custody for 'security and audit' reasons*. <https://www.theblock.co/post/339698/base-defends-moving-sequencer-fees-to-coinbase-custody-for-security-and-audit-reasons>
[^theblock-outage]: The Block (2025). *Base network says sequencer handoff failure caused 33-minute mainnet outage*. <https://www.theblock.co/post/365732/base-network-sequencer-failure>
[^base-postmortem]: Base (2026). *Postmortem: June 25th block production outage*. <https://base.org/blog/postmortem-june-25th-block-production-outage>
[^theblock-june]: The Block (2026). *Coinbase-incubated Base suffers mainnet chain stall interrupting block production*. <https://theblock.co/news/ecosystems/2026-06-25-coinbase-incubated-base-blockchain-suffers-unsafe-head-stall-interrupting-block-production-406213>
[^base-network]: Base documentation. *Connecting to Base*. <https://docs.base.org/base-chain/quickstart/connecting-to-base>
[^base-superchain]: Base (2023). *Base's Commitment to Decentralization with the Superchain*. <https://base.org/blog/bases-commitment-to-decentralization-with-the-superchain>
[^base-faultproofs]: Base (2024). *Fault proofs are now live on Base Mainnet*. <https://base.org/blog/fault-proofs-are-now-live-on-base-mainnet>
[^base-unified]: Base (2026). *A new, unified stack for Base Chain*. <https://base.org/blog/next-chapter-for-base-chain-1>
[^theblock-socialfi]: The Block (2026). *Coinbase CEO Brian Armstrong says Base App's SocialFi features 'didn't quite work'*. <https://www.theblock.co/post/392080/coinbase-ceo-brian-armstrong-says-base-apps-socialfi-features-didnt-quite-work>
[^theblock-cobie]: The Block (2026). *Coinbase's Jesse Pollak hands Base app leadership to Cobie after admitting social bets fell short*. <https://www.theblock.co/post/408504/coinbases-jesse-pollak-hands-base-app-leadership-cobie-social-bets-fell-short>
[^theblock-wallet]: The Block (2026). *Coinbase rebrands Base App back to Coinbase Wallet after just over a year as social experiment falls short*. <https://www.theblock.co/news/defi/2026-09-10-coinbase-rebrands-base-app-back-to-coinbase-wallet-after-just-over-a-year-as-social-experiment-falls-short-414115>
[^base-stocks]: Base (2026). *Stocks just got updated*. <https://base.org/blog/tokenized-stocks>
