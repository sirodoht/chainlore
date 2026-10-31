---
title: Satoshi Nakamoto
ticker: None
category: Person
written_by: GPT-6-Astra high
status: ai-fact-checked
checked: 2026-10-31
checked_by: GPT-6-Astra high
updated: 2026-10-31
---

# Satoshi Nakamoto

Satoshi Nakamoto is the pseudonym associated with the creation of
[Bitcoin](bitcoin.md), the publication of its whitepaper in 2008, and the
initial software release in January 2009. The public record includes
mailing-list messages, software announcements, and correspondence with
early contributors. It does not establish a confirmed real-world identity
for the name.[^announcement][^release][^judgment]

| | |
|---|---|
| Known for | Bitcoin whitepaper and initial software |
| Whitepaper announcement | 2008-10-31[^announcement] |
| Genesis block timestamp | 2009-01-03[^genesis] |
| v0.1 mailing-list announcement | 2009-01-08, in the archive's EST timestamp[^release] |
| Documented later correspondence | April 2011[^hearn] |
| Identity | Pseudonymous; unresolved[^judgment] |

## Whitepaper and design

Preparations preceded the public announcement. In an email dated 22 August
2008, preserved in correspondence supplied by Wei Dai, Nakamoto asked Dai
for the publication year of his b-money proposal so it could be cited
properly. Nakamoto said Adam Back had pointed out similarities and directed
them to Dai's work. The message linked to a draft under the title
*Electronic Cash Without a Trusted Third Party*. This exchange documents
contact with earlier digital-cash researchers before the mailing-list
publication, without establishing how much of the design came from any
one predecessor.[^dai]

On 31 October 2008, Nakamoto posted a link to *Bitcoin: A Peer-to-Peer
Electronic Cash System* on the cryptography mailing list. The announcement
proposed electronic payments without a central trusted operator and
invited discussion of a peer-to-peer solution to double-spending.[^announcement]

The paper combines digital signatures, a timestamped chain of blocks,
proof of work, and incentives for participants. Its security argument
depends on honest nodes controlling more computational power than a
cooperating attacker. The references include earlier work such as Adam
Back's Hashcash and Wei Dai's b-money, placing the proposal within a
longer history of digital-cash research.[^paper]

The problem was more than proving who could authorise a payment: digital
signatures alone could not establish whether the same funds had already
been spent. Nakamoto proposed a shared transaction history whose ordering
was secured by computational work. Replacing an earlier block would
require redoing its work and catching up with the blocks added after it.
New coins and transaction fees would reward participants for maintaining
that history.[^paper]

The paper also distinguished public transaction records from the identities
behind them. It proposed using fresh keys to reduce linkability, while
acknowledging that transactions combining several inputs could reveal
common ownership. Its privacy discussion therefore described limits as
well as possible protections.[^paper]

## Launch and early participants

Discussion began before the software was publicly released. In a
November 2008 reply to Hal Finney on the cryptography mailing list,
Nakamoto described how nodes would retain pending transactions, check
signatures, and resolve competing branches. Nakamoto also said that
writing the code had preceded writing the paper: implementation was
needed to establish that the design's problems could be solved. This
was the creator's account of the development sequence, rather than a
dated record of every programming milestone.[^discussion]

The exchange addressed a practical question for merchants: when was a
payment sufficiently settled to justify handing over goods? Nakamoto
explained that an attacker trying to replace a payment would have to
compete with the work accumulating on the accepted history, and suggested
waiting perhaps an hour before shipping. That was an early explanation
of confirmation risk, rather than a guarantee that any fixed waiting
period makes a payment irreversible. Finney's questions show that
transaction propagation and competing histories were already being
scrutinised before launch.[^discussion]

Bitcoin's genesis block carries a timestamp of 3 January 2009. Its
transaction embeds the text "The Times 03/Jan/2009 Chancellor on brink of
second bailout for banks." Bitcoin Core's source preserves both that
message and the block's identifying parameters. The code also records
that the genesis transaction's 50-bitcoin output cannot be spent, a
special property of the initial block.[^genesis]

The original mailing-list archive dates the v0.1 release announcement to
8 January 2009 at 14:27 EST. It supplied a Windows download with
open-source C++ code.[^release]

Nakamoto warned that the software was experimental and that a restart
could become necessary. The announcement invited users to keep nodes
available for incoming connections and explained how to generate coins
on an ordinary PC. Initial mining difficulty was deliberately low, with
competition expected to raise it through automatic adjustments.[^release]

The same announcement described a maximum issuance of 21 million coins,
with the amount issued falling by half roughly every four years. It
also anticipated transaction fees eventually replacing newly generated
coins as the main payment to network operators.[^release]

Hal Finney's 2013 retrospective supplies a participant's account of those
first days. His interest drew on earlier digital-cash work, including
his own reusable proof-of-work experiment, RPOW, and correspondence with
Wei Dai and Nick Szabo. He recalled downloading the release immediately,
mining an early block, and receiving ten bitcoins from Nakamoto as a test. He described
their subsequent email exchanges as a cycle of bug reports and fixes,
with Finney testing the program and Nakamoto responding.[^finney]

Finney also recalled running the software on a CPU and eventually stopping
because of heat and fan noise. His account connects the launch to
practical experimentation on personal computers. It records his direct
experience of the software and correspondence, rather than establishing
the real-world identity of the person using the Nakamoto name.[^finney]

## Development and withdrawal

Correspondence published by early contributor Martti Malmi shows the
practical work surrounding the program. In November 2009, Malmi reported
installing two candidate forum systems, phpBB3 and Simple Machines Forum,
for comparison. In December, Nakamoto praised the new Drupal-based
bitcoin.org site. The exchanges document work on the project's website
and discussion infrastructure alongside software development.[^malmi]

The same archive preserves a July 2010 message about removing qualified
anonymity claims from the homepage. Nakamoto warned that transaction history
could reveal information and that using Bitcoin anonymously required
precautions. Separately, a July release message described version 0.3's
command-line JSON-RPC support and credited Laszlo for the Mac OS X
version. The archive therefore records both a more careful public
description of privacy and contributions to making the software usable
beyond its original Windows release.[^malmi]

An urgent incident interrupted that development in August 2010. On
15 August, Nakamoto announced version 0.3.10 as an overflow patch for
block 74,638. The announcement urged users to upgrade. The edited post
reported that the correct chain had overtaken the bad chain and said
upgraded clients would reorganise automatically; deleting local block
files was no longer necessary. The record distinguishes the software
fix from the subsequent recovery of the accepted chain. Because the
post was edited on 16 August, its recovery instructions should not all
be treated as statements made at the instant the patch was first
announced.[^overflow]

The patch announcement also listed Windows, Linux, and Mac OS X packages
and credited tcatm for a four-way SSE2 SHA-256 implementation. That
optimisation was described as improving hashing performance on some CPUs.
Even an emergency release thus combined a consensus-related repair with
platform packaging and another contributor's performance work.[^overflow]

Nakamoto also expressed concern about attracting attention before the
software was ready. On 5 December 2010, during a forum discussion about
WikiLeaks accepting Bitcoin, Nakamoto appealed against that use at the
time. The post described a small beta-stage community and argued that
the publicity could overwhelm the project while raising little money
for WikiLeaks. It documents caution about growth and exposure, but does
not by itself explain the later decision to withdraw from development
or establish what happened to Nakamoto afterwards.[^wikileaks]

Nakamoto continued publishing technical updates after the launch. In a
12 December 2010 forum post announcing version 0.3.19, Nakamoto described
new controls against denial-of-service attacks and the removal of
temporary safe-mode alerts. The post explicitly warned that the software
remained vulnerable to denial of service. It presented the release as
an incremental improvement, with further defensive work still needed.[^development]

Nakamoto also discussed development with early contributors. In an April
2011 email exchange preserved by recipient Mike Hearn, Nakamoto explained
how pre-signed transactions and a timelock could structure a contract,
then encouraged Hearn's Java implementation of Bitcoin. In the message
dated 23 April, Nakamoto said they had moved to other work and expressed
confidence in Gavin and the other developers.[^hearn]

The exchange also explains a constraint on Bitcoin's scripting system:
Nakamoto warned that reliance on changing external information, or
information that differed between nodes, could split the chain. The
proposed contract instead arranged signatures and a timed release in
advance, so participants knew the terms before committing their funds.[^hearn]

That email documents a withdrawal from active involvement. It does not
establish the author's motives, later circumstances, or legal identity;
those conclusions go beyond the message.[^hearn]

## Identity claims and litigation

In *Crypto Open Patent Alliance v Wright*, the High Court of England and
Wales considered Craig Wright's claim to be Nakamoto. The court announced
its conclusion on 14 March 2024 and published its reasons on 20 May. It
found that Wright was not the person who used the pseudonym in 2008–2011,
did not write the whitepaper or initial software, and did not create
Bitcoin. The judgment rejected a particular identity claim; it did not
identify the actual creator.[^judgment]

Subsequent proceedings concerned compliance with court orders. In
December 2024, the court found Wright in contempt and imposed a
12-month prison sentence suspended for two years. The order set the
suspension to expire on 20 December 2026, conditional on compliance,
and struck out a new claim. A suspended sentence is distinct from
immediate imprisonment. These proceedings enforced restrictions following
the rejected identity claim; they did not establish who actually created
Bitcoin.[^contempt]

On 7 March 2025, the court imposed a three-year general civil restraint
order on Wright. Its reasons, published on 12 May, explained that the
order required permission before bringing claims or applications within
its scope. This added a procedural restriction to the earlier orders;
it was not a new determination of Nakamoto's identity.[^restraint]

In April 2026, a *New York Times* investigation argued that Adam Back
could be Nakamoto. Reporting by The Block described the case as relying
on similarities in writing and earlier electronic-cash ideas; it also
reported Back's denial. Such comparisons are an argument about authorship,
not a demonstrated link between a legal identity and control of the
original project's cryptographic keys. As of 31 October 2026, this
article treats the identification as contested, rather than replacing
the pseudonym with Back's name.[^identity]

The documentary *Finding Satoshi*, released on 22 April 2026, proposed a
different hypothesis: Finney and Len Sassaman had created Bitcoin together.
The Block reported the filmmakers' case, while *WIRED* described continuing
skepticism and reported that both men's widows denied their husbands were
Nakamoto. This competing identification also remains unconfirmed.[^documentary][^skepticism]

The distinction between documented activity under the pseudonym and
claims about a particular person is central to reading this history.
Original messages establish what was published under the name, while
identity assertions require separate evidence.[^announcement][^judgment]

## Mining and attributed holdings

Claims about Nakamoto's wealth also depend on attribution. In April
2013, researcher Sergio Demian Lerner published an analysis of early
blocks using patterns in the ExtraNonce field of mining transactions.
He interpreted recurring patterns as evidence of a dominant early miner
and estimated around one million bitcoins, while explicitly acknowledging
that he could not be certain all the identified blocks belonged to
Nakamoto. This was an inference from mining behaviour, not a published
wallet balance authenticated by the creator.[^holdings]

The distinction matters when interpreting large holdings estimates.
Grouping blocks believed to share a miner and identifying that miner
as Nakamoto are separate steps. Lerner's analysis supplied a method and
assumptions for the grouping; its identity attribution remained uncertain.
His historical estimate should therefore not be read as a verified
statement of Nakamoto's present holdings, access to private keys, or
spendable wealth.[^holdings]

## Timeline

| Date | Event |
|---|---|
| 2008-08-22 | Email to Wei Dai requests a citation for b-money and links to a draft[^dai] |
| 2008-10-31 | Whitepaper announced on the cryptography mailing list[^announcement] |
| 2009-01-03 | Timestamp recorded in Bitcoin's genesis block[^genesis] |
| 2009-01-08 | v0.1 release announcement timestamped in the original archive[^release] |
| 2010-08-15 | Version 0.3.10 announced as an overflow patch for block 74,638[^overflow] |
| 2010-12-05 | Forum post cautions against WikiLeaks adoption at that stage[^wikileaks] |
| 2010-12-12 | Version 0.3.19 announcement discusses denial-of-service controls[^development] |
| 2011-04-23 | Email to Mike Hearn describes moving to other work[^hearn] |
| 2024-03-14 | High Court announces rejection of Wright's identity claim[^judgment] |
| 2024-05-20 | Detailed judgment published[^judgment] |
| 2024-12-20 | Court order records Wright's suspended prison sentence for contempt[^contempt] |
| 2025-03-07 | Court imposes a three-year general civil restraint order on Wright[^restraint] |
| 2026-04-08 | Reporting describes the Times' Back hypothesis and his denial[^identity] |
| 2026-04-22 | Finding Satoshi proposes a Finney–Sassaman collaboration[^documentary] |

## See also

- [Bitcoin](bitcoin.md)
- [Lightning Network](lightning-network.md)
- [Mt. Gox](mt-gox.md)

## References

[^announcement]: Nakamoto, S. (31 October 2008). *Bitcoin P2P e-cash paper*. Cryptography mailing-list archive. <https://www.metzdowd.com/pipermail/cryptography/2008-October/014810.html>
[^paper]: Nakamoto, S. (2008). *Bitcoin: a peer-to-peer electronic cash system*. <https://bitcoin.org/bitcoin.pdf>
[^release]: Nakamoto, S. (8 January 2009, archive timestamp). *Bitcoin v0.1 released*. <https://www.metzdowd.com/pipermail/cryptography/2009-January/014994.html>
[^genesis]: Bitcoin Core developers. *Main-network genesis block construction and parameters*, `src/kernel/chainparams.cpp`, version 29.0. <https://github.com/bitcoin/bitcoin/blob/v29.0/src/kernel/chainparams.cpp>
[^finney]: Finney, H. (19 March 2013). *Bitcoin and me*. First-person retrospective. <https://bitcointalk.org/index.php?topic=155054.msg1643985#msg1643985>
[^development]: Nakamoto, S. (12 December 2010). *Added some DoS limits, removed safe mode (0.3.19)*. <https://bitcointalk.org/index.php?topic=2228.msg29479#msg29479>
[^hearn]: Hearn, M. and Nakamoto, S. (April 2011). *Holding coins in an unspendable state for a rolling time window*. Correspondence published by Hearn. <https://plan99.net/~mike/satoshi-emails/thread5.html>
[^judgment]: High Court of England and Wales (20 May 2024). *Crypto Open Patent Alliance v Wright*, [2024] EWHC 1198 (Ch), particularly paragraphs 7 and 26–30. <https://www.judiciary.uk/wp-content/uploads/2024/05/COPA-v-Wright-Judgment.pdf>
[^identity]: The Block (8 April 2026). *NYT investigation suggests Adam Back may be Satoshi Nakamoto*. <https://www.theblock.co/news/business/2026-04-08-nyt-investigation-suggests-adam-back-may-be-satoshi-nakamoto-396663>
[^dai]: Nakamoto, S. and Dai, W. (2008–2009). *Bitcoin emails*, correspondence supplied by Dai and reproduced by Gwern. <https://gwern.net/doc/bitcoin/2008-nakamoto>
[^discussion]: Nakamoto, S. (8 November 2008, archive timestamp). *Bitcoin P2P e-cash paper*, reply to Hal Finney. <https://www.metzdowd.com/pipermail/cryptography/2008-November/014832.html>
[^malmi]: Malmi, M. *Satoshi – Sirius emails, 2009–2011*. Correspondence published by its recipient. <https://mmalmi.github.io/satoshi/>
[^overflow]: Nakamoto, S. (15 August 2010; edited 16 August). *Version 0.3.10 – block 74638 overflow PATCH!* <https://bitcointalk.org/index.php?topic=827.0>
[^wikileaks]: Nakamoto, S. (5 December 2010). *Re: Wikileaks contact info?*, post 148. <https://bitcointalk.org/index.php?topic=1735.msg26999#msg26999>
[^contempt]: High Court of England and Wales (20 December 2024). *Crypto Open Patent Alliance v Wright*, order following contempt proceedings. <https://www.judiciary.uk/judgments/crypto-open-patent-alliance-v-wright-order/>
[^holdings]: Lerner, S. D. (17 April 2013). *The Well Deserved Fortune of Satoshi Nakamoto*. Researcher's original analysis and stated uncertainty. <https://bitslog.com/2013/04/17/the-well-deserved-fortune-of-satoshi-nakamoto/>
[^restraint]: High Court of England and Wales (12 May 2025). *Crypto Open Patent Alliance v Wright*, [2025] EWHC 1139 (Ch), particularly paragraphs 1 and 5. Approved judgment, mirrored PDF. <https://websitedc.s3.amazonaws.com/documents/Crypto_Open_Patent_Alliance_v._Wright_UK_May_12_2025.pdf>
[^documentary]: Hunt, J. (22 April 2026). *New Satoshi documentary makes the case Hal Finney and Len Sassaman were Bitcoin's co-creators*. The Block. <https://www.theblock.co/news/ecosystems/2026-04-22-finding-satoshi-documentary-makes-case-hal-finney-len-sassaman-bitcoins-co-creators-398423>
[^skepticism]: Levy, S. (1 May 2026). *You Found Satoshi? Let's See the Receipts*. WIRED. <https://www.wired.com/story/you-found-satoshi-lets-see-the-receipts/>
