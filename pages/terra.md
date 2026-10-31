---
title: Terra
ticker: LUNA
category: Layer 1
written_by: Opus 5.5 High
status: ai-fact-checked
checked: 2026-10-30
checked_by: Opus 5.5 High
updated: 2026-10-30
---

# Terra

**Terra** is a proof-of-stake blockchain built with the Cosmos SDK and
Tendermint consensus, launched in 2019 by Terraform Labs, a Singapore
company co-founded by Do Kwon and Daniel Shin. Its staking and
governance token was **LUNA**, and it issued algorithmic stablecoins,
chief among them TerraUSD (UST), which were meant to hold their peg
through a mint-and-burn swap with LUNA rather than through reserves of
cash.[^classic-protocol][^sec-2023] In May 2022 UST lost its dollar peg
and both tokens fell close to zero, wiping out at least US$40 billion of
market value according to the SEC.[^sec-complaint] The original chain
continues as Terra Classic (LUNC), and a new chain without UST was
launched under the Terra and LUNA names.[^terra-protocol][^block-phoenix] Kwon
later pleaded guilty to fraud in the United States and was sentenced to
15 years in prison.[^reuters-sentence]

| | |
|---|---|
| Type | Proof-of-stake blockchain (Cosmos SDK, Tendermint) |
| Developer | Terraform Labs Pte. Ltd. (Singapore) |
| Founders | Do Kwon, Daniel Shin |
| Founded | 2018 |
| Mainnet (Columbus) | 2019-04-24 |
| Columbus-5 upgrade | 2021-09-30 |
| Stablecoins | TerraUSD (UST, now USTC), TerraKRW (KRT) and others |
| Collapse | May 2022 |
| Successor chain | Terra (`phoenix-1`), launched 2022-05-28 |
| Tickers | LUNC and USTC (original chain); LUNA (new chain) |
| Live data | [CoinGecko: LUNA](https://www.coingecko.com/en/coins/terra-luna-2), [CoinGecko: LUNC](https://www.coingecko.com/en/coins/terra-luna) |

## History

### Founding and Chai

Daniel Shin, who founded the South Korean e-commerce company Ticket
Monster (TMON) in 2010, co-founded Terraform Labs with Do Kwon in
2018.[^dlnews-shin] In August 2018 the project announced US$32 million in
funding from investors including Binance Labs and Polychain Capital,
presenting Terra as a payments currency for Asian e-commerce
partners.[^fortune-2018]

According to the SEC, Kwon and Shin launched Chai, a Korean mobile
payment service, in or around June 2019. Chai and Terraform shared
offices and staff until early 2020, though Kwon stayed on Chai's board
until about May 2022.[^sec-complaint] Chai integrated Terra's won-pegged
stablecoin in 2019 and says it had no relationship with Terraform Labs
after early 2020. According to DL News, Shin left Terra in late
2019.[^dlnews-shin]
The SEC alleged that Terraform and Kwon falsely claimed Chai payments
were settled on the Terra blockchain, when Chai transactions were
instead copied onto the chain to make them appear to run
there.[^sec-complaint]

### Launch and growth

Kwon and others published the white paper "Terra Money: Stability and
Adoption" in April 2019, and the blockchain launched on or about 24
April 2019 with one billion LUNA tokens.[^sec-complaint] Besides UST,
Terra issued stablecoins tracking other currencies, such as TerraKRW
(KRT).[^classic-glossary][^nber]

Terraform launched the Anchor Protocol in March 2021 and advertised
returns of 19–20% on UST deposits.[^sec-complaint] Liu, Makarov and
Schoar found that Anchor was not self-sustaining: its yield reserve was
topped up by Terraform Labs (US$71 million in July 2021) and by the Luna
Foundation Guard (US$510 million in February 2022). Of about 18.5
billion UST outstanding before the crash, about 12 billion sat in
Anchor.[^nber]

On 23 May 2021 UST fell to nearly US$0.90 before recovering, and
Terraform said the algorithm had restored the peg.[^sec-complaint] The
SEC later found that Tai Mo Shan, a subsidiary of Jump Trading, had
bought more than US$20 million of UST under an agreement in which
Terraform vested Tai Mo Shan's existing option to buy LUNA at a
discount, and that this trading negligently misled the market about the
mechanism. Tai Mo Shan settled in December 2024 for
about US$123 million without admitting or denying the
findings.[^tms-order][^tms-block] Kwon later admitted in his US plea that
he made false statements about why the peg recovered.[^reuters-sentence]

### Columbus-5

The Columbus-5 upgrade took effect on 30 September 2021. It moved Terra
to Cosmos SDK v0.43 and added IBC support. From then on, all
seigniorage from minting stablecoins was burned, instead of most going
to a community pool.[^c5-guide][^nber]

### Mirror Protocol subpoena

Terraform launched Mirror Protocol in 2020. It let users trade "mAssets"
that tracked the prices of US stocks.[^sec-subpoena] On 20 September
2021 SEC staff served Kwon with a subpoena at Messari's Mainnet
conference in New York, and in October Terraform and Kwon sued the SEC,
arguing the subpoenas were improperly issued and
served.[^decrypt-mirror] The SEC asked a federal court in Manhattan to
enforce them on 12 November 2021.[^sec-subpoena] On 8 June 2022 the
Second Circuit upheld the subpoenas.[^block-mirror]

### Luna Foundation Guard

In January 2022 Kwon announced the Luna Foundation Guard (LFG), a
non-profit meant to build reserves backing the UST peg.[^nber] The SEC
said LFG had no employees, was controlled by Kwon, and was funded with a
gift of 50 million LUNA from Terraform.[^sec-complaint] LFG raised US$1
billion by selling LUNA, with Jump Trading and Three Arrows Capital as
lead investors, and held its reserves mostly in bitcoin.[^nber] By 7 May
2022 it held 80,394 BTC, which Fortune reported made it the
second-largest known bitcoin holder after MicroStrategy.[^fortune-lfg]

## Stablecoin mechanism

Terra's stablecoins had no cash backing. The protocol's market module
let users swap US$1 worth of LUNA for 1 UST, and 1 UST for US$1 worth of
LUNA, using oracle prices. If UST traded above US$1, arbitrageurs could
burn LUNA to mint UST and sell it; below US$1, they could buy UST cheaply
and burn it for US$1 of new LUNA. Either trade pushed the price towards
the peg.[^classic-protocol][^nber] LUNA holders also staked it with the
top 130 validators, who produced blocks under Tendermint
consensus.[^classic-protocol]

Liu, Makarov and Schoar compare UST to convertible debt of unlimited
maturity backed by LUNA. Redeeming UST inflates LUNA's supply. If
holders expect that dilution to push LUNA down, they have a reason to
sell first, which can produce a "death spiral" in which both tokens fall
together.[^nber]

## Collapse

### The run

Liu, Makarov and Schoar date the start of the run to 7 May 2022. That
day Terraform Labs removed 150 million UST from the UST-3Crv pool on
Curve, a planned move to a new pool. Soon after, a large wallet withdrew
85 million UST from Anchor and sold it on Curve in one trade, other large
sales followed, and UST's discount on Curve widened to 2.5%. The authors
argue that the pool change was not harmful in itself but could have
served as a coordinating event when confidence was already weak.[^nber] The SEC
described the trigger as large UST sales by one or more sophisticated
trading firms.[^sec-complaint]

Terraform and LFG tried to defend the peg. According to a post-collapse
audit cited by Liu, Makarov and Schoar, they spent about US$2.5 billion,
including 80,071 BTC, buying UST and LUNA. Late on 9 May UST fell to
about US$0.75, and by the end of 13 May less than 2 billion UST remained
in Anchor.[^nber] On 16 May LFG said it had 313 BTC left.[^fortune-lfg]
As UST was redeemed, LUNA's supply rose above 25 billion
tokens.[^block-halt] By 12 May LUNA had lost more than 99% of its value
and UST traded around US$0.37.[^tc-halt]

### Chain halts

On 12 May 2022 validators halted the chain at block 7,603,700. Terraform
Labs said this was to prevent governance attacks after severe LUNA
inflation. Block production resumed later that day.[^tc-halt][^block-halt] Late on
12 May US time (13 May UTC) Terra halted again, at block 7,607,789, so
validators could plan to rebuild the network.[^block-halt]

### Terra 2.0 and Terra Classic

On 25 May 2022 holders passed governance proposal 1623, creating a new
chain. Its mainnet, `phoenix-1`, launched at 06:00 UTC on 28 May
2022[^phoenix-genesis][^block-phoenix] without an algorithmic stablecoin, and new LUNA was airdropped to
holders of the old chain's tokens based on snapshots taken before and
after the depeg.[^terra-protocol][^block-phoenix] (Terra's documentation
gives 27 May.)[^terra-protocol] The original chain
was renamed Terra Classic, with its tokens trading as LUNC and USTC,
while the new chain took the LUNA name.[^block-phoenix][^defiant-lunc][^cg-lunc][^cg-ustc]

### Contagion

Liu, Makarov and Schoar say the crash set off failures at other firms,
including Celsius and Three Arrows Capital, and contributed to the later
fall of [FTX](ftx.md).[^nber] Celsius had rushed to withdraw its funds
from Anchor during the collapse. It paused withdrawals in mid-June 2022
and filed for Chapter 11 on 13 July 2022.[^fortune-celsius]

Three Arrows Capital had bet on LUNA, and its co-founder Su Zhu later
said the firm failed to see that LUNA could fall to almost zero within
days.[^block-3ac] On 27 June 2022 the broker Voyager Digital issued a
default notice to Three Arrows over a loan of 15,250 BTC and 350 million
USDC.[^block-voyager] Voyager filed for Chapter 11 in early July 2022,
and Three Arrows entered liquidation in the British Virgin
Islands.[^fortune-celsius]

### Academic analyses

Liu, Makarov and Schoar (NBER working paper, 2023; later published in
the *Journal of Financial Economics*) argue that the run was probably
not caused by concentrated manipulation by a third party but by growing
doubts about whether the system could last. Wealthier and more
sophisticated investors ran first and lost less; poorer and less
sophisticated investors ran later and lost more. Blockchain transparency
let investors watch each other, which sped up the run.[^nber]

Briola, Vidal-Tomás, Wang and Aste traced the trigger events in hourly
and transaction data, argued that Terra's heavy reliance on Anchor made
it fragile, and found no evidence of herding across 61 large
cryptocurrencies during the crash.[^briola]

## Legal proceedings

### South Korea

Prosecutors in Seoul obtained an arrest warrant for Kwon in September
2022,[^koreatimes-2025] and South Korea asked Interpol to issue a red
notice for him that month.[^ap-montenegro] On 25 April 2023 prosecutors
indicted Shin and nine others on charges including violations of the
Capital Markets Act, alleging that they made 463 billion won in profit
and that Terra was a "fictitious" project.[^block-shin] Prosecutors also
alleged that Shin sold pre-issued LUNA without proper disclosure and
that Chai misused customer data.[^dlnews-shin] The defendants deny the
charges. Shin's lawyers say he split from Kwon in 2020 and blame Kwon's
later management for the collapse.[^block-shin][^hankook] In December
2025 the first-instance trial had been running for nearly three years
without a verdict.[^hankook]

Korean prosecutors estimate that about 200,000 local victims lost
about 300 billion won. They want to try Kwon in South Korea, and one
said a conviction there could bring a sentence of more than 30
years.[^koreatimes-2025][^decrypt-korea]

### Arrest in Montenegro and extradition

On 23 March 2023 Kwon and Han Chang-joon, Terraform's former chief
financial officer, were arrested at Podgorica airport in Montenegro
while trying to fly to Dubai on forged Costa Rican
passports.[^block-arrest][^semafor][^fortune-montenegro] The same day,
US prosecutors in Manhattan charged Kwon with securities fraud, wire
fraud, commodities fraud and conspiracy.[^semafor] On 19 June 2023 a
Podgorica court sentenced both men to four months in prison for the
forgery.[^fortune-montenegro][^block-forgery]

The United States and South Korea both sought Kwon's extradition.
Montenegrin courts ruled for the US in February 2024, switched to South
Korea in March 2024, and then went through further appeals. In late
December 2024 Justice Minister Bojan Božović ordered extradition to the
US, and Kwon was handed to FBI agents on 31 December 2024.[^block-extradition]

### SEC civil case

The SEC sued Terraform and Kwon on 16 February 2023, alleging that they
sold crypto asset securities in unregistered transactions, marketed UST
as a "yield-bearing" stablecoin paying up to 20% through Anchor, and
misled investors about a Korean payment app's use of the
chain.[^sec-2023] On 28 December 2023 the court found them liable
for unregistered offers and sales, and on 5 April 2024 a jury found them
liable for fraud.[^sec-2024]

In June 2024 they settled for about US$4.5 billion, and Judge Jed Rakoff
approved the settlement.[^coindesk-settlement] Terraform agreed to
pay about US$3.59 billion in disgorgement, US$467 million in interest and
a US$420 million penalty, and to wind down. Kwon agreed to pay US$110
million in disgorgement plus interest, jointly with Terraform, and a
US$80 million penalty.[^sec-2024]

### Terraform Labs bankruptcy

Terraform Labs filed for Chapter 11 in Delaware on 21 January
2024.[^block-bankruptcy] On 19 September 2024 the court approved its
wind-down. Terraform estimated it would pay stakeholders between
US$184.5 million and US$442.2 million, and the SEC agreed to recover only
after harmed investors and other unsecured creditors were paid in
full.[^block-winddown]

In December 2025 the estate's plan administrator, Todd Snyder, sued Jump
Trading, its co-founder William DiSomma and former president Kanav Kariya
for US$4 billion, alleging that Jump profited from and accelerated the
collapse. Jump called the suit a "desperate attempt" to shift blame from
Terraform and Kwon.[^block-jump][^bl-jump] In February 2026 Snyder sued
Jane Street and three individuals, alleging insider trading linked to
Terraform's Curve pool withdrawal on 7 May 2022.[^block-jane-suit][^bl-jane] In
April 2026 Jane Street moved to dismiss, calling the case an attempt to
make it "foot the bill" for Terraform's own fraud.[^block-jane][^bl-jane]
No ruling on either suit had been reported as of April 2026.

### US criminal case

In January 2025 a superseding indictment charged Kwon with nine counts,
including securities, wire and commodities fraud and money laundering
conspiracy.[^reuters-sentence] On 12 August 2025 he pleaded guilty to
one count of conspiracy to commit commodities fraud, securities fraud and
wire fraud, and one count of wire fraud. He agreed to forfeit more than
US$19 million, and prosecutors agreed not to seek more than 12 years. His
lawyer said Kwon "takes responsibility for misleading the Terra
community".[^ap-plea]

On 11 December 2025 Judge Paul Engelmayer sentenced Kwon to 15 years,
more than prosecutors had sought. The defence had asked for five years,
arguing that third-party firms were partly to blame for the
crash.[^block-sentence][^reuters-sentence] Under the plea agreement, US
prosecutors will not oppose a transfer to South Korea once Kwon has
served half his sentence.[^reuters-sentence] Korean prosecutors said in
December 2025 that they intend to try him there if he is
returned.[^koreatimes-2025]

## Timeline

| Date | Event |
|---|---|
| 2018 | Terraform Labs founded by Do Kwon and Daniel Shin |
| 2019-04-24 | Terra mainnet launches |
| 2021-03 | Anchor Protocol launched |
| 2021-05-23 | UST falls to about US$0.90; Tai Mo Shan buys UST |
| 2021-09-20 | SEC serves Kwon with Mirror subpoena |
| 2021-09-30 | Columbus-5 upgrade |
| 2022-01 | Luna Foundation Guard announced |
| 2022-05-07 | Large UST withdrawals from Anchor and sales on Curve |
| 2022-05-12 | Chain halted; halted again early on 13 May (UTC) |
| 2022-05-28 | New Terra chain launches; old chain becomes Terra Classic |
| 2022-07-13 | Celsius files for Chapter 11 |
| 2022-09 | South Korean arrest warrant for Kwon |
| 2023-02-16 | SEC sues Terraform Labs and Kwon |
| 2023-03-23 | Kwon arrested in Montenegro; US charges filed |
| 2023-04-25 | Shin and nine others indicted in South Korea |
| 2024-01-21 | Terraform Labs files for Chapter 11 |
| 2024-04-05 | Jury finds Terraform and Kwon liable for fraud |
| 2024-06-13 | SEC announces US$4.5 billion settlement |
| 2024-12-31 | Kwon extradited to the United States |
| 2025-08-12 | Kwon pleads guilty |
| 2025-12-11 | Kwon sentenced to 15 years |
| 2025-12 | Plan administrator sues Jump Trading |
| 2026-02 | Estate sues Jane Street |

## See also

- [Tether](tether.md) and [USDC](usdc.md), fiat-backed stablecoins
- [FTX](ftx.md), whose fall followed the 2022 contagion
- [Bitcoin](bitcoin.md), the main reserve asset of the Luna Foundation Guard

## References

[^classic-protocol]: Terra Classic documentation. *Terra protocol*. <https://classic-docs.terra.money/docs/learn/protocol.html>
[^classic-glossary]: Terra Classic documentation. *Glossary*. <https://classic-docs.terra.money/docs/learn/glossary.html>
[^c5-guide]: Terra Classic documentation. *Columbus-5 migration guide*. <https://classic-docs.terra.money/docs/develop/reference/migration-guide.html>
[^terra-protocol]: Terra documentation. *Protocol*. <https://docs.terra.money/learn/protocol>
[^sec-2023]: U.S. Securities and Exchange Commission (2023). *SEC charges Terraform and CEO Do Kwon with defrauding investors in crypto schemes*. <https://www.sec.gov/newsroom/press-releases/2023-32>
[^sec-complaint]: U.S. Securities and Exchange Commission (2023). *SEC v. Terraform Labs Pte Ltd. and Do Hyeong Kwon*, amended complaint, No. 1:23-cv-1346 (S.D.N.Y.). <https://www.sec.gov/files/terraform-labs-pte-ltd-amended-complaint.pdf>
[^sec-2024]: U.S. Securities and Exchange Commission (2024). *Terraform and Kwon to pay $4.5 billion following fraud verdict*. <https://www.sec.gov/news/press-release/2024-73>
[^coindesk-settlement]: CoinDesk (2024). *U.S. judge signs off on $4.5B Terraform-Do Kwon settlement with SEC*. <https://www.coindesk.com/policy/2024/06/13/us-judge-signs-off-on-45b-terraform-do-kwon-settlement-with-sec>
[^sec-subpoena]: U.S. Securities and Exchange Commission (2021). *SEC files subpoena enforcement action against Terraform Labs and its CEO*. Litigation Release No. 25262. <https://www.sec.gov/litigation/litreleases/lr-25262>
[^tms-order]: U.S. Securities and Exchange Commission (2024). *In the Matter of Tai Mo Shan Limited*, Release No. 33-11349. <https://www.sec.gov/files/litigation/admin/2024/33-11349.pdf>
[^tms-block]: The Block (2024). *SEC fines Jump Trading subsidiary $123 million for propping up TerraUSD stablecoin during depeg*. <https://theblock.co/news/regulation/2024-12-21-sec-fines-jump-trading-subsidiary-123-million-for-propping-up-terrausd-stablecoin-during-depeg-332096>
[^fortune-2018]: Fortune (2018). *Cryptocurrency exchanges back $32 million stable coin project*. <https://fortune.com/crypto/2018/08/29/cryptocurrency-exchanges-back-32-million-stable-coin-project>
[^dlnews-shin]: DL News (2023). *Terra's Daniel Shin braces for trial in South Korea as co-founder Do Kwon jailed in Balkans*. <https://www.dlnews.com/articles/people-culture/terra-cofounder-daniel-shin-goes-to-trial-as-do-kwon-jailed/>
[^nber]: Liu, J., Makarov, I., and Schoar, A. (2023). *Anatomy of a run: the Terra Luna crash*. NBER Working Paper 31160. <https://www.nber.org/papers/w31160>
[^briola]: Briola, A., Vidal-Tomás, D., Wang, Y., and Aste, T. (2022). *Anatomy of a stablecoin's failure: the Terra-Luna case*. arXiv:2207.13914. <https://arxiv.org/abs/2207.13914>
[^fortune-lfg]: Fortune (2022). *Luna Foundation Guard has now dumped $2.4 billion from its bitcoin reserves*. <https://fortune.com/2022/05/16/luna-foundation-guard-dumps-bitcoin-reserves-terra-usd-peg/>
[^tc-halt]: TechCrunch (2022). *Terra resumes blockchain production after halting to prevent hacks amid UST crash*. <https://techcrunch.com/2022/05/12/terra-halts-its-blockchain-to-prevent-hacks-ust/>
[^block-halt]: The Block (2022). *Terra says it has halted blockchain for second time in 24 hours*. <https://www.theblock.co/linked/146722/terra-says-it-has-halted-blockchain-for-second-time-in-24-hours>
[^phoenix-genesis]: Terra (2022). *phoenix-1 genesis file*. <https://phoenix-genesis.s3.us-west-1.amazonaws.com/genesis.json>
[^block-phoenix]: The Block (2022). *Terra gets second life as new blockchain goes live with LUNA 2.0 airdrop*. <https://www.theblock.co/post/149127/terra-gets-second-life-as-new-blockchain-goes-live-with-luna-2-0-airdrop>
[^defiant-lunc]: The Defiant. *What is LUNC?*. <https://thedefiant.io/what-is-lunc>
[^cg-lunc]: CoinGecko. *Terra Luna Classic (LUNC)*. <https://www.coingecko.com/en/coins/terra-luna>
[^cg-ustc]: CoinGecko. *TerraClassicUSD (USTC)*. <https://www.coingecko.com/en/coins/terrausd>
[^decrypt-mirror]: Decrypt (2021). *Terra's Do Kwon was served by SEC at crypto conference*. <https://decrypt.co/81356/terra-do-kwon-served-sec-subpoena-crypto-conference-sources>
[^block-mirror]: The Block (2022). *Terraform Labs ordered to cooperate with SEC probe of Mirror Protocol*. <https://www.theblock.co/post/151069/terraform-labs-ordered-to-cooperate-with-sec-probe-of-mirror-protocol>
[^fortune-celsius]: Fortune (2022). *Celsius files for Chapter 11 bankruptcy*. <https://fortune.com/2022/07/13/celsius-files-bankruptcy-chapter-11-withdrawals>
[^block-3ac]: The Block (2022). *Three Arrows founders tell Bloomberg 'the whole situation is regrettable'*. <https://www.theblock.co/post/159110/three-arrows-founders-tell-bloomberg-the-whole-situation-is-regrettable>
[^block-voyager]: The Block (2022). *Voyager Digital issues default notice against Three Arrows Capital*. <https://www.theblock.co/post/154316/voyager-digital-issues-default-notice-against-three-arrows-capital>
[^ap-montenegro]: Associated Press (2023). *Montenegro: South Korea, US seek extradition of Do Kwon*. Via WSLS. <https://www.wsls.com/business/2023/03/29/montenegro-south-korea-us-seek-extradition-of-do-kwon>
[^block-arrest]: The Block (2023). *Terraform Labs CEO Do Kwon believed to be arrested in Montenegro*. <https://www.theblock.co/post/222286/do-kwon-terra-luna-arrested-montenegro>
[^semafor]: Semafor (2023). *Do Kwon charged after arrest in Montenegro*. <https://semafor.com/article/03/24/2023/do-kwon-charged-arrest-montenegro-fugitive-crypto>
[^fortune-montenegro]: Fortune (2023). *Terra's Do Kwon sentenced to 4 months in a Balkan prison for document forgery*. <https://fortune.com/crypto/2023/06/19/terras-do-kwon-sentenced-to-4-months-in-a-balkan-prison-for-document-forgery>
[^block-forgery]: The Block (2023). *Do Kwon found guilty in Montenegro fake passport case*. <https://www.theblock.co/post/235448/do-kwon-found-guilty-in-montenegro-fake-passport-case>
[^block-extradition]: The Block (2024). *Montenegro extradites Terraform Labs co-founder Do Kwon to the US with help from Interpol*. <https://www.theblock.co/post/332727/montenegro-extradites-terraform-labs-co-founder-do-kwon-to-the-us-with-help-from-interpol>
[^ap-plea]: Associated Press (2025). *Crypto mogul Do Kwon, known as 'the cryptocurrency king,' pleads guilty to fraud charges*. Via KSAT. <https://www.ksat.com/business/2025/08/12/crypto-mogul-do-kwon-known-as-the-cryptocurrency-king-pleads-guilty-to-fraud-charges/>
[^reuters-sentence]: Reuters (2025). *TerraUSD creator Do Kwon sentenced to 15 years over $40 billion crypto collapse*. Via Yahoo Finance. <https://finance.yahoo.com/news/terrausd-creator-kwon-sentenced-over-111455036.html>
[^block-sentence]: The Block (2025). *Terraform Labs founder Do Kwon sentenced to 15 years over $40 billion Terra-Luna collapse*. <https://www.theblock.co/post/382204/terraform-labs-founder-do-kwon-sentenced-to-15-years-over-40-billion-terra-luna-collapse-inner-city-press>
[^koreatimes-2025]: The Korea Times (2025). *Crypto mogul Do Kwon may face separate trial in Korea despite 15-year US sentence*. <https://www.koreatimes.co.kr/southkorea/law-crime/20251215/crypto-mogul-do-kwon-may-face-separate-trial-in-korea-despite-15-year-us-sentence>
[^decrypt-korea]: Decrypt (2025). *Terra founder Do Kwon may face South Korean trial despite 15-year US prison sentence*. <https://decrypt.co/352347/terra-founder-do-kwon-face-south-korean-trial-15-year-us-prison-sentence>
[^block-shin]: The Block (2023). *Terra co-founder Shin and nine others formally charged by South Korea*. <https://www.theblock.co/post/228098/daniel-shin-terra-co-founder-charged>
[^hankook]: Hankook Ilbo (2025). *'테라·루나' 권도형 미국서 15년형…'공범 지목' 10명은 한국에서 재판 중*. <https://www.hankookilbo.com/news/article/A2025121215450001105>
[^block-bankruptcy]: The Block (2024). *Terraform Labs files for Chapter 11 bankruptcy in Delaware*. <https://www.theblock.co/post/273683/terraform-labs-files-chapter-11-bankruptcy-in-delaware>
[^block-winddown]: The Block (2024). *Terraform Labs gets sign off from US bankruptcy judge to begin winding down: Reuters*. <https://www.theblock.co/post/317414/terraform-labs-gets-sign-off-from-us-bankruptcy-judge-to-begin-winding-down-reuters>
[^block-jump]: The Block (2025). *Terraform Labs liquidator sues Jump Trading for $4 billion in damages*. <https://www.theblock.co/post/383263/terraform-labs-sues-jump-trading>
[^bl-jump]: Bloomberg Law (2025). *Jump Trading faces $4 billion Terraform administrator suit*. <https://news.bloomberglaw.com/bankruptcy-law/terraform-administrator-files-4-billion-lawsuit-against-jump>
[^block-jane-suit]: The Block (2026). *Terraform Labs sues Jane Street for alleged insider trading prior to Terra-Luna collapse: WSJ*. <https://www.theblock.co/news/regulation/2026-02-23-terraform-labs-sues-jane-street-390915>
[^block-jane]: The Block (2026). *Jane Street asks court to dismiss Terraform Labs' insider trading lawsuit*. <https://www.theblock.co/post/398713/jane-street-asks-court-dismiss-terraform-labs-insider-trading-lawsuit>
[^bl-jane]: Bloomberg Law (2026). *Jane Street seeks dismissal of Terraform insider-trading suit*. <https://news.bloomberglaw.com/bankruptcy-law/jane-street-seeks-dismissal-of-terraform-insider-trading-suit>
