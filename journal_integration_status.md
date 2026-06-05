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
| 601 | Journal Of Invasive Cardiology / H M P COMMUNICATIONS | 1042-3931 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 602 | Europe'S Journal Of Psychology Psychopen / Unknown Publisher | 1841-0413 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 603 | Gerion Universidad Complutense Madrid / Unknown Publisher | 0213-0181 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 604 | Gerión Revista De Historia Antigua / Unknown Publisher | 1698-2444 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 605 | Revista De Economia Contemporanea Universidade Federal Do Rio De Janeiro - Ufrj / Unknown Publisher | 1415-9848 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 606 | Rem - International Engineering Journal Escola De Minas / Unknown Publisher | 2448-167X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 607 | Security And Human Rights The Security And Human Rights Monitor / Unknown Publisher | 1874-7337 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 608 | Revista Brasileira De Direito Processual Penal Instituto Brasileiro De Direito Processual Penal / Unknown Publisher | 2359-3881 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 609 | Medicina Nei Secoli University Of Rome La Sapienza / Unknown Publisher | 0394-9001 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 610 | Oil Crop Science Keai Communications Co. / Unknown Publisher | 2096-2428 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 611 | International Journal Of Asia Digital Art And Design Asia Digital Art And Design Association / N°   ISSN   E-ISSN | 1738-8074 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 612 | Milrev: Metro Islamic Law Review Faculty Of Sharia, Iain Metro / Unknown Publisher | 2986-528X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 613 | Tabano Pontificia Universidad Catolica Argentina / Unknown Publisher | 1852-7221 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 614 | Litteraria Pragensia Charles University, Faculty Of Arts / Unknown Publisher | 0862-8424 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 615 | Juridical Tribune - Review Of Comparative And International Law Society Of Juridical And Administrative Sciences / Unknown Publisher | 3008-637X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 616 | Journal Of Dental Materials And Techniques Mashhad University Of Medical Sciences / Unknown Publisher | 2252-0317 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 617 | Annals Of Saudi Medicine / K FAISAL SPEC HOSP RES CENTRE | 1319-9226 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 618 | New Scientist / NEW SCIENTIST LTD | 0262-4079 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 619 | The New Scientist / Unknown Publisher | 1356-1766 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 620 | Medicine (Spain) Ediciones Doyma, S.L. / Unknown Publisher | 0304-5412 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 621 | Medicine - Programa De Formación Médica Continuada Acreditado / Unknown Publisher | 1576-1967 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 622 | Annals Of Geophysics / IST NAZIONALE DI GEOFISICA E  VULCANOLOGIA | 1593-5213 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 623 | Revista Chilena De Derecho Privado Universidad Diego Portales / Unknown Publisher | 0718-0233 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 624 | Erdkunde / UNIV BONN, GEOGRAPHISCHES  INST | 0014-0015 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 625 | Erdkunde Erdkunde / Unknown Publisher | 2702-5985 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 626 | Sotsiologicheskie Issledovaniya / RUSSIAN ACAD SCIENCES, STATE  ACAD UNIV HUMANITIES (GAUGN) | 0132-1625 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 627 | Boletin Medico Del Hospital Infantil De Mexico Hospital Infantil De Mexico Federico Gomez / Unknown Publisher | 0539-6115 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 628 | Journal Of Clinical Pediatric  Dentistry / MRE PRESS | 1053-4628 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 629 | Applicationes Mathematicae Institute Of Mathematics. Polish Academy Of Sciences / N°   ISSN   E-ISSN | 1233-7234 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 630 | Structural Heart Cardiovascular Research Foundation / Unknown Publisher | 2474-8706 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 631 | History In Africa African Studies Association / Unknown Publisher | 0361-5413 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 632 | Western Journal Of Communication / Unknown Publisher | 1745-1027 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 633 | Petroleum Geoscience / GEOLOGICAL SOC PUBL HOUSE | 1354-0793 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 634 | Journal Of Rheumatic Diseases Korean College Of Rheumatology / Unknown Publisher | 2093-940X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 635 | Giornale Italiano Di Psicopatologia Pacini Editore Srl / Unknown Publisher | 1592-1107 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 636 | Stanovnistvo Demographic Research Centre / Unknown Publisher | 0038-982X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 637 | Al-Istinbath: Jurnal Hukum Islam State Institute For Islamic Studies Curup / Unknown Publisher | 2548-3374 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 638 | Consortium Psychiatricum Eco-Vector Llc / Unknown Publisher | 2712-7672 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 639 | Management And Prospective Recherches Et Publications En Management A.S.B.L / Unknown Publisher | 2983-8304 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 640 | Archaologisches  Korrespondenzblatt / LEIBNIZ-ZENTRUM FUER  ARCHAEOLOGIE | 0342-734X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 641 | Principia Komitet Slowianoznawstwa Pan / Unknown Publisher | 0867-5392 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 642 | Bulletin Of Insectology / ALMA MATER STUDIORUM, UNIV  BOLOGNA | 2283-0332 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 643 | Journal Of Agriculture And Rural Development In The Tropics  And Subtropics, Supplement University Of Kassel / Unknown Publisher | 1613-8422 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 644 | Lujun Gongcheng Daxue Xuebao/Journal Of Army Engineering  University Of Pla Army Engineering University Of Pla / Unknown Publisher | 2097-0730 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 645 | Revista Mexicana De Biodiversidad Universidad Nacional Autonoma De Mexico / Unknown Publisher | 1870-509X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 646 | International Journal Of Biological And Chemical Sciences International Formulae Group (Ifg) / Unknown Publisher | 1991-8631 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 647 | Revista Brasileira De Geografia Fisica Universidade Federal De Pernambuco / Unknown Publisher | 1984-2295 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 648 | World Politics / JOHNS HOPKINS UNIV PRESS | 0043-8871 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 649 | Mis Quarterly / SOC INFORM MANAGE-MIS RES  CENT | 0276-7783 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 650 | Oncology Nursing Forum / ONCOLOGY NURSING SOC | 0190-535X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 651 | Electronic Research Archive / AMER INST MATHEMATICAL  SCIENCES-AIMS | 2688-1594 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 652 | Journal Of Field Ornithology / RESILIENCE ALLIANCE | 0273-8570 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 653 | Mortality Routledge / Unknown Publisher | 1357-6275 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 654 | Investigaciones Geograficas Interuniversity Institute Of Geography And University Of  Alicante / Unknown Publisher | 0213-4691 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 655 | Acs Applied Optical Materials American Chemical Society / Unknown Publisher | 2771-9855 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 656 | Mit Sloan Management Review / SLOAN MANAGEMENT REVIEW  ASSOC, MIT SLOAN SCHOOL  MANAGEMENT | 1532-8937 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 657 | Ra-Revista De Arquitectura / UNIV NAVARRA, SERVICIO  PUBLICACIONES | 1138-5596 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 658 | Subterranean Biology / INT SOC SUBTERRANEAN BIOL | 1314-2615 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 659 | Researches In Earth Sciences Shahid Beheshti University / Unknown Publisher | 2008-8299 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 660 | Surgery Eastern Europe Professionalnye Izdaniya / Unknown Publisher | 2226-5384 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 661 | Apunts Sports Medicine Generalitat De Catalunya, Department De La Presidencia,  Secretaria General De L Esport / Unknown Publisher | 2666-5069 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 662 | Journal Of Asian Sociology Institute Of Social Development And Policy Research, Seoul  National University / Unknown Publisher | 2671-4574 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 663 | Iranian Endodontic Journal Iranian Centre For Endodontic Research / Unknown Publisher | 1735-7497 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 664 | Listy Filologicke / INST CLASSICAL STUD ACAD SCI  CZECH REPUBLIC | 0024-4457 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 665 | International Journal Of Supply And Operations Management Kharazmi University / N°   ISSN   E-ISSN | 2383-1359 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 666 | Southern Energy Construction Energy Observer Magazine Co., Ltd. / Unknown Publisher | 2095-8676 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 667 | Qiche Gongcheng/Automotive Engineering Society Of Automotive Engineers Of China (Sae-China) / Unknown Publisher | 1000-680X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 668 | Meanjin / MEANJIN COMPANY LTD | 1448-8094 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 669 | Problemi Society For Theoretical Psychoanalysis / Unknown Publisher | 0555-2419 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 670 | Journal Of Bioscience And  Bioengineering / SOC BIOSCIENCE BIOENGINEERING  JAPAN | 1347-4421 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 671 | Philosophy Today / PHILOSOPHY TODAY DEPAUL UNIV | 0031-8256 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 672 | Acta Pharmaceutica Sinica B / INST MATERIA MEDICA, CHINESE  ACAD MEDICAL SCIENCES | 2211-3835 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 673 | Indian Journal Of Pure & Applied  Physics / NATL INST SCIENCE  COMMUNICATION-NISCAIR | 0019-5596 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 674 | Zhongguo Shiyou Daxue Xuebao (Ziran Kexue Ban)/Journal Of  China University Of Petroleum (Edition Of Natural Science) University Of Petroleum, China / Unknown Publisher | 1673-5005 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 675 | Malaysian Journal Of Medicine And Health Sciences Faculty Of Medicine And Health Sciences, University Putra  Malaysia / Unknown Publisher | 1675-8544 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 676 | Malaysian Journal Of Medicine And Health Sciences / Unknown Publisher | 2636-9346 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 677 | European Public Law Kluwer Law International / Unknown Publisher | 1354-3725 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 678 | Medical Archives Academy Of Medical Sciences In Bosnia And Herzegovina / Unknown Publisher | 0350-199X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 679 | Journal Of Telecommunications And Information Technology National Institute Of Telecommunications / Unknown Publisher | 1509-4553 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 680 | Journal Of Vocational Education And Training Routledge / Unknown Publisher | 1363-6820 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 681 | Ieie Transactions On Smart Processing And Computing Institute Of Electronics Engineers Of Korea / Unknown Publisher | 2287-5255 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 682 | Indonesian Journal Of Obstetrics And Gynecology Indonesian Society Of Obstetrics And Gynecology / Unknown Publisher | 2338-6401 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 683 | Ain Shams Dental Journal (Egypt) Ain Shams University, Faculty Of Dentistry / Unknown Publisher | 1110-7642 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 684 | Plant Ecology And Evolution / SOC ROYAL BOTAN BELGIQUE | 2032-3913 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 685 | History Of Economic Ideas Fabrizio Serra Editore Srl / Unknown Publisher | 1122-8792 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 686 | Communication Law And Policy Routledge / Unknown Publisher | 1081-1680 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 687 | Filosoficky Casopis / FILOSOFICKY CASOPIS INST  PHILOSOPHY | 0015-1831 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 688 | Viral Hepatitis Journal Galenos Publishing House / Unknown Publisher | 1307-9441 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 689 | Ukrainian Journal Of Radiology And Oncology Grigoriev Institute For Medical Radiology And Oncology Nams  Of Ukraine / Unknown Publisher | 2708-7166 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 690 | Science Of Traditional Chinese Medicine Wolters Kluwer Health / Unknown Publisher | 2836-9211 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 691 | Siriraj Medical Journal Siraraj Hospital Faculty Of Medicine / Unknown Publisher | 2629-995X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 692 | Journal Of Ear Nose Throat And Head Neck Surgery Turkiye Klinikleri / Unknown Publisher | 1300-6525 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 693 | Journal Of Law, Market And Innovation University Of Torino / Unknown Publisher | 2785-7867 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 694 | Ancient Numismatic Fabrizio Serra Editore / Unknown Publisher | 2724-2145 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 695 | Journal Of Biomedical Optics / SPIE-SOC PHOTO-OPTICAL  INSTRUMENTATION ENGINEERS | 1083-3668 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 696 | Strategic Direction / Unknown Publisher | 1758-8588 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 697 | Progress In Electromagnetics  Research-Pier / EMW PUBLISHING | 1070-4698 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 698 | Brazilian Journal Of Veterinary Research And Animal Science Faculdade De Medicina Veterinaria E Zootecnia, Usp / Unknown Publisher | 1413-9596 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 699 | Mankind Quarterly Ulster Institute For Social Research / Unknown Publisher | 0025-2344 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 700 | Asia Marketing Journal Korean Marketing Association / Unknown Publisher | 1598-7868 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 701 | East European Journal Of Physics V N Karazin Kharkiv National University / Unknown Publisher | 2312-4334 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 702 | Nematropica / ORGANIZATION TROP AMER  NEMATOLOGISTS | 0099-5444 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 703 | Journal Of Mining And  Metallurgy Section B-Metallurgy / TECHNICAL FACULTY, BOR-SERBIA | 1450-5339 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 704 | Visible Language University Of Cincinnati / Unknown Publisher | 0022-2224 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 705 | Journal Of War And Culture Studies Maney Publishing / Unknown Publisher | 1752-6272 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 706 | Cuadernos De Investigacion Historica Fundacion Universitaria Espanola / Unknown Publisher | 0210-6272 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 707 | Slovensky Narodopis Slovak Academy Of Sciences / Unknown Publisher | 1335-1303 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 708 | Electronic Transactions On  Numerical Analysis / KENT STATE UNIVERSITY | 1068-9613 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 709 | Etna - Electronic Transactions On Numerical Analysis / Unknown Publisher | 1097-4067 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 710 | E-Review Of Tourism Research Texas A And M University / Unknown Publisher | 1941-5842 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 711 | Red Cedar Review Michigan State University Press / Unknown Publisher | 0034-1967 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 712 | Journal Of Monolingual And Bilingual Speech Equinox Publishing Ltd / Unknown Publisher | 2631-8407 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 713 | Geologica Macedonica Goce Delchev University Of Shtip / N°   ISSN   E-ISSN | 0352-1206 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 714 | Computational Methods For Differential Equations University Of Tabriz / Unknown Publisher | 2383-2533 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 715 | Journal Of Vacuum Science &  Technology A / A V S AMER INST PHYSICS | 0734-2101 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 716 | Environmental Research Letters / IOP PUBLISHING LTD | 1748-9326 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 717 | Revista Brasileira De Zootecnia- Brazilian Journal Of Animal  Science / REVISTA BRASILEIRA ZOOTECNIA  BRAZILIAN JOURNAL ANIMAL SCI | 1516-3598 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 718 | Current Opinion In Ophthalmology / Unknown Publisher | 1080-8132 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 719 | Journal Of The Japanese Society  For Food Science And  Technology-Nippon Shokuhin  Kagaku Kogaku Kaishi / JAPAN SOC FOOD SCIENCE  TECHNOLOGY | 1341-027X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 720 | Periodica Polytechnica Mechanical Engineering Budapest University Of Technology And Economics / Unknown Publisher | 0324-6051 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 721 | Science Immunology / AMER ASSOC ADVANCEMENT  SCIENCE | 2470-9468 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 722 | Acta Mycologica Polish Botanical Society / Unknown Publisher | 0001-625X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 723 | Gedrag & Organisatie / UITGEVERIJ LEMMA B V | 0921-5077 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 724 | Egyptian Journal Of Petroleum Egyptian Petroleum Research Institute / Unknown Publisher | 1110-0621 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 725 | Global Bioethics Routledge / Unknown Publisher | 1128-7462 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 726 | Psychology And Law Moscow State University Of Psychology And Education / Unknown Publisher | 2222-5196 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 727 | American Journal Of Animal And Veterinary Sciences Science Publications / Unknown Publisher | 1557-4555 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 728 | Journal Of Service Theory And Practice / Unknown Publisher | 2055-6233 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 729 | Caritas Et Veritas University Of South Bohemia / Unknown Publisher | 1805-0948 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 730 | Journal Of Intelligence Studies In Business Halmstad University / Unknown Publisher | 2001-015X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 731 | Journal Of Intelligence Studies In Business / Unknown Publisher | 2001-0168 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 732 | Cis Iron And Steel Review Ore And Metals Publishing House / Unknown Publisher | 2072-0815 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 733 | Cis Iron And Steel Review / Unknown Publisher | 2414-1089 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 734 | Disena Pontificia Universidad Catolica De Chile / Unknown Publisher | 0718-8447 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 735 | Activitas Nervosa Superior Rediviva Slovak Academy Of Sciences / Unknown Publisher | 1337-933X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 736 | Critica D Arte / CASA EDITRICE LE LETTERE | 0011-1511 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 737 | Iranian Journal Of Veterinary Science And Technology Ferdowsi University Of Mashhad / Unknown Publisher | 2008-465X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 738 | Schweizer Zeitschrift Fur Gynakologie Rosenfluh Publikationen / N°   ISSN   E-ISSN | 1661-0199 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 739 | Bautechnik / ERNST & SOHN | 0932-8351 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 740 | California History / CALIFORNIA HISTORICAL SOC | 0162-2897 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 741 | Human Rights Quarterly / JOHNS HOPKINS UNIV PRESS | 0275-0392 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 742 | Cultural Critique / UNIV MINNESOTA PRESS | 0882-4371 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 743 | Voprosy Onkologii Autonomous Non-Profit Scientific And Medical Organization / Unknown Publisher | 0507-3758 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 744 | Voprosy Onkologii / Unknown Publisher | 2949-4915 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 745 | Jurnal Infektologii  Interregional Public Organization Association Of Infectious  Disease Specialists Of Saint-Petersburg And Leningrad Region  (Ipo Aidsspbr) / Unknown Publisher | 2072-6732 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 746 | Mcb Molecular And Cellular Biomechanics Sin-Chn Scientific Press / Unknown Publisher | 1556-5297 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 747 | Z Badan Nad Ksiazka I Ksiegozbiorami Historycznymi University Of Warsaw / Unknown Publisher | 1897-0788 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 748 | Çocuk Ve Gençlik Ruh Sağlığı Dergisi / Turkish Journal Of Child And Adolescent Mental Health / Unknown Publisher | 1301-3904 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 749 | Turkish Journal Of Child And Adolescent Mental Health Galenos Publishing House / Unknown Publisher | 2687-3532 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 750 | Art-Sanat Dergisi Istanbul University Press / Unknown Publisher | 2148-3582 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 751 | Torture International Rehabilitation Council For Torture Victims / Unknown Publisher | 1018-8185 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 752 | Cryoletters / CRYO LETTERS | 0143-2044 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 753 | East Asian Journal Of Popular Culture Intellect Ltd. / Unknown Publisher | 2051-7084 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 754 | Dynamic Relationships Management Journal Slovenian Academy Of Management / Unknown Publisher | 2232-5867 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 755 | Journal Of Optimization, Differential Equations And Their  Applications Oles Honchar Dnipro National University / Unknown Publisher | 2617-0108 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 756 | Iranian Journal Of Information Processing Management Iranian Research Institute For Information Science And  Technology / Unknown Publisher | 2251-8223 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 757 | International Journal Of Standardization Research Igi Global Publishing / Unknown Publisher | 2470-8542 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 758 | Journal Fur Neurologie, Neurochirurgie Und Psychiatrie Krause Und Pachernegg Gmbh / Unknown Publisher | 1608-1587 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 759 | Banking And Finance Review School Of Business Central Connecticut State University / Unknown Publisher | 1947-6140 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 760 | Cigre Science And Engineering Cigre / Unknown Publisher | 2426-1335 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 761 | Fujita Medical Journal Fujita Medical Society / Unknown Publisher | 2189-7255 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 762 | Environmental Science &  Technology / AMER CHEMICAL SOC | 0013-936X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 763 | Bioresources / NORTH CAROLINA STATE UNIV DEPT  WOOD & PAPER SCI | 1930-2126 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 764 | Journal Of The History Of  Philosophy / JOHNS HOPKINS UNIV PRESS | 0022-5053 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 765 | Revista Espanola De Cirugia Ortopedica Y Traumatologia Ediciones Doyma, S.L. / Unknown Publisher | 1888-4415 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 766 | Revista Española De Cirugía Ortopédica Y Traumatología / Unknown Publisher | 2340-5392 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 767 | Credit And Capital Markets Duncker Und Humblot Gmbh / Unknown Publisher | 2199-1227 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 768 | Mm Science Journal Mm Science Journal / Unknown Publisher | 1803-1269 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 769 | Mm Science Journal / Unknown Publisher | 1805-0646 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 770 | Psiquiatría Biológica / Unknown Publisher | 1696-9138 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 771 | Urology Reports (St. Petersburg) Eco-Vector Llc / Unknown Publisher | 2225-9074 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 772 | Acta Cybernetica University Of Szeged, Institute Of Informatics / Unknown Publisher | 0324-721X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 773 | Acta Cybernetica / Unknown Publisher | 2676-993X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 774 | French Politics, Culture And Society Berghahn Journals / Unknown Publisher | 1537-6370 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 775 | Paediatric Surgery (Ukraine) Group Of Companies Med Expert, Llc / Unknown Publisher | 2304-0041 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 776 | International Journal Of Education Through Art Intellect Ltd. / Unknown Publisher | 1743-5234 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 777 | Zoophilologica Wydawnictwo Uniwersytetu Slaskiego / Unknown Publisher | 2451-3849 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 778 | Revista Guillermo De Ockham University Of San Buenaventura - Cali / Unknown Publisher | 1794-192X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 779 | International Journal Of Online Pedagogy And Course Design Igi Global Publishing / Unknown Publisher | 2155-6873 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 780 | Journal Of Contemporary Archaeology Equinox Publishing Ltd / Unknown Publisher | 2051-3429 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 781 | Croatian Journal Of Forest  Engineering / ZAGREB UNIV, FAC FORESTRY | 1845-5719 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 782 | Croatian Journal Of Forest Engineering / Unknown Publisher | 1848-9672 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 783 | International Journal For Research In Vocational Education And  Training  European Research Network Vocational Education And  Training / Unknown Publisher | 2197-8638 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 784 | Mongolian Geoscientist Mongolian University Of Science And Technology / Unknown Publisher | 2220-0622 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 785 | Historica (Ostrava) University Of Ostrava / Unknown Publisher | 1803-7550 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 786 | Indonesian Journal Of International And Comparative Law Institute For Migrant Rights Press / Unknown Publisher | 2338-770X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 787 | Malaysian Construction Research Journal Construction Research Institute Of Malaysia / Unknown Publisher | 2590-4140 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 788 | Harvard Civil Rights-Civil Liberties  Law Review / HARVARD LAW SCHOOL | 1943-5061 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 789 | Brazilian Journal Of Medical And  Biological Research / ASSOC BRAS DIVULG CIENTIFICA | 0100-879X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 790 | Revista Brasileira De  Epidemiologia Associacao Brasileira De Pos - Graduacao Em Saude Coletiva / Unknown Publisher | 1415-790X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 791 | Arthuriana / SCRIPTORIUM PRESS | 1078-6279 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 792 | Studies In Regional Science Japan Section Of The Regional Science Association  International / Unknown Publisher | 0287-6256 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 793 | Belleten / TURK TARIH KURUMU | 0041-4255 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 794 | Archipel-Etudes  Interdisciplinaires Sur Le Monde  Insulindien / ASSOC ARCHIPEL | 0044-8613 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 795 | Medicine, Conflict And Survival Routledge / Unknown Publisher | 1362-3699 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 796 | The Tocqueville Review/La Revue Tocqueville / Unknown Publisher | 1918-6649 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 797 | Italianist Maney Publishing / Unknown Publisher | 0261-4340 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 798 | International Journal Of The Economics Of Business Routledge / Unknown Publisher | 1357-1516 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 799 | Journal Of Environmental  Engineering And Landscape  Management / VILNIUS GEDIMINAS TECH UNIV | 1648-6897 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 800 | Turkish Archives Of Pediatrics Aves / Unknown Publisher | 2757-6256 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 801 | African Invertebrates / COUNCIL NATAL MUSEUM | 1681-5556 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 802 | Revista Espanola De Cardiologia Suplementos Ediciones Doyma, S.L. / Unknown Publisher | 1131-3587 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 803 | Hikma Ucopress. Editorial Universidad De Cordoba / Unknown Publisher | 1579-9794 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 804 | Social Work And Social Sciences Review Whiting And Birch / Unknown Publisher | 0953-5225 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 805 | Lcgc North America / MJH LIFE SCIENCES | 1527-5949 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 806 | New Design Ideas Jomard Publishing / Unknown Publisher | 2522-4875 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 807 | Ideology And Politics Journal Foundation For Good Politics / Unknown Publisher | 2227-6068 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 808 | Gastroenterology And Hepatology From Bed To Bench Shahid Beheshti Medical University / Unknown Publisher | 2008-4234 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 809 | Fundamental And Applied Mathematics Moscow State University / Unknown Publisher | 2076-6203 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 810 | Composites Theory And Practice Polish Society Of Composite Materials / Unknown Publisher | 2084-6096 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 811 | Journal Of Physics G-Nuclear And  Particle Physics / IOP PUBLISHING LTD | 0954-3899 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 812 | Journal Of Health Care For The  Poor And Underserved / JOHNS HOPKINS UNIV PRESS | 1049-2089 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 813 | Acta Societatis Botanicorum  Poloniae / POLSKIE TOWARZYSTWO  BOTANICZNE | 0001-6977 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 814 | Salud Publica De Mexico / INST NACIONAL SALUD PUBLICA | 0036-3634 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 815 | Practical Neurology Bmj Publishing Group / Unknown Publisher | 1474-7758 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 816 | Italian Culture Maney Publishing / Unknown Publisher | 0161-4622 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 817 | Journal Of King Saud University - Engineering Sciences / Unknown Publisher | 2213-1558 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 818 | Coluna/ Columna Oficial Da Sociedade Brasileira De Coluna / Unknown Publisher | 1808-1851 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 819 | Coluna/Columna / Unknown Publisher | 2177-014X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 820 | Journal Of Tea Science Editorial Office Of Journal Of Tea Science / Unknown Publisher | 1000-369X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 821 | Imaging Science In Dentistry Korean Academy Of Oral And Maxillofacial Radiology / Unknown Publisher | 2233-7822 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 822 | International Arab Journal Of Dentistry Saint Joseph University Of Beirut, Faculty Of Dental Medicine / Unknown Publisher | 2218-0885 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 823 | Zdravstveno Varstvo / INST PUBLIC HEALTH REPUBLIC  SLOVENIA | 0351-0026 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 824 | Proceedings Of The Ice - Engineering History And Heritage Ice Publishing / Unknown Publisher | 1757-9430 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 825 | Filozofski Vestnik / ZRC PUBLISHING | 0353-4510 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 826 | Journal Of Urban And Regional Analysis Bucharest University Press / Unknown Publisher | 2067-4082 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 827 | Ecocycles European Ecocycles Society / Unknown Publisher | 2416-2140 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 828 | Philosophy Kitchen University Of Torino / Unknown Publisher | 2385-1945 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 829 | Bibliothecae.It Universita Di Bologna, Dipartimento Di Beni Culturali, Alma  Mater Studiorum / Unknown Publisher | 2283-9364 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 830 | Journal Of The Indian Statistical Association Indian Statistical Association / Unknown Publisher | 0537-2585 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 831 | Applied Physics Express / IOP PUBLISHING LTD | 1882-0778 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 832 | Reviews In American History / JOHNS HOPKINS UNIV PRESS | 0048-7511 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 833 | Cahiers D'Etudes Africaines Cairn France / N°   ISSN   E-ISSN | 0008-0055 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 834 | Chinese Journal Of Endocrinology And Metabolism Chinese Medical Journals Publishing House Co.Ltd / Unknown Publisher | 1000-6699 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 835 | Industrial And Commercial Training / Unknown Publisher | 1758-5767 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 836 | Revue De Geographie Alpine- Journal Of Alpine Research / IGA-ASSOC DIFFUSION RECHERCHE  ALPINE | 0035-1121 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 837 | International Journal Of  Womens Health / DOVE MEDICAL PRESS LTD | 1179-1411 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 838 | Athenea Digital Universitat Autonoma De Barcelona / Unknown Publisher | 1578-8946 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 839 | International Journal Of Public Sector Management / Unknown Publisher | 1758-6666 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 840 | Zeitschrift Fur Germanistik / PETER LANG GMBH | 0323-7982 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 841 | Zeitschrift Für Germanistik / Unknown Publisher | 2235-1272 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 842 | Journal Of The Korean Society Of Surveying, Geodesy,  Photogrammetry And Cartography Korean Society Of Surveying / Unknown Publisher | 1598-4850 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 843 | Journal Of The Korean Society Of Surveying Geodesy Photogrammetry And Cartography / Unknown Publisher | 2288-260X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 844 | Sociologia Urbana E Rurale Francoangeli Edizioni / N°   ISSN   E-ISSN | 0392-4939 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 845 | Japan Journal Of Food Engineering Japan Society For Food Engineering / Unknown Publisher | 1345-7942 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 846 | Japan Journal Of Food Engineering / Unknown Publisher | 1884-5924 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 847 | Gorenie I Vzryv Torus Press Publishing House / N°   ISSN   E-ISSN | 2305-9117 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 848 | Asia-Pacific Journal Of Research In Early Childhood Education Pacific Early Childhood Education Research Association / Unknown Publisher | 1976-1961 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 849 | Chilean Journal Of Agricultural And Animal Sciences Universidad De Concepcion / Unknown Publisher | 0719-3882 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 850 | Nervno-Myshechnye Bolezni Abv-Press Publishing House / Unknown Publisher | 2222-8721 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 851 | Dynamics Of Asymmetric Conflict: Pathways Toward Terrorism  And Genocide Routledge / Unknown Publisher | 1746-7586 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 852 | Geographical Sciences Japanese Society For Geographical Sciences / Unknown Publisher | 0286-4886 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 853 | Polyolefins Journal Iran Polymer And Petrochemical Institute / Unknown Publisher | 2322-2212 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 854 | Review Of Economic Research On Copyright Issues Society For Economic Research On Copyright Issues / Unknown Publisher | 1698-1359 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 855 | Diabetologie Metabolismus Endokrinologie Vyziva Tigis Spol. S.R.O. / Unknown Publisher | 1212-6853 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 856 | Journal Of Physics B-Atomic  Molecular And Optical Physics / IOP PUBLISHING LTD | 0953-4075 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 857 | Universum Universidad De Talca / Unknown Publisher | 0716-498X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 858 | Journal Of Agro-Environment Science Editorial Board Of Journal Of Agro-Environment Science / Unknown Publisher | 1672-2043 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 859 | Journal Of Pain And Palliative Care Pharmacotherapy Informa Healthcare / Unknown Publisher | 1536-0288 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 860 | Scandinavian Studies / SOC ADVANCEMENT SCAND STUD | 0036-5637 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 861 | Russian Journal Of Pediatric Surgery, Anesthesia And Intensive  Care Eco-Vector Llc / Unknown Publisher | 2219-4061 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 862 | Korean Journal Of Medical Education Korean Society Of Medical Education / N°   ISSN   E-ISSN | 2005-727X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 863 | Revija Za Socijalnu Politiku / SVEUCLISTE ZAGREBU, PRAVNI  FAKULTED-UNIV ZAGREB, FAC LAW | 1330-2965 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 864 | Scandinavian Journal Of Urology / MEDICAL JOURNAL SWEDEN AB | 2168-1805 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 865 | Implicit Religion Equinox Publishing Ltd / Unknown Publisher | 1463-9955 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 866 | Acta Chiropterologica / MUSEUM & INST ZOOLOGY PAS- POLISH ACAD SCIENCES | 1508-1109 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 867 | Mathematical Modeling And Computing Lviv Polytechnic National University / N°   ISSN   E-ISSN | 2312-9794 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 868 | International Journal Of Construction Education And Research Routledge / Unknown Publisher | 1550-3984 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 869 | Sport Science University Of Travnik / Unknown Publisher | 1840-3662 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 870 | Global Media And China / Unknown Publisher | 2059-4364 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 871 | Geopolitica(S) Universidad Complutense Madrid / N°   ISSN   E-ISSN | 2172-3958 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 872 | Cesko-Slovenska Pediatrie Czech Medical Association J.E. Purkyne / Unknown Publisher | 0069-2328 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 873 | Animal Science And Food Technology National University Of Life And Environmental Sciences Of  Ukraine / Unknown Publisher | 2706-8331 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 874 | Review Of Computer Engineering Research Conscientia Beam / Unknown Publisher | 2410-9142 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 875 | Estudios De Fonetica Experimental Universitat De Barcelona / Unknown Publisher | 1575-5533 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 876 | Journal Of Mycology And Infection Korean Society For Medical Mycology / Unknown Publisher | 3058-423X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 877 | Trends In Phytochemical Research Islamic Azad University / Unknown Publisher | 2588-3623 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 878 | Gaojishu Tongxin/Chinese High Technology Letters Institute Of Scientific And Technical Information Of China / N°   ISSN   E-ISSN | 1002-0470 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 879 | Tidsskrift For Den Norske Legeforening Den Norske Legeforening / Unknown Publisher | 0029-2001 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 880 | Journal Of Chemical Information  And Modeling / AMER CHEMICAL SOC | 1549-9596 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 881 | Revista Medica De Chile / SOC MEDICA SANTIAGO | 0034-9887 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 882 | Gaceta Sanitaria / Unknown Publisher | 1697-8498 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 883 | Bioscience Journal Universidade Federal De Uberlandia / Unknown Publisher | 1516-3725 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 884 | Bioscience Journal / UNIV FEDERAL UBERLANDIA | 1981-3163 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 885 | Forum For Linguistic Studies Bilingual Publishing Group / Unknown Publisher | 2705-0602 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 886 | Turkish Journal Of Biology / TUBITAK SCIENTIFIC &  TECHNOLOGICAL RESEARCH  COUNCIL TURKEY | 1300-0152 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 887 | Kybernetika / KYBERNETIKA | 0023-5954 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 888 | Ocean Science Journal / KOREA INST OCEAN SCIENCE &  TECHNOLOGY-KIOST | 1738-5261 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 889 | Anesthesia Progress Allen Press Inc. / Unknown Publisher | 0003-3006 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 890 | Dissolution Technologies / DISSOLUTION TECHNOLOGIES, INC | 1521-298X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 891 | Slavic And East European Information Resources Routledge / Unknown Publisher | 1522-8886 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 892 | Althea Medical Journal University Of Padjadjaran Faculty Of Medicine / Unknown Publisher | 2337-4330 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 893 | Fuzzy Information And Engineering Tsinghua University Press / Unknown Publisher | 1616-8658 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 894 | International Journal Of Gaming And Computer-Mediated  Simulations Igi Global Publishing / Unknown Publisher | 1942-3888 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 895 | Journal Of African Cinemas Intellect Ltd. / Unknown Publisher | 1754-9221 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 896 | Applied Environmental Research Environmental Research Institute, Chulalongkorn University / N°   ISSN   E-ISSN | 2287-0741 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 897 | Jambura Journal Of Biomathematics Universitas Negeri Gorontalo / Unknown Publisher | 2723-0317 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 898 | Periodico Di Mineralogia / SAPIENZA UNIV EDITRICE | 0369-8963 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 899 | Cultural Perspectives Vasile Alecsandri University Of Bacau / Unknown Publisher | 1224-239X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 900 | International Journal Of High Risk Behaviors And Addiction Brieflands / Unknown Publisher | 2251-8711 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 901 | Engineering, Technology And Applied Science Research Dr D. Pylarinos / Unknown Publisher | 1792-8036 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 902 | Beijing Youdian Xueyuan Xuebao/Journal Of Beijing University  Of Posts And Telecommunications Beijing University Press / Unknown Publisher | 1000-5145 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 903 | Biomedical Reports Spandidos Publications / Unknown Publisher | 2049-9434 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 904 | Herzschrittmachertherapie Und Elektrophysiologie D. Steinkopff-Verlag / Unknown Publisher | 0938-7412 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 905 | Scientific And Technical Journal Of Information Technologies,  Mechanics And Optics Itmo University / Unknown Publisher | 2226-1494 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 906 | Sa Journal Of Industrial Psychology Aosis (Pty) Ltd / Unknown Publisher | 0258-5200 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 907 | International Journal Of Sociology / Unknown Publisher | 0020-7659 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 908 | Ankara Universitesi Eczacilik Fakultesi Dergisi University Of Ankara / Unknown Publisher | 1015-3918 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 909 | Teoria De La Educacion Universidad De Salamanca, Facultad De Educacion / Unknown Publisher | 1130-3743 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 910 | Estudos De Psicologia (Natal) Universidade Federal Do Rio Grande Do Norte / Unknown Publisher | 1413-294X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 911 | Comparative Migration Studies / Unknown Publisher | 2214-8590 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 912 | Journal Of Asia-Pacific Business Routledge / Unknown Publisher | 1059-9231 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 913 | Deturope Regional Science Association Of Subotica (Drustvo Za  Regionalne Nauke) / Unknown Publisher | 1821-2506 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 914 | Norwegian-American Studies University Of Minnesota Press / Unknown Publisher | 0078-1983 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 915 | International Tinnitus Journal International Tinnitus Journal / Unknown Publisher | 0946-5448 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 916 | Journal Of Skyscape Archaeology Equinox Publishing Ltd / Unknown Publisher | 2055-348X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 917 | Journal Of East Asian Cultures Eotvos Lorand Tudomanyegyetem / Unknown Publisher | 2060-9655 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 918 | European Journal Of Statistics Ada Academica / Unknown Publisher | 2806-0954 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 919 | Journal Of Dentistry For Children American Academy Of Pediatric Dentistry / Unknown Publisher | 1551-8949 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 920 | Journal Of Heat And Mass Transfer Research Semnan University, Center Of Excellence In Nonlinear Analysis  And Applications / Unknown Publisher | 2383-3068 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 921 | Archives Of Pathology &  Laboratory Medicine / COLL AMER PATHOLOGISTS | 0003-9985 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 922 | Journal Of Archaeological Science Reports / Unknown Publisher | 2352-4103 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 923 | Journal Of Electronic Imaging / SPIE-SOC PHOTO-OPTICAL  INSTRUMENTATION ENGINEERS | 1017-9909 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 924 | Applied Mathematics And Information Sciences Natural Sciences Publishing / Unknown Publisher | 1935-0090 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 925 | Logical Methods In Computer  Science / LOGICAL METHODS COMPUTER  SCIENCE E V | 1860-5974 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 926 | Rechtsgeschichte Klostermann / Unknown Publisher | 1619-4993 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 927 | Kesmas: Jurnal Kesehatan Masyarakat Nasional Universitas Indonesia, Faculty Of Public Health / Unknown Publisher | 1907-7505 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 928 | Asia-Pacific Journal Of Science And Technology Khon Kaen University,Research And Technology Transfer  Affairs Division / N°   ISSN   E-ISSN | 2539-6293 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 929 | Avances En Odontoestomatologia Ediciones Avances S.L. / Unknown Publisher | 0213-1285 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 930 | Avances En Odontoestomatología / Unknown Publisher | 2340-3152 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 931 | Carsologica Sinica Institute Of Karst Geology Of Chinese Academy Of Geology  Sciences / Unknown Publisher | 1001-4810 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 932 | Microbial Cell / SHARED SCIENCE PUBLISHERS OG | 2311-2638 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 933 | Clinical And Experimental Hepatology Termedia Publishing House Ltd. / Unknown Publisher | 2392-1099 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 934 | Facta Universitatis-Series  Mechanical Engineering / UNIV NIS | 0354-2025 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 935 | Articulo - Journal Of Urban Research Articulo - Journal Of Urban Research / Unknown Publisher | 1661-4941 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 936 | International Journal Of Islamic Thought Universiti Kebangsaan Malaysia Press / Unknown Publisher | 2232-1314 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 937 | Russian Journal Of Nonlinear Dynamics Institute Of Computer Science Izhevsk / Unknown Publisher | 2658-5316 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 938 | Notas Economicas Imprensa Da Universidade De Coimbra / N°   ISSN   E-ISSN | 0872-4733 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 939 | Journal Of Music, Technology And Education Intellect Ltd. / Unknown Publisher | 1752-7066 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 940 | Jordanian Journal Of Computers And Information Technology Scientific Research Support Fund Of Jordan / Unknown Publisher | 2413-9351 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 941 | Environmental Analysis Health And Toxicology Korean Society Of Environmental Health And Toxicology / Unknown Publisher | 2671-9525 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 942 | Curriculum Studies In Health And Physical Education Routledge / Unknown Publisher | 2574-2981 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 943 | Journal Of Islamic Law Institut Agama Islam Negeri Pontianak / Unknown Publisher | 2721-5032 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 944 | Bulgarian Historical Review- Revue Bulgare D Histoire / PUBL HOUSE BULGARIAN ACAD SCI | 0204-8906 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 945 | Studi Secenteschi / CASA EDITRICE LEO S OLSCHKI | 0081-6248 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 946 | Hippokratia / LITHOGRAPHIA | 1108-4189 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 947 | Mining Safety And Environmental Protection Editoral Office Of Mining Safety And Environmental Protection / Unknown Publisher | 1008-4495 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 948 | Drugs Of The Future Clarivate / Unknown Publisher | 0377-8282 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 949 | Przemysl Chemiczny / WYDAWNICTWO SIGMA-NOT SP  ZOO | 0033-2496 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 950 | Przemysł Chemiczny / Unknown Publisher | 2449-9951 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 951 | Bioscience Reports / PORTLAND PRESS LTD | 0144-8463 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 952 | Journal Of Robotics And Mechatronics Fuji Technology Press / Unknown Publisher | 0915-3942 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 953 | The Family Journal / Unknown Publisher | 1552-3950 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 954 | Mountain Research And  Development / INT MOUNTAIN SOC | 0276-4741 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 955 | Palaeoentomology Magnolia Press / Unknown Publisher | 2624-2826 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 956 | International Journal For Quality Research University Of Montenegro / N°   ISSN   E-ISSN | 1800-6450 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 957 | Esbocos Universidade Federal De Santa Catarina / Unknown Publisher | 1414-722X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 958 | Evidence-Based Practice In Child And Adolescent Mental Health Routledge / Unknown Publisher | 2379-4925 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 959 | Medica Jadertina Opca Bolnica Zadar / Unknown Publisher | 0351-0093 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 960 | Medica Jadertina / Unknown Publisher | 1848-817X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 961 | Archiwum Medycyny Sadowej I Kryminologii Polskie Towarzystwo Medycyny Sadowej I Kryminologii / Unknown Publisher | 0324-8267 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 962 | African Evaluation Journal Aosis (Pty) Ltd / Unknown Publisher | 2306-5133 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 963 | Pravara Medical Review Deemed University / Unknown Publisher | 0975-0533 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 964 | Jurnal Penelitian Kehutanan Wallacea Hasanuddin University Faculty Of Forestry / Unknown Publisher | 2302-299X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 965 | Biopesticides International Connect Journals / Unknown Publisher | 0973-483X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 966 | Quaderns De Filologia: Estudis Literaris Universitat De Valencia / Unknown Publisher | 1135-4178 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 967 | Critical Education Institute For Critical Education Studies / Unknown Publisher | 1920-4175 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 968 | Youth Voice Journal Rj4All Publications / Unknown Publisher | 2049-2073 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 969 | Aportes Schedas / Unknown Publisher | 2386-4850 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 970 | Archistor Universita Mediterranea Di Reggio Calabria / Unknown Publisher | 2384-8898 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 971 | Petrological Journal University Of Isfahan / Unknown Publisher | 2322-2182 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 972 | Journal Of The Korean Physical  Society / KOREAN PHYSICAL SOC | 0374-4884 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 973 | Journal Of Vacuum Science &  Technology B / A V S AMER INST PHYSICS | 2166-2746 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 974 | Revue De Musicologie / EDITIONS TRANSATLANTIQUES | 0035-1601 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 975 | Revue De Musicologie Societe Francaise De Musicologie / Unknown Publisher | 1958-5632 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 976 | Daedalus / MIT PRESS | 0011-5266 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 977 | Scalable Computing West University Of Timisoara / Unknown Publisher | 1895-1767 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 978 | Limnetica / ASOC ESPAN LIMNOL-MISLATA | 0213-8409 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 979 | Journal Of Park And Recreation Administration Sagamore Publishing Llc / Unknown Publisher | 0735-1968 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 980 | Kennedy Institute Of Ethics  Journal / JOHNS HOPKINS UNIV PRESS | 1054-6863 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 981 | Canadian Journal Of Latin American And Caribbean Studies / Revue Canadienne Des Études Latino-Américaines Et Caraïbes / Unknown Publisher | 2333-1461 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 982 | Black Camera Indiana University Press / Unknown Publisher | 1536-3155 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 983 | Journal Of Visual Communication In Medicine Informa Healthcare / Unknown Publisher | 1745-3054 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 984 | Novosti Sistematiki Nizshikh Rastenii Komarov Botanical Institute / Unknown Publisher | 0568-5435 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 985 | Novosti Sistematiki Nizshikh Rastenii / Unknown Publisher | 2713-2609 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 986 | Pharos Journal Of Theology Africa Journals / Unknown Publisher | 2414-3324 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 987 | Infectious Disease Modelling Keai Communications Co. / Unknown Publisher | 2468-0427 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 988 | Journal Of Occupational Therapy, Schools, And Early  Intervention Routledge / Unknown Publisher | 1941-1243 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 989 | Mississippi Quarterly / JOHNS HOPKINS UNIV PRESS | 0026-637X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 990 | Annals Of Economics And Finance / WUHAN UNIV JOURNALS PRESS | 1529-7373 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 991 | Getty Research Journal / GETTY RESEARCH INST | 1944-8740 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 992 | International Journal Of Fashion Studies Intellect Ltd. / Unknown Publisher | 2051-7106 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 993 | Nanomedicine Research Journal Tehran University Of Medical Sciences / Unknown Publisher | 2476-3489 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 994 | Zaranda De Ideas Asociacion De Arqueologos Profesionales De La Republica  Argentina / Unknown Publisher | 1853-1296 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 995 | Revista Cubana De Informacion En Ciencias De La Salud Centro Nacional De Informacion De Ciencias Medicas / Unknown Publisher | 2307-2113 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 996 | Trends In Carbohydrate Research Association Of Carbohydrate Chemists And Technologists / Unknown Publisher | 0975-0304 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 997 | Journal Of Central South  University / JOURNAL OF CENTRAL SOUTH UNIV | 2227-5223 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 998 | Reviews Of Modern Physics / AMER PHYSICAL SOC | 0034-6861 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 999 | Journal Of Zoo And Wildlife  Medicine / AMER ASSOC ZOO VETERINARIANS | 1042-7260 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1000 | Statistics / Unknown Publisher | 1026-7786 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1001 | International Journal For Housing Science And Its Applications International Association For Housing Science / Unknown Publisher | 0146-6518 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1002 | Bilgi Dunyasi University And Research Librarians Association, Ankara / Unknown Publisher | 1302-3217 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1003 | Bilgi Dünyası / Unknown Publisher | 2148-354X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1004 | Revista Brasileira De Educacao Especial Associacao Brasileira De Pesquisadores Em Educacao Especial / Unknown Publisher | 1413-6538 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1005 | Revista Brasileira De Educação Especial / Unknown Publisher | 1980-5470 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1006 | Cuadernos De Arte De La Universidad De Granada Editorial Universidad De Granada / Unknown Publisher | 0210-962X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1007 | Advances In Horticultural Science University Of Florence / Unknown Publisher | 0394-6169 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1008 | Journal Of Iberian And Latin American Research Routledge / Unknown Publisher | 1326-0219 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1009 | Journal Of Symplectic Geometry / INT PRESS BOSTON, INC | 1527-5256 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1010 | Aniki: Portuguese Journal Of The Moving Image Association Of Moving Image Researchers (Aim) / Unknown Publisher | 2183-1750 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1011 | European Journal Of Mental Health Semmelweis University Institute Of Mental Health / Unknown Publisher | 1788-4934 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1012 | Cuadernos.Info Pontificia Universidad Catolica De Chile / N°   ISSN   E-ISSN | 0719-3661 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1013 | Imago - Revista De Emblematica Y Cultura Visual University Of Valencia / Unknown Publisher | 2171-0147 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1014 | Hawaii Journal Of Health And Social Welfare University Health Partners Of Hawaii / Unknown Publisher | 2641-5216 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1015 | Peuce Institutul De Cercetari Eco-Muzeale (Icem) Tulcea / Unknown Publisher | 0258-8102 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1016 | Peuce. / Unknown Publisher | 2734-7427 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1017 | Arya Atherosclerosis Isfahan Cardiovascular Research Center / Unknown Publisher | 1735-3955 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1018 | Salud(I)Ciencia Sociedad Iberoamericana De Informacion Cientifica / Unknown Publisher | 1667-8982 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1019 | Journal Of Advances In Medical Education And Professionalism Shriaz University Of Medical Sciences / Unknown Publisher | 2322-2220 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1020 | Japanese Journal Of Lung Cancer Japan Lung Cancer Society / Unknown Publisher | 0386-9628 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1021 | Haigan / Unknown Publisher | 1348-9992 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1022 | Biopolymers And Cell National Academy Of Sciences Of Ukraine / Unknown Publisher | 0233-7657 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1023 | Nonlinear Analysis-Modelling  And Control / VILNIUS UNIV, INST MATHEMATICS  & INFORMATICS | 1392-5113 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1024 | International Journal Of  Precision Engineering And  Manufacturing-Green  Technology / KOREAN SOC PRECISION ENG | 2198-0810 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1025 | Main Group Chemistry / Unknown Publisher | 1026-7581 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1026 | Clean Air Journal National Association Of Clean Air / Unknown Publisher | 1017-1703 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1027 | Aus Universidad Austral De Chile / Unknown Publisher | 0718-204X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1028 | Monographs In Oral Science / Unknown Publisher | 1662-3843 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1029 | Journal Of Integrated Coastal Zone Management Aprh (Associacao Portuguesa Dos Recursos Hidricos) / Unknown Publisher | 1646-8872 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1030 | Revista De  Investigacion En Educacion Universidade De Vigo - Facultad De Ciencias De La Educacion Y  Del Deporte / Unknown Publisher | 1697-5200 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1031 | Europa Xxi Insitute Of Geography And Spatial Organization Polish  Academy Of Sciences / Unknown Publisher | 1429-7132 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1032 | Geoloski Anali Balkanskoga Poluostrva University Of Belgrade / Unknown Publisher | 0350-0608 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1033 | Jazz Education In Research And Practice Indiana University Press / Unknown Publisher | 2639-7668 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1034 | Word And Text Petroleum-Gas University Of Ploiesti / Unknown Publisher | 2069-9271 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1035 | Litera (Turkey) Istanbul University Press / Unknown Publisher | 1304-0057 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1036 | Kedi Journal Of Educational  Policy / KOREAN EDUCATIONAL  DEVELOPMENTAL INST | 1739-4341 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1037 | Psicologia Sociale Il Mulino Publishing House / N°   ISSN   E-ISSN | 1827-2517 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1038 | Journal Of Virology / Unknown Publisher | 1070-6321 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1039 | Epilepsia / Unknown Publisher | 1528-1157 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1040 | Russian Chemical Reviews / ND ZELINSKY INST ORGANIC  CHEMISTRY, RAS - ZIOC RAS | 0036-021X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1041 | Agricultural Engineering/Inżynieria Rolnicza / Unknown Publisher | 1429-7264 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1042 | Empan Editions Eres / Unknown Publisher | 1152-3336 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1043 | Empan / Unknown Publisher | 1776-2812 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1044 | Annales Scientifiques De L Ecole  Normale Superieure / SOC MATHEMATIQUE FRANCE | 0012-9593 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1045 | Ai Magazine / AMER ASSOC ARTIFICIAL INTELL | 0738-4602 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1046 | Philosophy And Literature / JOHNS HOPKINS UNIV PRESS | 0190-0013 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1047 | Journal Of Postgraduate Medical Institute Postgraduate Medical Institute / Unknown Publisher | 1013-5472 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1048 | Journal Of Engineering Sciences Assiut University, Faculty Of Engineering / Unknown Publisher | 1687-0530 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1049 | Aula Abierta Universidad De Oviedo / Unknown Publisher | 0210-2773 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1050 | Accounting Education Routledge / Unknown Publisher | 0963-9284 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1051 | Northern Scotland Centre For Scottish Studies, University Of Aberdeen / Unknown Publisher | 0306-5278 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1052 | Northern Scotland / Unknown Publisher | 2042-2717 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1053 | South African Journal For  Research In Sport Physical  Education And Recreation / STELLENBOSCH UNIV | 0379-9069 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1054 | South African Journal For Research In Sport, Physical Education  And Recreation North-West Unversity / Unknown Publisher | 2960-2386 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1055 | Recherche Et Pratiques Pedagogiques En Langues De Specialite -  Cahiers De L'Apliut  Association Des Professeurs De Langues Des Instituts  Universitaires De Technologie (Apliut) / Unknown Publisher | 2119-5242 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1056 | Revista Geografica Venezolana Universidad De Los Andes / Unknown Publisher | 1012-1617 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1057 | Muziki Routledge / Unknown Publisher | 1753-593X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1058 | International Journal Of Medical Parasitology And Epidemiology  Sciences Aras Part Medical International Press / Unknown Publisher | 2766-6492 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1059 | Journal Of Bodies, Sexualities, And Masculinities Berghahn Journals / Unknown Publisher | 2688-8149 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1060 | Landfall / UNIV OTAGO PRESS | 0023-7930 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1061 | Journal Of Current Science And Technology Rangsit University / Unknown Publisher | 2630-0583 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1062 | Journal Of Contemporary Social Sciences And Humanities / Unknown Publisher | 2985-055X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1063 | Lusitania Sacra Universidade Catolica Portuguesa, Centro De Estudos De  Historia Religiosa / Unknown Publisher | 2182-8822 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1064 | Aut Journal Of Modeling And Simulation Amirkabir University Of Technology / Unknown Publisher | 2588-2961 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1065 | Archivos De Zootecnia Ucopress. Editorial Universidad De Cordoba / Unknown Publisher | 0004-0592 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1066 | Issues In Accounting Education American Accounting Association / Unknown Publisher | 0739-3172 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1067 | Journal Of Gastrointestinal And  Liver Diseases / MEDICAL UNIV PRESS | 1841-8724 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1068 | Mekhatronika, Avtomatizatsiya, Upravlenie New Technologies Publishing House / Unknown Publisher | 1684-6427 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1069 | Annals Of The Polish Association Of Agricultural And Agribusiness  Economists The Association Of Agriculture And Agribusiness Economists / Unknown Publisher | 2657-781X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1070 | Cooperativismo E Economia Social Faculty Of Legal Sciences And Labor, University Of Vigo / Unknown Publisher | 1130-2682 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1071 | Journal Of Feminist Family Therapy Routledge / Unknown Publisher | 0895-2833 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1072 | Archivos De Prevencion Riesgos Laborales Academy Of Medical And Health Sciences Of Catalonia And The  Balearic Islands / Unknown Publisher | 1138-9672 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1073 | Journal Of The Japan Epilepsy Society Japan Epilepsy Society / Unknown Publisher | 0912-0890 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1074 | Bradleya / BRITISH CACTUS & SUCCULENT SOC | 0265-086X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1075 | Signo Y Pensamiento Pontificia Universidad Javeriana / Unknown Publisher | 0120-4823 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1076 | Transactions Of Famena / UNIV ZAGREB FAC MECHANICAL  ENGINEERING & NAVAL  ARCHITECTURE | 1333-1124 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1077 | Transactions Of Famena University Of Zagreb / Unknown Publisher | 1849-1391 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1078 | Acta Zoologica Bulgarica / INST ZOOLOGY, BAS | 0324-0770 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1079 | International Journal Of Interdisciplinary Social And Community Common Ground Research Networks / N°   ISSN   E-ISSN   Studies | 2324-7576 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1080 | Amha - Acta Medico-Historica Adriatica Croatian Scientific Society For The History Of Health / Unknown Publisher | 1334-4366 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1081 | Acta Medico-Historica Adriatica / Unknown Publisher | 1334-6253 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1082 | Plasma Physics And Technology Czech Technical University / Unknown Publisher | 2336-2626 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1083 | Journal Of Verification, Validation And Uncertainty  Quantification The American Society Of Mechanical Engineers(Asme) / Unknown Publisher | 2377-2158 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1084 | Topics In Linguistics / Unknown Publisher | 1337-7590 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1085 | Topics In Linguistics Univerzita Konstantina Filozofa V Nitre / Unknown Publisher | 2199-6504 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1086 | Journal Of Central Banking Law And Institutions Bank Indonesia Institute / Unknown Publisher | 2809-9885 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1087 | Engineering Geology And Hydrogeology Geological Institute “Strashimir Dimitrov”, Bulgarian Academy  Of Sciences / Unknown Publisher | 0204-7934 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1088 | Farmaceuticos Comunitarios Sociedad Espanola De Farmacia Clinica Familiar Y Comunitaria / Unknown Publisher | 1885-8619 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1089 | Shanghai Jiaotong Daxue Xuebao/Journal Of Shanghai Jiaotong  University Shanghai Jiaotong University / Unknown Publisher | 1006-2467 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1090 | Genes & Development / COLD SPRING HARBOR LAB PRESS,  PUBLICATIONS DEPT | 0890-9369 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1091 | Turkish Journal Of Medical  Sciences / TUBITAK SCIENTIFIC &  TECHNOLOGICAL RESEARCH  COUNCIL TURKEY | 1300-0144 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1092 | Journal Of Animal And Plant  Sciences-Japs / PAKISTAN AGRICULTURAL  SCIENTISTS FORUM | 1018-7081 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1093 | Czech Journal Of Food Sciences / CZECH ACADEMY AGRICULTURAL  SCIENCES | 1212-1800 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1094 | South African Journal Of Physiotherapy Aosis (Pty) Ltd / N°   ISSN   E-ISSN | 0379-6175 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1095 | Allergy, Asthma And Clinical Immunology Biomed Central Ltd / Unknown Publisher | 1710-1484 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1096 | Obrazovanie I Nauka Russian State Vocational Pedagogical University / Unknown Publisher | 1994-5639 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1097 | Journal De Theorie Des Nombres  De Bordeaux / UNIV BORDEAUX, INST  MATHEMATIQUES BORDEAUX | 1246-7405 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1098 | Revista Brasileira De Cineantropometria E Desempenho  Humano Universidade Federal De Santa Catarina / Unknown Publisher | 1415-8426 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1099 | Studies In African Linguistics University Of Florida Press / Unknown Publisher | 0039-3533 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1100 | Egyptian Journal Of Ear, Nose, Throat And Allied Sciences Egyptian Society Of Ear Nose Throat And Allied Sciences / Unknown Publisher | 2090-0740 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1101 | Clinica Y Salud / COLEGIO OFICIAL PSICOLOGOS  MADRID | 1130-5274 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1102 | Journal Of Tropical Biodiversity And Biotechnology Universitas Gadjah Mada, Faculty Of Biology / Unknown Publisher | 2540-9573 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1103 | Archiwum Historii Filozofii I Mysli Spolecznej Wydawnictwo Instytutu Filozofii I Socjologii Polskiej Akademii  Nauk / Unknown Publisher | 0066-6874 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1104 | Journal Of Oncological Science Turkiye Klinikleri / Unknown Publisher | 2452-3364 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1105 | Journal Of Open Humanities Data Ubiquity Press / N°   ISSN   E-ISSN | 2059-481X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1106 | Ocean And Coastal Research / INST OCEANOGRAFICO, UNIV SAO  PAULO | 2675-2824 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1107 | Journal Of Conchology / CONCHOLOGICAL SOC GREAT  BRITAIN & IRELAND | 2755-3531 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1108 | American Journal Of Veterinary  Research / AMER VETERINARY MEDICAL ASSOC | 0002-9645 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1109 | British Journal Of Oral &  Maxillofacial Surgery / CHURCHILL LIVINGSTONE | 0266-4356 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1110 | Eastern-European Journal Of Enterprise Technologies Technology Center / Unknown Publisher | 1729-3774 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1111 | Han-Guk Hyeonmigyeong Hakoeji/Applied Microscopy / Unknown Publisher | 2234-6198 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1112 | Empiria Universidad Nacional De Educacion A Distancia (Uned) / Unknown Publisher | 1139-5737 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1113 | Revista Catalana De Dret Públic / Unknown Publisher | 1885-5709 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1114 | Revista Catalana De Dret Public Public Administration School Of Catalonia / Unknown Publisher | 1885-8252 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1115 | International Studies In Sociology Of Education Routledge / Unknown Publisher | 0962-0214 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1116 | Performance Measurement And Metrics / Unknown Publisher | 1758-6925 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1117 | Studia Z Filologii Polskiej I Slowianskiej Polish Academy Of Sciences, Institute Of Slavic Studies / Unknown Publisher | 0081-7090 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1118 | South Asian Diaspora Routledge / Unknown Publisher | 1943-8184 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1119 | Journal Of Islamic Monetary Economics And Finance Bank Indonesia Institute / Unknown Publisher | 2460-6146 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1120 | Clinical And Experimental Morphology Mdv Group / Unknown Publisher | 2226-5988 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1121 | Heritage And Sustainable Development Research And Development Academy / Unknown Publisher | 2712-0554 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1122 | Utrecht Journal Of International And European Law Ubiquity Press / Unknown Publisher | 2053-5341 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1123 | Music Theory And Analysis Leuven University Press / Unknown Publisher | 2295-5917 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1124 | Nuclear Analysis Keai Publishing Communications Ltd. / Unknown Publisher | 2773-1839 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1125 | Nanjing Youdian Daxue Xuebao (Ziran Kexue Ban)/Journal Of  Nanjing University Of Posts And Telecommunications (Natural  Science)  Journal Of Nanjing Institute Of Posts And Telecommunications / Unknown Publisher | 1673-5439 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1126 | Ermeneutica Letteraria Fabrizio Serra Editore / Unknown Publisher | 1827-8957 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1127 | Chinese Journal Of Endemiology Chinese Medical Journals Publishing House Co.Ltd / N°   ISSN   E-ISSN | 2095-4255 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1128 | Educational Leadership / ASSOC SUPERVISION CURRICULUM  DEVELOPMENT | 0013-1784 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1129 | Mathematical Research Letters / INT PRESS BOSTON, INC | 1073-2780 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1130 | Neoplasma / AEPRESS SRO | 0028-2685 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1131 | Metallofizika I Noveishie Tekhnologii G.V. Kurdyumov Institute For Metal Physics Of N.A.S. Of  Ukraine / N°   ISSN   E-ISSN | 1024-1809 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1132 | Journal Of Medical Investigation University Of Tokushima / N°   ISSN   E-ISSN | 1343-1420 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1133 | Russian Sociological Review National Research University Higher School Of Economics / Unknown Publisher | 1728-192X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1134 | Journal Of Tropical Forest  Science / FOREST RESEARCH INST MALAYSIA | 0128-1283 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1135 | Philologia Hispalensis Universidad De Sevilla / Unknown Publisher | 1132-0265 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1136 | Novosti Khirurgii Vitebsk State Medical University / Unknown Publisher | 1993-7512 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1137 | Analitika I Kontrol Ural Federal University / Unknown Publisher | 2073-1442 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1138 | Journal Of The Asabe / AMER SOC AGRICULTURAL &  BIOLOGICAL ENGINEERS | 2769-3287 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1139 | Boletin De Arqueologia Pucp Pontificia Universidad Católica Del Perú / Unknown Publisher | 1029-2004 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1140 | Revista De Poetica Medieval Alcala University / Unknown Publisher | 1137-8905 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1141 | Chinese Journal Of Hematology Chinese Medical Journals Publishing House Co.Ltd / Unknown Publisher | 0253-2727 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1142 | European Oral Research Istanbul University Press / Unknown Publisher | 2630-6158 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1143 | Shodoznavstvo A. Yu. Krymskyi Institute Of Oriental Studies Of The National  Academy Of Sciences Of Ukraine / Unknown Publisher | 1682-671X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1144 | Journal Of Food Quality And Hazards Control Shahid Sadoughi University Of Medical Sciences / Unknown Publisher | 2345-6825 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1145 | Journal Of Neurocritical Care / Unknown Publisher | 2005-0348 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1146 | Journal Of Neurocritical Care Korean Neurocritical Care Society / Unknown Publisher | 2508-1349 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1147 | Revista De Teledeteccion Universidad Politecnica De Valencia / Unknown Publisher | 1133-0953 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1148 | Water Cycle Keai Communications Co. / Unknown Publisher | 2666-4453 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1149 | International Journal Of Economics And Management Universiti Putra Malaysia / Unknown Publisher | 1823-836X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1150 | International Journal Of Economics And Management / Unknown Publisher | 2600-9390 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1151 | Literaturna Misal Institute For Literature, Bulgarian Academy Of Sciences / Unknown Publisher | 0324-0495 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1152 | Transport Findings Findings Press / Unknown Publisher | 2652-0397 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1153 | Journal Of Sport For Development Journal Of Sport For Development / Unknown Publisher | 2330-0574 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1154 | Business And Professional Ethics Journal Philosophy Documentation Center / Unknown Publisher | 0277-2027 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1155 | Studia Theologica-Czech Republic / UNIV PALACKEHO OLOMOUCI | 1212-8570 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1156 | Novos Estudos Cebrap Centro Brasileiro De Analise E Planejamento / Unknown Publisher | 0101-3300 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1157 | Acta Scientiarum Language And Culture Universidade Estadual De Maringa / Unknown Publisher | 1983-4675 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1158 | Brazilian Journal Of Veterinary Pathology Brazilian Association Of Veterinary Pathology / Unknown Publisher | 1983-0246 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1159 | World Academy Of Sciences Journal Spandidos Publications / Unknown Publisher | 2632-2900 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1160 | Asia Pacific Journal Of Mathematics Asia Pacific Academic / Unknown Publisher | 2357-2205 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1161 | Archivum Mathematicum Masarykova Universita / Unknown Publisher | 0044-8753 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1162 | Iranian Journal Of Toxicology Arak University Of Medical Sciences / Unknown Publisher | 2008-2967 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1163 | Biblica Et Patristica Thoruniensia Uniwersytet Mikolaja Kopernika / Unknown Publisher | 1689-5150 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1164 | Fronteiras (Brazil) Federal University Of Fronteira Sul / Unknown Publisher | 1415-8701 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1165 | State Crime Journal Pluto Journals / Unknown Publisher | 2046-6056 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1166 | State Crime Journal / Unknown Publisher | 2046-6064 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1167 | Turkiye Klinikleri Pediatri Ortadogu Reklam Tanitim Yayincilik Turizm Egitim Insaat  Sanayi Ve Ticaret A.S. / Unknown Publisher | 2146-8990 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1168 | International Journal Of Science, Mathematics And Technology  Learning Common Ground Research Networks / Unknown Publisher | 2327-7971 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1169 | Neuphilologische Mitteilungen / MODERN LANGUAGE SOC | 2736-9714 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1170 | European Food And Feed Law Review Lexxion / Unknown Publisher | 1862-2720 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1171 | Asian Myrmecology / UNIV MALAYSIA SABAH | 1985-1944 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1172 | International Journal Of Research In Industrial Engineering Ayandegan Institute Of Higher Education / Unknown Publisher | 2783-1337 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1173 | Avant Scene Opera / AVANT-SCENE OPERA | 0295-1371 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1174 | Journal Of Veterinary Parasitology Indian Association For The Advancement Of Veterinary  Parasitology / Unknown Publisher | 0971-1031 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1175 | Journal Of Photopolymer Science  And Technology / TECHNICAL ASSOC  PHOTOPOLYMERS,JAPAN | 0914-9244 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1176 | Tobacco Induced Diseases / EUROPEAN PUBLISHING | 1617-9625 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1177 | Experimental And Clinical  Transplantation / BASKENT UNIV | 2146-8427 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1178 | Revue D Etudes Comparatives Est- Ouest / PRESSES UNIV FRANCE | 0338-0599 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1179 | Polar Research / OPEN ACADEMIA AB | 0800-0395 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1180 | Kiva Routledge / Unknown Publisher | 0023-1940 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1181 | International Journal Of Marine  And Coastal Law / MARTINUS NIJHOFF PUBL | 0927-3522 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1182 | Pachyderm / IUCN-SSC ASIAN ELEPHANT  SPECIALIST GROUP | 1026-2881 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1183 | Journal Of Engineering Design And Technology / Unknown Publisher | 1758-8901 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1184 | Journal Of Nephropharmacology Society Of Diabetic Nephropathy Prevention / Unknown Publisher | 2345-4202 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1185 | Journal Of Korean Academy Of Nursing Administration Korean Academy Of Nursing Administration / Unknown Publisher | 1225-9330 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1186 | Opera Historica University Of South Bohemia / Unknown Publisher | 1805-790X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1187 | Canadian Journal Of Health History / Unknown Publisher | 2816-6469 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1188 | Skase Journal Of Translation And Interpretation Slovak Association For The Study Of English / Unknown Publisher | 1336-7811 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1189 | Competition Policy International Competition Policy International Inc. / Unknown Publisher | 1554-0189 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1190 | Shengwu Yixue Gongchengxue Zazhi/Journal Of Biomedical  Engineering  West China Hospital, Sichuan Institute Of Biomedical  Engineering / Unknown Publisher | 1001-5515 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1191 | Annals Of Medicine Informa Healthcare / Unknown Publisher | 1651-2219 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1192 | Revista Medica Electronica Editorial Ciencias Medicas / Unknown Publisher | 1684-1824 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1193 | Journal Of Theoretical And Applied Mechanics/Mechanika Teoretyczna I Stosowana / Unknown Publisher | 0079-3701 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1194 | Journal Of Theoretical And  Applied Mechanics / POLISH SOC THEORETICAL &  APPLIED MECHANICS | 1429-2955 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1195 | Acta Agrobotanica Polish Botanical Society / Unknown Publisher | 0065-0951 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1196 | Polish Journal Of Food And  Nutrition Sciences / INST ANIMAL REPRODUCTION &  FOOD RESEARCH POLISH ACAD  SCIENCES OLSZTYN | 1230-0322 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1197 | Investigacion Y Educacion En Enfermeria Facultad De Enfermeria De La Universidad De Antioquia / Unknown Publisher | 0120-5307 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1198 | Silniki Spalinowe/Combustion Engines / Unknown Publisher | 0138-0346 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1199 | Combustion Engines Polish Scientific Society Of Combustion Engines / Unknown Publisher | 2300-9896 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1200 | Physical Oceanography Marine Hydrophysical Institute Of Ras / Unknown Publisher | 0928-5105 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1201 | South African Journal Of  Industrial Engineering / SOUTHERN AFRICAN INST  INDUSTRIAL ENGINEERING | 1012-277X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1202 | Applied Mathematics And Mechanics Editorial Office Of Applied Mathematics And Mechanics / Unknown Publisher | 1000-0887 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1203 | Hkie Transactions Hong Kong Institution Of Engineers Hong Kong Institution Of Engineers / Unknown Publisher | 1023-697X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1204 | Hkie Transactions / Unknown Publisher | 2326-3733 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1205 | Research In Post-Compulsory Education Routledge / Unknown Publisher | 1359-6748 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1206 | Gema Online Journal Of Language Studies Penerbit Universiti Kebangsaan Malaysia / Unknown Publisher | 1675-8021 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1207 | Popular Communication Routledge / Unknown Publisher | 1540-5702 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1208 | Journal Of Risk / INCISIVE MEDIA | 1465-1211 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1209 | Materiali Per Una Storia Della Cultura Giuridica Societa Editrice Il Mulino / Unknown Publisher | 1120-9607 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1210 | Materiali Per Una Storia Della Cultura Giuridica / Unknown Publisher | 2612-209X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1211 | Art, Design And Communication In Higher Education Intellect Ltd. / Unknown Publisher | 1474-273X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1212 | Suranaree Journal Of Social Science Suranaree University Of Technology / Unknown Publisher | 2651-088X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1213 | Mineralia Slovaca State Geological Institute Of Dionyz Stur (Bratislava) / Unknown Publisher | 0369-2086 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1214 | Mineralia Slovaca / Unknown Publisher | 1338-3523 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1215 | Alfred Nobel University Journal Of Philology Alfred Nobel University / Unknown Publisher | 3041-217X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1216 | New Zealand Veterinary Journal / Unknown Publisher | 1176-0702 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1217 | Dental Update George Warman Publications / Unknown Publisher | 0305-5000 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1218 | Dental Update / Unknown Publisher | 2515-589X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1219 | Bmj Open Quality Bmj Publishing Group / Unknown Publisher | 2399-6641 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1220 | Euphrosyne-Revista De Filologia  Classica / BREPOLS PUBL | 0870-0133 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1221 | Korean Journal Of Pain / KOREAN PAIN SOC | 2005-9159 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1222 | Diacritics-A Review Of  Contemporary Criticism / JOHNS HOPKINS UNIV PRESS | 0300-7162 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1223 | Revista De Salud Publica Universidad Nacional De Colombia / Unknown Publisher | 0124-0064 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1224 | World Leisure Journal / Unknown Publisher | 0441-9057 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1225 | International Journal Of Cardiovascular Sciences Sociedade Brasileira De Cardiologia / Unknown Publisher | 2359-4802 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1226 | Folia Malacologica Association Of Polish Malacologists / Unknown Publisher | 1506-7629 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1227 | Anaesthesia, Pain And Intensive Care Faculty Of Anaesthesia, Pain And Intensive Care, Afms / Unknown Publisher | 1607-8322 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1228 | Pediatria I Medycyna Rodzinna Medical Communications / Unknown Publisher | 1734-1531 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1229 | Pediatria I Medycyna Rodzinna / Unknown Publisher | 2391-5021 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1230 | Kemas Universitas Negeri Semarang / N°   ISSN   E-ISSN | 1858-1196 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1231 | Studia Poliana / Unknown Publisher | 1139-6660 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1232 | Studia Poliana Servicio De Publicaciones De La Universidad De Navarra / Unknown Publisher | 2387-1830 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1233 | Ukrainian Geographical Journal Publishing House Akademperiodyka / Unknown Publisher | 1561-4980 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1234 | Rehabilitace A Fyzikalni Lekarstvi Czech Medical Association J.E. Purkyne / Unknown Publisher | 1211-2658 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1235 | Revista Do Instituto Historico E Geografico Do Rio Grande Do Sul Historical And Geographical Institute Of Rio Grande Do Sul / Unknown Publisher | 1678-3484 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1236 | Journal Of Epigraphic Studies Fabrizio Serra Editore Srl / Unknown Publisher | 2611-979X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1237 | New English Teacher Theodore Maria School Of Arts, Assumption University / Unknown Publisher | 1905-7725 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1238 | Gynakologische Praxis Mediengruppe Oberfranken - Fachverlage Gmbh & Co. Kg / Unknown Publisher | 2198-1701 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1239 | Interpretation-A Journal Of  Political Philosophy / INTERPRETATION, INC | 0020-9635 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1240 | Indian Journal Of Animal Sciences / INDIAN COUNC AGRICULTURAL RES | 0367-8318 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1241 | The Indian Journal Of Animal Sciences / Unknown Publisher | 2394-3327 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1242 | Revista Mexicana De Ciencias Agricolas National Institute Of Forestry, Agricultural And Livestock  Research / Unknown Publisher | 2007-0934 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1243 | Gigiena I Sanitariya Federal Scientific Center Of Hygiene Named After Ff Erisman / Unknown Publisher | 0016-9900 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1244 | Elements / MINERALOGICAL SOC AMER | 1811-5209 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1245 | Allergology International / JAPANESE SOC ALLERGOLOGY | 1323-8930 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1246 | Journal Of Disaster Research Fuji Technology Press / Unknown Publisher | 1881-2473 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1247 | Jmv-Journal De Médecine Vasculaire / Unknown Publisher | 2542-4521 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1248 | Journal Of Ecumenical Studies / JOURNAL ECUMENICAL STUDIES | 0022-0558 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1249 | Journal Of Physical And Chemical Reference Data / Unknown Publisher | 1546-5969 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1250 | Ciudades / Unknown Publisher | 1133-6579 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1251 | Ciudades Instituto Universitario De Urbanistica De La Universidad De  Valladolid / Unknown Publisher | 2445-3943 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1252 | Ichnos/Ichnos : An International Journal For Plant And Animal Traces / Unknown Publisher | 1026-7999 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1253 | Journal Of Oral Research Universidad De Concepcion / Unknown Publisher | 0719-2460 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1254 | Functiones Et Approximatio, Commentarii Mathematici Adam Mickiewicz University / Unknown Publisher | 0208-6573 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1255 | Turkish Journal Of Surgery Turkish Surgical Society / Unknown Publisher | 2564-6850 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1256 | Rozhledy V Chirurgii Czech Medical Association J.E. Purkyne / Unknown Publisher | 0035-9351 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1257 | International Journal Of Informatics And Communication  Technology Intelektual Pustaka Media Utama / Unknown Publisher | 2252-8776 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1258 | Journal Of The Botanical Research Institute Of Texas Botanical Research Institute Of Texas Inc. / Unknown Publisher | 1934-5259 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1259 | Journal Of The Botanical Research Institute Of Texas / Unknown Publisher | 2644-1608 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1260 | Thought-A Journal Of Philosophy / PHILOSOPHY DOCUMENTATION  CENTER | 2161-2234 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1261 | Agronomia Colombiana Universidad Nacional De Colombia / Unknown Publisher | 0120-9965 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1262 | Geodesy And Cartography Vilnius Gediminas Technical University / Unknown Publisher | 2029-6991 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1263 | Logos: Revista De Linguistica, Filosofia Y Literatura Universidad De La Serena,Departamento De Artes Y Letras / Unknown Publisher | 0716-7520 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1264 | Samarah Universitas Islam Negeri Ar-Raniry / Unknown Publisher | 2549-3132 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1265 | International Journal Of Ageing And Later Life Linkoping University Electronic Press / Unknown Publisher | 1652-8670 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1266 | Folia Cryptogamica Estonica Estonian Naturalists' Society / Unknown Publisher | 1406-2070 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1267 | Korean Journal Of Chemical  Engineering / KOREAN INSTITUTE CHEMICAL   ENGINEERS | 0256-1115 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1268 | Superconductor Science &  Technology / IOP PUBLISHING LTD | 0953-2048 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1269 | Journal Of Speech Language And  Hearing Research / AMER SPEECH-LANGUAGE-HEARING  ASSOC | 1092-4388 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1270 | Applied Ecology And  Environmental Research / ALOKI APPLIED ECOLOGICAL  RESEARCH AND FORENSIC INST LTD | 1589-1623 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1271 | Giornale Italiano Di Cardiologia Cepi S.R.L. / Unknown Publisher | 1827-6806 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1272 | Journal Of Experimental Zoology India Dr. P. R. Yadav / Unknown Publisher | 0972-0030 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1273 | Scienceasia / SCIENCE SOCIETY THAILAND | 1513-1874 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1274 | Medical News Of North Caucasus Stavropol State Medical University / Unknown Publisher | 2073-8137 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1275 | Communications - Scientific Letters Of The University Of Zilina University Of Zilina / Unknown Publisher | 2585-7878 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1276 | Rehabilitacion Ediciones Doyma, S.L. / Unknown Publisher | 0048-7120 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1277 | Xibei Gongye Daxue Xuebao/Journal Of Northwestern  Polytechnical University Northwestern Polytechnical University / Unknown Publisher | 1000-2758 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1278 | Xibei Gongye Daxue Xuebao/Journal Of Northwestern Polytechnical University / Unknown Publisher | 2609-7125 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1279 | Transactions Of Japanese Society For Medical And Biological  Engineering Japanese Society For Medical And Biological Engineering / Unknown Publisher | 1347-443X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1280 | Brazilian Journal Of Oral Sciences Universidade Estadual De Campinas / Unknown Publisher | 1677-3217 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1281 | Revista Espanola De Drogodependencias Associacion Espanola De Estudio En Drogodependencias / Unknown Publisher | 0213-7615 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1282 | Revista Española De Drogodependencias / Unknown Publisher | 2341-1759 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1283 | Drugs In Context Bioexcel Publishing Ltd. / Unknown Publisher | 1740-4398 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1284 | International Journal Of Literary Humanities Common Ground Research Networks / Unknown Publisher | 2327-7912 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1285 | @Grh Association Francophone De Gestion Des Relations Humaines / Unknown Publisher | 2034-9130 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1286 | Peace And Conflict Studies Network Of Peace And Conflict Studies / Unknown Publisher | 1082-7307 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1287 | Journal Of The History Of Analytical Philosophy University Of Victoria / Unknown Publisher | 2159-0303 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1288 | Austral Journal Of Veterinary  Sciences / UNIV AUSTRAL CHILE, FAC CIENCIAS  VETERINARIAS | 0719-8000 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1289 | Tiyatro Elestirmenligi Ve Dramaturji Bolumu Dergisi Istanbul University Press / Unknown Publisher | 2687-4636 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1290 | Acta Pharmaceutica Sciencia Istanbul Medipol University / N°   ISSN   E-ISSN | 1307-2080 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1291 | Journal Of Stratigraphy And Sedimentology Researches University Of Isfahan / Unknown Publisher | 2008-7888 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1292 | Pediatrics / AMER ACAD PEDIATRICS | 0031-4005 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1293 | Brazilian Journal Of Biology Instituto Internacional De Ecologia / Unknown Publisher | 1519-6984 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1294 | Zygon / OPEN LIBRARY HUMANITIES | 0591-2385 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1295 | Media Asia / Unknown Publisher | 2377-6277 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1296 | Journal Of The American  Mosquito Control Association / AMER MOSQUITO CONTROL ASSOC | 1943-6270 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1297 | Journal Of Occupational Science / Unknown Publisher | 2158-1576 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1298 | Journal Of Structured Finance Portfolio Management Research / Unknown Publisher | 1551-9783 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1299 | Journal Of Horticultural Sciences Society For Promotion Of Horticulture / Unknown Publisher | 0973-354X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1300 | Geologija Geological Survey Of Slovenia / Unknown Publisher | 0016-7789 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1301 | Journal Of Hiv/Aids And Social Services Routledge / Unknown Publisher | 1538-1501 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1302 | Rig Kulturhistorisk Tidskrift Foreningen For Svensk Kulturhistoria / Unknown Publisher | 0035-5267 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1303 | Rig / Unknown Publisher | 2002-3863 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1304 | Schole Novosibirskij Gosudarstvennyj Universitet / Unknown Publisher | 1995-4328 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1305 | Ethical Thought Ras Institute Of Philosophy / Unknown Publisher | 2074-4870 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1306 | Universal Journal Of Mathematics And Applications Emrah Evren Kara / Unknown Publisher | 2619-9653 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1307 | Clinical Transplantation And Research Korean Society For Transplantation / Unknown Publisher | 3022-6783 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1308 | Notizie Di Politeia Politeia / Unknown Publisher | 1128-2401 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1309 | Yankuang Ceshi Science China Press / Unknown Publisher | 0254-5357 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1310 | Revista Cubana De Educacion Medica Superior Editorial Ciencias Medicas / Unknown Publisher | 0864-2141 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1311 | Journal Of Roman Archaeology Journal Of Roman Archaeology L.L.C. / Unknown Publisher | 1063-4304 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1312 | Ausa Patronat D'Estudis Osonencs / Unknown Publisher | 2014-1246 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1313 | Mechanics Of Advanced Composite Structures Semnan University, Faculty Of Mechanical Engineering / Unknown Publisher | 2423-4826 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1314 | Argumenta University Of Sassari / Unknown Publisher | 2465-2334 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1315 | Journal Of High Energy Physics / Unknown Publisher | 1126-6708 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1316 | American Family Physician / AMER ACAD FAMILY PHYSICIANS | 0002-838X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1317 | Estudos Avancados Instituto De Estudos Avancados Da Universidade De Sao Paulo / Unknown Publisher | 0103-4014 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1318 | Journal De Mycologie Medicale / MASSON EDITEUR | 1156-5233 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1319 | Turkish Journal Of Mathematics / TUBITAK SCIENTIFIC &  TECHNOLOGICAL RESEARCH  COUNCIL TURKEY | 1300-0098 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1320 | Journal Of Wine Research Routledge / N°   ISSN   E-ISSN | 0957-1264 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1321 | Journal Of Social Work Practice In The Addictions Routledge / Unknown Publisher | 1533-256X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1322 | Journal Of Social Work Practice In The Addictions / Unknown Publisher | 1533-2578 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1323 | Revista De Economia Mundial / UNIV HUELVA, SERV  PUBLICACIONES | 1576-0162 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1324 | Pakistan Journal Of Phytopathology Pakistan Phytopathological Society / Unknown Publisher | 1019-763X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1325 | Forum Geografi Muhammadiyah University Of Surakarta / Unknown Publisher | 0852-0682 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1326 | Per Linguam Department Of General Linguistics, Stellenbosch University / Unknown Publisher | 0259-2312 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1327 | Mongolian Studies Kalmyk Scientific Centre Of Russian Academy Of Sciences / Unknown Publisher | 2500-1523 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1328 | Journal Of Tropical Crop Science Ipb University Department Of Agronomy And Horticulture / Unknown Publisher | 2356-0169 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1329 | The Southern African Journal Of Entrepreneurship And Small Business Management / Unknown Publisher | 1015-3977 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1330 | Southern African Journal Of Entrepreneurship And Small  Business Management Aosis (Pty) Ltd / Unknown Publisher | 2071-3185 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1331 | Jahr University Of Rijeka, Faculty Of Medicine / N°   ISSN   E-ISSN | 1847-6376 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1332 | Tapa Johns Hopkins University Press / Unknown Publisher | 2575-7180 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1333 | Logi / Unknown Publisher | 1804-3216 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1334 | Town And Regional Planning University Of The Free State / Unknown Publisher | 1012-280X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1335 | Croatian Economic Survey Institute Of Economics (Zagreb) / Unknown Publisher | 1330-4860 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1336 | Ancient Asia Arf India / Unknown Publisher | 2042-5937 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1337 | Pamatky Archeologicke / ACAD SCIENCES CZECH REP, INST  ARCHAEOLOGY | 0031-0506 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1338 | Antiqvorvm Philosophia Fabrizio Serra Editore Srl / N°   ISSN   E-ISSN | 1973-5030 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1339 | Zhongguo Dianji Gongcheng Xuebao/Proceedings Of The  Chinese Society Of Electrical Engineering Chinese Society For Electrical Engineering / Unknown Publisher | 0258-8013 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1340 | Geology / GEOLOGICAL SOC AMER, INC | 0091-7613 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1341 | Journal Of World Trade / KLUWER LAW INT | 1011-6702 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1342 | Kodai Mathematical Journal / INST SCIENCE TOKYO, DEPT  MATHEMATICS | 0386-5991 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1343 | Kodai Mathematical Journal Tokyo Institute Of Technology / Unknown Publisher | 1881-5472 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1344 | Harvard Educational Review / HARVARD GRADUATE SCHOOL  EDUCATION | 0017-8055 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1345 | Journal Of Oral And Maxillofacial Surgery Medicine And Pathology / Unknown Publisher | 2212-5566 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1346 | Economy Of Regions Institute Of Economics, The Ural Branch Of Russian Academy Of  Sciences / Unknown Publisher | 2072-6414 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1347 | Miznarodnij Endokrinologicnij Zurnal Zaslavsky Publishing House / Unknown Publisher | 2224-0721 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1348 | Archives Of Suicide Research / Unknown Publisher | 1573-8159 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1349 | Journal Of Pediatric Neurosciences / Unknown Publisher | 1998-3948 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1350 | Sleep Medicine Clinics W.B. Saunders / N°   ISSN   E-ISSN | 1556-407X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1351 | Filolog (Banja Luka) Faculty Of Philology Banja Luka / Unknown Publisher | 1986-5864 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1352 | Childhood And Philosophy State Univ Of Rio De Janeiro - Center Of Childhood And  Philosophy Studies / Unknown Publisher | 1984-5987 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1353 | Heart International Touch Medical Media / Unknown Publisher | 1826-1868 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1354 | Aatcc Review / AMER ASSOC TEXTILE CHEMISTS  COLORISTS-AATCC | 1532-8813 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1355 | Statistika Czech Statistical Office / Unknown Publisher | 0322-788X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1356 | Extreme Medicine Federal Medical Biological Agency Publishing Group / Unknown Publisher | 2713-2757 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1357 | Iranian Journal Of Otorhinolaryngology Mashhad University Of Medical Sciences / Unknown Publisher | 2251-7251 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1358 | British Journal Of Hospital  Medicine / MA HEALTHCARE LTD | 1750-8460 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1359 | Mathematical Biosciences And Engineering American Institute Of Mathematical Sciences / Unknown Publisher | 1547-1063 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1360 | Allergologia Et  Immunopathologia / CODON PUBLICATIONS | 0301-0546 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1361 | Iawa Journal - Ku Leuven/Iawa Journal / Unknown Publisher | 2294-1924 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1362 | Acta Anatomica Sinica Editorial Board Of Acta Anatomica Sinica / Unknown Publisher | 0529-1356 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1363 | Emergencias / SOC ESPANOLA MEDICINA  URGENCIAS & EMERGENCIAS- SEMES | 1137-6821 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1364 | Teoria Y Realidad Constitucional Univ Nacional De Educacion A Distancia (Uned) / Unknown Publisher | 1139-5583 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1365 | International Forum Of Psychoanalysis Routledge / Unknown Publisher | 0803-706X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1366 | Iranian Journal Of Pediatrics / BRIEFLANDS | 2008-2142 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1367 | Journal Of Science-Advanced  Materials And Devices / VIETNAM NATL UNIV | 2468-2179 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1368 | Clinical And Investigative  Medicine / CANADIAN SOC CLINICAL  INVESTIGATION | 0147-958X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1369 | Revista De La Educacion Superior Asociacion Nacional De Universidades E Instituciones De  Educacion Superior A.C / Unknown Publisher | 0185-2760 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1370 | Rassegna Italiana Di Sociologia Sociologia Editrice Il Mulino / Unknown Publisher | 0486-0349 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1371 | Rassegna Italiana Di Sociologia / Unknown Publisher | 2612-1433 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1372 | Patologiya Krovoobrashcheniya I Kardiokhirurgiya Meshalkin National Medical Research Center / Unknown Publisher | 1681-3472 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1373 | Journal Of Internet Commerce Routledge / Unknown Publisher | 1533-2861 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1374 | Researches In Mathematics Oles Honchar Dnipro National University / Unknown Publisher | 2664-4991 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1375 | Archivos De Historia Del Movimiento Obrero Y La Izquierda Centro De Estudios Historicos De Los Trabajadores Y Las  Izquierdas / Unknown Publisher | 2313-9749 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1376 | Journal Of Geometric Mechanics American Institute Of Mathematical Sciences / Unknown Publisher | 1941-4889 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1377 | Organizations And Markets In Emerging Economies Vilnius University Press / Unknown Publisher | 2029-4581 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1378 | International Journal Of Design In Society Common Ground Research Networks / Unknown Publisher | 2325-1328 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1379 | Journal Of Islamic And Muslim Studies Indiana University Press / Unknown Publisher | 2470-7066 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1380 | Constitutional Review  Center For Research And Case Analysis And Library  Management Of The Constitutional Court Of The Republic Of  Indonesia / Unknown Publisher | 2460-0016 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1381 | International Journal Of Climate Change: Impacts And  Responses Common Ground Research Networks / Unknown Publisher | 2833-4140 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1382 | Studi Emigrazione Centro Studi Emigrazione / Unknown Publisher | 0039-2936 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1383 | Journal Of Coatings Technology And Research / Unknown Publisher | 2168-8028 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1384 | African Journal Of Reproductive  Health / WOMENS HEALTH & ACTION  RESEARCH CENTRE | 2141-3606 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1385 | Sulla Via Del Catai Centro Studi Martino Martini / Unknown Publisher | 1970-3449 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1386 | Studii Si Cercetari Fliologice, Seria Limbi Romanice Editura Universitatea Din Pitesti / Unknown Publisher | 2344-4851 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1387 | Angle Orthodontist / E H ANGLE EDUCATION RESEARCH  FOUNDATION, INC | 0003-3219 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1388 | Vox Patrum John Paul Ii Catholic University Of Lublin / N°   ISSN   E-ISSN | 0860-9411 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1389 | Revue D'Ethique Et De Theologie Morale Editions Du Cerf / N°   ISSN   E-ISSN | 1266-0078 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1390 | Jordan Medical Journal The University Of Jordan / Unknown Publisher | 0446-9283 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1391 | Jordan Medical Journal / Unknown Publisher | 2664-8091 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1392 | Nashim Indiana University Press / Unknown Publisher | 0793-8934 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1393 | Journal Of Punjab Academy Of Forensic Medicine And Toxicology Punjab Academy Of Forensic Medicine And Toxicology / Unknown Publisher | 0972-5687 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1394 | Praktyka Teoretyczna University Of Wroclaw / Unknown Publisher | 2081-8130 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1395 | Banking Law Journal Sheshunoff Information Services / Unknown Publisher | 0005-5506 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1396 | The Banking Law Journal / Unknown Publisher | 2381-3512 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1397 | Journal Of Urban And Environmental Engineering Universidade Federal Da Paraiba / Unknown Publisher | 1982-3932 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1398 | Short Film Studies Intellect Ltd. / Unknown Publisher | 2042-7824 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1399 | Manusya Chulalongkorn University / Unknown Publisher | 0859-9920 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1400 | Potato Journal The Indian Potato Association / Unknown Publisher | 0970-8235 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1401 | Bid Universitat De Barcelona / Unknown Publisher | 1575-5886 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1402 | Atom Indonesia National Nuclear Energy Agency / Unknown Publisher | 0126-1568 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1403 | Jurnal Kajian Bali Udayana University / Unknown Publisher | 2088-4443 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1404 | Uum Journal Of Legal Studies Universiti Utara Malaysia Press / Unknown Publisher | 0127-9483 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1405 | Asiaintervention Europa Group / Unknown Publisher | 2426-3958 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1406 | Lurralde: Investigacion Y Espacio Instituto Geografico Vasco Andres De Urdaneta / Unknown Publisher | 0211-5891 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1407 | Yiyong Shengwu Lixue/Journal Of Medical Biomechanics Editorial Department Of Journal Of Shanghai Second Medical  University / N°   ISSN   E-ISSN | 1004-7220 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1408 | Amphibian & Reptile Conservation / AMPHIBIAN CONSERVATION  RESEARCH CENTER & LAB | 1083-446X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1409 | Naihuo Cailiao/Refractories Institute Of Refractories Research / Unknown Publisher | 1001-1935 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1410 | Mathematics And Computational Sciences Qom University Of Technology / Unknown Publisher | 2717-2708 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1411 | Revista General De Derecho Constitucional Iustel / Unknown Publisher | 1886-6212 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1412 | Journal Of Philosophical Investigations University Of Tabriz / Unknown Publisher | 2423-4419 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1413 | Anales Del Instituto De Investigaciones Esteticas Universidad Nacional Autonoma De Mexico / Unknown Publisher | 0185-1276 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1414 | Egyptian Journal Of Histology Egyptian Society Of Histology And Cytology / Unknown Publisher | 1110-0559 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1415 | Medicina Interna De Mexico Comunicaciones Cientificas Mexicanas S.A. De C.V. / Unknown Publisher | 0186-4866 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1416 | Rhodora / NEW ENGLAND BOTANICAL CLUB  INC | 0035-4902 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1417 | Gulf Journal Of Mathematics Canadian University Of Dubai / Unknown Publisher | 2309-4966 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1418 | Journal Of Web Librarianship Routledge / Unknown Publisher | 1932-2909 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1419 | Acta Microbiologica Sinica Acta Microbiologica Sinica Editorial Office / Unknown Publisher | 0001-6209 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1420 | Suvremena Lingvistika Croatian Philological Society / Unknown Publisher | 0586-0296 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1421 | Suvremena Lingvistika / Unknown Publisher | 1847-117X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1422 | Ariel-A Review Of International  English Literature / JOHNS HOPKINS UNIV PRESS | 0004-1327 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1423 | Revista Brasileira De  Ensino De Fisica Sociedade Brasileira De Fisica / Unknown Publisher | 0102-4744 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1424 | Zeitschrift Fur Franzosische  Sprache Und Literatur / FRANZ STEINER VERLAG GMBH | 0044-2747 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1425 | Medicina Y Laboratorio Universidad De Antioquia / N°   ISSN   E-ISSN | 0123-2576 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1426 | Journal Of The American Musical Instrument Society American Musical Instrument Society / Unknown Publisher | 0362-3300 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1427 | Japan Review International Research Center For Japanese Studies / Unknown Publisher | 2434-3129 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1428 | Versus Societa Editrice Il Mulino / Unknown Publisher | 2612-0909 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1429 | Journal Of The Society For Asian Humanities Australian Society For Asian Humanities / Unknown Publisher | 2653-0848 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1430 | Chinese Journal On Internet Of Things Beijing Xintong Media Co., Ltd. / Unknown Publisher | 2096-3750 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1431 | Journal Of The Mathematical  Society Of Japan / MATH SOC JAPAN | 0025-5645 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1432 | Journal Of The Mathematical Society Of Japan / Unknown Publisher | 1881-1167 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1433 | International Journal Of Productivity And Performance Management / Unknown Publisher | 1758-6658 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1434 | Innovar Universidad Nacional De Colombia / N°   ISSN   E-ISSN | 0121-5051 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1435 | Quaternaire / SOC GEOLOGIQUE FRANCE | 1142-2904 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1436 | Asian Ethnicity Routledge / Unknown Publisher | 1463-1369 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1437 | Quality Assurance And Safety Of  Crops & Foods / CODON PUBLICATIONS | 1757-8361 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1438 | Revista De La Union Matematica  Argentina / UNION MATEMATICA ARGENTINA | 0041-6932 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1439 | Mathematical Proceedings Of The Royal Irish Academy Royal Irish Academy / Unknown Publisher | 1393-7197 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1440 | Digital Diagnostics Eco-Vector Llc / Unknown Publisher | 2712-8490 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1441 | Digital Education Review Universitat De Barcelona / Unknown Publisher | 2013-9144 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1442 | Regional Anesthesia And Acute Pain Management Eco-Vector Llc / Unknown Publisher | 1993-6508 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1443 | Exceptionality Education International Scholarship At Western / Unknown Publisher | 1918-5227 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1444 | Notas Sobre Mamiferos Sudamericanos Sarem Sociedad Argentina Para El Estudio De Los Mamiferos / Unknown Publisher | 2618-4788 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1445 | Studies In Ancient Art And Civilization Ksiegarnia Akademicka Publishing Ltd / Unknown Publisher | 1899-1548 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1446 | Historia Social Fundacion Instituto De Historia Social / Unknown Publisher | 0214-2570 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1447 | Historia Social / Unknown Publisher | 3020-6286 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1448 | Georgian Medical News Georgian Association Of Business Press / Unknown Publisher | 1512-0112 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1449 | Current Research In Social Psychology University Of Iowa / Unknown Publisher | 1088-7423 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1450 | Argumenta Philosophica Herder Editorial / Unknown Publisher | 2462-5906 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1451 | Aquaculture Science Japanese Society For Aquaculture Research, Nishimura  Toushadou Ltd. / Unknown Publisher | 2185-0194 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1452 | Pasaa Chulalongkorn University Language Institute / Unknown Publisher | 0125-2488 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1453 | Revista De Saude Publica / REVISTA DE SAUDE PUBLICA | 0034-8910 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1454 | Chinese Journal Of Microecology Editorial Office Of Chinese Journal Of Microecology / Unknown Publisher | 1005-376X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1455 | Dix-Septieme Siecle / SOC ETUD 17 SIECLE | 0012-4273 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1456 | Environmental Epidemiology Wolters Kluwer Health / Unknown Publisher | 2474-7882 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1457 | Brazilian Journal Of Nephrology Sociedade Brasileira De Nefrologia / N°   ISSN   E-ISSN | 0101-2800 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1458 | Preventive Nutrition And Food Science Korean Society Of Food Science And Nutrition / Unknown Publisher | 2287-1098 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1459 | Revue D'Histoire Des Sciences Cairn France / Unknown Publisher | 0151-4105 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1460 | Manufacturing Letters Society Of Manufacturing Engineers / Unknown Publisher | 2213-8463 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1461 | Ambiente E Sociedade Universidade Estadual De Campinas / Unknown Publisher | 1414-753X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1462 | Ambiente & Sociedade / Unknown Publisher | 1809-4422 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1463 | Zhurnal Mikrobiologii Epidemiologii I Immunobiologii Central Research Institute For Epidemiology / Unknown Publisher | 0372-9311 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1464 | Revista Facultad De Medicina Universidad Nacional De Colombia / Unknown Publisher | 0120-0011 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1465 | Research Involvement And Engagement Biomed Central Ltd / Unknown Publisher | 2056-7529 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1466 | Wallace Stevens Journal Johns Hopkins University Press / Unknown Publisher | 0148-7132 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1467 | The Wallace Stevens Journal / Unknown Publisher | 2160-0570 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1468 | Journal Of Cerebrovascular And Endovascular Neurosurgery Korean Society Of Cerebrovascular Surgeons (Kscvs) / N°   ISSN   E-ISSN | 2234-8565 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1469 | Wounds-A Compendium Of  Clinical Research And Practice / H M P COMMUNICATIONS | 1044-7946 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1470 | Dicenda Universidad Complutense Madrid / Unknown Publisher | 0212-2952 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1471 | Dicenda Estudios De Lengua Y Literatura Españolas / Unknown Publisher | 1698-2460 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1472 | Biomedical Photonics Russian Photodynamic Association / Unknown Publisher | 2413-9432 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1473 | Sound Studies Routledge / Unknown Publisher | 2055-1959 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1474 | Infectious Diseases And Immunity Wolters Kluwer Health / Unknown Publisher | 2096-9511 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1475 | Canadian Journal Of European And Russian Studies Carleton University - Centre For European Studies / N°   ISSN   E-ISSN | 2562-8429 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1476 | Global Transitions Keai Communications Co. / Unknown Publisher | 2589-7918 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1477 | Studia Iuridica Cassoviensia Pavol Jozef Safarik University In Kosice Faculty Of Law / Unknown Publisher | 1339-3995 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1478 | Fabriksoftware Gito Verlag / Unknown Publisher | 2569-7692 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1479 | Tradition And Modernity In Veterinary Medicine Faculty Of Veterinary Medicine, University Of Forestry / Unknown Publisher | 2534-9341 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1480 | Harvard Law Review / HARVARD LAW REV ASSOC | 0017-811X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1481 | Wit Transactions On Ecology And The Environment Witpress / Unknown Publisher | 1743-3541 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1482 | Journal Of Micromechanics And  Microengineering / IOP PUBLISHING LTD | 0960-1317 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1483 | Folia Pharmacologica Japonica Japanese Pharmacological Society / Unknown Publisher | 0015-5691 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1484 | Egyptian Journal Of Chemistry Nidoc (Nat.Inform.Document.Centre) / Unknown Publisher | 0449-2285 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1485 | Middle East Journal / MIDDLE EAST INST | 0026-3141 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1486 | Revista De  Administracao Publica Fundacao Getulio Vargas / Unknown Publisher | 0034-7612 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1487 | Journal Of Ship Research / SOC NAVAL ARCHITECTS & MARINE  ENGINEERS | 0022-4502 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1488 | Public Health And Life Environment Federal Center For Hygiene And Epidemiology / Unknown Publisher | 2219-5238 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1489 | Ibom Medical Journal Nigerian Medical Association, Akwa Ibom State Branch / Unknown Publisher | 2735-9964 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1490 | Earth Sciences Research Journal / UNIV NACIONAL DE COLOMBIA | 1794-6190 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1491 | Journal Of African Media Studies / INTELLECT LTD | 1751-7974 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1492 | Journal Of The Institute Of Image Electronics Engineers Of Japan Institute Of Image Electronics Engineers Of Japan / Unknown Publisher | 0285-9831 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1493 | Anthropological Journal Of European Cultures Berghahn Journals / Unknown Publisher | 1755-2923 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1494 | Boyhood Studies Berghahn Journals / Unknown Publisher | 2375-9240 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1495 | Aloma Facultat De Psicologia, Ciencies De L'Educacio I De L'Esport  Blanquerna / Unknown Publisher | 1138-3194 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1496 | Psychoterapia Polish Psychiatric Association / Unknown Publisher | 0239-4170 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1497 | Psychoterapia / Unknown Publisher | 2391-5862 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1498 | Patristica Et Mediaevalia Institute Of Philosophy Dr. Alejandro Korn, Faculty Of  Philosophy And Arts, University Of Buenos Aires / N°   ISSN   E-ISSN | 0325-2280 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1499 | Latin American Legal Studies Universidad Adolfo Ibanez / Unknown Publisher | 0719-9104 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1500 | Musik Und Kirche / BARENREITER-VERLAG | 0027-4771 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1501 | International Journal Of Esthetic Dentistry Quintessenz Verlags-Gmbh / Unknown Publisher | 2198-591X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1502 | Journal Of The Canadian Dental  Association / CANADIAN DENTAL ASSOC | 1488-2159 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1503 | Stomatologija Ausra / Unknown Publisher | 1392-8589 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1504 | Theoretical Biology Forum / FABRIZIO SERRA EDITORE | 2283-7175 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1505 | Cristianesimo Nella Storia Societa Editrice Il Mulino / N°   ISSN   E-ISSN | 2612-2227 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1506 | Biologia Plantarum / ACAD SCIENCES CZECH REPUBLIC,  INST EXPERIMENTAL BOTANY | 0006-3134 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1507 | Bmb Reports / KOREAN SOCIETY BIOCHEMISTRY &  MOLECULAR BIOLOGY | 1976-6696 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1508 | International Journal Of Learning, Teaching And Educational  Research Society For Research And Knowledge Management / Unknown Publisher | 1694-2116 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1509 | Practica Otologica, Supplement Society Of Practical Otolaryngology / Unknown Publisher | 0912-1870 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1510 | Practica Oto-Rhino-Laryngologica Suppl / Unknown Publisher | 2185-1557 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1511 | Cahiers Du Monde Russe Editions Ehess: Ecole Des Hautes Etudes En Sciences Sociales / Unknown Publisher | 1252-6576 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1512 | California Agriculture / UNIV CALIFORNIA, OAKLAND,  DIVISION AGRICULTURE & NATURAL  RESOURCES | 0008-0845 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1513 | Vestnik Volgogradskogo Gosudarstvennogo Universiteta, Seriia  4: Istoriia, Regionovedenie, Mezhdunarodnye Otnosheniia Volgograd State University / Unknown Publisher | 1998-9938 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1514 | Allelopathy Journal International Allelopathy Foundation / Unknown Publisher | 0971-4693 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1515 | Allelopathy Journal / Unknown Publisher | 0973-5046 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1516 | Journal Of Asia-Pacific Biodiversity National Science Museum Od Korea / Unknown Publisher | 2287-884X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1517 | Environment And History / WHITE HORSE PRESS | 0967-3407 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1518 | Asclepio-Revista De Historia De La  Medicina Y De La Ciencia / CONSEJO SUPERIOR  INVESTIGACIONES CIENTIFICAS-CSIC | 0210-4466 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1519 | Analise Psicologica Instituto Superior De Psicologia Aplicada / Unknown Publisher | 0870-8231 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1520 | Análise Psicológica / Unknown Publisher | 1646-6020 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1521 | Cultura, Ciencia Y Deporte Universidad Catolica San Antonio Murcia / Unknown Publisher | 1696-5043 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1522 | Cultura Ciencia Y Deporte / Unknown Publisher | 1989-7413 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1523 | Perinola-Revista De Investigacion  Quevediana / UNIV NAVARRA, SERVICIO  PUBLICACIONES | 1138-6363 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1524 | La Perinola / Unknown Publisher | 2254-6359 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1525 | International Journal Of Automotive Engineering Society Of Automotive Engineers Of Japan Inc / Unknown Publisher | 2185-0984 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1526 | Aquatic Sciences And Engineering Istanbul University Faculty Of Aquatic Sciences / Unknown Publisher | 2602-473X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1527 | Serangga Penerbit Universiti Kebangsaan Malaysia / Unknown Publisher | 1394-5130 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1528 | Bmj Surgery, Interventions, And Health Technologies Bmj Publishing Group / Unknown Publisher | 2631-4940 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1529 | Miscellanea Hadriatica Et Mediterranea University Of Zadar / Unknown Publisher | 1849-0670 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1530 | Vie Et Milieu-Life And  Environment / OBSERVATOIRE OCEANOLOGIQUE  BANYULS | 0240-8759 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1531 | Tobacco Science And Technology Editorial Office Of Tobacco Science And Technology / Unknown Publisher | 1002-0861 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1532 | Thammasat Review Thammasat University / Unknown Publisher | 2630-0303 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1533 | Journal Of Food And Nutrition  Research / VUP FOOD RESEARCH INST,  BRATISLAVA | 1338-4260 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1534 | Rusi Journal Routledge / Unknown Publisher | 0307-1847 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1535 | Current Opinion In Otolaryngology & Head & Neck Surgery / Unknown Publisher | 1080-8086 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1536 | Canadian Pharmacists Journal Canadian Pharmacists Association / Unknown Publisher | 1715-1635 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1537 | Canadian Pharmacists Journal / Revue Des Pharmaciens Du Canada / Unknown Publisher | 1913-701X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1538 | Food Processing: Techniques And Technology Kemerovo State University / Unknown Publisher | 2074-9414 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1539 | Urology Times Advanstar Communications Inc. / Unknown Publisher | 0093-9722 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1540 | Revue Internationale De  Philosophie / REVUE INT PHILOSOPHIE | 0048-8143 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1541 | Literatura Y Linguistica Universidad Catolica Silva Henriquez / Unknown Publisher | 0716-5811 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1542 | Literatura Y Lingüística / Unknown Publisher | 0717-621X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1543 | Journal Of The Turkish German Gynecology Association Galenos Publishing House / Unknown Publisher | 1309-0380 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1544 | Decision Science Letters Growing Science / Unknown Publisher | 1929-5804 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1545 | Rla Universidad De Concepcion / Unknown Publisher | 0033-698X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1546 | Rla-Revista De Linguistica Teorica  Y Aplicada / UNIV CONCEPCION, FAC  HUMANIDADES ARTE | 0718-4883 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1547 | Critical Inquiry In Language Studies Routledge / Unknown Publisher | 1542-7587 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1548 | Malaysian Journal Of Syariah And Law Faculty Of Syariah And Law, Islamic Science University Of  Malaysia (Usim) / Unknown Publisher | 1985-7454 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1549 | Maternal-Fetal Medicine Wolters Kluwer Health / Unknown Publisher | 2096-6954 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1550 | Biophysics Reports Science China Press / Unknown Publisher | 2364-3420 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1551 | Food Studies Common Ground Research Networks / Unknown Publisher | 2160-1933 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1552 | Crossings Intellect Ltd. / Unknown Publisher | 2040-4344 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1553 | Bibliotecas, Anales De Investigacion Biblioteca Nacional De Cuba Jose Marti / Unknown Publisher | 0006-176X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1554 | Suma De Negocios Fundacion Universitaria Konrad Lorenz / Unknown Publisher | 2027-5692 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1555 | Journal Of Algebraic Hyperstructures And Logical Algebras / Unknown Publisher | 2676-6000 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1556 | Journal Of Algebraic Hyperstructures And Logical Algebras University Of Hatef (Hatef College University) / Unknown Publisher | 2676-6019 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1557 | Teologicka Reflexe Karolinum - Nakladatelstvi Univerzity Karlovy / Unknown Publisher | 1211-1872 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1558 | Mobility Humanities The Academy Of Mobility Humanities, Konkuk University / Unknown Publisher | 2799-8118 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1559 | Economics Bulletin Economics Bulletin / Unknown Publisher | 1545-2921 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1560 | Acta Botanica Malacitana Universidad De Malaga / Unknown Publisher | 0210-9506 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1561 | Philippine Journal Of Science Department Of Science And Technology / Unknown Publisher | 0031-7683 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1562 | Budownictwo I Architektura Politechnika Lubelska / Unknown Publisher | 1899-0665 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1563 | Public Policy And Administration Mykolo Romerio Universitetas / Unknown Publisher | 1648-2603 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1564 | Oncology In Clinical Practice Wydawnictwo Via Medica / Unknown Publisher | 2450-1654 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1565 | Journal Of Orthoptera Research Orthopterists' Society / Unknown Publisher | 1082-6467 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1566 | Ardea / NEDERLANDSE ORNITHOLOGISCHE  UNIE | 0373-2266 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1567 | Journal Of Pediatric Research Galenos Publishing House / Unknown Publisher | 2147-9445 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1568 | The Journal Of Pediatric Research / Unknown Publisher | 2587-2478 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1569 | Cuadernos De Historia Moderna Universidad Complutense Madrid / Unknown Publisher | 0214-4018 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1570 | Cuadernos De Historia Moderna / Unknown Publisher | 1696-747X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1571 | Zhongguo Ying Yong Sheng Li Xue Za Zhi = Zhongguo Yingyong  Shenglixue Zazhi = Chinese Journal Of Applied Physiology Zhongguo Yingyong Shenglixue Zazhi Bianjibu / Unknown Publisher | 1000-6834 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1572 | Acta Iadertina University Of Zadar / Unknown Publisher | 1845-3392 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1573 | Jurnal Hukum Islam Faculty Of Sharia, Universitas Islam Negeri K.H. Abdurrahman  Wahid Pekalongan / Unknown Publisher | 1829-7382 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1574 | Revue Francaise D'Ethique Appliquee Eres / Unknown Publisher | 2427-0687 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1575 | Categories And General Algebraic Structures With Applications Shahid Beheshti University / Unknown Publisher | 2345-5853 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1576 | Annuaire Roumain D'Anthropologie Publishing House Of The Romanian Academy / Unknown Publisher | 0570-2259 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1577 | Revista De Neurologia / IMR PRESS | 0210-0010 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1578 | Research In Economics Academic Press / N°   ISSN   E-ISSN | 1090-9443 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1579 | Psychoanalytic Perspectives Routledge / Unknown Publisher | 1551-806X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1580 | Economic Annals-Xxi Institute Of Society Transformation / Unknown Publisher | 1728-6220 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1581 | Academic Pathology Association Of Pathology Chairs / Unknown Publisher | 2374-2895 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1582 | Asap Journal Johns Hopkins University Press / Unknown Publisher | 2381-4705 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1583 | Musica Hodie / UNIV FEDERAL GOIAS | 1676-3939 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1584 | Odonatologica / SOC INT ODONATOLOGICA | 0375-0183 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1585 | Proceedings Of The Institution Of Civil Engineers: Forensic  Engineering Ice Publishing / Unknown Publisher | 2043-9903 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1586 | Astrodynamics / Unknown Publisher | 2522-008X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1587 | Astrodynamics Tsinghua University Press / Unknown Publisher | 2522-0098 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1588 | Journal Of Holistic Nursing And Midwifery Guilan University Of Medical Sciences / Unknown Publisher | 2588-3712 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1589 | Philologia Classica Saint Petersburg State University / Unknown Publisher | 0202-2532 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1590 | Trends In Biomaterials And Artificial Organs Society For Biomaterials And Artificial Organs - India / Unknown Publisher | 0971-1198 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1591 | Ornitologia Colombiana Asociacion Colombiana De Ornitologia / Unknown Publisher | 1794-0915 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1592 | International Journal Of Environmental Sustainability Common Ground Research Networks / Unknown Publisher | 2325-1077 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1593 | Demografie Cesky Statisticky Urad / Unknown Publisher | 0011-8265 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1594 | Revue De Qumran J. Gabalda Et Cie / N°   ISSN   E-ISSN | 0035-1725 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1595 | Revue De Qumrân / Unknown Publisher | 2506-7567 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1596 | Color Culture And Science Gruppo Del Colore - Associazione Italiana Colore / Unknown Publisher | 2384-9568 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1597 | Architecture Research University Of Ljubljana, Faculty Of Architecture / Unknown Publisher | 1580-5573 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1598 | Organic Letters / AMER CHEMICAL SOC | 1523-7052 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1599 | Polymer Engineering And Science / Unknown Publisher | 0096-8129 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1600 | Journal Of Aircraft / AMER INST AERONAUTICS   ASTRONAUTICS | 0021-8669 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1601 | Nurse Education Today / CHURCHILL LIVINGSTONE | 0260-6917 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1602 | Dialectica / PHILOSOPHIE.CH | 0012-2017 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1603 | Dirasat: Human And Social Sciences The University Of Jordan / Unknown Publisher | 1026-3721 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1604 | Canadian Journal Of Hospital Pharmacy Canadian Society Of Hospital Pharmacists / Unknown Publisher | 0008-4123 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1605 | Bois Et Forets Des Tropiques / CIRAD-CENTRE COOPERATION INT  RECHERCHE AGRONOMIQUE POUR | 0006-579X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1606 | Rilce-Revista De Filologia  Hispanica / UNIV NAVARRA, SERVICIO  PUBLICACIONES | 0213-2370 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1607 | Inra Productions Animales Institut National De Recherche Pour L'Agriculture, L'Alimentation  Et L'Environnement (Inrae) / Unknown Publisher | 2273-774X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1608 | Revista Cubana De Pediatria Editorial Ciencias Medicas / Unknown Publisher | 0034-7531 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1609 | Tizard Learning Disability Review / Unknown Publisher | 2042-8782 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1610 | Logistique Et Management Informa Uk Ltd / Unknown Publisher | 1250-7970 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1611 | Neuroscience Journal Of Shefaye Khatam Shefa Neuroscience Research Center / Unknown Publisher | 2322-1887 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1612 | Historia Agraria / UNIV MURCIA | 1139-1472 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1613 | Izvestiya Vuzov. Poroshkovaya Metallurgiya I Funktsional'Nye  Pokrytiya Izdatel'Stvo Kalvis / Unknown Publisher | 1997-308X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1614 | Proceedings Of The Institution Of Civil Engineers: Engineering  And Computational Mechanics Ice Publishing / Unknown Publisher | 1755-0777 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1615 | Computer Science Agh University Of Science And Technology / Unknown Publisher | 1508-2806 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1616 | Revista Criminalidad Policia Nacional De Colombia / Unknown Publisher | 1794-3108 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1617 | Italia Contemporanea Francco Angeli Edizioni / Unknown Publisher | 2531-4033 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1618 | Revista Colombiana De Matematicas Universidad Nacional De Colombia / Unknown Publisher | 0034-7426 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1619 | Mathematical Statistics And Learning European Mathematical Society Publishing House / Unknown Publisher | 2520-2316 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1620 | Biologist Institute Of Biology / Unknown Publisher | 0006-3347 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1621 | Clinical Neuropsychiatry Giovanni Fioriti Editore / Unknown Publisher | 1724-4935 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1622 | Tanaffos Shaheed Beheshti University Of Medical Sciences And Health  Services / Unknown Publisher | 1735-0344 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1623 | Journal Of Fuzzy Extension And Applications Research Expansion Alliance (Rea) / Unknown Publisher | 2783-1442 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1624 | Journal Of The Ghana Science Association Ghana Science Association / Unknown Publisher | 2737-713X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1625 | Gorteria: Tijdschrift Voor Onderzoek Aan De Wilde Flora Naturalis Biodiversity Center / Unknown Publisher | 2542-8578 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1626 | Journal Of Clinical Investigation / AMER SOC CLINICAL  INVESTIGATION INC | 0021-9738 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1627 | Revista De La Facultad De Ciencias Agrarias Universidad Nacional De Cuyo / N°   ISSN   E-ISSN | 0370-4661 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1628 | Revista De La Facultad De Ciencias  Agrarias / UNIV NACIONAL CUYO, FAC  CIENCIAS AGRARIAS | 1853-8665 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1629 | Revista Panamericana De Salud  Publica-Pan American Journal Of  Public Health / PAN AMER HEALTH ORGANIZATION | 1020-4989 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1630 | Bulletin Of The Korean  Mathematical Society / KOREAN MATHEMATICAL SOC | 1015-8634 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1631 | Bulletin Of The Korean Mathematical Society / Unknown Publisher | 2234-3016 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1632 | Review Of Metaphysics / PHILOSOPHY EDUCATION SOC, INC | 0034-6632 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1633 | The Review Of Metaphysics / Unknown Publisher | 1549-4853 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1634 | Baltistica Vilnius University, Department Of Baltic Studies / Unknown Publisher | 0132-6503 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1635 | Apunts. Educacion Fisica Y Deportes Institut Nacional D'Educacio Fisica De Catalunya / Unknown Publisher | 1577-4015 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1636 | International Journal Of Rotating Machinery / Unknown Publisher | 1026-7115 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1637 | Clinical Dentistry (Russia) Clinical Dentistry Llc / Unknown Publisher | 1811-153X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1638 | Biologicni Studii Ivan Franko National University Of Lviv / Unknown Publisher | 1996-4536 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1639 | Kavkazskij Entomologiceskij Bulleten Southern Scientific Centre Of The Russian Academy Of Sciences / Unknown Publisher | 1814-3326 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1640 | Journal Of Agricultural Extension Agricultural Extension Society Of Nigeria / Unknown Publisher | 1119-944X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1641 | Comunicacion Y Sociedad (Mexico) Universidad De Guadalajara / Unknown Publisher | 0188-252X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1642 | Journal Of Endometriosis And Pelvic Pain Disorders Wichtig Publishing Srl / Unknown Publisher | 2284-0265 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1643 | Journal Of Health And Pollution Pure Earth / Unknown Publisher | 2156-9614 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1644 | Memoria E Ricerca Societa Editrice Il Mulino / N°   ISSN   E-ISSN | 1127-0195 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1645 | Foldtani Kozlony Hungarian Geological Society / Unknown Publisher | 0015-542X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1646 | Földtani Közlöny / Unknown Publisher | 2559-902X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1647 | Anuario De Psicologia Universitat De Barcelona / Unknown Publisher | 0066-5126 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1648 | Bonn Zoological Bulletin Zoologisches Forschungsmuseum Alexander Koenig / Unknown Publisher | 2190-7307 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1649 | Research In Community And Public Health Nursing Korean Academy Of Community Health Nursing / Unknown Publisher | 2983-0648 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1650 | Bollettino Filosofico University Of Naples Federico Ii / Unknown Publisher | 1593-7178 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1651 | Journal Of Anthropological  Sciences / IST ITALIANO ANTROPOLOGIA | 2037-0644 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1652 | Corrosion / NATL ASSOC CORROSION ENG | 0010-9312 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1653 | Ethnomusicology / SOC ETHNOMUSICOLOGY INC | 0014-1836 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1654 | Journal Of Democracy / JOHNS HOPKINS UNIV PRESS | 1045-5736 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1655 | Journal Of The Korean Society For Railway Korean Society For Railway / Unknown Publisher | 1738-6225 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1656 | International Journal Of  Periodontics & Restorative  Dentistry / QUINTESSENCE PUBLISHING CO INC | 0198-7569 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1657 | Bulletin For International Taxation International Bureau Of Fiscal Documentation (Ibfd) / Unknown Publisher | 1819-5490 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1658 | Jasss-The Journal Of Artificial  Societies And Social Simulation / J A S S S | 1460-7425 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1659 | Production Associacao Brasileira De Engenharia De Producao / Unknown Publisher | 0103-6513 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1660 | Clinical And Experimental  Otorhinolaryngology / KOREAN SOC OTORHINOLARYNGOL | 1976-8710 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1661 | China Petroleum Exploration Petroleum Industry Press / Unknown Publisher | 1672-7703 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1662 | Philip Roth Studies Purdue University Press / N°   ISSN   E-ISSN | 1547-3929 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1663 | Utrecht Law Review Igitur, Utrecht Publishing And Archiving Services / Unknown Publisher | 1871-515X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1664 | Jurnal Ekonomi Malaysia Penerbit Universiti Kebangsaan Malaysia / Unknown Publisher | 0127-1962 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1665 | Journal Of Digital And Social Media Marketing Henry Stewart Publications / Unknown Publisher | 2050-0076 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1666 | Turismo Y Sociedad Universidad Externado De Colombia / Unknown Publisher | 0120-7555 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1667 | Turkiye Klinikleri Dermatoloji Ortadogu Reklam Tanitim Yayincilik Turizm Egitim Insaat  Sanayi Ve Ticaret A.S. / Unknown Publisher | 2146-9016 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1668 | Journal Of Innovative Image Processing Inventive Research Organization / Unknown Publisher | 2582-4252 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1669 | East Asian Archives Of Psychiatry Hong Kong Academy Of Medicine Press / Unknown Publisher | 2078-9947 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1670 | Metabolism And Target Organ Damage Oae Publishing Inc. / Unknown Publisher | 2769-6375 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1671 | Cornova Institute Of Czech Literature Czech Academy Of Sciences / Unknown Publisher | 1804-6983 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1672 | Journal Of Southeast Asian Human Rights University Of Jember / Unknown Publisher | 2599-2147 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1673 | Sustainable Operations And Computers Keai Communications Co. / Unknown Publisher | 2666-4127 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1674 | Turkish World Mathematical Society Journal Of Applied And  Engineering Mathematics Isik University / Unknown Publisher | 2146-1147 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1675 | International Journal Of Film And Media Arts Lusofona University / Unknown Publisher | 2183-9271 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1676 | Phyton-Annales Rei Botanicae / FERDINAND BERGER SOEHNE | 0079-2047 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1677 | Psl Quarterly Review Economia Civile / Unknown Publisher | 2037-3635 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1678 | Sun Yat-Sen Journal Of Humanities National Sun Yat-Sen University, College Of Liberal Arts / Unknown Publisher | 1024-3631 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1679 | Ippta: Quarterly Journal Of Indian Pulp And Paper Technical  Association Indian Pulp And Paper Technical Association / Unknown Publisher | 0379-5462 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1680 | Journal Of Organic Chemistry / AMER CHEMICAL SOC | 0022-3263 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1681 | Leading Edge Society Of Exploration Geophysicists / Unknown Publisher | 1070-485X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1682 | Contributions To Indian Sociology / Unknown Publisher | 0069-9667 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1683 | Revista Mexicana De Urologia Sociedad Mexicana De Urologia. Colegio De Profesionistas A.C. / Unknown Publisher | 0185-4542 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1684 | Breathe European Respiratory Society / Unknown Publisher | 1810-6838 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1685 | Allergy Asthma & Immunology  Research / KOREAN ACAD ASTHMA ALLERGY &  CLINICAL IMMUNOLOGY | 2092-7355 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1686 | Annals Of Clinical And Experimental Neurology Eco-Vector Llc / Unknown Publisher | 2075-5473 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1687 | Journal Of Advanced  Prosthodontics / KOREAN ACAD PROSTHODONTICS | 2005-7806 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1688 | Review Of Korean Studies The Academy Of Korean Studies / Unknown Publisher | 1229-0076 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1689 | Wildlife Society Bulletin / Unknown Publisher | 1938-5463 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1690 | Trans Universidad De Malaga / Unknown Publisher | 1137-2311 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1691 | Trans Revista De Traductología / Unknown Publisher | 2603-6967 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1692 | Archiwum Kryminologii  Institute Of Law Studies Of The Polish Academy Of Sciences And  The Committee On Legal Sciences Of The Polish Academy Of  Sciences / Unknown Publisher | 0066-6890 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1693 | Canadian Veterinary Journal- Revue Veterinaire Canadienne / CANADIAN VET MED ASSOC | 0008-5286 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1694 | 452ºf Universitat De Barcelona, Facultad De Filologia / Unknown Publisher | 2013-3294 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1695 | Journal Of Interventional Medicine Keai Publishing Communications Ltd. / Unknown Publisher | 2096-3602 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1696 | Lasers In Engineering / OLD CITY PUBLISHING INC | 0898-1507 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1697 | Occhiali - Rivista Sul Mediterraneo Islamico Universita Della Calabria / Unknown Publisher | 2532-6740 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1698 | Historia Philosophica Fabrizio Serra Editore / Unknown Publisher | 1724-6121 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1699 | Ager Ceddar / Unknown Publisher | 2340-4655 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1700 | Chemical Engineering Progress / AMER INST CHEMICAL ENGINEERS | 1945-0710 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1701 | Guangzi Xuebao/Acta Photonica Sinica Chinese Optical Society / Unknown Publisher | 1004-4213 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1702 | Bmgn-The Low Countries  Historical Review / KONINKLIJK NEDERLANDS  HISTORISCH GENOOTSCHAP | 0165-0505 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1703 | Journal Of Molecular  Endocrinology / BIOSCIENTIFICA LTD | 0952-5041 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1704 | Journal Of Chinese Pharmaceutical Sciences Chinese Pharmaceutical Association / Unknown Publisher | 1003-1057 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1705 | Research Journal Of Chemistry And Environment World Researchers Associations / Unknown Publisher | 0972-0626 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1706 | Asia Pacific Journal Of Health Management / Unknown Publisher | 1833-3818 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1707 | Asia Pacific Journal Of Health Management Australasian College Of Health Service Management / Unknown Publisher | 2204-3136 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1708 | Ideas Institut Des Ameriques / Unknown Publisher | 1950-5701 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1709 | Espacio, Tiempo Y Forma, Serie Vii: Historia Del Arte Universidad Nacional De Educacion A Distancia (Uned) / Unknown Publisher | 1130-4715 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1710 | Ukrainian Botanical Journal Publishing House Akademperiodyka / Unknown Publisher | 0372-4123 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1711 | Cancer Informatics Libertas Academica Ltd. / Unknown Publisher | 1176-9351 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1712 | Animal Biodiversity And  Conservation / MUSEU DE CIENCIES NATURALS- ZOOLOGIA | 1578-665X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1713 | Revista Ciencias De La Salud Universidad Del Rosario / Unknown Publisher | 2145-4507 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1714 | Journal Of Geriatric Cardiology / TSINGHUA UNIV PRESS | 1671-5411 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1715 | Soudobe Dejiny Institute Of Contemporary History Of The Czech Academy Of  Sciences / Unknown Publisher | 1210-7050 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1716 | Health Psychology Research Open Medical Publishing / Unknown Publisher | 2420-8124 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1717 | Learning And Teaching Berghahn Journals / Unknown Publisher | 1755-2273 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1718 | Journal Of Comparative Asian Development Igi Global Publishing / Unknown Publisher | 1533-9114 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1719 | Harmonia: Journal Of Arts Research And Education Universitas Negeri Semarang / Unknown Publisher | 1411-5115 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1720 | Rakenteiden Mekaniikka Aalto-Yliopisto - Rakennustekniikan Laitos / Unknown Publisher | 0783-6104 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1721 | Avicenna Journal Of Medical Biotechnology Avicenna Research Institute / Unknown Publisher | 2008-2835 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1722 | Soil And Environment Soil Science Society Of Pakistan / Unknown Publisher | 2074-9546 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1723 | For The Learning Of Mathematics Flm Publishing Association / Unknown Publisher | 0228-0671 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1724 | Michigan Law Review / MICH LAW REV ASSOC | 0026-2234 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1725 | Jurnal Teknologi Penerbit Utm Press / Unknown Publisher | 0127-9696 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1726 | Journal Of Neurointerventional  Surgery / BMJ PUBLISHING GROUP | 1759-8478 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1727 | Learning & Memory / COLD SPRING HARBOR LAB PRESS,  PUBLICATIONS DEPT | 1072-0502 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1728 | Knowledge Organization / NOMOS VERLAGSGESELLSCHAFT  MBH & CO KG | 0943-7444 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1729 | Postmodern Culture / JOHNS HOPKINS UNIV PRESS | 1053-1920 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1730 | Journal Of The History Of  Sexuality / UNIV TEXAS PRESS | 1043-4070 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1731 | Urban Planning Cogitatio Press / Unknown Publisher | 2183-7635 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1732 | Current Trends In Biotechnology And Pharmacy Association Of Biotechnology And Pharmacy / Unknown Publisher | 0973-8916 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1733 | Water Science And Engineering Editorial Office Of Water Science And Engineering / Unknown Publisher | 1674-2370 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1734 | Soldagem & Inspecao / ASSOC BRASIL SOLDAGEM | 0104-9224 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1735 | Revija Za Sociologiju Hrvatsko Sociolosko Drustvo/Croatian Sociological Association / N°   ISSN   E-ISSN | 0350-154X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1736 | Revija Za Sociologiju / Unknown Publisher | 1846-7954 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1737 | Obrana A Strategie University Of Defence / Unknown Publisher | 1214-6463 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1738 | Psychiatrikē = Psychiatriki Hellenike Psychiatrike Hetaireia / Unknown Publisher | 1105-2333 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1739 | Yegah Musicology Journal Tolga Karaca / Unknown Publisher | 2792-0178 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1740 | De Jure: Jurnal Hukum Dan Syar'Iah Maulana Malik Ibrahim State Islamic University Of Malang / Unknown Publisher | 2085-1618 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1741 | Produccion Y Limpia Corporacion Universitaria Lasallista / Unknown Publisher | 1909-0455 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1742 | Modern Chinese Literature And  Culture / FOREIGN LANGUAGE PUBL | 1520-9857 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1743 | Analecta Hermeneutica International Institute For Hermeneutics / Unknown Publisher | 1918-7351 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1744 | Gis-Zeitschrift Fur Geoinformatik Wichmann, Vde / Unknown Publisher | 1869-9391 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1745 | Disegno Uid Unione Italiana Disegno / Unknown Publisher | 2533-2899 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1746 | Philippine Studies: Historical And Ethnographic Viewpoints Ateneo De Manila University / Unknown Publisher | 2244-1093 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1747 | Language Speech And Hearing  Services In Schools / AMER SPEECH-LANGUAGE-HEARING  ASSOC | 0161-1461 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1748 | Annales De L Institut Henri  Poincare-Probabilites Et  Statistiques / INST MATHEMATICAL STATISTICS- IMS | 0246-0203 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1749 | Crop Research Gaurav Publications / N°   ISSN   E-ISSN | 0970-4884 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1750 | Zeitschrift Der Deutschen  Gesellschaft Fur  Geowissenschaften / E SCHWEIZERBARTSCHE  VERLAGSBUCHHANDLUNG | 1860-1804 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1751 | Cytojournal / SCIENTIFIC SCHOLAR LLC | 0974-5963 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1752 | Advances In Geo-Energy Research Yandy Scientific Press / Unknown Publisher | 2207-9963 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1753 | Hesperis-Tamuda Universite Mohammed V De Rabat - Institut Scientifique / Unknown Publisher | 0018-1005 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1754 | Paradigmi Societa Editrice Il Mulino / Unknown Publisher | 1120-3404 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1755 | Sibirskiy Psikhologicheskiy Zhurnal Tomsk State University / Unknown Publisher | 1726-7080 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1756 | Zeitschrift Fur Technikfolgenabschatzung In Theorie Und Praxis /  Journal For Technology Assessment In Theory And Practice Oekom - Gesellschaft Fuer Oekologische Kommunikation Mbh / Unknown Publisher | 2567-8833 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1757 | Journal Of The Indian Medical Association Evangel Publishing / Unknown Publisher | 0019-5847 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1758 | Mizan Law Review St Mary'S University / Unknown Publisher | 1998-9881 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1759 | Prohistoria Historia Políticas De La Historia / Unknown Publisher | 1514-0032 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1760 | Prohistoria. Historia, Politicas De La Historia Scientific Technological Center Conicet-Rosario / Unknown Publisher | 1851-9504 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1761 | Population Review Sociological Demography Press / Unknown Publisher | 0032-471X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1762 | Revista Mexicana De Ciencias  Geologicas / CENTRO GEOCIENCIAS UNAM | 1026-8774 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1763 | Studia Historica, Historia Antigua Ediciones Universidad De Salamanca / Unknown Publisher | 0213-2052 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1764 | South Dakota Journal Of Medicine South Dakota State Medical Association / Unknown Publisher | 0038-3317 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1765 | Pure And Applied Functional Analysis Yokohama Publications / Unknown Publisher | 2189-3756 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1766 | Linguistica Antverpiensia, New Series – Themes In Translation  Studies  Department Of Applied Linguistics, Translators And  Interpreters, University Of Antwerp / Unknown Publisher | 0304-2294 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1767 | Wiadomosci Konserwatorskie Zarzad Glowny Stowarzyszenia Konserwatorow Zabytkow / Unknown Publisher | 0860-2395 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1768 | Ecs Journal Of Solid State Science  And Technology / ELECTROCHEMICAL SOC INC | 2162-8769 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1769 | Ama Journal Of Ethics American Medical Association / Unknown Publisher | 2376-6980 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1770 | Harvard Business Review / HARVARD BUSINESS SCHOOL  PUBLISHING CORPORATION | 0017-8012 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1771 | Historia Mexicana / COLEGIO DE MEXICO CENTRO DE  ESTUDIOS HISTORICOS | 0185-0172 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1772 | Vestnik Samarskogo Gosudarstvennogo Tekhnicheskogo  Universiteta, Seriya Fiziko-Matematicheskie Nauki Samara State Technical University / Unknown Publisher | 1991-8615 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1773 | Ankara Universitesi Ilahiyat Fakultesi Dergisi Ankara University, Journal Of The Faculty Of Divinity / Unknown Publisher | 1301-0522 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1774 | Agriculture And Natural Resources Kasetsart University / Unknown Publisher | 2452-316X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1775 | Revista De Ciencia Politica Pontificia Universidad Catolica De Chile / Unknown Publisher | 0716-1417 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1776 | Revista De Ciencia Politica / PONTIFICIA UNIV CATOLICA CHILE,  INST CIENCIA POLITICA | 0718-090X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1777 | Pediatric Traumatology, Orthopaedics And Reconstructive  Surgery Eco-Vector Llc / Unknown Publisher | 2309-3994 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1778 | Propulsion And Power Research / KEAI PUBLISHING LTD | 2212-540X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1779 | Electrica Istanbul University / Unknown Publisher | 2619-9831 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1780 | Computer Science Research Notes Vaclav Skala Union Agency / Unknown Publisher | 2464-4617 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1781 | Forensic Anthropology University Of Florida Press / Unknown Publisher | 2573-5020 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1782 | Etnografia Peter The Great Museum Of Anthropology And Ethnography  (Kunstkamera), Russian Academy Of Sciences / Unknown Publisher | 2618-8600 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1783 | Peristil Croatian Society Of Art Historians / Unknown Publisher | 0553-6707 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1784 | Asia Maior Viella / N°   ISSN   E-ISSN | 2385-2526 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1785 | Asia Maior The Journal Of The Italian Think Tank On Asia Founded By Giorgio Borsa In 1989 / Unknown Publisher | 2612-6680 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1786 | Gomal Journal Of Medical Sciences Gomal Medical College / Unknown Publisher | 1819-7973 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1787 | Bsglg Societe Geographique De Liege / Unknown Publisher | 0770-7576 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1788 | European Journal Of Comparative Economics University Carlo Cattaneo / Unknown Publisher | 1824-2979 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1789 | Journal Of Advanced Research In Experimental Fluid Mechanics  And Heat Transfer Penerbit Akademia Baru / Unknown Publisher | 2756-8202 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1790 | International Journal Of  Computerized Dentistry / QUINTESSENCE PUBLISHING CO INC | 1463-4201 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1791 | Revista De Demografia Historica Asociacion De Demografia Historica / Unknown Publisher | 1696-702X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1792 | Journal Of The Geological Society / GEOLOGICAL SOC PUBL HOUSE | 0016-7649 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1793 | Medwave Medwave Estudios Ltda / Unknown Publisher | 0717-6384 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1794 | Canadian Family Physician / COLL FAMILY PHYSICIANS CANADA | 0008-350X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1795 | Journal Of The Korea Concrete Institute Korea Concrete Institute / Unknown Publisher | 1229-5515 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1796 | Human Reproduction Update / Unknown Publisher | 1362-4946 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1797 | The International Journal Of Press/Politics / Unknown Publisher | 1040-1620 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1798 | Iraqi Journal For Electrical And Electronic Engineering College Of Engineering, University Of Basrah / Unknown Publisher | 1814-5892 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1799 | Journal Of Applied Nonlinear Dynamics L & H Scientific Publishing, Llc / Unknown Publisher | 2164-6457 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1800 | International Journal Of Cognitive Therapy Guilford Publications / Unknown Publisher | 1937-1209 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1801 | Journal Of Islamic Thought And Civilization University Of Management And Technology / Unknown Publisher | 2075-0943 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1802 | Nanomaterials And Energy Ice Publishing / Unknown Publisher | 2045-9831 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1803 | Journal Of Business Ethics Education Neilsonjournals Publishing / Unknown Publisher | 1649-5195 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1804 | Swiss Journal Of Sociology Schweizerische Gesellschaft Fur Soziologie / Unknown Publisher | 0379-3664 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1805 | Russian Journal Of Economics Non-Profit Partnership 'Voprosy Ekonomiki' / Unknown Publisher | 2405-4739 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1806 | International Journal Of Organizational Diversity Common Ground Research Networks / Unknown Publisher | 2328-6229 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1807 | Cadernos De Sociomuseologia Lusofona University / Unknown Publisher | 1646-3714 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1808 | Musica Tecnologia Firenze University Press / Unknown Publisher | 1974-0042 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1809 | American Poetry Review / OLD CITY PUBLISHING INC | 0360-3709 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1810 | Yingyong Kexue Xuebao/Journal Of Applied Sciences Shanghai Science And Technology Press / Unknown Publisher | 0255-8297 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1811 | Dalian Haishi Daxue Xuebao/Journal Of Dalian Maritime  University Editorial Office Of Journal Of Dalian Maritime University / Unknown Publisher | 1006-7736 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1812 | Politica Y Gobierno Centro De Investigacion Y Docencia Economicas A.C. / Unknown Publisher | 1405-1060 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1813 | Journal Of Chinese Agricultural Mechanization Journal Of Chinese Agricultural Mechanization Editorial Office / Unknown Publisher | 2095-5553 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1814 | Development / COMPANY BIOLOGISTS LTD | 0950-1991 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1815 | Journal Of The Institute Of Electrical Engineers Of Japan The Institute Of Electrical Engineers Of Japan / Unknown Publisher | 1340-5551 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1816 | Annales De Biologie Clinique / JLE | 0003-3898 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1817 | International Journal Of  Automotive Technology / KOREAN SOC AUTOMOTIVE  ENGINEERS-KSAE | 1229-9138 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1818 | Voix & Images / UNIV QUEBEC-MONTREAL | 0318-9201 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1819 | Seibutsu-Kogaku Kaishi Society For Biotechnology, Japan / Unknown Publisher | 0919-3758 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1820 | Dermatology Practical &  Conceptual / MATTIOLI 1885 | 2160-9381 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1821 | International Journal Of Mining Science And Technology / Unknown Publisher | 2589-062X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1822 | Trends In Anaesthesia And Critical Care Churchill Livingstone / Unknown Publisher | 2210-8440 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1823 | Cardiac Electrophysiology Clinics W.B. Saunders / Unknown Publisher | 1877-9182 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1824 | Journal Of Korean Academy Of Psychiatric And Mental Health  Nursing Korean Academy Of Psychiatric And Mental Health Nursing / Unknown Publisher | 1225-8482 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1825 | Theory And Event Johns Hopkins University Press / Unknown Publisher | 1092-311X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1826 | Infectio Asociacion Colombiana De Infectologia / Unknown Publisher | 0123-9392 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1827 | Infectio / Unknown Publisher | 2422-3794 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1828 | Journal For The Study Of  Religions And Ideologies / UNIV BABES-BOLYAI | 1583-0039 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1829 | Longitudinal And Life Course  Studies / BRISTOL UNIV PRESS & POLICY  PRESS | 1757-9597 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1830 | National Medical Journal Of  India / SCIENTIFIC SCHOLAR LLC | 2583-150X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1831 | Gulf And Caribbean Research University Of Southern Mississippi / Unknown Publisher | 1528-0470 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1832 | Plural. History. Culture. Society Ion Creanga State Pedagogical University / Unknown Publisher | 2345-1262 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1833 | International Journal Of Sociology Of Education Hipatia Editorial / Unknown Publisher | 2014-3575 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1834 | Jordan Journal Of Electrical Engineering Tafila Technical University / Unknown Publisher | 2409-9600 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1835 | Journal Of Military And Veterans' Health Australasian Military Medicine Association / Unknown Publisher | 1835-1271 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1836 | Journal Of Military And Veterans' Health/Journal Of Military And Veterans' Health. / Unknown Publisher | 1839-2733 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1837 | Lekar A Technika Czech Medical Association J.E. Purkyne / Unknown Publisher | 0301-5491 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1838 | Lékař A Technika - Clinician And Technology / Unknown Publisher | 2336-5552 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1839 | Scires-It Caspur -Ciber Publishing / Unknown Publisher | 2239-4303 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1840 | Arquivos Brasileiros De  Cardiologia / ARQUIVOS BRASILEIROS  CARDIOLOGIA | 0066-782X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1841 | International Journal Of Computer Mathematics / Unknown Publisher | 1026-7425 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1842 | Missouri Review / UNIV MISSOURI, COLL ARTS &  SCIENCE | 0191-1961 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1843 | Clinical Epidemiology / DOVE MEDICAL PRESS LTD | 1179-1349 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1844 | Journal Of Psychiatry &  Neuroscience / CMA-CANADIAN MEDICAL ASSOC | 1180-4882 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1845 | Ceska A Slovenska Neurologie A  Neurochirurgie / CZECH MEDICAL SOC | 1210-7859 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1846 | Bakhtiniana Less Catholic University - Sao Paulo / Unknown Publisher | 2176-4573 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1847 | Iium Engineering Journal International Islamic University Malaysia / Unknown Publisher | 1511-788X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1848 | Journal Of Condensed Matter Nuclear Science The International Society For Condensed Matter Nuclear  Science / Unknown Publisher | 2227-3123 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1849 | International Journal Of Software Innovation Igi Global Publishing / Unknown Publisher | 2166-7160 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1850 | Journal Of Project Management (Canada) Growing Science / Unknown Publisher | 2371-8366 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1851 | Azerbaijan Journal Of Mathematics Institute Of Mathematics And Mechanics Nas Of Azerbaijan / Unknown Publisher | 2218-6816 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1852 | Vestnik Sankt-Peterburgskogo Universiteta. Ekonomika Saint Petersburg State University / Unknown Publisher | 1026-356X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1853 | Sustainable Marine Structures Nan Yang Academy Of Sciences Pte. Ltd / Unknown Publisher | 2661-3158 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1854 | Civil Szemle / UJ MANDATUM KONYVKIADO | 1786-3341 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1855 | Civil Szemle Civil Szemle Foundation / Unknown Publisher | 3004-2119 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1856 | Bestuur Sebelas Maret University Faculty Of Law / Unknown Publisher | 2302-3783 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1857 | Journal Of International Buddhist Studies Mahachulalongkornrajavidyalaya University / Unknown Publisher | 1906-6244 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1858 | Verifiche / ASSOC TRENTINA SCI UMANE | 0391-4186 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1859 | Encuentros (Maracaibo) Rafael Maria Baralt National Experimental University / Unknown Publisher | 2610-8046 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1860 | Journal Of Instrumental Analysis China Association For Instrumental Analysis / Unknown Publisher | 1004-4957 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1861 | Silicon Semiconductor Angel Business Communications Ltd. / Unknown Publisher | 2050-7801 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1862 | International Journal Of Molecular And Cellular Medicine Babol University Of Medical Sciences / Unknown Publisher | 2251-9645 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1863 | Eurointervention / EUROPA EDITION | 1774-024X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1864 | Mmwr-Morbidity And Mortality  Weekly Report / CENTERS  DISEASE CONTROL &  PREVENTION | 0149-2195 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1865 | Children'S Literature Association Quarterly Johns Hopkins University Press / Unknown Publisher | 0885-0429 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1866 | Defence Technology / KEAI PUBLISHING LTD | 2096-3459 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1867 | Endocrine Pathology / HUMANA PRESS INC | 1046-3976 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1868 | Adicciones / SOCIDROGALCOHOL | 0214-4840 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1869 | Gastro Hep Advances American Gastroenterological Association / Unknown Publisher | 2772-5723 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1870 | Historical Review-La Revue  Historique / NATL HELLENIC RES FOUNDATION | 1790-3572 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1871 | Guncel Pediatri Galenos Publishing House / Unknown Publisher | 1304-9054 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1872 | Journal Of Applied Accounting Research / Unknown Publisher | 1758-8855 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1873 | Journal Of Oral & Facial Pain And  Headache / MRE PRESS | 2333-0376 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1874 | Nephrology And Dialysis Jsc Vidal Rus / Unknown Publisher | 1680-4422 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1875 | International Journal Of Serious Games Serious Games Society / Unknown Publisher | 2384-8766 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1876 | Economic And Political Studies Routledge / Unknown Publisher | 2095-4816 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1877 | Marine And Fishery Sciences (Mafis) / Unknown Publisher | 2683-7595 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1878 | Marine And Fishery Sciences National Institute Of Fisheries Research And Development / Unknown Publisher | 2683-7951 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1879 | Revista De Psicologia Del Deporte Sociedad Revista De Psicologia Del Deporte / Unknown Publisher | 1132-239X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1880 | Medialingvistika Saint Petersburg State University / Unknown Publisher | 2312-0274 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1881 | Revista De La Sociedad Geologica De Espana Sociedad Geologica De Espana / Unknown Publisher | 0214-2708 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1882 | National Health Statistics Reports U.S. National Center For Health Statistics / Unknown Publisher | 2164-8344 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1883 | Agathon - International Journal Of Architecture, Art And Design Universita Di Palermo / Unknown Publisher | 2532-683X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1884 | American Scholar / PHI BETA KAPPA SOC | 2162-2892 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1885 | Tissue & Cell / CHURCHILL LIVINGSTONE | 0040-8166 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1886 | Periodicals Of Engineering And Natural Sciences International University Of Sarajevo / Unknown Publisher | 2303-4521 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1887 | Journal Of Poultry Science / JAPAN POULTRY SCIENCE ASSOC | 1346-7395 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1888 | Revista Brasileira De Saude E Producao Animal Universidade Federal Da Bahia / Unknown Publisher | 1519-9940 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1889 | Design Principles And Practices Common Ground Research Networks / Unknown Publisher | 1833-1874 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1890 | Revista Internacional De Linguistica Iberoamericana Vervuert Verlag / Unknown Publisher | 1579-9425 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1891 | Revista Gerencia Y Politicas De Salud Pontificia Universidad Javeriana / Unknown Publisher | 1657-7027 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1892 | Gerencia Y Políticas De Salud / Unknown Publisher | 2500-6177 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1893 | Pistes Institut De Recherche Robert-Sauve En Sante Et En Securite Du  Travail / Unknown Publisher | 1481-9384 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1894 | Journal Of Technical Education And Training Penerbit Uthm / Unknown Publisher | 2229-8932 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1895 | Journal Of Technical Education And Training / Unknown Publisher | 2600-7932 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1896 | Polski Merkuriusz Lekarski Wydawnictwo Aluna / Unknown Publisher | 1426-9686 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1897 | Povolzhskii Ekologicheskii Zhurnal Kmk Scientific Press Ltd. / Unknown Publisher | 1684-7318 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1898 | International Journal Of Human Capital And Information  Technology Professionals Igi Publishing / Unknown Publisher | 1947-3478 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1899 | Petita: Jurnal Kajian Ilmu Hukum Dan Syariah Lembaga Kajian Konstitusi Indonesia (Lkki), Fakultas Syariah  Dan Hukum, Universitas Islam Negeri Ar-Raniry / Unknown Publisher | 2502-8006 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1900 | Journal Of Philosophical Economics: Reflections On Economic  And Social Issues Bucharest University Of Economic Studies Publishing House / N°   ISSN   E-ISSN | 1843-2298 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1901 | Poe Studies-History Theory  Interpretation / JOHNS HOPKINS UNIV PRESS | 1754-6095 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1902 | Lithuanian Annual Strategic Review The General Jonas Zemaitis Military Academy Of Lithuania / Unknown Publisher | 1648-8024 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1903 | Australian Journal Of Learning Difficulties Routledge / Unknown Publisher | 1940-4158 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1904 | Intelligent Medicine Chinese Medical Association / Unknown Publisher | 2096-9376 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1905 | Journal Of Environmental Informatics Letters International Society For Environmental Information Sciences / Unknown Publisher | 2663-6859 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1906 | Journal Of Mining And Environment Shahrood University Of Technology / Unknown Publisher | 2251-8606 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1907 | Gmsarn International Journal Greater Mekong Subregion Academic And Research Network,  Asian Institute Of Technology / Unknown Publisher | 1905-9094 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1908 | Alytes Issca / Unknown Publisher | 0753-4973 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1909 | Research In Social Psychology Japanese Society Of Social Psychology / Unknown Publisher | 0916-1503 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1910 | Sistemi Intelligenti Il Mulino Publishing House / Unknown Publisher | 1120-9550 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1911 | China Surfactant Detergent And Cosmetics Editorial Office China Surfactant Detergent And Cosmetics / Unknown Publisher | 2097-2806 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1912 | Gastrointestinal Endoscopy / Unknown Publisher | 1085-8741 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1913 | Cochrane Database Of Systematic Reviews / Unknown Publisher | 1464-780X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1914 | Revue Belge De Philologie Et D  Histoire / REVUE BELGE PHILOLOGIE HISTOIRE | 0035-0818 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1915 | Revue Belge De Philologie Et D Histoire / Unknown Publisher | 2295-9068 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1916 | Indian Journal Of Agronomy Indian Society Of Agronomy / Unknown Publisher | 0537-197X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1917 | American Journal Of Managed  Care / MANAGED CARE & HEALTHCARE  COMMUNICATIONS LLC | 1088-0224 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1918 | Children And Schools National Association Of Social Workers / Unknown Publisher | 1532-8759 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1919 | Children & Schools / Unknown Publisher | 1545-682X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1920 | Journal Of Radiotherapy In Practice / Unknown Publisher | 1467-1131 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1921 | Res Anthropology And Aesthetics / Unknown Publisher | 2327-9621 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1922 | Journal Of Feminist Studies In  Religion / INDIANA UNIV PRESS | 1553-3913 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1923 | Korean Studies University Of Hawaii Press / Unknown Publisher | 0145-840X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1924 | Acta Otorhinolaryngologica  Italica / PACINI EDITORE | 0392-100X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1925 | Journal Of Culinary Science & Technology / Unknown Publisher | 1542-8044 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1926 | Pertanika Journal Of Tropical Agricultural Science Universiti Putra Malaysia / Unknown Publisher | 1511-3701 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1927 | Pertanika Journal Of Tropical Agricultural Science / Unknown Publisher | 2231-8542 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1928 | Rastitel'Nost' Rossii Russian Academy Of Sciences, V.L. Komarov Institute Of Botany / Unknown Publisher | 2073-0659 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1929 | Vegetation Of Russia / Unknown Publisher | 2687-1556 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1930 | Engineering Solid Mechanics Growing Science / Unknown Publisher | 2291-8744 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1931 | Acta Onomastica Czech Academy Of Sciences / Unknown Publisher | 1211-4413 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1932 | Acta Onomastica / Unknown Publisher | 2571-0907 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1933 | Journal Of Geodetic Science / Unknown Publisher | 2081-9919 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1934 | Osmanli Medeniyeti Arastirmalari Dergisi Selim Hilmi Ozkan / Unknown Publisher | 2458-9519 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1935 | Geriatrie Et Psychologie  Neuropsychiatrie Du  Vieillissement / JLE | 2115-7863 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1936 | Voices-The Journal Of New York  Folklore / NEW YORK FOLKLORE SOC | 0361-204X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1937 | Advanced Mathematical Models And Applications Jomard Publishing / Unknown Publisher | 2519-4445 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1938 | Vjesnik Dalmatinskih Arhiva State Archives In Sibenik / Unknown Publisher | 2757-0932 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1939 | Journal Of Turkish Society For Rheumatology Galenos Publishing House / Unknown Publisher | 2651-2653 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1940 | Philosophical Inquiries Edizioni Ets / Unknown Publisher | 2282-0248 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1941 | Archives Of Metallurgy And  Materials / POLSKA AKAD NAUK, POLISH ACAD  SCIENCES, INST METALL & MATER  SCI PAS | 1733-3490 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1942 | Western Journal Of Emergency  Medicine / WESTJEM | 1936-900X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1943 | Foot Churchill Livingstone / Unknown Publisher | 0958-2592 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1944 | Einstein (Sao Paulo, Brazil) Instituto De Ensino E Pesquisa Albert Einstein / Unknown Publisher | 1679-4508 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1945 | Gospodarka Surowcami  Mineralnymi-Mineral Resources  Management / POLSKA AKAD NAUK, POLISH ACAD  SCIENCES, MINER & ENERGY ECON  RES INST PAS | 0860-0953 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1946 | Advances In Climate Change  Research / KEAI PUBLISHING LTD | 1674-9278 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1947 | Advances In Climate Change Research Keai Communications Co. / Unknown Publisher | 2524-1761 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1948 | Horizonte Medico Universidad De San Martin De Porres, Facultad De Medicina / Unknown Publisher | 1727-558X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1949 | Horticultural Plant Journal / KEAI PUBLISHING LTD | 2095-9885 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1950 | Fontes Artis Musicae / A-R EDITIONS | 0015-6191 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1951 | Brazilian Business Review Fucape Business School / N°   ISSN   E-ISSN | 1808-2386 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1952 | Mexico Y La Cuenca Del Pacifico Universidad De Guadalajara / Unknown Publisher | 1665-0174 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1953 | Revista Baiana De Enfermagem Universidade Federal Da Bahia / Unknown Publisher | 0102-5430 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1954 | Journal Of Nutrition And Health Korean Nutrition Society / Unknown Publisher | 2288-3886 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1955 | Trends In Psychiatry And Psychotherapy Associacao De Psiquiatria Do Rio Grande Do Sul / Unknown Publisher | 2237-6089 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1956 | Psikhologicheskii Zhurnal / RUSSIAN ACAD SCIENCES, STATE  ACAD UNIV HUMANITIES (GAUGN) | 0205-9592 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1957 | Cardiologia Hungarica Promenade Publishing House Kft / Unknown Publisher | 0133-5596 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1958 | Biological Communications Saint Petersburg State University / Unknown Publisher | 2542-2154 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1959 | Journal Of Audiology And Otology Korean Audiological Society And Korean Otological Society / Unknown Publisher | 2384-1621 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1960 | Catalan Journal Of Communication And Cultural Studies Intellect Ltd. / Unknown Publisher | 1757-1898 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1961 | Folia Oecologica Institute Of Forest Ecology Of The Slovak Academy Of Sciences / Unknown Publisher | 1336-5266 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1962 | Folia Oecologica / Unknown Publisher | 1338-7014 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1963 | Con A De Animacion Universidad Politecnica De Valencia / Unknown Publisher | 2173-3511 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1964 | Medical Data Mining Tmr Publishing Group / Unknown Publisher | 2624-1587 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1965 | Humanities, Arts And Social Sciences Studies Silpakorn University / Unknown Publisher | 2630-0079 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1966 | Cardiology Letters Slovak Society Of Cardiology / Unknown Publisher | 1338-3655 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1967 | Osservatorio Del Diritto Civile E Commerciale Societa Editrice Il Mulino / Unknown Publisher | 2281-2628 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1968 | Osservatorio Del Diritto Civile E Commerciale / Unknown Publisher | 2612-4076 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1969 | Knjizevna Smotra / CROATIAN PHILOLOGICAL SOC | 0455-0463 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1970 | Artificial Intelligence In  Agriculture / KEAI PUBLISHING LTD | 2097-2113 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1971 | Annals Of Family Medicine / ANNALS FAMILY MEDICINE | 1544-1709 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1972 | Siberian Medical Review Krasnoyarsk State Medical University / Unknown Publisher | 1819-9496 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1973 | Sang Thrombose Vaisseaux John Libbey Eurotext / Unknown Publisher | 0999-7385 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1974 | Journal Of Artificial Intelligence  Research / AI ACCESS FOUNDATION | 1076-9757 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1975 | Critical Review Of International Social And Political Philosophy Routledge / Unknown Publisher | 1369-8230 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1976 | Teaching Education Routledge / Unknown Publisher | 1047-6210 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1977 | Mapan-Journal Of Metrology  Society Of India / METROLOGY SOC INDIA | 0970-3950 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1978 | Egyptian Journal Of Aquatic Research National Institute Of Oceanography And Fisheries / Unknown Publisher | 1687-4285 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1979 | Journal Of Educators Online Grand Canyon University / Unknown Publisher | 1547-500X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1980 | International Journal Of Gastrointestinal Intervention Society Of Gastrointestinal Intervention / Unknown Publisher | 2636-0004 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1981 | Acta Gymnica Palacky University / Unknown Publisher | 2336-4912 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1982 | Grassroots Journal Of Natural Resources Grassroots Institute / Unknown Publisher | 2581-6853 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1983 | Croatian And Comparative Public Administration Institute For Public Administration,  Croatian And Comparative  Public Administration / Unknown Publisher | 1848-0357 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1984 | Revista Chilena De Derecho Y Tecnologia Universidad De Chile / Unknown Publisher | 0719-2576 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1985 | Nuclear Engineering  International / WILMINGTON PUBL | 0029-5507 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1986 | Nuclear Engineering International / Unknown Publisher | 2514-4367 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1987 | Mendel Brno University Of Technology / Unknown Publisher | 1803-3814 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1988 | Mendel / Unknown Publisher | 1803-3822 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1989 | Cirugia Pediatrica : Organo Oficial De La Sociedad Espanola De  Cirugia Pediatrica Masson Publishing / Unknown Publisher | 0214-1221 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1990 | CirugíA PediáTrica/Cirugía Pediátrica / Unknown Publisher | 2445-2807 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1991 | Journal Of Automation And Intelligence Keai Communications Co. / Unknown Publisher | 2949-8554 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1992 | Orbis Idearum History Of Ideas Research Centre, Jagiellonian University  Krakow / Unknown Publisher | 2353-3900 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1993 | Journal Of The Ramanujan  Mathematical Society / RAMANUJAN MATHEMATICAL SOC | 2320-3110 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1994 | Folia Geographica University Of Presov / Unknown Publisher | 1336-6157 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1995 | Journal Of Chemical Education / AMER CHEMICAL SOC | 0021-9584 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1996 | Biochemical Society Transactions / PORTLAND PRESS LTD | 0300-5127 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1997 | Kardiologiya / RUSSIAN HEART FAILURE SOC | 0022-9040 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1998 | Demographic Research / MAX PLANCK INST DEMOGRAPHIC  RESEARCH | 1435-9871 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 1999 | Aerospace Medicine And Human  Performance / AEROSPACE MEDICAL ASSOC | 2375-6314 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2000 | Revista Internacional De  Contaminacion Ambiental / CENTRO CIENCIAS ATMOSFERA  UNAM | 0188-4999 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
