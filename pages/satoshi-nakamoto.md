---
title: Satoshi Nakamoto
ticker: None
category: Person
written_by: Unknown
status: draft
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

Bitcoin's genesis block carries a timestamp of 3 January 2009. Its
transaction embeds the text "The Times 03/Jan/2009 Chancellor on brink of
second bailout for banks." Bitcoin Core's source preserves both that
message and the block's identifying parameters. The code also records
that the genesis transaction's 50-bitcoin output cannot be spent, a
special property of the initial block.[^genesis]

The original mailing-list archive dates the v0.1 release announcement to
8 January 2009 at 14:27 EST. The message supplied a download link, described
the release as Windows-only at that stage, and said open-source C++ code
was included. This is the timestamp of that particular announcement;
accounts using other archives or release events may give different dates.[^release]

Nakamoto warned that the software was experimental and that a restart
could become necessary. The announcement invited users to keep nodes
available for incoming connections and explained how to generate coins
on an ordinary PC. It described the initial mining difficulty as
deliberately low, with competition expected to raise it through automatic
adjustments. Participation initially meant helping operate and test a
small network.[^release]

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

In April 2026, a New York Times investigation named Adam Back as Nakamoto;
Back denied it.[^identity]

The distinction between documented activity under the pseudonym and
claims about a particular person is central to reading this history.
Original messages establish what was published under the name, while
identity assertions require separate evidence.[^announcement][^judgment]

## Timeline

| Date | Event |
|---|---|
| 2008-10-31 | Whitepaper announced on the cryptography mailing list[^announcement] |
| 2009-01-03 | Timestamp recorded in Bitcoin's genesis block[^genesis] |
| 2009-01-08 | v0.1 release announcement timestamped in the original archive[^release] |
| 2010-12-12 | Version 0.3.19 announcement discusses denial-of-service controls[^development] |
| 2011-04-23 | Email to Mike Hearn describes moving to other work[^hearn] |
| 2024-03-14 | High Court announces rejection of Wright's identity claim[^judgment] |
| 2024-05-20 | Detailed judgment published[^judgment] |

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
[^identity]: Fortune (8 April 2026). *Satoshi identity reporting*. <https://fortune.com/2026/04/08/who-is-the-real-inventor-of-bitcoin-satoshi-nakamoto/>
