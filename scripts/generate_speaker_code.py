#!/usr/bin/env python3
import os
import sys

speakers = [
        { 
         'name': 'Andrei Maiboroda',
         'project': 'Ipsilon - Ethereum Foundation',
         'bio': ''
        },
        { 
         'name': 'Ansgar Dietrichs', 
         'project': 'Ethereum Foundation', 
         'bio': 'Researcher at Ethereum Foundation' 
         },
        {
            'name': 'Alex Beregszaszi',
            'project': 'Ipsilon - Ethereum Foundation',
            'bio': ''
        },
        {   'name': 'Alex Gluchowski',
            'project': 'Matter Labs',
            'bio': 'Alex Gluchowski is the Co-founder and CEO of Matter Labs, creators of zkSync.\nAs the world\'s most Ethereum-aligned Layer-2 solution, zkSync is on a mission to accelerate the mass adoption of crypto for personal sovereignty.\nAlex is a highly experienced software architect and 3x founder with 15+ years of startup and engineering experience.\nPrior to founding Matter Labs, he was the founding CTO of PaulCamper, the largest online camper-sharing platform in Europe.'
        },
        {
            'name': 'Ayman Bouchareb',
            'project': 'Nethermind',
            'bio': 'Ayman is a 24 years old software engineer from Morocco, joined Nethermind last year as part of the core team, and mostly focus on EVM related topics (since Ayman likes VMs), and now Ayman works on small EIPs that touchs the EVM for Shanghai and Cancun forks as well as working on the full EOF update for the EVM.'
        },
        {
            'name': 'Ben Livshitz',
            'project': 'Matter Labs',
            'bio': 'Ben is the VP of Research at Matter Labs and an associate professor at Imperial College London.\nBen is a computer scientist with a Ph.D. in computer science from Stanford University, with an h-index of 57 and over 10,000 citations to his papers. He is an inventor skilled at translating academic research into industrial practice, a research manager leading high-performance applied research teams, and a professor. Most of his work has direct industrial applications.\nCurrently, he serves as the VP of Research at Matter Labs. Previously, he led teams as the CEO of Zilliqa Research, a layer-1 blockchain, and as the Chief Scientist at Brave Software, leading innovative development across cryptography, machine learning, performance, security, privacy, and other domains. For many years, he worked as a researcher at Microsoft Research in Seattle.\nHe has also taught at UW, MIT, and Imperial College London. He has also filed dozens of patents based on his inventions.'
        },
        {
            'name': 'Carlos Matallana',
            'project': 'Polygon zkEVM',
            'bio': 'Protocol blockchain engineer focused on L2 solutions.\nStarted working on Iden3 and then switch to develop the PoC of a rollup back in 2019.\nThen Carlos started on Hermez network as a protocol engineer which became polygon zkEVM',
        },
        {
            'name': 'CPerezz',
            'project': 'Privacy&Scaling Explorations - Ethereum Foundation',
            'bio': 'Working at PSE for 3+years. One of the main contributors of the ZKEVM and Halo2-PSE & halo2curves mantainer (among others).\nCurrently working on folding among any other random things that pickup my interest.',
        },
        {
            'name': 'Daniel Kirchner',
            'project': 'Solidity - Ethereum Foundation',
            'bio': ''
        },
        {
            'name': 'Daniel Marzec',
            'project': 'Flashbots',
            'bio': 'SUAVE Protocol R&D'
        },
        { 
         'name': 'David Pearce', 
         'project': 'Consensys', 
         'bio': "David is a research engineer in the Trustworthy Smart Contracts Team at ConsenSys.\nDavid's current focus is on the application of formal methods to smart contracts.\nBefore that, David was an Associate Professor in the School of Engineering and Computer Science at Victoria University of Wellington, NZ.\nDavid graduated from the Department of Computing at Imperial College London, and moved to New Zealand in 2004.\nDavid's research interests are in programming languages, compilers, static analysis and formal verification.  David is the author of the Whiley programming language which (like Dafny) supports formal verification of functional specifications (i.e. preconditions / postconditions)." 
         },
        {
         'name': 'David Weisiger',
         'project': 'Taiko Labs',
         'bio': 'Head of DevRel @ Taiko Labs',
         },
        { 
         'name': 'Danno Ferrin', 
         'project': 'Hyperledger Besu', 
         'bio': 'Danno is Principal Software Engineer at Hedera Hashgraph, where he integrates the EVM into the Hedera network.\nPreviously he was Lead Protocol Engineer at ConsenSys Software Inc on their Ethereum Mainnet team, where he chose to go "full crypto" after leaving Google.\nDanno also worked at McDonalds as a crew member in his youth, so he is fully hedged against any DeFi downturn.\nDanno is a maintainer for the Hyperledger Besu project.'
         },
        {
            'name': 'Dragan Rakita',
            'project': 'Paradigm',
            'bio': 'Reth core dev, revm author.'
        },
        {
            'name': 'Eduard Sanou',
            'project': 'PSE',
            'bio': 'Learned zk in iden3 (now Polygon Hermez) while developing a decentralized identity protocol, and later a zkRollup.\nNow working on the zkEVM CE project in PSE (EF) for nearly 2 years',
        },
        {
            'name': 'Federico Kunze Küllmer',
            'project': 'Evmos',
            'bio': 'Founder of Evmos, CEO at Altiplanic. Previously IBC & Cosmos Core Engineer',
            'picture': 'federico_kunze_kullmer'
            },
        {
            'name': 'Greg Colvin',
            'project': '',
            'bio': ''
        },
        {
            'name': 'Harikrishnan Mulackal',
            'project': '',
            'bio': '',
        },
        { 
         'name': 'Jacek Glen', 
         'project': 'Gas Cost Estimator - Imapp', 
         'bio': 'Jacek have almost 20 years of experience developing and designing systems in industries spanning from banking to finance to big data to insurance.\nIn recent years, Jacek have focused on all aspects of blockchain technologies. Jacek is involved in developing Ethereum clients, smart contracts and web3 apps.'
         },
        {
            'name': 'John Toman',
            'project': 'Certora Inc.',
            'bio': 'Dr. John Toman is the VP of R&D at Certora Inc.\nHe leads the development of the Certora Prover and specializes in static analysis.\nHe received his PhD in 2019 from the University of Washington.\nDr. Toman’s research focuses on bringing the power of automated verification to real-world, industrial settings. His award-winning, impact-focused research has been published at several top conferences in the field.'
        },
        {
            'name': 'Jordi Baylina',
            'project': 'Polygon',
            'bio': ''
        }, 
        {
            'name': 'Jose Pedro Sousa',
            'project': 'Aztec Labs',
            'bio': 'A musician and teacher became Developer Relations Engineer at Aztec.\nPreviously at Polygon and Mindera, this fellow geek loves web3 and its private solutions, and is a serious candidate for "jack of all trades, master of none".',
        },
        {
            'name': 'Leo Alt',
            'project': 'powdr',
            'bio': 'Leo currently works on powdr building zkVM tooling.\nBefore that he worked on Formal Verification and Solidity at the Ethereum Foundation for many years, mostly doing research and building tools for formal verification of smart contracts and zk circuits.\nLeo also holds a PhD in Computer Science, focused on SMT solving and software verification.',
        },
        {
            'name': 'Lightclient',
            'project': 'Geth - Ethereum Foundation',
            'bio': ''
        },
        {
            'name': 'Mamy André-Ratsimbazafy',
            'project': 'Taiko',
            'bio': 'Mamy has been an Ethereum core dev for 5 years, developing the Nimbus consensus client. After the success of The Merge, he now focuses on scaling Ethereum, by leading the ZK engineering team at Taiko.',
            'picture': 'mamy_andre_ratsimbazafy'
        },
        {
            'name': 'Marius van der Wijden',
            'project': 'Geth - Ethereum Foundation',
            'bio': 'Marius is a developer at the Ethereum Foundation as a member of the Geth client team.'
        },
        {
            'name': 'Morgan Weaver',
            'project': 'OpenZeppelin',
            'bio': 'Morgan came to Web3 in early 2022, from the fields of deep learning, DevOps, and distributed systems within the Web2 landscape.\nThroughout this transition, Morgan has enjoyed building knowledge in Solidity, smart contract auditing, and systems-level Web3 security.\nWhile their work at OpenZeppelin has heavily focused on onchain monitoring and automation as well as proof of concept work, it has also included contributions to security standards with the Ethereum Enterprise Alliance, and participation in many hackathons, communities and events.\nMorgan lives and works in Lisbon, and intends to help Web3 make a positive disruption is the existing social, financial, and operational structures of Web2.',
        },
        {
            'name': 'Neville Grech',
            'project': 'Dedaub',
            'bio': "Neville is the Director and co-founder of <a href=\"https://dedaub.com\">Dedaub</a>. Neville expertise is focused on program analysis, mostly applied to security applications.\nBefore Dedaub Neville had a mostly academic career.  Have authored the first work that applies static analysis to the security of smart contracts, this work was subsequently <a href=\"https://www.sigplan.org/Highlights/Papers/\"> highlighted by ACM SIGPLAN </a> and <a href=\"https://cacm.acm.org/magazines/2020/10/247600-madmax/fulltext\"> Communications of the ACM</a>.\nThroughout Naville's career also developed novel techniques and tools in the areas of energy efficient software development, smart contracts, semantics and generative programming.\nSome popular tools Naville have codeveloped include decompilers and security analyzers for the Ethereum platform (MadMax and Gigahorse) and Java pointer and taint analysis frameworks (Doop, P/Taint and HeapDL).\nPreviously, Naville was Reach High Fellow at the University of Athens, a Senior Research Associate at the University of Bristol, and have worked in industry as a Data Scientist and Software Engineer.\nNaville hold a PhD from the University of Southampton."
        },
        {
            'name': 'Niklas Kunkel',
            'project': 'Chronicle Labs - Chronicle Protocol - MakerDAO',
            'bio': 'Founder of Chronicle Labs, the developers of Chronicle Protocol.\nNik began his crypto journey at IBM Research, where he worked on the Hyperledger blockchain and early supply chain finance applications.\nIn 2017 he joined MakerDAO to create Dai, the first decentralized stablecoin on Ethereum.\nNik is responsible for creating DSProxy. An industry-standard account abstraction primitive, OasisDEX, the first decentralized exchange on Ethereum with an order matching engine, as well as Chronicle Oracle Protocol, which secures over $10B of assets locked in MakerDAO.',
        },
        {
            'name': 'Orest Tarasiuk',
            'project': 'Scroll',
            'bio': 'Old-school computer scientist and founder-CTO. Now working on scaling blockchains using ZK.',
        },
        {
            'name': 'Paweł Bylica',
            'project': 'Ipsilon - Ethereum Foundation',
            'bio': '',
            'picture': 'pawel_bylica'
        },
        {
            'name': 'Radosław Zagórowicz',
            'project': 'Ipsilon - Ethereum Foundation',
            'bio': '',
            'picture': 'radoslaw_zagorowicz'
        },
        {
            'name': 'Rami Khalil',
            'project': 'Zeth (RISC Zero)',
            'bio': ''
        },
        {
            'name': 'Raul Jordan',
            'project': 'Offchain Labs',
            'bio': 'Raul Jordan is a senior software engineer at Offchain Labs and a maintainer of the Prysm Ethereum consensus client.\nHes an avid fan of programming languages and onboarding a lot more developers outside of blockchain into the exciting world of Ethereum technology.'
        },
        {
            'name': 'Remco',
            'project': 'Nomic Foundation',
            'bio': 'Remco is the tech lead on Nomic Foundation\'s EDR team, where he works on the open-source building blocks that empower developers to create new dev tools for the Ethereum ecosystem.',
        },
        {
            'name': 'Raoul Schaffranek',
            'project': 'Runtime Verification',
            'bio': 'Raoul Schaffranek studied Computer Science at RWTH Aachen University, Germany, where he obtained B.Sc. and M.Sc. degrees.\nHe wrote his master thesis about compositional modeling and fully automated verification of distributed systems and formalized his findings with the Isabelle proof assistant.\nBefore joining RV, Raoul worked for more than eight years as a software engineer for the German software company graphodata AG.\nRaoul considers programming a human-centric rather than machine-centric activity, and he firmly believes that we should build modern programming languages and verification tools upon this perspective.',
        },
        {
            'name': 'Simi Vera',
            'project': 'OpenZeppelin',
            'bio': 'Smriti has been working at OpenZeppelin as a Blockchain Security Engineer, since 2020.\nPrior to transition into web3 security, she was working as a blockchain solutions engineer. She comes from a software development background, and has a masters in Data Analytics.',
        },
        {
            'name': 'Tim Beiko',
            'project': 'Ethereum Foundation',
            'bio': 'Tim runs the AllCoreDevs call for Ethereum'
        },
        {
            'name': 'Ujval Misra',
            'project': 'UC Berkeley; Specular',
            'bio': 'Ujval is a CS PhD student at UC Berkeley, advised by Dawn Song.\nHis research interests broadly lie in security and privacy—particularly in the context of decentralized trust.\nHis recent focus has been on decentralization problems in Ethereum-based L2 systems.',
        },
        {
            'name': 'Ulaş Erdoğan',
            'project': 'Clave',
            'bio': 'Ulaş is a Blockchain developer based in Istanbul. Currently a member of the Clave team which is building an AA-based wallet solution utilizing secure elements for signature abstraction in the mobile devices. Ulaş  is also Head of Development in the Ethylene Studio and ex-president of ITU Blockchain, which is the first and biggest university blockchain society in Turkey.',
            'picture': 'ulas_erdogan',
        },
        ]



if __name__ == "__main__":
    SPACING = " " * 15

    original_file = "./index.html"
    if not os.path.exists(original_file):
        original_file="../index.html"
        if not os.path.exists(original_file):
            print(f"ERROR: index.html not found")
            exit(1)

    original_content = open(original_file, "r").read()
    original_content_begin = original_content.split(f"{SPACING}<!-- SPEAKERS_START -->\n")[0]
    original_content_end = original_content.split(f"{SPACING}<!-- SPEAKERS_END -->\n")[1]

    i = 0
    debug=False
    generated_code = ""

    if len(sys.argv) == 2 and sys.argv[1] == "debug":
        debug=True

    generated_code+=f"{SPACING}<!-- SPEAKERS_START -->\n"

    for s in speakers:
        i += 1

        name_id = s['name'].lower().replace(' ', '_')
        if 'picture' in s.keys():
            name_id = s['picture']
        image_path = f"../images/speakers/{name_id}.jpg"
        if not os.path.exists(f"../images/speakers/{name_id}.jpg"):
            name_id = "default"
            if debug:
                print(f"{image_path} not found")
        bio = s['bio'].replace('\n', '</p><p>')

        if debug:
            print(f"{s['name']}")
            print(f"{image_path}")
            print(f"{name_id}")

        generated_code += f"""{SPACING}<section id="speaker_{i}">
    {SPACING}<img class="circular-square" src="images/speakers/{name_id}.jpg" alt="{s['name']}"/>
    {SPACING}<h3>{s['name']}</h3>
    {SPACING}<h4>{s['project']}</h4>
    """

        if bio != "":
            generated_code += f"""
    {SPACING}<ul class="actions">
    {SPACING}    <li><a id="show_bio_{i}" onclick="showBio({i})" href="#speaker_{i}" class="button scrolly">Read Bio</a></li>
    {SPACING}</ul>
    {SPACING}<div id="bio_{i}" class="hidden">
    {SPACING}    <p>{bio}</p>
    {SPACING}    <ul class="actions">
    {SPACING}        <li><a id="hide_bio_{i}" onclick="hideBio({i})" href="#speaker_{i}" class="button scrolly">Hide Bio</a></li>
    {SPACING}    </ul>
    {SPACING}  </div>
    """

        generated_code += f"""
    {SPACING}</section>\n"""

    if i % 2 == 1:
        generated_code += f"{SPACING}<section></section>\n"

    generated_code+= f"{SPACING}<!-- SPEAKERS_END -->\n"

    new_content = f"{original_content_begin}{generated_code}{original_content_end}"

    new_content_file = open(original_file, "w")
    new_content_file.write(new_content)
    new_content_file.close()
