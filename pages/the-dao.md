---
title: The DAO
ticker: DAO
category: History
written_by: GPT-6-Astra high
status: draft
updated: 2026-10-31
---

# The DAO

The DAO was an Ethereum-based investment organisation launched in 2016.
Participants exchanged ether for DAO tokens and could vote on proposals
to fund projects. An exploit in June 2016 led to an Ethereum hard fork
that moved affected funds into a recovery contract.[^report][^attack][^fork]

| | |
|---|---|
| Network | [Ethereum](ethereum.md) |
| Token | DAO |
| Offering | 30 April–28 May 2016 |
| Raised | Approximately 12 million ETH |
| Exploit | 17 June 2016 |
| Recovery fork | 20 July 2016, block 1,920,000 |
| SEC investigation report | 25 July 2017 |

## Design and fundraising

According to the SEC's investigation, The DAO sold approximately
1.15 billion tokens for around 12 million ETH during its offering,
valued at roughly $150 million at the time. The organisation was intended
to finance projects and distribute potential returns to participants;
its token was more than a receipt for an ordinary software purchase.[^report]

The design combined token voting with human gatekeeping. Curators
screened and whitelisted proposals before holders could vote on them.
The SEC later emphasised the role of Slock.it, its co-founders, and the
curators in establishing and managing the undertaking. Token voting did
not eliminate dependence on those actors.[^report]

## The exploit

On 17 June 2016, the Ethereum Foundation reported an attack on The DAO's
split function. The attacker used recursive calls to obtain ether
repeatedly within a transaction and move it into a child DAO. This was a
contract-level vulnerability: executing the contract's code as written
did not make the code's financial behaviour safe.[^attack]

The child DAO's waiting period prevented immediate withdrawal of the
diverted ether. The Foundation's initial response discussed a proposed
soft fork to restrict movements of affected funds while further options
were considered. That proposal was an intermediate response, distinct
from the hard fork ultimately carried out in July.[^attack][^fork]

## The fork and Ethereum Classic

On 20 July, Ethereum block 1,920,000 implemented an exceptional state
change. The Foundation reported that about 12 million ETH from affected
DAO contracts, including funds held by protective white-hat operations,
was transferred into a withdrawal contract. This recovery total should
not be confused with the amount originally diverted by the attacker.[^fork]

Participants who rejected the intervention continued the chain without
the recovery change, which became Ethereum Classic. Ethereum's own
history records the disagreement as being about intervening after an
application failure, rather than fixing a defect in the underlying
protocol.[^history]

The fork announcement also warned participants following the non-fork
chain about replay attacks. A split ledger can create operational issues
in addition to a disagreement over governance: a signed transaction may
need protection against unintended use on another branch.[^fork]

## Securities-law significance

The SEC's July 2017 report concluded that the DAO tokens were securities
under US law. The agency explained that the economic realities of an
offering matter regardless of its terminology or technology. Its
announcement said it had decided not to bring charges in this instance,
instead publishing its findings to caution market participants.[^release]

## See also

- [Ethereum](ethereum.md)
- [Smart contract](smart-contract.md)
- [Vitalik Buterin](vitalik-buterin.md)

## References

[^report]: SEC (2017-07-25). *Report of Investigation Pursuant to Section 21(a) of the Securities Exchange Act of 1934: The DAO*, Release No. 81207. <https://www.sec.gov/litigation/investreport/34-81207.pdf>
[^attack]: Buterin, V. (2016-06-17). *CRITICAL UPDATE Re: DAO Vulnerability*. Ethereum Foundation. <https://blog.ethereum.org/2016/06/17/critical-update-re-dao-vulnerability>
[^fork]: Buterin, V. (2016-07-20). *Hard Fork Completed*. Ethereum Foundation. <https://blog.ethereum.org/2016/07/20/hard-fork-completed>
[^history]: ethereum.org. *Timeline of all Ethereum forks*, DAO fork. <https://ethereum.org/en/history/>
[^release]: SEC (2017-07-25). *SEC Issues Investigative Report Concluding DAO Tokens, a Digital Asset, Were Securities*. <https://www.sec.gov/newsroom/press-releases/2017-131>
