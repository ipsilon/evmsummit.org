#!/usr/bin/env python3
import os

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
        {
            'name': 'Ayman Bouchareb',
            'project': 'Nethermind',
            'bio': 'Ayman is a 24yo software engineer from Morocco, joined Nethermind last year as part of the core team, and mostly focus on EVM related topics (since Ayman likes VMs), and now Ayman works on small EIPs that touchs the EVM for Shanghai and Cancun forks as well as working on the full EOF update for the EVM.'
        },
        { 
         'name': 'David Pearce', 
         'project': 'Consensys', 
         'bio': "David is a research engineer in the Trustworthy Smart Contracts Team at ConsenSys.\nDavid's current focus is on the application of formal methods to smart contracts.\nBefore that, David was an Associate Professor in the School of Engineering and Computer Science at Victoria University of Wellington, NZ.\nDavid graduated from the Department of Computing at Imperial College London, and moved to New Zealand in 2004.\nDavid's research interests are in programming languages, compilers, static analysis and formal verification.  David is the author of the Whiley programming language which (like Dafny) supports formal verification of functional specifications (i.e. preconditions / postconditions)." 
         },
        {
            'name': 'Daniel Kirchner',
            'project': 'Solidity',
            'bio': ''
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
            'name': 'Greg Colvin',
            'project': '',
            'bio': ''
        },
        { 
         'name': 'Jacek Glen', 
         'project': 'Gas Cost Estimator - Imapp', 
         'bio': 'Jacek have almost 20 years of experience developing and designing systems in industries spanning from banking to finance to big data to insurance.\nIn recent years, Jacek have focused on all aspects of blockchain technologies. Jacek is involved in developing Ethereum clients, smart contracts and web3 apps.'
         },
        {
            'name': 'Jordi Baylina',
            'project': 'Polygon',
            'bio': ''
        }, 
        {
            'name': 'Lightclient',
            'project': 'Geth',
            'bio': ''
        },
        {
            'name': 'Mamy André-Ratsimbazafy',
            'project': 'Taiko',
            'bio': '',
            'picture': 'mamy_andre_ratsimbazafy'
        },
        {
            'name': 'Marius van der Wijden',
            'project': 'Geth - Ethereum Foundation',
            'bio': 'Marius is a developer at the Ethereum Foundation as a member of the Geth client team.'
        },
        {
            'name': 'Neville Grech',
            'project': 'Dedaub',
            'bio': "Neville is the Director and co-founder of <a href=\"https://dedaub.com\">Dedaub</a>. Neville expertise is focused on program analysis, mostly applied to security applications.\nBefore Dedaub Neville had a mostly academic career.  Have authored the first work that applies static analysis to the security of smart contracts, this work was subsequently <a href=\"https://www.sigplan.org/Highlights/Papers/\"> highlighted by ACM SIGPLAN </a> and <a href=\"https://cacm.acm.org/magazines/2020/10/247600-madmax/fulltext\"> Communications of the ACM</a>.\nThroughout Naville's career also developed novel techniques and tools in the areas of energy efficient software development, smart contracts, semantics and generative programming.\nSome popular tools Naville have codeveloped include decompilers and security analyzers for the Ethereum platform (MadMax and Gigahorse) and Java pointer and taint analysis frameworks (Doop, P/Taint and HeapDL).\nPreviously, Naville was Reach High Fellow at the University of Athens, a Senior Research Associate at the University of Bristol, and have worked in industry as a Data Scientist and Software Engineer.\nNaville hold a PhD from the University of Southampton."
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
            'name': 'Tim Beiko',
            'project': 'Ethereum Foundation',
            'bio': 'Tim runs the AllCoreDevs call for Ethereum'
        },
        ]


i = 0
code = ""
spacing = " " * 15
for s in speakers:
    i += 1

    print("<!--")
    name_id = s['name'].lower().replace(' ', '_')
    print(name_id)
    if 'picture' in s.keys():
        name_id = s['picture']
    print(name_id)
    image_path = f"../images/speakers/{name_id}.jpg"
    print(image_path)
    if not os.path.exists(f"../images/speakers/{name_id}.jpg"):
        name_id = "default"
    print(name_id)
    print("-->")
    bio = s['bio'].replace('\n', '</p><p>')

    code += f"""{spacing}<section id="speaker_{i}">
{spacing}<img class="circular-square" src="images/speakers/{name_id}.jpg" alt="{s['name']}"/>
{spacing}<h3>{s['name']}</h3>
{spacing}<h4>{s['project']}</h4>"""

    if bio != "":
        code += f"""
{spacing}<ul class="actions">
{spacing}    <li><a id="show_bio_{i}" onclick="showBio({i})" href="#speaker_{i}" class="button scrolly">Read Bio</a></li>
{spacing}</ul>
{spacing}<div id="bio_{i}" class="hidden">
{spacing}    <p>{bio}</p>
{spacing}    <ul class="actions">
{spacing}        <li><a id="hide_bio_{i}" onclick="hideBio({i})" href="#speaker_{i}" class="button scrolly">Hide Bio</a></li>
{spacing}    </ul>
{spacing}  </div>
"""

    code += f"""
{spacing}</section>\n"""

if i % 2 == 1:
    code += f"{spacing}<section></section>"

print(code)
