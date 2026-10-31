---
title: Zero-knowledge proof
ticker: None
category: Infrastructure
written_by: GPT-6-Astra high
status: ai-fact-checked
checked_by: GPT-6-Astra high
checked: 2026-10-31
updated: 2026-10-31
---

# Zero-knowledge proof

A zero-knowledge proof lets a prover demonstrate a statement's validity
without revealing the secret information used to establish it. That
secret information is often called a witness. Blockchain applications
use these techniques both to protect information and to verify
computations efficiently; these are related but distinct objectives.[^overview][^groth]

| | |
|---|---|
| Participants | Prover and verifier |
| Hidden input | Witness |
| Core properties | Completeness, soundness, zero knowledge |
| Example constructions | Groth16 and ZK-STARKs |
| Blockchain uses | Privacy and verification of computation |

## What the proof establishes

Completeness means that an honest prover with a valid witness can
convince an honest verifier. Soundness limits a dishonest prover's
ability to convince the verifier of a false statement. Zero knowledge
means the verifier learns no additional secret information from the
proof beyond what the statement itself reveals. Real constructions
specify security assumptions and error probabilities rather than
promising unconditional security in every setting.[^overview]

The statement and the witness must be distinguished. Demonstrating
membership in an eligible set need not disclose which member the prover
is. However, whatever the application publishes separately remains
public; a proof cannot erase information already exposed by the
surrounding system.[^overview][^rollups]

## Succinct proofs and setup

Jens Groth's 2016 paper introduced a pairing-based construction commonly
called Groth16. It proves satisfaction of an arithmetic circuit using
a proof of three group elements and a small verification calculation.
The paper's construction is zero knowledge: the verifier can check the
claim without learning the witness. This illustrates how a proof can
be much smaller than the computation whose correctness it
establishes.[^groth][^implementation]

Setup assumptions differ between systems. The 2018 ZK-STARK paper by
Eli Ben-Sasson, Iddo Bentov, Yinon Horesh, and Michael Riabzev describes
a transparent construction that does not require a trusted party to
create secret setup information. Its demonstration proves a claim
about a database without revealing the underlying private records.
Transparency concerns setup trust; it does not mean disclosing the
private witness.[^stark]

## Rollups and privacy

A validity-proof rollup executes transactions outside Ethereum and
submits a proof that a proposed state update follows its rules. Ethereum
can verify that proof without repeating every individual execution.
This is a scaling use of cryptographic proofs.[^rollups]

The label “ZK-rollup” does not by itself promise confidential
transactions. Ethereum's documentation explains that rollups publish
enough data for others to reconstruct their state, whether as compressed
transactions or state differences. A system can use succinct validity
proofs while keeping its transaction history public. Assessing privacy
therefore requires examining the complete application and its published
data, not only the proof system's name.[^rollups]

## See also

- [Rollup](rollup.md)
- [Ethereum](ethereum.md)
- [Smart contract](smart-contract.md)
- [Tornado Cash](tornado-cash.md)

## References

[^overview]: Ethereum documentation. *Zero-knowledge proofs*. <https://ethereum.org/zero-knowledge-proofs/>
[^groth]: Groth, J. (2016). *On the Size of Pairing-based Non-interactive Arguments*. Cryptology ePrint Archive, 2016/260. <https://eprint.iacr.org/2016/260>
[^stark]: Ben-Sasson, E., Bentov, I., Horesh, Y., and Riabzev, M. (2018). *Scalable, transparent, and post-quantum secure computational integrity*. Cryptology ePrint Archive, 2018/046. <https://eprint.iacr.org/2018/046>
[^rollups]: Ethereum documentation. *Zero-knowledge rollups*. <https://ethereum.org/developers/docs/scaling/zk-rollups/>
[^implementation]: Arkworks contributors. *ark-groth16 0.6.0 source: lib.rs*. <https://docs.rs/ark-groth16/0.6.0/src/ark_groth16/lib.rs.html>
