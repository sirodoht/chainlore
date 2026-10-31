---
title: Stablecoin
ticker: —
category: Stablecoin
written_by: Opus 5.5 High
status: ai-fact-checked
checked: 2026-10-31
checked_by: GPT-6-Astra high
updated: 2026-10-31
---

# Stablecoin

A **stablecoin** is a crypto asset designed to hold a fixed value against
a reference asset, usually one US dollar. Most large stablecoins, such as
[Tether](tether.md)'s USDT and [USDC](usdc.md), are issued by companies
that hold reserves of cash and short-term government debt. Others are
minted against crypto collateral, hedged with derivatives, or held to
their target by incentives alone, as in the original design of TerraUSD, which collapsed
in May 2022.[^fed-stable][^nber-terra] The Bank for International
Settlements (BIS) estimated in 2026 that about 98% of stablecoin value
was denominated in dollars.[^bis-170] The United States, the European
Union, and other jurisdictions have adopted issuer-specific frameworks,
while the BIS questions whether stablecoins can underpin a monetary
system.[^genius][^mica-149][^bis-aer]

| | |
|---|---|
| Type | Crypto asset designed to hold a stable value |
| Main designs | Reserve-backed, crypto-collateralised, synthetic, algorithmic |
| Early examples | BitUSD, Tether, NuBits (all 2014) |
| Main reference currency | US dollar |
| US law | GENIUS Act (signed 2025-07-18) |
| EU law | Markets in Crypto-Assets Regulation (stablecoin titles apply from 2024-06-30) |
| Live data | [DefiLlama](https://defillama.com/stablecoins), [Tether transparency](https://tether.to/en/transparency/), [Circle transparency](https://www.circle.com/transparency) |

## Definition

There is no single definition. The GENIUS Act defines a "payment
stablecoin" as a digital asset that is, or is designed to be, used as a
means of payment or settlement, whose issuer is obligated to redeem it
for a fixed amount of monetary value, and which the issuer represents
will hold a stable value. The definition excludes national currency,
deposits, and securities.[^genius] The EU's Markets in Crypto-Assets
Regulation (MiCA) distinguishes two stable-value categories: an e-money token references
one official currency. An asset-referenced token is not an e-money token
and references another value or right, or a combination of them,
including one or more official currencies.[^mica-3]

The BIS argues that stablecoins behave like financial assets rather than
money. Its 2025 annual report says they typically fail the test of
singleness, because they do not always trade at par with one another,
and also fail the test of elasticity. It concludes that they "perform
poorly when assessed against the three tests for serving as the mainstay
of the monetary system".[^bis-aer] Gorton and Zhang compare them to the
privately issued banknotes of nineteenth-century America.[^gorton]

## History

### Early designs

The Block dates BitUSD, a token collateralised by BitShares, to July
2014 and describes it as the earliest mainstream stablecoin. It lost its
peg in November 2018 and remained off its peg when The Block reported in
February 2019.[^block-bitusd] Realcoin was
announced that same month, July 2014, and was renamed Tether in November
2014.[^realcoin][^rebrand] NuBits began in September 2014 and held its
peg for about twenty months before falling below 50 cents in
2016. It subsequently recovered its peg, according to a 2017 Cato
Institute account.[^nubits][^cato-nubits]

MakerDAO launched Dai on Ethereum on 18 December 2017, backed solely by
ether.[^coindesk-dai] Multi-Collateral Dai went live on 18 November
2019, starting with ether and Basic Attention Token as collateral. It
took the Dai name, the older token was renamed Sai, and the launch added
the Dai Savings Rate.[^block-mcd]

Basis raised US$133 million for an algorithmic stablecoin and shut down
in December 2018, returning unspent money. Its chief executive said
lawyers had concluded its bond and share tokens could not avoid being
securities.[^techcrunch-basis]

### Libra and the regulatory response

Facebook announced Libra on 18 June 2019, with a planned association of
28 founding members, among them Visa, Mastercard, PayPal, and
Uber.[^coindesk-libra] The project, later named Diem, confirmed its
shutdown on 31 January 2022, selling its technology to Silvergate. Its
chief executive, Stuart Levey, said talks with federal regulators had
made clear that it could not launch.[^coindesk-diem]

### Terra and the 2022 collapses

Algorithmic designs failed repeatedly in this period. Iron Finance's
IRON broke its peg on 16 June 2021 in what Federal Reserve staff
analysed as a run.[^fed-iron] [Terra](terra.md)'s UST lost its peg in May
2022; Liu, Makarov, and Schoar describe the unwinding as a run in which
the blockchain made other investors’ actions visible and accelerated withdrawals.[^nber-terra] USDN and
HUSD also lost their pegs in 2022.[^ct-usdn][^block-husd]

### Regulation and institutional issuers

In March 2023 the failure of Silicon Valley Bank, which held about 8% of
USDC's reserves, pushed USDC to about 86 cents until US authorities
protected depositors.[^fed-svb] US legislation followed in July 2025
with the GENIUS Act.[^genius] Banks and payment firms have also entered
the market: PayPal in 2023, SoFi Bank in December 2025, and Open USD, whose
partners include Coinbase, Mastercard, and Visa, on 30 September
2026.[^paypal-launch][^block-sofi][^unchained-ousd][^coindesk-openusd]

Federal Reserve staff put aggregate stablecoin market capitalisation at
US$317 billion on 6 April 2026 and said growth had flattened in late
2025 and early 2026.[^fed-2025] Current totals are on
[DefiLlama](https://defillama.com/stablecoins), which tracked more than
400 pegged assets in October 2026.[^llama][^llama-detail]

## Types

Federal Reserve staff sort stablecoins by how they are stabilised:
off-chain collateralised, on-chain collateralised, and uncollateralised
or algorithmic. They conclude that a run driven by sentiment alone
disappears only when the collateral matches the currency of the
peg.[^fed-stable]

### Reserve-backed

The issuer holds cash, bank deposits, government debt, or money market
funds, and redeems tokens for fiat with approved customers. Holders rely
on the issuer's solvency, its banks, and the accuracy of its
disclosures. Federal Reserve staff say arbitrage for these coins breaks
down once the market loses faith in the peg.[^fed-stable]

### Crypto-collateralised

Users lock crypto in smart contracts and mint stablecoins against it,
usually with more collateral than debt. Positions that fall below a
required ratio are liquidated. Federal Reserve staff say these designs
"might experience more frequent and pronounced runs".[^fed-stable]
Liquity's LUSD uses redemption for ether at face value, less a variable
redemption fee, to help support its peg.[^liquity-redemption]

### Synthetic

Ethena's USDe is described by its issuer as "a synthetic dollar, backed
with crypto assets and corresponding short futures positions", and it
distinguishes this from fiat-backed stablecoins.[^ethena-overview] Its
documentation attributes USDe's peg stability to delta-neutral hedges of
the underlying assets.[^ethena-docs]

### Algorithmic

Uncollateralised designs hold few or no reserves and rely on supply
changes and incentives. Federal Reserve staff write that "such incentives
generate a run as a self-reinforcing prophecy".[^fed-stable] Clements
argues that algorithmic stablecoins are "inherently
fragile".[^clements] Beanstalk says it "uses credit instead of
collateral".[^bean-docs]

### Stablecoin-backed and wrapped

Some tokens represent claims on other stablecoins. Their documentation
describes USDai as collateralised by PYUSD, Polymarket's pUSD and Avant's
avUSD by USDC, and Saturn's USDat by a PYUSD wrapper.[^usdai-docs][^polymarket-docs][^avant-docs][^saturn-docs]

## How pegs are maintained

Issuers mint and burn directly in a primary market, usually with a
limited set of customers, while everyone else trades in secondary
markets. Federal Reserve staff write that "secondary markets actually
price the assets and help enable a stablecoin to maintain its dollar
peg". Their 2024 account contrasts Dai’s model, in which Ethereum users
could mint coins by depositing collateral.[^fed-primary]

Lyons and Viswanath-Natraj treat a peg like a fixed exchange rate. They
find that arbitrage keeps Tether near its peg and that issuance plays a
limited role, with stabilisation mainly coming from the demand
side.[^lyons] Ma, Zeng, and Zhang find that arbitrage is concentrated,
reporting that, in their historical sample, an average of six agents per
month redeemed Tether for cash. They argue that efficient arbitrage helps
price stability but raises run risk.[^ma] Federal Reserve staff wrote in
April 2026 that stablecoins with safer, more liquid reserves have lower
run risk and have seen relatively stronger adoption.[^fed-2025]

## Uses and effects

The International Monetary Fund attributes most recent growth to crypto
trading, and says future demand could come from payments and
tokenisation.[^imf] Visa said in April 2026 that its stablecoin
settlement pilot had reached an annualised US$7 billion.[^coindesk-visa]

Stablecoin reserves have become large enough to affect government debt
markets. A BIS working paper finds that inflows lower three-month
Treasury bill yields, with larger effects during market
stress.[^bis-1270] Another finds that stablecoin flows appear largely
unaffected by capital flow restrictions.[^bis-1370]

## Risks and criticism

- Runs. Hyun Song Shin of the BIS warns of fire sales of backing assets
  and says stablecoins lack the settlement function of central bank
  money.[^reuters-bis]
- Dollarisation. BIS staff write that "digital dollarisation poses acute
  risks to monetary sovereignty" in emerging markets, and the IMF says
  stablecoins may contribute to currency substitution where confidence
  in domestic money is low.[^bis-170][^imf]
- Illicit finance. Chainalysis attributed 84%
  of identified illicit crypto transaction volume in 2025 to stablecoins.
  This is the share of identified illicit volume, not the share of
  stablecoin activity that was illicit.[^block-chainalysis] The Financial Action
  Task Force described them in March 2026 as a relatively stable medium
  for moving proceeds.[^fatf] A UN report named USDT in Southeast Asia;
  Tether said it was disappointed and that its tokens can be traced on
  public blockchains.[^block-un]
- Central control. Issuers of reserve-backed coins can freeze tokens, and
  the GENIUS Act requires the ability to block, freeze, and reject
  transactions.[^genius] The dispute over when an issuer should use that
  power is covered in [USDC](usdc.md#incidents-and-controversies).
- Stacked exposure. Federal Reserve staff identify complex intermediation
  chains and vertical integration as vulnerabilities.[^fed-2025]

## Regulation

### United States

The GENIUS Act, signed on 18 July 2025, takes effect on the earlier of 18
months after enactment or 120 days after regulators issue final rules.
It requires reserves of at least one to one in assets such as dollars,
deposits at insured institutions, and Treasuries with 93 days or less to maturity. It
requires monthly disclosure and bars issuers from paying interest or
yield to holders. From three years after enactment, service providers may
not offer or sell payment stablecoins to people in the United States
unless a permitted issuer issued them or an exception applies, including
the route for qualifying foreign issuers.[^genius]

The Office of the Comptroller of the Currency (OCC) issued a final rule
under the Act on 21 October 2026, effective 18 January 2027. The final
rule also identifies that as the Act’s effective date.[^occ-final] WilmerHale
describes it as the first from a federal banking agency. The final rule
dropped a proposed presumption that would have treated some
issuer-funded intermediary rewards as prohibited issuer yield; the
statutory ban on issuers paying yield and the OCC’s anti-evasion
authority remain.[^wilmerhale][^occ-final] A May 2026 text of the CLARITY Act barred yield
equivalent to bank interest but kept rewards tied to activity, and the
bill failed to clear the Senate's 60-vote threshold for beginning debate on 15 September
2026.[^coindesk-yield][^coindesk-clarity] New York set its own rules
earlier, in guidance issued on 8 June 2022.[^nydfs-2022]

### European Union

MiCA's titles on asset-referenced and e-money tokens have applied since
30 June 2024.[^mica-149] Tether announced the end of support for its euro token that year, citing
regulation and falling demand.[^block-eurt] European officials are
divided. Christine Lagarde, president of the European Central Bank, said
on 8 May 2026 that "the case for promoting euro-denominated stablecoins
is far weaker than it appears", a position opposed to that of Bundesbank
president Joachim Nagel, who backed them.[^block-lagarde] Qivalis, a
company backed by 37 European banks, announced on 14 October 2026 that
it had received an e-money authorisation from De Nederlandsche Bank.[^qivalis-dnb]

On 8 October 2026 ESMA said MiCA-authorised service providers should
cease services involving non-compliant stablecoins for EU clients,
including custody and transfers. It allowed tightly supervised,
time-limited activity to wind down existing exposures, with remediation
no later than three months after the opinion.[^esma-october]

On 14 October 2026 the European Banking Authority classified USDC as the
EU's first significant e-money token under MiCA. Its announcement set
12 November for dual supervision by the EBA and France's ACPR, with the
EBA taking responsibility for reserves, liquidity and other specified
prudential matters.[^eba-usdc]

### United Kingdom

The Bank of England published its approach to sterling systemic
stablecoins on 22 June 2026, replacing holding limits with a temporary
issuance guardrail.[^boe] The Financial Conduct Authority published
final rules on 30 June 2026, and KPMG reports they take effect from
October 2027.[^skadden-fca][^kpmg-uk]

The government's October 2026 Budget also proposed legislation to treat
eligible stablecoins more like money for tax purposes. HMRC's proposal
would exempt individuals' and trustees' disposals from Capital Gains Tax
and base certain company transactions on accounting amounts, with
transitional provisions. The planned start dates were 6 April 2027 for
individuals and trustees and 1 April for companies; these were prospective
changes, not the tax rules already in force.[^uk-budget-tax][^hmrc-tax]

### Asia

- Hong Kong. The Stablecoins Ordinance took effect on 1 August
  2025.[^hkma] The Hong Kong Monetary Authority issued its first licences
  on 10 April 2026, to HSBC and Anchorpoint Financial, a venture of
  Standard Chartered, HKT, and Animoca
  Brands.[^charltons][^hsbc-licence] Anchorpoint began rolling out HKDAP in
  August 2026, and Decrypt reported that HSBC's RedCoin went live in
  October.[^block-hkdap][^decrypt-redcoin]
- Singapore. The Monetary Authority of Singapore finalised a framework
  for single-currency stablecoins on 15 August 2023, requiring par
  redemption within five business days.[^mas]
- Japan. Amendments to the Payment Services Act were enacted on 3 June
  2022.[^iflr] JPYC launched under this regime on 27 October
  2025.[^block-jpyc]
- South Korea. A Digital Asset Basic Act was proposed in April 2026. The
  Bank of Korea argued that only banks holding 51% of an issuer should be
  able to issue stablecoins.[^coindesk-korea] As of 31 October 2026 the
  framework remained in progress: The Block reported on 22 October that
  government consultations were nearing completion.[^block-korea]

### International

The Financial Stability Board published recommendations for global
stablecoin arrangements on 17 July 2023.[^fsb-2023] Its review of October
2025 found that their regulation "is lagging".[^fsb-2025] In October
2026 it outlined further work on cross-border vulnerabilities, monitoring,
cooperation, and implementation of those recommendations.[^fsb-2026]

## List of stablecoins

These are selected examples, including tokens tracked by DefiLlama in
October 2026 and smaller ones of historical interest.[^llama] Backing is as the issuer states it, unless noted. A dash
means no launch date was confirmed from a source. Current supply is on
[DefiLlama](https://defillama.com/stablecoins).

### Reserve-backed US dollar tokens

| Token | Ticker | Issuer | Launched | Stated backing and notes |
|---|---|---|---|---|
| Agora Dollar | AUSD | Agora Bermuda Limited | — | Short-term Treasuries, overnight repo, and cash; licensed in Bermuda[^agora] |
| CASH | CASH | Bridge, designed by Phantom | 2025 | Backed 1:1 by dollars; Phantom Cash accounts were available by November[^phantom-cash] |
| CFX MoveUSD | MOVEUSD | CFX Labs | — | Issued by CFX on Solana, Base, and Ethereum[^wormhole-moveusd] |
| First Digital USD | FDUSD | First Digital group | 2023-06 | Cash and equivalents; reserves held by First Digital Trust[^taiwan-fd][^block-binance-busd] |
| Frax USD | frxUSD | Frax Protocol | — | Described as fiat-redeemable and fully collateralised[^chaos-frxusd] |
| Gemini Dollar | GUSD | Gemini | 2018-09 | Cash or equivalents; regulated by New York[^gemini][^forklog-gusd] |
| Global Dollar | USDG | Paxos Digital Singapore | 2024-11-01 | Deposits, short-term government debt; DBS holds reserve cash[^paxos-usdg] |
| M | M | Governance-approved minters on M0 | — | Base token for custom stablecoin extensions[^block-m0] |
| Open USD | OUSD | Bridge, for Open Standard | 2026-09-30 | Reserves at BlackRock, Lead Bank, and BNY[^unchained-ousd] |
| Pax Dollar | USDP | Paxos | 2018-09 | Launched as Paxos Standard; dollar-backed[^coindesk-pax] |
| PayPal USD | PYUSD | Paxos Trust Company | 2023-08-07 | Dollar deposits, short-term Treasuries, equivalents[^paypal-launch] |
| Ripple USD | RLUSD | Ripple's New York trust company | 2024-12-17 | Dollar deposits, Treasuries, cash equivalents[^ripple][^fortune-rlusd] |
| SoFiUSD | SOFID | SoFi Bank, N.A. | 2025-12 | Matched 1:1 with cash, per SoFi[^block-sofi] |
| TrueUSD | TUSD | Techteryx (owner) | — | Reserve dispute; see [Incidents](#incidents)[^coindesk-tusd] |
| [Tether](tether.md) | USDT | Tether group | 2014 | Mostly US Treasuries, with gold and bitcoin[^fy-2025] |
| USA₮ | USAT | Anchorage Digital Bank | 2026-01-27 | Tether-branded US token; liquid reserves[^usat-launch][^usat] |
| [USDC](usdc.md) | USDC | Circle | 2018-09-26 | Cash and a BlackRock-managed reserve fund[^coindesk-usdc][^transparency] |
| USD1 | USD1 | BitGo Bank & Trust, for World Liberty Financial | 2025 | Treasuries, deposits, equivalents; announced 2025-03-25; BitGo was the exclusive issuer as of the OCC's August 2026 decision[^block-usd1][^bitgo][^occ-wlf] |
| USD0 | USD0 | Usual Protocol | 2024-05 | Tokenised Treasury bills and repos[^usual-docs][^usual-roadmap] |
| USDGO | USDGO | Anchorage Digital Bank; distributed by OSL | 2026-02 | Dollars and high-quality liquid assets[^anchorage-usdgo] |
| USDtb | USDtb | Anchorage Digital Bank, with Ethena | 2024-12 | Treasury assets, including BlackRock's BUIDL fund[^block-usdtb][^anchorage-ethena] |

### Crypto-backed, synthetic, and algorithmic US dollar tokens

| Token | Ticker | Issuer | Launched | Design |
|---|---|---|---|---|
| Alchemix USD | alUSD | Alchemix | — | Minted against yield-bearing collateral; fixed-term Transmuter redemption supports the soft peg[^alchemix] |
| apxUSD | apxUSD | Apyx | — | Synthetic; backed mainly by Strategy's STRC preferred stock[^apyx] |
| Astherus USDF | USDF | Astherus, renamed Aster in 2025 | — | Minted 1:1 from USDT; funds deployed in trading strategies, per Aster[^hackernoon-aster][^aster-usdf] |
| Beanstalk | BEAN | Beanstalk DAO | — | No collateral requirement; uses credit[^bean-docs] |
| BOLD | BOLD | Liquity V2 | 2025-05-19 | Backed only by WETH, wstETH, and rETH; live date is the relaunch[^liquity-bold][^liquity-v2] |
| crvUSD | crvUSD | Curve | 2023-05-17 | Liquidation mechanism LLAMMA, plus PegKeepers[^galaxy-crvusd] |
| Dai | DAI | Maker Protocol, now Sky | 2017-12-18 | Multi-collateral vaults; upgradeable 1:1 to USDS[^coindesk-dai][^dss][^block-sky] |
| DOLA | DOLA | Inverse Finance | — | Debt-backed; generated through borrowing on FiRM[^inverse] |
| Ethena USDe | USDe | Ethena Labs | 2024-02 | Delta-hedged crypto collateral[^ethena-docs][^bankless-ethena] |
| Falcon USD | USDf | Falcon Finance | 2025-04-30 | Overcollateralised; market-neutral strategies[^decrypt-falcon][^falcon] |
| GHO | GHO | [Aave](aave.md) | 2023-07-15 | Minted by borrowing against Aave collateral[^gho-block][^gho-docs] |
| Gyro Dollar | GYD | Gyroscope | — | Autonomous mint and redeem pricing with diversified reserves[^gyro] |
| Liquity USD | LUSD | Liquity V1 | 2021-04-05 | Ether only; 110% minimum collateral ratio[^forklog-liquity][^liquity-redemption] |
| Magic Internet Money | MIM | Abracadabra | — | Minted against interest-bearing tokens[^abracadabra] |
| Mustang USD | MUST | Mustang Finance, on SagaEVM | — | Tracker classifies it as crypto-backed; its coverage is marked ended from 2026-02-16[^llama-detail] |
| Sky Dollar | USDS | Sky, formerly MakerDAO | 2024 | Upgraded version of DAI[^block-sky][^sky] |
| Solstice USX | USX | Solstice Labs | 2025-09-30 | Backed 1:1 by stable collateral, per its launch release[^decrypt-usx] |
| USDa | USDa | Avalon Labs | 2024-11 | Collateralised by bitcoin, per its launch release[^decrypt-usda] |
| USDD | USDD | TRON DAO Reserve at launch | 2022-05-05 | Launched as algorithmic; now overcollateralised[^block-usdd][^block-usdd2] |

### Stablecoin-backed US dollar tokens

| Token | Ticker | Issuer | Launched | Backing |
|---|---|---|---|---|
| Avant USD | avUSD | Avant Protocol | — | USDC, 1:1[^avant-docs] |
| Polymarket USD | pUSD | Polymarket | 2026-04 | USDC, 1:1; sole collateral on Polymarket[^polymarket-docs][^ct-polymarket] |
| Saturn Dollar | USDat | Saturn | — | PYUSDx, a wrapper of PYUSD issued by MoonPay Digital Assets[^saturn-docs] |
| USD.AI | USDai | USD.AI | — | PYUSD; loan exposure sits in staked sUSDai[^usdai-docs] |
| United Stables | U | United Stables | 2025-12-18 | Stablecoins including USDT, USDC, and USD1, as minting collateral[^bnb-u] |

### Other currencies

| Token | Ticker | Peg | Issuer | Launched | Notes |
|---|---|---|---|---|---|
| A7A5 | A7A5 | Russian rouble | Old Vector (Kyrgyzstan) | 2025-01 | Under US sanctions; see [Incidents](#incidents)[^ofac-a7a5][^elliptic] |
| AUDD | AUDD | Australian dollar | AUDC Pty Ltd, Novatti affiliate | 2022-11 | Initially launched on Stellar[^audd-launch][^audd-terms] |
| AxCNH | AxCNH | Offshore yuan | AnchorX (Hong Kong) | 2025-09-17 | The HKMA said no such coin was issued in Hong Kong[^standard-axcnh] |
| Bilira | TRYB | Turkish lira | BiLira | — | Reserves in Turkish bank accounts[^bilira] |
| Brazilian Digital Token | BRZ | Brazilian real | Transfero | 2019 | Backed 1:1 with reals, per Transfero[^transfero] |
| EUR CoinVertible | EURCV | Euro | Societe Generale-Forge | 2023-04 | 100% backed by cash, per the issuer[^sgforge][^kitco-eurcv] |
| EURC | EURC | Euro | Circle Internet Financial Europe | 2022-06-30 | Launched as Euro Coin; French e-money institution[^circle-euroc][^circle-eurc] |
| Eurite | EURI | Euro | Banking Circle S.A. | 2024-08-26 | Redeemable at par[^banking-circle] |
| Frankencoin | ZCHF | Swiss franc | Decentralised | 2023-04 | Oracle-free, collateralised; date is public beta[^frankencoin] |
| HKDAP | HKDAP | Hong Kong dollar | Anchorpoint Financial | 2026-08-12 | Phased rollout, first to institutional distributors and professional investors[^block-hkdap] |
| JPY Coin | JPYC | Japanese yen | JPYC Inc. | 2025-10-27 | Deposits and government bonds, per the company[^block-jpyc] |
| JPYSC | JPYSC | Japanese yen | SBI Shinsei Trust Bank | 2026-06-24 | Reserves managed by a trust bank[^block-jpysc] |
| Monerium EUR | EURe | Euro | Monerium hf | — | Supervised by the Central Bank of Iceland[^monerium] |
| RedCoin | RCHKD | Hong Kong dollar | HSBC | 2026-10 | Reported on HSBC's private ledger, inside its PayMe app[^decrypt-redcoin] |
| STASIS Euro | EURS | Euro | STASIS (Malta) | 2018 | Euro-backed, per STASIS[^stasis] |
| XSGD | XSGD | Singapore dollar | StraitsX SGD Issuance Pte Ltd | — | Pegged 1:1 to SGD; issuer holds a Major Payment Institution licence[^straitsx-terms][^mas-straitsx] |

### Commodity-backed tokens

| Token | Ticker | Reference | Issuer | Notes |
|---|---|---|---|---|
| Pax Gold | PAXG | One fine troy ounce of gold | Paxos | Launched 2019-09-05; London Good Delivery gold[^paxos-gold] |
| Tether Gold | XAUT | One fine troy ounce of gold | TG Commodities, S.A. de C.V. | Gold held in Switzerland, per issuer[^tether-gold] |

### Announced

| Project | Reference | Status |
|---|---|---|
| Qivalis | Euro | E-money authorisation on 2026-10-14; issuance planned within months[^qivalis-dnb] |

### Related fund shares and yield products

Some instruments marketed alongside stablecoins are fund shares, debt securities, or yield products.[^buidl][^figure-ylds][^gate]

| Token | Ticker | What it is |
|---|---|---|
| BlackRock USD Institutional Digital Liquidity Fund | BUIDL | Fund shares offered under securities-law exemptions to qualified investors; BlackRock says they may not hold US$1 at all times[^buidl] |
| Figure YLDS | YLDS | A yield-bearing SEC-registered debt security[^figure-ylds] |
| Gate USD | GUSD | Described by Gate as "a principal-protected flexible earn product"[^gate] |
| Multipli rwaUSDi | rwaUSDi | A permissioned credit token for private credit pools, with delayed redemption[^multipli] |

### Failed, retired, and winding down

| Token | Ticker | Date | Outcome |
|---|---|---|---|
| Basis | — | 2018-12 | Shut down and returned unspent capital[^techcrunch-basis] |
| BitUSD | BitUSD | 2018-11 | Lost its peg; global settlement triggered on 2018-11-25[^block-bitusd] |
| Binance USD | BUSD | 2023-02-21 | Paxos stopped minting at the direction of New York's regulator[^paxos-busd] |
| Diem | — | 2022-01-31 | Abandoned before launch[^coindesk-diem] |
| Elixir deUSD | deUSD | 2025-11-06 | Shut down after losses tied to Stream Finance[^block-deusd] |
| Euro Tether | EURT | 2025-11-27 | Redemption deadline after Tether ended support[^block-eurt] |
| Tether CNH | CNHT | 2026-02-20 | New issuance stopped; redemption support scheduled to end 2027-02-20[^tether-cnht] |
| Fei USD | FEI | 2022-08 | Fei Labs proposed winding down Tribe DAO on 2022-08-19[^boardroom-fei] |
| flexUSD | flexUSD | 2022-06 | Its issuer, CoinFLEX, halted withdrawals and later restructured[^block-coinflex][^llama-detail] |
| GMO GYEN | GYEN | 2026-11-11 | Redemption deadline in a wind-down by GMO Trust[^gmo] |
| HUSD | HUSD | 2022-10 | Delisted by Huobi; fell to about US$0.30[^block-husd] |
| Legacy Frax Dollar | FRAX | 2025 | Original FRAX; proposed renaming in FIP-428, see below[^fip-428] |
| Iron | IRON | 2021-06-16 | Run; settled near 75 cents[^fed-iron] |
| Neutrino USD | USDN | 2022 | Repeated depegs, as low as US$0.53[^ct-usdn] |
| NuBits | NBT | 2016 | Fell below 50 cents, then recovered its peg; this row records the historical depeg[^nubits][^cato-nubits] |
| RAI | RAI | 2025-06 | Unpegged managed-float asset; shut down through global settlement[^reflexer-faq][^reflexer-x] |
| Real USD | USDR | 2023-10-11 | Fell about 50% in a rush of redemptions[^block-usdr] |
| Stable Labs USDX | USDX | 2025-11-06 | The Block reported a fall below US$0.60; its contemporaneous report did not establish a cause[^block-usdx] |
| Stream xUSD | xUSD | 2025-11 | Stream disclosed a US$93 million loss; fell to about US$0.26[^decrypt-xusd] |
| Synthetix sUSD | sUSD | 2026-06 | Deprecated under SIP-423[^synthetix-docs] |
| [TerraUSD](terra.md) | UST | 2022-05 | Collapsed with LUNA[^nber-terra] |
| USDH | USDH | 2026 | Phase-out announced on [Hyperliquid](hyperliquid.md)[^block-usdh] |

Binance also issued a separate Binance-Peg BUSD on other chains, and
stopped supporting BUSD in 2023, offering conversion to FDUSD.[^block-binance-busd]
FRAX originally combined collateralised and algorithmic design.[^frax-original] A
2025 proposal called for renaming it Legacy Frax Dollar and giving the FRAX
name to the governance token, FXS. CoinEx announced support for that swap in January
2026.[^fip-428][^coinex-frax]

## Incidents

| Date | Token | What happened |
|---|---|---|
| 2020-03-12 | Dai | Ether's crash under-collateralised Dai. One bidder won about 62,843 ether for almost no Dai in auctions; estimates of the shortfall differ.[^ct-maker][^glassnode] |
| 2021-06-16 | IRON | Run on a token about 75% backed by USDC and 25% by TITAN.[^fed-iron] |
| 2022-04 | BEAN | Attacker used flash loans to take over governance; Cointelegraph reported losses of US$182 million.[^ct-bean] |
| 2022-05 | UST | Collapse of TerraUSD and LUNA.[^nber-terra] |
| 2022-06-13 | USDD | Fell to 91 cents on KuCoin; the reserve added US$650 million of USDC.[^fortune-usdd] |
| 2023-03-10–13 | USDC | Fell to about 86 cents during the weekend after Silicon Valley Bank failed.[^fed-svb] |
| 2024-01-30 | MIM | Fell to US$0.76 after a US$6.5 million exploit.[^unchained-mim] |
| 2024-09-24 | TUSD | The SEC charged TrueCoin and TrustToken with misrepresenting TUSD's backing. They settled without admitting or denying the claims.[^sec-tusd] |
| 2025-01 | USD0++ | Cointelegraph reported that Usual's staked token fell to US$0.89 after a new floor price.[^ct-usd0][^block-usd0] |
| 2025-04-02 | FDUSD | Justin Sun said First Digital Trust could not meet redemptions; it called this false and said FDUSD was solvent. Decrypt reported a low of US$0.95 using CoinGecko data.[^decrypt-fdusd][^block-fdusd] |
| 2025-04 | sUSD | Fell to US$0.66. Synthetix attributed the depeg to changes under SIP-420.[^decrypt-susd][^synthetix-blog] |
| 2025-07 | USDf | CoinMarketCap recorded a low of US$0.9783. Falcon's Andrei Grachev attributed the brief depeg to market sentiment and said the token remained overcollateralised.[^ct-falcon] |
| 2025-08-07 | USDP, PYUSD | New York's regulator fined their issuer, Paxos, US$26.5 million over due diligence on Binance; Paxos said the matters were historical.[^nydfs-paxos][^block-paxos] |
| 2025-08-14 | A7A5 | The US Treasury sanctioned its issuer, Old Vector, and the exchange Grinex.[^ofac-a7a5] Elliptic reports no new minting apart from interest payments since July 2025.[^elliptic] |
| 2025-10-10 | USDe | Fell to about US$0.65 on Binance; Ethena's chief executive said one venue was out of line. Binance said it paid about US$283 million across affected USDe, BNSOL, and WBETH users.[^ct-usde][^block-binance] |
| 2025-10-15 | PYUSD | Paxos minted 300 trillion PYUSD in error and burned the excess tokens.[^block-pyusd][^bloomberg-pyusd] |
| 2025-10-17 | TUSD | An amended DIFC judgment recorded the continuation of injunctions over up to US$456 million in the Techteryx–Aria reserve dispute. It addressed interim protection, not a final finding on the contested claims.[^difc-tusd] |
| 2026-01-21 | MUST | Saga reported that a SagaEVM exploit affected Colt and Mustang and moved nearly US$7 million in assets to Ethereum.[^saga-incident] |
| 2026-03-22 | USR | About 80 million unbacked Resolv USR were minted. CertiK estimated losses at approximately US$26.8 million.[^certik-usr] |

World Liberty Financial, the group behind USD1, has ties to the Trump
family. Senator Elizabeth Warren asked the OCC
to pause its trust charter application until President Trump divested.
The OCC granted preliminary conditional approval on 14 August 2026 and
made the start of business conditional on completing preopening
requirements.[^warren-wlf][^occ-wlf]

## Timeline

| Date | Event |
|---|---|
| 2014-07 | BitUSD debuts; Realcoin announced |
| 2014-09 | NuBits begins |
| 2014-11-20 | Realcoin renamed Tether |
| 2017-12-18 | Dai launches on Ethereum |
| 2018-09-26 | USDC released for trading |
| 2018-12 | Basis shuts down |
| 2019-06-18 | Facebook announces Libra |
| 2019-11-18 | Multi-Collateral Dai goes live |
| 2020-03-12 | Maker's Black Thursday |
| 2021-06-16 | Iron Finance run |
| 2022-01-31 | Diem confirms shutdown |
| 2022-05 | TerraUSD collapses |
| 2022-06-08 | New York issues stablecoin guidance |
| 2023-02-21 | Paxos stops minting BUSD |
| 2023-03-10–13 | USDC depegs during the Silicon Valley Bank failure weekend |
| 2023-07-17 | FSB final recommendations |
| 2023-08-15 | Singapore finalises its framework |
| 2024-02 | Ethena USDe opens to the public |
| 2024-06-30 | MiCA stablecoin titles apply |
| 2025-07-18 | GENIUS Act signed |
| 2025-08-01 | Hong Kong Stablecoins Ordinance takes effect |
| 2025-11 | Stream xUSD and Elixir deUSD fail |
| 2026-04-10 | First Hong Kong issuer licences |
| 2026-06-30 | UK Financial Conduct Authority final rules |
| 2026-09-15 | CLARITY Act fails to advance in the Senate |
| 2026-09-30 | Open USD goes live |
| 2026-10-14 | Qivalis authorised by De Nederlandsche Bank |
| 2026-10-21 | OCC final rule under the GENIUS Act |

## See also

- [Ethena](ethena.md)
- [Curve](curve.md)

- [MakerDAO and Sky](makerdao-sky.md)

- [Tether](tether.md), issuer of USDT
- [USDC](usdc.md), issued by Circle
- [Terra](terra.md), whose UST collapsed in 2022
- [Aave](aave.md), issuer of GHO
- [Hyperliquid](hyperliquid.md)
- [Ethereum](ethereum.md)

## References

[^fed-stable]: Baughman, G., Carapella, F., Gerszten, J., and Mills, D. (2022). *The stable in stablecoins*. FEDS Notes, Board of Governors of the Federal Reserve System. <https://www.federalreserve.gov/econres/notes/feds-notes/the-stable-in-stablecoins-20221216.html>
[^nber-terra]: Liu, J., Makarov, I., and Schoar, A. (2023). *Anatomy of a run: the Terra Luna crash*. NBER Working Paper 31160. <https://www.nber.org/papers/w31160>
[^bis-170]: Aldasoro, I., Frost, J., and Ito, H. (2026). *The impact of stablecoins on the international monetary and financial system*. BIS Papers No 170. <https://www.bis.org/publ/bppdf/bispap170.htm>
[^genius]: US Congress (2025). *Public Law 119-27, GENIUS Act*. <https://www.congress.gov/119/plaws/publ27/PLAW-119publ27.htm>
[^mica-149]: ESMA. *MiCA Article 149: Entry into force and application*. <https://www.esma.europa.eu/publications-and-data/interactive-single-rulebook/mica/article-149-entry-force-and-application>.
[^mica-3]: ESMA. *MiCA Article 3: Definitions*, paragraphs 1(6)–(7). <https://www.esma.europa.eu/publications-and-data/interactive-single-rulebook/mica/article-3-definitions>.
[^bis-aer]: Bank for International Settlements (2025). *Annual Economic Report 2025*, chapter III. <https://www.bis.org/publ/arpdf/ar2025e3.htm>
[^gorton]: Zhang, J. Y. and Gorton, G. B. (2023). *Taming wildcat stablecoins*. University of Chicago Law Review 90(3): 909-972. <https://repository.law.umich.edu/articles/2896>
[^block-bitusd]: The Block (2019). *BitUSD hasn't had its $1 peg for more than two months*. <https://www.theblock.co/news/markets/2019-02-15-bitusd-hasnt-had-its-1-peg-for-more-than-two-months-11876>
[^realcoin]: CoinDesk (2014). *Brock Pierce announces dollar-backed cryptocurrency 'Realcoin'*. <https://www.coindesk.com/markets/2014/07/09/brock-pierce-announces-dollar-backed-cryptocurrency-realcoin>
[^rebrand]: CoinDesk (2014). *Realcoin rebrands as 'Tether' to avoid altcoin association*. <https://www.coindesk.com/markets/2014/11/20/realcoin-rebrands-as-tether-to-avoid-altcoin-association>
[^nubits]: Moneyness (2016). *The end of a stablecoin*. <https://www.moneyness.ca/2016/08/end-of-stablecoin.html>
[^coindesk-dai]: CoinDesk. *Dai price and overview*. <https://www.coindesk.com/price/dai/>
[^block-mcd]: The Block (2019). *Multi-Collateral Dai goes live on MakerDAO*. <https://www.theblock.co/news/ecosystems/2019-11-18-multi-collateral-dai-goes-live-on-makerdao-47416>
[^techcrunch-basis]: TechCrunch (2018). *Basis, backed with $133 million from top VCs to build a price-stable cryptocurrency, says it's shutting down and returning the money*. <https://techcrunch.com/2018/12/13/basis-backed-with-133-million-from-top-vcs-to-build-a-price-stable-cryptocurrency-says-its-shutting-down-and-returning-the-money>
[^coindesk-libra]: CoinDesk (2019). *Facebook unveils Libra cryptocurrency, targeting 1.7 billion unbanked*. <https://www.coindesk.com/markets/2019/06/18/facebook-unveils-libra-cryptocurrency-targeting-17-billion-unbanked>
[^coindesk-diem]: CoinDesk (2022). *Diem confirms shutdown as Silvergate acquires the project's assets*. <https://www.coindesk.com/business/2022/01/31/silvergate-bank-confirms-diem-tech-acquisition>
[^fed-iron]: Board of Governors of the Federal Reserve System (2022). *Runs on algorithmic stablecoins: evidence from Iron, Titan, and Steel*. FEDS Notes. <https://www.federalreserve.gov/econres/notes/feds-notes/runs-on-algorithmic-stablecoins-evidence-from-iron-titan-and-steel-20220602.htm>
[^ct-usdn]: Cointelegraph (2022). *Waves founder announces new stablecoin as USDN depegs*. <https://cointelegraph.com/news/waves-founder-announces-new-stablecoin-as-usdn-depegs>
[^block-husd]: The Block (2022). *HUSD stablecoin sharply loses peg even further, drops to just $0.30*. <https://www.theblock.co/news/markets/2022-10-31-husd-stablecoin-sharply-loses-peg-even-further-drops-to-just-0-30-181312>
[^fed-svb]: Du, C., Sonawane, R., and Watsky, C. (2025). *In the shadow of bank runs: lessons from the Silicon Valley Bank failure and its impact on stablecoins*. FEDS Notes, Board of Governors of the Federal Reserve System. <https://www.federalreserve.gov/econres/notes/feds-notes/in-the-shadow-of-bank-run-lessons-from-the-silicon-valley-bank-failure-and-its-impact-on-stablecoins-20251217.html>
[^paypal-launch]: PayPal (2023). *PayPal launches U.S. dollar stablecoin*. <https://newsroom.paypal-corp.com/2023-08-07-PayPal-Launches-U-S-Dollar-Stablecoin>
[^block-sofi]: The Block (2025). *SoFi launches SoFiUSD stablecoin to offer settlement infrastructure for banks and fintechs*. <https://www.theblock.co/news/markets/2025-12-18-sofi-launches-sofi-usd-stablecoin-383146>
[^unchained-ousd]: Unchained (2026). *Open USD stablecoin goes live as Stripe, Visa and Mastercard open it to businesses*. <https://unchainedcrypto.com/open-usd-stablecoin-goes-live-as-stripe-visa-and-mastercard-open-it-to-businesses/>
[^coindesk-openusd]: CoinDesk (2026). *Open USD rattled Circle's stock, but its key backers still support USDC*. <https://www.coindesk.com/business/2026/08/03/open-usd-rattled-circle-s-stock-but-its-key-backers-still-support-usdc>
[^fed-2025]: Carapella, F., Lubis, A., and Vardoulakis, A. (2026). *Stablecoins in 2025: developments and financial stability implications*. FEDS Notes, Board of Governors of the Federal Reserve System. <https://www.federalreserve.gov/econres/notes/feds-notes/stablecoins-in-2025-developments-and-financial-stability-implications-20260408.html>
[^llama]: DefiLlama. *Stablecoins*. <https://defillama.com/stablecoins>
[^llama-detail]: DefiLlama. *Stablecoin data API*. <https://stablecoins.llama.fi/stablecoins>
[^liquity-redemption]: Liquity. *Redemptions and LUSD price stability*. <https://docs.liquity.org/liquity-v1/faq/lusd-redemptions.md>
[^ethena-overview]: Ethena Labs. *Ethena overview*. <https://docs.ethena.fi/overview/ethena-overview.md>
[^ethena-docs]: Ethena Labs. *Ethena documentation*. <https://docs.ethena.fi/llms-full.txt>
[^clements]: Ryan Clements (2021). *Built to Fail: The Inherent Fragility of Algorithmic Stablecoins*, Wake Forest Law Review Online 11:131. <https://www.wakeforestlawreview.com/wp-content/uploads/2021/10/11WakeForestLRevOnline131.pdf>.
[^bean-docs]: Beanstalk. *How Beanstalk works*. <https://docs.bean.money/almanac/introduction/how-beanstalk-works.md>
[^usdai-docs]: USD.AI. *USD.AI docs*. <https://docs.usd.ai/>
[^polymarket-docs]: Polymarket. *Polymarket USD*. <https://docs.polymarket.com/concepts/pusd.md>
[^avant-docs]: Avant Protocol. *Core tokens*. <https://docs.avantprotocol.com/overview/core-tokens.md>
[^saturn-docs]: Saturn. *USDat overview*. <https://saturncredit.gitbook.io/saturn-docs/solution/usdat-overview.md>
[^fed-primary]: Watsky, C., Allen, J., Daud, H., Demuth, J., Little, D., Rodden, M., and Seira, A. (2024). *Primary and secondary markets for stablecoins*. FEDS Notes, Board of Governors of the Federal Reserve System. <https://www.federalreserve.gov/econres/notes/feds-notes/primary-and-secondary-markets-for-stablecoins-20240223.html>
[^lyons]: Lyons, R. K. and Viswanath-Natraj, G. (2020). *What keeps stablecoins stable?* NBER Working Paper 27136. <https://www.nber.org/papers/w27136>
[^ma]: Ma, Y., Zeng, Y., and Zhang, A. L. (2025). *Stablecoin runs and the centralization of arbitrage*. NBER Working Paper 33882. <https://www.nber.org/papers/w33882>
[^imf]: Adrian, T. and others (2025). *Understanding stablecoins*. International Monetary Fund Departmental Paper 25/09. <https://www.imf.org/en/Publications/Departmental-Papers/Issues/2025/12/02/Understanding-Stablecoins-570602>
[^coindesk-visa]: CoinDesk (2026). *Visa expands stablecoin settlement network as volume hits $7 billion run rate*. <https://www.coindesk.com/business/2026/04/29/visa-expands-stablecoin-settlement-network-as-volume-hits-usd7-billion-run-rate>
[^bis-1270]: Ahmed, R. and Aldasoro, I. (2025). *Stablecoins and safe asset prices*. BIS Working Papers No 1270. <https://www.bis.org/publ/work1270.htm>
[^bis-1370]: Hofmann, B., Mehrotra, A., and Paulick, J. (2026). *Dollarisation and monetary control: what lessons for the rise of stablecoins?* BIS Working Papers No 1370. <https://www.bis.org/publ/work1370.htm>
[^reuters-bis]: Reuters, via The Globe and Mail (2025). *Central bank body BIS delivers stark stablecoin warning*. <https://www.theglobeandmail.com/investing/article-central-bank-body-bis-delivers-stark-stablecoin-warning>
[^block-chainalysis]: Chainalysis (2026). *2026 Crypto Crime Report Introduction*. <https://www.chainalysis.com/blog/2026-crypto-crime-report-introduction/>.
[^fatf]: FATF (2026). *Targeted report on Stablecoins and Unhosted Wallets — Peer-to-Peer Transactions*, 3 March. <https://www.fatf-gafi.org/en/publications/Virtualassets/targeted-report-stablecoins-unhosted-wallets.html>.
[^block-un]: The Block (2024). *United Nations identifies USDT as prominent choice for fraud in SEA: FT*. <https://www.theblock.co/news/markets/2024-01-15-usdt-fraud-southeast-asia-united-nations-272568>
[^wilmerhale]: WilmerHale (2026). *OCC finalizes GENIUS Act rule for permitted payment stablecoin issuers, easing several key proposed requirements and raising new issues*. <https://www.wilmerhale.com/en/insights/client-alerts/20261027-occ-finalizes-genius-act-rule-for-permitted-payment-stablecoin-issuers-easing-several-key-proposed-requirements-and-raising-new-issues>
[^coindesk-yield]: CoinDesk (2026). *Clarity Act text lets crypto firms offer stablecoin rewards while shielding bank yield*. <https://www.coindesk.com/policy/2026/05/01/clarity-act-text-lets-crypto-firms-offer-stablecoin-rewards-while-shielding-bank-yield>
[^coindesk-clarity]: CoinDesk (2026). *Crypto industry reacts after Clarity Act fails Senate vote*. <https://www.coindesk.com/policy/2026/09/15/clarity-act-fails-in-senate-here-is-how-the-crypto-industry-is-reacting>
[^nydfs-2022]: New York State Department of Financial Services (2022). *Guidance on the issuance of U.S. dollar-backed stablecoins*. <https://www.dfs.ny.gov/industry_guidance/industry_letters/il20220608_issuance_stablecoins>
[^block-eurt]: The Block (2024). *Tether to end support for EURT stablecoin citing MiCA regulations, falling demand*. <https://www.theblock.co/post/328483/tether-discontinues-eurt>
[^block-lagarde]: The Block (2026). *ECB's Lagarde flags euro-denominated stablecoins as financial stability risk, diverging from Bundesbank stance*. <https://www.theblock.co/news/macro/2026-05-08-ecbs-lagarde-flags-euro-denominated-stablecoins-as-financial-stability-risk-diverging-from-bundesbank-stance-400548>
[^qivalis-dnb]: Qivalis (2026). *Qivalis receives authorisation as an Electronic Money Institution from De Nederlandsche Bank*. <https://qivalis.eu/press/news/qivalis-receives-authorisation-as-an-electronic-money-institution-from-de-nederlandsche-bank>
[^boe]: Bank of England (2026). *Sterling-denominated systemic stablecoins*. <https://www.bankofengland.co.uk/paper/2026/ps/sterling-denominated-systemic-stablecoin>
[^skadden-fca]: Skadden (2026). *FCA finalises core rules for the UK cryptoasset regime*. <https://www.skadden.com/insights/publications/2026/07/fca-finalises-core-rules-for-the-uk-cryptoasset-regime>
[^kpmg-uk]: KPMG (2026). *The UK's finalised regulatory regime for cryptoassets*. <https://kpmg.com/xx/en/our-insights/regulatory-insights/the-uk-finalised-regulatory-regime-for-cryptoassets.html>
[^hkma]: Hong Kong Monetary Authority. *Stablecoin issuers*. <https://www.hkma.gov.hk/eng/key-functions/international-financial-centre/stablecoin-issuers/>
[^charltons]: Charltons (2026). *HKMA issues first stablecoin issuer licences*. <https://www.charltonslaw.com/hkma-issues-first-stablecoin-issuer-licences/>
[^block-hkdap]: The Block (2026). *Standard Chartered-backed Anchorpoint begins HKDAP stablecoin rollout*. <https://www.theblock.co/news/business/2026-08-12-standard-chartered-anchorpoint-hkdap-stablecoin-rollout-411575>
[^decrypt-redcoin]: Decrypt (2026). *Hong Kong bank HSBC stablecoin 3 million wallets*. <https://decrypt.co/381760/hong-kong-bank-hsbc-stablecoin-3-million-wallets>
[^hsbc-licence]: HSBC (2026). *HSBC welcomes HKMA's grant of a Hong Kong stablecoin issuer licence*. <https://www.about.hsbc.com.hk/news-and-media/hsbc-welcomes-hkmas-grant-of-a-hong-kong-stablecoin-issuer-licence>
[^mas]: Monetary Authority of Singapore (2023). *MAS finalises stablecoin regulatory framework*. <https://www.mas.gov.sg/news/media-releases/2023/mas-finalises-stablecoin-regulatory-framework>
[^iflr]: IFLR (sponsored content). *Stablecoins under Japan's amended Payment Services Act*. <https://www.iflr.com/article/2ai02f5kcnevykck8zoqo/sponsored/stablecoins-under-japans-amended-payment-services-act>
[^block-jpyc]: The Block (2025). *Japan's JPYC launches country's first yen-denominated stablecoin*. <https://www.theblock.co/news/business/2025-10-27-japan-jpyc-launches-yen-stablecoin-376199>
[^coindesk-korea]: CoinDesk (2026). *South Korea proposes cryptocurrency law with bank-style rules for stablecoins*. <https://www.coindesk.com/policy/2026/04/08/south-korea-proposes-cryptocurrency-law-with-bank-style-rules-for-stablecoins>
[^fsb-2023]: Financial Stability Board (2023). *High-level recommendations for the regulation, supervision and oversight of global stablecoin arrangements: final report*. <https://www.fsb.org/2023/07/high-level-recommendations-for-the-regulation-supervision-and-oversight-of-global-stablecoin-arrangements-final-report/>
[^fsb-2025]: Financial Stability Board (2025). *FSB finds significant gaps and inconsistencies in implementation of crypto and stablecoin recommendations*. <https://www.fsb.org/2025/10/fsb-finds-significant-gaps-and-inconsistencies-in-implementation-of-crypto-and-stablecoin-recommendations/>
[^agora]: Agora. *Agora*. <https://www.agora.finance/>
[^wormhole-moveusd]: Wormhole (2025). *MOVEUSD stablecoin chooses Wormhole's NTT standard for multichain expansion*. <https://wormhole.com/blog/moveusd-stablecoin-chooses-wormholes-ntt-standard-for-multichain-expansion>
[^taiwan-fd]: Taiwan News, via GlobeNewswire (2026). *First Digital signs definitive agreement to become a publicly listed company*. <https://www.taiwannews.com.tw/en/news/6453338>
[^chaos-frxusd]: Chaos Labs (2025). *frxUSD token review*. <https://chaoslabs.xyz/posts/frxusd-token-review>
[^gemini]: Gemini. *Gemini Dollar*. <https://www.gemini.com/dollar>
[^forklog-gusd]: ForkLog (2018). *Gemini launches world's first regulated stablecoin*. <https://forklog.com/en/gemini-launches-worlds-first-regulated-stablecoin/>
[^paxos-usdg]: Paxos (2024). *Paxos introduces Global Dollar (USDG)*. <https://paxos.com/blog/paxos-introduces-global-dollar-usdg/>
[^block-m0]: The Block (2024). *Cosmos-based Noble first to launch custom stablecoin using cryptodollar infrastructure startup M^0*. <https://www.theblock.co/post/329332/cosmos-based-noble-first-to-launch-custom-stablecoin-using-cryptodollar-infrastructure-startup-m0>
[^coindesk-pax]: Paxos (2018). *Paxos launches new stablecoin, Paxos Standard (PAX)*. <https://www.paxos.com/newsroom/paxos-launches-new-stablecoin-paxos-standard-pax>.
[^ripple]: Ripple. *Stablecoin solutions*. <https://ripple.com/products/stablecoin/>
[^fortune-rlusd]: Ripple (2024). *Ripple USD Launches Globally*, 16 December. <https://ripple.com/ripple-press/raising-the-standard-for-stablecoins-ripple-usd-launches-globally/>.
[^coindesk-tusd]: CoinDesk (2025). *Tron's Justin Sun bailed out TUSD as stablecoin's $456M reserves were stuck in limbo, filings show*. <https://www.coindesk.com/markets/2025/04/02/tron-s-justin-sun-bailed-out-tusd-as-stablecoin-s-usd456m-reserves-were-stuck-in-limbo>
[^fy-2025]: CoinDesk (2026). *Tether's gold holdings top $17 billion as net profits surpassed $10 billion for 2025*. <https://www.coindesk.com/business/2026/01/30/tether-s-gold-holdings-top-usd17-billion-as-net-profits-surpassed-usd10-billion-for-2025>
[^transparency]: Circle. *Transparency and stability*. <https://www.circle.com/transparency>
[^usat-launch]: CoinDesk (2026). *Tether takes the fight to Circle with a new 'made in America' stablecoin*. <https://www.coindesk.com/business/2026/01/27/tether-debuts-federally-regulated-usat-stablecoin-via-anchorage-digital>
[^usat]: USAT. *USA₮*. <https://usat.io/>
[^coindesk-usdc]: CoinDesk (2018). *USD Coin arrives: Circle's crypto stablecoin is now trading*. <https://www.coindesk.com/markets/2018/09/26/usd-coin-arrives-circles-crypto-stablecoin-is-now-trading>
[^block-usd1]: The Block (2025). *World Liberty Financial debuts plan for USD1 stablecoin as President Trump continues push for crypto legislation*. <https://www.theblock.co/post/347995/world-liberty-financial-debuts-plan-for-usd1-stablecoin-as-president-trump-continues-push-for-crypto-legislation>
[^bitgo]: BitGo. *USD1 attestations*. <https://www.bitgo.com/usd1/attestations>
[^usual-docs]: Usual. *USD0*. <https://docs.usual.money/usual-products/usd0-stablecoin/usd0.md>
[^usual-roadmap]: Usual. *Usual: the first two years*. <https://docs.usual.money/resources-and-ecosystem/roadmap/usual-the-first-two-years.md>
[^anchorage-usdgo]: Anchorage Digital (2026). *USDGO officially launches under federal oversight*. <https://www.anchorage.com/insights/usdgo-officially-launches-under-federal-oversight>
[^block-usdtb]: The Block (2025). *Anchorage Digital to issue first GENIUS-compliant stablecoin in US with Ethena Labs*. <https://www.theblock.co/post/364119/anchorage-digital-genius-stablecoin-ethena>
[^anchorage-ethena]: Anchorage Digital. *Ethena Labs: launching the first federally regulated stablecoin*. <https://www.anchorage.com/client-stories/ethena-labs>
[^alchemix]: Alchemix. *alAssets*. <https://docs.alchemix.fi/user/concepts/alAssets>
[^apyx]: Apyx. *Peg stability model*. <https://docs.apyx.fi/solution-overview/peg-stability-model.md>
[^liquity-bold]: Liquity. *BOLD and Earn*. <https://docs.liquity.org/v2-faq/bold-and-earn.md>
[^liquity-v2]: Liquity (2025). *Liquity V2 is LIVE*. <https://www.liquity.org/blog/liquity-v2-is-live>
[^galaxy-crvusd]: Galaxy (2023). *Curve Finance's crvUSD: a novel stablecoin design by Curve*. <https://galaxy.com/insights/research/curve-stablecoin-crvusd>
[^dss]: Maker. *Multi Collateral Dai*, dss repository. <https://raw.githubusercontent.com/makerdao/dss/master/README.md>
[^inverse]: Inverse Finance. *Getting started*. <https://docs.inverse.finance/>
[^bankless-ethena]: Bankless. *The year Ethena took over*. <https://www.bankless.com/read/the-year-ethena-took-over>
[^decrypt-falcon]: Decrypt, via Chainwire (2025). *Falcon Finance opens to the public and launches "Falcon Miles" points program*. <https://decrypt.co/317070/falcon-finance-opens-to-the-public-and-launches-falcon-miles-points-program>
[^falcon]: Falcon Finance. *USDf peg stability*. <https://docs.falcon.finance/mechanism/usdf-synthetic-dollar/usdf-peg-stability>
[^gho-block]: The Block (2023). *Aave DAO deploys GHO stablecoin on Ethereum mainnet*. <https://www.theblock.co/post/239688/aave-dao-deploys-gho-stablecoin-on-ethereum-mainnet>
[^gho-docs]: Aave documentation. *GHO stablecoin*. <https://aave.com/docs/ecosystem/gho>
[^gyro]: Gyroscope. *GYD overview*. <https://docs.gyro.finance/gyd/>
[^forklog-liquity]: ForkLog (2021). *Liquity DeFi protocol launches on Ethereum mainnet*. <https://forklog.com/en/liquity-defi-protocol-launches-on-ethereum-mainnet/>
[^abracadabra]: Abracadabra. *Introduction*. <https://docs.abracadabra.money/>
[^block-sky]: The Block (2024). *MakerDAO rebrands to Sky, DAI stablecoin optionally upgradeable to USDS*. <https://www.theblock.co/post/313235/makerdao-mkr-sky-dai-stablecoin-usds>
[^sky]: Sky.money (2026). *Understanding the SKY Token*. <https://sky.money/blog/understanding-the-sky-token>.
[^decrypt-usx]: Decrypt, via Chainwire (2025). *Solstice Finance officially launches USX, a Solana-native stablecoin with $160M deposited TVL*. <https://decrypt.co/342125/solstice-finance-officially-launches-usx-a-solana-native-stablecoin-with-160m-deposited-tvl>
[^decrypt-usda]: Decrypt, via Avalon Labs (2024). *Avalon Labs introduces USDa: a BTC-backed stablecoin for liquidity in DeFi and CeFi ecosystems*. <https://decrypt.co/291138/avalon-labs-introduces-usda-a-btc-backed-stablecoin>
[^block-usdd]: The Block (2022). *Tron's new algorithmic stablecoin USDD goes live*. <https://www.theblock.co/post/145231/trons-new-stablecoin-usdd-goes-live>
[^block-usdd2]: The Block (2025). *Justin Sun says 'stop' asking questions about the next iteration of Tron's USDD stablecoin and its 20% yield*. <https://www.theblock.co/post/334835/justin-sun-says-stop-asking-questions-about-the-next-iteration-of-trons-usdd-stablecoin-and-its-20-yield>
[^hackernoon-aster]: Chainwire, via HackerNoon (2025). *Aster emerges: Astherus rebrands to lead decentralized perpetual trading*. <https://hackernoon.com/aster-emerges-astherus-rebrands-to-lead-decentralized-perpetual-trading>
[^ct-polymarket]: Cointelegraph (2026). *Polymarket overhauls smart contracts with new Protocol V2 rollout*. <https://cointelegraph.com/news/polymarket-smart-contract-overhaul-protocol-v2>
[^bnb-u]: BNB Chain (2025). *United Stables launches U as a native stablecoin on BNB Chain*. <https://www.bnbchain.org/en/blog/united-stables-launches-u-as-a-native-stablecoin-on-bnb-chain>
[^ofac-a7a5]: US Department of the Treasury (2025). *Treasury sanctions cryptocurrency exchange and network enabling sanctions evasion and cyber criminals*. <https://home.treasury.gov/news/press-releases/sb0225>
[^elliptic]: Elliptic (2026). *The fall of A7A5: how sanctions strangled the ruble stablecoin*. <https://www.elliptic.co/insights/the-fall-of-a7a5-how-sanctions-strangled-the-ruble-stablecoin/>
[^standard-axcnh]: The Standard (2025). *China's yuan stablecoin debut in Kazakhstan signals blockchain ambition*. <https://www.thestandard.com.hk/innovation/article/312793/Chinas-yuan-stablecoin-debut-in-Kazakhstan-signals-blockchain-ambition>
[^bilira]: BiLira. *TRYB stablecoin*. <https://bilira.co/en/product/tryb-stablecoin>
[^transfero]: Transfero. *BRZ*. <https://transfero.com/brz-stablecoin>
[^sgforge]: Societe Generale-Forge. *EUR CoinVertible*. <https://www.sgforge.com/product/coinvertible/>
[^kitco-eurcv]: Kitco (2023). *SocGen unveils EUR CoinVertible, a euro-pegged stablecoin on the Ethereum network*. <https://www.kitco.com/news/article/2023-04-20/socgen-unveils-eur-coinvertible-euro-pegged-stablecoin-ethereum-network>
[^circle-euroc]: Circle (2022). *Circle announces a fully-reserved, euro-backed stablecoin, Euro Coin (EUROC)*. <https://www.circle.com/pressroom/circle-announces-a-fully-reserved-euro-backed-stablecoin-euro-coin-euroc>
[^circle-eurc]: Circle. *EURC*. <https://www.circle.com/eurc>
[^banking-circle]: Banking Circle (2024). *Banking Circle launches the first bank-backed MiCA-compliant stablecoin, EURI*. <https://www.bankingcircle.com/banking-circle-launches-the-first-bank-backed-mica-compliant-stablecoin-euri/>
[^frankencoin]: Frankencoin (2023). *Introducing Frankencoin: an oracle-free collateralized Swiss franc stablecoin project*. <https://frankencoin.substack.com/p/introducing-frankencoin-an-oracle>
[^block-jpysc]: The Block (2026). *SBI Group launches Japan's first trust bank-backed stablecoin JPYSC*. <https://www.theblock.co/news/defi/2026-06-24-japan-sbi-group-launches-jpysc-405952>
[^monerium]: Monerium (2025). *White paper: Monerium EURe*. <https://monerium.com/whitepapers/eure-whitepaper.xhtml>
[^paxos-gold]: Paxos (2019). *Paxos launches PAX Gold: physical gold on the blockchain*. <https://www.paxos.com/newsroom/paxos-launches-pax-gold-physical-gold-on-the-blockchain>
[^buidl]: BlackRock, via Silicon UK (2024). *BlackRock launches its first tokenized fund, BUIDL, on the Ethereum network*. <https://www.silicon.co.uk/press-release/blackrock-launches-its-first-tokenized-fund-buidl-on-the-ethereum-network>
[^gate]: Gate. *GUSD*. <https://www.gate.com/gusd>
[^multipli]: Multipli. *rwaUSDi: the institutional credit layer for tokenized private markets*. <https://docs.multipli.fi/rwausd/liquidity-classes-why-segmentation-by-design/rwausdi-the-institutional-credit-layer-for-tokenized-private-markets.md>
[^paxos-busd]: Paxos (2023). *Paxos will halt minting new BUSD tokens*. <https://www.paxos.com/newsroom/paxos-will-halt-minting-new-busd-tokens>
[^block-deusd]: The Block (2025). *Elixir sunsets deUSD synthetic stablecoin following Stream Finance unwinding, aims for full redemptions*. <https://www.theblock.co/news/markets/2025-11-06-elixir-sunsets-deusd-synthetic-stablecoin-following-stream-finance-unwinding-aims-full-redemptions-377961>
[^boardroom-fei]: Boardroom (2022). *This week in governance: August 25*. <https://governance.substack.com/p/-this-week-in-governance-august-25>
[^block-coinflex]: The Block (2023). *Coinflex says restructuring plan is approved by Seychelles court*. <https://www.theblock.co/news/business/2023-03-07-coinflex-restructuring-plan-approved-217724>
[^gmo]: GMO-Z.com Trust Company. *GMO Trust stablecoin site*. <https://stablecoin.z.com>
[^reflexer-faq]: Reflexer. *FAQ*. <https://docs.reflexer.finance/faq>
[^reflexer-x]: Reflexer (2025). *Global Settlement update*. <https://x.com/reflexerfinance/status/1933586893658296722>
[^block-usdr]: The Block (2023). *Real USD (USDR) stablecoin depegs and price crashes by 50%*. <https://www.theblock.co/news/markets/2023-10-11-real-usd-usdr-stablecoin-depegs-and-price-crashes-by-50-255946>
[^decrypt-xusd]: Decrypt (2025). *Stream Finance stablecoin plunges 77% after protocol's fund manager loses $93 million*. <https://decrypt.co/347285/stream-finance-stablecoin-plunges-77-protocol-fund-manager-loses-93-million>
[^synthetix-docs]: Synthetix (2026). *420 legacy staking*. <https://docs.synthetix.io/legacy-migration/420-legacy-staking>
[^block-usdh]: The Block (2026). *Coinbase becomes Hyperliquid's official USDC treasury deployer as USDH sunsets*. <https://www.theblock.co/post/401233/coinbase-hyperliquid-official-deployer-usdc>
[^block-binance-busd]: The Block (2023). *Binance to end support for BUSD, encourages conversion to FDUSD*. <https://www.theblock.co/post/248301/binance-ends-busd-support-fdusd>
[^fip-428]: Frax Core Team (2025). *[FIP-428] Frax North Star proposal, V2*. <https://gov.frax.finance/t/fip-428-frax-north-star-proposal-v2/3652>
[^coinex-frax]: CoinEx (2026). *CoinEx will support FXS mainnet swap and token rename*. <https://www.coinex.com/tr/announcements/detail/44884713967124>
[^ct-maker]: Cointelegraph (2020). *Maker debt crisis post-mortem recommends new safeguards*. <https://cointelegraph.com/news/maker-debt-crisis-post-mortem-recommends-new-safeguards>
[^glassnode]: Glassnode (2020). *What really happened to MakerDAO?* <https://research.glassnode.com/what-really-happened-to-makerdao/>
[^ct-bean]: Cointelegraph (2022). *Beanstalk Farms loses $182M in DeFi governance exploit*. <https://cointelegraph.com/news/beanstalk-farms-loses-182m-in-defi-governance-exploit>
[^fortune-usdd]: Fortune, via CoinDesk (2022). *Another algorithmic stablecoin loses its peg as Tron's USDD falls, with founder Justin Sun vowing to deploy $2 billion*. <https://fortune.com/2022/06/13/algorithmic-stablecoin-usdd-loses-peg-justin-sun-tron-decentralized-usd>
[^unchained-mim]: Unchained (2024). *MIM loses peg after $6.5 million exploit on Abracadabra Ethereum cauldrons*. <https://unchainedcrypto.com/mim-loses-peg-after-6-5-million-exploit-on-abracadabra-ethereum-cauldrons/>
[^sec-tusd]: US Securities and Exchange Commission (2024). *Press release 2024-145*. <https://www.sec.gov/newsroom/press-releases/2024-145>
[^ct-usd0]: Cointelegraph (2025). *Usual Protocol to activate 'revenue switch' after USD0++ depegs*. <https://cointelegraph.com/news/usd0-stablecoin-depeg-revenue-switch>
[^block-usd0]: The Block (2025). *Usual Money's protocol update sparks community concern as USD0++ drops below 92 cents*. <https://www.theblock.co/news/defi/2025-01-10-usual-money-protocol-update-333995>
[^decrypt-fdusd]: Decrypt (2025). *Binance-backed FDUSD stablecoin loses dollar peg following Justin Sun accusations*. <https://decrypt.co/312984/fdusd-stablecoin-loses-dollar-peg-justin-sun>
[^decrypt-susd]: Decrypt (2025). *Synthetix's sUSD stablecoin depegs to new low of $0.66*. <https://decrypt.co/315338/synthetixs-susd-stablecoin-depegs-to-new-low-of-0-66>
[^synthetix-blog]: Synthetix (2025). *The Repeggening*. <https://blog.synthetix.io/the-repeggening/>
[^ct-falcon]: Cointelegraph (2025). *Falcon USD stablecoin depegs amid liquidity drop and transparency fears*. <https://cointelegraph.com/news/falcon-usd-stablecoin-depegs-liquidity-collateral-concerns>
[^nydfs-paxos]: New York State Department of Financial Services (2025). *Press release on Paxos settlement*. <https://www.dfs.ny.gov/reports_and_publications/press_releases/pr20250806>
[^block-paxos]: The Block (2025). *Paxos settles with New York financial regulator for $48.5 million over involvement with Binance BUSD partnership*. <https://www.theblock.co/post/366002/paxos-settles-with-new-york-financial-regulator-for-48-5-million-over-involvement-with-binance-busd-partnership>
[^ct-usde]: Cointelegraph (2025). *USDe depeg oracle issues, Ethena founder*. <https://cointelegraph.com/news/usde-depeg-oracle-issues-ethena-founder>
[^block-binance]: The Block (2025). *Binance pays $283 million in compensation following Friday's depegs, covering user losses*. <https://theblock.co/post/374295/binance-pays-283-million-in-compensation-following-fridays-depegs-covering-user-losses>
[^block-pyusd]: The Block (2025). *Paxos mistakenly mints $300 trillion PYUSD on Ethereum, citing tech error*. <https://www.theblock.co/post/374870/paxos-mistakenly-mints-300-trillion>

[^cato-nubits]: Lawrence H. White, Cato Institute (2017). *Dollar-Denominated Cryptocurrencies: Flops and Tethered Success*. <https://www.cato.org/blog/dollar-denominated-cryptocurrencies-flops-tethered-success>.

[^occ-wlf]: OCC (2026). *Corporate Decision 1385*, 14 August, pp. 1–2. Archived copy of the OCC decision; original OCC site under maintenance at check time. <https://upload.wikimedia.org/wikipedia/commons/a/a6/Corporate_Decision_1385_Re_Application_to_Charter_World_Liberty_Trust_Company.pdf>.

[^tether-cnht]: Tether (2026). *Tether Updates Users on a Strategic Transition for CNH₮*. <https://tether.io/news/tether-updates-users-on-a-strategic-transition-for-cnht-to-better-support-community-driven-product-focus/>.

[^block-fdusd]: The Block (2025). *The Daily*, 2 April, FDUSD depeg and First Digital response. <https://www.theblock.co/newsletters/the-daily/2025-04-02-the-daily-crypto-market-braces-for-trumps-liberation-day-impact-fdusd-stablecoin-depegs-after-justin-sun-raises-solvency-concerns-and-more-349328>.

[^bloomberg-pyusd]: Bloomberg (2025). *Paxos Mistakenly Issues $300 Trillion of PayPal Stablecoin*. <https://news.bloomberglaw.com/crypto/paxos-mistakenly-issues-300-trillion-of-paypal-stablecoin>.

[^difc-tusd]: DIFC Courts (2025). *Techteryx Ltd v Aria Commodities DMCC and others*, amended judgment 17 October, especially paragraphs 2, 384 and 419. <https://www.difccourts.ae/rules-decisions/judgments-orders/digital-economy-court/techteryx-ltd-v-1-aria-commodities-dmcc-2-mashreq-bank-psc-3-emirates-nbd-bank-pjsc-4-abu-dhabi-islamic-bank-pjsc-2025-difc-dec>.

[^saga-incident]: Saga (2026). *SagaEVM Security Incident — Investigation Update*, 22 January. <https://medium.com/sagaxyz/sagaevm-security-incident-investigation-update-29a1d2a6b0cd>.

[^certik-usr]: CertiK (2026). *Resolv Protocol Incident Analysis*. <https://www.certik.com/blog/resolv-protocol-incident-analysis>.

[^warren-wlf]: Elizabeth Warren (2026). *Letter to Comptroller Jonathan Gould*, 13 January. <https://www.banking.senate.gov/imo/media/doc/0113lettertooccrewlfapplication.pdf>.

[^phantom-cash]: Phantom (2025). *Phantom Cash Accounts Are Here*, 17 November. <https://phantom.com/learn/blog/phantom-cash-accounts-are-here>.

[^aster-usdf]: Aster documentation. *How USDF Works*. <https://docs.asterdex.com/usdf-stablecoin/overview/how-usdf-works.md>.

[^audd-launch]: AUDD (2022). *The Building Blocks that make AUDD the Secure Stablecoin of the Future*, 8 November. <https://www.audd.digital/the-building-blocks-that-make-audd-the-secure-stablecoin-of-the-future/>.

[^audd-terms]: AUDD (2024). *AUDD Terms and Conditions*, 2 July. <https://www.audd.digital/audd-terms-and-conditions/>.

[^stasis]: STASIS. *The History of Euro Internet Money*. <https://stasis.net/about-us>.

[^straitsx-terms]: StraitsX (2026). *Token Terms and Conditions*, effective 18 July. <https://www.straitsx.com/legal/token>.

[^mas-straitsx]: Monetary Authority of Singapore. *StraitsX SGD Issuance Pte Ltd*, Financial Institutions Directory. <https://eservices.mas.gov.sg/fid/institution/detail/420461-STRAITSX-SGD-ISSUANCE-PTE-LTD>.

[^figure-ylds]: Figure. *YLDS*, issuer disclosure of SEC-registered fixed-income debt security. <https://www.ylds.com/>.

[^tether-gold]: Tether (2026). *Tether Gold Accounts for More Than Half the Entire Gold-Backed Stablecoin Market as XAU₮ Surpasses $4 Billion in Value*, 26 January. <https://tether.io/news/tether-gold-accounts-for-more-than-half-the-entire-gold-backed-stablecoin-market-as-xaut-surpasses-4-billion-in-value/>.

[^frax-original]: Frax Finance documentation. *Original Design*. <https://docs.frax.finance/frax-v1-original/original-design>.

[^block-usdx]: The Block (2025). *Synthetic stablecoin USDX depegs below $0.60, PancakeSwap and Lista monitoring the situation*. <https://www.theblock.co/news/markets/2025-11-06-synthetic-stablecoin-usdx-depegs-pancakeswap-lista-377917>.

[^block-korea]: The Block (2026). *South Korea’s crypto bill nears completion while tax debate intensifies*, 22 October. <https://www.theblock.co/news/regulation/2026-10-22-south-koreas-crypto-bill-nears-completion-421880>.

[^occ-final]: OCC (2026). *Final rule implementing the GENIUS Act*, Federal Register 91:67000–67194, published 23 October. <https://www.govinfo.gov/content/pkg/FR-2026-10-23/html/2026-21706.htm>.

[^esma-october]: ESMA (2026). *ESMA sets out supervisory expectations on services related to unauthorised stablecoins*, 8 October. <https://www.esma.europa.eu/press-news/esma-news/esma-sets-out-supervisory-expectations-services-related-unauthorised>.

[^fsb-2026]: FSB (2026). *FSB Chair sets out FSB work on AI and stablecoins*, 12 October. <https://www.fsb.org/2026/10/fsb-chair-sets-out-fsb-work-on-ai-and-stablecoins/>.

[^eba-usdc]: European Banking Authority (2026-10-14). *The EBA classifies USDC as the first significant e-money token in the European Union*. <https://www.eba.europa.eu/publications-and-media/press-releases/eba-classifies-usdc-first-significant-e-money-token-european-union>.

[^uk-budget-tax]: HM Treasury (2026-10-28). *Budget 2026: overview of tax legislation and rates*, section 1.35. <https://www.gov.uk/government/publications/budget-2026-overview-of-tax-legislation-and-rates-ootlar/budget-2026-overview-of-tax-legislation-and-rates-ootlar>.

[^hmrc-tax]: HM Revenue & Customs (updated 2026-10-28). *Taxation of stablecoins*. <https://www.gov.uk/government/publications/tax-treatment-of-stablecoins/taxation-of-stablecoins>.
