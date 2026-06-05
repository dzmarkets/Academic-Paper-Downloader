# Journal Integration Tracking List

Use this list to track the status of integrated direct resolvers and prevent loops or duplicate work.

| # | Journal / Publisher | Match Rule (DOI Prefix / Text) | Status | Notes |
|---|---------------------|-------------------------------|--------|-------|
| 1 | Springer Open | `10.1007` or `10.1186` | `Implemented` | Heuristics implemented |
| 2 | Elsevier (ScienceDirect) | `10.1016` | `Verified` | Verified fallback to Crossref/Unpaywall |
| 3 | Wiley | `10.1002` or `10.1111` | `Implemented` | Heuristics implemented |
| 4 | PLOS ONE | `10.1371` | `Verified` | Direct resolver verified by unit test |
| 5 | IEEE Xplore (OA) | `10.1109` | `Verified` | Verified fallback to Unpaywall |
| 6 | Nature | `10.1038` | `Implemented` | Heuristics implemented |
| 7 | Science (AAAS) | `10.1126` | `Implemented` | Heuristics implemented |
| 8 | MDPI | `10.3390` | `Implemented` | Heuristics implemented |
| 9 | Frontiers | `10.3389` | `Verified` | Direct resolver verified by unit test |
| 10 | BioMed Central (BMC) | `10.1186` (BMC subset) | `Implemented` | Heuristics implemented |
| 11 | Oxford Academic (OUP) | `10.1093` | `Implemented` | Heuristics implemented |
| 12 | Cambridge Core (CUP) | `10.1017` | `Verified` | Verified fallback to Unpaywall |
| 13 | Sage | `10.1177` | `Implemented` | Heuristics implemented |
| 14 | Taylor & Francis | `10.1080` | `Verified` | Verified fallback to T&F API / Unpaywall |
| 15 | IOP Science | `10.1088` | `Implemented` | Heuristics implemented |
| 16 | Zenodo (CERN) | `10.5281` | `Verified` | Verified fallback to Zenodo API |
| 17 | arXiv | `10.48550` or `arxiv` | `Verified` | Verified fallback to arXiv direct |
| 18 | AAS (American Astronomical Soc) | `10.3847` | `Implemented` | Heuristics implemented |
| 19 | RSC (Royal Soc Chemistry) | `10.1039` | `Verified` | Verified fallback to Unpaywall |
| 20 | ACS (American Chemical Soc) | `10.1021` | `Implemented` | Heuristics implemented |
| 21 | Scientific Reports | `scientific reports` | `Implemented` | Nature heuristics implemented |
| 22 | Nature Communications | `nature communications` | `Implemented` | Nature heuristics implemented |
| 23 | MDPI Sensors | `sensors` | `Implemented` | MDPI heuristics implemented |
| 24 | MDPI Cells | `cells` | `Implemented` | MDPI heuristics implemented |
| 25 | Frontiers in Immunology | `frontiers in immunology` | `Verified` | Frontiers direct resolver verified by unit test |
| 26 | Annual Reviews | `10.1146` | `Implemented` | Heuristics implemented |
| 27 | American Physical Society (APS) | `10.1103` | `Implemented` | Heuristics implemented |
| 28 | University of Chicago Press | `10.1086` | `Implemented` | Heuristics implemented |
| 29 | Royal Society | `10.1098` | `Implemented` | Heuristics implemented |
| 30 | ASCE | `10.1061` | `Implemented` | Heuristics implemented |
| 31 | Emerald | `10.1108` | `Implemented` | Heuristics implemented |
| 32 | SIAM | `10.1137` | `Implemented` | Heuristics implemented |
| 33 | Pleiades Publishing | `10.1134` (Pleiades subset) | `Implemented` | Heuristics implemented (via Springer) |
| 34 | MDPI Animals | `animals` | `Verified` | Verified fallback (under MDPI `10.3390`) |
| 35 | MDPI Sustainability | `sustainability` | `Verified` | Verified fallback (under MDPI `10.3390`) |
| 36 | MDPI Energies | `energies` | `Verified` | Verified fallback (under MDPI `10.3390`) |
| 37 | Frontiers in Psychology | `frontiers in psychology` | `Verified` | Verified fallback (under Frontiers `10.3389`) |
| 38 | Frontiers in Oncology | `frontiers in oncology` | `Verified` | Verified fallback (under Frontiers `10.3389`) |
| 39 | Nature Genetics | `nature genetics` | `Implemented` | Heuristics implemented (under Nature `10.1038`) |
| 40 | Nature Medicine | `nature medicine` | `Implemented` | Heuristics implemented (under Nature `10.1038`) |
| 41 | Nature Biotechnology | `nature biotechnology` | `Implemented` | Heuristics implemented (under Nature `10.1038`) |
| 42 | PLOS Pathogens | `10.1371/journal.ppat` | `Verified` | Verified fallback (under PLOS `10.1371`) |
| 43 | PLOS Computational Biology | `10.1371/journal.pcbi` | `Verified` | Verified fallback (under PLOS `10.1371`) |
| 44 | Johns Hopkins University Press | `10.1353` | `Verified` | Verified fallback to Muse / Unpaywall |
| 45 | MIT Press | `10.1162` | `Verified` | Verified fallback to MIT Press / Unpaywall |
| 46 | Karger | `10.1159` | `Verified` | Verified fallback to Karger / Unpaywall |
| 47 | SPIE | `10.1117` | `Verified` | Verified fallback to SPIE / Unpaywall |
| 48 | BMJ | `10.1136` | `Verified` | Verified fallback to BMJ / Unpaywall |
| 49 | ASME | `10.1115` | `Verified` | Verified fallback to ASME / Unpaywall |
| 50 | JAMA (AMA) | `10.1001` | `Verified` | Verified fallback to JAMA / Unpaywall |

