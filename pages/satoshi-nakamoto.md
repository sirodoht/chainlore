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

## Software and correspondence

The original mailing-list archive dates the v0.1 release announcement to
8 January 2009 at 14:27 EST. The message supplied a download link, described
the release as Windows-only at that stage, and said open-source C++ code
was included. This is the timestamp of that particular announcement;
accounts using other archives or release events may give different dates.[^release]

Nakamoto also discussed development with early contributors. In an April
2011 email exchange preserved by recipient Mike Hearn, Nakamoto explained
how pre-signed transactions and a timelock could structure a contract,
then encouraged Hearn's Java implementation of Bitcoin. In the message
dated 23 April, Nakamoto said they had moved to other work and expressed
confidence in Gavin and the other developers.[^hearn]

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
| 2009-01-08 | v0.1 release announcement timestamped in the original archive[^release] |
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
[^hearn]: Hearn, M. and Nakamoto, S. (April 2011). *Holding coins in an unspendable state for a rolling time window*. Correspondence published by Hearn. <https://plan99.net/~mike/satoshi-emails/thread5.html>
[^judgment]: High Court of England and Wales (20 May 2024). *Crypto Open Patent Alliance v Wright*, [2024] EWHC 1198 (Ch), particularly paragraphs 7 and 26–30. <https://www.judiciary.uk/wp-content/uploads/2024/05/COPA-v-Wright-Judgment.pdf>
[^identity]: Fortune (8 April 2026). *Satoshi identity reporting*. <https://fortune.com/2026/04/08/who-is-the-real-inventor-of-bitcoin-satoshi-nakamoto/>
