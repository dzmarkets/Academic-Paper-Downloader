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
| 51 | Lippincott Williams & Wilkins (LWW) | `10.1097` | `Verified` | Verified fallback to LWW / Unpaywall |
| 52 | Walter De Gruyter GMBH | `10.1515` | `Implemented` | Heuristics implemented |
| 53 | World Scientific Publishing | `10.1142` | `Implemented` | Heuristics implemented |
| 54 | Brill | `10.1163` | `Verified` | Verified fallback to Brill / Unpaywall |
| 55 | Mary Ann Liebert | `10.1089` | `Implemented` | Heuristics implemented |
| 56 | Georg Thieme Verlag (Thieme) | `10.1055` | `Implemented` | Heuristics implemented |
| 57 | Bentham Science Publishers | `10.2174` | `Verified` | Verified fallback to Bentham / Unpaywall |
| 58 | Duke University Press | `10.1215` | `Verified` | Verified fallback to Duke UP / Unpaywall |
| 59 | Cell Press | `10.1016/j.cell` | `Verified` | Verified fallback (under Elsevier `10.1016`) |
| 60 | Educational Publishing Foundation (APA) | `10.1037` (EPF subset) | `Verified` | Verified fallback (under APA `10.1037`) |
| 61 | Association for Computing Machinery (ACM) | `10.1145` | `Implemented` | Heuristics implemented |
| 62 | IOS Press | `10.3233` | `Verified` | Verified fallback to IOS Press / Unpaywall |
| 63 | Wolters Kluwer Medknow | `10.4103` | `Verified` | Verified fallback to Medknow / Unpaywall |
| 64 | John Benjamins Publishing | `10.1075` | `Verified` | Verified fallback to Benjamins / Unpaywall |
| 65 | Sciendo | `10.2478` | `Verified` | Verified fallback to Sciendo / Unpaywall |
| 66 | CSIRO Publishing | `10.1071` | `Implemented` | Heuristics implemented |
| 67 | Palgrave Macmillan | `10.1057` | `Implemented` | Heuristics implemented (via Springer) |
| 68 | European Mathematical Society (EMS) | `10.4171` | `Verified` | Verified fallback to EMS / Unpaywall |
| 69 | KeAi Publishing | `10.1016/j.jia` (KeAi subset) | `Verified` | Verified fallback (under Elsevier `10.1016`) |
| 70 | Canadian Science Publishing | `10.1139` | `Verified` | Verified fallback to CSP / Unpaywall |
| 71 | University of Toronto Press | `10.3138` | `Verified` | Verified fallback to UTP / Unpaywall |
| 72 | Science Press (China) | `10.1360` (Science Press subset) | `Verified` | Verified fallback to Science Press / Unpaywall |
| 73 | EDP Sciences | `10.1051` | `Verified` | Verified fallback to EDP / Unpaywall |
| 74 | Human Kinetics | `10.1123` | `Verified` | Verified fallback to Human Kinetics / Unpaywall |
| 75 | Inderscience Enterprises | `10.1504` | `Verified` | Verified fallback to Inderscience / Unpaywall |
| 76 | AIP Publishing | `10.1063` | `Verified` | Verified fallback to AIP / Unpaywall |
| 77 | American Physiological Society | `10.1152` | `Implemented` | Heuristics implemented |
| 78 | University of California Press | `10.1525` | `Verified` | Verified fallback to UC Press / Unpaywall |
| 79 | AME Publishing Company | `10.21037` | `Verified` | Verified fallback to AME / Unpaywall |
| 80 | Slack Inc. | `10.3928` | `Verified` | Verified fallback to Slack / Unpaywall |
| 81 | Adis International | `10.2165` | `Implemented` | Heuristics implemented (via Springer) |
| 82 | University of Illinois Press | `10.5406` | `Verified` | Verified fallback to UIP / Unpaywall |
| 83 | American Geophysical Union (AGU) | `10.1029` (AGU subset) | `Verified` | Verified fallback (under Wiley `10.1002`) |
| 84 | Peeters Publishers | `10.2143` | `Verified` | Verified fallback to Peeters / Unpaywall |
| 85 | Akademiai Kiado | `10.1556` | `Verified` | Verified fallback to Akademiai / Unpaywall |
| 86 | University of Pennsylvania Press | `10.1353` (Penn subset) | `Verified` | Verified fallback (under Muse `10.1353`) |
| 87 | Tech Science Press | `10.32604` | `Verified` | Verified fallback to Tech Science / Unpaywall |
| 88 | Hogrefe Publishing | `10.1026` or `10.1027` | `Verified` | Verified fallback to Hogrefe / Unpaywall |
| 89 | Liverpool University Press | `10.3828` | `Verified` | Verified fallback to LUP / Unpaywall |
| 90 | Penn State University Press | `10.5325` | `Verified` | Verified fallback to PSUP / Unpaywall |
| 91 | IWA Publishing | `10.2166` | `Verified` | Verified fallback to IWA / Unpaywall |
| 92 | American Society for Microbiology (ASM) | `10.1128` | `Implemented` | Heuristics implemented |
| 93 | Begell House | `10.1615` | `Verified` | Verified fallback to Begell / Unpaywall |
| 94 | Pensoft Publishers | `10.3897` | `Verified` | Verified fallback to Pensoft / Unpaywall |
| 95 | American Association for Cancer Research (AACR) | `10.1158` | `Verified` | Verified fallback to AACR / Unpaywall |
| 96 | Copernicus Publications | `10.5194` | `Verified` | Verified fallback to Copernicus / Unpaywall |
| 97 | Edinburgh University Press | `10.3366` | `Implemented` | Heuristics implemented |
| 98 | Edizioni Minerva Medica | `10.23736` | `Verified` | Verified fallback to Minerva Medica / Unpaywall |
| 99 | American Psychological Association (APA) | `10.1037` | `Verified` | Verified fallback to APA / Unpaywall |
| 100 | American Meteorological Society (AMS) | `10.1175` | `Verified` | Verified fallback to AMS / Unpaywall |

