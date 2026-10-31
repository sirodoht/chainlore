---
title: Smart contract
ticker: None
category: Infrastructure
written_by: GPT-6-Astra high
status: ai-fact-checked
checked: 2026-10-31
checked_by: GPT-6-Astra high
updated: 2026-10-31
---

# Smart contract

A smart contract is a program deployed on a blockchain. On
[Ethereum](ethereum.md), it has an address, executable code, and persistent
state. Transactions can invoke its functions, and contracts can call other
contracts. Network nodes execute these operations according to the same
rules.[^intro]

| | |
|---|---|
| Type | Blockchain program |
| Ethereum execution environment | Ethereum Virtual Machine |
| Common Ethereum languages | Solidity, Vyper[^intro] |
| Example interface | ERC-20 for fungible tokens[^erc20] |
| Example upgrade mechanism | Delegating proxy[^proxy] |

## Execution

Ethereum contracts are compiled into code that its virtual machine can
execute. Deploying a contract is a transaction and consumes gas, as does
executing operations through transactions. Contracts can enforce conditions
before allowing an operation and combine calls to other programs into an
application.[^intro]

ERC-20 illustrates how standard interfaces support this composition. A
token contract exposes operations for reading balances, transferring tokens,
and granting spending allowances. Applications can integrate that interface
without requiring each issuer to invent different transaction methods.
The standard specifies an interface, not a guarantee about the token's
value or its issuer.[^erc20]

## Permissions and upgrades

An Ethereum contract account is controlled by its code. Its rules may
authorise particular accounts to perform privileged operations; being
deployed on a public chain does not itself make every operation open to
everyone.[^accounts][^intro]

Ethereum also allows externally owned accounts to delegate to contract code
under EIP-7702. The delegated code executes in the account's context, so its
permissions and implementation affect the account's security.[^delegation]

A proxy delegates execution to an implementation contract while retaining
its own storage. An upgrade changes which implementation it uses. ERC-1967
standardises storage locations for the implementation, beacon, and
administrator, helping tools identify these relationships. An upgradeable
application therefore needs scrutiny of both its current code and the
authority able to replace that code.[^proxy]

## Limitations and failures

Solidity's security documentation identifies reentrancy as a risk when a
contract gives control to another contract before completing its own state
changes. It also warns that information marked `private` in Solidity is
not secret from observers of the blockchain. Compiler and platform bugs
remain possible even when application code appears correct.[^security]

External events require an [oracle](blockchain-oracle.md) to supply data
that the contract can read. Agreement about execution does not establish
that the supplied information accurately represents the outside world.[^oracles]

## Timeline

| Date | Event |
|---|---|
| 2015-07-30 | Ethereum's Frontier network launches[^frontier] |
| 2015-11-19 | ERC-20 proposed[^erc20] |
| 2019-04-24 | ERC-1967 proxy storage proposal created[^proxy] |

## See also

- [Non-fungible token](nft.md)
- [Cryptocurrency wallet](cryptocurrency-wallet.md)
- [Uniswap](uniswap.md)
- [Aave](aave.md)
- [The DAO](the-dao.md)
- [Safe](safe.md)
- [Account abstraction](account-abstraction.md)

## References

[^intro]: ethereum.org. *Introduction to smart contracts*. <https://ethereum.org/en/developers/docs/smart-contracts/>
[^erc20]: Vogelsteller, F. and Buterin, V. (2015). *ERC-20: Token Standard*. <https://eips.ethereum.org/EIPS/eip-20>
[^accounts]: ethereum.org. *Ethereum accounts*. <https://ethereum.org/en/developers/docs/accounts/>
[^proxy]: Palladino, S., Giordano, F. and Croubois, H. (2019). *ERC-1967: Proxy Storage Slots*. <https://eips.ethereum.org/EIPS/eip-1967>
[^security]: Solidity documentation. *Security considerations*. <https://docs.soliditylang.org/en/latest/security-considerations.html>
[^oracles]: ethereum.org. *Oracles*. <https://ethereum.org/en/developers/docs/oracles/>
[^frontier]: Ethereum Foundation (30 July 2015). *Ethereum launches*. <https://blog.ethereum.org/2015/07/30/ethereum-launches>
[^delegation]: Ethereum Improvement Proposals. *EIP-7702: Set Code for EOAs*. <https://eips.ethereum.org/EIPS/eip-7702>
