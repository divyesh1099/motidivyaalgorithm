# motidivyaalgorithm
This is a quantum safe algorithm.

## Research and References
  1. [Quantum-Safe Cryptography (QSC)](https://www.etsi.org/technologies/quantum-safe-cryptography?jjj=1684295678409)
   - Popular cryptographic schemes based on these hard problems – including RSA and Elliptic Curve Cryptography – will be easily broken by a quantum computer.
   - Without quantum-safe cryptography and security, all information that is transmitted on public channels now – or in the future – is vulnerable to eavesdropping. Even encrypted data that is safe against current adversaries can be stored for later decryption once a practical quantum computer becomes available.
   2. [What Is Quantum-Safe Cryptography, and Why Do We Need It?](https://www.ibm.com/cloud/blog/what-is-quantum-safe-cryptography-and-why-do-we-need-it)
   - Two of the main types of cryptographic algorithms in use today for the protection of data work in different ways:

   - Symmetric algorithms use the same secret key to encrypt and decrypt data.
   - Asymmetric algorithms, also known as public key algorithms, use two keys that are mathematically related: a public key and a private key.
   - The National Institute of Standards and Technology (NIST) initiated a Post-Quantum Cryptography Standardization Program to identify new algorithms that can resist threats posed by quantum computers.

   - After three rounds of evaluation, NIST has identified seven finalists. They plan to select a small number of new quantum-safe algorithms early this year and have new quantum-safe standards in place by 2024. As part of this program, IBM researchers have been involved in the development of three quantum-safe cryptographic algorithms based on lattice cryptography that are in the final round of consideration: CRYSTALS-Kyber, CRYSTALS-Dilithium and Falcon.
   - When meeting with clients getting started on their journey to quantum safety, we share a few of the key milestones to help them get ready to adopt new quantum-safe standards:

   - Discover and classify data: The first step involves classifying the value of your data and understanding compliance requirements. This helps you create a data inventory.
   - Create a crypto inventory: Once you have classified your data, you will need to identify how your data is encrypted, as well as other uses of cryptography to create a crypto inventory that will help you during your migration planning. Your crypto inventory will include information like encryption protocols, symmetric and asymmetric algorithms, key lengths, crypto providers, etc. 
   - Embrace crypto agility: The transition to quantum-safe standards will be a multi-year journey as standards evolve and vendors move to adopt quantum-safe technology. Use a flexible approach and be prepared to make replacements. Implement a hybrid approach as recommended by industry experts by using both classical and quantum-safe cryptographic algorithms. This maintains compliance with current standards while adding quantum-safe protection.
   ![IBM Steps Towards Quantum Safety](./Research%20Assets/IBMMilestonesTowardsQuantumCryptography.png)
   3. [Post Quantum Cryptography Selected Algorithm NIST](https://csrc.nist.gov/projects/post-quantum-cryptography/selected-algorithms-2022)
   