---
title: Elliptic curve cryptography
ticker: None
category: Concept
status: draft
updated: 2026-10-31
written_by: claude-haiku-5-5 (high effort)
---

Elliptic curve cryptography (ECC) refers to cryptographic schemes built on the arithmetic of points on elliptic curves over finite fields.[^6][^1] This is an unverified draft, not fact-checked. It covers the cryptographic uses of elliptic curves and is based only on the sources listed in the References section.

| Property | Detail |
|---|---|
| Name | Elliptic curve cryptography (ECC) |
| Ticker | None |
| Basic object | Curve y² ≡ x³ + ax + b (mod p) over a prime field Fp[^1] |
| Standards body | SECG (Standards for Efficient Cryptography Group); SEC 2 v2.0 dated 27 January 2010[^1] |
| Example curve | secp256k1, used by Bitcoin[^1][^2] |
| Bitcoin signatures | Traditionally ECDSA over secp256k1 with SHA-256 hashes; BIP-340 proposes 64-byte Schnorr signatures over the same curve[^2] |
| BIP-340 | Assigned 2020-01-19; status recorded as “Deployed”[^2] |
| Notable controversy | Dual_EC_DRBG, a random bit generator; NIST removed it from draft guidance in 2014[^3][^4] |

## History

Elliptic curve cryptographic schemes were proposed independently in 1985 by Neal Koblitz and Victor Miller, according to a reference-work entry seen in search results but not opened for this draft.[^6]

According to Matthew Green, NIST and NSA released a pseudorandom number generator based on elliptic curve cryptography in 2005–2006.[^5] Scientific American states that NIST published the standard in 2006 and that the International Organization for Standardization later adopted it.[^4]

Green says that shortly afterwards, Shumow and Ferguson pointed out that the algorithm might contain an NSA backdoor, and that in 2007 two Microsoft researchers argued that its weaknesses could combine to open a backdoor.[^5] Scientific American reports that the Microsoft engineers stopped short of accusing NIST or the NSA of inserting it intentionally.[^4]

SEC 2 version 2.0 was published by Certicom Research and dated 27 January 2010.[^1]

## Technology

SEC 2 defines elliptic curve domain parameters over a prime field Fp as a sextuple T = (p, a, b, G, n, h). These consist of a prime p defining the field, coefficients a and b, a base point G, the prime order n of G, and the cofactor h = #E(Fp)/n.[^1]

SEC 2 states that for parameters where log₂ p = 2t, the curve gives about t bits of security, because solving the logarithm problem on the curve is believed to take about 2^t operations.[^1]

SEC 2 recommends curves over Fp at 192, 224, 256, 384 and 521 bits. It describes Koblitz curves and “verifiably random” curves. SECG states that no trapdoors can have been placed in the verifiably random parameters during their generation; this is SECG's own claim, and this draft did not independently check it.[^1]

SEC 2 specifies secp256k1 as a Koblitz curve with a = 0 and b = 7, a 256-bit prime field, and cofactor h = 1. It lists a strength of 128 bits, comparable to a 3072-bit RSA/DSA modulus.[^1]

BIP-340 states that Bitcoin has traditionally authenticated transactions with ECDSA signatures over secp256k1 using SHA-256 hashes. It proposes 64-byte Schnorr signatures over the same curve and lists provable security among its motivations for Schnorr over ECDSA.[^2]

## Governance

SEC 2 is published by Certicom Research, with copyright held by Certicom Corp. The document permits copying provided it is identified as SEC 2.[^1]

SEC 2 states that the next scheduled review would take place in February 2015. This draft could not confirm whether that review happened.[^1]

SEC 2 notes that compliance with the document may require use of an invention covered by patent rights.[^1]

BIP-340 lists Pieter Wuille, Jonas Nick and Tim Ruffing as authors and is licensed under BSD-2-Clause. Its header links a bitcoin-dev discussion dated 2018-07-06.[^2]

NIST removed Dual_EC_DRBG from its revised draft, SP 800-90A Rev. 1, and recommended that current users move to one of the three remaining approved algorithms.[^3]

## Incidents and controversies

Dual_EC_DRBG (Dual Elliptic Curve Deterministic Random Bit Generator) was one of four deterministic random bit generators in NIST's SP 800-90 standard.[^4] Green says it is up to a thousand times slower than its symmetric-key alternatives, while noting that slowness is not necessarily one of its flaws.[^5]

In May 2006, researchers at Eindhoven University of Technology reported that the algorithm was insecure and that an attack against it was easy to launch on “an ordinary PC”.[^4]

In September 2013, news reports based on documents leaked by Edward Snowden prompted public concern about the algorithm. Those reports said it was vulnerable to tampering that could allow a backdoor. This is a reported allegation, not a finding by NIST, and this draft does not establish whether such a backdoor was inserted.[^4]

NIST said it “would not deliberately weaken a cryptographic standard”. Scientific American notes that NIST stood by that statement after an editor's note.[^4]

After the 2013 reports, NIST immediately recommended against using the algorithm and reissued SP 800-90A for public comment.[^3] On 19 September 2013, RSA advised developers not to use the default Dual_EC_DRBG generator in its BSAFE product.[^5]

Bruce Schneier, quoted by Scientific American, said that Microsoft, Cisco, Symantec and RSA included the algorithm in their cryptographic libraries primarily because they need it to be eligible for government contracts.[^4]

Paul Kocher, quoted by Scientific American, said that “there's really nothing that impacts the fundamental mathematics underpinning encryption here”.[^4]

## Timeline

| Date | Event |
|---|---|
| 1985 | Koblitz and Miller are credited with independently proposing elliptic curve cryptographic schemes.[^6] |
| 2006 | NIST publishes the standard that includes Dual_EC_DRBG; Green gives the release period as 2005–2006.[^4][^5] |
| 2006-05 | Eindhoven researchers report that the algorithm is insecure.[^4] |
| 2007 | Microsoft engineers flag a possible backdoor without accusing NIST or the NSA.[^4] |
| 2010-01-27 | SEC 2 version 2.0 is dated.[^1] |
| 2013-09 | NIST recommends against Dual_EC_DRBG and reissues SP 800-90A for comment.[^3] |
| 2013-09-19 | RSA warns developers not to use the default Dual_EC_DRBG generator in BSAFE.[^5] |
| 2014-04-21 | NIST removes Dual_EC_DRBG from its revised draft guidance.[^3] |
| 2015-02 | SEC 2's next scheduled review is due; this draft could not confirm it occurred.[^1] |
| 2018-07-06 | A bitcoin-dev discussion is linked from the BIP-340 header.[^2] |
| 2020-01-19 | BIP-340 is assigned; its status is recorded as Deployed.[^2] |

## References

[^1]: [SEC 2: Recommended Elliptic Curve Domain Parameters](https://www.secg.org/sec2-v2.pdf)

[^2]: [bips/bip-0340.mediawiki at master · bitcoin/bips](https://github.com/bitcoin/bips/blob/master/bip-0340.mediawiki)

[^3]: [NIST Removes Cryptography Algorithm from Random Number Generator Recommendations](https://www.nist.gov/news-events/news/2014/04/nist-removes-cryptography-algorithm-random-number-generator-recommendations)

[^4]: [NSA Efforts to Evade Encryption Technology Damaged U.S. Cryptography Standard](https://www.scientificamerican.com/article/nsa-nist-encryption-scandal/)

[^5]: [The Many Flaws of Dual_EC_DRBG](https://blog.cryptographyengineering.com/2013/09/18/the-many-flaws-of-dualecdrbg/)

[^6]: [Elliptic Curve Cryptography](https://link.springer.com/rwe/10.1007/978-3-642-27739-9_245-2)
