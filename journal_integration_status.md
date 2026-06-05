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


| 101 | Human Biology / WAYNE STATE UNIV PRESS | 0018-7143 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 102 | Tien Tzu Hsueh Pao/Acta Electronica Sinica Chinese Institute Of Electronics / Unknown Publisher | 0372-2112 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 103 | Revista Brasileira De Ginecologia E Obstetricia Federacao Brasileira Das Sociedades De Ginecologia E  Obstetricia / Unknown Publisher | 0100-7203 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 104 | Revue D'Elevage Et De Medecine Veterinaire Des Pays Tropicaux  (France) Cirad / Unknown Publisher | 0035-1865 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 105 | Izvestiya Vysshikh Uchebnykh Zavedeniy. Prikladnaya  Nelineynaya Dinamika Saratov State University / Unknown Publisher | 0869-6632 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 106 | Guerres Mondiales Et Conflits  Contemporains / PRESSES UNIV FRANCE | 0984-2292 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 107 | Journal Of The Korean Association Of Oral And Maxillofacial Surgeons / Unknown Publisher | 1225-1585 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 108 | Journal Of The Korean Association Of Oral And Maxillofacial  Surgeons Korean Association Of Oral And Maxillofacial Surgeons / Unknown Publisher | 2234-5930 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 109 | Women Informa Uk Ltd / Unknown Publisher | 0957-4042 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 110 | Journal Of Web Engineering / RIVER PUBLISHERS | 1540-9589 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 111 | Journal Of The Torrey Botanical  Society / TORREY BOTANICAL SOC | 1095-5674 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 112 | Revista Brasileira De Linguistica Aplicada Universidade De Minas Gerais / Unknown Publisher | 1676-0786 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 113 | Journal Of Pathology And Translational Medicine Korean Society Of Pathologists / Unknown Publisher | 2383-7837 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 114 | Diyala Journal Of Engineering Sciences University Of Diyala / Unknown Publisher | 1999-8716 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 115 | Slavia Orientalis Panstwowe Wydawnictwo Naukowe / Unknown Publisher | 0037-6744 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 116 | Cuadernos De Turismo Escuela Universitaria De Turismo, Universidad De Murcia / Unknown Publisher | 1139-7861 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 117 | International Journal Of Stem  Cells / KOREAN SOC STEM CELL RESEARCH | 2005-3606 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 118 | Annali Italiani Di Chirurgia / EDIZIONI LUIGI POZZI | 0003-469X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 119 | Suomen Antropologi Finnish Anthropological Society / Unknown Publisher | 0355-3930 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 120 | Revista Oficial Del Poder Judicial Poder Judicial Del Peru / Unknown Publisher | 1997-6682 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 121 | Problemy Analiza Petrozavodsk State University / Unknown Publisher | 2306-3424 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 122 | Journal Of Electronics, Electromedical Engineering, And Medical  Informatics  Jurusan Teknik Elektromedik, Politeknik Kesehatan Kemenkes  Surabaya, Indonesia / Unknown Publisher | 2656-8632 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 123 | Corpus Pragmatics / Unknown Publisher | 2509-9507 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 124 | Conservacion Colombiana Fundacion Proaves Carrera / N°   ISSN   E-ISSN | 1900-1592 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 125 | East African Journal Of Neurological Sciences East African Association Of Neurological Surgeons / N°   ISSN   E-ISSN | 2957-4315 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 126 | Policy And Practice Centre For Global Education / Unknown Publisher | 1748-135X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 127 | Vasomed Wpv Wirtschafts- Und Praxisverlag Gmbh / Unknown Publisher | 0942-1181 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 128 | Minimax Theory And Its Applications Heldermann Verlag / Unknown Publisher | 2199-1421 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 129 | International Journal Of Marketing Semiotics And Discourse  Studies University Of Kassel / Unknown Publisher | 2195-2280 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 130 | International Journal Of Oral  And Maxillofacial Surgery / CHURCHILL LIVINGSTONE | 0901-5027 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 131 | Journal Of Manufacturing  Science And Engineering- Transactions Of The Asme / ASME | 1087-1357 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 132 | Journal Of Radiological  Protection / IOP PUBLISHING LTD | 0952-4746 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 133 | Konstruktion Vdi Fachmedien Gmbbh & Co. / Unknown Publisher | 0720-5953 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 134 | Konstruktion / Unknown Publisher | 1436-4921 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 135 | Biological Research / SOC BIOLGIA CHILE | 0716-9760 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 136 | Studia Iuridica Lublinensia Wydawnictwo Uniwersytetu Marii Curie-Sklodowskiej W  Lublinie / Unknown Publisher | 1731-6375 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 137 | Revista Espanola De Patologia Ediciones Doyma, S.L. / Unknown Publisher | 1699-8855 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 138 | Journal Of Microwave Power And Electromagnetic Energy / Unknown Publisher | 2472-4041 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 139 | Berliner Und Munchener  Tierarztliche Wochenschrift / SCHLUETERSCHE  VERLAGSGESELLSCHAFT MBH & CO  KG | 0005-9366 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 140 | Palabra Clave Universidad De La Sabana / Unknown Publisher | 0122-8285 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 141 | Palabra Clave / Unknown Publisher | 2027-534X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 142 | Drvna Industrija / ZAGREB UNIV, FAC FORESTRY | 0012-6772 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 143 | Current Cardiovascular Imaging Reports Current Medicine Group / Unknown Publisher | 1941-9066 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 144 | South African Journal Of Childhood Education Openjournals Publishing Aosis (Pty) Ltd / Unknown Publisher | 2223-7674 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 145 | Hepatoma Research Oae Publishing Inc. / N°   ISSN   E-ISSN | 2394-5079 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 146 | Bar - Brazilian Administration Review Anpad - Associacao Nacional De Pos-Graduacao E Pesquisa  Em Administracao / Unknown Publisher | 1807-7692 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 147 | International Journal For Computational Civil And Structural  Engineering Asv Publishing House / Unknown Publisher | 2587-9618 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 148 | Russian Journal Of Woman And Child Health Meditsina-Inform Llc / Unknown Publisher | 2618-8430 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 149 | Antropologicheskij Forum Peter The Great Museum Of Anthropology And Ethnography  (Kunstkamera), Russian Academy Of Sciences / Unknown Publisher | 1815-8870 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 150 | Journal Of Magazine Media University Of Nebraska Press / Unknown Publisher | 2576-7887 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 151 | Journal Of Contemporary East Asia Studies Routledge / Unknown Publisher | 2476-1028 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 152 | Note Di Matematica Pitagora Editrice / Unknown Publisher | 1123-2536 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 153 | The Journal Of The Japanese Forestry Society Nihon Ringakkai / N°   ISSN   E-ISSN | 0021-485X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 154 | Acta Linguistica Lithuanica Institute Of The Lithuanian Language / Unknown Publisher | 1648-4444 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 155 | Islas Central University Marta Abreu De Las Villas / N°   ISSN   E-ISSN | 0047-1542 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 156 | Revista Clinica Espanola / EDICIONES DOYMA S A | 0014-2565 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 157 | Semergen Ediciones Doyma, S.L. / Unknown Publisher | 1138-3593 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 158 | Medicina De Familia Semergen / Unknown Publisher | 1696-9073 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 159 | Nano-Micro Letters / SHANGHAI JIAO TONG UNIV PRESS | 2150-5551 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 160 | Journal Of Integrative  Neuroscience / IMR PRESS | 0219-6352 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 161 | Vestnik Khirurgii Imeni I.I.Grekova Aesculapius / Unknown Publisher | 0042-4625 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 162 | Grekov S Bulletin Of Surgery / Unknown Publisher | 2686-7370 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 163 | Zanco Journal Of Pure And Applied Sciences Salahaddin University - Erbil / Unknown Publisher | 2218-0230 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 164 | European Journal Of Psychotherapy And Counselling Routledge / Unknown Publisher | 1364-2537 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 165 | Gazeta De Antropologia Univesidad De Granada / Unknown Publisher | 0214-7564 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 166 | Iranian Rehabilitation Journal University Of Social Welfare And Rehabilitation Sciences / N°   ISSN   E-ISSN | 1735-3602 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 167 | Actas Espanolas De Psiquiatria / JUAN JOSE LOPEZ-IBOR  FOUNDATION | 1139-9287 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 168 | Journal Of Information And Communication Technology Universiti Utara Malaysia Press / Unknown Publisher | 1675-414X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 169 | Russian Journal Of Theriology / KMK SCIENTIFIC PRESS LTD,  MOSCOW STATE UNIV | 1682-3559 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 170 | Acta Silvatica Et Lignaria Hungarica University Of West Hungary Press / Unknown Publisher | 1786-691X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 171 | Bulletin Of Kamchatka Regional Association Educational- Scientific Center. Earth Sciences Institute Of Volcanology And Seismology Feb Ras / Unknown Publisher | 1816-5524 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 172 | Exploratory Animal And Medical Research West Bengal Veterinary Alumni Association / Unknown Publisher | 2277-470X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 173 | Denver Law Review / UNIV DENVER, STURM COLLEGE  LAW | 2469-6463 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 174 | Denver Law Review University Of Denver Sturm College Of Law / Unknown Publisher | 2469-6471 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 175 | Journal Of Global Faultlines Pluto Journals / Unknown Publisher | 2054-2089 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 176 | Magyar Onkológia / Unknown Publisher | 2060-0399 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 177 | Asean Journal Of Science And Engineering Universitas Pendidikan Indonesia / Unknown Publisher | 2776-5938 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 178 | Intrecci D'Arte University Of Bologna / Unknown Publisher | 2240-7251 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 179 | Epidemiologie, Mikrobiologie, Imunologie Czech Medical Association J.E. Purkyne / Unknown Publisher | 1805-451X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 180 | Journal Of Applied And Computational Mechanics Shahid Chamran University Of Ahvaz / Unknown Publisher | 2383-4536 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 181 | Southwestern Entomologist / SOUTHWESTERN ENTOMOLOGICAL  SOC | 0147-1724 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 182 | Acta Physica Polonica B, Proceedings Supplement Jagellonian University / Unknown Publisher | 1899-2358 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 183 | Acta Physica Polonica B Proceedings Supplement / Unknown Publisher | 2082-7865 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 184 | Aquatic Mammals / EUROPEAN ASSOC AQUATIC  MAMMALS | 0167-5427 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 185 | Journal Of Distribution Science Kodisa Foundation / Unknown Publisher | 1738-3110 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 186 | International Review Of Victimology / Unknown Publisher | 2047-9433 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 187 | Vegueta University Of Las Palmas De Gran Canaria, Faculty Of  Geography And History / Unknown Publisher | 1133-598X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 188 | Moving Image / UNIV MINNESOTA PRESS | 1532-3978 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 189 | African Journal Of Laboratory Medicine Aosis (Pty) Ltd / Unknown Publisher | 2225-2002 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 190 | Historical Reflections-Reflexions  Historiques / BERGHAHN JOURNALS | 0315-7997 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 191 | Singapore Academy Of Law Journal Academy Publishing / N°   ISSN   E-ISSN | 0218-2009 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 192 | Zeitschrift Fur Dialektologie Und  Linguistik / FRANZ STEINER VERLAG GMBH | 0044-1449 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 193 | Squalen Bulletin Of Marine And Fisheries Postharvest And  Biotechnology  Research And Development Center For Marine And Fisheries  Product Processing And Biotechnology / Unknown Publisher | 2089-5690 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 194 | Revue D'Assyriologie Et D'Archeologie Orientale Presses Universitaires De France / Unknown Publisher | 0373-6032 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 195 | Revue D Assyriologie Et D Archéologie Orientale / Unknown Publisher | 2104-3817 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 196 | Media E Jornalismo Instituto De Comunicacao Da Nova / Unknown Publisher | 1645-5681 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 197 | Mythlore The Mythopoeic Society / Unknown Publisher | 0146-9339 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 198 | Nordic Journal Of Educational History University Of Umea / Unknown Publisher | 2001-7766 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 199 | Revista Iberoamericana De Psicologia Y Salud Ediciones Doyma, S.L. / Unknown Publisher | 1989-9246 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 200 | Journal Of The Textile Association Textile Association (India) / Unknown Publisher | 0368-4636 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 201 | Journal Of The Textile Association / Unknown Publisher | 2347-2537 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 202 | Spool Tu Delft Open / Unknown Publisher | 2215-0897 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 203 | Contemporary Southeast Asia / INST SOUTHEAST ASIAN STUDIES- ISEAS | 1793-284X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 204 | Agbioforum University Of Missouri / Unknown Publisher | 1522-936X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 205 | Series: International Journal Of Tv Serial Narratives University Of Bologna / Unknown Publisher | 2421-454X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 206 | Dance Magazine / DANCE MAGAZINE INC | 0011-6009 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 207 | Revista Aequitas Asociacion Veritas-Estudios Sobre Historia, Derecho E  Instituciones / Unknown Publisher | 2174-9493 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 208 | Esarda Bulletin Publications Office Of The European Union / Unknown Publisher | 1977-5296 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 209 | Mycosystema Science China Press / Unknown Publisher | 1672-6472 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 210 | Pasiphae Fabrizio Serra Editore / Unknown Publisher | 1974-0565 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 211 | Journal Of Biological Chemistry American Society For Biochemistry And Molecular Biology Inc. / Unknown Publisher | 0021-9258 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 212 | Journal Of Biological Chemistry / Unknown Publisher | 1067-8816 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 213 | Jixie Gongcheng Xuebao/Chinese Journal Of Mechanical  Engineering Editorial Office Of Chinese Journal Of Mechanical Engineering / Unknown Publisher | 0577-6686 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 214 | Japanese Journal Of Neurosurgery Japanese Congress Of Neurological Surgeons / Unknown Publisher | 0917-950X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 215 | Japanese Journal Of Neurosurgery / Unknown Publisher | 2187-3100 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 216 | Journal Of The Korean Wood Science And Technology Korean Society Of Wood Science Technology / Unknown Publisher | 1017-0715 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 217 | Japanese Journal Of Allergology Japanese Society Of Allergology / Unknown Publisher | 0021-4884 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 218 | Paediatria Croatica Children'S University Hospital Zagreb / Unknown Publisher | 1330-1403 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 219 | Journal Of Micro- Nanopatterning Materials And  Metrology-Jm3 / SPIE-SOC PHOTO-OPTICAL  INSTRUMENTATION ENGINEERS | 1932-5150 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 220 | Geosciences Journal / GEOLOGICAL SOCIETY KOREA | 1226-4806 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 221 | Arquivos Brasileiros De Cirurgia Digestiva : Abcd = Brazilian  Archives Of Digestive Surgery Colegio Brasileiro De Cirurgia Digestiva / Unknown Publisher | 0102-6720 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 222 | Teaching Artist Journal Routledge / Unknown Publisher | 1541-1796 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 223 | Slavica Slovaca Jan Stanislav Institute Of Slavistics, Slovak Committee Of  Slavists / Unknown Publisher | 0037-6787 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 224 | International Journal Of Nanoelectronics And Materials Universiti Malaysia Perlis / Unknown Publisher | 1985-5761 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 225 | Zeitschrift Fur Historische  Forschung / DUNCKER AND HUMBLOT GMBH | 0340-0174 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 226 | World Journal Of Entrepreneurship, Management And  Sustainable Development World Association For Sustainable Development / Unknown Publisher | 2042-5961 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 227 | Prace Filologiczne. Literaturoznawstwo University Of Warsaw / Unknown Publisher | 2084-6045 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 228 | Journal Of Asean Studies Bina Nusantara University / Unknown Publisher | 2338-1353 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 229 | Custos E Agronegocio On Line / UNIV FED RURAL PERNAMBUCO,  DEPT ADMINISTRACAO | 1808-2882 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 230 | Innovation Journal Innovation Journal / Unknown Publisher | 1715-3816 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 231 | Revisiones En Cancer Aran Ediciones S.A. / Unknown Publisher | 0213-8573 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 232 | Revisiones En Cáncer / Unknown Publisher | 2952-3206 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 233 | Electronic Journal Of Business Research Methods Academic Conferences And Publishing International Limited / Unknown Publisher | 1477-7029 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 234 | Cahiers De Civilisation Medievale / CENTRE ETUD SUPERIEUR CIV MED | 0007-9731 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 235 | Harvard Journal Of Asiatic  Studies / HARVARD-YENCHING INST | 0073-0548 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 236 | Journal Of World History / UNIV HAWAII PRESS | 1045-6007 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 237 | Iconos Flacso Ecuador / Unknown Publisher | 1390-1249 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 238 | Íconos - Revista De Ciencias Sociales / Unknown Publisher | 2224-6983 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 239 | Ingeniare Universidad De Tarapaca / Unknown Publisher | 0718-3291 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 240 | Womans Art Journal / OLD CITY PUBLISHING INC | 0270-7993 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 241 | Iranian Journal Of Applied Animal Science Islamic Azad University / Unknown Publisher | 2251-628X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 242 | Japanese Journal Of Chemotherapy Japanese Society Of Chemotherapy / Unknown Publisher | 1340-7007 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 243 | Vestnik Urologii/Urology Herald Rostovskii Gosudarstvennyi Meditsinskii Universitet / N°   ISSN   E-ISSN | 2308-6424 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 244 | Condensed Matter And Interphases Voronezh State University / Unknown Publisher | 1606-867X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 245 | Shengwu Gongcheng Xuebao/Chinese Journal Of Biotechnology Chinese Academy Of Sciences / Unknown Publisher | 1000-3061 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 246 | Contratexto Universidad De Lima / Unknown Publisher | 1025-9945 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 247 | Economia Agro-Alimentare Francoangeli / Unknown Publisher | 1126-1668 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 248 | Projeto Historia Pontifícia Universidade Católica De São Paulo / Unknown Publisher | 0102-4442 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 249 | Proceedings Of The National Academy Of Sciences Of Belarus,  Medical Series  Republican Unitary Enterprise Publishing House “Belorusskaja  Nauka” / Unknown Publisher | 1814-6023 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 250 | International Journal Of E-Services And Mobile Applications Igi Global Publishing / Unknown Publisher | 1941-627X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 251 | Ilahiyat Studies Bursa Ilahiyat Foundation / Unknown Publisher | 1309-1719 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 252 | International Journal Of Mathematics And Physics Al-Farabi Kazakh State National University / Unknown Publisher | 2218-7987 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 253 | Global Privacy Law Review Wolters Kluwer / Unknown Publisher | 2666-3570 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 254 | Dileme: Razprave O Vprasanjih Sodobne Slovenske Zgodovine Study Centre For National Reconciliation (Scnr) / Unknown Publisher | 2591-1201 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 255 | Federal Register Office Of The Federal Register / Unknown Publisher | 0097-6326 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 256 | Bmj Bmj Publishing Group / Unknown Publisher | 0959-8146 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 257 | Pide Working Papers Pakistan Institute Of Development Economics / Unknown Publisher | 0078-8228 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 258 | Brewingscience Fachverlag Hans Carl / Unknown Publisher | 1613-2041 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 259 | Technai Fabrizio Serra Editore / Unknown Publisher | 2037-7967 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 260 | Agricultural Biotechnology Journal Shahid Bahonar University Of Kerman / Unknown Publisher | 2228-6500 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 261 | Applied Engineering In  Agriculture / AMER SOC AGRICULTURAL &  BIOLOGICAL ENGINEERS | 0883-8542 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 262 | Research In African Literatures / INDIANA UNIV PRESS | 0034-5210 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 263 | International Journal Of Cosmetic Science / Unknown Publisher | 1467-2494 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 264 | Gastrointestinal Endoscopy Clinics Of North America W.B. Saunders / Unknown Publisher | 1052-5157 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 265 | Netherlands Heart Journal / BOHN STAFLEU VAN LOGHUM BV | 1568-5888 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 266 | Korean Journal Of Physiology &  Pharmacology / KOREAN JOURNAL OF PHYSIOLOGY  & PHARMACOLOGY | 1226-4512 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 267 | Genij Ortopedii Russian Ilizarov Scientific Center For Restorative Traumatology  And Orthopaedics / Unknown Publisher | 1028-4427 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 268 | International Review Of Research  In Open And Distributed Learning / ATHABASCA UNIV PRESS | 1492-3831 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 269 | Journal Of Medical Biochemistry / SOC MEDICAL BIOCHEMISTS SERBIA | 1452-8258 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 270 | International Journal Of  Offshore And Polar Engineering / INT SOC OFFSHORE POLAR  ENGINEERS | 1053-5381 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 271 | Ilha Do Desterro Universidade Federal De Santa Catarina / Unknown Publisher | 0101-4846 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 272 | Tropical Animal Science Journal Bogor Agricultural University / Unknown Publisher | 2615-787X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 273 | Egyptian Journal Of Community Medicine Egyptian Community Medicine Association / Unknown Publisher | 1110-1865 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 274 | Tromboz, Gemostaz I Reologiya Hemostasis And Rheology Llc / Unknown Publisher | 2078-1008 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 275 | Journal Of Engineering, Project, And Production Management Engineering Project And Production Management / Unknown Publisher | 2221-6529 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 276 | Theoretical And Practical Research In The Economic Fields Asers Publishing House / Unknown Publisher | 2068-7710 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 277 | Russian Military Medical Academy Reports Eco-Vector Llc / Unknown Publisher | 2713-2315 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 278 | Journal Of Settlements And Spatial Planning Centre For Research On Settlements And Urbanism, Faculty Of  Geography, Babes-Bolyai University / Unknown Publisher | 2069-3419 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 279 | Journal Of Electronic Commerce  Research / CALIFORNIA STATE UNIV | 1526-6133 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 280 | Sae International Journal Of Electrified Vehicles Sae International / Unknown Publisher | 2691-3747 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 281 | Quaestio Facti University Of Girona / Unknown Publisher | 2604-6202 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 282 | Politica Y Gobierno / CENTRO DE INVESTIGACION Y  DOCENCIA ECONOMICAS | 1665-2037 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 283 | Journal For The Liberal Arts And Sciences School Of Education,Oakland City University / Unknown Publisher | 2167-3756 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 284 | Plos Neglected Tropical Diseases Public Library Of Science / Unknown Publisher | 1935-2727 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 285 | Plos Neglected Tropical Diseases / PUBLIC LIBRARY SCIENCE | 1935-2735 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 286 | Journal Of Physical Education And Sport Editura Universitatii Din Pitesti / Unknown Publisher | 2247-8051 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 287 | Journal Of The American Animal  Hospital Association / AMER ANIMAL HOSPITAL ASSOC | 0587-2871 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 288 | Saeculum / BOEHLAU VERLAG GMBH & CIE | 0080-5319 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 289 | Kufa Journal Of Engineering University Of Kufa / Unknown Publisher | 2071-5528 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 290 | European Journal Of Physiotherapy Informa Healthcare / Unknown Publisher | 2167-9169 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 291 | Psicoperspectivas Individuo Y Sociedad / Unknown Publisher | 0717-7798 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 292 | Psicoperspectivas Pontificia Universidad Catolica De Valparaiso / Unknown Publisher | 0718-6924 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 293 | Journal Of Ship Production And  Design / SOC NAVAL ARCHITECTS & MARINE  ENGINEERS | 2158-2866 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 294 | Creativity Studies Vilnius Gediminas Technical University / Unknown Publisher | 2345-0479 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 295 | International Journal Of Medical Toxicology And Forensic  Medicine Shahid Beheshti University Of Medical Sciences / Unknown Publisher | 2251-8762 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 296 | Studia Aurea Universitat Autonoma De Barcelona / Unknown Publisher | 1988-1088 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 297 | Journal Of Fungal Research Editorial Department Of Journal Of Fungal Research / Unknown Publisher | 1672-3538 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 298 | Journal Of Burma Studies Center For Burma Studies At Northern Illinois University / Unknown Publisher | 1094-799X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 299 | Geofizika / UNIV ZAGREB , ANDRIJA  MOHOROVICIC GEOPHYS INST | 0352-3659 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 300 | Magnetic Resonance Letters Keai Communications Co. / Unknown Publisher | 2097-0048 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 301 | Convergencias: Revista De Investigacao E Ensino Das Artes Polytechnic Institute Of Castelo Branco Higher School Of  Applied Arts / Unknown Publisher | 1646-9054 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 302 | Asia-Pacific Review Routledge / Unknown Publisher | 2364-1177 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 303 | Biophysical Bulletin V N Karazin Kharkiv National University / Unknown Publisher | 2075-3810 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 304 | Criminology, Criminal Justice, Law And Society Western Society Of Criminology / Unknown Publisher | 2332-886X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 305 | International Journal Of Euro-Mediterranean Studies Emuni University / Unknown Publisher | 1855-3362 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 306 | Acta Geoscientica Sinica Di Qiu Xue Bao Bian Ji Bu / Unknown Publisher | 1006-3021 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 307 | Psychology Hub Sapienza Universita Editrice / Unknown Publisher | 2723-973X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 308 | Informes De La Construccion / CONSEJO SUPERIOR  INVESTIGACIONES CIENTIFICAS-CSIC | 0020-0883 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 309 | Current Opinion In Immunology / CURRENT BIOLOGY LTD | 0952-7915 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 310 | Assiut Veterinary Medical Journal (Egypt) Assiut University, Faculty Of Veterinary Medicine / Unknown Publisher | 1012-5973 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 311 | Current Opinion In Cardiology / Unknown Publisher | 1080-787X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 312 | Project Baikal Russian Academy Of Architecture And Construction Sciences,  Vostoksibacademcenter / Unknown Publisher | 2307-4485 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 313 | Journal Of Clinical Neurology / KOREAN NEUROLOGICAL ASSOC | 1738-6586 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 314 | European Journal Of Tourism Research International University College / Unknown Publisher | 1314-0817 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 315 | U.S. Geological Survey Scientific Investigations Map Us Geological Survey / Unknown Publisher | 2329-1311 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 316 | Scientific Investigations Map / Unknown Publisher | 2333-7923 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 317 | Journal Of Couple And Relationship Therapy Routledge / Unknown Publisher | 1533-2683 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 318 | Laboratorio De Arte University Of Seville, Department Of Art History / Unknown Publisher | 1130-5762 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 319 | South African Computer Journal South African Institute Of Computer Scientists And Information  Technologists / Unknown Publisher | 1015-7999 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 320 | Bialostockie Studia Literaturoznawcze Faculty Of Philology, University Of Bialystok / Unknown Publisher | 2082-9701 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 321 | Journal Of Siberian Federal University: Chemistry Siberian Federal University / Unknown Publisher | 1998-2836 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 322 | Libri Et Liberi Croatian Association Of Researchers In Children'S Literature / Unknown Publisher | 1848-3488 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 323 | Muzeologia A Kulturne Dedicstvo Muzeologia A Kulturne Dedicstvo, O.Z / Unknown Publisher | 1339-2204 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 324 | Potestas Universitat Jaume I / Unknown Publisher | 1888-9867 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 325 | Lotus International / EDITORIALE LOTUS | 1124-9064 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 326 | National Center For Health Statistics Data Brief United States National Center For Health Statistics / Unknown Publisher | 1941-4927 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 327 | Journal Of Food Health And Bioenvironmental Science Research And Development Institute Suan Dusit University / Unknown Publisher | 2630-0311 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 328 | Australasian Journal Of Combinatorics University Of Queensland Press / Unknown Publisher | 2202-3518 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 329 | Journal Of Geodesy And Geoinformation Science Sinomaps Press / Unknown Publisher | 2096-1650 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 330 | China Rubber Industry Editorial Office Of China Rubber Industry / Unknown Publisher | 1000-890X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 331 | Macromolecules / AMER CHEMICAL SOC | 0024-9297 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 332 | American Biology Teacher / NATL ASSOC BIOLOGY TEACHERS  INC | 0002-7685 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 333 | Huisarts En Wetenschap Bohn Stafleu Van Loghum / Unknown Publisher | 0018-7070 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 334 | China Safety Science Journal Editorial Department Of China Safety Science Journal / Unknown Publisher | 1003-3033 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 335 | Central European Journal Of Urology Polish Urological Association / Unknown Publisher | 2080-4806 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 336 | Texas Heart Institute Journal / TEXAS HEART INST | 0730-2347 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 337 | Southern African Journal Of Hiv  Medicine / AOSIS | 1608-9693 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 338 | Journal Of Drugs In Dermatology / JOURNAL OF DRUGS IN  DERMATOLOGY | 1545-9616 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 339 | Nigerian Journal Of Parasitology Parasitology And Public Health Society Of Nigeria / Unknown Publisher | 1117-4145 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 340 | Briefings In Functional Genomics / Unknown Publisher | 2041-2647 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 341 | Proceedings Of Institution Of Civil Engineers: Construction  Materials Ice Publishing / Unknown Publisher | 1747-650X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 342 | Revista Cubana De Medicina Tropical Editorial Ciencias Medicas / Unknown Publisher | 0375-0760 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 343 | Oral Science International The Japanese Stomatological Society / Unknown Publisher | 1348-8643 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 344 | Psicologia Associacao Portuguesa De Psicologia / Unknown Publisher | 0874-2049 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 345 | Opuholi Zenskoj Reproduktivnoj Sistemy Abv-Press Publishing House / Unknown Publisher | 1994-4098 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 346 | Journal Of Wireless Mobile Networks, Ubiquitous Computing,  And Dependable Applications  Innovative Information Science And Technology Research  Group / Unknown Publisher | 2093-5374 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 347 | Tempo Psicanalitico Sociedade De Psicanalise Iracy Doyle / Unknown Publisher | 0101-4838 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 348 | International Journal Of Ambient Computing And Intelligence Igi Global Publishing / Unknown Publisher | 1941-6237 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 349 | Acta Adriatica / INST OCEANOGRAFIJU I RIBARSTVO | 0001-5113 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 350 | Chemical Biology Letters Sciencein Publishing / Unknown Publisher | 2347-9825 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 351 | Migracijske I Etnicke Teme Institute For Migration And Ethnic Studies / Unknown Publisher | 1333-2546 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 352 | Journal Of Medicinal Plants For Economic Development Aosis (Pty) Ltd / Unknown Publisher | 2519-559X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 353 | Acdi Anuario Colombiano De Derecho Internacional Universidad Del Rosario / N°   ISSN   E-ISSN | 2027-1131 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 354 | Biopharm International / ADVANSTAR COMMUNICATIONS  INC | 1542-166X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 355 | Quintessence International / QUINTESSENCE PUBLISHING CO INC | 0033-6572 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 356 | International Journal Of Industrial Engineering And Production  Research Iran University Of Science And Technology / Unknown Publisher | 2345-363X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 357 | Contemporary Social Sciences Sichuan Academy Of Social Sciences / Unknown Publisher | 2096-0212 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 358 | Rivista Di Storia Economica Societa Editrice Il Mulino / Unknown Publisher | 2612-1026 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 359 | Clinical Ophthalmology Dove Medical Press Ltd. / Unknown Publisher | 1177-5467 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 360 | Indian Journal Of Genetics And  Plant Breeding / INDIAN SOC GENET PLANT  BREEDING | 0019-5200 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 361 | Pouvoirs: Revue D'Etudes Constitutionnelles Et Politiques Editions Du Seuil / Unknown Publisher | 0152-0768 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 362 | Current Atherosclerosis Reports / CURRENT MEDICINE GROUP | 1523-3804 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 363 | Keio Journal Of Medicine Keio University School Of Medicine / Unknown Publisher | 0022-9717 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 364 | Epistemology And Philosophy Of Science Institute Of Philosophy, Russian Academy Of Sciences / Unknown Publisher | 1811-833X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 365 | Economic And Environmental Geology The Korean Society Of Economic And Environmental Geology / Unknown Publisher | 1225-7281 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 366 | Revue Archeologique Presses Universitaires De France / Unknown Publisher | 0035-0737 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 367 | Revue Archéologique / Unknown Publisher | 2104-3868 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 368 | Functional Materials National Academy Of Sciences Of Ukraine / Unknown Publisher | 1027-5495 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 369 | International Journal Of Analysis And Applications Semnan University, Center Of Excellence In Nonlinear Analysis  And Applications / Unknown Publisher | 2291-8639 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 370 | Revista De Historia Industrial / UNIV BARCELONA, DEPT HISTORIA,  INST ECONOMIQUES | 1132-7200 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 371 | Orthopedic Reviews Open Medical Publishing / Unknown Publisher | 2035-8164 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 372 | Journal Of Food Products Marketing Routledge / Unknown Publisher | 1045-4446 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 373 | Sententiae Vinnytsia National Technical University / Unknown Publisher | 2075-6461 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 374 | Academy Of Management Annals / ACAD MANAGEMENT | 1941-6067 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 375 | Australasian Drama Studies / AUSTRALASIAN ASSOC THEATRE  DRAMA & PERFORMANCE STUDIES | 0810-4123 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 376 | Australasian Drama Studies Australasian Association For Theatre, Drama And Performance  Studies / Unknown Publisher | 2209-640X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 377 | International Journal Of Decision Support System Technology Igi Global Publishing / Unknown Publisher | 1941-6296 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 378 | Journal Of Mathematical Physics  Analysis Geometry / B. VERKIN INST LOW TEMPERATURE  PHYSICS AND ENGINEERING NATL  ACAD SCIENCES UKRAINE | 1812-9471 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 379 | Ibsen Studies Routledge / Unknown Publisher | 1502-1866 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 380 | Ejournal Of Edemocracy And Open Government Department For E-Governance And Administration / Unknown Publisher | 2075-9517 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 381 | Middle East Development Journal Routledge / Unknown Publisher | 1793-8120 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 382 | Journal Of Conflict Archaeology Maney Publishing / Unknown Publisher | 1574-0773 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 383 | Pakistan Journal Of Engineering And Applied Sciences University Of Engineering And Technology, Lahore / Unknown Publisher | 1995-1302 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 384 | Journal Of Cardiovascular Aging Oae Publishing Inc. / Unknown Publisher | 2768-5993 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 385 | Yuhang Xuebao/Journal Of Astronautics Chinese Society Of Astronautics / Unknown Publisher | 1000-1328 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 386 | Neurologia Medico-Chirurgica / JAPAN NEUROSURGICAL SOC | 0470-8105 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 387 | New Directions For Teaching And Learning / Unknown Publisher | 1536-0768 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 388 | Archives Of Biological Sciences / INST BIOLOSKA ISTRAZIVANJA  SINISA STANKOVIC | 0354-4664 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 389 | Journal Of Shellfish Research / NATL SHELLFISHERIES ASSOC | 0730-8000 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 390 | Grasas Y Aceites / CONSEJO SUPERIOR  INVESTIGACIONES CIENTIFICAS-CSIC | 0017-3495 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 391 | Bmj Open Sport And Exercise Medicine Bmj Publishing Group / Unknown Publisher | 2055-7647 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 392 | Human Affairs / Unknown Publisher | 1338-2373 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 393 | Augustinian Studies / PHILOSOPHY DOCUMENTATION  CENTER | 0094-5323 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 394 | Spiritus-A Journal Of Christian  Spirituality / JOHNS HOPKINS UNIV PRESS | 1533-1709 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 395 | Avian Conservation And Ecology / RESILIENCE ALLIANCE | 1712-6568 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 396 | Annales Mathematiques Blaise Pascal Universite Clermont Auvergne / N°   ISSN   E-ISSN | 1259-1734 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 397 | Rasprave Instituta Za Hrvatski Jezik I Jezikoslovlje Institut Za Hrvatski Jezik I Jezikoslovlje / Unknown Publisher | 1331-6745 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 398 | Rasprave Instituta Za Hrvatski Jezik I Jezikoslovlje / Unknown Publisher | 1849-0379 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 399 | Shedet Fayoum University, Faculty Of Archaeology / Unknown Publisher | 2356-8704 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 400 | Resital Faculty Of Performing Arts, Institut Seni Indonesia Yogyakarta / N°   ISSN   E-ISSN | 2085-9910 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 401 | Sae International Journal Of Transportation Safety Sae International / N°   ISSN   E-ISSN | 2327-5626 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 402 | Učënye Zapiski Kazanskogo Universiteta. Seriâ  Estestvennye Nauki/Učënye Zapiski Kazanskogo Universiteta. Seriâ Estestvennye Nauki/Učenye Zapiski Kazanskogo Gosudarstvennogo Universiteta. Seriâ Estestvennye Nauki / Unknown Publisher | 1815-6169 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 403 | Uchenye Zapiski Kazanskogo Universiteta. Seriya Estestvennye  Nauki Kazan Federal University / Unknown Publisher | 2500-218X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 404 | Gematologiya I Transfuziologiya / MINISTERSTVO  ZDRAVOOKHRANENIYA | 0234-5730 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 405 | World Literature Studies / INST WORLD LITERATURE, SLOVAK  ACAD SCIENCES | 1337-9275 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 406 | Unnes Journal Of Public Health Universitas Negeri Semarang / Unknown Publisher | 2252-6781 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 407 | Schutzian Research Zeta Books / Unknown Publisher | 2067-0621 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 408 | Energy Storage And Saving Keai Publishing Communications Ltd. / Unknown Publisher | 2772-6835 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 409 | Elia Universidad De Sevilla / Unknown Publisher | 1576-5059 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 410 | Journal Of Critical And Intensive Care Society Of Turkish Intensivists / Unknown Publisher | 2717-6428 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 411 | Indian Journal Of Engineering Discovery Scientific Society / Unknown Publisher | 2319-7757 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 412 | Health Education And Health Promotion Tarbiat Modares University / Unknown Publisher | 2345-2897 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 413 | Journal Of Health System Research Isfahan University Of Medical Sciences(Iums) / Unknown Publisher | 2322-5564 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 414 | Journal Of Signal Processing Editorial Board Of Journal Of Signal Processing / Unknown Publisher | 1003-0530 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 415 | Annals Of Mathematics / PRINCETON UNIV, DEPT  MATHEMATICS | 0003-486X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 416 | Nonlinearity / IOP PUBLISHING LTD | 0951-7715 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 417 | Journal Of The Korean Society Of Clothing And Textiles Korean Society Of Clothing And Textiles / Unknown Publisher | 1225-1151 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 418 | Review Of African Political  Economy / SCIENCEOPEN | 0305-6244 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 419 | Iranian Red Crescent Medical  Journal / DUBAI IRANIAN HOSP | 2074-1804 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 420 | Great Lakes Entomologist Michigan Entomological Society / Unknown Publisher | 0090-0222 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 421 | Chinese Medicine (United Kingdom) Biomed Central Ltd / Unknown Publisher | 1991-0150 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 422 | Journal For Specialists In Group Work Routledge / Unknown Publisher | 0193-3922 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 423 | The Journal For Specialists In Group Work / Unknown Publisher | 1549-6295 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 424 | Geofizicheskiy Zhurnal Subbotin Institute Of Geophysics Of The National Academy Of  Sciences Of Ukraine (Sig Of Nasu). / N°   ISSN   E-ISSN | 0203-3100 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 425 | Medicina Moderna Bucharest College Of Physicians / Unknown Publisher | 1223-0472 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 426 | Review Of Central And East  European Law / MARTINUS NIJHOFF PUBL | 0925-9880 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 427 | Review Of Central And East European Law / Unknown Publisher | 1573-0352 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 428 | El-Cezeri Journal Of Science And Engineering Tubitak / Unknown Publisher | 2148-3736 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 429 | Geochemistry-Exploration  Environment Analysis / GEOLOGICAL SOC PUBL HOUSE | 1467-7873 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 430 | Zuchtungskunde / EUGEN ULMER GMBH CO | 0044-5401 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 431 | Boletim De Ciencias Geodesicas Universidade Federal Do Parana / Unknown Publisher | 1413-4853 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 432 | Contagion: Journal Of Violence, Mimesis, And Culture Michigan State University / Unknown Publisher | 1075-7201 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 433 | She Ji Tongji University Press / Unknown Publisher | 2405-8718 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 434 | Scientific Bulletin Of Mukachevo State University. Series  Economics Mukachevo State University / Unknown Publisher | 2313-8114 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 435 | Jurnal Ilmiah Islam Futura Universitas Islam Negeri Ar-Raniry / Unknown Publisher | 1412-1190 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 436 | Metatheoria Editorial De La  Universidad Nacional De Tres De Febrero  (Eduntref) / Unknown Publisher | 1853-2322 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 437 | Journal Of Emergency Practice And Trauma Kerman University Of Medical Sciences / Unknown Publisher | 2383-4544 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 438 | Journal Of Geometry And Symmetry In Physics Bulgarian Academy Of Sciences, Institute Of Mechanics / Unknown Publisher | 1312-5192 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 439 | Cincinnati Romance Review Department Of Romance Languages And Literatures / Unknown Publisher | 2155-8817 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 440 | International Journal Of Plasma Environmental Science And  Technology Institute Of Electrostatics Japan / Unknown Publisher | 2435-0125 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 441 | Revista Espanola De  Investigaciones Sociologicas / CENTRO INVESTIGACIONES  SOCIOLOGICAS | 0210-5233 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 442 | Colombia Medica / CORPORACION EDITORA MEDICA  VALLE | 0120-8322 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 443 | Journal Of Posthumanism Transnational Press London Ltd / Unknown Publisher | 2634-3576 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 444 | Agricultural Science Digest Agricultural Research Communication Centre / Unknown Publisher | 0253-150X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 445 | Radioengineering / SPOLECNOST PRO  RADIOELEKTRONICKE INZENYRSTVI | 1210-2512 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 446 | Military Balance Routledge / Unknown Publisher | 0459-7222 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 447 | Asian Cinema Intellect Ltd. / Unknown Publisher | 1059-440X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 448 | Proceedings Of The Institution Of Civil Engineers: Bridge  Engineering Ice Publishing / Unknown Publisher | 1478-4637 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 449 | Acta Carsologica / KARST RESEARCH INST ZRC SAZU | 0583-6050 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 450 | Zeszyty Wiejskie Lodz University Press / Unknown Publisher | 1506-6541 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 451 | Transactions Of The Atomic Energy Society Of Japan Atomic Energy Society Of Japan / N°   ISSN   E-ISSN | 1347-2879 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 452 | Cuadernos Electronicos De Filosofia Del Derecho University Of Valencia, Human Rights Institute. / Unknown Publisher | 1138-9877 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 453 | Macedonian Journal Of  Chemistry And Chemical  Engineering / SOC CHEMISTS TECHNOLOGISTS  MADECONIA | 1857-5552 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 454 | Laboratorium: Russian Review Of Social Research Institute For European Russian And Eurasian Studies, The  George Washington University / Unknown Publisher | 2076-8214 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 455 | Bmj Nutrition, Prevention And Health Bmj Publishing Group / Unknown Publisher | 2516-5542 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 456 | Historia Provinciae - Zurnal Regional'Noj Istorii Cherepovets State University / Unknown Publisher | 2587-8344 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 457 | Darulfunun Ilahiyat Istanbul Universitesi / Unknown Publisher | 2630-6069 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 458 | Health And Social Care Delivery Research Nihr Journals Library / Unknown Publisher | 2755-0060 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 459 | Casopis Za Suvremenu Povijest Croatian Institute Of History / Unknown Publisher | 0590-9597 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 460 | Studi E Saggi Linguistici Edizioni Ets / Unknown Publisher | 0085-6827 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 461 | Economia Y Politica Universidad Adolfo Ibanez / N°   ISSN   E-ISSN | 0719-4714 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 462 | Bollettino Storico - Bibliografico Subalpino Deputazione Subalpina Di Storia Patria / Unknown Publisher | 0391-6715 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 463 | Nanomedicine Journal Mashhad University Of Medical Sciences / Unknown Publisher | 2322-5904 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 464 | Estudios Bizantinos Universidad De Alcala / Unknown Publisher | 2952-1432 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 465 | Organometallics / AMER CHEMICAL SOC | 0276-7333 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 466 | Structural Concrete / ERNST & SOHN | 1464-4177 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 467 | Journal Of The Southern African Institute Of Mining And Metallurgy / Unknown Publisher | 0038-223X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 468 | Journal Of The Southern African  Institute Of Mining And  Metallurgy / SOUTHERN  AFRICAN INST MINING  METALLURGY | 2411-9717 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 469 | Journal Of Earth Science / CHINA UNIV GEOSCIENCES, WUHAN | 1674-487X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 470 | Geogaceta Sociedad Geologica De Espana / Unknown Publisher | 0213-683X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 471 | Applied Mathematics/Applied Mathematics. A Journal Of Chinese Universities/Gao-Xiao Yingyong Shuxue Xuebao / Unknown Publisher | 1000-4424 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 472 | Applied Mathematics-A Journal Of  Chinese Universities Series B / ZHEJIANG UNIV PRESS | 1005-1031 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 473 | Catholic Biblical Quarterly / CATHOLIC BIBLICAL ASSOC AMER | 0008-7912 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 474 | Korean Journal Of Adult Nursing Korean Society Of Adult Nursing / N°   ISSN   E-ISSN | 1225-4886 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 475 | Rivista Geografica Italiana Francoangeli Edizioni / Unknown Publisher | 0035-6697 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 476 | Research In Learning Technology Association For Learning Technology / Unknown Publisher | 2156-7069 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 477 | Andes Pediatrica Sociedad Chilena De Pediatria / Unknown Publisher | 2452-6045 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 478 | Studies On Ethno-Medicine Kamla-Raj Enterprises / Unknown Publisher | 0973-5070 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 479 | Studies On Ethno-Medicine / Unknown Publisher | 2456-6772 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 480 | Soils And Rocks Associacao Brasileira De Mecanica Dos Solos / Unknown Publisher | 1980-9743 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 481 | Soils And Rocks / Unknown Publisher | 2675-5475 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 482 | Phytoprotection / QUEBEC SOC PROTECT PLANTS | 0031-9511 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 483 | Contemporary Italian Politics Routledge / Unknown Publisher | 2324-8823 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 484 | Acta Medica Lituanica Vilnius University Press / Unknown Publisher | 1392-0138 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 485 | Revista De Derecho Administrativo Economico Pontifica Universidad Catolica De Chile, Programa De Derecho  Administrativo Economico / Unknown Publisher | 0717-4888 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 486 | Shagi/ Steps Russian Presidential Academy Of National Economy And Public  Administration / Unknown Publisher | 2412-9410 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 487 | Revista Brasileira De Ciencias Policiais National Police Academy / Unknown Publisher | 2178-0013 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 488 | Journal Of The National Cancer Center Chinese National Cancer Center / Unknown Publisher | 2096-8663 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 489 | Tec Empresarial Business School, Instituto Tecnologico De Costa Rica / Unknown Publisher | 1659-2395 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 490 | Japanese Political Economy Routledge / Unknown Publisher | 2329-194X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 491 | Operational Research In Engineering Sciences: Theory And  Applications Regional Association For Security And Crisis Management / Unknown Publisher | 2620-1607 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 492 | Journal Of Adhesive Dentistry / QUINTESSENCE PUBLISHING CO INC | 1461-5185 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 493 | Zeitschrift Fur Ostmitteleuropa-Forschung Herder Institute For Historical Research On East Central Europe  - Institute Of The Leibniz Association / Unknown Publisher | 2701-0449 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 494 | Sen-I Gakkaishi / SOC FIBER SCIENCE TECHNOLOGY | 0037-9875 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 495 | Eurosurveillance / EUR CENTRE DIS PREVENTION &  CONTROL | 1025-496X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 496 | Jmir Research Protocols Jmir Publications Inc. / Unknown Publisher | 1929-0748 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 497 | Acta Odontologica Scandinavica / MEDICAL JOURNAL SWEDEN AB | 0001-6357 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 498 | New Physics: Sae Mulli Korean Physical Society / Unknown Publisher | 0374-4914 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 499 | Journal Of Differential Geometry / INT PRESS BOSTON, INC | 0022-040X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 500 | Schweizerische Zeitschrift Fur Forstwesen Swiss Forestry Society / Unknown Publisher | 0036-7818 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 501 | Sovremennye Problemy Distantsionnogo Zondirovaniya Zemli Iz  Kosmosa Space Research Institute Of The Russian Academy Of Sciences / Unknown Publisher | 2070-7401 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 502 | Transnav Faculty Of Navigation, Gdynia Maritime University / Unknown Publisher | 2083-6473 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 503 | Cahiers De Psychologie Clinique De Boeck Supérieur / Unknown Publisher | 1370-074X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 504 | International Journal Of  Simulation Modelling / DAAAM INTERNATIONAL VIENNA | 1726-4529 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 505 | Journal Of Curriculum And Teaching Sciedu Press / Unknown Publisher | 1927-2677 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 506 | Oncogematologiya Abv-Press Publishing House / Unknown Publisher | 1818-8346 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 507 | Quaderni Storici / SOC ED IL MULINO | 0301-6307 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 508 | Folia Linguistica Et Litteraria University Of Montenegro / Unknown Publisher | 1800-8542 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 509 | L1 Educational Studies In Language And Literature International Association For Research In L1 Education (Arle) / Unknown Publisher | 1567-6617 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 510 | Neurological Research And Practice Biomed Central Ltd / Unknown Publisher | 2524-3489 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 511 | Fundamina Juta And Company Ltd / Unknown Publisher | 1021-545X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 512 | International Journal Of Sociotechnology And Knowledge  Development Igi Global Publishing / Unknown Publisher | 1941-6253 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 513 | Riset Geologi Dan Pertambangan National Research And Innovation Agency (Brin) / Unknown Publisher | 0125-9849 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 514 | Reports On Mathematical Logic / JAGIELLONIAN UNIV, THEORETICAL  COMPUTER SCIENCE DEPT | 0137-2904 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 515 | Reports On Mathematical Logic Jagiellonian University Press / Unknown Publisher | 2084-2589 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 516 | Journal Of The Mexican Chemical  Society / SOC QUIMICA MEXICO | 1665-9686 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 517 | Rivista Di Archeologia Giorgio Bretschneider / Unknown Publisher | 2284-4546 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 518 | Hygiene + Medizin Mhp-Verlag Gmbh / Unknown Publisher | 0172-3790 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 519 | Journal Of Geophysical Research- Oceans / AMER GEOPHYSICAL UNION | 2169-9275 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 520 | Thermal Science / VINCA INST NUCLEAR SCI | 0354-9836 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 521 | Indian Journal Of Agricultural Research Agricultural Research Communication Centre / Unknown Publisher | 0367-8245 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 522 | Revista Brasileira De Cirurgia Plastica Sociedade Brasileira De Cirurgia Plastica / Unknown Publisher | 1983-5175 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 523 | Veterinarski Glasnik Veterinarski Fakultet / Unknown Publisher | 0350-2457 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 524 | Endoxa Universidad Nacional De Educacion A Distancia (Uned) / Unknown Publisher | 1133-5351 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 525 | Revista U.D.C.A Actualidad And Divulgacion Cientifica Universidad De Ciencias Aplicadas Y Ambientales U.D.C.A / Unknown Publisher | 0123-4226 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 526 | Hispania-Revista Espanola De  Historia / CONSEJO SUPERIOR  INVESTIGACIONES CIENTIFICAS-CSIC | 0018-2141 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 527 | Asia-Pacific Review / Unknown Publisher | 1469-2937 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 528 | Journal Of Religious And Theological Information Routledge / Unknown Publisher | 1047-7845 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 529 | Journal Of Applied Linguistics And Professional Practice Equinox Publishing Ltd / Unknown Publisher | 2040-3658 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 530 | Nuevo Derecho University Institution Of Envigado / Unknown Publisher | 2011-4540 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 531 | Biomaterials Translational Chinese Medical Multimedia Press Co Ltd / Unknown Publisher | 2096-112X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 532 | Die Kuste German Coastal Engineering Research Council (Kfki) / Unknown Publisher | 0452-7739 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 533 | Intralinea University Of Bologna / Unknown Publisher | 1827-000X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 534 | Journal Of Pain / CHURCHILL LIVINGSTONE | 1526-5900 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 535 | Journal Of Sedimentary Research / SEPM-SOC SEDIMENTARY GEOLOGY | 1527-1404 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 536 | Virittaja University Of Helsinki / Unknown Publisher | 0042-6806 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 537 | Virittäjä / Unknown Publisher | 2242-8828 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 538 | Arquivo Brasileiro De Medicina  Veterinaria E Zootecnia / ARQUIVO BRASILEIRO MEDICINA  VETERINARIA ZOOTECNIA | 0102-0935 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 539 | Annales Medico-Psychologiques / MASSON EDITEUR | 0003-4487 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 540 | Quarterly Of Applied  Mathematics / BROWN UNIV | 0033-569X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 541 | International Journal Of Interactive Mobile Technologies International Federation Of Engineering Education Societies  (Ifees) / Unknown Publisher | 1865-7923 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 542 | Zhongguo Jixie Gongcheng/China Mechanical Engineering China Mechanical Engineering Magazine Office / Unknown Publisher | 1004-132X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 543 | Idealistic Studies / PHILOSOPHY DOCUMENTATION  CENTER | 0046-8541 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 544 | European Education Routledge / Unknown Publisher | 1056-4934 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 545 | International Review Of Law, Computers And Technology Routledge / Unknown Publisher | 1360-0869 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 546 | Revista Mexicana De Ingenieria  Quimica / UNIV AUTONOMA  METROPOLITANA-IZTAPALAPA | 1665-2738 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 547 | Russian Journal Of Earth Sciences Geophysical Center Of The Russian Academy Of Sciences / Unknown Publisher | 1681-1178 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 548 | Rossijskij Žurnal Nauk O Zemle/Russian Journal Of Earth Sciences / Unknown Publisher | 1681-1194 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 549 | Periodicum Biologorum / PERIODICUM BIOLOGORUM | 0031-5362 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 550 | Journal Of Current Ophthalmology Iranian Society Of Opthalmology / Unknown Publisher | 2452-2325 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 551 | Psychiatry And Clinical  Psychopharmacology / AVES | 2475-0573 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 552 | Journal Of Seed Science / ABRATES-ASSOC BRASILEIRA  TECHNOLOGIA SEMENTES | 2317-1537 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 553 | Sign Language & Linguistics / Unknown Publisher | 1569-996X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 554 | Biblos Universidade De Coimbra - Faculdade De Letras / Unknown Publisher | 0870-4112 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 555 | Journal Of Vibration Testing And System Dynamics L And H Scientific Publishing, Llc / Unknown Publisher | 2475-4811 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 556 | Ars (Bratislava) Art Research Centre Of Slovak Academy Of Sciences / Unknown Publisher | 0044-9008 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 557 | Artificial Intelligence In Geosciences Keai Communications Co. / Unknown Publisher | 2666-5441 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 558 | Fmc. Formación Médica Continuada/Fomeco. Formación Médica Continuada / Unknown Publisher | 1132-6476 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 559 | Fmc Formacion Medica Continuada En Atencion Primaria Ediciones Doyma, S.L. / Unknown Publisher | 1578-9675 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 560 | Socialni Prace Association Of Educators In Social Work / Unknown Publisher | 1805-885X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 561 | Rare Metal Materials And  Engineering / NORTHWEST INST NONFERROUS  METAL RESEARCH | 1002-185X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 562 | Journal Of Bacteriology / Unknown Publisher | 1067-8832 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 563 | Deutsches Arzteblatt  International / DEUTSCHER AERZTE-VERLAG GMBH | 1866-0452 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 564 | Gerontechnology International Society For Gerontechnology / N°   ISSN   E-ISSN | 1569-1101 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 565 | Rae-Revista De Administracao De  Empresas / FUNDACAO GETULIO VARGAS | 0034-7590 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 566 | Brazilian Journal Of  Cardiovascular Surgery / SOC BRASIL CIRURGIA CARDIOVASC | 0102-7638 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 567 | Revista Peruana De Ginecologia Y Obstetricia Peruvian Society Of Obstetrics And Gynecology / Unknown Publisher | 2304-5124 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 568 | Gut And Liver / EDITORIAL OFFICE GUT & LIVER | 1976-2283 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 569 | Ciencia Animal Brasileira Universidade Federal De Goias (Ufg) / Unknown Publisher | 1518-2797 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 570 | Chemistry And Chemical Technology Lviv Polytechnic National University / Unknown Publisher | 1996-4196 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 571 | The Tqm Journal / Unknown Publisher | 1754-274X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 572 | Seminars In Spine Surgery W.B. Saunders / Unknown Publisher | 1040-7383 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 573 | Revista Espanola De Orientacion Y Psicopedagogia Universidad Nacional De Educacion A Distancia (Uned) / Unknown Publisher | 1139-7853 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 574 | Anais Do Museu Paulista Universidade De Sao Paulo / Unknown Publisher | 0101-4714 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 575 | Kuban Scientific Medical Bulletin Kuban State Medical University / Unknown Publisher | 1608-6228 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 576 | Vniversitas Pontificia Universidad Javeriana / N°   ISSN   E-ISSN | 0041-9060 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 577 | Language Teaching Research Quarterly European Knowledge Development (Eurokd) / Unknown Publisher | 2667-6753 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 578 | Journal Of Applied Veterinary Sciences Egyptian Society For Animal Management (Esam) / Unknown Publisher | 1687-4072 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 579 | Russian Journal Of Stomatology Media Sphera Publishing Group / Unknown Publisher | 2072-6406 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 580 | Water Conservation And Management Zibeline International Publishing Sdn. Bhd. / Unknown Publisher | 2523-5664 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 581 | Catalan Journal Of Linguistics Universitat Autonoma De Barcelona / Unknown Publisher | 1695-6885 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 582 | Catalan Journal Of Linguistics / Unknown Publisher | 2014-9719 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 583 | Strides In Development Of Medical Education Journal Kerman University Of Medical Sciences / Unknown Publisher | 2645-3452 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 584 | Teknomekanik / Unknown Publisher | 1979-6102 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 585 | Teknomekanik Universitas Negeri Padang / Unknown Publisher | 2621-8720 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 586 | Tamkang Review Tamkang University / Unknown Publisher | 0049-2949 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 587 | Dia-Noesis University Of Western Macedonia / Unknown Publisher | 2459-413X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 588 | Boletin Geologico Colombian Geological Service / Unknown Publisher | 0120-1425 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 589 | Malaysian Journal Of Pathology / MALAYSIAN JOURNAL PATHOLOGY | 0126-8635 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 590 | Journal Of Zoonotic Diseases University Of Tabriz / Unknown Publisher | 2476-535X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 591 | Byu Studies Quarterly / BRIGHAM YOUNG UNIV | 2167-8480 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 592 | Jinshu Rechuli/Heat Treatment Of Metals Chinese Heat Treatment Society / N°   ISSN   E-ISSN | 0254-6051 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 593 | Indiana Ibero - Amerikanisches Institut / Unknown Publisher | 0341-8642 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 594 | Isij International / IRON STEEL INST JAPAN KEIDANREN  KAIKAN | 0915-1559 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 595 | Plos Biology / PUBLIC LIBRARY SCIENCE | 1544-9173 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 596 | Journal Of Pharmacological  Sciences / JAPANESE PHARMACOLOGICAL SOC | 1347-8613 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 597 | Homme Et La Societe Editions Anthropos / Unknown Publisher | 0018-4306 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 598 | Romantisme / EDITIONS SEDES | 0048-8593 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 599 | Journal Of Plant Biotechnology Korean Society Of Plant Biotechnology / Unknown Publisher | 1229-2818 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 600 | Journal Of Plant Biotechnology / Unknown Publisher | 1598-6365 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
