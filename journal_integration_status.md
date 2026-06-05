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
| 2001 | INTERNATIONAL JOURNAL OF  RADIATION ONCOLOGY BIOLO / ELSEVIER SCIENCE INC | 0360-3016 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2002 | JOURNAL OF IMMUNOLOGICAL  METHODS / ELSEVIER | 0022-1759 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2003 | HUMAN BIOLOGY / WAYNE STATE UNIV PRESS | 1534-6617 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2004 | Asia-Pacific Journal: Japan Focus Cambridge Univer / Unknown | 1557-4660 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2005 | Revista Brasileira de Ginecologia e Obstetricia Fe / Unknown | 1806-9339 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2006 | EMERGENCY MEDICINE CLINICS OF  NORTH AMERICA / W B SAUNDERS CO-ELSEVIER INC | 0733-8627 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2007 | Revue d'Elevage et de Medecine Veterinaire des Pay / Unknown | 1951-6711 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2008 | Family Court Review John Wiley & Sons Inc. / Unknown | 1531-2445 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2009 | DEMOCRATIZATION / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1351-0347 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2010 | LEADERSHIP & ORGANIZATION  DEVELOPMENT JOURNAL / EMERALD GROUP PUBLISHING LTD | 0143-7739 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2011 | AUSTRALIAN ARCHAEOLOGY / TAYLOR & FRANCIS LTD | 0312-2417 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2012 | CLINICAL TRIALS / SAGE PUBLICATIONS LTD | 1740-7745 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2013 | CLIMATE POLICY / TAYLOR & FRANCIS LTD | 1469-3062 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2014 | AQUACULTURAL ENGINEERING / ELSEVIER SCI LTD | 0144-8609 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2015 | INTERNATIONAL JOURNAL OF HUMAN  RIGHTS / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1364-2987 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2016 | Izvestiya Vysshikh Uchebnykh Zavedeniy. Prikladnay / Unknown | 2542-1905 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2017 | GUERRES MONDIALES ET CONFLITS  CONTEMPORAINS / PRESSES UNIV FRANCE | 2101-0137 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2018 | CHILD NEUROPSYCHOLOGY / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 0929-7049 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2019 | Journal of the Korean Association of Oral and Maxi / Unknown | 2234-7550 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2020 | Women Informa UK Ltd / Unknown | 1470-1367 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2021 | JOURNAL OF WEB ENGINEERING / RIVER PUBLISHERS | 1544-5976 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2022 | Journal for Nurses in Professional Development Lip / Unknown | 2169-9798 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2023 | JOURNAL OF THE TORREY BOTANICAL  SOCIETY / TORREY BOTANICAL SOC | 1940-0616 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2024 | Revista Brasileira de Linguistica Aplicada Univers / Unknown | 1984-6398 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2025 | South African Journal of Clinical Nutrition Taylor / Unknown | 1607-0658 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2026 | Journal of Pathology and Translational Medicine Ko / Unknown | 2383-7845 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2027 | Diyala Journal of Engineering Sciences University  / Unknown | 2616-6909 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2028 | HIGH POWER LASER SCIENCE AND  ENGINEERING / CAMBRIDGE UNIV PRESS | 2052-3289 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2029 | FUNGAL DIVERSITY / SPRINGER | 1560-2745 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2030 | Cuadernos de Turismo Escuela Universitaria de Turi / Unknown | 1989-4635 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2031 | INTERNATIONAL JOURNAL OF STEM  CELLS / KOREAN SOC STEM CELL RESEARCH | 2005-5447 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2032 | ANNALI ITALIANI DI CHIRURGIA / EDIZIONI LUIGI POZZI | 2239-253X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2033 | JOURNAL OF INVESTIGATIVE  PSYCHOLOGY AND OFFENDER  / WILEY | 1544-4759 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2034 | Suomen Antropologi Finnish Anthropological Society / Unknown | 1799-8972 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2035 | Revista Oficial del Poder Judicial Poder Judicial  / Unknown | 2663-9130 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2036 | EUROPEAN REVIEW OF SOCIAL  PSYCHOLOGY / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1046-3283 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2037 | Problemy Analiza Petrozavodsk State University / Unknown | 2306-3432 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2038 | Journal of The Institution of Engineers (India): S / Unknown | 2250-2483 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2039 | Corpus Pragmatics Springer Science + Business Medi / Unknown | 2509-9515 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2040 | International Journal of Electronic Commerce Studi / N°   ISSN   E-ISSN | 2073-9729 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2041 | International Journal of Comparative Education and / Unknown | 2309-4907 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2042 | East African Journal of Neurological Sciences East / N°   ISSN   E-ISSN | 2957-4323 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2043 | Policy and Practice Centre for Global Education / Unknown | 2053-4272 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2044 | NEUROLOGY / LIPPINCOTT WILLIAMS & WILKINS | 0028-3878 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2045 | CHEMIE INGENIEUR TECHNIK / WILEY-V C H VERLAG GMBH | 0009-286X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2046 | INTERNATIONAL JOURNAL OF ORAL  AND MAXILLOFACIAL S / CHURCHILL LIVINGSTONE | 1399-0020 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2047 | INTERNATIONAL JOURNAL OF  SYSTEMATIC AND EVOLUTION / MICROBIOLOGY SOC | 1466-5026 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2048 | AMERICAN JOURNAL OF MEDICAL  GENETICS PART A / WILEY | 1552-4825 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2049 | NUCLEAR SCIENCE AND ENGINEERING / TAYLOR & FRANCIS INC | 0029-5639 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2050 | JOURNAL OF MANUFACTURING  SCIENCE AND ENGINEERING- / ASME | 1528-8935 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2051 | PROCEEDINGS OF THE INSTITUTION OF  MECHANICAL ENGI / SAGE PUBLICATIONS LTD | 1350-6501 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2052 | JOURNAL OF RADIOLOGICAL  PROTECTION / IOP PUBLISHING LTD | 1361-6498 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2053 | PERIODICA MATHEMATICA  HUNGARICA / SPRINGER | 0031-5303 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2054 | International Journal of Operational Research Inde / Unknown | 1745-7645 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2055 | JOURNAL OF RISK RESEARCH / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1366-9877 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2056 | JOURNAL OF FAMILY THERAPY / WILEY | 0163-4445 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2057 | BIOLOGICAL RESEARCH / SOC BIOLGIA CHILE | 0717-6287 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2058 | Journal of Control, Automation and Electrical Syst / Unknown | 2195-3880 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2059 | Studia Iuridica Lublinensia Wydawnictwo Uniwersyte / Unknown | 2449-8289 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2060 | Revista Espanola de Patologia Ediciones Doyma, S.L / Unknown | 1988-561X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2061 | COLLECTANEA MATHEMATICA / SPRINGER-VERLAG ITALIA SRL | 0010-0757 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2062 | JOURNAL OF MICROWAVE POWER  AND ELECTROMAGNETIC EN / TAYLOR & FRANCIS INC | 0832-7823 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2063 | JOURNAL OF EXPERIMENTAL ZOOLOGY  PART A-ECOLOGICAL / WILEY | 2471-5638 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2064 | DEVELOPING WORLD BIOETHICS / WILEY | 1471-8731 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2065 | JOURNAL OF HYMENOPTERA  RESEARCH / PENSOFT PUBLISHERS | 1070-9428 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2066 | Journal of Echocardiography Springer Japan / Unknown | 1349-0222 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2067 | EUROPEAN JOURNAL OF INDUSTRIAL  RELATIONS / SAGE PUBLICATIONS LTD | 0959-6801 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2068 | DRVNA INDUSTRIJA / ZAGREB UNIV, FAC FORESTRY | 1847-1153 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2069 | IEEE Journal of Radio Frequency Identification Ins / Unknown | 2469-7281 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2070 | IEEE Journal of Radio Frequency Identification / Unknown | 2469-729X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2071 | Current Cardiovascular Imaging Reports Current Med / Unknown | 1941-9074 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2072 | South African Journal of Childhood Education OpenJ / Unknown | 2223-7682 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2073 | Hepatoma Research OAE Publishing Inc. / N°   ISSN   E-ISSN | 2454-2520 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2074 | Journal of Entrepreneurship in Emerging Economies  / Unknown | 2053-4604 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2075 | EVOLUTION LETTERS / OXFORD UNIV PRESS | 2056-3744 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2076 | International Journal for Computational Civil and  / Unknown | 2588-0195 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2077 | LANGUAGE LEARNING AND  DEVELOPMENT / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1547-3341 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2078 | Food Chemistry: Molecular Sciences Elsevier B.V. / Unknown | 2666-5662 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2079 | Russian Journal of Woman and Child Health Meditsin / Unknown | 2686-7184 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2080 | Antropologicheskij Forum Peter the Great Museum of / Unknown | 1815-8889 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2081 | Journal of Magazine Media University of Nebraska P / Unknown | 2576-7895 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2082 | Integrative and Complementary Therapies Mary Ann L / Unknown | 2768-3192 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2083 | Journal of Contemporary East Asia Studies Routledg / Unknown | 2476-1036 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2084 | Advances in Operations Research John Wiley and Son / Unknown | 1687-9147 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2085 | Review of Evolutionary Political Economy Springer  / Unknown | 2662-6136 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2086 | Meteorologica Centro Argentino de Meteorologos / Unknown | 0325-187X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2087 | Meteorologica / Unknown | 2347-0364 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2088 | Note di Matematica Pitagora Editrice / Unknown | 1590-0932 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2089 | GASTROENTEROLOGY / W B SAUNDERS CO-ELSEVIER INC | 0016-5085 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2090 | PERCEPTUAL AND MOTOR SKILLS / SAGE PUBLICATIONS INC | 0031-5125 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2091 | OPHTHALMOLOGY / ELSEVIER SCIENCE INC | 0161-6420 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2092 | JOURNAL OF MEDICAL VIROLOGY / WILEY | 0146-6615 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2093 | REVISTA CLINICA ESPANOLA / EDICIONES DOYMA S A | 1578-1860 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2094 | CHILDREN AND YOUTH SERVICES  REVIEW / PERGAMON-ELSEVIER SCIENCE LTD | 0190-7409 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2095 | JOURNAL OF ARID ENVIRONMENTS / ACADEMIC PRESS LTD- ELSEVIER  SCIENCE LT | 0140-1963 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2096 | GeoJournal Springer Science and Business Media Deu / Unknown | 0343-2521 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2097 | BOUNDARY-LAYER METEOROLOGY / SPRINGER | 0006-8314 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2098 | NMR IN BIOMEDICINE / WILEY | 0952-3480 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2099 | HUMAN & EXPERIMENTAL  TOXICOLOGY / SAGE PUBLICATIONS LTD | 0960-3271 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2100 | JOURNAL OF SOIL AND WATER  CONSERVATION / TAYLOR & FRANCIS LTD | 0022-4561 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2101 | INDIAN JOURNAL OF ORTHOPAEDICS / SPRINGER HEIDELBERG | 0019-5413 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2102 | Semergen Ediciones Doyma, S.L. / Unknown | 1578-8865 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2103 | NANO-MICRO LETTERS / SHANGHAI JIAO TONG UNIV PRESS | 2311-6706 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2104 | INTERNATIONAL JOURNAL OF NUMBER  THEORY / WORLD SCIENTIFIC PUBL CO PTE  LTD | 1793-0421 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2105 | BREASTFEEDING MEDICINE / MARY ANN LIEBERT, INC | 1556-8253 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2106 | REVIEWS IN MEDICAL VIROLOGY / WILEY | 1052-9276 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2107 | Scientia Sinica Mathematica Science Press / Unknown | 1674-7216 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2108 | INTERNATIONAL JOURNAL OF  CIRCUMPOLAR HEALTH / TAYLOR & FRANCIS LTD | 1239-9736 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2109 | JOURNAL OF REAL-TIME IMAGE  PROCESSING / SPRINGER HEIDELBERG | 1861-8200 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2110 | CRITICAL REVIEWS IN ANALYTICAL  CHEMISTRY / TAYLOR & FRANCIS INC | 1040-8347 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2111 | JOURNAL OF INTEGRATIVE  NEUROSCIENCE / IMR PRESS | 1757-448X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2112 | DATA MINING AND KNOWLEDGE  DISCOVERY / SPRINGER | 1384-5810 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2113 | NATURAL RESOURCE MODELING / WILEY | 0890-8575 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2114 | Zanco Journal of Pure and Applied Sciences Salahad / Unknown | 2412-3986 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2115 | European Journal of Psychotherapy and Counselling  / Unknown | 1469-5901 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2116 | Gazeta de Antropologia Univesidad de Granada / Unknown | 2340-2792 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2117 | CURRENT COMPUTER-AIDED DRUG  DESIGN / BENTHAM SCIENCE PUBL LTD | 1573-4099 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2118 | SCHOOL PSYCHOLOGY / EDUCATIONAL PUBLISHING  FOUNDATION-AMERI | 2578-4218 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2119 | Iranian Rehabilitation Journal University of Socia / N°   ISSN   E-ISSN | 1735-3610 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2120 | MEDICINA DELLO SPORT / EDIZIONI MINERVA MEDICA | 0025-7826 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2121 | ACTAS ESPANOLAS DE PSIQUIATRIA / JUAN JOSE LOPEZ-IBOR  FOUNDATION | 1578-2735 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2122 | Journal of Information and Communication Technolog / Unknown | 2180-3862 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2123 | ADVANCES IN ASTRONOMY / WILEY | 1687-7969 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2124 | Acta Silvatica et Lignaria Hungarica University of / Unknown | 1787-064X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2125 | Bulletin of Kamchatka Regional Association Educati / Unknown | 1816-5532 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2126 | Exploratory Animal and Medical Research West Benga / Unknown | 2319-247X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2127 | Journal of Global Faultlines Pluto Journals / Unknown | 2397-7825 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2128 | Economic History of Developing Regions Taylor and  / Unknown | 2078-0389 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2129 | Magyar Onkologia Akademiai Kiado / Unknown | 0025-0244 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2130 | International Journal of Chinese Linguistics John  / Unknown | 2213-8706 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2131 | ASEAN Journal of Science and Engineering Universit / Unknown | 2776-6098 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2132 | CROP SCIENCE / WILEY | 0011-183X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2133 | ATMOSPHERIC ENVIRONMENT / PERGAMON-ELSEVIER SCIENCE LTD | 1352-2310 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2134 | FRONTIERS IN PSYCHIATRY / FRONTIERS MEDIA SA | 1664-0640 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2135 | INTERNATIONAL RELATIONS / SAGE PUBLICATIONS LTD | 0047-1178 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2136 | EUROPEAN JOURNAL OF FOREST  RESEARCH / SPRINGER | 1612-4669 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2137 | JOURNAL OF BIOMATERIALS SCIENCE- POLYMER EDITION / TAYLOR & FRANCIS LTD | 0920-5063 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2138 | OCEAN DYNAMICS / SPRINGER HEIDELBERG | 1616-7228 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2139 | NUCLEAR DATA SHEETS / ACADEMIC PRESS INC ELSEVIER  SCIENCE | 0090-3752 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2140 | INTERNATIONAL JOURNAL OF  COMPUTER INTEGRATED  MAN / TAYLOR & FRANCIS LTD | 0951-192X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2141 | JOURNAL OF SOUTHERN AFRICAN  STUDIES / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 0305-7070 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2142 | SOUTHWESTERN ENTOMOLOGIST / SOUTHWESTERN ENTOMOLOGICAL  SOC | 2162-2647 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2143 | AQUATIC MAMMALS / EUROPEAN ASSOC AQUATIC  MAMMALS | 1996-7292 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2144 | Strabismus Taylor and Francis Ltd. / Unknown | 0927-3972 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2145 | Journal of Distribution Science KODISA Foundation / Unknown | 2093-7717 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2146 | IRAN-JOURNAL OF THE BRITISH  INSTITUTE OF PERSIAN  / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 0578-6967 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2147 | OPEN HOUSE INTERNATIONAL- SUSTAINABLE & SMART ARCH / EMERALD GROUP PUBLISHING LTD | 0168-2601 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2148 | Medicinal Plants - International Journal of Phytom / Unknown | 0975-4261 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2149 | JOURNAL OF DESTINATION  MARKETING & MANAGEMENT / ELSEVIER | 2212-571X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2150 | International Review of Victimology SAGE Publicati / Unknown | 0269-7580 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2151 | Vegueta University of Las Palmas de Gran Canaria,  / Unknown | 2341-1112 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2152 | MOVING IMAGE / UNIV MINNESOTA PRESS | 1542-4235 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2153 | African Journal of Laboratory Medicine AOSIS (Pty) / Unknown | 2225-2010 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2154 | Journal of Historical Research in Marketing Emeral / Unknown | 1755-750X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2155 | HISTORICAL REFLECTIONS-REFLEXIONS  HISTORIQUES / BERGHAHN JOURNALS | 1939-2419 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2156 | ACOUSTICS AUSTRALIA / SPRINGER SINGAPORE PTE LTD | 0814-6039 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2157 | ZEITSCHRIFT FUR DIALEKTOLOGIE UND  LINGUISTIK / FRANZ STEINER VERLAG GMBH | 2366-2395 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2158 | Squalen Bulletin of Marine and Fisheries Postharve / Unknown | 2406-9272 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2159 | International Journal of Noncommunicable Diseases  / Unknown | 2468-8827 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2160 | HONG KONG JOURNAL OF  OCCUPATIONAL THERAPY / SAGE PUBLICATIONS LTD | 1569-1861 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2161 | JOURNAL OF MATHEMATICS AND  MUSIC / TAYLOR & FRANCIS LTD | 1745-9737 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2162 | Media e Jornalismo Instituto de Comunicacao da NOV / Unknown | 2183-5462 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2163 | Nordic Journal of Educational History University o / Unknown | 2001-9076 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2164 | Chinese Journal of Academic Radiology Springer / Unknown | 2520-8985 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2165 | Revista Iberoamericana de Psicologia y Salud Edici / Unknown | 2171-2069 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2166 | Study Abroad Research in Second Language Acquisiti / Unknown | 2405-5522 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2167 | Spool TU Delft Open / Unknown | 2215-0900 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2168 | RENDICONTI LINCEI-SCIENZE FISICHE E  NATURALI / SPRINGER-VERLAG ITALIA SRL | 2037-4631 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2169 | Rendiconti Lincei Springer Science and Business Me / Unknown | 2385-2623 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2170 | JOURNAL OF BIOLOGICAL CHEMISTRY / ELSEVIER | 1083-351X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2171 | JOURNAL OF MATERIALS ENGINEERING  AND PERFORMANCE / SPRINGER | 1059-9495 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2172 | IEEE JOURNAL OF SELECTED TOPICS IN  APPLIED EARTH  / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 1939-1404 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2173 | PANCREATOLOGY / ELSEVIER | 1424-3903 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2174 | ACTAS UROLOGICAS ESPANOLAS / ELSEVIER ESPANA | 0210-4806 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2175 | TOXICS / MDPI | 2305-6304 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2176 | DEVELOPMENT GROWTH &  DIFFERENTIATION / WILEY | 0012-1592 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2177 | STATISTICAL METHODS IN MEDICAL  RESEARCH / SAGE PUBLICATIONS LTD | 0962-2802 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2178 | AQUACULTURE NUTRITION / WILEY | 1353-5773 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2179 | Enfermeria Clinica Elsevier Espana S.L.U / Unknown | 1130-8621 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2180 | CIRCULATION-ARRHYTHMIA AND  ELECTROPHYSIOLOGY / LIPPINCOTT WILLIAMS & WILKINS | 1941-3084 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2181 | JOURNAL OF EDUCATIONAL  ADMINISTRATION / EMERALD GROUP PUBLISHING LTD | 0957-8234 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2182 | ZEITSCHRIFT FUR ASSYRIOLOGIE UND  VORDERASIATISCHE / WALTER DE GRUYTER GMBH | 0084-5299 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2183 | Journal of the Korean Wood Science and Technology  / Unknown | 2233-7180 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2184 | Journal of Financial Crime Emerald Group Publishin / Unknown | 1359-0790 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2185 | Paediatria Croatica Children's University Hospital / Unknown | 1846-405X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2186 | Journal of Micro/Nanolithography MEMS and MOEMS / Unknown | 1932-5134 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2187 | JOURNAL OF AGING STUDIES / ELSEVIER SCIENCE INC | 0890-4065 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2188 | SEXUALITY RESEARCH AND SOCIAL  POLICY / SPRINGER | 1553-6610 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2189 | INTERNATIONAL JOURNAL OF SPORT  NUTRITION AND EXER / HUMAN KINETICS PUBL INC | 1526-484X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2190 | Twentieth Century British History Oxford Universit / Unknown | 0955-2359 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2191 | GEOSCIENCES JOURNAL / GEOLOGICAL SOCIETY KOREA | 1598-7477 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2192 | Arquivos brasileiros de cirurgia digestiva : ABCD  / Unknown | 2317-6326 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2193 | Journal of Health Management Sage Publications Ind / Unknown | 0972-0634 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2194 | MULTIDIMENSIONAL SYSTEMS AND  SIGNAL PROCESSING / SPRINGER | 0923-6082 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2195 | AUSTRALIAN SYSTEMATIC BOTANY / CSIRO PUBLISHING | 1030-1887 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2196 | Eng Multidisciplinary Digital Publishing Institute / Unknown | 2673-4117 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2197 | COMMUNITY ECOLOGY / SPRINGER HEIDELBERG | 1585-8553 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2198 | COMPARATIVE EUROPEAN POLITICS / PALGRAVE MACMILLAN LTD | 1472-4790 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2199 | Environmental Processes Springer Science and Busin / Unknown | 2198-7491 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2200 | Asian Review of Accounting Emerald Group Publishin / Unknown | 1321-7348 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2201 | Teaching Artist Journal Routledge / Unknown | 1541-180X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2202 | International Journal of Reconfigurable and Embedd / Unknown | 2089-4864 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2203 | Slavica Slovaca Jan Stanislav Institute of Slavist / Unknown | 1336-2364 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2204 | eFood John Wiley and Sons Inc / Unknown | 2666-3066 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2205 | International Journal of Nanoelectronics and Mater / Unknown | 2232-1535 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2206 | ZEITSCHRIFT FUR HISTORISCHE  FORSCHUNG / DUNCKER AND HUMBLOT GMBH | 1865-5599 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2207 | World Journal of Entrepreneurship, Management and  / Unknown | 2042-597X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2208 | HOME CULTURES / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1740-6315 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2209 | Bridge Structures SAGE Publications Ltd / Unknown | 1573-2487 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2210 | Prace Filologiczne. Literaturoznawstwo University  / Unknown | 2658-2503 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2211 | Geographies Multidisciplinary Digital Publishing I / Unknown | 2673-7086 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2212 | Journal of ASEAN Studies Bina Nusantara University / Unknown | 2338-1361 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2213 | GEOGRAPHICAL JOURNAL / WILEY | 0016-7398 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2214 | JOURNAL OF BONE AND MINERAL  RESEARCH / OXFORD UNIV PRESS | 0884-0431 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2215 | PRAKTISCHE METALLOGRAPHIE- PRACTICAL METALLOGRAPHY / WALTER DE GRUYTER GMBH | 0032-678X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2216 | CAHIERS DE CIVILISATION MEDIEVALE / CENTRE ETUD SUPERIEUR CIV MED | 2119-1026 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2217 | BRITISH JOURNAL OF EDUCATIONAL  PSYCHOLOGY / WILEY | 0007-0998 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2218 | MINERALIUM DEPOSITA / SPRINGER | 0026-4598 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2219 | Art Documentation University of Chicago Press / Unknown | 0730-7187 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2220 | LANGUAGE SCIENCES / ELSEVIER SCI LTD | 0388-0001 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2221 | SOUTH AFRICAN JOURNAL OF  PSYCHOLOGY / SAGE PUBLICATIONS LTD | 0081-2463 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2222 | HARVARD JOURNAL OF ASIATIC  STUDIES / HARVARD-YENCHING INST | 1944-6454 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2223 | JOURNAL OF WORLD HISTORY / UNIV HAWAII PRESS | 1527-8050 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2224 | JOURNAL OF HEALTH POPULATION  AND NUTRITION / BMC | 1606-0997 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2225 | JOURNAL OF CHILDRENS  ORTHOPAEDICS / SAGE PUBLICATIONS INC | 1863-2521 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2226 | American Journal of Preventive Cardiology Elsevier / Unknown | 2666-6677 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2227 | Reading Psychology Taylor and Francis Ltd. / Unknown | 0270-2711 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2228 | Iconos FLACSO Ecuador / Unknown | 1390-8065 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2229 | JOURNAL OF TURBULENCE / TAYLOR & FRANCIS LTD | 1468-5248 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2230 | Global Pediatric Health SAGE Publications Inc. / Unknown | 2333-794X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2231 | Ingeniare Universidad de Tarapaca / Unknown | 0718-3305 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2232 | WOMANS ART JOURNAL / OLD CITY PUBLISHING INC | 2158-8457 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2233 | INTERNATIONAL JOURNAL OF LAW IN  CONTEXT / CAMBRIDGE UNIV PRESS | 1744-5523 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2234 | LOGOPEDICS PHONIATRICS VOCOLOGY / TAYLOR & FRANCIS LTD | 1401-5439 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2235 | STOCHASTIC MODELS / TAYLOR & FRANCIS INC | 1532-4214 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2236 | Japanese Journal of Chemotherapy Japanese Society  / Unknown | 1884-5886 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2237 | International Journal of Technology, Policy and Ma / Unknown | 1468-4322 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2238 | Condensed Matter and Interphases Voronezh State Un / Unknown | 2687-0711 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2239 | Shengwu Gongcheng Xuebao/Chinese Journal of Biotec / Unknown | 1872-2075 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2240 | JOURNAL OF SPECTRAL THEORY / EUROPEAN MATHEMATICAL SOC- EMS | 1664-039X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2241 | Contratexto Universidad de Lima / Unknown | 1993-4904 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2242 | Economia Agro-Alimentare FrancoAngeli / Unknown | 1972-4802 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2243 | Projeto Historia Pontifícia Universidade Católica  / Unknown | 2176-2767 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2244 | Proceedings of the National Academy of Sciences of / Unknown | 2524-2350 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2245 | International Journal of E-Services and Mobile App / Unknown | 1941-6288 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2246 | Journal of Patient Safety and Risk Management SAGE / Unknown | 2516-0435 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2247 | Journal of European Tort Law Walter de Gruyter Gmb / Unknown | 1868-9612 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2248 | Ilahiyat Studies Bursa IlahIyat Foundation / Unknown | 1309-1786 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2249 | CHEST Pulmonary Elsevier B.V. / Unknown | 2949-7892 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2250 | International Journal of Mathematics and Physics a / Unknown | 2409-5508 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2251 | PSYCHOLOGICAL SCIENCE IN THE  PUBLIC INTEREST / SAGE PUBLICATIONS LTD | 1539-6053 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2252 | Communications in Applied and Industrial Mathemati / Unknown | 2038-0909 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2253 | Global Privacy Law Review Wolters Kluwer / Unknown | 2666-3589 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2254 | THROMBOSIS RESEARCH / PERGAMON-ELSEVIER SCIENCE LTD | 0049-3848 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2255 | BRAIN STIMULATION / ELSEVIER SCIENCE INC | 1876-4754 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2256 | BULLETIN DU CANCER / ELSEVIER MASSON, CORPORATION  OFFICE | 0007-4551 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2257 | INTERNATIONAL JOURNAL OF APPLIED  CERAMIC TECHNOLO / WILEY | 1546-542X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2258 | ERKENNTNIS / SPRINGER | 0165-0106 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2259 | APPLIED ENGINEERING IN  AGRICULTURE / AMER SOC AGRICULTURAL &  BIOLOGICAL ENGI | 1943-7838 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2260 | RESEARCH IN AFRICAN LITERATURES / INDIANA UNIV PRESS | 1527-2044 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2261 | RESEARCH IN NURSING & HEALTH / WILEY | 0160-6891 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2262 | CLINICS IN PERINATOLOGY / W B SAUNDERS CO-ELSEVIER INC | 0095-5108 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2263 | INTERNATIONAL JOURNAL OF  COSMETIC SCIENCE / WILEY | 0142-5463 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2264 | GIFTED CHILD QUARTERLY / SAGE PUBLICATIONS INC | 0016-9862 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2265 | ACM SIGCOMM COMPUTER  COMMUNICATION REVIEW / ASSOC COMPUTING MACHINERY | 0146-4833 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2266 | SLAS DISCOVERY / ELSEVIER SCIENCE INC | 2472-5552 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2267 | International Studies Sage Publications India Pvt. / Unknown | 0020-8817 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2268 | Gastrointestinal Endoscopy Clinics of North Americ / Unknown | 1558-1950 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2269 | NETHERLANDS HEART JOURNAL / BOHN STAFLEU VAN LOGHUM BV | 1876-6250 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2270 | KOREAN JOURNAL OF PHYSIOLOGY &  PHARMACOLOGY / KOREAN JOURNAL OF PHYSIOLOGY  & PHARMACO | 2093-3827 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2271 | Genij Ortopedii Russian Ilizarov Scientific Center / Unknown | 2542-131X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2272 | EDUCATIONAL PSYCHOLOGIST / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 0046-1520 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2273 | JOURNAL OF MEDICAL BIOCHEMISTRY / SOC MEDICAL BIOCHEMISTS SERBIA | 1452-8266 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2274 | Journal of Chiropractic Medicine Elsevier Inc. / Unknown | 1556-3707 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2275 | SHAW-THE JOURNAL OF BERNARD  SHAW STUDIES / PENN STATE UNIV PRESS | 0741-5842 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2276 | Journal of Small Business and Entrepreneurship Tay / N°   ISSN   E-ISSN | 0827-6331 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2277 | History of Economics Review Informa:  Taylor & Fra / Unknown | 1037-0196 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2278 | Veterinary Medicine International John Wiley and S / Unknown | 2042-0048 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2279 | Pratique Neurologique - FMC Elsevier Masson s.r.l. / Unknown | 1878-7762 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2280 | TRAINING AND EDUCATION IN  PROFESSIONAL PSYCHOLOGY / EDUCATIONAL PUBLISHING  FOUNDATION-AMERI | 1931-3918 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2281 | GEOTECTONICS / PLEIADES PUBLISHING INC | 0016-8521 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2282 | Ilha do Desterro Universidade Federal de Santa Cat / Unknown | 2175-8026 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2283 | Frontiers in Big Data Frontiers Media SA / N°   ISSN   E-ISSN | 2624-909X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2284 | International Journal of Security and Networks Ind / Unknown | 1747-8405 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2285 | Society and Business Review Emerald Group Publishi / Unknown | 1746-5680 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2286 | IET Networks John Wiley & Sons Inc. / Unknown | 2047-4954 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2287 | Tropical Animal Science Journal Bogor Agricultural / Unknown | 2615-790X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2288 | Journal for the Study of the Pseudepigrapha SAGE P / Unknown | 0951-8207 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2289 | HEALTH PSYCHOLOGY REVIEW / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1743-7199 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2290 | Egyptian Journal of Community Medicine Egyptian Co / Unknown | 2090-2611 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2291 | Tromboz, Gemostaz i Reologiya Hemostasis and Rheol / Unknown | 2687-1483 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2292 | Journal of Engineering, Project, and Production Ma / Unknown | 2223-8379 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2293 | Russian Military Medical Academy Reports Eco-Vecto / Unknown | 2713-2323 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2294 | Compounds Multidisciplinary Digital Publishing Ins / Unknown | 2673-6918 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2295 | Journal of Settlements and Spatial Planning Centre / Unknown | 2248-2199 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2296 | JOURNAL OF ELECTRONIC COMMERCE  RESEARCH / CALIFORNIA STATE UNIV | 1938-9027 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2297 | SAE International Journal of Electrified Vehicles  / Unknown | 2691-3755 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2298 | Quaestio Facti University of Girona / Unknown | 2660-4515 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2299 | CLASSICAL REVIEW / CAMBRIDGE UNIV PRESS | 0009-840X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2300 | JOURNAL OF NEUROLOGICAL SURGERY  PART B-SKULL BASE / THIEME MEDICAL PUBL INC | 2193-6331 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2301 | CONCURRENCY AND COMPUTATION- PRACTICE & EXPERIENCE / WILEY | 1532-0626 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2302 | IEEE TRANSACTIONS ON CYBERNETICS / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 2168-2267 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2303 | JOURNAL OF NURSING EDUCATION / SLACK INC | 0148-4834 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2304 | CELL TRANSPLANTATION / SAGE PUBLICATIONS INC | 0963-6897 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2305 | GLYCOBIOLOGY / OXFORD UNIV PRESS INC | 0959-6658 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2306 | JOURNALS OF GERONTOLOGY SERIES  B-PSYCHOLOGICAL SC / OXFORD UNIV PRESS INC | 1079-5014 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2307 | Journal of Physical Education and Sport Editura Un / Unknown | 2247-806X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2308 | RESEARCH IN SOCIAL &  ADMINISTRATIVE PHARMACY / ELSEVIER SCIENCE INC | 1551-7411 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2309 | NANOMEDICINE / TAYLOR & FRANCIS LTD | 1743-5889 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2310 | GLOBAL ECOLOGY AND  BIOGEOGRAPHY / WILEY | 1466-822X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2311 | VETERINARY ANAESTHESIA AND  ANALGESIA / ELSEVIER | 1467-2987 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2312 | COUNSELING PSYCHOLOGIST / SAGE PUBLICATIONS INC | 0011-0000 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2313 | MINERALOGY AND PETROLOGY / SPRINGER WIEN | 0930-0708 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2314 | Physics of Particles and Nuclei Letters Pleiades P / Unknown | 1531-8567 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2315 | JOURNAL OF AUSTRALIAN STUDIES / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1444-3058 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2316 | LIBRI-INTERNATIONAL JOURNAL OF  LIBRARIES AND INFO / WALTER DE GRUYTER GMBH | 0024-2667 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2317 | JOURNAL OF THE AMERICAN ANIMAL  HOSPITAL ASSOCIATI / AMER ANIMAL HOSPITAL ASSOC | 1547-3317 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2318 | MECHANICS BASED DESIGN OF  STRUCTURES AND MACHINES / TAYLOR & FRANCIS INC | 1539-7734 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2319 | EUROPEAN JOURNAL OF CELL BIOLOGY / ELSEVIER GMBH | 0171-9335 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2320 | ARCHIVES OF WOMENS MENTAL  HEALTH / SPRINGER WIEN | 1434-1816 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2321 | QUEUEING SYSTEMS / SPRINGER | 0257-0130 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2322 | SAECULUM / BOEHLAU VERLAG GMBH & CIE | 2194-4075 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2323 | LIMNOLOGICA / ELSEVIER GMBH | 0075-9511 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2324 | KI - Kunstliche Intelligenz Springer International / Unknown | 0933-1875 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2325 | Kufa Journal of Engineering University of Kufa / Unknown | 2523-0018 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2326 | European Journal of Physiotherapy Informa Healthca / Unknown | 2167-9177 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2327 | JOURNAL OF SHIP PRODUCTION AND  DESIGN / SOC NAVAL ARCHITECTS & MARINE  ENGINEERS | 2158-2874 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2328 | ARABIC SCIENCES AND PHILOSOPHY / CAMBRIDGE UNIV PRESS | 0957-4239 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2329 | Creativity Studies Vilnius Gediminas Technical Uni / Unknown | 2345-0487 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2330 | JOURNAL ON MULTIMODAL USER  INTERFACES / SPRINGER | 1783-7677 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2331 | International Journal of Medical Toxicology and Fo / Unknown | 2251-8770 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2332 | Studia Aurea Universitat Autonoma de Barcelona / Unknown | 2462-6813 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2333 | Journal of Burma Studies Center for Burma Studies  / Unknown | 2010-314X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2334 | Cyborg and Bionic Systems American Association for / Unknown | 2097-1087 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2335 | CYBORG AND BIONIC SYSTEMS / AMER ASSOC ADVANCEMENT  SCIENCE | 2692-7632 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2336 | GEOFIZIKA / UNIV ZAGREB , ANDRIJA  MOHOROVICIC GEOPH | 1846-6346 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2337 | Magnetic Resonance Letters KeAi Communications Co. / Unknown | 2772-5162 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2338 | Convergencias: Revista de Investigacao e Ensino da / Unknown | 2184-0180 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2339 | Biophysical Bulletin V N Karazin Kharkiv National  / Unknown | 2075-3829 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2340 | International Journal of Euro-Mediterranean Studie / Unknown | 2232-6022 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2341 | JOURNAL OF ELECTRONIC MATERIALS / SPRINGER | 0361-5235 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2342 | PEPTIDES / ELSEVIER SCIENCE INC | 0196-9781 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2343 | JOURNAL OF CRITICAL CARE / W B SAUNDERS CO-ELSEVIER INC | 0883-9441 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2344 | INFORMES DE LA CONSTRUCCION / CONSEJO SUPERIOR  INVESTIGACIONES CIENTI | 1988-3234 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2345 | CURRENT OPINION IN IMMUNOLOGY / CURRENT BIOLOGY LTD | 1879-0372 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2346 | BIOSYSTEMS ENGINEERING / ACADEMIC PRESS INC ELSEVIER  SCIENCE | 1537-5110 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2347 | Assiut Veterinary Medical Journal (Egypt) Assiut U / Unknown | 2314-5226 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2348 | CURRENT OPINION IN CARDIOLOGY / LIPPINCOTT WILLIAMS & WILKINS | 0268-4705 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2349 | JOURNAL OF CONSUMER RESEARCH / OXFORD UNIV PRESS INC | 0093-5301 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2350 | BULLETIN OF THE INSTITUTE OF  CLASSICAL STUDIES / OXFORD UNIV PRESS | 0076-0730 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2351 | NEUROCIRUGIA / ELSEVIER ESPANA SLU | 1130-1473 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2352 | ANNALS OF DIAGNOSTIC PATHOLOGY / ELSEVIER SCIENCE INC | 1092-9134 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2353 | ACTA ZOOLOGICA / WILEY | 0001-7272 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2354 | Project Baikal Russian Academy of Architecture and / Unknown | 2309-3072 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2355 | MINERVA / SPRINGER | 0026-4695 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2356 | PROGRESS IN POLYMER SCIENCE / PERGAMON-ELSEVIER SCIENCE LTD | 0079-6700 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2357 | Oral and Maxillofacial Surgery Springer Verlag / Unknown | 1865-1550 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2358 | INSTRUCTIONAL SCIENCE / SPRINGER | 0020-4277 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2359 | JOURNAL OF CLINICAL NEUROLOGY / KOREAN NEUROLOGICAL ASSOC | 2005-5013 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2360 | SINGAPORE JOURNAL OF TROPICAL  GEOGRAPHY / WILEY | 0129-7619 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2361 | BEHAVIOURAL NEUROLOGY / WILEY | 0953-4180 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2362 | HAU-JOURNAL OF ETHNOGRAPHIC  THEORY / UNIV CHICAGO PRESS | 2049-1115 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2363 | JOURNAL OF OCCUPATIONAL HEALTH  PSYCHOLOGY / EDUCATIONAL PUBLISHING  FOUNDATION-AMERI | 1076-8998 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2364 | JOURNAL OF AGRARIAN CHANGE / WILEY | 1471-0358 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2365 | Journal of Cross-Cultural Gerontology Springer New / Unknown | 0169-3816 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2366 | Journal of Pediatric Rehabilitation Medicine SAGE  / Unknown | 1874-5393 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2367 | JOURNAL OF MATHEMATICS TEACHER  EDUCATION / SPRINGER | 1386-4416 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2368 | HUMAN PERFORMANCE / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 0895-9285 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2369 | European Journal of Tourism Research International / Unknown | 1994-7658 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2370 | U.S. Geological Survey Scientific Investigations M / Unknown | 2329-132X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2371 | INFORMATION SYSTEMS AND E- BUSINESS MANAGEMENT / SPRINGER HEIDELBERG | 1617-9846 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2372 | Ecopsychology Mary Ann Liebert Inc. / Unknown | 1942-9347 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2373 | Journal of Couple and Relationship Therapy Routled / Unknown | 1533-2691 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2374 | Laboratorio de Arte University of Seville, Departm / Unknown | 2253-8305 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2375 | International Journal of Agile Systems and Managem / Unknown | 1741-9174 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2376 | South African Computer Journal South African Insti / Unknown | 2313-7835 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2377 | Bialostockie Studia Literaturoznawcze Faculty of P / Unknown | 2720-0078 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2378 | Journal of Siberian Federal University: Chemistry  / Unknown | 2313-6049 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2379 | Libri et Liberi Croatian Association of Researcher / Unknown | 1848-5871 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2380 | Muzeologia a Kulturne Dedicstvo Muzeologia a kultu / Unknown | 2453-9759 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2381 | International Journal of Space Science and Enginee / Unknown | 2048-8459 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2382 | Contact SAGE Publications Inc. / Unknown | 2515-2564 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2383 | Transactions on Energy Systems and Engineering App / Unknown | 2745-0120 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2384 | Potestas Universitat Jaume I / Unknown | 2340-499X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2385 | National Center for Health Statistics Data Brief U / Unknown | 1941-4935 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2386 | MACROMOLECULES / AMER CHEMICAL SOC | 1520-5835 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2387 | AMERICAN BIOLOGY TEACHER / NATL ASSOC BIOLOGY TEACHERS  INC | 1938-4211 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2388 | JOURNAL OF FORENSIC SCIENCES / WILEY | 0022-1198 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2389 | BIOLOGICAL TRACE ELEMENT  RESEARCH / SPRINGERNATURE | 0163-4984 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2390 | Huisarts en Wetenschap Bohn Stafleu van Loghum / Unknown | 1876-5912 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2391 | GEOTECHNIQUE / EMERALD GROUP PUBLISHING LTD | 0016-8505 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2392 | JOURNAL OF AMERICAN COLLEGE  HEALTH / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 0744-8481 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2393 | Uniform Law Review Oxford University Press / Unknown | 1124-3694 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2394 | JOURNAL OF ANALYTICAL METHODS IN  CHEMISTRY / WILEY | 2090-8865 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2395 | STUDIES IN CHRISTIAN ETHICS / SAGE PUBLICATIONS LTD | 0953-9468 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2396 | JOURNAL OF ENGINEERING DESIGN / TAYLOR & FRANCIS LTD | 0954-4828 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2397 | ASIA PACIFIC BUSINESS REVIEW / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1360-2381 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2398 | STYLE / PENN STATE UNIV PRESS | 0039-4238 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2399 | AQUATIC INSECTS / TAYLOR & FRANCIS LTD | 0165-0424 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2400 | PERIODONTOLOGY 2000 / WILEY | 0906-6713 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2401 | Central European Journal of Urology Polish Urologi / Unknown | 2080-4873 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2402 | TEXAS HEART INSTITUTE JOURNAL / TEXAS HEART INST | 1526-6702 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2403 | MANAGEMENT AND ORGANIZATION  REVIEW / CAMBRIDGE UNIV PRESS | 1740-8776 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2404 | SOUTHERN AFRICAN JOURNAL OF HIV  MEDICINE / AOSIS | 2078-6751 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2405 | ITALIAN JOURNAL OF DERMATOLOGY  AND VENEREOLOGY / EDIZIONI MINERVA MEDICA | 2784-8450 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2406 | EURASIAN GEOGRAPHY AND  ECONOMICS / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1538-7216 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2407 | BRIEFINGS IN FUNCTIONAL GENOMICS / OXFORD UNIV PRESS | 2041-2649 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2408 | Proceedings of Institution of Civil Engineers: Con / Unknown | 1747-6518 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2409 | BRITISH POLITICS / PALGRAVE MACMILLAN LTD | 1746-918X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2410 | Oral Science International The Japanese Stomatolog / Unknown | 1881-4204 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2411 | PSICOLOGIA Associacao Portuguesa de Psicologia / Unknown | 2183-2471 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2412 | Mathematische Semesterberichte Springer Verlag / Unknown | 0720-728X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2413 | Opuholi Zenskoj Reproduktivnoj Sistemy ABV-press P / Unknown | 1999-8627 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2414 | Journal of Wireless Mobile Networks, Ubiquitous Co / Unknown | 2093-5382 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2415 | FinTech Multidisciplinary Digital Publishing Insti / Unknown | 2674-1032 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2416 | Tempo Psicanalitico Sociedade de Psicanalise Iracy / Unknown | 2316-6576 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2417 | International Journal of Ambient Computing and Int / Unknown | 1941-6245 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2418 | ACTA ADRIATICA / INST OCEANOGRAFIJU I RIBARSTVO | 1846-0453 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2419 | ACTA CARDIOLOGICA SINICA / TAIWAN SOC CARDIOLOGY | 1011-6842 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2420 | Chemistry, Didactics, Ecology, Metrology Sciendo / Unknown | 1640-9019 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2421 | Current Gerontology and Geriatrics Research John W / Unknown | 1687-7063 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2422 | Fatigue of Aircraft Structures De Gruyter Open Ltd / Unknown | 2081-7738 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2423 | Migracijske i Etnicke Teme Institute for Migration / Unknown | 1848-9184 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2424 | Journal of Medicinal Plants for Economic Developme / Unknown | 2616-4809 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2425 | ACDI Anuario Colombiano de Derecho Internacional U / N°   ISSN   E-ISSN | 2145-4493 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2426 | BIOPHARM INTERNATIONAL / ADVANSTAR COMMUNICATIONS  INC | 1939-1862 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2427 | EUROPEAN JOURNAL OF CLINICAL  INVESTIGATION / WILEY | 0014-2972 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2428 | FITOTERAPIA / ELSEVIER | 0367-326X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2429 | Clinical Ophthalmology Dove Medical Press Ltd. / Unknown | 1177-5483 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2430 | INDIAN JOURNAL OF GENETICS AND  PLANT BREEDING / INDIAN SOC GENET PLANT  BREEDING | 0975-6906 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2431 | CELL PROLIFERATION / WILEY | 0960-7722 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2432 | AQUATIC BOTANY / ELSEVIER | 0304-3770 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2433 | CONTEMPORARY PHYSICS / TAYLOR & FRANCIS LTD | 0010-7514 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2434 | JOURNAL OF COMPARATIVE  PHYSIOLOGY B-BIOCHEMICAL S / SPRINGER HEIDELBERG | 0174-1578 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2435 | JOURNAL OF IMMIGRANT AND  MINORITY HEALTH / SPRINGER | 1557-1912 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2436 | WATER RESOURCES / MAIK  NAUKA/INTERPERIODICA/SPRINGER | 0097-8078 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2437 | Pouvoirs: Revue d'Etudes Constitutionnelles et Pol / Unknown | 2101-0390 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2438 | SCOTTISH JOURNAL OF POLITICAL  ECONOMY / WILEY | 0036-9292 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2439 | SYSTEMATIC ENTOMOLOGY / WILEY | 0307-6970 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2440 | CURRENT ATHEROSCLEROSIS REPORTS / CURRENT MEDICINE GROUP | 1534-6242 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2441 | Keio Journal of Medicine Keio University School of / Unknown | 1880-1293 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2442 | Epistemology and Philosophy of Science Institute o / Unknown | 2311-7133 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2443 | Asian Journal of Civil Engineering Springer Nature / Unknown | 1563-0854 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2444 | SPORTS HEALTH-A MULTIDISCIPLINARY  APPROACH / SAGE PUBLICATIONS INC | 1941-0921 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2445 | Economic and Environmental Geology The Korean Soci / Unknown | 2288-7962 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2446 | WETLANDS ECOLOGY AND  MANAGEMENT / SPRINGER | 0923-4861 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2447 | Functional Materials National Academy of Sciences  / Unknown | 2218-2993 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2448 | AFRICAN DEVELOPMENT REVIEW- REVUE AFRICAINE DE DEV / WILEY | 1017-6772 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2449 | International Journal of Continuing Engineering Ed / Unknown | 1560-4624 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2450 | JOURNAL OF ARABIC LITERATURE / BRILL | 0085-2376 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2451 | REVISTA DE HISTORIA INDUSTRIAL / UNIV BARCELONA, DEPT HISTORIA,  INST ECO | 2385-3247 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2452 | Orthopedic Reviews Open Medical Publishing / Unknown | 2035-8237 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2453 | Journal of Food Products Marketing Routledge / Unknown | 1540-4102 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2454 | Sententiae Vinnytsia National Technical University / Unknown | 2308-8915 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2455 | International Journal of Biometrics Inderscience E / Unknown | 1755-8301 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2456 | ACADEMY OF MANAGEMENT ANNALS / ACAD MANAGEMENT | 1941-6520 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2457 | Competition and Regulation in Network Industries S / Unknown | 1783-5917 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2458 | International Journal of Decision Support System T / Unknown | 1941-630X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2459 | ANNUAL REVIEW OF ANALYTICAL  CHEMISTRY / ANNUAL REVIEWS | 1936-1327 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2460 | JOURNAL OF MATHEMATICAL PHYSICS  ANALYSIS GEOMETRY / B. VERKIN INST LOW TEMPERATURE  PHYSICS  | 1817-5805 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2461 | Ibsen Studies Routledge / Unknown | 1741-8720 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2462 | International Journal of Fluid Mechanics Research  / Unknown | 2152-5102 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2463 | ANNUAL REVIEW OF ORGANIZATIONAL  PSYCHOLOGY AND OR / ANNUAL REVIEWS | 2327-0608 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2464 | Middle East Development Journal Routledge / Unknown | 1793-8171 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2465 | Journal of Conflict Archaeology Maney Publishing / Unknown | 1574-0781 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2466 | Cardiovascular Digital Health Journal Elsevier Inc / Unknown | 2666-6936 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2467 | Pakistan Journal of Engineering and Applied Scienc / Unknown | 2415-0584 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2468 | Feminist Anthropology John Wiley and Sons Inc / Unknown | 2643-7961 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2469 | Journal of Second Language Studies John Benjamins  / Unknown | 2542-3835 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2470 | FRENCH JOURNAL OF UROLOGY / ELSEVIER MASSON, CORPORATION  OFFICE | 2950-4201 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2471 | JOURNAL OF ANTIBIOTICS / SPRINGERNATURE | 0021-8820 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2472 | NEUROLOGIA MEDICO-CHIRURGICA / JAPAN NEUROSURGICAL SOC | 1349-8029 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2473 | IMMUNOLOGY AND CELL BIOLOGY / WILEY | 0818-9641 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2474 | NEUROGASTROENTEROLOGY AND  MOTILITY / WILEY | 1350-1925 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2475 | SOLAR RRL / WILEY-V C H VERLAG GMBH | 2367-198X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2476 | JOURNAL OF HISTOTECHNOLOGY / TAYLOR & FRANCIS LTD | 0147-8885 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2477 | INTEGRATION-THE VLSI JOURNAL / ELSEVIER | 0167-9260 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2478 | INTERNATIONAL JOURNAL OF  PHYTOREMEDIATION / TAYLOR & FRANCIS INC | 1522-6514 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2479 | New Directions for Teaching and Learning Wiley-Bla / Unknown | 0271-0633 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2480 | IEEE-CAA JOURNAL OF AUTOMATICA  SINICA / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 2329-9266 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2481 | ARCHIVES OF BIOLOGICAL SCIENCES / INST BIOLOSKA ISTRAZIVANJA  SINISA STANK | 1821-4339 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2482 | JOURNAL OF SHELLFISH RESEARCH / NATL SHELLFISHERIES ASSOC | 1943-6319 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2483 | GRASAS Y ACEITES / CONSEJO SUPERIOR  INVESTIGACIONES CIENTI | 1988-4214 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2484 | ENVIRONMENT AND URBANIZATION / SAGE PUBLICATIONS LTD | 0956-2478 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2485 | EVOLUTIONARY ANTHROPOLOGY / WILEY | 1060-1538 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2486 | JOURNAL OF WORLD BUSINESS / ELSEVIER SCIENCE INC | 1090-9516 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2487 | JOURNAL OF VETERINARY DENTISTRY / SAGE PUBLICATIONS INC | 0898-7564 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2488 | HISTORY OF SCIENCE / SAGE PUBLICATIONS LTD | 0073-2753 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2489 | FRONTIERS IN  NEUROENDOCRINOLOGY / ACADEMIC PRESS INC ELSEVIER  SCIENCE | 0091-3022 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2490 | Human Affairs Walter de Gruyter GmbH / Unknown | 1210-3055 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2491 | AUGUSTINIAN STUDIES / PHILOSOPHY DOCUMENTATION  CENTER | 2153-7917 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2492 | CURRENT GENE THERAPY / BENTHAM SCIENCE PUBL LTD | 1566-5232 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2493 | CHILDHOOD-A GLOBAL JOURNAL OF  CHILD RESEARCH / SAGE PUBLICATIONS LTD | 0907-5682 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2494 | SPIRITUS-A JOURNAL OF CHRISTIAN  SPIRITUALITY / JOHNS HOPKINS UNIV PRESS | 1535-3117 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2495 | FEMINIST THEOLOGY / SAGE PUBLICATIONS LTD | 0966-7350 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2496 | JOURNAL OF INNATE IMMUNITY / KARGER | 1662-811X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2497 | COST EFFECTIVENESS AND RESOURCE  ALLOCATION / BMC | 1478-7547 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2498 | Renaissance Drama University of Chicago Press / Unknown | 0486-3739 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2499 | Annales Mathematiques Blaise Pascal Universite Cle / N°   ISSN   E-ISSN | 2118-7436 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2500 | Shedet Fayoum University, Faculty of Archaeology / Unknown | 2536-9954 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2501 | Resital Faculty of Performing Arts, Institut Seni  / N°   ISSN   E-ISSN | 2338-6770 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2502 | SAE International Journal of Transportation Safety / N°   ISSN   E-ISSN | 2327-5634 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2503 | Uchenye Zapiski Kazanskogo Universiteta. Seriya Es / Unknown | 2542-064X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2504 | GEMATOLOGIYA I TRANSFUZIOLOGIYA / MINISTERSTVO  ZDRAVOOKHRANENIYA | 2411-3042 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2505 | WORLD LITERATURE STUDIES / INST WORLD LITERATURE, SLOVAK  ACAD SCIE | 1337-9690 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2506 | Unnes Journal of Public Health Universitas Negeri  / Unknown | 2548-7604 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2507 | Schutzian Research Zeta Books / Unknown | 2248-1907 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2508 | Elia Universidad de Sevilla / Unknown | 2253-8283 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2509 | Indian Journal of Engineering Discovery Scientific / Unknown | 2319-7765 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2510 | Health Education and Health Promotion Tarbiat Moda / Unknown | 2588-5715 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2511 | Journal of Health System Research Isfahan Universi / Unknown | 2783-4093 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2512 | GEOTECHNIQUE LETTERS / EMERALD GROUP PUBLISHING LTD | 2049-825X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2513 | Key Issues in Teacher Education: Policy, Research  / Unknown | 2772-5979 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2514 | Dynamics of Continuous, Discrete and Impulsive Sys / Unknown | 1492-8760 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2515 | AMERICAN JOURNAL OF PHYSICAL  MEDICINE & REHABILIT / LIPPINCOTT WILLIAMS & WILKINS | 0894-9115 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2516 | POLAR RECORD / CAMBRIDGE UNIV PRESS | 0032-2474 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2517 | EUROPEAN JOURNAL OF PAIN / WILEY | 1090-3801 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2518 | ANNALS OF MATHEMATICS / PRINCETON UNIV, DEPT  MATHEMATICS | 1939-8980 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2519 | XENOBIOTICA / TAYLOR & FRANCIS LTD | 0049-8254 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2520 | NONLINEARITY / IOP PUBLISHING LTD | 1361-6544 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2521 | EXPERIMENTAL AND MOLECULAR  PATHOLOGY / ACADEMIC PRESS INC ELSEVIER  SCIENCE | 0014-4800 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2522 | MEDICINAL CHEMISTRY RESEARCH / SPRINGER BIRKHAUSER | 1054-2523 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2523 | STEREOTACTIC AND FUNCTIONAL  NEUROSURGERY / KARGER | 1011-6125 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2524 | JOURNAL OF INTERVENTIONAL  CARDIAC ELECTROPHYSIOLO / SPRINGER | 1383-875X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2525 | EUROPEAN JOURNAL OF ONCOLOGY  NURSING / ELSEVIER SCI LTD | 1462-3889 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2526 | VETERINARY AND COMPARATIVE  ORTHOPAEDICS AND TRAUM / GEORG THIEME VERLAG KG | 0932-0814 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2527 | Journal of the Korean Society of Clothing and Text / Unknown | 2234-0793 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2528 | KINETICS AND CATALYSIS / PLEIADES PUBLISHING INC | 0023-1584 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2529 | REVIEW OF AFRICAN POLITICAL  ECONOMY / SCIENCEOPEN | 1740-1720 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2530 | IRANIAN RED CRESCENT MEDICAL  JOURNAL / DUBAI IRANIAN HOSP | 2074-1812 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2531 | ENVIRONMENTAL MICROBIOLOGY  REPORTS / WILEY | 1758-2229 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2532 | EATING DISORDERS / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1064-0266 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2533 | JOURNAL OF DIGESTIVE DISEASES / WILEY | 1751-2972 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2534 | LANGUAGE TEACHING RESEARCH / SAGE PUBLICATIONS LTD | 1362-1688 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2535 | CHINESE MEDICINE / BMC | 1749-8546 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2536 | COSTUME-THE JOURNAL OF THE  COSTUME SOCIETY / EDINBURGH UNIV PRESS | 0590-8876 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2537 | ASIA PACIFIC VIEWPOINT / WILEY | 1360-7456 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2538 | Geofizicheskiy Zhurnal Subbotin Institute of Geoph / N°   ISSN   E-ISSN | 2524-1052 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2539 | JOURNAL OF LITERARY SEMANTICS / DE GRUYTER MOUTON | 0341-7638 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2540 | TEXTILE-CLOTH AND CULTURE / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1475-9756 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2541 | Medicina Moderna Bucharest College of Physicians / Unknown | 2360-2473 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2542 | GEOCHEMISTRY-EXPLORATION  ENVIRONMENT ANALYSIS / GEOLOGICAL SOC PUBL HOUSE | 2041-4943 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2543 | Boletim de Ciencias Geodesicas Universidade Federa / Unknown | 1982-2170 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2544 | ECOLOGICAL CHEMISTRY AND  ENGINEERING S-CHEMIA I I / SCIENDO | 1898-6196 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2545 | Contagion: Journal of Violence, Mimesis, and Cultu / Unknown | 1930-1200 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2546 | She Ji Tongji University Press / Unknown | 2405-8726 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2547 | Journal of Experimental Political Science Cambridg / Unknown | 2052-2630 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2548 | Scientific Bulletin of Mukachevo State University. / Unknown | 2518-1254 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2549 | Jurnal Ilmiah Islam Futura Universitas Islam Neger / Unknown | 2407-7542 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2550 | Law, Innovation and Technology Taylor and Francis  / N°   ISSN   E-ISSN | 1757-9961 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2551 | South Asian Journal of Human Resources Management  / Unknown | 2322-0937 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2552 | Metatheoria Editorial de la  Universidad Nacional  / Unknown | 1853-2330 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2553 | Journal of Geometry and Symmetry in Physics Bulgar / Unknown | 1314-5673 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2554 | Carbon Neutrality Springer / Unknown | 2731-3948 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2555 | WATER REUSE / IWA PUBLISHING | 2709-6092 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2556 | AMERICAN JOURNAL OF  GASTROENTEROLOGY / LIPPINCOTT WILLIAMS & WILKINS | 0002-9270 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2557 | PROTOPLASMA / SPRINGER WIEN | 0033-183X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2558 | IEEE TRANSACTIONS ON ULTRASONICS  FERROELECTRICS A / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 0885-3010 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2559 | IEEE Transactions on Ultrasonics Ferroelectrics an / Unknown | 2373-7840 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2560 | JOURNAL OF COMPOSITE MATERIALS / SAGE PUBLICATIONS LTD | 0021-9983 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2561 | INFECTION / SPRINGER HEIDELBERG | 0300-8126 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2562 | APPLIED SOIL ECOLOGY / ELSEVIER | 0929-1393 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2563 | TEACHING AND TEACHER EDUCATION / PERGAMON-ELSEVIER SCIENCE LTD | 0742-051X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2564 | BASIC & CLINICAL PHARMACOLOGY &  TOXICOLOGY / WILEY | 1742-7835 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2565 | CELL RESEARCH / SPRINGERNATURE | 1001-0602 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2566 | CONTEMPORARY CLINICAL TRIALS / ELSEVIER SCIENCE INC | 1551-7144 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2567 | JOURNAL OF CHINESE PHILOSOPHY / BRILL | 0301-8121 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2568 | REVISTA ESPANOLA DE  INVESTIGACIONES SOCIOLOGICAS / CENTRO INVESTIGACIONES  SOCIOLOGICAS | 1988-5903 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2569 | COLOMBIA MEDICA / CORPORACION EDITORA MEDICA  VALLE | 1657-9534 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2570 | CLINICAL IMPLANT DENTISTRY AND  RELATED RESEARCH / WILEY | 1523-0899 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2571 | JOURNAL OF MANAGEMENT &  ORGANIZATION / CAMBRIDGE UNIV PRESS | 1833-3672 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2572 | Journal of Posthumanism Transnational Press London / Unknown | 2634-3584 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2573 | Agricultural Science Digest Agricultural Research  / Unknown | 0976-0547 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2574 | Journal of Indian Prosthodontic Society Wolters Kl / Unknown | 0972-4052 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2575 | JOURNAL OF FOREST RESEARCH / TAYLOR & FRANCIS LTD | 1341-6979 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2576 | DEVELOPMENTAL NEUROPSYCHOLOGY / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1532-6942 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2577 | GERMAN JOURNAL OF HUMAN  RESOURCE MANAGEMENT- ZEIT / SAGE PUBLICATIONS INC | 2397-0022 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2578 | JOURNAL OF HOSPITALITY AND  TOURISM MANAGEMENT / ELSEVIER | 1447-6770 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2579 | INTERNATIONAL JOURNAL OF  SYSTEMATIC THEOLOGY / WILEY | 1463-1652 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2580 | JPAD-JOURNAL OF PREVENTION OF  ALZHEIMERS DISEASE / ELSEVIER | 2274-5807 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2581 | RADIOENGINEERING / SPOLECNOST PRO  RADIOELEKTRONICKE INZENY | 1805-9600 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2582 | CAMERA OBSCURA / DUKE UNIV PRESS | 0270-5346 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2583 | Military Balance Routledge / Unknown | 1479-9022 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2584 | BRAIN CONNECTIVITY / MARY ANN LIEBERT, INC | 2158-0014 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2585 | Asian Cinema Intellect Ltd. / Unknown | 2049-6710 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2586 | Proceedings of the Institution of Civil Engineers: / Unknown | 1751-7664 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2587 | ACTA CARSOLOGICA / KARST RESEARCH INST ZRC SAZU | 1580-2612 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2588 | Zeszyty Wiejskie Lodz University Press / Unknown | 2657-4373 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2589 | Transactions of the Atomic Energy Society of Japan / N°   ISSN   E-ISSN | 2186-2931 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2590 | International Journal of Arts and Technology Inder / Unknown | 1754-8853 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2591 | MACEDONIAN JOURNAL OF  CHEMISTRY AND CHEMICAL  ENG / SOC CHEMISTS TECHNOLOGISTS  MADECONIA | 1857-5625 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2592 | Laboratorium: Russian Review of Social Research In / Unknown | 2078-1938 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2593 | International Journal of Foresight and Innovation  / Unknown | 1740-2816 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2594 | INTERNATIONAL JOURNAL OF  OPTOMECHATRONICS / TAYLOR & FRANCIS INC | 1559-9612 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2595 | Darulfunun Ilahiyat Istanbul Universitesi / Unknown | 2651-5083 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2596 | Health and Social Care Delivery Research NIHR Jour / Unknown | 2755-0079 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2597 | Casopis za Suvremenu Povijest Croatian Institute o / Unknown | 1848-9079 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2598 | HEROIN ADDICTION AND RELATED  CLINICAL PROBLEMS / PACINI EDITORE | 1592-1638 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2599 | Heroin addiction and related clinical problems / Unknown | 2531-4122 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2600 | Studi e Saggi Linguistici Edizioni ETS / Unknown | 2281-9142 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2601 | Economia y Politica Universidad Adolfo Ibanez / N°   ISSN   E-ISSN | 0719-4803 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2602 | ORGANOMETALLICS / AMER CHEMICAL SOC | 1520-6041 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2603 | POWDER TECHNOLOGY / ELSEVIER | 0032-5910 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2604 | PHARMACOLOGICAL RESEARCH / ACADEMIC PRESS LTD- ELSEVIER  SCIENCE LT | 1043-6618 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2605 | LUNG / SPRINGER | 0341-2040 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2606 | JOURNAL OF MICROSCOPY / WILEY | 0022-2720 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2607 | STOCHASTIC PROCESSES AND THEIR  APPLICATIONS / ELSEVIER | 0304-4149 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2608 | JOURNAL OF CARDIOTHORACIC  SURGERY / BMC | 1749-8090 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2609 | NATURE REVIEWS MICROBIOLOGY / NATURE PORTFOLIO | 1740-1526 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2610 | MOLECULAR CANCER / BMC | 1476-4598 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2611 | STRUCTURAL CONCRETE / ERNST & SOHN | 1751-7648 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2612 | IEEE INTERNET COMPUTING / IEEE COMPUTER SOC | 1089-7801 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2613 | IEEE Potentials Institute of Electrical and Electr / Unknown | 0278-6648 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2614 | IEEE Potentials / Unknown | 1558-1772 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2615 | CONSERVATION GENETICS / SPRINGER | 1566-0621 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2616 | Brain Communications Oxford University Press / Unknown | 2632-1297 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2617 | JOURNAL OF EARTH SCIENCE / CHINA UNIV GEOSCIENCES, WUHAN | 1867-111X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2618 | CNS & NEUROLOGICAL DISORDERS- DRUG TARGETS / BENTHAM SCIENCE PUBL | 1871-5273 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2619 | Geogaceta Sociedad Geologica de Espana / Unknown | 2173-6545 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2620 | APPLIED MATHEMATICS-A JOURNAL OF  CHINESE UNIVERSI / ZHEJIANG UNIV PRESS | 1993-0445 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2621 | CATHOLIC BIBLICAL QUARTERLY / CATHOLIC BIBLICAL ASSOC AMER | 2163-2529 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2622 | FRONTIERS OF INFORMATION  TECHNOLOGY & ELECTRONIC  / ZHEJIANG UNIV PRESS | 2095-9184 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2623 | Journal of Personal Selling and Sales Management T / Unknown | 0885-3134 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2624 | SEED SCIENCE RESEARCH / CAMBRIDGE UNIV PRESS | 0960-2585 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2625 | Korean Journal of Adult Nursing Korean Society of  / N°   ISSN   E-ISSN | 2288-338X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2626 | Rivista Geografica Italiana FrancoAngeli Edizioni / Unknown | 2499-748X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2627 | IRBM / ELSEVIER SCIENCE INC | 1876-0988 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2628 | PLANT BIOTECHNOLOGY REPORTS / SPRINGER | 1863-5466 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2629 | INTERNATIONAL JOURNAL OF PUBLIC  THEOLOGY / BRILL | 1569-7320 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2630 | Research in Learning Technology Association for Le / Unknown | 2156-7077 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2631 | Andes Pediatrica Sociedad Chilena de Pediatria / Unknown | 2452-6053 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2632 | Mental Health and Social Inclusion Emerald Group P / N°   ISSN   E-ISSN | 2042-8308 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2633 | PHYTOPROTECTION / QUEBEC SOC PROTECT PLANTS | 1710-1603 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2634 | ACM TRANSACTIONS ON STORAGE / ASSOC COMPUTING MACHINERY | 1553-3077 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2635 | Contemporary Italian Politics Routledge / Unknown | 2324-8831 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2636 | Acta Medica Lituanica Vilnius University Press / Unknown | 2029-4174 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2637 | Journal of Family Business Management Emerald Grou / Unknown | 2043-6238 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2638 | Revista de Derecho Administrativo Economico Pontif / Unknown | 0719-5591 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2639 | Shagi/ Steps Russian Presidential Academy of Natio / Unknown | 2782-1765 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2640 | Revista Brasileira de Ciencias Policiais National  / Unknown | 2318-6917 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2641 | Adolescents Multidisciplinary Digital Publishing I / Unknown | 2673-7051 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2642 | Journal of the National Cancer Center Chinese Nati / Unknown | 2667-0054 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2643 | Tec Empresarial Business School, Instituto Tecnolo / Unknown | 1659-3359 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2644 | Asian Journal of Legal Education SAGE Publications / Unknown | 2322-0058 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2645 | Advances in Cancer Biology - Metastasis Elsevier I / Unknown | 2667-3940 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2646 | Japanese Political Economy Routledge / Unknown | 2329-1958 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2647 | Operational Research in Engineering Sciences: Theo / Unknown | 2620-1747 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2648 | JOURNAL OF ADHESIVE DENTISTRY / QUINTESSENCE PUBLISHING CO INC | 1757-9988 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2649 | SEN-I GAKKAISHI / SOC FIBER SCIENCE TECHNOLOGY | 1884-2259 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2650 | JOURNAL OF PHYTOPATHOLOGY / WILEY | 0931-1785 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2651 | EUROSURVEILLANCE / EUR CENTRE DIS PREVENTION &  CONTROL | 1560-7917 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2652 | Abstract and Applied Analysis John Wiley and Sons  / Unknown | 1085-3375 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2653 | ACTA ODONTOLOGICA SCANDINAVICA / MEDICAL JOURNAL SWEDEN AB | 1502-3850 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2654 | New Physics: Sae Mulli Korean Physical Society / Unknown | 2289-0041 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2655 | JOURNAL OF DIFFERENTIAL GEOMETRY / INT PRESS BOSTON, INC | 1945-743X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2656 | FAMILY & COMMUNITY HEALTH / LIPPINCOTT WILLIAMS & WILKINS | 0160-6379 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2657 | CLINICAL AUTONOMIC RESEARCH / SPRINGER HEIDELBERG | 0959-9851 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2658 | JOURNAL OF SCHOOL NURSING / SAGE PUBLICATIONS INC | 1059-8405 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2659 | Schweizerische Zeitschrift fur Forstwesen Swiss Fo / Unknown | 2235-1469 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2660 | Sovremennye Problemy Distantsionnogo Zondirovaniya / Unknown | 2411-0280 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2661 | JOURNAL FOR THE THEORY OF SOCIAL  BEHAVIOUR / WILEY | 0021-8308 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2662 | European archives of paediatric dentistry : offici / Unknown | 1818-6300 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2663 | CHILDRENS LITERATURE IN EDUCATION / SPRINGER | 0045-6713 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2664 | Nuclear Physics News Taylor and Francis Ltd. / N°   ISSN   E-ISSN | 1061-9127 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2665 | TransNav Faculty of Navigation, Gdynia Maritime Un / Unknown | 2083-6481 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2666 | CHILDRENS GEOGRAPHIES / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1473-3277 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2667 | Journal of Environmental Studies and Sciences Spri / Unknown | 2190-6483 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2668 | ECONOMIC CHANGE AND  RESTRUCTURING / SPRINGER | 1573-9414 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2669 | Philosophy and Technology Springer Netherlands / Unknown | 2210-5433 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2670 | JOURNAL OF RENAL CARE / WILEY | 1755-6678 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2671 | Cahiers de Psychologie Clinique De Boeck Supérieur / Unknown | 1782-1401 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2672 | INTERNATIONAL JOURNAL OF  SIMULATION MODELLING / DAAAM INTERNATIONAL VIENNA | 1996-8566 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2673 | CONSUMPTION MARKETS & CULTURE / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1025-3866 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2674 | Journal of Curriculum and Teaching Sciedu Press / Unknown | 1927-2685 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2675 | VEHICULAR COMMUNICATIONS / ELSEVIER | 2214-2096 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2676 | Vehicular Communications Elsevier Inc. / Unknown | 2214-210X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2677 | RESEARCH IN DANCE EDUCATION / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1464-7893 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2678 | KNOWLEDGE AND MANAGEMENT OF  AQUATIC ECOSYSTEMS / EDP SCIENCES S A | 1961-9502 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2679 | Oncogematologiya ABV-press Publishing House / Unknown | 2413-4023 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2680 | QUADERNI STORICI / SOC ED IL MULINO | 2612-1972 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2681 | DYNAMIC GAMES AND APPLICATIONS / SPRINGER BIRKHAUSER | 2153-0785 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2682 | International Journal of Services, Economics and M / Unknown | 1753-0822 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2683 | Folia Linguistica et Litteraria University of Mont / Unknown | 2337-0955 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2684 | L1 Educational Studies in Language and Literature  / Unknown | 1573-1731 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2685 | INTERNATIONAL JOURNAL OF  COMPUTER-SUPPORTED  COLL / SPRINGER | 1556-1607 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2686 | Journal of Computational Social Science Springer N / Unknown | 2432-2717 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2687 | Fundamina Juta and Company Ltd / Unknown | 2411-7870 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2688 | International Journal of Sociotechnology and Knowl / Unknown | 1941-6261 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2689 | Advances in Fuzzy Systems John Wiley and Sons Ltd / Unknown | 1687-7101 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2690 | Riset Geologi dan Pertambangan National Research a / Unknown | 2354-6638 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2691 | Journal of Global Operations and Strategic Sourcin / Unknown | 2398-5364 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2692 | JOURNAL OF THE MEXICAN CHEMICAL  SOCIETY / SOC QUIMICA MEXICO | 1870-249X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2693 | Tongji Daxue Xuebao/Journal of Tongji University S / Unknown | 0253-374X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2694 | JOURNAL OF THE ASSOCIATION FOR  INFORMATION SYSTEM / ASSOC INFORMATION SYSTEMS | 1536-9323 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2695 | APPLIED SOFT COMPUTING / ELSEVIER | 1568-4946 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2696 | VETERINARY MICROBIOLOGY / ELSEVIER | 0378-1135 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2697 | EXPERIMENTAL AND CLINICAL  ENDOCRINOLOGY & DIABETE / GEORG THIEME VERLAG KG | 0947-7349 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2698 | JOURNAL OF GEOPHYSICAL RESEARCH- OCEANS / AMER GEOPHYSICAL UNION | 2169-9291 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2699 | THERMAL SCIENCE / VINCA INST NUCLEAR SCI | 2334-7163 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2700 | STEEL RESEARCH INTERNATIONAL / WILEY-V C H VERLAG GMBH | 1611-3683 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2701 | CLUSTER COMPUTING-THE JOURNAL  OF NETWORKS SOFTWAR / SPRINGER | 1386-7857 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2702 | ANNALS OF TELECOMMUNICATIONS / SPRINGER INT PUBL AG | 0003-4347 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2703 | INTERNATIONAL JOURNAL OF  OBSTETRIC ANESTHESIA / ELSEVIER SCI LTD | 0959-289X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2704 | INTERNATIONAL JOURNAL OF  INTELLIGENT SYSTEMS / WILEY | 0884-8173 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2705 | INTERDISCIPLINARY SCIENCE REVIEWS / SAGE PUBLICATIONS INC | 0308-0188 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2706 | JOURNAL OF FIELD ARCHAEOLOGY / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 0093-4690 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2707 | JOURNAL OF MATERIAL CYCLES AND  WASTE MANAGEMENT / SPRINGER | 1438-4957 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2708 | Annales de Cardiologie et d'Angeiologie Elsevier M / Unknown | 0003-3928 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2709 | BOUNDARY 2-AN INTERNATIONAL  JOURNAL OF LITERATURE / DUKE UNIV PRESS | 0190-3659 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2710 | Indian Journal of Agricultural Research Agricultur / Unknown | 0976-058X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2711 | EXPERT REVIEW OF CLINICAL  IMMUNOLOGY / TAYLOR & FRANCIS LTD | 1744-666X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2712 | Manuelle Medizin Springer Verlag / Unknown | 0025-2514 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2713 | JOURNAL DE MATHEMATIQUES PURES  ET APPLIQUEES / ELSEVIER | 0021-7824 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2714 | CYBERNETICS AND SYSTEMS / TAYLOR & FRANCIS INC | 0196-9722 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2715 | Revista Brasileira de Cirurgia Plastica Sociedade  / Unknown | 2177-1235 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2716 | BIOSTATISTICS / OXFORD UNIV PRESS | 1465-4644 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2717 | INDUSTRIAL ARCHAEOLOGY REVIEW / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 0309-0728 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2718 | INTERNATIONAL JOURNAL OF SPEECH- LANGUAGE PATHOLOG / TAYLOR & FRANCIS LTD | 1754-9507 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2719 | Veterinarski Glasnik Veterinarski Fakultet / Unknown | 2406-0771 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2720 | Endoxa Universidad Nacional de Educacion a Distanc / Unknown | 2174-5676 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2721 | Revista U.D.C.A Actualidad and Divulgacion Cientif / Unknown | 2619-2551 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2722 | Monte Carlo Methods and Applications Walter de Gru / Unknown | 0929-9629 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2723 | HISPANIA-REVISTA ESPANOLA DE  HISTORIA / CONSEJO SUPERIOR  INVESTIGACIONES CIENTI | 1988-8368 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2724 | Studies in Gender and Sexuality Taylor and Francis / Unknown | 1524-0657 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2725 | RESEARCH AND PRACTICE FOR  PERSONS WITH SEVERE DIS / SAGE PUBLICATIONS INC | 1540-7969 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2726 | Environmental Science: Atmospheres Royal Society o / Unknown | 2634-3606 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2727 | International Journal of Geosynthetics and Ground  / Unknown | 2199-9260 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2728 | ARCHNET-IJAR INTERNATIONAL  JOURNAL OF ARCHITECTUR / EMERALD GROUP PUBLISHING LTD | 1938-7806 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2729 | GENETIC PROGRAMMING AND  EVOLVABLE MACHINES / SPRINGER | 1389-2576 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2730 | Asia-Pacific Review Routledge / Unknown | 1343-9006 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2731 | Journal of Advances in Management Research Emerald / Unknown | 0972-7981 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2732 | Pedagogy in Health Promotion SAGE Publications Inc / Unknown | 2373-3799 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2733 | Journal of Religious and Theological Information R / Unknown | 1528-6924 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2734 | Journal of Applied Linguistics and Professional Pr / Unknown | 2040-3666 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2735 | Word Structure Edinburgh University Press / Unknown | 1750-1245 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2736 | Visual Informatics Elsevier B.V. / Unknown | 2468-502X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2737 | Nuevo Derecho University Institution of Envigado / Unknown | 2500-672X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2738 | Geoscience Communication Copernicus Publications / Unknown | 2569-7102 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2739 | GEOENERGY SCIENCE AND  ENGINEERING / ELSEVIER | 2949-8929 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2740 | APPLIED MATHEMATICS AND  COMPUTATION / ELSEVIER SCIENCE INC | 0096-3003 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2741 | JOURNAL OF PAIN / CHURCHILL LIVINGSTONE | 1528-8447 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2742 | PLANETARY AND SPACE SCIENCE / PERGAMON-ELSEVIER SCIENCE LTD | 0032-0633 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2743 | JOURNAL OF SEDIMENTARY RESEARCH / SEPM-SOC SEDIMENTARY GEOLOGY | 1938-3681 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2744 | JOURNAL OF PSYCHOLOGY / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 0022-3980 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2745 | ARQUIVO BRASILEIRO DE MEDICINA  VETERINARIA E ZOOT / ARQUIVO BRASILEIRO MEDICINA  VETERINARIA | 1678-4162 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2746 | ANNALES MEDICO-PSYCHOLOGIQUES / MASSON EDITEUR | 1769-6631 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2747 | PHARMACOLOGY & THERAPEUTICS / PERGAMON-ELSEVIER SCIENCE LTD | 0163-7258 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2748 | JOURNAL OF MIDWIFERY & WOMENS  HEALTH / WILEY | 1526-9523 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2749 | JOURNAL OF INTERNATIONAL  ECONOMICS / ELSEVIER | 0022-1996 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2750 | QUARTERLY OF APPLIED  MATHEMATICS / BROWN UNIV | 1552-4485 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2751 | FLOW MEASUREMENT AND  INSTRUMENTATION / ELSEVIER SCI LTD | 0955-5986 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2752 | SOCIAL SCIENCE RESEARCH / ACADEMIC PRESS INC ELSEVIER  SCIENCE | 0049-089X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2753 | MOBILE NETWORKS & APPLICATIONS / SPRINGER | 1383-469X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2754 | CURRENT PSYCHIATRY REPORTS / SPRINGER | 1523-3812 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2755 | AIR QUALITY ATMOSPHERE AND  HEALTH / SPRINGER | 1873-9318 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2756 | JOURNAL OF ENERGY ENGINEERING / ASCE-AMER SOC CIVIL ENGINEERS | 0733-9402 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2757 | JOURNAL OF AUTOMATED REASONING / SPRINGER | 0168-7433 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2758 | Energy and Environmental Materials John Wiley & So / Unknown | 2575-0348 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2759 | ENERGY & ENVIRONMENTAL  MATERIALS / WILEY | 2575-0356 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2760 | JOURNAL OF HIGHER EDUCATION  POLICY AND MANAGEMENT / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1360-080X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2761 | IDEALISTIC STUDIES / PHILOSOPHY DOCUMENTATION  CENTER | 2153-8239 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2762 | JOURNAL OF APPLIED ANIMAL  WELFARE SCIENCE / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1088-8705 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2763 | WORLD JOURNAL OF EMERGENCY  SURGERY / BMC | 1749-7922 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2764 | European Education Routledge / Unknown | 1944-7086 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2765 | International Review of Law, Computers and Technol / Unknown | 1364-6885 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2766 | REVISTA MEXICANA DE INGENIERIA  QUIMICA / UNIV AUTONOMA  METROPOLITANA-IZTAPALAPA | 2395-8472 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2767 | Russian Journal of Earth Sciences Geophysical Cent / Unknown | 1681-1208 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2768 | PERIODICUM BIOLOGORUM / PERIODICUM BIOLOGORUM | 1849-0964 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2769 | Jeunesse: Young People, Texts, Cultures University / Unknown | 1920-2601 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2770 | SOCIOLOGY OF RACE AND ETHNICITY / SAGE PUBLICATIONS INC | 2332-6492 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2771 | PSYCHIATRY AND CLINICAL  PSYCHOPHARMACOLOGY / AVES | 2475-0581 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2772 | ACM TRANSACTIONS ON COMPUTING  EDUCATION / ASSOC COMPUTING MACHINERY | 1946-6226 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2773 | Court Historian Taylor and Francis Ltd. / Unknown | 1462-9712 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2774 | JOURNAL OF SEED SCIENCE / ABRATES-ASSOC BRASILEIRA  TECHNOLOGIA SE | 2317-1545 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2775 | JOURNAL OF INTEGRATIVE AND  COMPLEMENTARY MEDICINE / MARY ANN LIEBERT, INC | 2768-3605 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2776 | Sign Language and Linguistics (Online) John Benjam / Unknown | 1387-9316 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2777 | Journal of Intelligent Systems and Internet of Thi / Unknown | 2690-6791 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2778 | Biblos Universidade de Coimbra - Faculdade de Letr / Unknown | 2183-7139 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2779 | Journal of Vibration Testing and System Dynamics L / Unknown | 2475-482X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2780 | ARS (Bratislava) Art Research Centre of Slovak Aca / Unknown | 2729-7349 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2781 | JSAMS Plus Elsevier B.V. / N°   ISSN   E-ISSN | 2772-6967 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2782 | Journal of Analysis Springer Science and Business  / Unknown | 0971-3611 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2783 | APPLIED SURFACE SCIENCE / ELSEVIER | 0169-4332 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2784 | JOURNAL OF BACTERIOLOGY / AMER SOC MICROBIOLOGY | 0021-9193 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2785 | INTERNATIONAL JOURNAL / SAGE PUBLICATIONS LTD | 0020-7020 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2786 | JOURNAL OF ENVIRONMENTAL  RADIOACTIVITY / ELSEVIER SCI LTD | 0265-931X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2787 | NEUROPHYSIOLOGIE CLINIQUE- CLINICAL NEUROPHYSIOLOG / ELSEVIER FRANCE-EDITIONS  SCIENTIFIQUES  | 0987-7053 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2788 | Gerontechnology International Society for Gerontec / N°   ISSN   E-ISSN | 1569-111X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2789 | EUROPEAN JOURNAL OF AGRONOMY / ELSEVIER | 1161-0301 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2790 | RAE-REVISTA DE ADMINISTRACAO DE  EMPRESAS / FUNDACAO GETULIO VARGAS | 2178-938X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2791 | BRAZILIAN JOURNAL OF  CARDIOVASCULAR SURGERY / SOC BRASIL CIRURGIA CARDIOVASC | 1678-9741 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2792 | JOURNAL OF THE AMERICAN ACADEMY  OF AUDIOLOGY / THIEME MEDICAL PUBL INC | 1050-0545 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2793 | Revista Peruana de Ginecologia y Obstetricia Peruv / Unknown | 2304-5132 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2794 | JOURNAL OF VIBRATION ENGINEERING  & TECHNOLOGIES / SPRINGER HEIDELBERG | 2523-3920 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2795 | INQUIRY-THE JOURNAL OF HEALTH  CARE ORGANIZATION P / SAGE PUBLICATIONS INC | 0046-9580 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2796 | GUT AND LIVER / EDITORIAL OFFICE GUT & LIVER | 2005-1212 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2797 | MABS / TAYLOR & FRANCIS INC | 1942-0862 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2798 | Journal of Applied Laboratory Medicine Oxford Univ / Unknown | 2475-7241 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2799 | Ciencia Animal Brasileira Universidade Federal De  / Unknown | 1809-6891 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2800 | TQM Journal Emerald Group Publishing Ltd. / Unknown | 1754-2731 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2801 | Labour John Wiley and Sons Inc / Unknown | 1121-7081 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2802 | Seminars in Spine Surgery W.B. Saunders / Unknown | 1558-4496 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2803 | Revista Espanola de Orientacion y Psicopedagogia U / Unknown | 1989-7448 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2804 | INFORMATION TECHNOLOGY FOR  DEVELOPMENT / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 0268-1102 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2805 | Anais do Museu Paulista Universidade De Sao Paulo / Unknown | 1982-0267 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2806 | Oncology Reviews Frontiers Media SA / Unknown | 1970-5557 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2807 | Kuban Scientific Medical Bulletin Kuban State Medi / Unknown | 2541-9544 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2808 | Vniversitas Pontificia Universidad Javeriana / N°   ISSN   E-ISSN | 2011-1711 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2809 | Interfacial Phenomena and Heat Transfer Begell Hou / Unknown | 2167-857X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2810 | City and Environment Interactions Elsevier B.V. / Unknown | 2590-2520 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2811 | Journal of Applied Veterinary Sciences Egyptian So / Unknown | 2090-3308 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2812 | Russian Journal of Stomatology Media Sphera Publis / Unknown | 2309-5156 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2813 | ASIAN HERPETOLOGICAL RESEARCH / SCIENCE PRESS | 2095-0357 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2814 | Water Conservation and Management Zibeline Interna / Unknown | 2523-5672 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2815 | MICROBIAL RISK ANALYSIS / ELSEVIER | 2352-3522 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2816 | WSEAS Transactions on Fluid Mechanics World Scient / Unknown | 1790-5087 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2817 | Strides in Development of Medical Education Journa / Unknown | 2645-3525 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2818 | Teknomekanik Universitas Negeri Padang / Unknown | 2621-9980 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2819 | Dia-noesis University of Western Macedonia / Unknown | 2732-7507 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2820 | AMERICAN NATURALIST / UNIV CHICAGO PRESS | 0003-0147 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2821 | HUMAN MOLECULAR GENETICS / OXFORD UNIV PRESS | 0964-6906 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2822 | BIOMEDICAL ENGINEERING- BIOMEDIZINISCHE TECHNIK / WALTER DE GRUYTER GMBH | 0013-5585 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2823 | EUROPEAN JOURNAL OF CLINICAL  PHARMACOLOGY / SPRINGER HEIDELBERG | 0031-6970 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2824 | ISIJ INTERNATIONAL / IRON STEEL INST JAPAN KEIDANREN  KAIKAN | 1347-5460 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2825 | CANADIAN JOURNAL OF PLANT  SCIENCE / CANADIAN SCIENCE PUBLISHING | 0008-4220 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2826 | PLOS BIOLOGY / PUBLIC LIBRARY SCIENCE | 1545-7885 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2827 | JOURNAL OF THE CHINESE CHEMICAL  SOCIETY / WILEY-V C H VERLAG GMBH | 0009-4536 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2828 | JOURNAL OF SOL-GEL SCIENCE AND  TECHNOLOGY / SPRINGER | 0928-0707 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2829 | IEEE TRANSACTIONS ON FUZZY  SYSTEMS / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 1063-6706 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2830 | BRITISH JOURNAL FOR THE HISTORY OF  SCIENCE / CAMBRIDGE UNIV PRESS | 0007-0874 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2831 | INTERNATIONAL JOURNAL OF CIRCUIT  THEORY AND APPLI / WILEY | 0098-9886 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2832 | EUROPEAN JOURNAL OF  COMBINATORICS / ACADEMIC PRESS LTD- ELSEVIER  SCIENCE LT | 0195-6698 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2833 | BEHAVIORAL ECOLOGY / OXFORD UNIV PRESS INC | 1045-2249 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2834 | JOURNAL OF PHARMACOLOGICAL  SCIENCES / JAPANESE PHARMACOLOGICAL SOC | 1347-8648 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2835 | Homme et la Societe Editions Anthropos / Unknown | 2101-0226 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2836 | Results in Chemistry Elsevier B.V. / Unknown | 2211-7156 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2837 | CLAY MINERALS / CAMBRIDGE UNIV PRESS | 0009-8558 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2838 | ROMANTISME / EDITIONS SEDES | 1957-7958 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2839 | MOLECULAR ONCOLOGY / WILEY | 1574-7891 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2840 | TRANSPORTATION / SPRINGER | 0049-4488 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2841 | ACM TRANSACTIONS ON MULTIMEDIA  COMPUTING COMMUNIC / ASSOC COMPUTING MACHINERY | 1551-6857 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2842 | IET ELECTRIC POWER APPLICATIONS / WILEY | 1751-8660 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2843 | JOURNAL OF BRYOLOGY / TAYLOR & FRANCIS LTD | 0373-6687 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2844 | PSYCHOLOGICAL METHODS / AMER PSYCHOLOGICAL ASSOC | 1082-989X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2845 | BILINGUALISM-LANGUAGE AND  COGNITION / CAMBRIDGE UNIV PRESS | 1366-7289 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2846 | GEO-SPATIAL INFORMATION SCIENCE / TAYLOR & FRANCIS LTD | 1009-5020 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2847 | VEGETATION HISTORY AND  ARCHAEOBOTANY / SPRINGER | 0939-6314 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2848 | Journal of Plant Biotechnology / Unknown | 2384-1397 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2849 | GLOBAL FINANCE JOURNAL / ELSEVIER | 1044-0283 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2850 | JOURNAL OF INVASIVE CARDIOLOGY / H M P COMMUNICATIONS | 1557-2501 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2851 | WILEY INTERDISCIPLINARY REVIEWS- COGNITIVE SCIENCE / WILEY | 1939-5078 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2852 | Gerion Universidad Complutense Madrid / Unknown | 1988-3080 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2853 | Revista de Economia Contemporanea Universidade Fed / Unknown | 1980-5527 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2854 | Security and Human Rights The Security and Human R / Unknown | 1875-0230 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2855 | ARCTIC SCIENCE / CANADIAN SCIENCE PUBLISHING | 2368-7460 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2856 | Revista Brasileira de Direito Processual Penal Ins / Unknown | 2525-510X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2857 | Journal of Humanitarian Logistics and Supply Chain / Unknown | 2042-6747 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2858 | Frontiers in Epidemiology Frontiers Media SA / Unknown | 2674-1199 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2859 | Oil Crop Science KeAi Communications Co. / Unknown | 2666-626X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2860 | Tabano Pontificia Universidad Catolica Argentina / Unknown | 2591-572X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2861 | Litteraria Pragensia Charles University, Faculty o / Unknown | 2571-452X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2862 | NEW SCIENTIST / NEW SCIENTIST LTD | 2059-5387 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2863 | COMPUTATIONAL MATERIALS SCIENCE / ELSEVIER | 0927-0256 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2864 | Medicine (Spain) Ediciones Doyma, S.L. / Unknown | 1578-8822 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2865 | JOURNAL OF PERSONALITY / WILEY | 0022-3506 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2866 | ANNALS OF GEOPHYSICS / IST NAZIONALE DI GEOFISICA E  VULCANOLOG | 2037-416X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2867 | EUROPEAN STROKE JOURNAL / SAGE PUBLICATIONS LTD | 2396-9873 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2868 | PHYSIOLOGICAL ENTOMOLOGY / WILEY | 0307-6962 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2869 | Revista Chilena de Derecho Privado Universidad Die / Unknown | 0718-8072 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2870 | HORTICULTURE RESEARCH / OXFORD UNIV PRESS INC | 2052-7276 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2871 | INTERNATIONAL BUSINESS REVIEW / ELSEVIER | 0969-5931 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2872 | SUGAR TECH / SPRINGER INDIA | 0972-1525 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2873 | Boletin Medico del Hospital Infantil de Mexico Hos / Unknown | 1665-1146 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2874 | JOURNAL OF CLINICAL PEDIATRIC  DENTISTRY / MRE PRESS | 1557-5268 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2875 | British Journal of Visual Impairment SAGE Publicat / Unknown | 0264-6196 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2876 | INTERNATIONAL JOURNAL OF  PSYCHIATRY IN CLINICAL P / TAYLOR & FRANCIS LTD | 1365-1501 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2877 | Applicationes Mathematicae Institute of Mathematic / N°   ISSN   E-ISSN | 1730-6280 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2878 | Scientia Pharmaceutica Multidisciplinary Digital P / Unknown | 0036-8709 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2879 | Structural Heart Cardiovascular Research Foundatio / Unknown | 2474-8714 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2880 | History in Africa African Studies Association / Unknown | 1558-2744 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2881 | MEDICAL LAW REVIEW / OXFORD UNIV PRESS | 0967-0742 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2882 | Western Journal of Communication Taylor and Franci / Unknown | 1057-0314 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2883 | International Journal of Grid and Utility Computin / Unknown | 1741-847X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2884 | PETROLEUM GEOSCIENCE / GEOLOGICAL SOC PUBL HOUSE | 2041-496X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2885 | INTERNATIONAL JOURNAL ON  SOFTWARE TOOLS FOR TECHN / SPRINGER HEIDELBERG | 1433-2779 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2886 | AlterNative SAGE Publications Inc. / Unknown | 1174-1740 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2887 | Law, Culture and the Humanities SAGE Publications  / Unknown | 1743-8721 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2888 | Moscow University Mathematics Bulletin Pleiades Pu / Unknown | 0027-1322 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2889 | Journal of Rheumatic Diseases Korean College of Rh / Unknown | 2233-4718 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2890 | MULTINATIONAL BUSINESS REVIEW / EMERALD GROUP PUBLISHING LTD | 1525-383X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2891 | JOURNAL OF HOSPITALITY AND  TOURISM TECHNOLOGY / EMERALD GROUP PUBLISHING LTD | 1757-9880 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2892 | CANADIAN JOURNAL OF FILM STUDIES- REVUE CANADIENNE / UNIV TORONTO PRESS INC | 0847-5911 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2893 | SURFACE INNOVATIONS / EMERALD GROUP PUBLISHING LTD | 2050-6252 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2894 | Stanovnistvo Demographic Research Centre / Unknown | 2217-3986 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2895 | Hydrogen (Switzerland) Multidisciplinary Digital P / Unknown | 2673-4141 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2896 | Al-Istinbath: Jurnal Hukum Islam State Institute f / Unknown | 2548-3382 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2897 | JOURNAL OF CHINESE LITERATURE AND  CULTURE / DUKE UNIV PRESS | 2329-0048 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2898 | Consortium Psychiatricum Eco-Vector LLC / Unknown | 2713-2919 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2899 | Power Electronic Devices and Components Elsevier B / Unknown | 2772-3704 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2900 | Frontiers in Photonics Frontiers Media SA / Unknown | 2673-6853 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2901 | Principia Komitet Slowianoznawstwa PAN / Unknown | 2084-3887 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2902 | AMERICAN JOURNAL OF THE MEDICAL  SCIENCES / ELSEVIER SCIENCE INC | 0002-9629 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2903 | NUCLEAR ENGINEERING AND DESIGN / ELSEVIER SCIENCE SA | 0029-5493 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2904 | PEDIATRIC PULMONOLOGY / WILEY | 1099-0496 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2905 | GEODERMA / ELSEVIER | 0016-7061 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2906 | RISK ANALYSIS / WILEY | 0272-4332 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2907 | CHEMISTRY AND PHYSICS OF LIPIDS / ELSEVIER IRELAND LTD | 0009-3084 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2908 | INTERNATIONAL JOURNAL OF  COLORECTAL DISEASE / SPRINGER | 0179-1958 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2909 | ADDITIVE MANUFACTURING / ELSEVIER | 2214-7810 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2910 | CLINICAL DRUG INVESTIGATION / ADIS INT LTD | 1173-2563 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2911 | International Journal of Biological and Chemical S / Unknown | 1997-342X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2912 | WORLD POLITICS / JOHNS HOPKINS UNIV PRESS | 1086-3338 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2913 | MIS QUARTERLY / SOC INFORM MANAGE-MIS RES  CENT | 2162-9730 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2914 | ONCOLOGY NURSING FORUM / ONCOLOGY NURSING SOC | 1538-0688 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2915 | International Journal of Modelling, Identification / Unknown | 1746-6172 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2916 | CHILD ABUSE REVIEW / WILEY | 0952-9136 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2917 | JACEP Open Elsevier Inc. / Unknown | 2688-1152 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2918 | MEXICAN STUDIES-ESTUDIOS  MEXICANOS / UNIV CALIFORNIA PRESS | 0742-9797 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2919 | JOURNAL OF FIELD ORNITHOLOGY / RESILIENCE ALLIANCE | 1557-9263 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2920 | TOPICS IN EARLY CHILDHOOD SPECIAL  EDUCATION / SAGE PUBLICATIONS INC | 0271-1214 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2921 | Mortality Routledge / Unknown | 1469-9885 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2922 | Investigaciones Geograficas Interuniversity Instit / Unknown | 1989-9890 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2923 | SEMINARS IN IMMUNOPATHOLOGY / SPRINGER HEIDELBERG | 1863-2297 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2924 | CELLULAR AND MOLECULAR  BIOENGINEERING / SPRINGER | 1865-5025 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2925 | INVERTEBRATE SYSTEMATICS / CSIRO PUBLISHING | 1445-5226 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2926 | IEEE Journal of Microwaves Institute of Electrical / Unknown | 2692-8388 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2927 | Clean Technologies Multidisciplinary Digital Publi / Unknown | 2571-8797 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2928 | RA-REVISTA DE ARQUITECTURA / UNIV NAVARRA, SERVICIO  PUBLICACIONES | 2254-6332 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2929 | SUBTERRANEAN BIOLOGY / INT SOC SUBTERRANEAN BIOL | 1768-1448 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2930 | Researches in Earth Sciences Shahid Beheshti Unive / Unknown | 2588-5898 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2931 | AMERICAN JOURNAL OF HEALTH  ECONOMICS / UNIV CHICAGO PRESS | 2332-3493 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2932 | Surgery Eastern Europe Professionalnye Izdaniya / Unknown | 2414-1992 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2933 | Droplet John Wiley and Sons Inc / Unknown | 2731-4375 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2934 | COCHRANE DATABASE OF SYSTEMATIC  REVIEWS / WILEY | 1361-6137 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2935 | International Journal of Persian Literature Penn S / Unknown | 2376-5739 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2936 | Journal of Asian Sociology Institute of Social Dev / Unknown | 2671-8200 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2937 | Iranian Endodontic Journal Iranian Centre for Endo / Unknown | 2008-2746 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2938 | LISTY FILOLOGICKE / INST CLASSICAL STUD ACAD SCI  CZECH REPU | 2570-9410 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2939 | International Journal of Supply and Operations Man / N°   ISSN   E-ISSN | 2383-2525 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2940 | Journal of the Siam Society Siam Society under Roy / Unknown | 0304-226X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2941 | INTERNATIONAL JOURNAL OF  BIOLOGICAL MACROMOLECULE / ELSEVIER | 0141-8130 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2942 | RENAISSANCE QUARTERLY / CAMBRIDGE UNIV PRESS | 0034-4338 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2943 | IEEE ANTENNAS AND WIRELESS  PROPAGATION LETTERS / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 1536-1225 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2944 | BULLETIN OF THE ATOMIC SCIENTISTS / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 0096-3402 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2945 | JOURNAL OF BIOSCIENCE AND  BIOENGINEERING / SOC BIOSCIENCE BIOENGINEERING  JAPAN | 1389-1723 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2946 | JOURNAL OF INTEGRATIVE PLANT  BIOLOGY / WILEY | 1672-9072 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2947 | DIGITAL SIGNAL PROCESSING / ACADEMIC PRESS INC ELSEVIER  SCIENCE | 1051-2004 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2948 | COMPARATIVE BIOCHEMISTRY AND  PHYSIOLOGY B-BIOCHEM / ELSEVIER SCIENCE INC | 1096-4959 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2949 | STRATEGIC MANAGEMENT JOURNAL / WILEY | 0143-2095 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2950 | INDIAN JOURNAL OF PSYCHIATRY / WOLTERS KLUWER MEDKNOW  PUBLICATIONS | 0019-5545 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2951 | ECOTOXICOLOGY / SPRINGER | 0963-9292 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2952 | ACM COMPUTING SURVEYS / ASSOC COMPUTING MACHINERY | 0360-0300 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2953 | AUTISM / SAGE PUBLICATIONS LTD | 1362-3613 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2954 | JOURNAL OF ECONOMIC EDUCATION / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 0022-0485 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2955 | PHILOSOPHY TODAY / PHILOSOPHY TODAY DEPAUL UNIV | 2329-8596 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2956 | ACTA PHARMACEUTICA SINICA B / INST MATERIA MEDICA, CHINESE  ACAD MEDIC | 2211-3843 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2957 | INDIAN JOURNAL OF PURE & APPLIED  PHYSICS / NATL INST SCIENCE  COMMUNICATION-NISCAIR | 0975-1041 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2958 | TRANSACTIONS IN GIS / WILEY | 1361-1682 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2959 | CLINICAL SPINE SURGERY / LIPPINCOTT WILLIAMS & WILKINS | 2380-0186 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2960 | Clinical Spine Surgery Lippincott Williams and Wil / Unknown | 2380-0194 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2961 | Australian Journal of Agricultural and Resource Ec / Unknown | 1364-985X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2962 | AUSTRALIAN JOURNAL OF  AGRICULTURAL AND RESOURCE   / WILEY | 1467-8489 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2963 | Medical Archives Academy of Medical Sciences in Bo / Unknown | 1986-5961 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2964 | Journal of Telecommunications and Information Tech / Unknown | 1899-8852 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2965 | Journal of Vocational Education and Training Routl / Unknown | 1747-5090 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2966 | ANNALS OF FUNCTIONAL ANALYSIS / SPRINGER BASEL AG | 2008-8752 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2967 | ACTA OECONOMICA / AKADEMIAI KIADO ZRT | 0001-6373 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2968 | JOURNAL OF VISUAL CULTURE / SAGE PUBLICATIONS INC | 1470-4129 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2969 | Indonesian Journal of Obstetrics and Gynecology In / Unknown | 2338-7335 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2970 | FOREIGN POLICY ANALYSIS / OXFORD UNIV PRESS | 1743-8586 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2971 | Ain Shams Dental Journal (Egypt) Ain Shams Univers / Unknown | 2735-5039 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2972 | Global Intellectual History Taylor and Francis Ltd / Unknown | 2380-1883 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2973 | PLANT ECOLOGY AND EVOLUTION / SOC ROYAL BOTAN BELGIQUE | 2032-3921 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2974 | INTERFACES AND FREE BOUNDARIES / EUROPEAN MATHEMATICAL SOC- EMS | 1463-9963 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2975 | Communication Law and Policy Routledge / Unknown | 1532-6926 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2976 | Advances in Mental Health Taylor and Francis Ltd. / N°   ISSN   E-ISSN | 1837-4905 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2977 | FILOSOFICKY CASOPIS / FILOSOFICKY CASOPIS INST  PHILOSOPHY | 2570-9232 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2978 | Viral Hepatitis Journal Galenos Publishing House / Unknown | 2147-2939 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2979 | European Journal of Management and Business Econom / Unknown | 2444-8451 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2980 | Green Energy and Intelligent Transportation Elsevi / N°   ISSN   E-ISSN | 2773-1537 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2981 | Ukrainian Journal of Radiology and Oncology Grigor / Unknown | 2708-7174 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2982 | Science of Traditional Chinese Medicine Wolters Kl / Unknown | 2836-922X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2983 | NUCLEAR INSTRUMENTS & METHODS  IN PHYSICS RESEARCH / ELSEVIER | 0168-583X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2984 | IEEE TRANSACTIONS ON ELECTRON  DEVICES / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 0018-9383 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2985 | ANALYTICAL BIOCHEMISTRY / ACADEMIC PRESS INC ELSEVIER  SCIENCE | 0003-2697 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2986 | ECOLOGY AND EVOLUTION / WILEY | 2045-7758 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2987 | COMMUNICATIONS IN ALGEBRA / TAYLOR & FRANCIS INC | 0092-7872 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2988 | CHEMBIOCHEM / WILEY-V C H VERLAG GMBH | 1439-4227 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2989 | Indian Journal of Otolaryngology and Head and Neck / Unknown | 0973-7707 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2990 | PROTEINS-STRUCTURE FUNCTION AND  BIOINFORMATICS / WILEY | 0887-3585 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2991 | INTERNATIONAL JOURNAL FOR  NUMERICAL METHODS IN FL / WILEY | 0271-2091 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2992 | JOURNAL OF BIOMEDICAL OPTICS / SPIE-SOC PHOTO-OPTICAL  INSTRUMENTATION  | 1560-2281 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2993 | HISPANIC REVIEW / UNIV PENNSYLVANIA PRESS | 0018-2176 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2994 | DRUG SAFETY / ADIS INT LTD | 0114-5916 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2995 | Strategic Direction Emerald Group Publishing Ltd. / Unknown | 0258-0543 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2996 | INTERNATIONAL JOURNAL OF  SURGICAL PATHOLOGY / SAGE PUBLICATIONS INC | 1066-8969 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2997 | ACTA MATHEMATICAE APPLICATAE  SINICA-ENGLISH SERIE / SPRINGER HEIDELBERG | 0168-9673 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2998 | COMMUNICATIONS EARTH &  ENVIRONMENT / SPRINGERNATURE | 2662-4435 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 2999 | PROGRESS IN ELECTROMAGNETICS  RESEARCH-PIER / EMW PUBLISHING | 1559-8985 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3000 | LIGHT-SCIENCE & APPLICATIONS / SPRINGERNATURE | 2047-7538 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3001 | ENVIRONMENTAL VALUES / SAGE PUBLICATIONS INC | 0963-2719 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3002 | Brazilian Journal of Veterinary Research and Anima / Unknown | 1678-4456 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3003 | HEALTH PROMOTION JOURNAL OF  AUSTRALIA / WILEY | 1036-1073 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3004 | NUKLEONIKA / SCIENDO | 0029-5922 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3005 | NEW DIRECTIONS FOR CHILD AND  ADOLESCENT DEVELOPME / WILEY | 1520-3247 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3006 | JAPAN JOURNAL OF NURSING SCIENCE / WILEY | 1742-7924 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3007 | Asia Marketing Journal Korean Marketing Associatio / Unknown | 2765-6500 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3008 | East European Journal of Physics V N Karazin Khark / Unknown | 2312-4539 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3009 | NEMATROPICA / ORGANIZATION TROP AMER  NEMATOLOGISTS | 2220-5608 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3010 | Nematropica / Unknown | 2220-5616 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3011 | OXFORD LITERARY REVIEW / EDINBURGH UNIV PRESS | 0305-1498 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3012 | Games Multidisciplinary Digital Publishing Institu / Unknown | 2073-4336 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3013 | JOURNAL OF MINING AND  METALLURGY SECTION B-METALL / TECHNICAL FACULTY, BOR-SERBIA | 2217-7175 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3014 | Journal of the Operations Research Society of Chin / Unknown | 2194-668X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3015 | PHILOSOPHICAL PERSPECTIVES / WILEY | 1520-8583 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3016 | Visible Language University of Cincinnati / Unknown | 2691-5529 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3017 | WMU Journal of Maritime Affairs Springer Science a / Unknown | 1651-436X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3018 | INTERNATIONAL JOURNAL FOR  UNCERTAINTY QUANTIFICAT / BEGELL HOUSE INC | 2152-5080 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3019 | Journal of War and Culture Studies Maney Publishin / Unknown | 1752-6280 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3020 | Cuadernos de Investigacion Historica Fundacion Uni / Unknown | 2660-5880 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3021 | Slovensky Narodopis Slovak Academy of Sciences / Unknown | 1339-9357 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3022 | Acta Historica Universitatis Klaipedensis Institut / Unknown | 1392-4095 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3023 | Translation and Translanguaging in Multilingual Co / Unknown | 2352-1805 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3024 | Red Cedar Review Michigan State University Press / Unknown | 1554-6721 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3025 | LGBTQ FAMILY-AN INTERDISCIPLINARY  JOURNAL / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 2770-3371 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3026 | Journal of Monolingual and Bilingual Speech Equino / Unknown | 2631-8415 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3027 | Geologica Macedonica Goce Delchev University of Sh / N°   ISSN   E-ISSN | 1857-8586 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3028 | E-Learning and Digital Media SAGE Publications Inc / Unknown | 1741-8887 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3029 | IEEE TRANSACTIONS ON MICROWAVE  THEORY AND TECHNIQ / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 0018-9480 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3030 | HEART LUNG AND CIRCULATION / ELSEVIER SCIENCE INC | 1443-9506 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3031 | JOURNAL OF VACUUM SCIENCE &  TECHNOLOGY A / A V S AMER INST PHYSICS | 1520-8559 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3032 | IEEE TRANSACTIONS ON SIGNAL  PROCESSING / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 1053-587X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3033 | HISTOPATHOLOGY / WILEY | 0309-0167 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3034 | JOURNAL OF THE AMERICAN COLLEGE  OF RADIOLOGY / ELSEVIER SCIENCE INC | 1546-1440 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3035 | BIOTECHNOLOGY PROGRESS / WILEY | 1520-6033 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3036 | REVISTA BRASILEIRA DE ZOOTECNIA- BRAZILIAN JOURNAL / REVISTA BRASILEIRA ZOOTECNIA  BRAZILIAN  | 1806-9290 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3037 | AMERICAN JOURNAL OF ECONOMICS  AND SOCIOLOGY / WILEY | 0002-9246 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3038 | KNEE / ELSEVIER | 0968-0160 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3039 | OPERATIONS RESEARCH LETTERS / ELSEVIER | 0167-6377 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3040 | AGING & MENTAL HEALTH / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1360-7863 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3041 | CURRENT OPINION IN  OPHTHALMOLOGY / LIPPINCOTT WILLIAMS & WILKINS | 1040-8738 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3042 | JOURNAL OF THE JAPANESE SOCIETY  FOR FOOD SCIENCE  / JAPAN SOC FOOD SCIENCE  TECHNOLOGY | 1881-6681 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3043 | JOURNAL OF GENETIC COUNSELING / WILEY | 1059-7700 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3044 | EXPERIMENTAL AND CLINICAL  PSYCHOPHARMACOLOGY / AMER PSYCHOLOGICAL ASSOC | 1064-1297 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3045 | JOURNAL OF FAMILY VIOLENCE / SPRINGER/PLENUM PUBLISHERS | 0885-7482 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3046 | JOURNAL OF INDUSTRIAL ECONOMICS / WILEY | 0022-1821 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3047 | Home Health Care Management and Practice SAGE Publ / Unknown | 1084-8223 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3048 | FOOD REVIEWS INTERNATIONAL / TAYLOR & FRANCIS INC | 1525-6103 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3049 | JOURNAL OF URBAN PLANNING AND  DEVELOPMENT / ASCE-AMER SOC CIVIL ENGINEERS | 0733-9488 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3050 | JOURNAL OF HEALTH SERVICES  RESEARCH & POLICY / SAGE PUBLICATIONS INC | 1355-8196 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3051 | Periodica Polytechnica Mechanical Engineering Buda / Unknown | 1587-379X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3052 | Acta Mycologica Polish Botanical Society / Unknown | 2353-074X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3053 | GEDRAG & ORGANISATIE / UITGEVERIJ LEMMA B V | 1875-7235 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3054 | CRITICAL CRIMINOLOGY / SPRINGER | 1205-8629 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3055 | Physician Assistant Clinics Elsevier Inc. / Unknown | 2405-7991 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3056 | Egyptian Journal of Petroleum Egyptian Petroleum R / Unknown | 2090-2468 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3057 | Global Bioethics Routledge / Unknown | 1591-7398 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3058 | American Journal of Animal and Veterinary Sciences / Unknown | 1557-4563 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3059 | CRITICAL REVIEWS IN THERAPEUTIC  DRUG CARRIER SYST / BEGELL HOUSE INC | 0743-4863 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3060 | JOURNAL OF PHOTOCHEMISTRY AND  PHOTOBIOLOGY C-PHOT / ELSEVIER | 1389-5567 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3061 | IET BIOMETRICS / WILEY | 2047-4938 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3062 | JOURNAL OF SERVICE THEORY AND  PRACTICE / EMERALD GROUP PUBLISHING LTD | 2055-6225 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3063 | Strategy Science INFORMS Institute for Operations  / Unknown | 2333-2050 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3064 | Mediterranean Geoscience Reviews Springer Nature / Unknown | 2661-863X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3065 | European Journal of Environmental Sciences Charles / Unknown | 1805-0174 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3066 | Disena Pontificia Universidad Catolica de Chile / Unknown | 2452-4298 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3067 | Activitas Nervosa Superior Rediviva Slovak Academy / Unknown | 1338-4015 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3068 | Reading Medieval Sources Brill / Unknown | 2589-2509 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3069 | ANNALS OF THE RHEUMATIC DISEASES / ELSEVIER | 0003-4967 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3070 | CLINICAL INFECTIOUS DISEASES / OXFORD UNIV PRESS INC | 1058-4838 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3071 | CHEMICAL ENGINEERING SCIENCE / PERGAMON-ELSEVIER SCIENCE LTD | 0009-2509 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3072 | COMMUNICATIONS IN  MATHEMATICAL PHYSICS / SPRINGER | 0010-3616 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3073 | JOURNAL OF SHOULDER AND ELBOW  SURGERY / MOSBY-ELSEVIER | 1058-2746 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3074 | BAUTECHNIK / ERNST & SOHN | 1437-0999 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3075 | AMERICAN STATISTICIAN / TAYLOR & FRANCIS INC | 0003-1305 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3076 | CANCER RADIOTHERAPIE / ELSEVIER | 1278-3218 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3077 | EDUCATION AND TRAINING / EMERALD GROUP PUBLISHING LTD | 0040-0912 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3078 | BIOTROPICA / WILEY | 0006-3606 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3079 | INTERNATIONAL SOCIAL WORK / SAGE PUBLICATIONS LTD | 0020-8728 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3080 | QUARTERLY JOURNAL OF  EXPERIMENTAL PSYCHOLOGY / SAGE PUBLICATIONS LTD | 1747-0218 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3081 | CALIFORNIA HISTORY / CALIFORNIA HISTORICAL SOC | 2327-1485 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3082 | ITALIAN JOURNAL OF PEDIATRICS / BMC | 1720-8424 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3083 | JOURNAL OF DRUG ISSUES / SAGE PUBLICATIONS INC | 0022-0426 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3084 | HUMAN RIGHTS QUARTERLY / JOHNS HOPKINS UNIV PRESS | 1085-794X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3085 | JOURNAL OF AGING AND PHYSICAL  ACTIVITY / HUMAN KINETICS PUBL INC | 1063-8652 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3086 | CULTURAL CRITIQUE / UNIV MINNESOTA PRESS | 1460-2458 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3087 | HONG KONG JOURNAL OF EMERGENCY  MEDICINE / WILEY | 1024-9079 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3088 | PRAXIS DER KINDERPSYCHOLOGIE UND  KINDERPSYCHIATRI / BRILL DEUTSCHLAND GMBH | 0032-7034 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3089 | Jurnal Infektologii  Interregional public organiza / Unknown | 2499-9865 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3090 | MCB Molecular and Cellular Biomechanics Sin-Chn Sc / Unknown | 1556-5300 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3091 | JOURNAL OF ORTHOPAEDICS AND  TRAUMATOLOGY / SPRINGER | 1590-9921 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3092 | JBI Evidence Synthesis Lippincott Williams and Wil / Unknown | 2689-8381 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3093 | International Journal of Business Performance Mana / Unknown | 1368-4892 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3094 | Z Badan nad Ksiazka i Ksiegozbiorami Historycznymi / Unknown | 2544-8730 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3095 | Journal of Control Science and Engineering John Wi / Unknown | 1687-5249 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3096 | Journal of Classical Sociology SAGE Publications L / Unknown | 1468-795X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3097 | Comparative Exercise Physiology Brill Wageningen A / Unknown | 1755-2540 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3098 | Asian Journal of Comparative Law Cambridge Univers / Unknown | 1932-0205 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3099 | FORUM (The Netherlands) John Benjamins Publishing  / Unknown | 1598-7647 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3100 | Journal of Scleroderma and Related Disorders SAGE  / Unknown | 2397-1983 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3101 | Sankhya B Springer India / Unknown | 0976-8386 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3102 | Torture International Rehabilitation Council for T / Unknown | 1997-3322 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3103 | INTERNATIONAL JOURNAL OF SPRAY  AND COMBUSTION DYN / SAGE PUBLICATIONS INC | 1756-8277 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3104 | CRYOLETTERS / CRYO LETTERS | 1742-0644 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3105 | East Asian Journal of Popular Culture Intellect Lt / Unknown | 2051-7092 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3106 | Acta Phlebologica Edizioni Minerva Medica S.p.A. / Unknown | 1593-232X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3107 | Cleaner and Circular Bioeconomy Elsevier B.V. / Unknown | 2772-8013 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3108 | Dynamic Relationships Management Journal Slovenian / Unknown | 2350-367X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3109 | Journal of Optimization, Differential Equations an / Unknown | 2663-6824 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3110 | Iranian Journal of Information Processing Manageme / Unknown | 2251-8231 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3111 | International Journal of Standardization Research  / Unknown | 2470-8550 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3112 | Journal fur Neurologie, Neurochirurgie und Psychia / Unknown | 1680-9440 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3113 | Banking and Finance Review School of Business Cent / Unknown | 1947-7945 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3114 | ENVIRONMENTAL SCIENCE &  TECHNOLOGY / AMER CHEMICAL SOC | 1520-5851 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3115 | SYNTHESIS-STUTTGART / GEORG THIEME VERLAG KG | 0039-7881 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3116 | JOURNAL OF THE HISTORY OF  PHILOSOPHY / JOHNS HOPKINS UNIV PRESS | 1538-4586 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3117 | INTERNATIONAL BIODETERIORATION &  BIODEGRADATION / ELSEVIER SCI LTD | 0964-8305 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3118 | AURIS NASUS LARYNX / ELSEVIER SCI LTD | 0385-8146 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3119 | TELECOMMUNICATIONS POLICY / ELSEVIER SCI LTD | 0308-5961 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3120 | Revista Espanola de Cirugia Ortopedica y Traumatol / Unknown | 1988-8856 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3121 | AFFILIA-FEMINIST INQUIRY IN SOCIAL  WORK / SAGE PUBLICATIONS INC | 0886-1099 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3122 | ENERGY FOR SUSTAINABLE  DEVELOPMENT / ELSEVIER | 0973-0826 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3123 | LAW AND HUMAN BEHAVIOR / EDUCATIONAL PUBLISHING  FOUNDATION-AMERI | 0147-7307 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3124 | JOURNAL OF VASCULAR RESEARCH / KARGER | 1018-1172 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3125 | ULTRASOUND QUARTERLY / LIPPINCOTT WILLIAMS & WILKINS | 0894-8771 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3126 | Credit and Capital Markets Duncker und Humblot Gmb / Unknown | 2199-1235 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3127 | COMPLEMENTARY THERAPIES IN  CLINICAL PRACTICE / ELSEVIER SCI LTD | 1744-3881 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3128 | Annals of the ICRP SAGE Publications Inc. / Unknown | 0146-6453 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3129 | OXFORD ART JOURNAL / OXFORD UNIV PRESS | 0142-6540 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3130 | MM Science Journal MM Science Journal / Unknown | 1805-0476 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3131 | CHINESE STUDIES IN HISTORY / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 0009-4633 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3132 | EUROPEAN EARLY CHILDHOOD  EDUCATION RESEARCH JOURN / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1350-293X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3133 | SCANDINAVIAN JOURNAL OF SURGERY / SAGE PUBLICATIONS LTD | 1457-4969 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3134 | ANALYSIS AND MATHEMATICAL  PHYSICS / SPRINGER BASEL AG | 1664-235X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3135 | Journal of Applied Research in Higher Education Em / Unknown | 1758-1184 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3136 | Psiquiatria Biologica Elsevier Espana S.L.U / Unknown | 1134-5934 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3137 | REVIEW OF ACCOUNTING STUDIES / SPRINGER | 1380-6653 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3138 | CITY & COMMUNITY / SAGE PUBLICATIONS INC | 1535-6841 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3139 | Urology Reports (St. Petersburg) Eco-Vector LLC / Unknown | 2687-1416 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3140 | French Politics, Culture and Society Berghahn Jour / Unknown | 1558-5271 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3141 | Scrutiny2 Taylor and Francis Ltd. / Unknown | 1753-5409 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3142 | Paediatric Surgery (Ukraine) Group of Companies Me / Unknown | 2521-1358 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3143 | International Journal of Education Through Art Int / Unknown | 2040-090X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3144 | ACM TRANSACTIONS ON COMPUTER  SYSTEMS / ASSOC COMPUTING MACHINERY | 0734-2071 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3145 | Zoophilologica Wydawnictwo Uniwersytetu Slaskiego / Unknown | 2719-2687 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3146 | Revista Guillermo de Ockham University of San Buen / Unknown | 2256-3202 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3147 | International Journal of Online Pedagogy and Cours / Unknown | 2155-6881 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3148 | Hand Therapy SAGE Publications Inc. / Unknown | 1758-9983 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3149 | Autoimmune Diseases John Wiley and Sons Ltd / Unknown | 2090-0422 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3150 | Journal of Contemporary Archaeology Equinox Publis / Unknown | 2051-3437 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3151 | Discover Mechanical Engineering Springer Nature / Unknown | 2731-6564 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3152 | International Journal for Research in Vocational E / Unknown | 2197-8646 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3153 | Journal of Business Cycle Research Springer Intern / Unknown | 2509-7962 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3154 | Mongolian Geoscientist Mongolian University of Sci / Unknown | 2663-5151 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3155 | Historica (Ostrava) University of Ostrava / Unknown | 2695-060X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3156 | Petroleum Geology and Experiment Science Press / Unknown | 1001-6112 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3157 | JOURNAL OF MATERIALS PROCESSING  TECHNOLOGY / ELSEVIER SCIENCE SA | 0924-0136 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3158 | MONATSHEFTE FUR CHEMIE / SPRINGER WIEN | 0026-9247 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3159 | SYNTHETIC COMMUNICATIONS / TAYLOR & FRANCIS INC | 0039-7911 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3160 | IEEE COMMUNICATIONS MAGAZINE / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 0163-6804 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3161 | JOURNAL OF THROMBOSIS AND  HAEMOSTASIS / ELSEVIER SCIENCE INC | 1538-7836 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3162 | JOURNAL OF INDUSTRIAL AND  ENGINEERING CHEMISTRY / ELSEVIER SCIENCE INC | 1226-086X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3163 | TRENDS IN PHARMACOLOGICAL  SCIENCES / CELL PRESS | 0165-6147 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3164 | BRAZILIAN JOURNAL OF MEDICAL AND  BIOLOGICAL RESEA / ASSOC BRAS DIVULG CIENTIFICA | 1414-431X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3165 | Journal of Risk and Financial Management Multidisc / Unknown | 1911-8066 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3166 | JOURNAL OF HYDROLOGY-REGIONAL  STUDIES / ELSEVIER | 2214-5818 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3167 | Adoption and Fostering SAGE Publications Ltd / Unknown | 0308-5759 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3168 | CHEM / CELL PRESS | 2451-9294 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3169 | Chem Elsevier Inc. / Unknown | 2451-9308 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3170 | Revista Brasileira de  Epidemiologia Associacao Br / Unknown | 1980-5497 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3171 | TOURISM ECONOMICS / SAGE PUBLICATIONS LTD | 1354-8166 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3172 | ARTHURIANA / SCRIPTORIUM PRESS | 1934-1539 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3173 | Studies in Regional Science Japan Section of the R / Unknown | 1880-6465 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3174 | ARCHIPEL-ETUDES  INTERDISCIPLINAIRES SUR LE MONDE  / ASSOC ARCHIPEL | 2104-3655 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3175 | JOURNAL OF BUSINESS AND  PSYCHOLOGY / SPRINGER | 0889-3268 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3176 | TOPICS IN GERIATRIC REHABILITATION / LIPPINCOTT WILLIAMS & WILKINS | 0882-7524 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3177 | CHEMPHOTOCHEM / WILEY-V C H VERLAG GMBH | 2367-0932 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3178 | CLINICAL NEURORADIOLOGY / SPRINGER HEIDELBERG | 1869-1439 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3179 | Medicine, Conflict and Survival Routledge / Unknown | 1743-9396 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3180 | Tocqueville Review University of Toronto Press / Unknown | 0730-479X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3181 | Italianist Maney Publishing / Unknown | 1748-619X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3182 | RESEARCH IN PHENOMENOLOGY / BRILL | 0085-5553 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3183 | JOURNAL OF POLICY AND PRACTICE IN  INTELLECTUAL DI / WILEY | 1741-1122 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3184 | Multimodal Technologies and Interaction Multidisci / Unknown | 2414-4088 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3185 | International Journal of the Economics of Business / Unknown | 1466-1829 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3186 | JOURNAL OF ENVIRONMENTAL  ENGINEERING AND LANDSCAP / VILNIUS GEDIMINAS TECH UNIV | 1822-4199 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3187 | MENTAL HEALTH AND PHYSICAL  ACTIVITY / ELSEVIER SCI LTD | 1755-2966 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3188 | EARTH SURFACE DYNAMICS / COPERNICUS GESELLSCHAFT MBH | 2196-6311 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3189 | AFRICAN INVERTEBRATES / COUNCIL NATAL MUSEUM | 2305-2562 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3190 | TRANSPORTMETRICA B-TRANSPORT  DYNAMICS / TAYLOR & FRANCIS LTD | 2168-0566 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3191 | Revista Espanola de Cardiologia Suplementos Edicio / Unknown | 1579-2250 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3192 | Hikma UCOPress. Editorial Universidad de Cordoba / Unknown | 2445-4559 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3193 | Social Work and Social Sciences Review Whiting and / Unknown | 1746-6105 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3194 | LCGC NORTH AMERICA / MJH LIFE SCIENCES | 1939-1889 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3195 | Journal of Horticultural Research Sciendo / Unknown | 2300-5009 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3196 | ANNUAL REVIEW OF STATISTICS AND  ITS APPLICATION / ANNUAL REVIEWS | 2326-8298 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3197 | Journal of Globalization and Development Walter de / Unknown | 1948-1837 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3198 | AAPPS Bulletin Springer / Unknown | 0218-2203 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3199 | New Design Ideas Jomard Publishing / Unknown | 2524-2148 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3200 | Archives of legal medicine Elsevier Masson s.r.l. / Unknown | 2950-3949 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3201 | EVOLUTION / OXFORD UNIV PRESS | 0014-3820 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3202 | FOOD RESEARCH INTERNATIONAL / ELSEVIER | 0963-9969 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3203 | LAB ON A CHIP / ROYAL SOC CHEMISTRY | 1473-0189 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3204 | COMMUNICATIONS IN SOIL SCIENCE  AND PLANT ANALYSIS / TAYLOR & FRANCIS INC | 0010-3624 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3205 | AGRICULTURAL WATER MANAGEMENT / ELSEVIER | 0378-3774 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3206 | JOURNAL OF PHYSICS G-NUCLEAR AND  PARTICLE PHYSICS / IOP PUBLISHING LTD | 1361-6471 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3207 | JAPANESE JOURNAL OF CLINICAL  ONCOLOGY / OXFORD UNIV PRESS | 0368-2811 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3208 | COMPUTERS & GRAPHICS-UK / PERGAMON-ELSEVIER SCIENCE LTD | 0097-8493 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3209 | IEEE JOURNAL OF EMERGING AND  SELECTED TOPICS IN P / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 2168-6777 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3210 | JOURNAL OF HEALTH CARE FOR THE  POOR AND UNDERSERV / JOHNS HOPKINS UNIV PRESS | 1548-6869 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3211 | ACTA SOCIETATIS BOTANICORUM  POLONIAE / POLSKIE TOWARZYSTWO  BOTANICZNE | 2083-9480 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3212 | SALUD PUBLICA DE MEXICO / INST NACIONAL SALUD PUBLICA | 1606-7916 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3213 | TRIBOLOGY TRANSACTIONS / TAYLOR & FRANCIS INC | 1040-2004 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3214 | LETTERS IN ORGANIC CHEMISTRY / BENTHAM SCIENCE PUBL LTD | 1570-1786 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3215 | Practical Neurology BMJ Publishing Group / Unknown | 1474-7766 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3216 | SCANDINAVIAN JOURNAL OF  ECONOMICS / WILEY | 0347-0520 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3217 | JOURNAL OF WATERWAY PORT  COASTAL AND OCEAN ENGINE / ASCE-AMER SOC CIVIL ENGINEERS | 0733-950X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3218 | Journal of Indian Association of Pediatric Surgeon / Unknown | 0971-9261 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3219 | JOURNAL OF MEDICAL BIOGRAPHY / SAGE PUBLICATIONS INC | 0967-7720 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3220 | ARCHIV FUR PAPYRUSFORSCHUNG  UND VERWANDTE GEBIETE / WALTER DE GRUYTER GMBH | 0066-6459 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3221 | ADVANCES IN CEMENT RESEARCH / EMERALD GROUP PUBLISHING LTD | 0951-7197 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3222 | ECONOMICS OF INNOVATION AND  NEW TECHNOLOGY / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1043-8599 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3223 | Italian Culture Maney Publishing / Unknown | 1559-0909 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3224 | Journal of King Saud University - Engineering Scie / Unknown | 1018-3639 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3225 | RUSSIAN LINGUISTICS / SPRINGER | 0304-3487 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3226 | Imaging Science in Dentistry Korean Academy of Ora / Unknown | 2233-7830 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3227 | PERSONALITY AND MENTAL HEALTH / WILEY | 1932-8621 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3228 | Frontiers in Bioinformatics Frontiers Media SA / Unknown | 2673-7647 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3229 | Frontiers in Conservation Science Frontiers Media  / Unknown | 2673-611X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3230 | International Journal of Accounting, Auditing and  / Unknown | 1740-8008 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3231 | International Journal of Tourism Cities Emerald Gr / Unknown | 2056-5607 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3232 | International Arab Journal of Dentistry Saint Jose / Unknown | 2709-4774 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3233 | Control Theory and Technology Springer Science + B / Unknown | 2095-6983 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3234 | ZDRAVSTVENO VARSTVO / INST PUBLIC HEALTH REPUBLIC  SLOVENIA | 1854-2476 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3235 | European Journal for Sport and Society Taylor and  / Unknown | 1613-8171 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3236 | Proceedings of the ICE - Engineering History and H / Unknown | 1757-9449 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3237 | FILOZOFSKI VESTNIK / ZRC PUBLISHING | 1581-1239 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3238 | JOURNAL OF MANAGEMENT  ANALYTICS / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 2327-0012 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3239 | Journal of Urban and Regional Analysis Bucharest U / Unknown | 2068-9969 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3240 | London Review of International Law Oxford Universi / Unknown | 2050-6325 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3241 | ROBOTIC INTELLIGENCE AND  AUTOMATION / EMERALD GROUP PUBLISHING LTD | 2754-6969 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3242 | Shejzat Centre for Albanian Studies Shejzat - Plei / Unknown | 2517-9624 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3243 | Biochimie Elsevier B.V. / Unknown | 6183-1638 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3244 | REVUE DE MEDECINE INTERNE / ELSEVIER FRANCE-EDITIONS  SCIENTIFIQUES  | 0248-8663 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3245 | NEUROPSYCHOPHARMACOLOGY / SPRINGERNATURE | 0893-133X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3246 | ANALYSIS / OXFORD UNIV PRESS | 0003-2638 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3247 | WEED SCIENCE / CAMBRIDGE UNIV PRESS | 0043-1745 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3248 | INTERMETALLICS / ELSEVIER SCI LTD | 0966-9795 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3249 | APPLIED PHYSICS EXPRESS / IOP PUBLISHING LTD | 1882-0786 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3250 | JOURNAL OF PEDIATRIC AND  ADOLESCENT GYNECOLOGY / ELSEVIER SCIENCE INC | 1083-3188 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3251 | CRITICAL REVIEWS IN ONCOLOGY  HEMATOLOGY / ELSEVIER SCIENCE INC | 1040-8428 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3252 | QUALITY AND RELIABILITY  ENGINEERING INTERNATIONAL / WILEY | 0748-8017 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3253 | INSURANCE MATHEMATICS &  ECONOMICS / ELSEVIER | 0167-6687 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3254 | EXPERT OPINION ON INVESTIGATIONAL  DRUGS / TAYLOR & FRANCIS LTD | 1354-3784 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3255 | REVIEWS IN AMERICAN HISTORY / JOHNS HOPKINS UNIV PRESS | 1080-6628 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3256 | IEEE TRANSACTIONS ON EDUCATION / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 0018-9359 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3257 | COMPUTATIONAL MATHEMATICS AND  MATHEMATICAL PHYSIC / PLEIADES PUBLISHING INC | 0965-5425 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3258 | Cahiers d'Etudes Africaines Cairn France / N°   ISSN   E-ISSN | 1777-5353 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3259 | Industrial and Commercial Training Emerald Group P / Unknown | 0019-7858 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3260 | REVUE DE GEOGRAPHIE ALPINE- JOURNAL OF ALPINE RESE / IGA-ASSOC DIFFUSION RECHERCHE  ALPINE | 1760-7426 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3261 | THEATRE RESEARCH INTERNATIONAL / CAMBRIDGE UNIV PRESS | 0307-8833 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3262 | IEEE JOURNAL OF SELECTED TOPICS IN  SIGNAL PROCESS / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 1932-4553 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3263 | International Social Security Review Wiley-Blackwe / Unknown | 0020-871X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3264 | Athenea Digital Universitat Autonoma de Barcelona / Unknown | 2014-4539 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3265 | AFRICAN STUDIES / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 0002-0184 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3266 | JOURNAL OF SEISMOLOGY / SPRINGER | 1383-4649 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3267 | EXPERIMENTAL AGING RESEARCH / TAYLOR & FRANCIS INC | 0361-073X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3268 | Queue Association for Computing Machinery (ACM) / Unknown | 1542-7730 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3269 | International Journal of Public Sector Management  / Unknown | 0951-3558 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3270 | MARKETING LETTERS / SPRINGER | 0923-0645 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3271 | International Journal of Computing Science and Mat / Unknown | 1752-5055 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3272 | Sociologia Urbana e Rurale FrancoAngeli Edizioni / N°   ISSN   E-ISSN | 1971-8403 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3273 | WILEY INTERDISCIPLINARY REVIEWS- CLIMATE CHANGE / WILEY | 1757-7780 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3274 | Quality in Ageing and Older Adults Emerald Group P / Unknown | 1471-7794 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3275 | Studies in Documentary Film Taylor and Francis Ltd / Unknown | 1750-3280 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3276 | Asia-Pacific Journal of Research in Early Childhoo / Unknown | 2233-5234 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3277 | Chilean Journal of Agricultural and Animal Science / Unknown | 0719-3890 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3278 | Nervno-Myshechnye Bolezni ABV-press Publishing Hou / Unknown | 2413-0443 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3279 | Dynamics of Asymmetric Conflict: Pathways toward T / Unknown | 1746-7594 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3280 | SOCIETY AND MENTAL HEALTH / SAGE PUBLICATIONS INC | 2156-8693 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3281 | Polyolefins Journal Iran Polymer and Petrochemical / Unknown | 2345-6868 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3282 | EUROPEAN JOURNAL OF  ANAESTHESIOLOGY / LIPPINCOTT WILLIAMS & WILKINS | 0265-0215 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3283 | JOURNAL OF PHYSICS B-ATOMIC  MOLECULAR AND OPTICAL / IOP PUBLISHING LTD | 1361-6455 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3284 | NATURE METHODS / NATURE PORTFOLIO | 1548-7091 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3285 | Universum Universidad de Talca / Unknown | 0718-2376 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3286 | JOURNAL OF MANIPULATIVE AND  PHYSIOLOGICAL THERAPE / MOSBY-ELSEVIER | 0161-4754 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3287 | AUSTRALIAN SOCIAL WORK / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 0312-407X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3288 | REVIEW OF INCOME AND WEALTH / WILEY | 0034-6586 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3289 | Journal of Pain and Palliative Care Pharmacotherap / Unknown | 1536-0539 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3290 | NATURAL RESOURCES RESEARCH / SPRINGER | 1520-7439 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3291 | JAMA HEALTH FORUM / AMER MEDICAL ASSOC | 2689-0186 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3292 | ZOOLOGY IN THE MIDDLE EAST / TAYLOR & FRANCIS LTD | 0939-7140 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3293 | TEXTILE HISTORY / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 0040-4969 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3294 | COGNITIVE PSYCHOLOGY / ACADEMIC PRESS INC ELSEVIER  SCIENCE | 0010-0285 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3295 | Limnology and Oceanography Bulletin Wiley-Blackwel / Unknown | 1539-607X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3296 | INTERNATIONAL POLITICAL SCIENCE  REVIEW / SAGE PUBLICATIONS LTD | 0192-5121 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3297 | SEMINARS IN PLASTIC SURGERY / THIEME MEDICAL PUBL INC | 1535-2188 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3298 | BRAZILIAN JOURNAL OF  ANESTHESIOLOGY / ELSEVIER SCIENCE INC | 0104-0014 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3299 | SCANDINAVIAN STUDIES / SOC ADVANCEMENT SCAND STUD | 2163-8195 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3300 | Russian Journal of Pediatric Surgery, Anesthesia a / Unknown | 2587-6554 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3301 | Australian and New Zealand Journal of Statistics W / Unknown | 1369-1473 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3302 | AUSTRALIAN & NEW ZEALAND  JOURNAL OF STATISTICS / WILEY | 1467-842X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3303 | Korean Journal of Medical Education Korean Society / N°   ISSN   E-ISSN | 2005-7288 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3304 | Journal of Enhanced Heat Transfer Begell House Inc / Unknown | 1026-5511 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3305 | JOURNAL OF ENHANCED HEAT  TRANSFER / BEGELL HOUSE INC | 1065-5131 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3306 | REVIJA ZA SOCIJALNU POLITIKU / SVEUCLISTE ZAGREBU, PRAVNI  FAKULTED-UNI | 1845-6014 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3307 | JOURNAL OF APPLIED RESEARCH IN  MEMORY AND COGNITI / AMER PSYCHOLOGICAL ASSOC | 2211-3681 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3308 | SCANDINAVIAN JOURNAL OF UROLOGY / MEDICAL JOURNAL SWEDEN AB | 2168-1813 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3309 | Implicit Religion Equinox Publishing Ltd / Unknown | 1743-1697 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3310 | ACTA CHIROPTEROLOGICA / MUSEUM & INST ZOOLOGY PAS- POLISH ACAD S | 1733-5329 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3311 | FOUNDATIONS OF COMPUTATIONAL  MATHEMATICS / SPRINGER | 1615-3375 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3312 | Mathematical Modeling and Computing Lviv Polytechn / N°   ISSN   E-ISSN | 2415-3788 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3313 | American Political Thought University of Chicago P / Unknown | 2161-1580 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3314 | Environmental Health Insights SAGE Publications In / Unknown | 1178-6302 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3315 | International Journal of Intelligent Robotics and  / Unknown | 2366-5971 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3316 | International Journal of Construction Education an / Unknown | 1557-8771 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3317 | International Journal of Water Inderscience Enterp / Unknown | 1465-6620 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3318 | Journal of Bone and Joint Infection Copernicus Pub / Unknown | 2206-3552 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3319 | Global Media and China SAGE Publications Ltd / Unknown | 2059-4372 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3320 | Illinois Classical Studies University of Illinois  / Unknown | 0363-1923 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3321 | Geopolitica(s) Universidad Complutense Madrid / N°   ISSN   E-ISSN | 2172-7155 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3322 | Cesko-Slovenska Pediatrie Czech Medical Associatio / Unknown | 1805-4501 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3323 | Animal Science and Food Technology National Univer / Unknown | 2706-834X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3324 | International Journal of Technoentrepreneurship In / Unknown | 1746-5370 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3325 | Review of Computer Engineering Research Conscienti / Unknown | 2412-4281 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3326 | Estudios de Fonetica Experimental Universitat de B / Unknown | 2385-3573 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3327 | Journal of Mycology and Infection Korean Society f / Unknown | 3058-4302 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3328 | PEDIATRIC RESEARCH / SPRINGERNATURE | 0031-3998 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3329 | JOURNAL OF INVESTIGATIVE  DERMATOLOGY / ELSEVIER SCIENCE INC | 0022-202X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3330 | GEOCHIMICA ET COSMOCHIMICA ACTA / PERGAMON-ELSEVIER SCIENCE LTD | 0016-7037 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3331 | Tidsskrift for den Norske Legeforening Den norske  / Unknown | 0807-7096 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3332 | JOURNAL OF CHEMICAL INFORMATION  AND MODELING / AMER CHEMICAL SOC | 1549-960X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3333 | UNIVERSITY OF PENNSYLVANIA LAW  REVIEW / UNIV PENN LAW SCH | 0041-9907 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3334 | University of Pennsylvania Law Review University o / Unknown | 1942-8537 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3335 | REVISTA MEDICA DE CHILE / SOC MEDICA SANTIAGO | 0717-6163 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3336 | GACETA SANITARIA / ELSEVIER | 0213-9111 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3337 | MOLECULAR CARCINOGENESIS / WILEY | 0899-1987 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3338 | PHILOSOPHICAL MAGAZINE LETTERS / TAYLOR & FRANCIS LTD | 0950-0839 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3339 | THERAPIE / ELSEVIER | 0040-5957 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3340 | PAEDAGOGICA HISTORICA / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 0030-9230 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3341 | NUCLEAR SCIENCE AND TECHNIQUES / SPRINGER SINGAPORE PTE LTD | 1001-8042 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3342 | EUROPEAN JOURNAL OF  PROTISTOLOGY / ELSEVIER GMBH | 0932-4739 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3343 | CURRENT ALZHEIMER RESEARCH / BENTHAM SCIENCE PUBL LTD | 1567-2050 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3344 | INTERNATIONAL JOURNAL OF  PSYCHIATRY IN MEDICINE / SAGE PUBLICATIONS INC | 0091-2174 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3345 | JOURNAL OF MANAGERIAL  PSYCHOLOGY / EMERALD GROUP PUBLISHING LTD | 0268-3946 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3346 | JOURNAL OF X-RAY SCIENCE AND  TECHNOLOGY / IOS PRESS | 0895-3996 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3347 | Counselling and Psychotherapy Research Wiley-Black / Unknown | 1473-3145 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3348 | PROCEEDINGS OF THE INSTITUTION OF  CIVIL ENGINEERS / EMERALD GROUP PUBLISHING LTD | 0965-092X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3349 | Forum for Linguistic Studies Bilingual Publishing  / Unknown | 2705-0610 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3350 | Apeiron Walter de Gruyter GmbH / N°   ISSN   E-ISSN | 0003-6390 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3351 | TURKISH JOURNAL OF BIOLOGY / TUBITAK SCIENTIFIC &  TECHNOLOGICAL RESE | 1303-6092 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3352 | HEALTH CARE ANALYSIS / SPRINGER | 1065-3058 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3353 | ASIAN ECONOMIC JOURNAL / WILEY | 1351-3958 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3354 | KYBERNETIKA / KYBERNETIKA | 1805-949X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3355 | OCEAN SCIENCE JOURNAL / KOREA INST OCEAN SCIENCE &  TECHNOLOGY-K | 2005-7172 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3356 | Anesthesia Progress Allen Press Inc. / Unknown | 1878-7177 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3357 | DISSOLUTION TECHNOLOGIES / DISSOLUTION TECHNOLOGIES, INC | 2376-869X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3358 | Slavic and East European Information Resources Rou / Unknown | 1522-9041 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3359 | NEW REVIEW OF FILM AND TELEVISION  STUDIES / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1740-0309 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3360 | INTERNATIONAL JOURNAL OF  HYPERTENSION / WILEY | 2090-0384 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3361 | Natural Products and Bioprospecting Springer Singa / Unknown | 2192-2195 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3362 | International Journal of Manufacturing Research In / Unknown | 1750-0591 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3363 | Oncology and Translational Medicine Lippincott Wil / Unknown | 2095-9621 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3364 | Fuzzy Information and Engineering Tsinghua Univers / Unknown | 1616-8666 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3365 | POLITICS PHILOSOPHY & ECONOMICS / SAGE PUBLICATIONS INC | 1470-594X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3366 | International Journal of Gaming and Computer-Media / Unknown | 1942-3896 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3367 | Journal of African Cinemas Intellect Ltd. / Unknown | 1754-923X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3368 | Applied Environmental Research Environmental Resea / N°   ISSN   E-ISSN | 2287-075X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3369 | PERIODICO DI MINERALOGIA / SAPIENZA UNIV EDITRICE | 2239-1002 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3370 | Cultural Perspectives Vasile Alecsandri University / Unknown | 2559-3439 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3371 | Photography in Asia Brill / Unknown | 2405-7800 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3372 | SPINE / LIPPINCOTT WILLIAMS & WILKINS | 0362-2436 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3373 | ASAIO JOURNAL / LIPPINCOTT WILLIAMS & WILKINS | 1058-2916 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3374 | JOURNAL OF THE AMERICAN MEDICAL  DIRECTORS ASSOCIA / ELSEVIER SCIENCE INC | 1525-8610 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3375 | JOURNAL OF GASTROINTESTINAL  SURGERY / ELSEVIER SCIENCE INC | 1091-255X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3376 | INTERNATIONAL JOURNAL FOR  PARASITOLOGY / ELSEVIER SCI LTD | 0020-7519 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3377 | APPLIED INTELLIGENCE / SPRINGER | 0924-669X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3378 | Engineering, Technology and Applied Science Resear / Unknown | 2241-4487 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3379 | JOURNAL OF THE AMERICAN  PHARMACISTS ASSOCIATION / ELSEVIER | 1544-3191 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3380 | Jahrbuch fur Wirtschaftsgeschichte Walter de Gruyt / Unknown | 0075-2800 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3381 | CURRENT OPINION IN  PHARMACOLOGY / ELSEVIER SCI LTD | 1471-4892 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3382 | TRANSLATIONAL LUNG CANCER  RESEARCH / AME PUBLISHING COMPANY | 2218-6751 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3383 | JOURNAL OF BIOPHARMACEUTICAL  STATISTICS / TAYLOR & FRANCIS INC | 1054-3406 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3384 | Value in Health Regional Issues Elsevier Inc. / Unknown | 2212-1099 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3385 | Biomedical Reports Spandidos Publications / Unknown | 2049-9442 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3386 | Journal of Basic and Clinical Physiology and Pharm / Unknown | 0792-6855 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3387 | SOUTH AFRICAN HISTORICAL JOURNAL / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 0258-2473 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3388 | RUSSIAN JOURNAL OF MARINE  BIOLOGY / MAIK  NAUKA/INTERPERIODICA/SPRINGER | 1063-0740 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3389 | Antitrust Bulletin SAGE Publications Inc. / Unknown | 0003-603X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3390 | Herzschrittmachertherapie und Elektrophysiologie D / Unknown | 1435-1544 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3391 | JOURNAL OF THE ACADEMY OF  CONSULTATION-LIAISON PS / ELSEVIER SCIENCE INC | 2667-2960 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3392 | Journal of the Academy of Consultation-Liaison Psy / Unknown | 2667-2979 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3393 | Scientific and Technical Journal of Information Te / Unknown | 2500-0373 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3394 | SA Journal of Industrial Psychology AOSIS (Pty) Lt / Unknown | 2071-0763 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3395 | MYCOBIOLOGY / TAYLOR & FRANCIS LTD | 1229-8093 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3396 | NBER MACROECONOMICS ANNUAL / UNIV CHICAGO PRESS | 0889-3365 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3397 | COGNITIVE PROCESSING / SPRINGER HEIDELBERG | 1612-4782 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3398 | International Journal of Sociology Taylor and Fran / Unknown | 1557-9336 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3399 | Ankara Universitesi Eczacilik Fakultesi Dergisi Un / Unknown | 2564-6524 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3400 | Teoria de la Educacion Universidad de Salamanca, F / Unknown | 2386-5660 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3401 | Estudos de Psicologia (Natal) Universidade Federal / Unknown | 1678-4669 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3402 | Journal of Industrial and Business Economics Sprin / Unknown | 0391-2078 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3403 | European Journal of Political Theory SAGE Publicat / Unknown | 1474-8851 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3404 | USER MODELING AND USER-ADAPTED  INTERACTION / SPRINGER | 0924-1868 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3405 | COMPARATIVE MIGRATION STUDIES / SPRINGERNATURE | 2214-594X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3406 | Journal of Asia-Pacific Business Routledge / Unknown | 1528-6940 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3407 | OPEN ARCHAEOLOGY / DE GRUYTER POLAND SP Z O O | 2300-6560 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3408 | INFORMATICS FOR HEALTH & SOCIAL  CARE / TAYLOR & FRANCIS INC | 1753-8157 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3409 | International Journal of Information Systems in th / Unknown | 1935-5688 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3410 | Norwegian-American Studies University of Minnesota / Unknown | 2643-8437 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3411 | Journal of Skyscape Archaeology Equinox Publishing / Unknown | 2055-3498 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3412 | Palgrave Studies in Prisons and Penology Springer: / Unknown | 2753-0604 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3413 | Journal of East Asian Cultures Eotvos Lorand Tudom / Unknown | 2786-2976 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3414 | Complex Psychiatry S. Karger AG / Unknown | 2673-298X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3415 | ARCHIVES OF PATHOLOGY &  LABORATORY MEDICINE / COLL AMER PATHOLOGISTS | 1543-2165 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3416 | SIAM JOURNAL ON MATHEMATICAL  ANALYSIS / SIAM PUBLICATIONS | 0036-1410 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3417 | JOURNAL OF ARCHAEOLOGICAL  SCIENCE-REPORTS / ELSEVIER | 2352-409X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3418 | SPECTROSCOPY LETTERS / TAYLOR & FRANCIS INC | 0038-7010 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3419 | JOURNAL OF ELECTRONIC IMAGING / SPIE-SOC PHOTO-OPTICAL  INSTRUMENTATION  | 1560-229X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3420 | JOURNAL OF GRAPH THEORY / WILEY | 0364-9024 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3421 | BMC ANESTHESIOLOGY / BMC | 1471-2253 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3422 | SOCIETY & NATURAL RESOURCES / TAYLOR & FRANCIS INC | 0894-1920 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3423 | JOURNAL OF THE NATIONAL MEDICAL  ASSOCIATION / ELSEVIER SCIENCE INC | 0027-9684 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3424 | Applied Mathematics and Information Sciences Natur / Unknown | 2325-0399 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3425 | SOCIAL COGNITIVE AND AFFECTIVE  NEUROSCIENCE / OXFORD UNIV PRESS | 1749-5016 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3426 | TOXICOLOGY RESEARCH / OXFORD UNIV PRESS | 2045-452X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3427 | Polymer Science - Series D Pleiades Publishing / Unknown | 1995-4212 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3428 | Rechtsgeschichte Klostermann / Unknown | 2195-9617 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3429 | HEALTH INFORMATION AND LIBRARIES  JOURNAL / WILEY | 1471-1834 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3430 | DOSE-RESPONSE / SAGE PUBLICATIONS INC | 1559-3258 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3431 | JAPANESE ECONOMIC REVIEW / SPRINGER HEIDELBERG | 1352-4739 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3432 | COLONIAL LATIN AMERICAN REVIEW / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1060-9164 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3433 | Kesmas: Jurnal Kesehatan Masyarakat Nasional Unive / Unknown | 2460-0601 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3434 | Interventional Cardiology Clinics Elsevier Inc. / N°   ISSN   E-ISSN | 2211-7458 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3435 | EUROPEAN PHYSICAL EDUCATION  REVIEW / SAGE PUBLICATIONS LTD | 1356-336X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3436 | Proceedings of the Indian National Science Academy / Unknown | 2454-9983 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3437 | Review of Philosophy and Psychology Springer Verla / Unknown | 1878-5158 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3438 | PROGRESS IN CRYSTAL GROWTH AND  CHARACTERIZATION O / PERGAMON-ELSEVIER SCIENCE LTD | 0960-8974 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3439 | MODERNIST CULTURES / EDINBURGH UNIV PRESS | 1753-8629 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3440 | Clinical and Experimental Hepatology Termedia Publ / Unknown | 2449-8238 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3441 | FACTA UNIVERSITATIS-SERIES  MECHANICAL ENGINEERING / UNIV NIS | 2335-0164 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3442 | International Journal of Islamic Thought Universit / Unknown | 2289-6023 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3443 | International Journal of Childbirth Springer Publi / Unknown | 2156-5287 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3444 | Minerva Dental and Oral Science Edizioni Minerva M / Unknown | 2724-6329 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3445 | Russian Journal of Nonlinear Dynamics Institute of / Unknown | 2658-5324 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3446 | Notas Economicas Imprensa da Universidade de Coimb / N°   ISSN   E-ISSN | 2183-203X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3447 | Journal of Music, Technology and Education Intelle / Unknown | 1752-7074 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3448 | Jordanian Journal of Computers and Information Tec / Unknown | 2415-1076 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3449 | Curriculum Studies in Health and Physical Educatio / Unknown | 2574-299X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3450 | Horticulture Advances Springer / Unknown | 2948-1104 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3451 | Journal of Islamic Law Institut Agama Islam Negeri / Unknown | 2721-5040 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3452 | BULGARIAN HISTORICAL REVIEW- REVUE BULGARE D HISTO / PUBL HOUSE BULGARIAN ACAD SCI | 2815-2905 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3453 | STUDI SECENTESCHI / CASA EDITRICE LEO S OLSCHKI | 2035-7966 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3454 | JOURNAL OF THE INDIAN SOCIETY OF  REMOTE SENSING / SPRINGER | 0255-660X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3455 | Mini-Monographs in Literary and Cultural Studies B / Unknown | 2772-5464 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3456 | JOURNAL OF QUANTITATIVE  SPECTROSCOPY & RADIATIVE  / PERGAMON-ELSEVIER SCIENCE LTD | 0022-4073 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3457 | ECOLOGICAL ECONOMICS / ELSEVIER | 0921-8009 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3458 | Drugs of the Future Clarivate / Unknown | 2013-0368 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3459 | BIOSCIENCE REPORTS / PORTLAND PRESS LTD | 1573-4935 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3460 | NUTRITION AND CANCER-AN  INTERNATIONAL JOURNAL / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 0163-5581 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3461 | Journal of Robotics and Mechatronics Fuji Technolo / Unknown | 1883-8049 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3462 | POTATO RESEARCH / SPRINGER | 0014-3065 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3463 | JOURNAL OF AGRICULTURAL  ECONOMICS / WILEY | 0021-857X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3464 | JOURNAL OF THE AMERICAN SOCIETY  OF BREWING CHEMIS / TAYLOR & FRANCIS LTD | 0361-0470 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3465 | JOURNAL OF COMPARATIVE  ECONOMICS / ACADEMIC PRESS INC ELSEVIER  SCIENCE | 0147-5967 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3466 | Family Journal SAGE Publications Inc. / Unknown | 1066-4807 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3467 | JOURNAL OF THE KOREAN CERAMIC  SOCIETY / SPRINGER HEIDELBERG | 1229-7801 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3468 | MOUNTAIN RESEARCH AND  DEVELOPMENT / INT MOUNTAIN SOC | 1994-7151 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3469 | PSYCHOANALYTIC DIALOGUES / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1048-1885 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3470 | TOPOI-AN INTERNATIONAL REVIEW OF  PHILOSOPHY / SPRINGER | 0167-7411 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3471 | COMMUNICATIONS IN  CONTEMPORARY MATHEMATICS / WORLD SCIENTIFIC PUBL CO PTE  LTD | 0219-1997 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3472 | FRENCH HISTORICAL STUDIES / DUKE UNIV PRESS | 0016-1071 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3473 | JOURNAL OF EXOTIC PET MEDICINE / ELSEVIER SCIENCE INC | 1557-5063 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3474 | JOURNAL OF RETAILING / ELSEVIER SCIENCE INC | 0022-4359 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3475 | JOURNAL OF SPECIAL EDUCATION  TECHNOLOGY / SAGE PUBLICATIONS INC | 0162-6434 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3476 | Parliaments, Estates and Representation Taylor and / Unknown | 0260-6755 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3477 | POLIS / BRILL | 0142-257X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3478 | EXTREMES / SPRINGER | 1386-1999 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3479 | Obstetrics and Gynecology International John Wiley / N°   ISSN   E-ISSN | 1687-9589 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3480 | Palaeoentomology Magnolia Press / Unknown | 2624-2834 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3481 | International Journal for Quality Research Univers / N°   ISSN   E-ISSN | 1800-7473 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3482 | Esbocos Universidade Federal de Santa Catarina / Unknown | 2175-7976 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3483 | International Journal of Nanoparticles Inderscienc / Unknown | 1753-2507 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3484 | Evidence-Based Practice in Child and Adolescent Me / Unknown | 2379-4933 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3485 | Composites: Mechanics, Computations, Applications  / Unknown | 2152-2057 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3486 | Journal of Environmental Economics and Policy Tayl / Unknown | 2160-6544 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3487 | Interest Groups and Advocacy Palgrave Macmillan Lt / Unknown | 2047-7414 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3488 | Archiwum Medycyny Sadowej i Kryminologii Polskie T / Unknown | 1689-1716 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3489 | ATHEROSCLEROSIS PLUS / ELSEVIER | 2667-0895 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3490 | African Evaluation Journal AOSIS (Pty) Ltd / Unknown | 2310-4988 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3491 | Pravara Medical Review Deemed University / Unknown | 0976-0164 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3492 | Ocean Systems Engineering Techno-Press / Unknown | 2093-6702 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3493 | Jurnal Penelitian Kehutanan Wallacea Hasanuddin Un / Unknown | 2407-7860 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3494 | Biopesticides International Connect Journals / Unknown | 0976-9412 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3495 | Quaderns de Filologia: Estudis Literaris Universit / Unknown | 2444-1457 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3496 | CYTOGENETIC AND GENOME  RESEARCH / KARGER | 1424-8581 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3497 | JOURNAL OF CHROMATOGRAPHY A / ELSEVIER | 0021-9673 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3498 | COLLOIDS AND SURFACES A- PHYSICOCHEMICAL AND ENGIN / ELSEVIER | 0927-7757 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3499 | JOURNAL OF EXPERIMENTAL BOTANY / OXFORD UNIV PRESS | 0022-0957 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3500 | FORESTS / MDPI | 1999-4907 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3501 | JOURNAL OF THE KOREAN PHYSICAL  SOCIETY / KOREAN PHYSICAL SOC | 1976-8524 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3502 | COMPUTERS & CHEMICAL  ENGINEERING / PERGAMON-ELSEVIER SCIENCE LTD | 0098-1354 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3503 | MOLECULAR BIOLOGY AND  EVOLUTION / OXFORD UNIV PRESS | 0737-4038 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3504 | AESTHETIC SURGERY JOURNAL / OXFORD UNIV PRESS INC | 1090-820X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3505 | EUROPEAN PHYSICAL JOURNAL- SPECIAL TOPICS / SPRINGER HEIDELBERG | 1951-6355 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3506 | TRANSPORTATION RESEARCH PART A- POLICY AND PRACTIC / PERGAMON-ELSEVIER SCIENCE LTD | 0965-8564 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3507 | JOURNAL OF LOSS PREVENTION IN THE  PROCESS INDUSTR / ELSEVIER SCI LTD | 0950-4230 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3508 | ACTA HISTOCHEMICA / ELSEVIER GMBH | 0065-1281 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3509 | JOURNAL OF VACUUM SCIENCE &  TECHNOLOGY B / A V S AMER INST PHYSICS | 2166-2754 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3510 | PRIMARY CARE / W B SAUNDERS CO-ELSEVIER INC | 0095-4543 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3511 | VIOLENCE AGAINST WOMEN / SAGE PUBLICATIONS INC | 1077-8012 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3512 | NEW ZEALAND JOURNAL OF CROP AND  HORTICULTURAL SCI / TAYLOR & FRANCIS LTD | 0114-0671 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3513 | REVISTA DE LA REAL ACADEMIA DE  CIENCIAS EXACTAS F / SPRINGER-VERLAG ITALIA SRL | 1578-7303 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3514 | Medical Journal of Babylon Wolters Kluwer Medknow  / Unknown | 1812-156X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3515 | DAEDALUS / MIT PRESS | 1548-6192 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3516 | DENDROCHRONOLOGIA / ELSEVIER GMBH | 1125-7865 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3517 | LIMNETICA / ASOC ESPAN LIMNOL-MISLATA | 1989-1806 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3518 | Limnetica / Unknown | 2660-8537 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3519 | Journal of Park and Recreation Administration Saga / Unknown | 2160-6862 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3520 | JOURNAL OF SPORT & SOCIAL ISSUES / SAGE PUBLICATIONS INC | 0193-7235 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3521 | KENNEDY INSTITUTE OF ETHICS  JOURNAL / JOHNS HOPKINS UNIV PRESS | 1086-3249 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3522 | Canadian Journal of Latin American and Caribbean S / Unknown | 0826-3663 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3523 | EPIGENETICS & CHROMATIN / BMC | 1756-8935 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3524 | ATTACHMENT & HUMAN  DEVELOPMENT / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1461-6734 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3525 | Black Camera Indiana University Press / Unknown | 1947-4237 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3526 | Journal of Visual Communication in Medicine Inform / Unknown | 1745-3062 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3527 | ARID LAND RESEARCH AND  MANAGEMENT / TAYLOR & FRANCIS INC | 1532-4982 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3528 | Religion and Education Taylor and Francis Ltd. / N°   ISSN   E-ISSN | 1550-7394 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3529 | Infectious Disease Modelling KeAi Communications C / Unknown | 2468-2152 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3530 | Journal of Occupational Therapy, Schools, and Earl / Unknown | 1941-1251 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3531 | PharmacoEconomics - Open Springer International Pu / Unknown | 2509-4254 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3532 | MISSISSIPPI QUARTERLY / JOHNS HOPKINS UNIV PRESS | 2689-517X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3533 | International Journal of Human Rights in Healthcar / Unknown | 2056-4902 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3534 | GETTY RESEARCH JOURNAL / GETTY RESEARCH INST | 2329-1249 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3535 | International Journal of Fashion Studies Intellect / Unknown | 2051-7114 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3536 | One Earth Cell Press / Unknown | 2367-8194 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3537 | GeoScape Sciendo / Unknown | 1802-1115 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3538 | Nanomedicine Research Journal Tehran University of / Unknown | 2476-7123 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3539 | PEDIATRIC CLINICS OF NORTH  AMERICA / W B SAUNDERS CO-ELSEVIER INC | 0031-3955 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3540 | NATURAL PRODUCT  COMMUNICATIONS / SAGE PUBLICATIONS INC | 1555-9475 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3541 | FOOD SCIENCE & NUTRITION / WILEY | 2048-7177 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3542 | ZOOLOGICAL JOURNAL OF THE  LINNEAN SOCIETY / OXFORD UNIV PRESS | 0024-4082 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3543 | ABDOMINAL RADIOLOGY / SPRINGER | 2366-004X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3544 | ACTA PHARMACOLOGICA SINICA / NATURE PUBL GROUP | 1671-4083 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3545 | Reviews of Modern Physics / Unknown | 1538-4527 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3546 | REVIEWS OF MODERN PHYSICS / AMER PHYSICAL SOC | 1539-0756 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3547 | JOURNAL OF ZOO AND WILDLIFE  MEDICINE / AMER ASSOC ZOO VETERINARIANS | 1937-2825 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3548 | METABOLIC BRAIN DISEASE / SPRINGER/PLENUM PUBLISHERS | 0885-7490 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3549 | JOURNAL OF SYSTEMS ARCHITECTURE / ELSEVIER | 1383-7621 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3550 | STATISTICS / TAYLOR & FRANCIS LTD | 0233-1888 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3551 | Optoelectronics Letters Springer Verlag / Unknown | 1673-1905 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3552 | SOCIOLOGY OF RELIGION / OXFORD UNIV PRESS INC | 1069-4404 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3553 | SOIL RESEARCH / CSIRO PUBLISHING | 1838-675X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3554 | DRUG METABOLISM REVIEWS / TAYLOR & FRANCIS LTD | 0360-2532 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3555 | Groundwater for Sustainable Development Elsevier B / Unknown | 2352-801X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3556 | INTERNATIONAL JOURNAL OF TURBO &  JET-ENGINES / WALTER DE GRUYTER GMBH | 0334-0082 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3557 | Annali dell'Universita di Ferrara Springer-Verlag  / Unknown | 0430-3202 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3558 | GROUP DECISION AND NEGOTIATION / SPRINGER | 0926-2644 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3559 | AZANIA-ARCHAEOLOGICAL RESEARCH  IN AFRICA / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 0067-270X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3560 | ANNALS OF DYSLEXIA / SPRINGER | 0736-9387 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3561 | HYPERTENSION IN PREGNANCY / TAYLOR & FRANCIS INC | 1064-1955 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3562 | Journal of Nursing Measurement Springer Publishing / Unknown | 1061-3749 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3563 | Journal of Clinical Neuromuscular Disease Lippinco / Unknown | 1522-0443 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3564 | KANTIAN REVIEW / CAMBRIDGE UNIV PRESS | 1369-4154 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3565 | Cuadernos de Arte de la Universidad de Granada Edi / Unknown | 2445-4567 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3566 | Advances in Horticultural Science University of Fl / Unknown | 1592-1573 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3567 | Journal of Iberian and Latin American Research Rou / Unknown | 2151-9668 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3568 | Journal of Low Power Electronics and Applications  / Unknown | 2079-9268 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3569 | JOURNAL OF SYMPLECTIC GEOMETRY / INT PRESS BOSTON, INC | 1540-2347 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3570 | Journal of Communications Software and Systems Uni / Unknown | 1845-6421 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3571 | Journal of Communications Software and Systems / Unknown | 1846-6079 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3572 | Frontiers of Law in China Higher Education Press L / Unknown | 1673-3428 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3573 | ACM Journal of Experimental Algorithmics Associati / Unknown | 1084-6654 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3574 | European Journal of Mental Health Semmelweis Unive / Unknown | 1788-7119 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3575 | Bioelectricity Mary Ann Liebert Inc. / Unknown | 2576-3105 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3576 | Cuadernos.info Pontificia Universidad Catolica de  / N°   ISSN   E-ISSN | 0719-367X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3577 | Computability SAGE Publications Ltd / Unknown | 2211-3568 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3578 | CCF Transactions on High Performance Computing Spr / Unknown | 2524-4922 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3579 | Imago - Revista de Emblematica y Cultura Visual Un / Unknown | 2254-9633 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3580 | Hawaii Journal of Health and Social Welfare Univer / Unknown | 2641-5224 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3581 | Imagination and Praxis: Criticality and Creativity / Unknown | 2542-9140 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3582 | JOURNAL OF THE ATMOSPHERIC  SCIENCES / AMER METEOROLOGICAL SOC | 0022-4928 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3583 | CELLULOSE / SPRINGER | 0969-0239 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3584 | SCOTTISH MEDICAL JOURNAL / SAGE PUBLICATIONS LTD | 0036-9330 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3585 | EXPLICATOR / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 0014-4940 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3586 | INTERNATIONAL JOURNAL OF  NURSING STUDIES / PERGAMON-ELSEVIER SCIENCE LTD | 0020-7489 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3587 | MENDELEEV COMMUNICATIONS / ELSEVIER | 0959-9436 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3588 | MEMBRANES / MDPI | 2077-0375 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3589 | Aktuelle Ernahrungsmedizin Klinik und Praxis Georg / Unknown | 0341-0501 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3590 | AMERICAN JOURNAL ON ADDICTIONS / WILEY | 1055-0496 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3591 | Biopolymers and Cell National Academy of Sciences  / Unknown | 1993-6842 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3592 | TWIN RESEARCH AND HUMAN  GENETICS / CAMBRIDGE UNIV PRESS | 1832-4274 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3593 | FOLIA LINGUISTICA / WALTER DE GRUYTER GMBH | 0165-4004 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3594 | PERSPECTIVES IN PUBLIC HEALTH / SAGE PUBLICATIONS LTD | 1757-9139 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3595 | JOURNAL OF MOLECULAR HISTOLOGY / SPRINGER | 1567-2379 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3596 | SOCIAL DEVELOPMENT / WILEY | 0961-205X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3597 | JOURNAL OF MEDICAL SCREENING / SAGE PUBLICATIONS LTD | 0969-1413 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3598 | JOURNAL OF CHILD SEXUAL ABUSE / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1053-8712 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3599 | JOURNAL OF FRENCH LANGUAGE  STUDIES / CAMBRIDGE UNIV PRESS | 0959-2695 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3600 | ASSAY AND DRUG DEVELOPMENT  TECHNOLOGIES / MARY ANN LIEBERT, INC | 1540-658X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3601 | NANOTECHNOLOGY REVIEWS / DE GRUYTER POLAND SP Z O O | 2191-9089 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3602 | PHENOMENOLOGY AND THE  COGNITIVE SCIENCES / SPRINGER | 1568-7759 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3603 | South Asia Research Sage Publications India Pvt. L / N°   ISSN   E-ISSN | 0262-7280 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3604 | Materials Science-Poland Sciendo / Unknown | 2083-1331 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3605 | MATERIALS SCIENCE-POLAND / SCIENDO | 2083-134X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3606 | NONLINEAR ANALYSIS-MODELLING  AND CONTROL / VILNIUS UNIV, INST MATHEMATICS  & INFORM | 2335-8963 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3607 | INTERNATIONAL JOURNAL OF  PRECISION ENGINEERING AN / KOREAN SOC PRECISION ENG | 2288-6206 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3608 | Radiological Physics and Technology Springer Japan / Unknown | 1865-0333 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3609 | MAIN GROUP CHEMISTRY / IOS PRESS | 1024-1221 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3610 | Advances in Radio Science Copernicus Publications / Unknown | 1684-9965 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3611 | Intractable and Rare Diseases Research Internation / Unknown | 2186-361X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3612 | Clean Air Journal National Association of Clean Ai / Unknown | 2410-972X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3613 | AUS Universidad Austral de Chile / Unknown | 0718-7262 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3614 | International Journal of Enterprise Information Sy / Unknown | 1548-1115 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3615 | Monographs in Oral Science S. Karger AG / Unknown | 0077-0892 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3616 | Revista de  Investigacion en Educacion Universidad / Unknown | 2172-3427 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3617 | Avicenna Journal of Clinical Microbiology and Infe / Unknown | 2383-0298 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3618 | Manuscript Studies University of Pennsylvania Pres / Unknown | 2380-1190 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3619 | Europa XXI Insitute of Geography and Spatial Organ / Unknown | 2300-8547 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3620 | Geoloski Anali Balkanskoga Poluostrva University o / Unknown | 2406-0747 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3621 | Life Metabolism Oxford University Press / Unknown | 2755-0230 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3622 | Jazz Education in Research and Practice Indiana Un / Unknown | 2639-7676 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3623 | Brain Multiphysics Elsevier B.V. / Unknown | 2666-5220 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3624 | Word and Text Petroleum-Gas University of Ploiesti / Unknown | 2247-9163 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3625 | JOURNAL OF VIROLOGY / AMER SOC MICROBIOLOGY | 0022-538X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3626 | EPILEPSIA / WILEY | 0013-9580 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3627 | JOURNAL OF THE LONDON  MATHEMATICAL SOCIETY-SECOND / WILEY | 0024-6107 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3628 | MATERIALS CHARACTERIZATION / ELSEVIER SCIENCE INC | 1044-5803 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3629 | BMC PREGNANCY AND CHILDBIRTH / BMC | 1471-2393 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3630 | Organic Chemistry Frontiers Royal Society of Chemi / Unknown | 2052-4110 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3631 | ORGANIC CHEMISTRY FRONTIERS / ROYAL SOC CHEMISTRY | 2052-4129 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3632 | ZEITSCHRIFT FUR SLAWISTIK / WALTER DE GRUYTER GMBH | 0044-3506 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3633 | RUSSIAN CHEMICAL REVIEWS / ND ZELINSKY INST ORGANIC  CHEMISTRY, RAS | 1468-4837 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3634 | Agricultural Engineering De Gruyter Open Ltd. / Unknown | 2083-1587 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3635 | INTERNATIONAL JOURNAL OF  ACAROLOGY / TAYLOR & FRANCIS INC | 0164-7954 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3636 | ANNALES SCIENTIFIQUES DE L ECOLE  NORMALE SUPERIEU / SOC MATHEMATIQUE FRANCE | 1873-2151 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3637 | AI MAGAZINE / AMER ASSOC ARTIFICIAL INTELL | 2371-9621 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3638 | PHILOSOPHY AND LITERATURE / JOHNS HOPKINS UNIV PRESS | 1086-329X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3639 | PSYCHOTHERAPY RESEARCH / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1050-3307 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3640 | INTEGRAL TRANSFORMS AND SPECIAL  FUNCTIONS / TAYLOR & FRANCIS LTD | 1065-2469 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3641 | E-POLYMERS / DE GRUYTER POLAND SP Z O O | 1618-7229 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3642 | INTERNATIONAL REVIEW FOR THE  SOCIOLOGY OF SPORT / SAGE PUBLICATIONS LTD | 1012-6902 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3643 | COGNITIVE DEVELOPMENT / ELSEVIER SCIENCE INC | 0885-2014 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3644 | Journal of Postgraduate Medical Institute Postgrad / Unknown | 1811-9387 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3645 | POLITICAL COMMUNICATION / TAYLOR & FRANCIS INC | 1058-4609 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3646 | Journal of Engineering Sciences Assiut University, / Unknown | 2356-8550 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3647 | Aula Abierta Universidad de Oviedo / Unknown | 2341-2313 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3648 | Accounting Education Routledge / Unknown | 1468-4489 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3649 | CHEMICAL AND PROCESS  ENGINEERING-NEW FRONTIERS / POLSKA AKAD NAUK, POLISH ACAD  SCIENCES | 0208-6425 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3650 | INTERNATIONAL JOURNAL OF SOCIAL  PSYCHOLOGY / SAGE PUBLICATIONS INC | 0213-4748 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3651 | SCHOOL MENTAL HEALTH / SPRINGER | 1866-2625 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3652 | FOLIA HORTICULTURAE / SCIENDO | 0867-1761 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3653 | RESEARCH IN ENGINEERING DESIGN / SPRINGER HEIDELBERG | 0934-9839 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3654 | Journal of Obstetrics, Gynecology and Cancer Resea / Unknown | 2476-5848 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3655 | Journal of Obstetrics Gynecology and Cancer Resear / Unknown | 2645-3843 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3656 | RIVISTA DEL NUOVO CIMENTO / SPRINGERNATURE | 0393-697X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3657 | New Journal of European Criminal Law SAGE Publicat / Unknown | 2032-2844 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3658 | International Journal of Disaster Resilience in th / Unknown | 1759-5908 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3659 | Recherche et Pratiques Pedagogiques en Langues de  / Unknown | 2257-5405 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3660 | Revista Geografica Venezolana Universidad de los A / Unknown | 2244-8853 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3661 | Muziki Routledge / Unknown | 1812-5980 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3662 | Advances in Human-Computer Interaction John Wiley  / N°   ISSN   E-ISSN | 1687-5893 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3663 | Curved and Layered Structures Walter de Gruyter Gm / Unknown | 2353-7396 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3664 | Urban Rail Transit Springer Science and Business M / Unknown | 2199-6679 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3665 | JOURNAL OF LANGUAGE LITERATURE  AND CULTURE / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 2051-2856 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3666 | Journal of Bodies, Sexualities, and Masculinities  / Unknown | 2688-8157 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3667 | CHROMATOGRAPHIA / SPRINGER HEIDELBERG | 0009-5893 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3668 | GERIATRIC NURSING / MOSBY-ELSEVIER | 0197-4572 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3669 | IMMUNOBIOLOGY / ELSEVIER GMBH | 0171-2985 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3670 | ETHNIC AND RACIAL STUDIES / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 0141-9870 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3671 | JOURNAL OF BIOLOGICAL EDUCATION / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 0021-9266 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3672 | COGNITION & EMOTION / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 0269-9931 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3673 | JOURNAL OF OCCUPATIONAL HEALTH / OXFORD UNIV PRESS | 1341-9145 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3674 | Archivos de Zootecnia UCOPress. Editorial Universi / Unknown | 1885-4494 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3675 | GENES TO CELLS / WILEY | 1356-9597 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3676 | JOURNAL OF HYDROMETEOROLOGY / AMER METEOROLOGICAL SOC | 1525-7541 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3677 | JOURNAL OF MUSCLE RESEARCH AND  CELL MOTILITY / SPRINGER | 0142-4319 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3678 | PALAEONTOLOGY / WILEY | 0031-0239 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3679 | EUROPEAN JOURNAL OF  INTERNATIONAL MANAGEMENT / INDERSCIENCE ENTERPRISES LTD | 1751-6757 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3680 | Journal of Patient Experience SAGE Publications In / Unknown | 2374-3735 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3681 | Issues in Accounting Education American Accounting / Unknown | 1558-7983 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3682 | VIRTUAL AND PHYSICAL PROTOTYPING / TAYLOR & FRANCIS LTD | 1745-2759 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3683 | JOURNAL OF GASTROINTESTINAL AND  LIVER DISEASES / MEDICAL UNIV PRESS | 1842-1121 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3684 | Behaviour Change Cambridge University Press / Unknown | 0813-4839 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3685 | RENEWABLE AGRICULTURE AND FOOD  SYSTEMS / CAMBRIDGE UNIV PRESS | 1742-1705 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3686 | Mekhatronika, Avtomatizatsiya, Upravlenie New Tech / Unknown | 2619-1253 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3687 | Annals of the Polish Association of Agricultural a / Unknown | 2657-7828 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3688 | Cooperativismo e Economia Social Faculty of Legal  / Unknown | 2660-6348 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3689 | Journal of Feminist Family Therapy Routledge / Unknown | 1540-4099 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3690 | BEN JONSON JOURNAL / EDINBURGH UNIV PRESS | 1079-3453 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3691 | Archivos de Prevencion Riesgos Laborales Academy o / Unknown | 1578-2549 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3692 | Journal of the Japan Epilepsy Society Japan Epilep / Unknown | 1347-5509 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3693 | INTERNATIONAL JOURNAL OF  HOUSING POLICY / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1949-1247 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3694 | INTERNATIONAL JOURNAL OF ORAL  SCIENCE / SPRINGERNATURE | 1674-2818 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3695 | Journal of High Speed Networks SAGE Publications L / Unknown | 0926-6801 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3696 | International Journal of Engineering Systems Model / Unknown | 1755-9758 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3697 | International Journal of Electronic Marketing and  / Unknown | 1741-1025 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3698 | Signo y Pensamiento Pontificia Universidad Javeria / Unknown | 2027-2731 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3699 | International Journal of Interdisciplinary Social  / N°   ISSN   E-ISSN   Studies | 2324-7584 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3700 | WSEAS Transactions on Power Systems World Scientif / Unknown | 1790-5060 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3701 | International Journal of Revenue Management Inders / Unknown | 1474-7332 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3702 | Plasma Physics and Technology Czech Technical Univ / Unknown | 2336-2634 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3703 | Hemato Multidisciplinary Digital Publishing Instit / Unknown | 2673-6357 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3704 | Journal of Verification, Validation and Uncertaint / Unknown | 2377-2166 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3705 | Fish and Shellfish Immunology Reports Elsevier Ltd / Unknown | 2667-0119 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3706 | Journal of Central Banking Law and Institutions Ba / Unknown | 2827-7775 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3707 | Engineering Geology and Hydrogeology Geological In / Unknown | 2738-6996 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3708 | CHEST / ELSEVIER | 0012-3692 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3709 | WATER SCIENCE AND TECHNOLOGY / IWA PUBLISHING | 0273-1223 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3710 | JOURNAL OF GEOLOGY / UNIV CHICAGO PRESS | 0022-1376 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3711 | CHEMICAL SOCIETY REVIEWS / ROYAL SOC CHEMISTRY | 0306-0012 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3712 | GENES & DEVELOPMENT / COLD SPRING HARBOR LAB PRESS,  PUBLICATI | 1549-5477 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3713 | CANCER IMMUNOLOGY RESEARCH / AMER ASSOC CANCER RESEARCH | 2326-6066 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3714 | TURKISH JOURNAL OF MEDICAL  SCIENCES / TUBITAK SCIENTIFIC &  TECHNOLOGICAL RESE | 1303-6165 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3715 | NEW ZEALAND JOURNAL OF BOTANY / TAYLOR & FRANCIS LTD | 0028-825X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3716 | HISTORY OF PHOTOGRAPHY / TAYLOR & FRANCIS LTD | 0308-7298 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3717 | MOLECULAR DIVERSITY / SPRINGER | 1381-1991 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3718 | JOURNAL OF ANIMAL AND PLANT  SCIENCES-JAPS / PAKISTAN AGRICULTURAL  SCIENTISTS FORUM | 2309-8694 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3719 | CAMBRIDGE QUARTERLY OF  HEALTHCARE ETHICS / CAMBRIDGE UNIV PRESS | 0963-1801 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3720 | TRANSACTIONS OF THE PHILOLOGICAL  SOCIETY / WILEY | 0079-1636 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3721 | JOURNAL OF FIELD ROBOTICS / WILEY | 1556-4959 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3722 | POETICS / ELSEVIER | 0304-422X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3723 | CZECH JOURNAL OF FOOD SCIENCES / CZECH ACADEMY AGRICULTURAL  SCIENCES | 1805-9317 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3724 | IEEE TRANSACTIONS ON EMERGING  TOPICS IN COMPUTATI / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 2471-285X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3725 | South African Journal of Physiotherapy AOSIS (Pty) / N°   ISSN   E-ISSN | 2410-8219 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3726 | PEDIATRIC OBESITY / WILEY | 2047-6302 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3727 | ALLERGY ASTHMA AND CLINICAL  IMMUNOLOGY / BMC | 1710-1492 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3728 | Arbitration International Oxford University Press / Unknown | 0957-0411 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3729 | JOURNAL OF RESEARCH IN CRIME AND  DELINQUENCY / SAGE PUBLICATIONS INC | 0022-4278 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3730 | Obrazovanie i Nauka Russian State Vocational Pedag / Unknown | 2310-5828 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3731 | JOURNAL DE THEORIE DES NOMBRES  DE BORDEAUX / UNIV BORDEAUX, INST  MATHEMATIQUES BORDE | 2118-8572 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3732 | JOURNAL OF MATHEMATICAL FLUID  MECHANICS / SPRINGER BASEL AG | 1422-6928 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3733 | RACE ETHNICITY AND EDUCATION / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1361-3324 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3734 | Revista Brasileira de Cineantropometria e Desempen / Unknown | 1980-0037 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3735 | JOURNAL OF APPLIED SPORT  PSYCHOLOGY / TAYLOR & FRANCIS LTD | 1041-3200 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3736 | HISTORY OF PSYCHOLOGY / EDUCATIONAL PUBLISHING  FOUNDATION-AMERI | 1093-4510 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3737 | PROGRESS IN PLANNING / PERGAMON-ELSEVIER SCIENCE LTD | 0305-9006 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3738 | Journal of Defense Modeling and Simulation SAGE Pu / Unknown | 1548-5129 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3739 | ACTA ORIENTALIA ACADEMIAE  SCIENTIARUM HUNGARICAE / AKADEMIAI KIADO ZRT | 0001-6446 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3740 | Studies in African Linguistics University of Flori / Unknown | 2154-428X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3741 | Gerontology and Geriatric Medicine SAGE Publicatio / Unknown | 2333-7214 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3742 | International Journal of Innovation Science Emeral / Unknown | 1757-2223 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3743 | Egyptian Journal of Ear, Nose, Throat and Allied S / Unknown | 2090-3405 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3744 | International Journal of Cloud Computing Inderscie / Unknown | 2043-9989 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3745 | Therapeutic Advances in Cardiovascular Disease SAG / Unknown | 1753-9447 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3746 | CLINICA Y SALUD / COLEGIO OFICIAL PSICOLOGOS  MADRID | 2174-0550 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3747 | Journal of Tropical Biodiversity and Biotechnology / Unknown | 2540-9581 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3748 | Information and Learning Science Emerald Publishin / Unknown | 2398-5348 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3749 | Archiwum Historii Filozofii i Mysli Spolecznej Wyd / Unknown | 2658-0438 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3750 | Pulmonary Therapy Adis / Unknown | 2364-1746 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3751 | Agriculture (Pol'nohospodarstvo) Sciendo / Unknown | 0551-3677 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3752 | Studies in Graduate and Postdoctoral Education Eme / Unknown | 2398-4686 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3753 | AMERICAN HISTORICAL REVIEW / OXFORD UNIV PRESS | 0002-8762 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3754 | EUROPEAN JOURNAL OF CANCER / ELSEVIER SCI LTD | 0959-8049 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3755 | ECOLOGY / WILEY | 0012-9658 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3756 | AMERICAN JOURNAL OF VETERINARY  RESEARCH / AMER VETERINARY MEDICAL ASSOC | 1943-5681 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3757 | BRITISH JOURNAL OF ORAL &  MAXILLOFACIAL SURGERY / CHURCHILL LIVINGSTONE | 1532-1940 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3758 | Eastern-European Journal of Enterprise Technologie / Unknown | 1729-4061 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3759 | HEALTH EDUCATION JOURNAL / SAGE PUBLICATIONS LTD | 0017-8969 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3760 | BRAIN AND BEHAVIOR / WILEY | 2162-3279 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3761 | JOURNAL OF GENERAL PSYCHOLOGY / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 0022-1309 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3762 | ARCHIVES OF INSECT BIOCHEMISTRY  AND PHYSIOLOGY / WILEY | 0739-4462 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3763 | Cogent Education Taylor and Francis Ltd. / Unknown | 2331-186X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3764 | NANO TODAY / ELSEVIER SCI LTD | 1748-0132 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3765 | MOLECULAR THERAPY NUCLEIC ACIDS / CELL PRESS | 2162-2531 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3766 | CHINA ECONOMIC REVIEW / ELSEVIER SCIENCE INC | 1043-951X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3767 | INTERNATIONAL JOURNAL OF  IMMUNOPATHOLOGY AND  PHA / SAGE PUBLICATIONS INC | 0394-6320 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3768 | JOURNALISM / SAGE PUBLICATIONS INC | 1464-8849 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3769 | CURRENT HYPERTENSION REPORTS / SPRINGER | 1522-6417 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3770 | SHIPS AND OFFSHORE STRUCTURES / TAYLOR & FRANCIS LTD | 1744-5302 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3771 | JOURNAL OF VETERINARY MEDICAL  EDUCATION / UNIV TORONTO PRESS INC | 0748-321X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3772 | DRUG DELIVERY AND TRANSLATIONAL  RESEARCH / SPRINGER HEIDELBERG | 2190-393X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3773 | SCOTTISH HISTORICAL REVIEW / EDINBURGH UNIV PRESS | 0036-9241 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3774 | Reflective Practice Taylor and Francis Ltd. / Unknown | 1462-3943 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3775 | Foresight Emerald Publishing / Unknown | 1463-6689 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3776 | International Journal of Information Technology an / Unknown | 2074-9007 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3777 | Applied Microscopy Springer Nature / Unknown | 2287-4445 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3778 | Journal of Herbs, Spices and Medicinal Plants Tayl / Unknown | 1049-6475 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3779 | GAMES AND CULTURE / SAGE PUBLICATIONS INC | 1555-4120 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3780 | Empiria Universidad Nacional de Educacion a Distan / Unknown | 2174-0682 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3781 | International Studies in Sociology of Education Ro / Unknown | 1747-5066 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3782 | ANTHROPOLOGICAL THEORY / SAGE PUBLICATIONS LTD | 1463-4996 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3783 | INTERNATIONAL JOURNAL OF CLINICAL  AND HEALTH PSYC / ELSEVIER SCIENCE INC | 1697-2600 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3784 | Speech, Language and Hearing Taylor and Francis Lt / Unknown | 2050-571X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3785 | Advances in Urology John Wiley and Sons Ltd / Unknown | 1687-6369 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3786 | Performance Measurement and Metrics Emerald Group  / Unknown | 1467-8047 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3787 | ACTA GEODAETICA ET GEOPHYSICA / SPRINGER | 2213-5812 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3788 | Studia z Filologii Polskiej i Slowianskiej Polish  / Unknown | 2392-2435 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3789 | ALGEBRAIC GEOMETRY / EUROPEAN MATHEMATICAL SOC- EMS | 2214-2584 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3790 | South Asian Diaspora Routledge / Unknown | 1943-8192 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3791 | Journal of Islamic Monetary Economics and Finance  / Unknown | 2460-6618 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3792 | Clinical and Experimental Morphology MDV Group / Unknown | 2686-6749 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3793 | Theatre and Performance Design Taylor and Francis  / Unknown | 2332-2551 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3794 | Music Theory And Analysis Leuven University Press / Unknown | 2295-5925 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3795 | JOURNAL OF EDUCATIONAL  PSYCHOLOGY / AMER PSYCHOLOGICAL ASSOC | 0022-0663 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3796 | ECONOMETRIC REVIEWS / TAYLOR & FRANCIS INC | 0747-4938 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3797 | THEORETICAL AND APPLIED FRACTURE  MECHANICS / ELSEVIER | 0167-8442 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3798 | CLINICAL AND EXPERIMENTAL  OPHTHALMOLOGY / WILEY | 1442-6404 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3799 | Intereconomics Sciendo / Unknown | 0020-5346 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3800 | SCANDINAVIAN JOURNAL OF  PSYCHOLOGY / WILEY | 0036-5564 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3801 | COMPUTER STANDARDS & INTERFACES / ELSEVIER | 0920-5489 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3802 | JOURNAL OF MEDICAL PRIMATOLOGY / WILEY | 0047-2565 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3803 | STRUCTURAL HEALTH MONITORING- AN INTERNATIONAL JOU / SAGE PUBLICATIONS LTD | 1475-9217 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3804 | MATHEMATICAL RESEARCH LETTERS / INT PRESS BOSTON, INC | 1945-001X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3805 | Politics and the Life Sciences Cambridge Universit / Unknown | 0730-9384 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3806 | Urology Practice Lippincott Williams and Wilkins / Unknown | 2352-0779 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3807 | STRUCTURAL CHANGE AND ECONOMIC  DYNAMICS / ELSEVIER | 0954-349X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3808 | ORGANIZATION / SAGE PUBLICATIONS LTD | 1350-5084 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3809 | IEEE Open Journal of the Communications Society In / Unknown | 2644-125X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3810 | AMERICAN BUSINESS LAW JOURNAL / WILEY | 0002-7766 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3811 | NEOPLASMA / AEPRESS SRO | 1338-4317 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3812 | Arid Zone Research Science Press / Unknown | 1001-4675 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3813 | AUSTRALIAN FEMINIST STUDIES / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 0816-4649 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3814 | Metallofizika i Noveishie Tekhnologii G.V. Kurdyum / N°   ISSN   E-ISSN | 2617-1511 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3815 | Journal of Medical Investigation University of Tok / N°   ISSN   E-ISSN | 1349-6867 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3816 | Russian Sociological Review National Research Univ / Unknown | 1728-1938 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3817 | Criminal Justice Policy Review SAGE Publications I / Unknown | 0887-4034 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3818 | JOURNAL OF TROPICAL FOREST  SCIENCE / FOREST RESEARCH INST MALAYSIA | 2521-9847 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3819 | Philologia Hispalensis Universidad de Sevilla / Unknown | 2253-8321 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3820 | Novosti Khirurgii Vitebsk State Medical University / Unknown | 2305-0047 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3821 | ADVANCED FIBER MATERIALS / SPRINGERNATURE | 2524-7921 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3822 | Analitika i Kontrol Ural Federal University / Unknown | 2073-1450 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3823 | Psychology of Consciousness: Theory Research, and  / Unknown | 2326-5523 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3824 | Journal of Eastern Mediterranean Archaeology and H / Unknown | 2166-3548 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3825 | INTERNATIONAL JOURNAL OF SYSTEMS  SCIENCE-OPERATIO / TAYLOR & FRANCIS LTD | 2330-2674 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3826 | JOURNAL OF THE ASABE / AMER SOC AGRICULTURAL &  BIOLOGICAL ENGI | 2769-3295 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3827 | Boletin de Arqueologia PUCP Pontificia Universidad / Unknown | 2304-4292 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3828 | Revista de Poetica Medieval Alcala University / Unknown | 2660-891X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3829 | Chinese Journal of Hematology Chinese Medical Jour / Unknown | 2707-9740 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3830 | European Oral Research Istanbul University Press / Unknown | 2651-2823 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3831 | Shodoznavstvo A. Yu. Krymskyi Institute of Orienta / Unknown | 2415-8712 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3832 | Journal of Food Quality and Hazards Control Shahid / Unknown | 2345-685X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3833 | Global Journal of Emerging Market Economies SAGE P / Unknown | 0974-9101 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3834 | Phenomics Springer / Unknown | 2730-583X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3835 | Revista de Teledeteccion Universidad Politecnica d / Unknown | 1988-8740 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3836 | Literaturna Misal Institute for Literature, Bulgar / Unknown | 1314-9237 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3837 | International Journal of Crashworthiness Taylor an / Unknown | 1573-8965 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3838 | EUROPEAN JOURNAL OF  ENDOCRINOLOGY / OXFORD UNIV PRESS | 0804-4643 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3839 | CHEMICAL PHYSICS / ELSEVIER | 0301-0104 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3840 | CHEMOTHERAPY / KARGER | 0009-3157 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3841 | CALCIFIED TISSUE INTERNATIONAL / SPRINGER | 0171-967X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3842 | AEU-INTERNATIONAL JOURNAL OF  ELECTRONICS AND COMM / ELSEVIER GMBH | 1434-8411 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3843 | SIGNAL PROCESSING-IMAGE  COMMUNICATION / ELSEVIER | 0923-5965 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3844 | PHYSIOLOGICAL RESEARCH / ACAD SCIENCES CZECH REPUBLIC,  INST PHYS | 0862-8408 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3845 | JOURNAL OF KNOT THEORY AND ITS  RAMIFICATIONS / WORLD SCIENTIFIC PUBL CO PTE  LTD | 0218-2165 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3846 | CHILD & YOUTH CARE FORUM / SPRINGER | 1053-1890 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3847 | Economic Research-Ekonomska Istrazivanja Taylor an / Unknown | 1331-677X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3848 | CHINESE GEOGRAPHICAL SCIENCE / SPRINGER | 1002-0063 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3849 | CHINA INFORMATION / SAGE PUBLICATIONS INC | 0920-203X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3850 | Journal of Clinical Ethics University of Chicago P / Unknown | 1046-7890 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3851 | Review of Black Political Economy Springer New Yor / N°   ISSN   E-ISSN | 0034-6446 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3852 | ATOMIC DATA AND NUCLEAR DATA  TABLES / ACADEMIC PRESS INC ELSEVIER  SCIENCE | 0092-640X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3853 | JOURNAL OF ENVIRONMENTAL LAW / OXFORD UNIV PRESS | 0952-8873 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3854 | INTERNATIONAL JOURNAL OF HIGH  PERFORMANCE COMPUTI / SAGE PUBLICATIONS LTD | 1094-3420 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3855 | Business and Professional Ethics Journal Philosoph / Unknown | 2153-7828 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3856 | ASSESSING WRITING / ELSEVIER SCI LTD | 1075-2935 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3857 | THERAPEUTIC ADVANCES IN  RESPIRATORY DISEASE / SAGE PUBLICATIONS LTD | 1753-4658 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3858 | STUDIA THEOLOGICA-CZECH REPUBLIC / UNIV PALACKEHO OLOMOUCI | 2570-9798 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3859 | APPLIED FRUIT SCIENCE / SPRINGER | 2948-2623 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3860 | Electronic Government Inderscience Enterprises Ltd / Unknown | 1740-7494 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3861 | Novos Estudos CEBRAP Centro Brasileiro de Analise  / Unknown | 1980-5403 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3862 | MARKETING THEORY / SAGE PUBLICATIONS INC | 1470-5931 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3863 | Acta Scientiarum Language and Culture Universidade / Unknown | 1983-4683 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3864 | Review of Law and Economics Walter de Gruyter GmbH / Unknown | 1555-5879 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3865 | International Journal of Vehicle Noise and Vibrati / Unknown | 1479-1471 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3866 | World Academy of Sciences Journal Spandidos Public / Unknown | 2632-2919 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3867 | Archivum Mathematicum Masarykova Universita / Unknown | 1212-5059 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3868 | Iranian Journal of Toxicology Arak University of M / Unknown | 2251-9459 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3869 | Biblica et Patristica Thoruniensia Uniwersytet Mik / Unknown | 2450-7059 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3870 | Fronteiras (Brazil) Federal University of Fronteir / Unknown | 2238-9717 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3871 | Futures and Foresight Science John Wiley and Sons  / Unknown | 2573-5152 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3872 | International Journal of Science, Mathematics and  / Unknown | 2327-915X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3873 | CHEMICAL PHYSICS REVIEWS / AIP PUBLISHING | 2688-4070 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3874 | International Journal of Accounting World Scientif / Unknown | 1094-4060 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3875 | Journal of Property, Planning and Environmental La / N°   ISSN   E-ISSN | 2514-9407 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3876 | European Food and Feed Law Review Lexxion / Unknown | 2190-8214 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3877 | JOURNAL OF PEDIATRIC  GASTROENTEROLOGY AND NUTRITI / WILEY | 0277-2116 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3878 | CLINICAL CANCER RESEARCH / AMER ASSOC CANCER RESEARCH | 1078-0432 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3879 | Measurement Techniques Springer Science and Busine / Unknown | 0543-1972 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3880 | Feddes Repertorium Wiley-Blackwell / Unknown | 0014-8962 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3881 | ART JOURNAL / TAYLOR & FRANCIS INC | 0004-3249 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3882 | ANTICANCER RESEARCH / INT INST ANTICANCER RESEARCH | 0250-7005 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3883 | JOURNAL OF MARRIAGE AND FAMILY / WILEY | 0022-2445 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3884 | TRANSLATIONAL CANCER RESEARCH / AME PUBLISHING COMPANY | 2218-676X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3885 | CANADIAN MATHEMATICAL BULLETIN- BULLETIN CANADIEN  / CAMBRIDGE UNIV PRESS | 0008-4395 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3886 | CHRONOBIOLOGY INTERNATIONAL / TAYLOR & FRANCIS INC | 0742-0528 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3887 | JOURNAL OF THROMBOSIS AND  THROMBOLYSIS / SPRINGER | 0929-5305 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3888 | JOURNAL OF PHOTOPOLYMER SCIENCE  AND TECHNOLOGY / TECHNICAL ASSOC  PHOTOPOLYMERS,JAPAN | 1349-6336 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3889 | DRONES / MDPI | 2504-446X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3890 | APIDOLOGIE / SPRINGER FRANCE | 0044-8435 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3891 | REVUE D ETUDES COMPARATIVES EST- OUEST / PRESSES UNIV FRANCE | 2259-6100 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3892 | SCIENCE & EDUCATION / SPRINGER | 0926-7220 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3893 | POLAR RESEARCH / OPEN ACADEMIA AB | 1751-8369 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3894 | ASTIN BULLETIN-THE JOURNAL OF THE  INTERNATIONAL A / CAMBRIDGE UNIV PRESS | 0515-0361 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3895 | JOURNAL OF INFORMETRICS / ELSEVIER | 1751-1577 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3896 | KIVA Routledge / Unknown | 2051-6177 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3897 | INTERNATIONAL JOURNAL OF MARINE  AND COASTAL LAW / MARTINUS NIJHOFF PUBL | 1571-8085 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3898 | JOURNAL OF AGRICULTURAL  BIOLOGICAL AND ENVIRONMEN / SPRINGER | 1085-7117 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3899 | Journal of Engineering, Design and Technology Emer / Unknown | 1726-0531 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3900 | REVIEWS OF ENVIRONMENTAL  CONTAMINATION AND TOXICO / SPRINGER | 0179-5953 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3901 | SCHOOL EFFECTIVENESS AND SCHOOL  IMPROVEMENT / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 0924-3453 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3902 | JOURNAL OF SERVICE RESEARCH / SAGE PUBLICATIONS INC | 1094-6705 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3903 | Indian Journal of Microbiology Research IP Innovat / Unknown | 2394-546X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3904 | CHINA FOUNDRY / SPRINGER SINGAPORE PTE LTD | 1672-6421 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3905 | Legal Theory Cambridge University Press / Unknown | 1352-3252 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3906 | INFORMATION TECHNOLOGY &  MANAGEMENT / SPRINGER | 1385-951X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3907 | International Journal of Christianity and Educatio / Unknown | 2056-9971 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3908 | INTERNATIONAL DATA PRIVACY LAW / OXFORD UNIV PRESS | 2044-3994 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3909 | Cybernetics and Physics Institute of Problems of M / Unknown | 2223-7038 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3910 | New Educator Taylor and Francis Ltd. / Unknown | 0250-6882 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3911 | HIV RESEARCH & CLINICAL PRACTICE / TAYLOR & FRANCIS LTD | 2578-7470 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3912 | Muslim World Journal of Human Rights Walter de Gru / Unknown | 1554-4419 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3913 | Opera Historica University of South Bohemia / Unknown | 2694-720X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3914 | Canadian Journal of Health History University of T / Unknown | 2816-6477 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3915 | Competition Policy International Competition Polic / Unknown | 1554-6853 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3916 | JOURNAL OF THE FRANKLIN INSTITUTE / PERGAMON-ELSEVIER SCIENCE LTD | 0016-0032 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3917 | School Science and Mathematics John Wiley & Sons I / Unknown | 0036-6803 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3918 | CANADIAN JOURNAL OF FISHERIES  AND AQUATIC SCIENCE / CANADIAN SCIENCE PUBLISHING | 0706-652X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3919 | MRS BULLETIN / SPRINGER HEIDELBERG | 0883-7694 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3920 | JOURNAL OF CHILD PSYCHOLOGY AND  PSYCHIATRY / WILEY | 0021-9630 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3921 | JOURNAL OF ETHNIC AND MIGRATION  STUDIES / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1369-183X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3922 | INTERNATIONAL JOURNAL OF URBAN  AND REGIONAL RESEA / WILEY | 0309-1317 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3923 | JOURNAL OF MOUNTAIN SCIENCE / SCIENCE PRESS | 1672-6316 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3924 | GEOGRAPHICAL RESEARCH / WILEY | 1745-5863 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3925 | REGIONAL SCIENCE AND URBAN  ECONOMICS / ELSEVIER | 0166-0462 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3926 | Journal of Theoretical and Applied Mechanics/Mecha / Unknown | 2543-6309 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3927 | Acta Agrobotanica Polish Botanical Society / Unknown | 2300-357X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3928 | Respirology Case Reports Wiley-Blackwell Publishin / Unknown | 2051-3380 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3929 | AUSTRALIAN JOURNAL OF PRIMARY  HEALTH / CSIRO PUBLISHING | 1448-7527 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3930 | POLISH JOURNAL OF FOOD AND  NUTRITION SCIENCES / INST ANIMAL REPRODUCTION &  FOOD RESEARC | 2083-6007 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3931 | Investigacion y Educacion en Enfermeria Facultad d / Unknown | 2216-0280 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3932 | POSITIVITY / SPRINGER | 1385-1292 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3933 | Combustion Engines Polish Scientific Society of Co / Unknown | 2658-1442 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3934 | Physical Oceanography Marine Hydrophysical Institu / Unknown | 1573-160X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3935 | JOURNAL OF BIOLOGICAL SYSTEMS / WORLD SCIENTIFIC PUBL CO PTE  LTD | 0218-3390 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3936 | SOUTH AFRICAN JOURNAL OF  INDUSTRIAL ENGINEERING / SOUTHERN AFRICAN INST  INDUSTRIAL ENGINE | 2224-7890 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3937 | Revista de Filologia de la Universidad de La Lagun / Unknown | 0212-4130 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3938 | BENEFICIAL MICROBES / BRILL | 1876-2883 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3939 | QUARTERLY REVIEWS OF BIOPHYSICS / CAMBRIDGE UNIV PRESS | 0033-5835 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3940 | AFTERALL / UNIV CHICAGO PRESS | 1465-4253 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3941 | Research in Post-Compulsory Education Routledge / Unknown | 1747-5112 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3942 | International Journal of Self-Propagating High-Tem / Unknown | 1061-3862 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3943 | GEMA Online Journal of Language Studies Penerbit U / Unknown | 2550-2131 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3944 | FOLIA BIOLOGICA / CHARLES UNIV PRAGUE, FIRST  FACULTY MEDI | 0015-5500 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3945 | Folia Biologica (Czech Republic) Charles Universit / Unknown | 2533-7602 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3946 | ANNUAL REVIEW OF APPLIED  LINGUISTICS / CAMBRIDGE UNIV PRESS | 0267-1905 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3947 | JOURNAL OF AMBIENT INTELLIGENCE  AND SMART ENVIRON / IOS PRESS | 1876-1364 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3948 | Gender Issues Springer New York / Unknown | 1098-092X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3949 | Unmanned Systems World Scientific / Unknown | 2301-3850 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3950 | Pacific Accounting Review Emerald Group Publishing / Unknown | 0114-0582 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3951 | Popular Communication Routledge / Unknown | 1540-5710 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3952 | JOURNAL OF RISK / INCISIVE MEDIA | 1755-2842 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3953 | REVISTA ROMANA DE MEDICINA DE  LABORATOR / SCIENDO | 1841-6624 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3954 | Archives of Mental Health Wolters Kluwer Medknow P / Unknown | 2589-9171 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3955 | Journal of Planning History SAGE Publications Inc. / Unknown | 1538-5132 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3956 | Art, Design and Communication in Higher Education  / Unknown | 2040-0896 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3957 | AMERICAN JOURNAL OF CULTURAL  SOCIOLOGY / PALGRAVE MACMILLAN LTD | 2049-7113 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3958 | Korean Language in America Penn State University P / Unknown | 2332-0346 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3959 | Alfred Nobel University Journal of Philology Alfre / Unknown | 3041-2188 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3960 | MAYO CLINIC PROCEEDINGS / ELSEVIER SCIENCE INC | 0025-6196 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3961 | JOURNAL OF THE OPERATIONAL  RESEARCH SOCIETY / TAYLOR & FRANCIS LTD | 0160-5682 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3962 | OBESITY SURGERY / SPRINGER | 0960-8923 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3963 | CRYSTAL RESEARCH AND TECHNOLOGY / WILEY-V C H VERLAG GMBH | 0232-1300 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3964 | EUROPEAN JOURNAL OF INTERNAL  MEDICINE / ELSEVIER | 0953-6205 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3965 | LINGUA / ELSEVIER | 0024-3841 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3966 | CRITICAL REVIEWS IN FOOD SCIENCE  AND NUTRITION / TAYLOR & FRANCIS INC | 1040-8398 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3967 | NEW ZEALAND VETERINARY JOURNAL / TAYLOR & FRANCIS LTD | 0048-0169 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3968 | COLD REGIONS SCIENCE AND  TECHNOLOGY / ELSEVIER | 0165-232X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3969 | CANADIAN GEOGRAPHIES- GEOGRAPHIES CANADIENNES / WILEY | 0008-3658 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3970 | FEMINIST REVIEW / SAGE PUBLICATIONS LTD | 0141-7789 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3971 | MELUS / OXFORD UNIV PRESS INC | 0163-755X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3972 | JOURNAL OF RELIGION IN AFRICA / BRILL | 0022-4200 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3973 | COMPREHENSIVE REVIEWS IN FOOD  SCIENCE AND FOOD SA / WILEY | 1541-4337 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3974 | JOURNAL OF HAPPINESS STUDIES / SPRINGER | 1389-4978 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3975 | American Journal of Lifestyle Medicine SAGE Public / Unknown | 1559-8276 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3976 | ECOSYSTEM SERVICES / ELSEVIER | 2212-0416 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3977 | Journal of Law and Religion Cambridge University P / Unknown | 0748-0814 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3978 | EUPHROSYNE-REVISTA DE FILOLOGIA  CLASSICA / BREPOLS PUBL | 2736-3082 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3979 | KOREAN JOURNAL OF PAIN / KOREAN PAIN SOC | 2093-0569 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3980 | DIACRITICS-A REVIEW OF  CONTEMPORARY CRITICISM / JOHNS HOPKINS UNIV PRESS | 1080-6539 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3981 | Revista de Salud Publica Universidad Nacional de C / Unknown | 2539-3596 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3982 | World Leisure Journal Taylor and Francis Ltd. / Unknown | 1607-8055 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3983 | Administrative Theory and Praxis Taylor and Franci / N°   ISSN   E-ISSN | 1084-1806 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3984 | International Journal of Cardiovascular Sciences S / Unknown | 2359-5647 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3985 | Folia Malacologica Association of Polish Malacolog / Unknown | 2300-7125 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3986 | Anaesthesia, Pain and Intensive Care Faculty of An / Unknown | 2220-5799 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3987 | PROCEEDINGS OF THE INSTITUTION OF  CIVIL ENGINEERS / EMERALD GROUP PUBLISHING LTD | 1741-7589 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3988 | ENVIRONMENTAL ARCHAEOLOGY / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1461-4103 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3989 | Pediatria i Medycyna Rodzinna / Unknown | 2451-0742 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3990 | DIFFERENCES-A JOURNAL OF FEMINIST  CULTURAL STUDIE / DUKE UNIV PRESS | 1040-7391 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3991 | EVOLVING SYSTEMS / SPRINGER HEIDELBERG | 1868-6478 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3992 | Kemas Universitas Negeri Semarang / N°   ISSN   E-ISSN | 2355-3596 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3993 | Cell Genomics Cell Press / Unknown | 2666-979X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3994 | International Journal of Knowledge Management Stud / Unknown | 1743-8268 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3995 | Studia Poliana / Unknown | 2386-8872 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3996 | Anesthesiology Research and Practice John Wiley an / Unknown | 1687-6962 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3997 | AMS Review Springer New York / N°   ISSN   E-ISSN | 1869-814X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3998 | JOURNAL OF COMPUTER LANGUAGES / ELSEVIER SCI LTD | 2590-1184 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 3999 | Frontiers in Systems Biology Frontiers Media SA / Unknown | 2674-0702 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4000 | Rehabilitace a Fyzikalni Lekarstvi Czech Medical A / Unknown | 1805-4552 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4001 | INTERNATIONAL JOURNAL OF  RADIATION ONCOLOGY BIOLO / ELSEVIER SCIENCE INC | 1879-355X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4002 | JOURNAL OF IMMUNOLOGICAL  METHODS / ELSEVIER | 1872-7905 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4003 | EMERGENCY MEDICINE CLINICS OF  NORTH AMERICA / W B SAUNDERS CO-ELSEVIER INC | 1558-0539 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4004 | Family Court Review John Wiley & Sons Inc. / Unknown | 1744-1617 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4005 | DEMOCRATIZATION / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1743-890X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4006 | LEADERSHIP & ORGANIZATION  DEVELOPMENT JOURNAL / EMERALD GROUP PUBLISHING LTD | 1472-5347 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4007 | AUSTRALIAN ARCHAEOLOGY / TAYLOR & FRANCIS LTD | 2470-0363 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4008 | CLINICAL TRIALS / SAGE PUBLICATIONS LTD | 1740-7753 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4009 | CLIMATE POLICY / TAYLOR & FRANCIS LTD | 1752-7457 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4010 | AQUACULTURAL ENGINEERING / ELSEVIER SCI LTD | 1873-5614 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4011 | INTERNATIONAL JOURNAL OF HUMAN  RIGHTS / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1744-053X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4012 | CHILD NEUROPSYCHOLOGY / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1744-4136 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4013 | Journal for Nurses in Professional Development Lip / Unknown | 2169-981X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4014 | South African Journal of Clinical Nutrition Taylor / Unknown | 2221-1268 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4015 | HIGH POWER LASER SCIENCE AND  ENGINEERING / CAMBRIDGE UNIV PRESS | 2095-4719 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4016 | FUNGAL DIVERSITY / SPRINGER | 1878-9129 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4017 | JOURNAL OF INVESTIGATIVE  PSYCHOLOGY AND OFFENDER  / WILEY | 1544-4767 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4018 | EUROPEAN REVIEW OF SOCIAL  PSYCHOLOGY / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1479-277X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4019 | Journal of The Institution of Engineers (India): S / Unknown | 2250-2491 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4020 | International Journal of Electronic Commerce Studi / N°   ISSN   E-ISSN | 2410-8588 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4021 | International Journal of Comparative Education and / Unknown | 2396-7404 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4022 | NEUROLOGY / LIPPINCOTT WILLIAMS & WILKINS | 1526-632X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4023 | CHEMIE INGENIEUR TECHNIK / WILEY-V C H VERLAG GMBH | 1522-2640 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4024 | INTERNATIONAL JOURNAL OF  SYSTEMATIC AND EVOLUTION / MICROBIOLOGY SOC | 1466-5034 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4025 | AMERICAN JOURNAL OF MEDICAL  GENETICS PART A / WILEY | 1552-4833 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4026 | NUCLEAR SCIENCE AND ENGINEERING / TAYLOR & FRANCIS INC | 1943-748X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4027 | PROCEEDINGS OF THE INSTITUTION OF  MECHANICAL ENGI / SAGE PUBLICATIONS LTD | 2041-305X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4028 | PERIODICA MATHEMATICA  HUNGARICA / SPRINGER | 1588-2829 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4029 | International Journal of Operational Research Inde / Unknown | 1745-7653 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4030 | JOURNAL OF RISK RESEARCH / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1466-4461 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4031 | JOURNAL OF FAMILY THERAPY / WILEY | 1467-6427 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4032 | Journal of Control, Automation and Electrical Syst / Unknown | 2195-3899 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4033 | COLLECTANEA MATHEMATICA / SPRINGER-VERLAG ITALIA SRL | 2038-4815 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4034 | JOURNAL OF EXPERIMENTAL ZOOLOGY  PART A-ECOLOGICAL / WILEY | 2471-5646 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4035 | DEVELOPING WORLD BIOETHICS / WILEY | 1471-8847 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4036 | JOURNAL OF HYMENOPTERA  RESEARCH / PENSOFT PUBLISHERS | 1314-2607 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4037 | Journal of Echocardiography Springer Japan / Unknown | 1880-344X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4038 | EUROPEAN JOURNAL OF INDUSTRIAL  RELATIONS / SAGE PUBLICATIONS LTD | 1461-7129 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4039 | Journal of Entrepreneurship in Emerging Economies  / Unknown | 2053-4612 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4040 | LANGUAGE LEARNING AND  DEVELOPMENT / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1547-5441 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4041 | Integrative and Complementary Therapies Mary Ann L / Unknown | 2768-3206 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4042 | Advances in Operations Research John Wiley and Son / Unknown | 1687-9155 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4043 | Review of Evolutionary Political Economy Springer  / Unknown | 2662-6144 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4044 | Meteorologica Centro Argentino de Meteorologos / Unknown | 1850-468X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4045 | GASTROENTEROLOGY / W B SAUNDERS CO-ELSEVIER INC | 1528-0012 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4046 | PERCEPTUAL AND MOTOR SKILLS / SAGE PUBLICATIONS INC | 1558-688X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4047 | OPHTHALMOLOGY / ELSEVIER SCIENCE INC | 1549-4713 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4048 | JOURNAL OF MEDICAL VIROLOGY / WILEY | 1096-9071 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4049 | CHILDREN AND YOUTH SERVICES  REVIEW / PERGAMON-ELSEVIER SCIENCE LTD | 1873-7765 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4050 | JOURNAL OF ARID ENVIRONMENTS / ACADEMIC PRESS LTD- ELSEVIER  SCIENCE LT | 1095-922X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4051 | GeoJournal Springer Science and Business Media Deu / Unknown | 1572-9893 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4052 | BOUNDARY-LAYER METEOROLOGY / SPRINGER | 1573-1472 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4053 | NMR IN BIOMEDICINE / WILEY | 1099-1492 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4054 | HUMAN & EXPERIMENTAL  TOXICOLOGY / SAGE PUBLICATIONS LTD | 1477-0903 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4055 | JOURNAL OF SOIL AND WATER  CONSERVATION / TAYLOR & FRANCIS LTD | 1941-3300 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4056 | INDIAN JOURNAL OF ORTHOPAEDICS / SPRINGER HEIDELBERG | 1998-3727 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4057 | INTERNATIONAL JOURNAL OF NUMBER  THEORY / WORLD SCIENTIFIC PUBL CO PTE  LTD | 1793-7310 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4058 | BREASTFEEDING MEDICINE / MARY ANN LIEBERT, INC | 1556-8342 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4059 | REVIEWS IN MEDICAL VIROLOGY / WILEY | 1099-1654 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4060 | Scientia Sinica Mathematica Science Press / Unknown | 2095-9427 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4061 | INTERNATIONAL JOURNAL OF  CIRCUMPOLAR HEALTH / TAYLOR & FRANCIS LTD | 2242-3982 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4062 | JOURNAL OF REAL-TIME IMAGE  PROCESSING / SPRINGER HEIDELBERG | 1861-8219 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4063 | CRITICAL REVIEWS IN ANALYTICAL  CHEMISTRY / TAYLOR & FRANCIS INC | 1547-6510 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4064 | DATA MINING AND KNOWLEDGE  DISCOVERY / SPRINGER | 1573-756X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4065 | NATURAL RESOURCE MODELING / WILEY | 1939-7445 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4066 | CURRENT COMPUTER-AIDED DRUG  DESIGN / BENTHAM SCIENCE PUBL LTD | 1875-6697 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4067 | SCHOOL PSYCHOLOGY / EDUCATIONAL PUBLISHING  FOUNDATION-AMERI | 2578-4226 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4068 | MEDICINA DELLO SPORT / EDIZIONI MINERVA MEDICA | 1827-1863 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4069 | ADVANCES IN ASTRONOMY / WILEY | 1687-7977 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4070 | Economic History of Developing Regions Taylor and  / Unknown | 2078-0397 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4071 | International Journal of Chinese Linguistics John  / Unknown | 2213-8714 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4072 | CROP SCIENCE / WILEY | 1435-0653 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4073 | ATMOSPHERIC ENVIRONMENT / PERGAMON-ELSEVIER SCIENCE LTD | 1873-2844 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4074 | INTERNATIONAL RELATIONS / SAGE PUBLICATIONS LTD | 1741-2862 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4075 | EUROPEAN JOURNAL OF FOREST  RESEARCH / SPRINGER | 1612-4677 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4076 | JOURNAL OF BIOMATERIALS SCIENCE- POLYMER EDITION / TAYLOR & FRANCIS LTD | 1568-5624 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4077 | OCEAN DYNAMICS / SPRINGER HEIDELBERG | 1616-7341 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4078 | NUCLEAR DATA SHEETS / ACADEMIC PRESS INC ELSEVIER  SCIENCE | 1095-9904 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4079 | INTERNATIONAL JOURNAL OF  COMPUTER INTEGRATED  MAN / TAYLOR & FRANCIS LTD | 1362-3052 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4080 | JOURNAL OF SOUTHERN AFRICAN  STUDIES / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1465-3893 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4081 | Strabismus Taylor and Francis Ltd. / Unknown | 1744-5132 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4082 | IRAN-JOURNAL OF THE BRITISH  INSTITUTE OF PERSIAN  / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 2396-9202 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4083 | OPEN HOUSE INTERNATIONAL- SUSTAINABLE & SMART ARCH / EMERALD GROUP PUBLISHING LTD | 2633-9838 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4084 | Medicinal Plants - International Journal of Phytom / Unknown | 0975-6892 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4085 | JOURNAL OF DESTINATION  MARKETING & MANAGEMENT / ELSEVIER | 2212-5752 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4086 | Journal of Historical Research in Marketing Emeral / Unknown | 1755-7518 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4087 | ACOUSTICS AUSTRALIA / SPRINGER SINGAPORE PTE LTD | 1839-2571 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4088 | International Journal of Noncommunicable Diseases  / Unknown | 2468-8835 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4089 | HONG KONG JOURNAL OF  OCCUPATIONAL THERAPY / SAGE PUBLICATIONS LTD | 1876-4398 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4090 | JOURNAL OF MATHEMATICS AND  MUSIC / TAYLOR & FRANCIS LTD | 1745-9745 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4091 | Chinese Journal of Academic Radiology Springer / Unknown | 2520-8993 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4092 | Study Abroad Research in Second Language Acquisiti / Unknown | 2405-5530 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4093 | JOURNAL OF MATERIALS ENGINEERING  AND PERFORMANCE / SPRINGER | 1544-1024 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4094 | IEEE JOURNAL OF SELECTED TOPICS IN  APPLIED EARTH  / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 2151-1535 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4095 | PANCREATOLOGY / ELSEVIER | 1424-3911 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4096 | ACTAS UROLOGICAS ESPANOLAS / ELSEVIER ESPANA | 1699-7980 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4097 | DEVELOPMENT GROWTH &  DIFFERENTIATION / WILEY | 1440-169X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4098 | STATISTICAL METHODS IN MEDICAL  RESEARCH / SAGE PUBLICATIONS LTD | 1477-0334 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4099 | AQUACULTURE NUTRITION / WILEY | 1365-2095 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4100 | Enfermeria Clinica Elsevier Espana S.L.U / Unknown | 1579-2013 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4101 | CIRCULATION-ARRHYTHMIA AND  ELECTROPHYSIOLOGY / LIPPINCOTT WILLIAMS & WILKINS | 1941-3149 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4102 | JOURNAL OF EDUCATIONAL  ADMINISTRATION / EMERALD GROUP PUBLISHING LTD | 1758-7395 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4103 | ZEITSCHRIFT FUR ASSYRIOLOGIE UND  VORDERASIATISCHE / WALTER DE GRUYTER GMBH | 1613-1150 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4104 | Journal of Financial Crime Emerald Group Publishin / Unknown | 1758-7239 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4105 | JOURNAL OF AGING STUDIES / ELSEVIER SCIENCE INC | 1879-193X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4106 | SEXUALITY RESEARCH AND SOCIAL  POLICY / SPRINGER | 1868-9884 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4107 | INTERNATIONAL JOURNAL OF SPORT  NUTRITION AND EXER / HUMAN KINETICS PUBL INC | 1543-2742 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4108 | Twentieth Century British History Oxford Universit / Unknown | 1477-4674 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4109 | Journal of Health Management Sage Publications Ind / Unknown | 0973-0729 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4110 | MULTIDIMENSIONAL SYSTEMS AND  SIGNAL PROCESSING / SPRINGER | 1573-0824 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4111 | AUSTRALIAN SYSTEMATIC BOTANY / CSIRO PUBLISHING | 1446-5701 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4112 | COMMUNITY ECOLOGY / SPRINGER HEIDELBERG | 1588-2756 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4113 | COMPARATIVE EUROPEAN POLITICS / PALGRAVE MACMILLAN LTD | 1740-388X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4114 | Environmental Processes Springer Science and Busin / Unknown | 2198-7505 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4115 | Asian Review of Accounting Emerald Group Publishin / Unknown | 1758-8863 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4116 | International Journal of Reconfigurable and Embedd / Unknown | 2722-2608 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4117 | HOME CULTURES / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1751-7427 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4118 | Bridge Structures SAGE Publications Ltd / Unknown | 1744-8999 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4119 | GEOGRAPHICAL JOURNAL / WILEY | 1475-4959 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4120 | JOURNAL OF BONE AND MINERAL  RESEARCH / OXFORD UNIV PRESS | 1523-4681 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4121 | PRAKTISCHE METALLOGRAPHIE- PRACTICAL METALLOGRAPHY / WALTER DE GRUYTER GMBH | 2195-8599 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4122 | BRITISH JOURNAL OF EDUCATIONAL  PSYCHOLOGY / WILEY | 2044-8279 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4123 | MINERALIUM DEPOSITA / SPRINGER | 1432-1866 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4124 | Art Documentation University of Chicago Press / Unknown | 2161-9417 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4125 | LANGUAGE SCIENCES / ELSEVIER SCI LTD | 1873-5746 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4126 | SOUTH AFRICAN JOURNAL OF  PSYCHOLOGY / SAGE PUBLICATIONS LTD | 2078-208X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4127 | JOURNAL OF HEALTH POPULATION  AND NUTRITION / BMC | 2072-1315 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4128 | JOURNAL OF CHILDRENS  ORTHOPAEDICS / SAGE PUBLICATIONS INC | 1863-2548 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4129 | Reading Psychology Taylor and Francis Ltd. / Unknown | 1521-0685 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4130 | INTERNATIONAL JOURNAL OF LAW IN  CONTEXT / CAMBRIDGE UNIV PRESS | 1744-5531 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4131 | LOGOPEDICS PHONIATRICS VOCOLOGY / TAYLOR & FRANCIS LTD | 1651-2022 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4132 | STOCHASTIC MODELS / TAYLOR & FRANCIS INC | 1532-6349 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4133 | International Journal of Technology, Policy and Ma / Unknown | 1741-5292 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4134 | JOURNAL OF SPECTRAL THEORY / EUROPEAN MATHEMATICAL SOC- EMS | 1664-0403 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4135 | Journal of Patient Safety and Risk Management SAGE / Unknown | 2516-0443 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4136 | Journal of European Tort Law Walter de Gruyter Gmb / Unknown | 1868-9620 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4137 | THROMBOSIS RESEARCH / PERGAMON-ELSEVIER SCIENCE LTD | 1879-2472 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4138 | BRAIN STIMULATION / ELSEVIER SCIENCE INC | 1935-861X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4139 | BULLETIN DU CANCER / ELSEVIER MASSON, CORPORATION  OFFICE | 1769-6917 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4140 | INTERNATIONAL JOURNAL OF APPLIED  CERAMIC TECHNOLO / WILEY | 1744-7402 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4141 | ERKENNTNIS / SPRINGER | 1572-8420 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4142 | RESEARCH IN NURSING & HEALTH / WILEY | 1098-240X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4143 | CLINICS IN PERINATOLOGY / W B SAUNDERS CO-ELSEVIER INC | 1557-9840 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4144 | INTERNATIONAL JOURNAL OF  COSMETIC SCIENCE / WILEY | 1468-2494 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4145 | GIFTED CHILD QUARTERLY / SAGE PUBLICATIONS INC | 1934-9041 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4146 | ACM SIGCOMM COMPUTER  COMMUNICATION REVIEW / ASSOC COMPUTING MACHINERY | 1943-5819 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4147 | SLAS DISCOVERY / ELSEVIER SCIENCE INC | 2472-5560 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4148 | International Studies Sage Publications India Pvt. / Unknown | 0973-0702 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4149 | EDUCATIONAL PSYCHOLOGIST / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1532-6985 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4150 | Journal of Chiropractic Medicine Elsevier Inc. / Unknown | 1556-3715 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4151 | SHAW-THE JOURNAL OF BERNARD  SHAW STUDIES / PENN STATE UNIV PRESS | 1529-1480 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4152 | Journal of Small Business and Entrepreneurship Tay / N°   ISSN   E-ISSN | 2169-2610 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4153 | History of Economics Review Informa:  Taylor & Fra / Unknown | 1838-6318 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4154 | Veterinary Medicine International John Wiley and S / Unknown | 2090-8113 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4155 | Pratique Neurologique - FMC Elsevier Masson s.r.l. / Unknown | 1878-7770 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4156 | TRAINING AND EDUCATION IN  PROFESSIONAL PSYCHOLOGY / EDUCATIONAL PUBLISHING  FOUNDATION-AMERI | 1931-3926 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4157 | GEOTECTONICS / PLEIADES PUBLISHING INC | 1556-1976 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4158 | International Journal of Security and Networks Ind / Unknown | 1747-8413 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4159 | Society and Business Review Emerald Group Publishi / Unknown | 1746-5699 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4160 | IET Networks John Wiley & Sons Inc. / Unknown | 2047-4962 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4161 | Journal for the Study of the Pseudepigrapha SAGE P / Unknown | 1745-5286 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4162 | HEALTH PSYCHOLOGY REVIEW / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1743-7202 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4163 | CLASSICAL REVIEW / CAMBRIDGE UNIV PRESS | 1464-3561 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4164 | JOURNAL OF NEUROLOGICAL SURGERY  PART B-SKULL BASE / THIEME MEDICAL PUBL INC | 2193-634X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4165 | CONCURRENCY AND COMPUTATION- PRACTICE & EXPERIENCE / WILEY | 1532-0634 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4166 | IEEE TRANSACTIONS ON CYBERNETICS / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 2168-2275 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4167 | JOURNAL OF NURSING EDUCATION / SLACK INC | 1938-2421 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4168 | CELL TRANSPLANTATION / SAGE PUBLICATIONS INC | 1555-3892 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4169 | GLYCOBIOLOGY / OXFORD UNIV PRESS INC | 1460-2423 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4170 | JOURNALS OF GERONTOLOGY SERIES  B-PSYCHOLOGICAL SC / OXFORD UNIV PRESS INC | 1758-5368 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4171 | RESEARCH IN SOCIAL &  ADMINISTRATIVE PHARMACY / ELSEVIER SCIENCE INC | 1934-8150 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4172 | NANOMEDICINE / TAYLOR & FRANCIS LTD | 1748-6963 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4173 | GLOBAL ECOLOGY AND  BIOGEOGRAPHY / WILEY | 1466-8238 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4174 | VETERINARY ANAESTHESIA AND  ANALGESIA / ELSEVIER | 1467-2995 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4175 | COUNSELING PSYCHOLOGIST / SAGE PUBLICATIONS INC | 1552-3861 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4176 | MINERALOGY AND PETROLOGY / SPRINGER WIEN | 1438-1168 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4177 | Physics of Particles and Nuclei Letters Pleiades P / Unknown | 1547-4771 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4178 | JOURNAL OF AUSTRALIAN STUDIES / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1835-6419 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4179 | LIBRI-INTERNATIONAL JOURNAL OF  LIBRARIES AND INFO / WALTER DE GRUYTER GMBH | 1865-8423 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4180 | MECHANICS BASED DESIGN OF  STRUCTURES AND MACHINES / TAYLOR & FRANCIS INC | 1539-7742 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4181 | EUROPEAN JOURNAL OF CELL BIOLOGY / ELSEVIER GMBH | 1618-1298 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4182 | ARCHIVES OF WOMENS MENTAL  HEALTH / SPRINGER WIEN | 1435-1102 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4183 | QUEUEING SYSTEMS / SPRINGER | 1572-9443 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4184 | LIMNOLOGICA / ELSEVIER GMBH | 1873-5851 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4185 | KI - Kunstliche Intelligenz Springer International / Unknown | 1610-1987 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4186 | ARABIC SCIENCES AND PHILOSOPHY / CAMBRIDGE UNIV PRESS | 1474-0524 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4187 | JOURNAL ON MULTIMODAL USER  INTERFACES / SPRINGER | 1783-8738 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4188 | JOURNAL OF ELECTRONIC MATERIALS / SPRINGER | 1543-186X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4189 | PEPTIDES / ELSEVIER SCIENCE INC | 1873-5169 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4190 | JOURNAL OF CRITICAL CARE / W B SAUNDERS CO-ELSEVIER INC | 1557-8615 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4191 | BIOSYSTEMS ENGINEERING / ACADEMIC PRESS INC ELSEVIER  SCIENCE | 1537-5129 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4192 | CURRENT OPINION IN CARDIOLOGY / LIPPINCOTT WILLIAMS & WILKINS | 1531-7080 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4193 | JOURNAL OF CONSUMER RESEARCH / OXFORD UNIV PRESS INC | 1537-5277 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4194 | BULLETIN OF THE INSTITUTE OF  CLASSICAL STUDIES / OXFORD UNIV PRESS | 2041-5370 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4195 | NEUROCIRUGIA / ELSEVIER ESPANA SLU | 2340-6305 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4196 | ANNALS OF DIAGNOSTIC PATHOLOGY / ELSEVIER SCIENCE INC | 1532-8198 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4197 | ACTA ZOOLOGICA / WILEY | 1463-6395 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4198 | MINERVA / SPRINGER | 1573-1871 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4199 | PROGRESS IN POLYMER SCIENCE / PERGAMON-ELSEVIER SCIENCE LTD | 1873-1619 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4200 | Oral and Maxillofacial Surgery Springer Verlag / Unknown | 1865-1569 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4201 | INSTRUCTIONAL SCIENCE / SPRINGER | 1573-1952 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4202 | SINGAPORE JOURNAL OF TROPICAL  GEOGRAPHY / WILEY | 1467-9493 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4203 | BEHAVIOURAL NEUROLOGY / WILEY | 1875-8584 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4204 | HAU-JOURNAL OF ETHNOGRAPHIC  THEORY / UNIV CHICAGO PRESS | 2575-1433 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4205 | JOURNAL OF OCCUPATIONAL HEALTH  PSYCHOLOGY / EDUCATIONAL PUBLISHING  FOUNDATION-AMERI | 1939-1307 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4206 | JOURNAL OF AGRARIAN CHANGE / WILEY | 1471-0366 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4207 | Journal of Cross-Cultural Gerontology Springer New / Unknown | 1573-0719 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4208 | Journal of Pediatric Rehabilitation Medicine SAGE  / Unknown | 1875-8894 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4209 | JOURNAL OF MATHEMATICS TEACHER  EDUCATION / SPRINGER | 1573-1820 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4210 | HUMAN PERFORMANCE / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1532-7043 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4211 | INFORMATION SYSTEMS AND E- BUSINESS MANAGEMENT / SPRINGER HEIDELBERG | 1617-9854 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4212 | International Journal of Agile Systems and Managem / Unknown | 1741-9182 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4213 | International Journal of Space Science and Enginee / Unknown | 2048-8467 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4214 | JOURNAL OF FORENSIC SCIENCES / WILEY | 1556-4029 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4215 | BIOLOGICAL TRACE ELEMENT  RESEARCH / SPRINGERNATURE | 1559-0720 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4216 | GEOTECHNIQUE / EMERALD GROUP PUBLISHING LTD | 1751-7656 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4217 | JOURNAL OF AMERICAN COLLEGE  HEALTH / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1940-3208 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4218 | Uniform Law Review Oxford University Press / Unknown | 2050-9065 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4219 | JOURNAL OF ANALYTICAL METHODS IN  CHEMISTRY / WILEY | 2090-8873 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4220 | STUDIES IN CHRISTIAN ETHICS / SAGE PUBLICATIONS LTD | 1745-5235 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4221 | JOURNAL OF ENGINEERING DESIGN / TAYLOR & FRANCIS LTD | 1466-1837 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4222 | ASIA PACIFIC BUSINESS REVIEW / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1743-792X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4223 | STYLE / PENN STATE UNIV PRESS | 2374-6629 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4224 | AQUATIC INSECTS / TAYLOR & FRANCIS LTD | 1744-4152 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4225 | PERIODONTOLOGY 2000 / WILEY | 1600-0757 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4226 | MANAGEMENT AND ORGANIZATION  REVIEW / CAMBRIDGE UNIV PRESS | 1740-8784 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4227 | ITALIAN JOURNAL OF DERMATOLOGY  AND VENEREOLOGY / EDIZIONI MINERVA MEDICA | 2784-8671 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4228 | EURASIAN GEOGRAPHY AND  ECONOMICS / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1938-2863 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4229 | BRIEFINGS IN FUNCTIONAL GENOMICS / OXFORD UNIV PRESS | 2041-2657 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4230 | BRITISH POLITICS / PALGRAVE MACMILLAN LTD | 1746-9198 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4231 | Mathematische Semesterberichte Springer Verlag / Unknown | 1432-1815 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4232 | Chemistry, Didactics, Ecology, Metrology Sciendo / Unknown | 2084-4506 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4233 | Current Gerontology and Geriatrics Research John W / Unknown | 1687-7071 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4234 | Fatigue of Aircraft Structures De Gruyter Open Ltd / Unknown | 2300-7591 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4235 | EUROPEAN JOURNAL OF CLINICAL  INVESTIGATION / WILEY | 1365-2362 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4236 | FITOTERAPIA / ELSEVIER | 1873-6971 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4237 | CELL PROLIFERATION / WILEY | 1365-2184 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4238 | AQUATIC BOTANY / ELSEVIER | 1879-1522 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4239 | CONTEMPORARY PHYSICS / TAYLOR & FRANCIS LTD | 1366-5812 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4240 | JOURNAL OF COMPARATIVE  PHYSIOLOGY B-BIOCHEMICAL S / SPRINGER HEIDELBERG | 1432-136X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4241 | JOURNAL OF IMMIGRANT AND  MINORITY HEALTH / SPRINGER | 1557-1920 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4242 | WATER RESOURCES / MAIK  NAUKA/INTERPERIODICA/SPRINGER | 1608-344X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4243 | SCOTTISH JOURNAL OF POLITICAL  ECONOMY / WILEY | 1467-9485 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4244 | SYSTEMATIC ENTOMOLOGY / WILEY | 1365-3113 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4245 | Asian Journal of Civil Engineering Springer Nature / Unknown | 2522-011X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4246 | SPORTS HEALTH-A MULTIDISCIPLINARY  APPROACH / SAGE PUBLICATIONS INC | 1941-7381 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4247 | WETLANDS ECOLOGY AND  MANAGEMENT / SPRINGER | 1572-9834 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4248 | AFRICAN DEVELOPMENT REVIEW- REVUE AFRICAINE DE DEV / WILEY | 1467-8268 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4249 | International Journal of Continuing Engineering Ed / Unknown | 1741-5055 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4250 | JOURNAL OF ARABIC LITERATURE / BRILL | 1570-064X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4251 | International Journal of Biometrics Inderscience E / Unknown | 1755-831X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4252 | Competition and Regulation in Network Industries S / Unknown | 2399-2956 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4253 | ANNUAL REVIEW OF ANALYTICAL  CHEMISTRY / ANNUAL REVIEWS | 1936-1335 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4254 | International Journal of Fluid Mechanics Research  / Unknown | 2152-5110 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4255 | ANNUAL REVIEW OF ORGANIZATIONAL  PSYCHOLOGY AND OR / ANNUAL REVIEWS | 2327-0616 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4256 | Journal of Second Language Studies John Benjamins  / Unknown | 2542-3843 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4257 | JOURNAL OF ANTIBIOTICS / SPRINGERNATURE | 1881-1469 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4258 | IMMUNOLOGY AND CELL BIOLOGY / WILEY | 1440-1711 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4259 | NEUROGASTROENTEROLOGY AND  MOTILITY / WILEY | 1365-2982 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4260 | JOURNAL OF HISTOTECHNOLOGY / TAYLOR & FRANCIS LTD | 2046-0236 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4261 | INTEGRATION-THE VLSI JOURNAL / ELSEVIER | 1872-7522 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4262 | INTERNATIONAL JOURNAL OF  PHYTOREMEDIATION / TAYLOR & FRANCIS INC | 1549-7879 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4263 | IEEE-CAA JOURNAL OF AUTOMATICA  SINICA / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 2329-9274 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4264 | ENVIRONMENT AND URBANIZATION / SAGE PUBLICATIONS LTD | 1746-0301 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4265 | EVOLUTIONARY ANTHROPOLOGY / WILEY | 1520-6505 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4266 | JOURNAL OF WORLD BUSINESS / ELSEVIER SCIENCE INC | 1878-5573 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4267 | JOURNAL OF VETERINARY DENTISTRY / SAGE PUBLICATIONS INC | 2470-4083 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4268 | HISTORY OF SCIENCE / SAGE PUBLICATIONS LTD | 1753-8564 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4269 | FRONTIERS IN  NEUROENDOCRINOLOGY / ACADEMIC PRESS INC ELSEVIER  SCIENCE | 1095-6808 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4270 | Human Affairs Walter de Gruyter GmbH / Unknown | 1337-401X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4271 | CURRENT GENE THERAPY / BENTHAM SCIENCE PUBL LTD | 1875-5631 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4272 | CHILDHOOD-A GLOBAL JOURNAL OF  CHILD RESEARCH / SAGE PUBLICATIONS LTD | 1461-7013 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4273 | FEMINIST THEOLOGY / SAGE PUBLICATIONS LTD | 1745-5189 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4274 | JOURNAL OF INNATE IMMUNITY / KARGER | 1662-8128 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4275 | Renaissance Drama University of Chicago Press / Unknown | 2164-3415 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4276 | AMERICAN JOURNAL OF PHYSICAL  MEDICINE & REHABILIT / LIPPINCOTT WILLIAMS & WILKINS | 1537-7385 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4277 | POLAR RECORD / CAMBRIDGE UNIV PRESS | 1475-3057 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4278 | EUROPEAN JOURNAL OF PAIN / WILEY | 1532-2149 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4279 | XENOBIOTICA / TAYLOR & FRANCIS LTD | 1366-5928 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4280 | EXPERIMENTAL AND MOLECULAR  PATHOLOGY / ACADEMIC PRESS INC ELSEVIER  SCIENCE | 1096-0945 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4281 | MEDICINAL CHEMISTRY RESEARCH / SPRINGER BIRKHAUSER | 1554-8120 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4282 | STEREOTACTIC AND FUNCTIONAL  NEUROSURGERY / KARGER | 1423-0372 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4283 | JOURNAL OF INTERVENTIONAL  CARDIAC ELECTROPHYSIOLO / SPRINGER | 1572-8595 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4284 | EUROPEAN JOURNAL OF ONCOLOGY  NURSING / ELSEVIER SCI LTD | 1532-2122 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4285 | VETERINARY AND COMPARATIVE  ORTHOPAEDICS AND TRAUM / GEORG THIEME VERLAG KG | 2567-6911 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4286 | KINETICS AND CATALYSIS / PLEIADES PUBLISHING INC | 1608-3210 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4287 | EATING DISORDERS / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1532-530X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4288 | JOURNAL OF DIGESTIVE DISEASES / WILEY | 1751-2980 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4289 | LANGUAGE TEACHING RESEARCH / SAGE PUBLICATIONS LTD | 1477-0954 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4290 | COSTUME-THE JOURNAL OF THE  COSTUME SOCIETY / EDINBURGH UNIV PRESS | 1749-6306 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4291 | ASIA PACIFIC VIEWPOINT / WILEY | 1467-8373 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4292 | JOURNAL OF LITERARY SEMANTICS / DE GRUYTER MOUTON | 1613-3838 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4293 | TEXTILE-CLOTH AND CULTURE / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1751-8350 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4294 | ECOLOGICAL CHEMISTRY AND  ENGINEERING S-CHEMIA I I / SCIENDO | 2084-4549 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4295 | Journal of Experimental Political Science Cambridg / Unknown | 2052-2649 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4296 | Law, Innovation and Technology Taylor and Francis  / N°   ISSN   E-ISSN | 1757-997X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4297 | South Asian Journal of Human Resources Management  / Unknown | 2349-5790 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4298 | Carbon Neutrality Springer / Unknown | 2788-8614 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4299 | WATER REUSE / IWA PUBLISHING | 2709-6106 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4300 | AMERICAN JOURNAL OF  GASTROENTEROLOGY / LIPPINCOTT WILLIAMS & WILKINS | 1572-0241 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4301 | PROTOPLASMA / SPRINGER WIEN | 1615-6102 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4302 | IEEE TRANSACTIONS ON ULTRASONICS  FERROELECTRICS A / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 1525-8955 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4303 | JOURNAL OF COMPOSITE MATERIALS / SAGE PUBLICATIONS LTD | 1530-793X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4304 | INFECTION / SPRINGER HEIDELBERG | 1439-0973 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4305 | APPLIED SOIL ECOLOGY / ELSEVIER | 1873-0272 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4306 | TEACHING AND TEACHER EDUCATION / PERGAMON-ELSEVIER SCIENCE LTD | 1879-2480 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4307 | BASIC & CLINICAL PHARMACOLOGY &  TOXICOLOGY / WILEY | 1742-7843 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4308 | CELL RESEARCH / SPRINGERNATURE | 1748-7838 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4309 | CONTEMPORARY CLINICAL TRIALS / ELSEVIER SCIENCE INC | 1559-2030 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4310 | JOURNAL OF CHINESE PHILOSOPHY / BRILL | 1540-6253 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4311 | CLINICAL IMPLANT DENTISTRY AND  RELATED RESEARCH / WILEY | 1708-8208 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4312 | JOURNAL OF MANAGEMENT &  ORGANIZATION / CAMBRIDGE UNIV PRESS | 1839-3527 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4313 | Journal of Indian Prosthodontic Society Wolters Kl / Unknown | 1998-4057 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4314 | JOURNAL OF FOREST RESEARCH / TAYLOR & FRANCIS LTD | 1610-7403 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4315 | DEVELOPMENTAL NEUROPSYCHOLOGY / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 8756-5641 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4316 | GERMAN JOURNAL OF HUMAN  RESOURCE MANAGEMENT- ZEIT / SAGE PUBLICATIONS INC | 2397-0030 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4317 | JOURNAL OF HOSPITALITY AND  TOURISM MANAGEMENT / ELSEVIER | 1839-5260 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4318 | INTERNATIONAL JOURNAL OF  SYSTEMATIC THEOLOGY / WILEY | 1468-2400 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4319 | JPAD-JOURNAL OF PREVENTION OF  ALZHEIMERS DISEASE / ELSEVIER | 2426-0266 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4320 | CAMERA OBSCURA / DUKE UNIV PRESS | 1529-1510 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4321 | BRAIN CONNECTIVITY / MARY ANN LIEBERT, INC | 2158-0022 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4322 | International Journal of Arts and Technology Inder / Unknown | 1754-8861 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4323 | International Journal of Foresight and Innovation  / Unknown | 1740-2824 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4324 | INTERNATIONAL JOURNAL OF  OPTOMECHATRONICS / TAYLOR & FRANCIS INC | 1559-9620 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4325 | POWDER TECHNOLOGY / ELSEVIER | 1873-328X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4326 | PHARMACOLOGICAL RESEARCH / ACADEMIC PRESS LTD- ELSEVIER  SCIENCE LT | 1096-1186 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4327 | LUNG / SPRINGER | 1432-1750 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4328 | JOURNAL OF MICROSCOPY / WILEY | 1365-2818 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4329 | STOCHASTIC PROCESSES AND THEIR  APPLICATIONS / ELSEVIER | 1879-209X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4330 | NATURE REVIEWS MICROBIOLOGY / NATURE PORTFOLIO | 1740-1534 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4331 | IEEE INTERNET COMPUTING / IEEE COMPUTER SOC | 1941-0131 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4332 | CONSERVATION GENETICS / SPRINGER | 1572-9737 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4333 | CNS & NEUROLOGICAL DISORDERS- DRUG TARGETS / BENTHAM SCIENCE PUBL | 1996-3181 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4334 | FRONTIERS OF INFORMATION  TECHNOLOGY & ELECTRONIC  / ZHEJIANG UNIV PRESS | 2095-9230 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4335 | Journal of Personal Selling and Sales Management T / Unknown | 1557-7813 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4336 | SEED SCIENCE RESEARCH / CAMBRIDGE UNIV PRESS | 1475-2735 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4337 | IRBM / ELSEVIER SCIENCE INC | 1959-0318 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4338 | PLANT BIOTECHNOLOGY REPORTS / SPRINGER | 1863-5474 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4339 | INTERNATIONAL JOURNAL OF PUBLIC  THEOLOGY / BRILL | 1872-5171 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4340 | Mental Health and Social Inclusion Emerald Group P / N°   ISSN   E-ISSN | 2042-8316 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4341 | ACM TRANSACTIONS ON STORAGE / ASSOC COMPUTING MACHINERY | 1553-3093 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4342 | Journal of Family Business Management Emerald Grou / Unknown | 2043-6246 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4343 | Asian Journal of Legal Education SAGE Publications / Unknown | 2348-2451 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4344 | JOURNAL OF PHYTOPATHOLOGY / WILEY | 1439-0434 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4345 | Abstract and Applied Analysis John Wiley and Sons  / Unknown | 1687-0409 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4346 | FAMILY & COMMUNITY HEALTH / LIPPINCOTT WILLIAMS & WILKINS | 1550-5057 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4347 | CLINICAL AUTONOMIC RESEARCH / SPRINGER HEIDELBERG | 1619-1560 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4348 | JOURNAL OF SCHOOL NURSING / SAGE PUBLICATIONS INC | 1546-8364 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4349 | JOURNAL FOR THE THEORY OF SOCIAL  BEHAVIOUR / WILEY | 1468-5914 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4350 | European archives of paediatric dentistry : offici / Unknown | 1996-9805 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4351 | CHILDRENS LITERATURE IN EDUCATION / SPRINGER | 1573-1693 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4352 | Nuclear Physics News Taylor and Francis Ltd. / N°   ISSN   E-ISSN | 1931-7336 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4353 | CHILDRENS GEOGRAPHIES / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1473-3285 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4354 | Journal of Environmental Studies and Sciences Spri / Unknown | 2190-6491 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4355 | ECONOMIC CHANGE AND  RESTRUCTURING / SPRINGER | 1574-0277 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4356 | Philosophy and Technology Springer Netherlands / Unknown | 2210-5441 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4357 | JOURNAL OF RENAL CARE / WILEY | 1755-6686 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4358 | CONSUMPTION MARKETS & CULTURE / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1477-223X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4359 | RESEARCH IN DANCE EDUCATION / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1470-1111 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4360 | DYNAMIC GAMES AND APPLICATIONS / SPRINGER BIRKHAUSER | 2153-0793 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4361 | International Journal of Services, Economics and M / Unknown | 1753-0830 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4362 | INTERNATIONAL JOURNAL OF  COMPUTER-SUPPORTED  COLL / SPRINGER | 1556-1615 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4363 | Journal of Computational Social Science Springer N / Unknown | 2432-2725 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4364 | Advances in Fuzzy Systems John Wiley and Sons Ltd / Unknown | 1687-711X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4365 | Journal of Global Operations and Strategic Sourcin / Unknown | 2398-5372 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4366 | APPLIED SOFT COMPUTING / ELSEVIER | 1872-9681 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4367 | VETERINARY MICROBIOLOGY / ELSEVIER | 1873-2542 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4368 | EXPERIMENTAL AND CLINICAL  ENDOCRINOLOGY & DIABETE / GEORG THIEME VERLAG KG | 1439-3646 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4369 | STEEL RESEARCH INTERNATIONAL / WILEY-V C H VERLAG GMBH | 1869-344X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4370 | CLUSTER COMPUTING-THE JOURNAL  OF NETWORKS SOFTWAR / SPRINGER | 1573-7543 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4371 | ANNALS OF TELECOMMUNICATIONS / SPRINGER INT PUBL AG | 1958-9395 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4372 | INTERNATIONAL JOURNAL OF  OBSTETRIC ANESTHESIA / ELSEVIER SCI LTD | 1532-3374 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4373 | INTERNATIONAL JOURNAL OF  INTELLIGENT SYSTEMS / WILEY | 1098-111X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4374 | INTERDISCIPLINARY SCIENCE REVIEWS / SAGE PUBLICATIONS INC | 1743-2790 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4375 | JOURNAL OF FIELD ARCHAEOLOGY / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 2042-4582 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4376 | JOURNAL OF MATERIAL CYCLES AND  WASTE MANAGEMENT / SPRINGER | 1611-8227 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4377 | Annales de Cardiologie et d'Angeiologie Elsevier M / Unknown | 1768-3181 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4378 | BOUNDARY 2-AN INTERNATIONAL  JOURNAL OF LITERATURE / DUKE UNIV PRESS | 1527-2141 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4379 | EXPERT REVIEW OF CLINICAL  IMMUNOLOGY / TAYLOR & FRANCIS LTD | 1744-8409 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4380 | Manuelle Medizin Springer Verlag / Unknown | 1433-0466 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4381 | JOURNAL DE MATHEMATIQUES PURES  ET APPLIQUEES / ELSEVIER | 1776-3371 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4382 | CYBERNETICS AND SYSTEMS / TAYLOR & FRANCIS INC | 1087-6553 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4383 | BIOSTATISTICS / OXFORD UNIV PRESS | 1468-4357 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4384 | INDUSTRIAL ARCHAEOLOGY REVIEW / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1745-8196 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4385 | INTERNATIONAL JOURNAL OF SPEECH- LANGUAGE PATHOLOG / TAYLOR & FRANCIS LTD | 1754-9515 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4386 | Monte Carlo Methods and Applications Walter de Gru / Unknown | 1569-3961 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4387 | Studies in Gender and Sexuality Taylor and Francis / Unknown | 1940-9206 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4388 | RESEARCH AND PRACTICE FOR  PERSONS WITH SEVERE DIS / SAGE PUBLICATIONS INC | 2169-2408 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4389 | International Journal of Geosynthetics and Ground  / Unknown | 2199-9279 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4390 | ARCHNET-IJAR INTERNATIONAL  JOURNAL OF ARCHITECTUR / EMERALD GROUP PUBLISHING LTD | 2631-6862 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4391 | GENETIC PROGRAMMING AND  EVOLVABLE MACHINES / SPRINGER | 1573-7632 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4392 | Journal of Advances in Management Research Emerald / Unknown | 2049-3207 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4393 | Pedagogy in Health Promotion SAGE Publications Inc / Unknown | 2373-3802 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4394 | Word Structure Edinburgh University Press / Unknown | 1755-2036 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4395 | Visual Informatics Elsevier B.V. / Unknown | 2543-2656 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4396 | APPLIED MATHEMATICS AND  COMPUTATION / ELSEVIER SCIENCE INC | 1873-5649 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4397 | PLANETARY AND SPACE SCIENCE / PERGAMON-ELSEVIER SCIENCE LTD | 1873-5088 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4398 | JOURNAL OF PSYCHOLOGY / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1940-1019 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4399 | PHARMACOLOGY & THERAPEUTICS / PERGAMON-ELSEVIER SCIENCE LTD | 1879-016X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4400 | JOURNAL OF MIDWIFERY & WOMENS  HEALTH / WILEY | 1542-2011 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4401 | JOURNAL OF INTERNATIONAL  ECONOMICS / ELSEVIER | 1873-0353 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4402 | FLOW MEASUREMENT AND  INSTRUMENTATION / ELSEVIER SCI LTD | 1873-6998 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4403 | SOCIAL SCIENCE RESEARCH / ACADEMIC PRESS INC ELSEVIER  SCIENCE | 1096-0317 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4404 | MOBILE NETWORKS & APPLICATIONS / SPRINGER | 1572-8153 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4405 | CURRENT PSYCHIATRY REPORTS / SPRINGER | 1535-1645 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4406 | AIR QUALITY ATMOSPHERE AND  HEALTH / SPRINGER | 1873-9326 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4407 | JOURNAL OF ENERGY ENGINEERING / ASCE-AMER SOC CIVIL ENGINEERS | 1943-7897 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4408 | JOURNAL OF AUTOMATED REASONING / SPRINGER | 1573-0670 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4409 | JOURNAL OF HIGHER EDUCATION  POLICY AND MANAGEMENT / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1469-9508 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4410 | JOURNAL OF APPLIED ANIMAL  WELFARE SCIENCE / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1532-7604 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4411 | Jeunesse: Young People, Texts, Cultures University / Unknown | 1920-261X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4412 | SOCIOLOGY OF RACE AND ETHNICITY / SAGE PUBLICATIONS INC | 2332-6506 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4413 | Court Historian Taylor and Francis Ltd. / Unknown | 2056-3450 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4414 | JOURNAL OF INTEGRATIVE AND  COMPLEMENTARY MEDICINE / MARY ANN LIEBERT, INC | 2768-3613 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4415 | Journal of Intelligent Systems and Internet of Thi / Unknown | 2769-786X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4416 | APPLIED SURFACE SCIENCE / ELSEVIER | 1873-5584 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4417 | JOURNAL OF BACTERIOLOGY / AMER SOC MICROBIOLOGY | 1098-5530 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4418 | INTERNATIONAL JOURNAL / SAGE PUBLICATIONS LTD | 2052-465X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4419 | JOURNAL OF ENVIRONMENTAL  RADIOACTIVITY / ELSEVIER SCI LTD | 1879-1700 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4420 | NEUROPHYSIOLOGIE CLINIQUE- CLINICAL NEUROPHYSIOLOG / ELSEVIER FRANCE-EDITIONS  SCIENTIFIQUES  | 1769-7131 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4421 | EUROPEAN JOURNAL OF AGRONOMY / ELSEVIER | 1873-7331 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4422 | JOURNAL OF THE AMERICAN ACADEMY  OF AUDIOLOGY / THIEME MEDICAL PUBL INC | 2157-3107 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4423 | JOURNAL OF VIBRATION ENGINEERING  & TECHNOLOGIES / SPRINGER HEIDELBERG | 2523-3939 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4424 | INQUIRY-THE JOURNAL OF HEALTH  CARE ORGANIZATION P / SAGE PUBLICATIONS INC | 1945-7243 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4425 | MABS / TAYLOR & FRANCIS INC | 1942-0870 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4426 | Journal of Applied Laboratory Medicine Oxford Univ / Unknown | 2576-9456 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4427 | Labour John Wiley and Sons Inc / Unknown | 1467-9914 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4428 | INFORMATION TECHNOLOGY FOR  DEVELOPMENT / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1554-0170 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4429 | Oncology Reviews Frontiers Media SA / Unknown | 1970-5565 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4430 | Interfacial Phenomena and Heat Transfer Begell Hou / Unknown | 2169-2785 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4431 | MICROBIAL RISK ANALYSIS / ELSEVIER | 2352-3530 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4432 | WSEAS Transactions on Fluid Mechanics World Scient / Unknown | 2224-347X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4433 | AMERICAN NATURALIST / UNIV CHICAGO PRESS | 1537-5323 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4434 | HUMAN MOLECULAR GENETICS / OXFORD UNIV PRESS | 1460-2083 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4435 | BIOMEDICAL ENGINEERING- BIOMEDIZINISCHE TECHNIK / WALTER DE GRUYTER GMBH | 1862-278X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4436 | EUROPEAN JOURNAL OF CLINICAL  PHARMACOLOGY / SPRINGER HEIDELBERG | 1432-1041 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4437 | CANADIAN JOURNAL OF PLANT  SCIENCE / CANADIAN SCIENCE PUBLISHING | 1918-1833 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4438 | JOURNAL OF THE CHINESE CHEMICAL  SOCIETY / WILEY-V C H VERLAG GMBH | 2192-6549 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4439 | JOURNAL OF SOL-GEL SCIENCE AND  TECHNOLOGY / SPRINGER | 1573-4846 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4440 | IEEE TRANSACTIONS ON FUZZY  SYSTEMS / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 1941-0034 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4441 | BRITISH JOURNAL FOR THE HISTORY OF  SCIENCE / CAMBRIDGE UNIV PRESS | 1474-001X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4442 | INTERNATIONAL JOURNAL OF CIRCUIT  THEORY AND APPLI / WILEY | 1097-007X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4443 | EUROPEAN JOURNAL OF  COMBINATORICS / ACADEMIC PRESS LTD- ELSEVIER  SCIENCE LT | 1095-9971 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4444 | BEHAVIORAL ECOLOGY / OXFORD UNIV PRESS INC | 1465-7279 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4445 | CLAY MINERALS / CAMBRIDGE UNIV PRESS | 1471-8030 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4446 | MOLECULAR ONCOLOGY / WILEY | 1878-0261 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4447 | TRANSPORTATION / SPRINGER | 1572-9435 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4448 | ACM TRANSACTIONS ON MULTIMEDIA  COMPUTING COMMUNIC / ASSOC COMPUTING MACHINERY | 1551-6865 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4449 | IET ELECTRIC POWER APPLICATIONS / WILEY | 1751-8679 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4450 | JOURNAL OF BRYOLOGY / TAYLOR & FRANCIS LTD | 1743-2820 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4451 | PSYCHOLOGICAL METHODS / AMER PSYCHOLOGICAL ASSOC | 1939-1463 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4452 | BILINGUALISM-LANGUAGE AND  COGNITION / CAMBRIDGE UNIV PRESS | 1469-1841 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4453 | GEO-SPATIAL INFORMATION SCIENCE / TAYLOR & FRANCIS LTD | 1993-5153 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4454 | VEGETATION HISTORY AND  ARCHAEOBOTANY / SPRINGER | 1617-6278 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4455 | GLOBAL FINANCE JOURNAL / ELSEVIER | 1873-5665 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4456 | WILEY INTERDISCIPLINARY REVIEWS- COGNITIVE SCIENCE / WILEY | 1939-5086 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4457 | Journal of Humanitarian Logistics and Supply Chain / Unknown | 2042-6755 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4458 | COMPUTATIONAL MATERIALS SCIENCE / ELSEVIER | 1879-0801 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4459 | JOURNAL OF PERSONALITY / WILEY | 1467-6494 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4460 | EUROPEAN STROKE JOURNAL / SAGE PUBLICATIONS LTD | 2396-9881 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4461 | PHYSIOLOGICAL ENTOMOLOGY / WILEY | 1365-3032 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4462 | HORTICULTURE RESEARCH / OXFORD UNIV PRESS INC | 2662-6810 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4463 | INTERNATIONAL BUSINESS REVIEW / ELSEVIER | 1873-6149 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4464 | SUGAR TECH / SPRINGER INDIA | 0974-0740 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4465 | British Journal of Visual Impairment SAGE Publicat / Unknown | 1744-5809 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4466 | INTERNATIONAL JOURNAL OF  PSYCHIATRY IN CLINICAL P / TAYLOR & FRANCIS LTD | 1471-1788 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4467 | Scientia Pharmaceutica Multidisciplinary Digital P / Unknown | 2218-0532 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4468 | MEDICAL LAW REVIEW / OXFORD UNIV PRESS | 1464-3790 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4469 | International Journal of Grid and Utility Computin / Unknown | 1741-8488 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4470 | INTERNATIONAL JOURNAL ON  SOFTWARE TOOLS FOR TECHN / SPRINGER HEIDELBERG | 1433-2787 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4471 | AlterNative SAGE Publications Inc. / Unknown | 1177-1801 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4472 | Law, Culture and the Humanities SAGE Publications  / Unknown | 1743-9752 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4473 | Moscow University Mathematics Bulletin Pleiades Pu / Unknown | 1934-8444 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4474 | MULTINATIONAL BUSINESS REVIEW / EMERALD GROUP PUBLISHING LTD | 2054-1686 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4475 | JOURNAL OF HOSPITALITY AND  TOURISM TECHNOLOGY / EMERALD GROUP PUBLISHING LTD | 1757-9899 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4476 | CANADIAN JOURNAL OF FILM STUDIES- REVUE CANADIENNE / UNIV TORONTO PRESS INC | 2561-424X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4477 | SURFACE INNOVATIONS / EMERALD GROUP PUBLISHING LTD | 2050-6260 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4478 | JOURNAL OF CHINESE LITERATURE AND  CULTURE / DUKE UNIV PRESS | 2329-0056 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4479 | AMERICAN JOURNAL OF THE MEDICAL  SCIENCES / ELSEVIER SCIENCE INC | 1538-2990 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4480 | NUCLEAR ENGINEERING AND DESIGN / ELSEVIER SCIENCE SA | 1872-759X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4481 | PEDIATRIC PULMONOLOGY / WILEY | 8755-6863 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4482 | GEODERMA / ELSEVIER | 1872-6259 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4483 | RISK ANALYSIS / WILEY | 1539-6924 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4484 | CHEMISTRY AND PHYSICS OF LIPIDS / ELSEVIER IRELAND LTD | 1873-2941 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4485 | INTERNATIONAL JOURNAL OF  COLORECTAL DISEASE / SPRINGER | 1432-1262 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4486 | ADDITIVE MANUFACTURING / ELSEVIER | 2214-8604 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4487 | CLINICAL DRUG INVESTIGATION / ADIS INT LTD | 1179-1918 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4488 | International Journal of Modelling, Identification / Unknown | 1746-6180 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4489 | CHILD ABUSE REVIEW / WILEY | 1099-0852 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4490 | MEXICAN STUDIES-ESTUDIOS  MEXICANOS / UNIV CALIFORNIA PRESS | 1533-8320 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4491 | TOPICS IN EARLY CHILDHOOD SPECIAL  EDUCATION / SAGE PUBLICATIONS INC | 1538-4845 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4492 | SEMINARS IN IMMUNOPATHOLOGY / SPRINGER HEIDELBERG | 1863-2300 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4493 | CELLULAR AND MOLECULAR  BIOENGINEERING / SPRINGER | 1865-5033 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4494 | INVERTEBRATE SYSTEMATICS / CSIRO PUBLISHING | 1447-2600 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4495 | AMERICAN JOURNAL OF HEALTH  ECONOMICS / UNIV CHICAGO PRESS | 2332-3507 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4496 | COCHRANE DATABASE OF SYSTEMATIC  REVIEWS / WILEY | 1469-493X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4497 | International Journal of Persian Literature Penn S / Unknown | 2376-5755 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4498 | INTERNATIONAL JOURNAL OF  BIOLOGICAL MACROMOLECULE / ELSEVIER | 1879-0003 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4499 | RENAISSANCE QUARTERLY / CAMBRIDGE UNIV PRESS | 1935-0236 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4500 | IEEE ANTENNAS AND WIRELESS  PROPAGATION LETTERS / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 1548-5757 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4501 | BULLETIN OF THE ATOMIC SCIENTISTS / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1938-3282 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4502 | JOURNAL OF INTEGRATIVE PLANT  BIOLOGY / WILEY | 1744-7909 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4503 | DIGITAL SIGNAL PROCESSING / ACADEMIC PRESS INC ELSEVIER  SCIENCE | 1095-4333 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4504 | COMPARATIVE BIOCHEMISTRY AND  PHYSIOLOGY B-BIOCHEM / ELSEVIER SCIENCE INC | 1879-1107 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4505 | STRATEGIC MANAGEMENT JOURNAL / WILEY | 1097-0266 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4506 | INDIAN JOURNAL OF PSYCHIATRY / WOLTERS KLUWER MEDKNOW  PUBLICATIONS | 1998-3794 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4507 | ECOTOXICOLOGY / SPRINGER | 1573-3017 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4508 | ACM COMPUTING SURVEYS / ASSOC COMPUTING MACHINERY | 1557-7341 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4509 | AUTISM / SAGE PUBLICATIONS LTD | 1461-7005 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4510 | JOURNAL OF ECONOMIC EDUCATION / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 2152-4068 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4511 | TRANSACTIONS IN GIS / WILEY | 1467-9671 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4512 | ANNALS OF FUNCTIONAL ANALYSIS / SPRINGER BASEL AG | 2639-7390 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4513 | ACTA OECONOMICA / AKADEMIAI KIADO ZRT | 1588-2659 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4514 | JOURNAL OF VISUAL CULTURE / SAGE PUBLICATIONS INC | 1741-2994 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4515 | FOREIGN POLICY ANALYSIS / OXFORD UNIV PRESS | 1743-8594 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4516 | Global Intellectual History Taylor and Francis Ltd / Unknown | 2380-1891 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4517 | INTERFACES AND FREE BOUNDARIES / EUROPEAN MATHEMATICAL SOC- EMS | 1463-9971 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4518 | Advances in Mental Health Taylor and Francis Ltd. / N°   ISSN   E-ISSN | 1838-7357 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4519 | European Journal of Management and Business Econom / Unknown | 2444-8494 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4520 | Green Energy and Intelligent Transportation Elsevi / N°   ISSN   E-ISSN | 2097-2512 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4521 | NUCLEAR INSTRUMENTS & METHODS  IN PHYSICS RESEARCH / ELSEVIER | 1872-9584 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4522 | IEEE TRANSACTIONS ON ELECTRON  DEVICES / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 1557-9646 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4523 | ANALYTICAL BIOCHEMISTRY / ACADEMIC PRESS INC ELSEVIER  SCIENCE | 1096-0309 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4524 | COMMUNICATIONS IN ALGEBRA / TAYLOR & FRANCIS INC | 1532-4125 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4525 | CHEMBIOCHEM / WILEY-V C H VERLAG GMBH | 1439-7633 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4526 | Indian Journal of Otolaryngology and Head and Neck / Unknown | 2231-3796 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4527 | PROTEINS-STRUCTURE FUNCTION AND  BIOINFORMATICS / WILEY | 1097-0134 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4528 | INTERNATIONAL JOURNAL FOR  NUMERICAL METHODS IN FL / WILEY | 1097-0363 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4529 | HISPANIC REVIEW / UNIV PENNSYLVANIA PRESS | 1553-0639 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4530 | DRUG SAFETY / ADIS INT LTD | 1179-1942 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4531 | INTERNATIONAL JOURNAL OF  SURGICAL PATHOLOGY / SAGE PUBLICATIONS INC | 1940-2465 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4532 | ACTA MATHEMATICAE APPLICATAE  SINICA-ENGLISH SERIE / SPRINGER HEIDELBERG | 1618-3932 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4533 | LIGHT-SCIENCE & APPLICATIONS / SPRINGERNATURE | 2095-5545 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4534 | ENVIRONMENTAL VALUES / SAGE PUBLICATIONS INC | 1752-7015 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4535 | HEALTH PROMOTION JOURNAL OF  AUSTRALIA / WILEY | 2201-1617 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4536 | NUKLEONIKA / SCIENDO | 1508-5791 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4537 | NEW DIRECTIONS FOR CHILD AND  ADOLESCENT DEVELOPME / WILEY | 1534-8687 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4538 | JAPAN JOURNAL OF NURSING SCIENCE / WILEY | 1742-7932 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4539 | OXFORD LITERARY REVIEW / EDINBURGH UNIV PRESS | 1757-1634 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4540 | Journal of the Operations Research Society of Chin / Unknown | 2194-6698 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4541 | PHILOSOPHICAL PERSPECTIVES / WILEY | 1758-2245 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4542 | WMU Journal of Maritime Affairs Springer Science a / Unknown | 1654-1642 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4543 | INTERNATIONAL JOURNAL FOR  UNCERTAINTY QUANTIFICAT / BEGELL HOUSE INC | 2152-5099 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4544 | Acta Historica Universitatis Klaipedensis Institut / Unknown | 2351-6526 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4545 | Translation and Translanguaging in Multilingual Co / Unknown | 2352-1813 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4546 | LGBTQ FAMILY-AN INTERDISCIPLINARY  JOURNAL / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 2770-338X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4547 | IEEE TRANSACTIONS ON MICROWAVE  THEORY AND TECHNIQ / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 1557-9670 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4548 | HEART LUNG AND CIRCULATION / ELSEVIER SCIENCE INC | 1444-2892 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4549 | IEEE TRANSACTIONS ON SIGNAL  PROCESSING / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 1941-0476 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4550 | HISTOPATHOLOGY / WILEY | 1365-2559 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4551 | JOURNAL OF THE AMERICAN COLLEGE  OF RADIOLOGY / ELSEVIER SCIENCE INC | 1558-349X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4552 | BIOTECHNOLOGY PROGRESS / WILEY | 8756-7938 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4553 | AMERICAN JOURNAL OF ECONOMICS  AND SOCIOLOGY / WILEY | 1536-7150 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4554 | KNEE / ELSEVIER | 1873-5800 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4555 | OPERATIONS RESEARCH LETTERS / ELSEVIER | 1872-7468 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4556 | AGING & MENTAL HEALTH / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1364-6915 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4557 | CURRENT OPINION IN  OPHTHALMOLOGY / LIPPINCOTT WILLIAMS & WILKINS | 1531-7021 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4558 | JOURNAL OF GENETIC COUNSELING / WILEY | 1573-3599 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4559 | EXPERIMENTAL AND CLINICAL  PSYCHOPHARMACOLOGY / AMER PSYCHOLOGICAL ASSOC | 1936-2293 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4560 | JOURNAL OF FAMILY VIOLENCE / SPRINGER/PLENUM PUBLISHERS | 1573-2851 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4561 | JOURNAL OF INDUSTRIAL ECONOMICS / WILEY | 1467-6451 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4562 | Home Health Care Management and Practice SAGE Publ / Unknown | 1552-6739 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4563 | FOOD REVIEWS INTERNATIONAL / TAYLOR & FRANCIS INC | 8755-9129 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4564 | JOURNAL OF URBAN PLANNING AND  DEVELOPMENT / ASCE-AMER SOC CIVIL ENGINEERS | 1943-5444 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4565 | JOURNAL OF HEALTH SERVICES  RESEARCH & POLICY / SAGE PUBLICATIONS INC | 1758-1060 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4566 | CRITICAL CRIMINOLOGY / SPRINGER | 1572-9877 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4567 | Physician Assistant Clinics Elsevier Inc. / Unknown | 2405-8009 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4568 | CRITICAL REVIEWS IN THERAPEUTIC  DRUG CARRIER SYST / BEGELL HOUSE INC | 2162-660X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4569 | JOURNAL OF PHOTOCHEMISTRY AND  PHOTOBIOLOGY C-PHOT / ELSEVIER | 1873-2739 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4570 | IET BIOMETRICS / WILEY | 2047-4946 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4571 | Strategy Science INFORMS Institute for Operations  / Unknown | 2333-2077 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4572 | Mediterranean Geoscience Reviews Springer Nature / Unknown | 2661-8648 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4573 | European Journal of Environmental Sciences Charles / Unknown | 2336-1964 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4574 | ANNALS OF THE RHEUMATIC DISEASES / ELSEVIER | 1468-2060 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4575 | CLINICAL INFECTIOUS DISEASES / OXFORD UNIV PRESS INC | 1537-6591 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4576 | CHEMICAL ENGINEERING SCIENCE / PERGAMON-ELSEVIER SCIENCE LTD | 1873-4405 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4577 | COMMUNICATIONS IN  MATHEMATICAL PHYSICS / SPRINGER | 1432-0916 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4578 | JOURNAL OF SHOULDER AND ELBOW  SURGERY / MOSBY-ELSEVIER | 1532-6500 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4579 | AMERICAN STATISTICIAN / TAYLOR & FRANCIS INC | 1537-2731 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4580 | CANCER RADIOTHERAPIE / ELSEVIER | 1769-6658 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4581 | EDUCATION AND TRAINING / EMERALD GROUP PUBLISHING LTD | 1758-6127 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4582 | BIOTROPICA / WILEY | 1744-7429 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4583 | INTERNATIONAL SOCIAL WORK / SAGE PUBLICATIONS LTD | 1461-7234 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4584 | QUARTERLY JOURNAL OF  EXPERIMENTAL PSYCHOLOGY / SAGE PUBLICATIONS LTD | 1747-0226 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4585 | ITALIAN JOURNAL OF PEDIATRICS / BMC | 1824-7288 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4586 | JOURNAL OF DRUG ISSUES / SAGE PUBLICATIONS INC | 1945-1369 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4587 | JOURNAL OF AGING AND PHYSICAL  ACTIVITY / HUMAN KINETICS PUBL INC | 1543-267X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4588 | HONG KONG JOURNAL OF EMERGENCY  MEDICINE / WILEY | 2309-5407 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4589 | PRAXIS DER KINDERPSYCHOLOGIE UND  KINDERPSYCHIATRI / BRILL DEUTSCHLAND GMBH | 2196-8225 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4590 | JOURNAL OF ORTHOPAEDICS AND  TRAUMATOLOGY / SPRINGER | 1590-9999 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4591 | International Journal of Business Performance Mana / Unknown | 1741-5039 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4592 | Journal of Control Science and Engineering John Wi / Unknown | 1687-5257 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4593 | Journal of Classical Sociology SAGE Publications L / Unknown | 1741-2897 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4594 | Comparative Exercise Physiology Brill Wageningen A / Unknown | 1755-2559 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4595 | Asian Journal of Comparative Law Cambridge Univers / Unknown | 2194-6078 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4596 | FORUM (The Netherlands) John Benjamins Publishing  / Unknown | 2451-909X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4597 | Journal of Scleroderma and Related Disorders SAGE  / Unknown | 2397-1991 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4598 | Sankhya B Springer India / Unknown | 0976-8394 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4599 | INTERNATIONAL JOURNAL OF SPRAY  AND COMBUSTION DYN / SAGE PUBLICATIONS INC | 1756-8285 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4600 | Acta Phlebologica Edizioni Minerva Medica S.p.A. / Unknown | 1827-1766 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4601 | SYNTHESIS-STUTTGART / GEORG THIEME VERLAG KG | 1437-210X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4602 | INTERNATIONAL BIODETERIORATION &  BIODEGRADATION / ELSEVIER SCI LTD | 1879-0208 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4603 | AURIS NASUS LARYNX / ELSEVIER SCI LTD | 1879-1476 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4604 | TELECOMMUNICATIONS POLICY / ELSEVIER SCI LTD | 1879-3258 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4605 | AFFILIA-FEMINIST INQUIRY IN SOCIAL  WORK / SAGE PUBLICATIONS INC | 1552-3020 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4606 | ENERGY FOR SUSTAINABLE  DEVELOPMENT / ELSEVIER | 2352-4669 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4607 | LAW AND HUMAN BEHAVIOR / EDUCATIONAL PUBLISHING  FOUNDATION-AMERI | 1573-661X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4608 | JOURNAL OF VASCULAR RESEARCH / KARGER | 1423-0135 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4609 | ULTRASOUND QUARTERLY / LIPPINCOTT WILLIAMS & WILKINS | 1536-0253 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4610 | COMPLEMENTARY THERAPIES IN  CLINICAL PRACTICE / ELSEVIER SCI LTD | 1873-6947 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4611 | Annals of the ICRP SAGE Publications Inc. / Unknown | 1872-969X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4612 | OXFORD ART JOURNAL / OXFORD UNIV PRESS | 1741-7287 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4613 | CHINESE STUDIES IN HISTORY / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1558-0407 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4614 | EUROPEAN EARLY CHILDHOOD  EDUCATION RESEARCH JOURN / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1752-1807 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4615 | SCANDINAVIAN JOURNAL OF SURGERY / SAGE PUBLICATIONS LTD | 1799-7267 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4616 | ANALYSIS AND MATHEMATICAL  PHYSICS / SPRINGER BASEL AG | 1664-2368 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4617 | Journal of Applied Research in Higher Education Em / Unknown | 2050-7003 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4618 | Psiquiatria Biologica Elsevier Espana S.L.U / Unknown | 1578-8962 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4619 | REVIEW OF ACCOUNTING STUDIES / SPRINGER | 1573-7136 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4620 | CITY & COMMUNITY / SAGE PUBLICATIONS INC | 1540-6040 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4621 | Scrutiny2 Taylor and Francis Ltd. / Unknown | 1812-5441 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4622 | ACM TRANSACTIONS ON COMPUTER  SYSTEMS / ASSOC COMPUTING MACHINERY | 1557-7333 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4623 | Hand Therapy SAGE Publications Inc. / Unknown | 1758-9991 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4624 | Autoimmune Diseases John Wiley and Sons Ltd / Unknown | 2090-0430 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4625 | Journal of Business Cycle Research Springer Intern / Unknown | 2509-7970 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4626 | JOURNAL OF MATERIALS PROCESSING  TECHNOLOGY / ELSEVIER SCIENCE SA | 1873-4774 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4627 | MONATSHEFTE FUR CHEMIE / SPRINGER WIEN | 1434-4475 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4628 | SYNTHETIC COMMUNICATIONS / TAYLOR & FRANCIS INC | 1532-2432 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4629 | IEEE COMMUNICATIONS MAGAZINE / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 1558-1896 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4630 | JOURNAL OF THROMBOSIS AND  HAEMOSTASIS / ELSEVIER SCIENCE INC | 1538-7933 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4631 | JOURNAL OF INDUSTRIAL AND  ENGINEERING CHEMISTRY / ELSEVIER SCIENCE INC | 1876-794X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4632 | TRENDS IN PHARMACOLOGICAL  SCIENCES / CELL PRESS | 1873-3735 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4633 | Journal of Risk and Financial Management Multidisc / Unknown | 1911-8074 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4634 | Adoption and Fostering SAGE Publications Ltd / Unknown | 1740-469X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4635 | TOURISM ECONOMICS / SAGE PUBLICATIONS LTD | 2044-0375 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4636 | JOURNAL OF BUSINESS AND  PSYCHOLOGY / SPRINGER | 1573-353X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4637 | TOPICS IN GERIATRIC REHABILITATION / LIPPINCOTT WILLIAMS & WILKINS | 1550-2414 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4638 | CLINICAL NEURORADIOLOGY / SPRINGER HEIDELBERG | 1869-1447 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4639 | RESEARCH IN PHENOMENOLOGY / BRILL | 1569-1640 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4640 | JOURNAL OF POLICY AND PRACTICE IN  INTELLECTUAL DI / WILEY | 1741-1130 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4641 | MENTAL HEALTH AND PHYSICAL  ACTIVITY / ELSEVIER SCI LTD | 1878-0199 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4642 | EARTH SURFACE DYNAMICS / COPERNICUS GESELLSCHAFT MBH | 2196-632X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4643 | TRANSPORTMETRICA B-TRANSPORT  DYNAMICS / TAYLOR & FRANCIS LTD | 2168-0582 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4644 | Journal of Horticultural Research Sciendo / Unknown | 2353-3978 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4645 | ANNUAL REVIEW OF STATISTICS AND  ITS APPLICATION / ANNUAL REVIEWS | 2326-831X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4646 | Journal of Globalization and Development Walter de / Unknown | 2194-6353 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4647 | AAPPS Bulletin Springer / Unknown | 2309-4710 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4648 | EVOLUTION / OXFORD UNIV PRESS | 1558-5646 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4649 | FOOD RESEARCH INTERNATIONAL / ELSEVIER | 1873-7145 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4650 | LAB ON A CHIP / ROYAL SOC CHEMISTRY | 1473-0197 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4651 | COMMUNICATIONS IN SOIL SCIENCE  AND PLANT ANALYSIS / TAYLOR & FRANCIS INC | 1532-2416 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4652 | AGRICULTURAL WATER MANAGEMENT / ELSEVIER | 1873-2283 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4653 | JAPANESE JOURNAL OF CLINICAL  ONCOLOGY / OXFORD UNIV PRESS | 1465-3621 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4654 | COMPUTERS & GRAPHICS-UK / PERGAMON-ELSEVIER SCIENCE LTD | 1873-7684 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4655 | IEEE JOURNAL OF EMERGING AND  SELECTED TOPICS IN P / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 2168-6785 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4656 | TRIBOLOGY TRANSACTIONS / TAYLOR & FRANCIS INC | 1547-397X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4657 | LETTERS IN ORGANIC CHEMISTRY / BENTHAM SCIENCE PUBL LTD | 1875-6255 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4658 | SCANDINAVIAN JOURNAL OF  ECONOMICS / WILEY | 1467-9442 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4659 | JOURNAL OF WATERWAY PORT  COASTAL AND OCEAN ENGINE / ASCE-AMER SOC CIVIL ENGINEERS | 1943-5460 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4660 | Journal of Indian Association of Pediatric Surgeon / Unknown | 1998-3891 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4661 | JOURNAL OF MEDICAL BIOGRAPHY / SAGE PUBLICATIONS INC | 1758-1087 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4662 | ARCHIV FUR PAPYRUSFORSCHUNG  UND VERWANDTE GEBIETE / WALTER DE GRUYTER GMBH | 1867-1551 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4663 | ADVANCES IN CEMENT RESEARCH / EMERALD GROUP PUBLISHING LTD | 1751-7605 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4664 | ECONOMICS OF INNOVATION AND  NEW TECHNOLOGY / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1476-8364 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4665 | RUSSIAN LINGUISTICS / SPRINGER | 1572-8714 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4666 | PERSONALITY AND MENTAL HEALTH / WILEY | 1932-863X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4667 | International Journal of Accounting, Auditing and  / Unknown | 1740-8016 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4668 | International Journal of Tourism Cities Emerald Gr / Unknown | 2056-5615 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4669 | Control Theory and Technology Springer Science + B / Unknown | 2198-0942 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4670 | European Journal for Sport and Society Taylor and  / Unknown | 2380-5919 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4671 | JOURNAL OF MANAGEMENT  ANALYTICS / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 2327-0039 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4672 | London Review of International Law Oxford Universi / Unknown | 2050-6333 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4673 | ROBOTIC INTELLIGENCE AND  AUTOMATION / EMERALD GROUP PUBLISHING LTD | 2754-6977 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4674 | REVUE DE MEDECINE INTERNE / ELSEVIER FRANCE-EDITIONS  SCIENTIFIQUES  | 1768-3122 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4675 | NEUROPSYCHOPHARMACOLOGY / SPRINGERNATURE | 1740-634X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4676 | ANALYSIS / OXFORD UNIV PRESS | 1467-8284 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4677 | WEED SCIENCE / CAMBRIDGE UNIV PRESS | 1550-2759 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4678 | INTERMETALLICS / ELSEVIER SCI LTD | 1879-0216 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4679 | JOURNAL OF PEDIATRIC AND  ADOLESCENT GYNECOLOGY / ELSEVIER SCIENCE INC | 1873-4332 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4680 | CRITICAL REVIEWS IN ONCOLOGY  HEMATOLOGY / ELSEVIER SCIENCE INC | 1879-0461 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4681 | QUALITY AND RELIABILITY  ENGINEERING INTERNATIONAL / WILEY | 1099-1638 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4682 | INSURANCE MATHEMATICS &  ECONOMICS / ELSEVIER | 1873-5959 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4683 | EXPERT OPINION ON INVESTIGATIONAL  DRUGS / TAYLOR & FRANCIS LTD | 1744-7658 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4684 | IEEE TRANSACTIONS ON EDUCATION / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 1557-9638 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4685 | COMPUTATIONAL MATHEMATICS AND  MATHEMATICAL PHYSIC / PLEIADES PUBLISHING INC | 1555-6662 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4686 | THEATRE RESEARCH INTERNATIONAL / CAMBRIDGE UNIV PRESS | 1474-0672 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4687 | IEEE JOURNAL OF SELECTED TOPICS IN  SIGNAL PROCESS / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 1941-0484 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4688 | International Social Security Review Wiley-Blackwe / Unknown | 1468-246X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4689 | AFRICAN STUDIES / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1469-2872 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4690 | JOURNAL OF SEISMOLOGY / SPRINGER | 1573-157X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4691 | EXPERIMENTAL AGING RESEARCH / TAYLOR & FRANCIS INC | 1096-4657 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4692 | Queue Association for Computing Machinery (ACM) / Unknown | 1542-7749 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4693 | MARKETING LETTERS / SPRINGER | 1573-059X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4694 | International Journal of Computing Science and Mat / Unknown | 1752-5063 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4695 | WILEY INTERDISCIPLINARY REVIEWS- CLIMATE CHANGE / WILEY | 1757-7799 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4696 | Quality in Ageing and Older Adults Emerald Group P / Unknown | 2042-8766 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4697 | Studies in Documentary Film Taylor and Francis Ltd / Unknown | 1750-3299 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4698 | SOCIETY AND MENTAL HEALTH / SAGE PUBLICATIONS INC | 2156-8731 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4699 | EUROPEAN JOURNAL OF  ANAESTHESIOLOGY / LIPPINCOTT WILLIAMS & WILKINS | 1365-2346 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4700 | NATURE METHODS / NATURE PORTFOLIO | 1548-7105 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4701 | JOURNAL OF MANIPULATIVE AND  PHYSIOLOGICAL THERAPE / MOSBY-ELSEVIER | 1532-6586 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4702 | AUSTRALIAN SOCIAL WORK / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1447-0748 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4703 | REVIEW OF INCOME AND WEALTH / WILEY | 1475-4991 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4704 | NATURAL RESOURCES RESEARCH / SPRINGER | 1573-8981 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4705 | ZOOLOGY IN THE MIDDLE EAST / TAYLOR & FRANCIS LTD | 2326-2680 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4706 | TEXTILE HISTORY / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1743-2952 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4707 | COGNITIVE PSYCHOLOGY / ACADEMIC PRESS INC ELSEVIER  SCIENCE | 1095-5623 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4708 | Limnology and Oceanography Bulletin Wiley-Blackwel / Unknown | 1539-6088 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4709 | INTERNATIONAL POLITICAL SCIENCE  REVIEW / SAGE PUBLICATIONS LTD | 1460-373X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4710 | SEMINARS IN PLASTIC SURGERY / THIEME MEDICAL PUBL INC | 1536-0067 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4711 | BRAZILIAN JOURNAL OF  ANESTHESIOLOGY / ELSEVIER SCIENCE INC | 2352-2291 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4712 | JOURNAL OF ENHANCED HEAT  TRANSFER / BEGELL HOUSE INC | 1563-5074 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4713 | JOURNAL OF APPLIED RESEARCH IN  MEMORY AND COGNITI / AMER PSYCHOLOGICAL ASSOC | 2211-369X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4714 | FOUNDATIONS OF COMPUTATIONAL  MATHEMATICS / SPRINGER | 1615-3383 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4715 | American Political Thought University of Chicago P / Unknown | 2161-1599 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4716 | International Journal of Intelligent Robotics and  / Unknown | 2366-598X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4717 | International Journal of Water Inderscience Enterp / Unknown | 1741-5322 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4718 | Illinois Classical Studies University of Illinois  / Unknown | 2328-5265 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4719 | International Journal of Technoentrepreneurship In / Unknown | 1746-5389 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4720 | PEDIATRIC RESEARCH / SPRINGERNATURE | 1530-0447 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4721 | JOURNAL OF INVESTIGATIVE  DERMATOLOGY / ELSEVIER SCIENCE INC | 1523-1747 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4722 | GEOCHIMICA ET COSMOCHIMICA ACTA / PERGAMON-ELSEVIER SCIENCE LTD | 1872-9533 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4723 | GACETA SANITARIA / ELSEVIER | 1578-1283 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4724 | MOLECULAR CARCINOGENESIS / WILEY | 1098-2744 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4725 | PHILOSOPHICAL MAGAZINE LETTERS / TAYLOR & FRANCIS LTD | 1362-3036 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4726 | THERAPIE / ELSEVIER | 1958-5578 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4727 | PAEDAGOGICA HISTORICA / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1477-674X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4728 | NUCLEAR SCIENCE AND TECHNIQUES / SPRINGER SINGAPORE PTE LTD | 2210-3147 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4729 | EUROPEAN JOURNAL OF  PROTISTOLOGY / ELSEVIER GMBH | 1618-0429 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4730 | CURRENT ALZHEIMER RESEARCH / BENTHAM SCIENCE PUBL LTD | 1875-5828 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4731 | INTERNATIONAL JOURNAL OF  PSYCHIATRY IN MEDICINE / SAGE PUBLICATIONS INC | 1541-3527 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4732 | JOURNAL OF MANAGERIAL  PSYCHOLOGY / EMERALD GROUP PUBLISHING LTD | 1758-7778 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4733 | JOURNAL OF X-RAY SCIENCE AND  TECHNOLOGY / IOS PRESS | 1095-9114 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4734 | Counselling and Psychotherapy Research Wiley-Black / Unknown | 1746-1405 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4735 | PROCEEDINGS OF THE INSTITUTION OF  CIVIL ENGINEERS / EMERALD GROUP PUBLISHING LTD | 1751-7710 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4736 | Apeiron Walter de Gruyter GmbH / N°   ISSN   E-ISSN | 2156-7093 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4737 | HEALTH CARE ANALYSIS / SPRINGER | 1573-3394 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4738 | ASIAN ECONOMIC JOURNAL / WILEY | 1467-8381 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4739 | NEW REVIEW OF FILM AND TELEVISION  STUDIES / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1740-7923 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4740 | INTERNATIONAL JOURNAL OF  HYPERTENSION / WILEY | 2090-0392 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4741 | Natural Products and Bioprospecting Springer Singa / Unknown | 2192-2209 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4742 | International Journal of Manufacturing Research In / Unknown | 1750-0605 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4743 | POLITICS PHILOSOPHY & ECONOMICS / SAGE PUBLICATIONS INC | 1741-3060 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4744 | SPINE / LIPPINCOTT WILLIAMS & WILKINS | 1528-1159 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4745 | ASAIO JOURNAL / LIPPINCOTT WILLIAMS & WILKINS | 1538-943X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4746 | JOURNAL OF THE AMERICAN MEDICAL  DIRECTORS ASSOCIA / ELSEVIER SCIENCE INC | 1538-9375 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4747 | JOURNAL OF GASTROINTESTINAL  SURGERY / ELSEVIER SCIENCE INC | 1873-4626 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4748 | INTERNATIONAL JOURNAL FOR  PARASITOLOGY / ELSEVIER SCI LTD | 1879-0135 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4749 | APPLIED INTELLIGENCE / SPRINGER | 1573-7497 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4750 | JOURNAL OF THE AMERICAN  PHARMACISTS ASSOCIATION / ELSEVIER | 1544-3450 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4751 | Jahrbuch fur Wirtschaftsgeschichte Walter de Gruyt / Unknown | 2196-6842 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4752 | CURRENT OPINION IN  PHARMACOLOGY / ELSEVIER SCI LTD | 1471-4973 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4753 | TRANSLATIONAL LUNG CANCER  RESEARCH / AME PUBLISHING COMPANY | 2226-4477 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4754 | JOURNAL OF BIOPHARMACEUTICAL  STATISTICS / TAYLOR & FRANCIS INC | 1520-5711 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4755 | Value in Health Regional Issues Elsevier Inc. / Unknown | 2212-1102 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4756 | Journal of Basic and Clinical Physiology and Pharm / Unknown | 2191-0286 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4757 | SOUTH AFRICAN HISTORICAL JOURNAL / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1726-1686 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4758 | RUSSIAN JOURNAL OF MARINE  BIOLOGY / MAIK  NAUKA/INTERPERIODICA/SPRINGER | 1608-3377 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4759 | Antitrust Bulletin SAGE Publications Inc. / Unknown | 1930-7969 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4760 | MYCOBIOLOGY / TAYLOR & FRANCIS LTD | 2092-9323 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4761 | NBER MACROECONOMICS ANNUAL / UNIV CHICAGO PRESS | 1537-2642 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4762 | COGNITIVE PROCESSING / SPRINGER HEIDELBERG | 1612-4790 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4763 | Journal of Industrial and Business Economics Sprin / Unknown | 1972-4977 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4764 | European Journal of Political Theory SAGE Publicat / Unknown | 1741-2730 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4765 | USER MODELING AND USER-ADAPTED  INTERACTION / SPRINGER | 1573-1391 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4766 | INFORMATICS FOR HEALTH & SOCIAL  CARE / TAYLOR & FRANCIS INC | 1753-8165 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4767 | International Journal of Information Systems in th / Unknown | 1935-5696 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4768 | Palgrave Studies in Prisons and Penology Springer: / Unknown | 2753-0612 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4769 | Complex Psychiatry S. Karger AG / Unknown | 2673-3005 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4770 | SIAM JOURNAL ON MATHEMATICAL  ANALYSIS / SIAM PUBLICATIONS | 1095-7154 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4771 | SPECTROSCOPY LETTERS / TAYLOR & FRANCIS INC | 1532-2289 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4772 | JOURNAL OF GRAPH THEORY / WILEY | 1097-0118 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4773 | SOCIETY & NATURAL RESOURCES / TAYLOR & FRANCIS INC | 1521-0723 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4774 | JOURNAL OF THE NATIONAL MEDICAL  ASSOCIATION / ELSEVIER SCIENCE INC | 1943-4693 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4775 | SOCIAL COGNITIVE AND AFFECTIVE  NEUROSCIENCE / OXFORD UNIV PRESS | 1749-5024 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4776 | TOXICOLOGY RESEARCH / OXFORD UNIV PRESS | 2045-4538 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4777 | Polymer Science - Series D Pleiades Publishing / Unknown | 1995-4220 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4778 | HEALTH INFORMATION AND LIBRARIES  JOURNAL / WILEY | 1471-1842 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4779 | JAPANESE ECONOMIC REVIEW / SPRINGER HEIDELBERG | 1468-5876 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4780 | COLONIAL LATIN AMERICAN REVIEW / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1466-1802 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4781 | Interventional Cardiology Clinics Elsevier Inc. / N°   ISSN   E-ISSN | 2211-7466 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4782 | EUROPEAN PHYSICAL EDUCATION  REVIEW / SAGE PUBLICATIONS LTD | 1741-2749 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4783 | Review of Philosophy and Psychology Springer Verla / Unknown | 1878-5166 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4784 | PROGRESS IN CRYSTAL GROWTH AND  CHARACTERIZATION O / PERGAMON-ELSEVIER SCIENCE LTD | 1878-4208 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4785 | MODERNIST CULTURES / EDINBURGH UNIV PRESS | 2041-1022 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4786 | International Journal of Childbirth Springer Publi / Unknown | 2156-5295 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4787 | Minerva Dental and Oral Science Edizioni Minerva M / Unknown | 2724-6337 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4788 | JOURNAL OF QUANTITATIVE  SPECTROSCOPY & RADIATIVE  / PERGAMON-ELSEVIER SCIENCE LTD | 1879-1352 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4789 | ECOLOGICAL ECONOMICS / ELSEVIER | 1873-6106 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4790 | NUTRITION AND CANCER-AN  INTERNATIONAL JOURNAL / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1532-7914 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4791 | POTATO RESEARCH / SPRINGER | 1871-4528 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4792 | JOURNAL OF AGRICULTURAL  ECONOMICS / WILEY | 1477-9552 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4793 | JOURNAL OF THE AMERICAN SOCIETY  OF BREWING CHEMIS / TAYLOR & FRANCIS LTD | 1943-7854 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4794 | JOURNAL OF COMPARATIVE  ECONOMICS / ACADEMIC PRESS INC ELSEVIER  SCIENCE | 1095-7227 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4795 | JOURNAL OF THE KOREAN CERAMIC  SOCIETY / SPRINGER HEIDELBERG | 2234-0491 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4796 | PSYCHOANALYTIC DIALOGUES / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1940-9222 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4797 | TOPOI-AN INTERNATIONAL REVIEW OF  PHILOSOPHY / SPRINGER | 1572-8749 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4798 | COMMUNICATIONS IN  CONTEMPORARY MATHEMATICS / WORLD SCIENTIFIC PUBL CO PTE  LTD | 1793-6683 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4799 | FRENCH HISTORICAL STUDIES / DUKE UNIV PRESS | 1527-5493 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4800 | JOURNAL OF EXOTIC PET MEDICINE / ELSEVIER SCIENCE INC | 1931-6283 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4801 | JOURNAL OF RETAILING / ELSEVIER SCIENCE INC | 1873-3271 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4802 | JOURNAL OF SPECIAL EDUCATION  TECHNOLOGY / SAGE PUBLICATIONS INC | 2381-3121 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4803 | Parliaments, Estates and Representation Taylor and / Unknown | 1947-248X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4804 | POLIS / BRILL | 2051-2996 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4805 | EXTREMES / SPRINGER | 1572-915X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4806 | Obstetrics and Gynecology International John Wiley / N°   ISSN   E-ISSN | 1687-9597 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4807 | International Journal of Nanoparticles Inderscienc / Unknown | 1753-2515 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4808 | Composites: Mechanics, Computations, Applications  / Unknown | 2152-2073 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4809 | Journal of Environmental Economics and Policy Tayl / Unknown | 2160-6552 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4810 | Interest Groups and Advocacy Palgrave Macmillan Lt / Unknown | 2047-7422 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4811 | ATHEROSCLEROSIS PLUS / ELSEVIER | 2667-0909 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4812 | Ocean Systems Engineering Techno-Press / Unknown | 2093-677X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4813 | JOURNAL OF CHROMATOGRAPHY A / ELSEVIER | 1873-3778 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4814 | COLLOIDS AND SURFACES A- PHYSICOCHEMICAL AND ENGIN / ELSEVIER | 1873-4359 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4815 | JOURNAL OF EXPERIMENTAL BOTANY / OXFORD UNIV PRESS | 1460-2431 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4816 | COMPUTERS & CHEMICAL  ENGINEERING / PERGAMON-ELSEVIER SCIENCE LTD | 1873-4375 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4817 | MOLECULAR BIOLOGY AND  EVOLUTION / OXFORD UNIV PRESS | 1537-1719 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4818 | AESTHETIC SURGERY JOURNAL / OXFORD UNIV PRESS INC | 1527-330X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4819 | EUROPEAN PHYSICAL JOURNAL- SPECIAL TOPICS / SPRINGER HEIDELBERG | 1951-6401 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4820 | TRANSPORTATION RESEARCH PART A- POLICY AND PRACTIC / PERGAMON-ELSEVIER SCIENCE LTD | 1879-2375 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4821 | JOURNAL OF LOSS PREVENTION IN THE  PROCESS INDUSTR / ELSEVIER SCI LTD | 1873-3352 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4822 | ACTA HISTOCHEMICA / ELSEVIER GMBH | 1618-0372 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4823 | PRIMARY CARE / W B SAUNDERS CO-ELSEVIER INC | 1558-299X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4824 | VIOLENCE AGAINST WOMEN / SAGE PUBLICATIONS INC | 1552-8448 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4825 | NEW ZEALAND JOURNAL OF CROP AND  HORTICULTURAL SCI / TAYLOR & FRANCIS LTD | 1175-8783 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4826 | REVISTA DE LA REAL ACADEMIA DE  CIENCIAS EXACTAS F / SPRINGER-VERLAG ITALIA SRL | 1579-1505 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4827 | Medical Journal of Babylon Wolters Kluwer Medknow  / Unknown | 2312-6760 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4828 | DENDROCHRONOLOGIA / ELSEVIER GMBH | 1612-0051 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4829 | JOURNAL OF SPORT & SOCIAL ISSUES / SAGE PUBLICATIONS INC | 1552-7638 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4830 | ATTACHMENT & HUMAN  DEVELOPMENT / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1469-2988 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4831 | ARID LAND RESEARCH AND  MANAGEMENT / TAYLOR & FRANCIS INC | 1532-4990 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4832 | Religion and Education Taylor and Francis Ltd. / N°   ISSN   E-ISSN | 1949-8381 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4833 | PharmacoEconomics - Open Springer International Pu / Unknown | 2509-4262 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4834 | International Journal of Human Rights in Healthcar / Unknown | 2056-4910 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4835 | PEDIATRIC CLINICS OF NORTH  AMERICA / W B SAUNDERS CO-ELSEVIER INC | 1557-8240 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4836 | NATURAL PRODUCT  COMMUNICATIONS / SAGE PUBLICATIONS INC | 1934-578X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4837 | ZOOLOGICAL JOURNAL OF THE  LINNEAN SOCIETY / OXFORD UNIV PRESS | 1096-3642 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4838 | ABDOMINAL RADIOLOGY / SPRINGER | 2366-0058 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4839 | ACTA PHARMACOLOGICA SINICA / NATURE PUBL GROUP | 1745-7254 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4840 | METABOLIC BRAIN DISEASE / SPRINGER/PLENUM PUBLISHERS | 1573-7365 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4841 | JOURNAL OF SYSTEMS ARCHITECTURE / ELSEVIER | 1873-6165 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4842 | STATISTICS / TAYLOR & FRANCIS LTD | 1029-4910 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4843 | Optoelectronics Letters Springer Verlag / Unknown | 1993-5013 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4844 | SOCIOLOGY OF RELIGION / OXFORD UNIV PRESS INC | 1759-8818 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4845 | SOIL RESEARCH / CSIRO PUBLISHING | 1838-6768 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4846 | DRUG METABOLISM REVIEWS / TAYLOR & FRANCIS LTD | 1097-9883 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4847 | INTERNATIONAL JOURNAL OF TURBO &  JET-ENGINES / WALTER DE GRUYTER GMBH | 2191-0332 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4848 | Annali dell'Universita di Ferrara Springer-Verlag  / Unknown | 1827-1510 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4849 | GROUP DECISION AND NEGOTIATION / SPRINGER | 1572-9907 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4850 | AZANIA-ARCHAEOLOGICAL RESEARCH  IN AFRICA / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1945-5534 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4851 | ANNALS OF DYSLEXIA / SPRINGER | 1934-7243 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4852 | HYPERTENSION IN PREGNANCY / TAYLOR & FRANCIS INC | 1525-6065 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4853 | Journal of Nursing Measurement Springer Publishing / Unknown | 1945-7049 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4854 | Journal of Clinical Neuromuscular Disease Lippinco / Unknown | 1537-1611 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4855 | KANTIAN REVIEW / CAMBRIDGE UNIV PRESS | 2044-2394 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4856 | Frontiers of Law in China Higher Education Press L / Unknown | 1673-3541 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4857 | Bioelectricity Mary Ann Liebert Inc. / Unknown | 2576-3113 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4858 | Computability SAGE Publications Ltd / Unknown | 2211-3576 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4859 | CCF Transactions on High Performance Computing Spr / Unknown | 2524-4930 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4860 | JOURNAL OF THE ATMOSPHERIC  SCIENCES / AMER METEOROLOGICAL SOC | 1520-0469 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4861 | CELLULOSE / SPRINGER | 1572-882X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4862 | SCOTTISH MEDICAL JOURNAL / SAGE PUBLICATIONS LTD | 2045-6441 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4863 | EXPLICATOR / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1939-926X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4864 | INTERNATIONAL JOURNAL OF  NURSING STUDIES / PERGAMON-ELSEVIER SCIENCE LTD | 1873-491X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4865 | MENDELEEV COMMUNICATIONS / ELSEVIER | 1364-551X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4866 | Aktuelle Ernahrungsmedizin Klinik und Praxis Georg / Unknown | 1438-9916 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4867 | AMERICAN JOURNAL ON ADDICTIONS / WILEY | 1521-0391 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4868 | TWIN RESEARCH AND HUMAN  GENETICS / CAMBRIDGE UNIV PRESS | 1839-2628 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4869 | FOLIA LINGUISTICA / WALTER DE GRUYTER GMBH | 1614-7308 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4870 | PERSPECTIVES IN PUBLIC HEALTH / SAGE PUBLICATIONS LTD | 1757-9147 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4871 | JOURNAL OF MOLECULAR HISTOLOGY / SPRINGER | 1567-2387 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4872 | SOCIAL DEVELOPMENT / WILEY | 1467-9507 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4873 | JOURNAL OF MEDICAL SCREENING / SAGE PUBLICATIONS LTD | 1475-5793 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4874 | JOURNAL OF CHILD SEXUAL ABUSE / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1547-0679 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4875 | JOURNAL OF FRENCH LANGUAGE  STUDIES / CAMBRIDGE UNIV PRESS | 1474-0079 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4876 | ASSAY AND DRUG DEVELOPMENT  TECHNOLOGIES / MARY ANN LIEBERT, INC | 1557-8127 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4877 | NANOTECHNOLOGY REVIEWS / DE GRUYTER POLAND SP Z O O | 2191-9097 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4878 | PHENOMENOLOGY AND THE  COGNITIVE SCIENCES / SPRINGER | 1572-8676 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4879 | South Asia Research Sage Publications India Pvt. L / N°   ISSN   E-ISSN | 1741-3141 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4880 | Radiological Physics and Technology Springer Japan / Unknown | 1865-0341 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4881 | MAIN GROUP CHEMISTRY / IOS PRESS | 1745-1167 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4882 | Advances in Radio Science Copernicus Publications / Unknown | 1684-9973 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4883 | Intractable and Rare Diseases Research Internation / Unknown | 2186-3644 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4884 | International Journal of Enterprise Information Sy / Unknown | 1548-1123 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4885 | Avicenna Journal of Clinical Microbiology and Infe / Unknown | 2383-0301 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4886 | Manuscript Studies University of Pennsylvania Pres / Unknown | 2381-5329 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4887 | JOURNAL OF VIROLOGY / AMER SOC MICROBIOLOGY | 1098-5514 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4888 | EPILEPSIA / WILEY | 1528-1167 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4889 | JOURNAL OF THE LONDON  MATHEMATICAL SOCIETY-SECOND / WILEY | 1469-7750 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4890 | MATERIALS CHARACTERIZATION / ELSEVIER SCIENCE INC | 1873-4189 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4891 | ZEITSCHRIFT FUR SLAWISTIK / WALTER DE GRUYTER GMBH | 2196-7016 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4892 | Agricultural Engineering De Gruyter Open Ltd. / Unknown | 2449-5999 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4893 | INTERNATIONAL JOURNAL OF  ACAROLOGY / TAYLOR & FRANCIS INC | 1945-3892 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4894 | PSYCHOTHERAPY RESEARCH / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1468-4381 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4895 | INTEGRAL TRANSFORMS AND SPECIAL  FUNCTIONS / TAYLOR & FRANCIS LTD | 1476-8291 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4896 | E-POLYMERS / DE GRUYTER POLAND SP Z O O | 2197-4586 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4897 | INTERNATIONAL REVIEW FOR THE  SOCIOLOGY OF SPORT / SAGE PUBLICATIONS LTD | 1461-7218 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4898 | COGNITIVE DEVELOPMENT / ELSEVIER SCIENCE INC | 1879-226X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4899 | POLITICAL COMMUNICATION / TAYLOR & FRANCIS INC | 1091-7675 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4900 | CHEMICAL AND PROCESS  ENGINEERING-NEW FRONTIERS / POLSKA AKAD NAUK, POLISH ACAD  SCIENCES | 2300-1925 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4901 | INTERNATIONAL JOURNAL OF SOCIAL  PSYCHOLOGY / SAGE PUBLICATIONS INC | 1579-3680 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4902 | SCHOOL MENTAL HEALTH / SPRINGER | 1866-2633 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4903 | FOLIA HORTICULTURAE / SCIENDO | 2083-5965 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4904 | RESEARCH IN ENGINEERING DESIGN / SPRINGER HEIDELBERG | 1435-6066 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4905 | Journal of Obstetrics, Gynecology and Cancer Resea / Unknown | 2645-3991 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4906 | RIVISTA DEL NUOVO CIMENTO / SPRINGERNATURE | 1826-9850 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4907 | New Journal of European Criminal Law SAGE Publicat / Unknown | 2399-293X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4908 | International Journal of Disaster Resilience in th / Unknown | 1759-5916 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4909 | Advances in Human-Computer Interaction John Wiley  / N°   ISSN   E-ISSN | 1687-5907 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4910 | Urban Rail Transit Springer Science and Business M / Unknown | 2199-6687 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4911 | JOURNAL OF LANGUAGE LITERATURE  AND CULTURE / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 2051-2864 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4912 | CHROMATOGRAPHIA / SPRINGER HEIDELBERG | 1612-1112 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4913 | GERIATRIC NURSING / MOSBY-ELSEVIER | 1528-3984 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4914 | IMMUNOBIOLOGY / ELSEVIER GMBH | 1878-3279 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4915 | ETHNIC AND RACIAL STUDIES / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1466-4356 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4916 | JOURNAL OF BIOLOGICAL EDUCATION / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 2157-6009 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4917 | COGNITION & EMOTION / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1464-0600 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4918 | JOURNAL OF OCCUPATIONAL HEALTH / OXFORD UNIV PRESS | 1348-9585 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4919 | GENES TO CELLS / WILEY | 1365-2443 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4920 | JOURNAL OF HYDROMETEOROLOGY / AMER METEOROLOGICAL SOC | 1525-755X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4921 | JOURNAL OF MUSCLE RESEARCH AND  CELL MOTILITY / SPRINGER | 1573-2657 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4922 | PALAEONTOLOGY / WILEY | 1475-4983 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4923 | EUROPEAN JOURNAL OF  INTERNATIONAL MANAGEMENT / INDERSCIENCE ENTERPRISES LTD | 1751-6765 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4924 | Journal of Patient Experience SAGE Publications In / Unknown | 2374-3743 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4925 | VIRTUAL AND PHYSICAL PROTOTYPING / TAYLOR & FRANCIS LTD | 1745-2767 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4926 | Behaviour Change Cambridge University Press / Unknown | 2049-7768 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4927 | RENEWABLE AGRICULTURE AND FOOD  SYSTEMS / CAMBRIDGE UNIV PRESS | 1742-1713 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4928 | BEN JONSON JOURNAL / EDINBURGH UNIV PRESS | 1755-165X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4929 | INTERNATIONAL JOURNAL OF  HOUSING POLICY / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1949-1255 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4930 | INTERNATIONAL JOURNAL OF ORAL  SCIENCE / SPRINGERNATURE | 2049-3169 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4931 | Journal of High Speed Networks SAGE Publications L / Unknown | 1875-8940 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4932 | International Journal of Engineering Systems Model / Unknown | 1755-9766 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4933 | International Journal of Electronic Marketing and  / Unknown | 1741-1033 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4934 | WSEAS Transactions on Power Systems World Scientif / Unknown | 2224-350X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4935 | International Journal of Revenue Management Inders / Unknown | 1741-8186 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4936 | CHEST / ELSEVIER | 1931-3543 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4937 | WATER SCIENCE AND TECHNOLOGY / IWA PUBLISHING | 1996-9732 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4938 | JOURNAL OF GEOLOGY / UNIV CHICAGO PRESS | 1537-5269 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4939 | CHEMICAL SOCIETY REVIEWS / ROYAL SOC CHEMISTRY | 1460-4744 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4940 | CANCER IMMUNOLOGY RESEARCH / AMER ASSOC CANCER RESEARCH | 2326-6074 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4941 | NEW ZEALAND JOURNAL OF BOTANY / TAYLOR & FRANCIS LTD | 1175-8643 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4942 | HISTORY OF PHOTOGRAPHY / TAYLOR & FRANCIS LTD | 2150-7295 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4943 | MOLECULAR DIVERSITY / SPRINGER | 1573-501X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4944 | CAMBRIDGE QUARTERLY OF  HEALTHCARE ETHICS / CAMBRIDGE UNIV PRESS | 1469-2147 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4945 | TRANSACTIONS OF THE PHILOLOGICAL  SOCIETY / WILEY | 1467-968X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4946 | JOURNAL OF FIELD ROBOTICS / WILEY | 1556-4967 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4947 | POETICS / ELSEVIER | 1872-7514 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4948 | PEDIATRIC OBESITY / WILEY | 2047-6310 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4949 | Arbitration International Oxford University Press / Unknown | 1875-8398 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4950 | JOURNAL OF RESEARCH IN CRIME AND  DELINQUENCY / SAGE PUBLICATIONS INC | 1552-731X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4951 | JOURNAL OF MATHEMATICAL FLUID  MECHANICS / SPRINGER BASEL AG | 1422-6952 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4952 | RACE ETHNICITY AND EDUCATION / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1470-109X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4953 | JOURNAL OF APPLIED SPORT  PSYCHOLOGY / TAYLOR & FRANCIS LTD | 1533-1571 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4954 | HISTORY OF PSYCHOLOGY / EDUCATIONAL PUBLISHING  FOUNDATION-AMERI | 1939-0610 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4955 | PROGRESS IN PLANNING / PERGAMON-ELSEVIER SCIENCE LTD | 1873-4510 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4956 | Journal of Defense Modeling and Simulation SAGE Pu / Unknown | 1557-380X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4957 | ACTA ORIENTALIA ACADEMIAE  SCIENTIARUM HUNGARICAE / AKADEMIAI KIADO ZRT | 1588-2667 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4958 | International Journal of Innovation Science Emeral / Unknown | 1757-2231 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4959 | International Journal of Cloud Computing Inderscie / Unknown | 2043-9997 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4960 | Therapeutic Advances in Cardiovascular Disease SAG / Unknown | 1753-9455 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4961 | Information and Learning Science Emerald Publishin / Unknown | 2398-5356 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4962 | Pulmonary Therapy Adis / Unknown | 2364-1754 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4963 | Agriculture (Pol'nohospodarstvo) Sciendo / Unknown | 1338-4376 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4964 | Studies in Graduate and Postdoctoral Education Eme / Unknown | 2398-4694 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4965 | AMERICAN HISTORICAL REVIEW / OXFORD UNIV PRESS | 1937-5239 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4966 | EUROPEAN JOURNAL OF CANCER / ELSEVIER SCI LTD | 1879-0852 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4967 | ECOLOGY / WILEY | 1939-9170 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4968 | HEALTH EDUCATION JOURNAL / SAGE PUBLICATIONS LTD | 1748-8176 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4969 | JOURNAL OF GENERAL PSYCHOLOGY / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1940-0888 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4970 | ARCHIVES OF INSECT BIOCHEMISTRY  AND PHYSIOLOGY / WILEY | 1520-6327 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4971 | NANO TODAY / ELSEVIER SCI LTD | 1878-044X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4972 | CHINA ECONOMIC REVIEW / ELSEVIER SCIENCE INC | 1873-7781 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4973 | INTERNATIONAL JOURNAL OF  IMMUNOPATHOLOGY AND  PHA / SAGE PUBLICATIONS INC | 2058-7384 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4974 | JOURNALISM / SAGE PUBLICATIONS INC | 1741-3001 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4975 | CURRENT HYPERTENSION REPORTS / SPRINGER | 1534-3111 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4976 | SHIPS AND OFFSHORE STRUCTURES / TAYLOR & FRANCIS LTD | 1754-212X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4977 | JOURNAL OF VETERINARY MEDICAL  EDUCATION / UNIV TORONTO PRESS INC | 1943-7218 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4978 | DRUG DELIVERY AND TRANSLATIONAL  RESEARCH / SPRINGER HEIDELBERG | 2190-3948 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4979 | SCOTTISH HISTORICAL REVIEW / EDINBURGH UNIV PRESS | 1750-0222 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4980 | Reflective Practice Taylor and Francis Ltd. / Unknown | 1470-1103 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4981 | Foresight Emerald Publishing / Unknown | 1465-9832 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4982 | International Journal of Information Technology an / Unknown | 2074-9015 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4983 | Applied Microscopy Springer Nature / Unknown | 2287-5123 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4984 | Journal of Herbs, Spices and Medicinal Plants Tayl / Unknown | 1540-3580 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4985 | GAMES AND CULTURE / SAGE PUBLICATIONS INC | 1555-4139 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4986 | ANTHROPOLOGICAL THEORY / SAGE PUBLICATIONS LTD | 1741-2641 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4987 | INTERNATIONAL JOURNAL OF CLINICAL  AND HEALTH PSYC / ELSEVIER SCIENCE INC | 2174-0852 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4988 | Speech, Language and Hearing Taylor and Francis Lt / Unknown | 2050-5728 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4989 | Advances in Urology John Wiley and Sons Ltd / Unknown | 1687-6377 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4990 | ACTA GEODAETICA ET GEOPHYSICA / SPRINGER | 2213-5820 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4991 | ALGEBRAIC GEOMETRY / EUROPEAN MATHEMATICAL SOC- EMS | 2313-1691 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4992 | Theatre and Performance Design Taylor and Francis  / Unknown | 2332-2578 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4993 | JOURNAL OF EDUCATIONAL  PSYCHOLOGY / AMER PSYCHOLOGICAL ASSOC | 1939-2176 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4994 | ECONOMETRIC REVIEWS / TAYLOR & FRANCIS INC | 1532-4168 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4995 | THEORETICAL AND APPLIED FRACTURE  MECHANICS / ELSEVIER | 1872-7638 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4996 | CLINICAL AND EXPERIMENTAL  OPHTHALMOLOGY / WILEY | 1442-9071 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4997 | Intereconomics Sciendo / Unknown | 1613-964X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4998 | SCANDINAVIAN JOURNAL OF  PSYCHOLOGY / WILEY | 1467-9450 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 4999 | COMPUTER STANDARDS & INTERFACES / ELSEVIER | 1872-7018 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5000 | JOURNAL OF MEDICAL PRIMATOLOGY / WILEY | 1600-0684 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5001 | STRUCTURAL HEALTH MONITORING- AN INTERNATIONAL JOU / SAGE PUBLICATIONS LTD | 1741-3168 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5002 | Politics and the Life Sciences Cambridge Universit / Unknown | 1471-5457 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5003 | Urology Practice Lippincott Williams and Wilkins / Unknown | 2352-0787 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5004 | STRUCTURAL CHANGE AND ECONOMIC  DYNAMICS / ELSEVIER | 1873-6017 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5005 | ORGANIZATION / SAGE PUBLICATIONS LTD | 1461-7323 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5006 | AMERICAN BUSINESS LAW JOURNAL / WILEY | 1744-1714 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5007 | AUSTRALIAN FEMINIST STUDIES / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1465-3303 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5008 | Criminal Justice Policy Review SAGE Publications I / Unknown | 1552-3586 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5009 | ADVANCED FIBER MATERIALS / SPRINGERNATURE | 2524-793X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5010 | Psychology of Consciousness: Theory Research, and  / Unknown | 2326-5531 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5011 | Journal of Eastern Mediterranean Archaeology and H / Unknown | 2166-3556 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5012 | INTERNATIONAL JOURNAL OF SYSTEMS  SCIENCE-OPERATIO / TAYLOR & FRANCIS LTD | 2330-2682 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5013 | Global Journal of Emerging Market Economies SAGE P / Unknown | 0975-2730 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5014 | Phenomics Springer / Unknown | 2730-5848 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5015 | EUROPEAN JOURNAL OF  ENDOCRINOLOGY / OXFORD UNIV PRESS | 1479-683X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5016 | CHEMICAL PHYSICS / ELSEVIER | 1873-4421 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5017 | CHEMOTHERAPY / KARGER | 1421-9794 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5018 | CALCIFIED TISSUE INTERNATIONAL / SPRINGER | 1432-0827 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5019 | AEU-INTERNATIONAL JOURNAL OF  ELECTRONICS AND COMM / ELSEVIER GMBH | 1618-0399 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5020 | SIGNAL PROCESSING-IMAGE  COMMUNICATION / ELSEVIER | 1879-2677 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5021 | PHYSIOLOGICAL RESEARCH / ACAD SCIENCES CZECH REPUBLIC,  INST PHYS | 1802-9973 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5022 | JOURNAL OF KNOT THEORY AND ITS  RAMIFICATIONS / WORLD SCIENTIFIC PUBL CO PTE  LTD | 1793-6527 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5023 | CHILD & YOUTH CARE FORUM / SPRINGER | 1573-3319 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5024 | Economic Research-Ekonomska Istrazivanja Taylor an / Unknown | 1848-9664 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5025 | CHINESE GEOGRAPHICAL SCIENCE / SPRINGER | 1993-064X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5026 | CHINA INFORMATION / SAGE PUBLICATIONS INC | 1741-590X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5027 | Journal of Clinical Ethics University of Chicago P / Unknown | 1945-5879 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5028 | Review of Black Political Economy Springer New Yor / N°   ISSN   E-ISSN | 1936-4814 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5029 | ATOMIC DATA AND NUCLEAR DATA  TABLES / ACADEMIC PRESS INC ELSEVIER  SCIENCE | 1090-2090 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5030 | JOURNAL OF ENVIRONMENTAL LAW / OXFORD UNIV PRESS | 1464-374X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5031 | INTERNATIONAL JOURNAL OF HIGH  PERFORMANCE COMPUTI / SAGE PUBLICATIONS LTD | 1741-2846 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5032 | ASSESSING WRITING / ELSEVIER SCI LTD | 1873-5916 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5033 | THERAPEUTIC ADVANCES IN  RESPIRATORY DISEASE / SAGE PUBLICATIONS LTD | 1753-4666 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5034 | APPLIED FRUIT SCIENCE / SPRINGER | 2948-2631 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5035 | Electronic Government Inderscience Enterprises Ltd / Unknown | 1740-7508 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5036 | MARKETING THEORY / SAGE PUBLICATIONS INC | 1741-301X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5037 | Review of Law and Economics Walter de Gruyter GmbH / Unknown | 2194-6000 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5038 | International Journal of Vehicle Noise and Vibrati / Unknown | 1479-148X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5039 | International Journal of Accounting World Scientif / Unknown | 2213-3933 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5040 | Journal of Property, Planning and Environmental La / N°   ISSN   E-ISSN | 2514-9415 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5041 | JOURNAL OF PEDIATRIC  GASTROENTEROLOGY AND NUTRITI / WILEY | 1536-4801 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5042 | CLINICAL CANCER RESEARCH / AMER ASSOC CANCER RESEARCH | 1557-3265 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5043 | Measurement Techniques Springer Science and Busine / Unknown | 1573-8906 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5044 | Feddes Repertorium Wiley-Blackwell / Unknown | 1522-239X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5045 | ART JOURNAL / TAYLOR & FRANCIS INC | 2325-5307 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5046 | ANTICANCER RESEARCH / INT INST ANTICANCER RESEARCH | 1791-7530 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5047 | JOURNAL OF MARRIAGE AND FAMILY / WILEY | 1741-3737 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5048 | TRANSLATIONAL CANCER RESEARCH / AME PUBLISHING COMPANY | 2219-6803 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5049 | CANADIAN MATHEMATICAL BULLETIN- BULLETIN CANADIEN  / CAMBRIDGE UNIV PRESS | 1496-4287 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5050 | CHRONOBIOLOGY INTERNATIONAL / TAYLOR & FRANCIS INC | 1525-6073 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5051 | JOURNAL OF THROMBOSIS AND  THROMBOLYSIS / SPRINGER | 1573-742X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5052 | APIDOLOGIE / SPRINGER FRANCE | 1297-9678 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5053 | SCIENCE & EDUCATION / SPRINGER | 1573-1901 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5054 | ASTIN BULLETIN-THE JOURNAL OF THE  INTERNATIONAL A / CAMBRIDGE UNIV PRESS | 1783-1350 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5055 | JOURNAL OF INFORMETRICS / ELSEVIER | 1875-5879 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5056 | JOURNAL OF AGRICULTURAL  BIOLOGICAL AND ENVIRONMEN / SPRINGER | 1537-2693 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5057 | REVIEWS OF ENVIRONMENTAL  CONTAMINATION AND TOXICO / SPRINGER | 2197-6554 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5058 | SCHOOL EFFECTIVENESS AND SCHOOL  IMPROVEMENT / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1744-5124 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5059 | JOURNAL OF SERVICE RESEARCH / SAGE PUBLICATIONS INC | 1552-7379 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5060 | Indian Journal of Microbiology Research IP Innovat / Unknown | 2394-5478 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5061 | CHINA FOUNDRY / SPRINGER SINGAPORE PTE LTD | 2365-9459 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5062 | Legal Theory Cambridge University Press / Unknown | 1469-8048 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5063 | INFORMATION TECHNOLOGY &  MANAGEMENT / SPRINGER | 1573-7667 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5064 | International Journal of Christianity and Educatio / Unknown | 2056-998X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5065 | INTERNATIONAL DATA PRIVACY LAW / OXFORD UNIV PRESS | 2044-4001 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5066 | Cybernetics and Physics Institute of Problems of M / Unknown | 2226-4116 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5067 | HIV RESEARCH & CLINICAL PRACTICE / TAYLOR & FRANCIS LTD | 2578-7489 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5068 | Muslim World Journal of Human Rights Walter de Gru / Unknown | 2194-6558 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5069 | JOURNAL OF THE FRANKLIN INSTITUTE / PERGAMON-ELSEVIER SCIENCE LTD | 1879-2693 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5070 | School Science and Mathematics John Wiley & Sons I / Unknown | 1949-8594 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5071 | CANADIAN JOURNAL OF FISHERIES  AND AQUATIC SCIENCE / CANADIAN SCIENCE PUBLISHING | 1205-7533 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5072 | MRS BULLETIN / SPRINGER HEIDELBERG | 1938-1425 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5073 | JOURNAL OF CHILD PSYCHOLOGY AND  PSYCHIATRY / WILEY | 1469-7610 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5074 | JOURNAL OF ETHNIC AND MIGRATION  STUDIES / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1469-9451 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5075 | INTERNATIONAL JOURNAL OF URBAN  AND REGIONAL RESEA / WILEY | 1468-2427 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5076 | JOURNAL OF MOUNTAIN SCIENCE / SCIENCE PRESS | 1993-0321 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5077 | GEOGRAPHICAL RESEARCH / WILEY | 1745-5871 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5078 | REGIONAL SCIENCE AND URBAN  ECONOMICS / ELSEVIER | 1879-2308 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5079 | AUSTRALIAN JOURNAL OF PRIMARY  HEALTH / CSIRO PUBLISHING | 1836-7399 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5080 | POSITIVITY / SPRINGER | 1572-9281 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5081 | JOURNAL OF BIOLOGICAL SYSTEMS / WORLD SCIENTIFIC PUBL CO PTE  LTD | 1793-6470 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5082 | Revista de Filologia de la Universidad de La Lagun / Unknown | 2530-8548 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5083 | BENEFICIAL MICROBES / BRILL | 1876-2891 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5084 | QUARTERLY REVIEWS OF BIOPHYSICS / CAMBRIDGE UNIV PRESS | 1469-8994 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5085 | AFTERALL / UNIV CHICAGO PRESS | 2156-4914 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5086 | International Journal of Self-Propagating High-Tem / Unknown | 1934-788X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5087 | ANNUAL REVIEW OF APPLIED  LINGUISTICS / CAMBRIDGE UNIV PRESS | 1471-6356 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5088 | JOURNAL OF AMBIENT INTELLIGENCE  AND SMART ENVIRON / IOS PRESS | 1876-1372 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5089 | Gender Issues Springer New York / Unknown | 1936-4717 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5090 | Unmanned Systems World Scientific / Unknown | 2301-3869 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5091 | Pacific Accounting Review Emerald Group Publishing / Unknown | 2041-5494 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5092 | REVISTA ROMANA DE MEDICINA DE  LABORATOR / SCIENDO | 2284-5623 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5093 | Archives of Mental Health Wolters Kluwer Medknow P / Unknown | 2589-918X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5094 | Journal of Planning History SAGE Publications Inc. / Unknown | 1552-6585 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5095 | AMERICAN JOURNAL OF CULTURAL  SOCIOLOGY / PALGRAVE MACMILLAN LTD | 2049-7121 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5096 | Korean Language in America Penn State University P / Unknown | 2374-670X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5097 | MAYO CLINIC PROCEEDINGS / ELSEVIER SCIENCE INC | 1942-5546 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5098 | JOURNAL OF THE OPERATIONAL  RESEARCH SOCIETY / TAYLOR & FRANCIS LTD | 1476-9360 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5099 | OBESITY SURGERY / SPRINGER | 1708-0428 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5100 | CRYSTAL RESEARCH AND TECHNOLOGY / WILEY-V C H VERLAG GMBH | 1521-4079 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5101 | EUROPEAN JOURNAL OF INTERNAL  MEDICINE / ELSEVIER | 1879-0828 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5102 | LINGUA / ELSEVIER | 1872-6135 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5103 | CRITICAL REVIEWS IN FOOD SCIENCE  AND NUTRITION / TAYLOR & FRANCIS INC | 1549-7852 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5104 | NEW ZEALAND VETERINARY JOURNAL / TAYLOR & FRANCIS LTD | 1176-0710 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5105 | COLD REGIONS SCIENCE AND  TECHNOLOGY / ELSEVIER | 1872-7441 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5106 | CANADIAN GEOGRAPHIES- GEOGRAPHIES CANADIENNES / WILEY | 1541-0064 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5107 | FEMINIST REVIEW / SAGE PUBLICATIONS LTD | 1466-4380 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5108 | MELUS / OXFORD UNIV PRESS INC | 1946-3170 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5109 | JOURNAL OF RELIGION IN AFRICA / BRILL | 1570-0666 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5110 | JOURNAL OF HAPPINESS STUDIES / SPRINGER | 1573-7780 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5111 | American Journal of Lifestyle Medicine SAGE Public / Unknown | 1559-8284 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5112 | Journal of Law and Religion Cambridge University P / Unknown | 2163-3088 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5113 | World Leisure Journal Taylor and Francis Ltd. / Unknown | 2333-4509 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5114 | Administrative Theory and Praxis Taylor and Franci / N°   ISSN   E-ISSN | 1949-0461 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5115 | PROCEEDINGS OF THE INSTITUTION OF  CIVIL ENGINEERS / EMERALD GROUP PUBLISHING LTD | 1751-7729 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5116 | ENVIRONMENTAL ARCHAEOLOGY / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1749-6314 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5117 | DIFFERENCES-A JOURNAL OF FEMINIST  CULTURAL STUDIE / DUKE UNIV PRESS | 1527-1986 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5118 | EVOLVING SYSTEMS / SPRINGER HEIDELBERG | 1868-6486 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5119 | International Journal of Knowledge Management Stud / Unknown | 1743-8276 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5120 | Studia Poliana / Unknown | 2387-1822 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5121 | Anesthesiology Research and Practice John Wiley an / Unknown | 1687-6970 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5122 | AMS Review Springer New York / N°   ISSN   E-ISSN | 1869-8182 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5123 | JOURNAL OF COMPUTER LANGUAGES / ELSEVIER SCI LTD | 2665-9182 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5124 | Studies in International Criminal Law Brill / Unknown | 2666-903X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5125 | MOLECULAR NUTRITION & FOOD  RESEARCH / WILEY | 1613-4125 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5126 | AMBIO / SPRINGER | 0044-7447 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5127 | JOURNAL OF PRODUCT INNOVATION  MANAGEMENT / WILEY | 0737-6782 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5128 | Revista Mexicana de Ciencias Agricolas National In / Unknown | 2007-9230 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5129 | PERFORMANCE RESEARCH / TAYLOR & FRANCIS LTD | 1352-8165 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5130 | ARCHIVES OF NATURAL HISTORY / EDINBURGH UNIV PRESS | 0260-9541 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5131 | BMC MEDICAL IMAGING / BMC | 1471-2342 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5132 | Gigiena i Sanitariya Federal Scientific Center of  / Unknown | 2412-0650 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5133 | Financial and Credit Activity: Problems of Theory  / Unknown | 2306-4994 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5134 | ELEMENTS / MINERALOGICAL SOC AMER | 1811-5217 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5135 | ALLERGOLOGY INTERNATIONAL / JAPANESE SOC ALLERGOLOGY | 1440-1592 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5136 | Personal and Ubiquitous Computing Springer London / Unknown | 1617-4909 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5137 | Journal of Disaster Research Fuji Technology Press / Unknown | 1883-8030 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5138 | BRITISH ACCOUNTING REVIEW / ELSEVIER SCI LTD | 0890-8389 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5139 | JOURNAL OF HUMAN KINETICS / TERMEDIA PUBLISHING HOUSE LTD | 1640-5544 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5140 | JMV-Journal de Medecine Vasculaire Elsevier Masson / Unknown | 2542-4513 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5141 | JOURNAL OF ECUMENICAL STUDIES / JOURNAL ECUMENICAL STUDIES | 2162-3937 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5142 | Jisuanji Xuebao/Chinese Journal of Computers Scien / Unknown | 0254-4164 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5143 | GROUP & ORGANIZATION  MANAGEMENT / SAGE PUBLICATIONS INC | 1059-6011 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5144 | ACM TRANSACTIONS ON SENSOR  NETWORKS / ASSOC COMPUTING MACHINERY | 1550-4859 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5145 | JOURNAL OF PHYSICAL AND CHEMICAL  REFERENCE DATA / AIP PUBLISHING | 0047-2689 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5146 | GESTA-INTERNATIONAL CENTER OF  MEDIEVAL ART / UNIV CHICAGO PRESS | 0016-920X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5147 | JOURNAL OF INTELLECTUAL  DISABILITIES / SAGE PUBLICATIONS LTD | 1744-6295 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5148 | ICHNOS-AN INTERNATIONAL JOURNAL  FOR PLANT AND ANI / TAYLOR & FRANCIS INC | 1042-0940 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5149 | Journal of Oral Research Universidad de Concepcion / Unknown | 0719-2479 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5150 | Global Social Policy SAGE Publications Ltd / Unknown | 1468-0181 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5151 | RHEUMATOLOGY AND THERAPY / SPRINGER | 2198-6576 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5152 | Functiones et Approximatio, Commentarii Mathematic / Unknown | 2080-9433 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5153 | Turkish Journal of Surgery Turkish Surgical Societ / Unknown | 2564-7032 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5154 | Asian Journal of International Law Cambridge Unive / Unknown | 2044-2513 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5155 | Journal of Parasitology Research John Wiley and So / Unknown | 2090-0023 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5156 | Rozhledy v Chirurgii Czech Medical Association J.E / Unknown | 1805-4579 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5157 | International Journal of Informatics and Communica / Unknown | 2722-2616 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5158 | Agronomia Colombiana Universidad Nacional de Colom / Unknown | 2357-3732 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5159 | Geodesy and Cartography Vilnius Gediminas Technica / Unknown | 2029-7009 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5160 | Logos: Revista de Linguistica, Filosofia y Literat / Unknown | 0719-3262 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5161 | Samarah Universitas Islam Negeri Ar-Raniry / Unknown | 2549-3167 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5162 | International Journal of Information Systems and C / Unknown | 1479-3121 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5163 | NEUROLOGICAL SCIENCES AND  NEUROPHYSIOLOGY / WOLTERS KLUWER MEDKNOW  PUBLICATIONS | 2636-865X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5164 | Sustainability and Climate Change Mary Ann Liebert / Unknown | 2692-2924 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5165 | Folia Cryptogamica Estonica Estonian Naturalists'  / Unknown | 1736-7786 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5166 | Journal of Studies in International Education SAGE / Unknown | 2789-634X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5167 | Journal of Gems and Gemmology Editorial Department / Unknown | 2096-9120 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5168 | METALS / MDPI | 2075-4701 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5169 | KOREAN JOURNAL OF CHEMICAL  ENGINEERING / KOREAN INSTITUTE CHEMICAL   ENGINEERS | 1975-7220 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5170 | MEAT SCIENCE / ELSEVIER SCI LTD | 0309-1740 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5171 | SUPERCONDUCTOR SCIENCE &  TECHNOLOGY / IOP PUBLISHING LTD | 1361-6668 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5172 | ZOOKEYS / PENSOFT PUBLISHERS | 1313-2970 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5173 | COMPLEXITY / WILEY | 1076-2787 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5174 | Infrared and Laser Engineering Science Press / Unknown | 1007-2276 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5175 | JOURNAL OF SPEECH LANGUAGE AND  HEARING RESEARCH / AMER SPEECH-LANGUAGE-HEARING  ASSOC | 1558-9102 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5176 | REVIEW OF PALAEOBOTANY AND  PALYNOLOGY / ELSEVIER | 0034-6667 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5177 | APPLIED ECOLOGY AND  ENVIRONMENTAL RESEARCH / ALOKI APPLIED ECOLOGICAL  RESEARCH AND F | 1785-0037 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5178 | TAIWANESE JOURNAL OF OBSTETRICS  & GYNECOLOGY / ELSEVIER TAIWAN | 1028-4559 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5179 | URBAN HISTORY / CAMBRIDGE UNIV PRESS | 0963-9268 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5180 | SOCIAL COMPASS / SAGE PUBLICATIONS LTD | 0037-7686 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5181 | ADMINISTRATION AND POLICY IN  MENTAL HEALTH AND ME / SPRINGER | 0894-587X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5182 | Journal of Experimental Zoology India DR. P. R. YA / Unknown | 0976-1780 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5183 | INTERNATIONAL JOURNAL OF  MEDICINAL MUSHROOMS / BEGELL HOUSE INC | 1521-9437 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5184 | Medical News of North Caucasus Stavropol State Med / Unknown | 2073-8145 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5185 | Rehabilitacion Ediciones Doyma, S.L. / Unknown | 1578-3278 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5186 | JOURNAL OF NONLINEAR OPTICAL  PHYSICS & MATERIALS / WORLD SCIENTIFIC PUBL CO PTE  LTD | 0218-8635 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5187 | Nanosystems: Physics, Chemistry, Mathematics ITMO  / Unknown | 2220-8054 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5188 | Transactions of Japanese Society for Medical and B / Unknown | 1881-4379 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5189 | JOURNAL OF LATIN AMERICAN  CULTURAL STUDIES / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1356-9325 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5190 | International Journal of Trichology Wolters Kluwer / Unknown | 0974-7753 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5191 | PATHOGENS AND GLOBAL HEALTH / TAYLOR & FRANCIS LTD | 2047-7724 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5192 | Brazilian Journal of Oral Sciences Universidade Es / Unknown | 1677-3225 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5193 | EUROPEAN JOURNAL OF ENGLISH  STUDIES / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1382-5577 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5194 | Journal of Youth Development Clemson University/Ti / Unknown | 2325-4009 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5195 | ARCHAEOLOGICAL DIALOGUES / CAMBRIDGE UNIV PRESS | 1380-2038 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5196 | CODESIGN-INTERNATIONAL JOURNAL  OF COCREATION IN D / TAYLOR & FRANCIS LTD | 1571-0882 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5197 | Drugs in Context BioExcel Publishing Ltd. / Unknown | 1745-1981 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5198 | AUTISM IN ADULTHOOD / MARY ANN LIEBERT, INC | 2573-9581 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5199 | International Journal of Literary Humanities Commo / Unknown | 2327-8676 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5200 | INTERNATIONAL JOURNAL OF  HUMANITIES AND ARTS COMP / EDINBURGH UNIV PRESS | 1753-8548 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5201 | @GRH Association Francophone de Gestion des Relati / Unknown | 2295-9149 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5202 | ADVANCES IN METHODS AND  PRACTICES IN PSYCHOLOGICA / SAGE PUBLICATIONS INC | 2515-2459 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5203 | English Text Construction John Benjamins Publishin / Unknown | 1874-8767 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5204 | AUSTRAL JOURNAL OF VETERINARY  SCIENCES / UNIV AUSTRAL CHILE, FAC CIENCIAS  VETERI | 0719-8132 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5205 | Biostatistics and Epidemiology Taylor and Francis  / Unknown | 2470-9360 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5206 | FASEB JOURNAL / WILEY | 0892-6638 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5207 | PEDIATRICS / AMER ACAD PEDIATRICS | 1098-4275 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5208 | ECONOMIC HISTORY REVIEW / WILEY | 0013-0117 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5209 | FRONTIERS IN NUTRITION / FRONTIERS MEDIA SA | 2296-861X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5210 | COMPUTERS & INDUSTRIAL  ENGINEERING / PERGAMON-ELSEVIER SCIENCE LTD | 0360-8352 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5211 | NUCLEAR TECHNOLOGY / TAYLOR & FRANCIS INC | 0029-5450 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5212 | PROCEEDINGS OF THE INSTITUTION OF  MECHANICAL ENGI / SAGE PUBLICATIONS LTD | 0954-4070 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5213 | Brazilian Journal of Biology Instituto Internacion / Unknown | 1678-4375 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5214 | ZYGON / OPEN LIBRARY HUMANITIES | 1467-9744 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5215 | PLATELETS / TAYLOR & FRANCIS INC | 0953-7104 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5216 | IEEE JOURNAL OF PHOTOVOLTAICS / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 2156-3381 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5217 | JOURNAL OF AGRICULTURAL  METEOROLOGY / SOC AGRICULTURAL METEOROLOGY  JAPAN | 0021-8588 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5218 | CRIMINOLOGY / WILEY | 0011-1384 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5219 | UPDATES IN SURGERY / SPRINGER-VERLAG ITALIA SRL | 2038-131X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5220 | SEMINARS IN INTERVENTIONAL  RADIOLOGY / THIEME MEDICAL PUBL INC | 0739-9529 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5221 | JOURNAL OF INTERNATIONAL  FINANCIAL MARKETS INSTIT / ELSEVIER | 1042-4431 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5222 | BRITISH JOURNAL FOR THE HISTORY OF  PHILOSOPHY / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 0960-8788 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5223 | BIOLOGICAL PSYCHIATRY-COGNITIVE  NEUROSCIENCE AND  / ELSEVIER | 2451-9022 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5224 | Media Asia Taylor and Francis Ltd. / Unknown | 0129-6612 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5225 | BULLETIN OF SPANISH STUDIES / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1475-3820 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5226 | CANADIAN JOURNAL OF  ADMINISTRATIVE SCIENCES-REVUE / WILEY | 0825-0383 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5227 | NATURE ELECTRONICS / NATURE PORTFOLIO | 2520-1131 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5228 | JOURNAL OF THE AMERICAN  MOSQUITO CONTROL ASSOCIAT / AMER MOSQUITO CONTROL ASSOC | 8756-971X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5229 | Journal of Occupational Science Taylor and Francis / Unknown | 1442-7591 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5230 | Journal of Structured Finance Portfolio Management / Unknown | 2374-1325 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5231 | Journal of Horticultural Sciences Society for Prom / Unknown | 2582-4899 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5232 | JOURNAL OF CONTEXTUAL  BEHAVIORAL SCIENCE / ELSEVIER | 2212-1447 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5233 | JOURNAL OF MUSICOLOGICAL  RESEARCH / TAYLOR & FRANCIS LTD | 0141-1896 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5234 | INTERNATIONAL JOURNAL OF  CHILDRENS SPIRITUALITY / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1364-436X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5235 | Geologija Geological Survey of Slovenia / Unknown | 1854-620X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5236 | REVIEW OF SYMBOLIC LOGIC / CAMBRIDGE UNIV PRESS | 1755-0203 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5237 | Oral Oncology Reports Elsevier Ltd / Unknown | 2772-9060 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5238 | Journal of Literary and Cultural Disability Studie / Unknown | 1757-6458 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5239 | Journal of HIV/AIDS and Social Services Routledge / Unknown | 1538-151X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5240 | Schole Novosibirskij Gosudarstvennyj Universitet / Unknown | 1995-4336 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5241 | METACOGNITION AND LEARNING / SPRINGER | 1556-1623 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5242 | Ethical Thought RAS Institute of Philosophy / Unknown | 2074-4897 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5243 | Ethics and Bioethics (in Central Europe) Sciendo / Unknown | 1338-5615 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5244 | Clinical Transplantation and Research Korean Socie / Unknown | 3022-7712 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5245 | JOURNAL OF HIGH ENERGY PHYSICS / SPRINGER | 1029-8479 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5246 | Journal of High Energy Physics / Unknown | 1127-2236 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5247 | MOLECULAR MICROBIOLOGY / WILEY | 0950-382X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5248 | PALAEOGEOGRAPHY  PALAEOCLIMATOLOGY  PALAEOECOLOGY / ELSEVIER | 0031-0182 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5249 | METABOLITES / MDPI | 2218-1989 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5250 | Peabody Journal of Education Taylor and Francis Lt / Unknown | 0161-956X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5251 | GONDWANA RESEARCH / ELSEVIER | 1342-937X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5252 | ETHNOHISTORY / DUKE UNIV PRESS | 0014-1801 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5253 | AMERICAN FAMILY PHYSICIAN / AMER ACAD FAMILY PHYSICIANS | 1532-0650 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5254 | American family physician / Unknown | 1532-0669 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5255 | WOOD SCIENCE AND TECHNOLOGY / SPRINGER | 0043-7719 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5256 | SURGICAL ONCOLOGY-OXFORD / ELSEVIER SCI LTD | 0960-7404 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5257 | Estudos Avancados Instituto de Estudos Avancados d / Unknown | 1806-9592 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5258 | JOURNAL DE MYCOLOGIE MEDICALE / MASSON EDITEUR | 1773-0449 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5259 | TURKISH JOURNAL OF MATHEMATICS / TUBITAK SCIENTIFIC &  TECHNOLOGICAL RESE | 1303-6149 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5260 | URBAN HISTORY REVIEW-REVUE D  HISTOIRE URBAINE / UNIV TORONTO PRESS INC | 0703-0428 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5261 | ENTOMOLOGICAL SCIENCE / WILEY | 1343-8786 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5262 | METABOLIC SYNDROME AND RELATED  DISORDERS / MARY ANN LIEBERT, INC | 1540-4196 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5263 | TRANSLATIONAL STROKE RESEARCH / SPRINGER | 1868-4483 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5264 | Alzheimer's and Dementia: Diagnosis, Assessment an / Unknown | 2352-8729 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5265 | JOURNAL OF ETHNOBIOLOGY AND  ETHNOMEDICINE / BMC | 1746-4269 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5266 | Journal of Wine Research Routledge / N°   ISSN   E-ISSN | 1469-9672 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5267 | Pediatric Reports Multidisciplinary Digital Publis / Unknown | 2036-749X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5268 | EXPOSITIONES MATHEMATICAE / ELSEVIER GMBH | 0723-0869 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5269 | Sante Mentale et Droit Elsevier Masson s.r.l. / Unknown | 2772-9710 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5270 | REVISTA DE ECONOMIA MUNDIAL / UNIV HUELVA, SERV  PUBLICACIONES | 2340-4264 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5271 | International Journal of Sport Policy and Politics / Unknown | 1940-6940 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5272 | Financial History Review Cambridge University Pres / Unknown | 0968-5650 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5273 | Pakistan Journal of Phytopathology Pakistan Phytop / Unknown | 2305-0284 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5274 | Forum Geografi Muhammadiyah University of Surakart / Unknown | 2460-3945 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5275 | International Journal of Web Information Systems E / Unknown | 1744-0084 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5276 | Per Linguam Department of General Linguistics, Ste / Unknown | 2224-0012 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5277 | Mongolian Studies Kalmyk Scientific Centre of Russ / Unknown | 2712-8059 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5278 | Adverse Drug Reaction Bulletin Lippincott Williams / Unknown | 0044-6394 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5279 | Journal of Tropical Crop Science IPB University De / Unknown | 2356-0177 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5280 | Sustainable Environment Taylor and Francis Ltd. / Unknown | 2765-8511 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5281 | Southern African Journal of Entrepreneurship and S / Unknown | 2522-7343 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5282 | Jahr University of Rijeka, Faculty of Medicine / N°   ISSN   E-ISSN | 1848-7874 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5283 | TAPA Johns Hopkins University Press / Unknown | 2575-7199 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5284 | LOGI - Scientific Journal on Transport and Logisti / Unknown | 2336-3037 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5285 | Town and Regional Planning University of the Free  / Unknown | 2415-0495 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5286 | Afghanistan Edinburgh University Press / Unknown | 2399-357X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5287 | Croatian Economic Survey Institute of Economics (Z / Unknown | 1846-3878 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5288 | PAMATKY ARCHEOLOGICKE / ACAD SCIENCES CZECH REP, INST  ARCHAEOLO | 2570-9496 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5289 | Precision Nutrition Lippincott Williams and Wilkin / N°   ISSN   E-ISSN | 2993-8139 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5290 | CURRENT BIOLOGY / CELL PRESS | 0960-9822 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5291 | EMBO JOURNAL / SPRINGERNATURE | 0261-4189 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5292 | JOURNAL OF MAMMALOGY / OXFORD UNIV PRESS INC | 0022-2372 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5293 | GEOLOGY / GEOLOGICAL SOC AMER, INC | 1943-2682 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5294 | ARCHIVES OF VIROLOGY / SPRINGER WIEN | 0304-8608 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5295 | WIRELESS PERSONAL  COMMUNICATIONS / SPRINGER | 0929-6212 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5296 | NEUROUROLOGY AND URODYNAMICS / WILEY | 0733-2467 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5297 | INTERNATIONAL JOURNAL OF  ELECTRONICS / TAYLOR & FRANCIS LTD | 0020-7217 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5298 | HEALTH PSYCHOLOGY / AMER PSYCHOLOGICAL ASSOC | 0278-6133 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5299 | AMERICAN JOURNAL OF NEPHROLOGY / KARGER | 0250-8095 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5300 | JOURNAL OF POROUS MATERIALS / SPRINGER | 1380-2224 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5301 | ADVANCED ROBOTICS / TAYLOR & FRANCIS LTD | 0169-1864 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5302 | JOURNAL OF WORLD TRADE / KLUWER LAW INT | 2210-2795 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5303 | PHYSIOLOGICAL GENOMICS / AMER PHYSIOLOGICAL SOC | 1094-8341 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5304 | JOURNAL OF EDUCATIONAL  MEASUREMENT / WILEY | 0022-0655 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5305 | BATTERIES & SUPERCAPS / WILEY-V C H VERLAG GMBH | 2566-6223 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5306 | METROECONOMICA / WILEY | 0026-1386 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5307 | HARVARD EDUCATIONAL REVIEW / HARVARD GRADUATE SCHOOL  EDUCATION | 1943-5045 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5308 | Journal of Oral and Maxillofacial Surgery, Medicin / Unknown | 2212-5558 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5309 | Economy of Regions Institute of Economics, The Ura / Unknown | 2411-1406 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5310 | Miznarodnij Endokrinologicnij Zurnal Zaslavsky Pub / Unknown | 2307-1427 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5311 | JOURNAL OF THE INTERNATIONAL  PHONETIC ASSOCIATION / CAMBRIDGE UNIV PRESS | 0025-1003 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5312 | ARCHIVES OF SUICIDE RESEARCH / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1381-1118 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5313 | ENGINEERING MANAGEMENT  JOURNAL / TAYLOR & FRANCIS LTD | 1042-9247 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5314 | Journal of Pediatric Neurosciences Wolters Kluwer  / Unknown | 1817-1745 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5315 | Sleep Medicine Clinics W.B. Saunders / N°   ISSN   E-ISSN | 1556-4088 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5316 | EDUCATIONAL RESEARCH REVIEW / ELSEVIER SCI LTD | 1747-938X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5317 | Psychological Science and Education Moscow State U / Unknown | 1814-2052 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5318 | MASS COMMUNICATION AND SOCIETY / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1520-5436 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5319 | JOURNAL OF ENGLISH LINGUISTICS / SAGE PUBLICATIONS INC | 0075-4242 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5320 | EAST ASIAN SCIENCE TECHNOLOGY  AND SOCIETY-AN INTE / TAYLOR & FRANCIS INC | 1875-2152 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5321 | NEUROLOGY-GENETICS / LIPPINCOTT WILLIAMS & WILKINS | 2376-7839 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5322 | Geotechnik Wiley-Blackwell / N°   ISSN   E-ISSN | 0172-6145 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5323 | Filolog (Banja Luka) Faculty of Philology Banja Lu / Unknown | 2233-1158 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5324 | SCIENCE AND TECHNOLOGY OF  NUCLEAR INSTALLATIONS / WILEY | 1687-6075 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5325 | JOURNAL OF THEORETICAL POLITICS / SAGE PUBLICATIONS LTD | 0951-6298 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5326 | GERIATRIC ORTHOPAEDIC SURGERY &  REHABILITATION / SAGE PUBLICATIONS INC | 2151-4585 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5327 | NPJ GENOMIC MEDICINE / NATURE PORTFOLIO | 2056-7944 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5328 | Childhood and Philosophy State Univ of Rio de Jane / Unknown | 2525-5061 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5329 | International Journal of Cell Biology John Wiley a / Unknown | 1687-8876 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5330 | Heart International Touch Medical Media / Unknown | 2036-2579 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5331 | Perspectives on Public Management and Governance O / Unknown | 2398-4910 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5332 | AATCC Review / Unknown | 2330-5525 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5333 | Statistika Czech Statistical Office / Unknown | 1804-8765 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5334 | Extreme Medicine Federal Medical Biological Agency / Unknown | 2713-2765 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5335 | Theory Workshop Brill / Unknown | 2590-1869 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5336 | NEPHROLOGY DIALYSIS  TRANSPLANTATION / OXFORD UNIV PRESS | 0931-0509 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5337 | TUMORI JOURNAL / SAGE PUBLICATIONS LTD | 0300-8916 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5338 | HASTINGS CENTER REPORT / WILEY | 0093-0334 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5339 | JOURNAL OF INHERITED METABOLIC  DISEASE / WILEY | 0141-8955 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5340 | ECONOMIC MODELLING / ELSEVIER | 0264-9993 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5341 | BRITISH JOURNAL OF HOSPITAL  MEDICINE / MA HEALTHCARE LTD | 1759-7390 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5342 | CIRCULATION-CARDIOVASCULAR  QUALITY AND OUTCOMES / LIPPINCOTT WILLIAMS & WILKINS | 1941-7705 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5343 | TRANSPORT IN POROUS MEDIA / SPRINGER | 0169-3913 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5344 | Mathematical Biosciences and Engineering American  / Unknown | 1551-0018 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5345 | ALLERGOLOGIA ET  IMMUNOPATHOLOGIA / CODON PUBLICATIONS | 1578-1267 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5346 | IMMUNOTHERAPY / TAYLOR & FRANCIS LTD | 1750-743X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5347 | EPIGENETICS / TAYLOR & FRANCIS INC | 1559-2294 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5348 | JOURNAL OF AGING AND HEALTH / SAGE PUBLICATIONS INC | 0898-2643 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5349 | IAWA JOURNAL / BRILL | 2294-1932 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5350 | LATIN AMERICAN POLITICS AND  SOCIETY / CAMBRIDGE UNIV PRESS | 1531-426X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5351 | EMERGENCIAS / SOC ESPANOLA MEDICINA  URGENCIAS & EMERG | 2386-5857 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5352 | Teoria y Realidad Constitucional Univ Nacional de  / Unknown | 2174-8950 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5353 | International Forum of Psychoanalysis Routledge / Unknown | 1651-2324 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5354 | IEEE GEOSCIENCE AND REMOTE  SENSING MAGAZINE / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 2168-6831 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5355 | IEEE Geoscience and Remote Sensing Magazine / Unknown | 2373-7468 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5356 | IRANIAN JOURNAL OF PEDIATRICS / BRIEFLANDS | 2008-2150 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5357 | ASIAN JOURNAL OF SOCIAL  PSYCHOLOGY / WILEY | 1367-2223 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5358 | JOURNAL OF SCIENCE-ADVANCED  MATERIALS AND DEVICES / VIETNAM NATL UNIV | 2468-2284 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5359 | CLINICAL AND INVESTIGATIVE  MEDICINE / CANADIAN SOC CLINICAL  INVESTIGATION | 1488-2353 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5360 | Revista de la Educacion Superior Asociacion Nacion / Unknown | 2395-9037 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5361 | Patologiya Krovoobrashcheniya i Kardiokhirurgiya M / Unknown | 2500-3119 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5362 | Journal of Internet Commerce Routledge / Unknown | 1533-287X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5363 | Researches in Mathematics Oles Honchar Dnipro Nati / Unknown | 2664-5009 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5364 | Archivos de Historia del Movimiento Obrero y la Iz / Unknown | 2683-9601 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5365 | Architecture Multidisciplinary Digital Publishing  / Unknown | 2673-8945 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5366 | International Journal of High Performance Systems  / N°   ISSN   E-ISSN | 1751-6528 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5367 | Marine Systems and Ocean Technology Springer Natur / Unknown | 1679-396X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5368 | Journal of Geometric Mechanics American Institute  / Unknown | 1941-4897 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5369 | SUBSTANCE USE & ADDICTION  JOURNAL / SAGE PUBLICATIONS INC | 2976-7342 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5370 | Organizations and Markets in Emerging Economies Vi / Unknown | 2345-0037 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5371 | International Journal of Design in Society Common  / Unknown | 2325-1360 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5372 | Genus Springer International Publishing AG / Unknown | 0016-6987 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5373 | Moral Philosophy and Politics Walter de Gruyter Gm / Unknown | 2194-5616 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5374 | Journal of Islamic and Muslim Studies Indiana Univ / Unknown | 2470-7074 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5375 | Constitutional Review  Center for Research and Cas / Unknown | 2548-3870 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5376 | JOURNAL OF COATINGS TECHNOLOGY  AND RESEARCH / SPRINGER | 1547-0091 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5377 | SURFACE SCIENCE / ELSEVIER | 0039-6028 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5378 | POLYHEDRON / PERGAMON-ELSEVIER SCIENCE LTD | 0277-5387 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5379 | ENGINEERING STRUCTURES / ELSEVIER SCI LTD | 0141-0296 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5380 | APPETITE / ACADEMIC PRESS LTD- ELSEVIER  SCIENCE LT | 0195-6663 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5381 | JOURNAL OF ANALYTICAL AND APPLIED  PYROLYSIS / ELSEVIER | 0165-2370 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5382 | QUALITY OF LIFE RESEARCH / SPRINGER | 0962-9343 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5383 | THEORY OF PROBABILITY AND ITS  APPLICATIONS / SIAM PUBLICATIONS | 0040-585X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5384 | AMERICAN EDUCATIONAL RESEARCH  JOURNAL / SAGE PUBLICATIONS INC | 0002-8312 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5385 | JOURNAL OF PEACE RESEARCH / SAGE PUBLICATIONS LTD | 0022-3433 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5386 | ALGORITHMICA / SPRINGER | 0178-4617 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5387 | NIGERIAN JOURNAL OF CLINICAL  PRACTICE / WOLTERS KLUWER MEDKNOW  PUBLICATIONS | 1119-3077 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5388 | CURRENT PHARMACEUTICAL  BIOTECHNOLOGY / BENTHAM SCIENCE PUBL LTD | 1389-2010 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5389 | ANGLE ORTHODONTIST / E H ANGLE EDUCATION RESEARCH  FOUNDATION | 1945-7103 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5390 | IEEE TRANSACTIONS ON  EVOLUTIONARY COMPUTATION / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 1089-778X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5391 | Psychological Perspectives Taylor and Francis Ltd. / Unknown | 0033-2925 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5392 | SOLAR SYSTEM RESEARCH / PLEIADES PUBLISHING INC | 0038-0946 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5393 | Vox Patrum John Paul II Catholic University of Lub / N°   ISSN   E-ISSN | 2719-3586 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5394 | JOURNAL OF SOCIAL PHILOSOPHY / WILEY | 0047-2786 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5395 | JOURNAL OF ORGANIZATIONAL  CHANGE MANAGEMENT / EMERALD GROUP PUBLISHING LTD | 0953-4814 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5396 | GEOGRAFISKA ANNALER SERIES B- HUMAN GEOGRAPHY / TAYLOR & FRANCIS LTD | 0435-3684 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5397 | Journal of Education for Library and Information S / Unknown | 0748-5786 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5398 | SOFTWARE AND SYSTEMS MODELING / SPRINGER HEIDELBERG | 1619-1366 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5399 | Revue d'Ethique et de Theologie Morale Editions du / N°   ISSN   E-ISSN | 2118-4518 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5400 | Quebec Studies Liverpool University Press / Unknown | 0737-3759 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5401 | Nashim Indiana University Press / Unknown | 1565-5288 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5402 | Journal of Punjab Academy of Forensic Medicine and / Unknown | 0974-083X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5403 | INFORMATION VISUALIZATION / SAGE PUBLICATIONS LTD | 1473-8716 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5404 | Energy and AI Elsevier B.V. / Unknown | 2666-5468 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5405 | Short Film Studies Intellect Ltd. / Unknown | 2042-7832 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5406 | Manusya Chulalongkorn University / Unknown | 2665-9077 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5407 | Atom Indonesia National Nuclear Energy Agency / Unknown | 2356-5322 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5408 | Particles Multidisciplinary Digital Publishing Ins / Unknown | 2571-712X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5409 | Law and Humanities Taylor and Francis Ltd. / Unknown | 1752-1483 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5410 | Jurnal Kajian Bali Udayana University / Unknown | 2580-0698 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5411 | Childhood in the Past Taylor and Francis Ltd. / Unknown | 1758-5716 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5412 | UUM Journal of Legal Studies Universiti Utara Mala / Unknown | 2229-984X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5413 | AsiaIntervention Europa Group / Unknown | 2491-0929 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5414 | Lurralde: Investigacion y Espacio Instituto Geogra / Unknown | 1697-3070 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5415 | CHEMICAL SCIENCE / ROYAL SOC CHEMISTRY | 2041-6520 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5416 | INTERNATIONAL JOURNAL OF  PEDIATRIC OTORHINOLARYNG / ELSEVIER IRELAND LTD | 0165-5876 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5417 | AMERICAN JOURNAL OF PREVENTIVE  MEDICINE / ELSEVIER SCIENCE INC | 0749-3797 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5418 | ANTIQUARIES JOURNAL / CAMBRIDGE UNIV PRESS | 0003-5815 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5419 | MODERN PHILOLOGY / UNIV CHICAGO PRESS | 0026-8232 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5420 | IMMUNITY / CELL PRESS | 1074-7613 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5421 | GENETIC RESOURCES AND CROP  EVOLUTION / SPRINGER | 0925-9864 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5422 | COGNITIVE SCIENCE / WILEY | 0364-0213 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5423 | Revue Francaise d'Allergologie Elsevier Masson s.r / Unknown | 1877-0312 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5424 | REVUE FRANCAISE D ALLERGOLOGIE / ELSEVIER MASSON, CORPORATION  OFFICE | 1877-0320 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5425 | CNS SPECTRUMS / CAMBRIDGE UNIV PRESS | 1092-8529 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5426 | JOURNAL OF THE ROYAL SOCIETY  INTERFACE / ROYAL SOC | 1742-5662 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5427 | HYPATIA-A JOURNAL OF FEMINIST  PHILOSOPHY / CAMBRIDGE UNIV PRESS | 0887-5367 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5428 | ARCHIVES OF PSYCHIATRIC NURSING / W B SAUNDERS CO-ELSEVIER INC | 0883-9417 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5429 | Anales del Instituto de Investigaciones Esteticas  / Unknown | 1870-3062 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5430 | JOURNAL OF BIOMATERIALS  APPLICATIONS / SAGE PUBLICATIONS LTD | 0885-3282 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5431 | INTERNATIONAL STUDIES REVIEW / OXFORD UNIV PRESS | 1468-2486 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5432 | Nefrologia Elsevier Espana S.L.U / Unknown | 2013-2514 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5433 | Egyptian Journal of Histology Egyptian Society of  / Unknown | 2090-2417 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5434 | PARALLAX / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1353-4645 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5435 | NINETEENTH-CENTURY MUSIC REVIEW / CAMBRIDGE UNIV PRESS | 1479-4098 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5436 | JOURNAL OF VECTOR BORNE DISEASES / WOLTERS KLUWER MEDKNOW  PUBLICATIONS | 0972-9062 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5437 | RHODORA / NEW ENGLAND BOTANICAL CLUB  INC | 1938-3401 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5438 | INTERNATIONAL JOURNAL OF  ANALYTICAL CHEMISTRY / WILEY | 1687-8760 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5439 | International Journal of Intelligent Systems Techn / Unknown | 1740-8865 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5440 | Journal of Web Librarianship Routledge / Unknown | 1932-2917 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5441 | International Journal of Healthcare Information Sy / Unknown | 1555-3396 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5442 | ARIEL-A REVIEW OF INTERNATIONAL  ENGLISH LITERATUR / JOHNS HOPKINS UNIV PRESS | 1920-1222 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5443 | Waste Management Bulletin Elsevier B.V. / Unknown | 2949-7507 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5444 | ZEITSCHRIFT FUR FRANZOSISCHE  SPRACHE UND LITERATU / FRANZ STEINER VERLAG GMBH | 2366-2425 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5445 | Medicina y Laboratorio Universidad de Antioquia / N°   ISSN   E-ISSN | 2500-7106 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5446 | Journal of Electrical Bioimpedance Sciendo / Unknown | 1891-5469 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5447 | CHANGE OVER TIME-AN  INTERNATIONAL JOURNAL OF  CON / UNIV PENNSYLVANIA PRESS | 2153-053X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5448 | Alloys MDPI Multidisciplinary Digital Publishing I / Unknown | 2674-063X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5449 | Northeast Journal of Complex Systems Binghamton Un / N°   ISSN   E-ISSN | 2577-8439 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5450 | Asian Journal of Anesthesiology Taiwan Society of  / Unknown | 2468-824X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5451 | Veterinary Record Open John Wiley & Sons Inc. / Unknown | 2399-2050 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5452 | AMERICAN ANTHROPOLOGIST / WILEY | 0002-7294 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5453 | AMERICAN SURGEON / SAGE PUBLICATIONS INC | 0003-1348 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5454 | TECHNICAL PHYSICS LETTERS / MAIK  NAUKA/INTERPERIODICA/SPRINGER | 1063-7850 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5455 | JOURNAL OF DENTISTRY / ELSEVIER SCI LTD | 0300-5712 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5456 | FUTURES / ELSEVIER SCI LTD | 0016-3287 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5457 | ISME JOURNAL / OXFORD UNIV PRESS | 1751-7362 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5458 | BIOTECHNOLOGY &  BIOTECHNOLOGICAL EQUIPMENT / TAYLOR & FRANCIS LTD | 1310-2818 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5459 | IEEE JOURNAL OF OCEANIC  ENGINEERING / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 0364-9059 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5460 | IEEE Journal of Oceanic Engineering / Unknown | 2373-7786 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5461 | JOURNAL OF PHYSICAL ACTIVITY &  HEALTH / HUMAN KINETICS PUBL INC | 1543-3080 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5462 | JOURNAL OF TRAVEL MEDICINE / OXFORD UNIV PRESS INC | 1195-1982 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5463 | INTERNATIONAL JOURNAL OF STROKE / SAGE PUBLICATIONS LTD | 1747-4930 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5464 | International journal of intelligent engineering a / Unknown | 1882-708X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5465 | International Journal of Intelligent Engineering a / Unknown | 2185-310X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5466 | CANADIAN PUBLIC ADMINISTRATION- ADMINISTRATION PUB / WILEY | 0008-4840 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5467 | COMPUTER-AIDED CIVIL AND  INFRASTRUCTURE ENGINEERI / WILEY | 1093-9687 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5468 | GROUND WATER MONITORING AND  REMEDIATION / WILEY | 1069-3629 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5469 | International Journal of Productivity and Performa / Unknown | 1741-0401 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5470 | Journal of Extra-Corporeal Technology EDP Sciences / Unknown | 0022-1058 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5471 | CANCER IMAGING / BMC | 1470-7330 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5472 | EDUCATIONAL ADMINISTRATION  QUARTERLY / SAGE PUBLICATIONS INC | 0013-161X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5473 | ODONTOLOGY / SPRINGER | 1618-1247 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5474 | FISHERIES OCEANOGRAPHY / WILEY | 1054-6006 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5475 | INTERNATIONAL JOURNAL OF LOW- CARBON TECHNOLOGIES / OXFORD UNIV PRESS | 1748-1317 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5476 | ANNUAL REVIEW OF NEUROSCIENCE / ANNUAL REVIEWS | 0147-006X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5477 | FACIES / SPRINGER | 0172-9179 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5478 | Innovar Universidad Nacional de Colombia / N°   ISSN   E-ISSN | 2248-6968 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5479 | QUATERNAIRE / SOC GEOLOGIQUE FRANCE | 1965-0795 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5480 | Asian Ethnicity Routledge / Unknown | 1469-2953 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5481 | QUALITY ASSURANCE AND SAFETY OF  CROPS & FOODS / CODON PUBLICATIONS | 1757-837X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5482 | REVISTA DE LA UNION MATEMATICA  ARGENTINA / UNION MATEMATICA ARGENTINA | 1669-9637 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5483 | Mathematical Proceedings of the Royal Irish Academ / Unknown | 2009-0021 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5484 | JOURNAL OF SURVEY STATISTICS AND  METHODOLOGY / OXFORD UNIV PRESS INC | 2325-0984 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5485 | Digital Diagnostics Eco-Vector LLC / Unknown | 2712-8962 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5486 | Surfaces Multidisciplinary Digital Publishing Inst / Unknown | 2571-9637 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5487 | Regional Anesthesia and Acute Pain Management Eco- / Unknown | 2687-1394 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5488 | Journal of Moravian History Penn State University  / Unknown | 1933-6632 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5489 | Journal of Japanese and Korean Cinema Taylor and F / Unknown | 1756-4905 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5490 | International Journal of Computer Games Technology / N°   ISSN   E-ISSN | 1687-7047 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5491 | Studies in Ancient Art and Civilization Ksiegarnia / Unknown | 2449-867X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5492 | History of European Political and Constitutional T / Unknown | 2589-5966 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5493 | LINEAR ALGEBRA AND ITS  APPLICATIONS / ELSEVIER SCIENCE INC | 0024-3795 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5494 | COMPUTER METHODS IN APPLIED  MECHANICS AND ENGINEE / ELSEVIER SCIENCE SA | 0045-7825 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5495 | AFRICAN STUDIES REVIEW / CAMBRIDGE UNIV PRESS | 0002-0206 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5496 | PERITONEAL DIALYSIS INTERNATIONAL / SAGE PUBLICATIONS INC | 0896-8608 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5497 | BUSINESS HORIZONS / ELSEVIER | 0007-6813 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5498 | REVISTA DE SAUDE PUBLICA / REVISTA DE SAUDE PUBLICA | 1518-8787 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5499 | ACTA PHYSIOLOGIAE PLANTARUM / SPRINGER HEIDELBERG | 0137-5881 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5500 | PSYCHOANALYTIC QUARTERLY / TAYLOR & FRANCIS INC | 0033-2828 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5501 | CONSCIOUSNESS AND COGNITION / ACADEMIC PRESS INC ELSEVIER  SCIENCE | 1053-8100 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5502 | RADIOPROTECTION / EDP SCIENCES S A | 0033-8451 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5503 | DIX-SEPTIEME SIECLE / SOC ETUD 17 SIECLE | 1969-6965 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5504 | PROCEEDINGS OF THE INSTITUTION OF  MECHANICAL ENGI / SAGE PUBLICATIONS LTD | 0954-4097 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5505 | Brazilian Journal of Nephrology Sociedade Brasilei / N°   ISSN   E-ISSN | 2175-8239 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5506 | Preventive Nutrition and Food Science Korean Socie / Unknown | 2287-8602 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5507 | Revue d'Histoire des Sciences Cairn France / Unknown | 1969-6582 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5508 | PLASTICS RUBBER AND COMPOSITES / SAGE PUBLICATIONS INC | 1465-8011 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5509 | REVIEWS IN THE NEUROSCIENCES / WALTER DE GRUYTER GMBH | 0334-1763 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5510 | ASIA PACIFIC JOURNAL OF EDUCATION / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 0218-8791 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5511 | Ambiente & sociedade / Unknown | 1983-0211 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5512 | Zhurnal Mikrobiologii Epidemiologii i Immunobiolog / Unknown | 2686-7613 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5513 | Journal of Police and Criminal Psychology Springer / Unknown | 0882-0783 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5514 | Journal of Patient-Reported Outcomes Springer Inte / Unknown | 2509-8020 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5515 | ANNUAL REVIEWS IN CONTROL / PERGAMON-ELSEVIER SCIENCE LTD | 1367-5788 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5516 | Revista Facultad de Medicina Universidad Nacional  / Unknown | 2357-3848 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5517 | Methods and Protocols Multidisciplinary Digital Pu / Unknown | 2409-9279 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5518 | TROPICAL ECOLOGY / SPRINGERNATURE | 0564-3295 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5519 | Cryptography Multidisciplinary Digital Publishing  / N°   ISSN   E-ISSN | 2410-387X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5520 | Journal of Cerebrovascular and Endovascular Neuros / N°   ISSN   E-ISSN | 2287-3139 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5521 | International Journal of Electronic Governance Ind / Unknown | 1742-7509 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5522 | International Journal of Information Systems and S / Unknown | 1935-5726 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5523 | WOUNDS-A COMPENDIUM OF  CLINICAL RESEARCH AND PRAC / H M P COMMUNICATIONS | 1943-2704 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5524 | Dicenda Universidad Complutense Madrid / Unknown | 1988-2556 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5525 | Journal of Asian Security and International Affair / Unknown | 2347-7970 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5526 | Advances in Applied Energy Elsevier Ltd / Unknown | 2666-7924 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5527 | ARCHIVES OF ASIAN ART / DUKE UNIV PRESS | 0066-6637 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5528 | Infectious Diseases and Immunity Wolters Kluwer He / Unknown | 2693-8839 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5529 | Progress in Landslide Research and Technology Spri / Unknown | 2731-3794 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5530 | Acta Linguistica Lithuanica Institute of the Lithu / Unknown | 2669-218X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5531 | HARVARD LAW REVIEW / HARVARD LAW REV ASSOC | 2161-976X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5532 | Zeitschrift der Savigny-Stiftung fur Rechtsgeschic / Unknown | 0323-4045 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5533 | WASTE MANAGEMENT / PERGAMON-ELSEVIER SCIENCE LTD | 0956-053X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5534 | JOURNAL OF PERIODONTOLOGY / WILEY | 0022-3492 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5535 | WIT Transactions on Ecology and the Environment WI / Unknown | 1746-448X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5536 | JOURNAL OF MICROMECHANICS AND  MICROENGINEERING / IOP PUBLISHING LTD | 1361-6439 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5537 | Folia Pharmacologica Japonica Japanese Pharmacolog / Unknown | 1347-8397 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5538 | JOURNAL OF NATURAL HISTORY / TAYLOR & FRANCIS LTD | 0022-2933 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5539 | Egyptian Journal of Chemistry NIDOC (Nat.Inform.Do / Unknown | 2357-0245 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5540 | BEHAVIOURAL PHARMACOLOGY / LIPPINCOTT WILLIAMS & WILKINS | 0955-8810 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5541 | JOURNAL OF CIRCUITS SYSTEMS AND  COMPUTERS / WORLD SCIENTIFIC PUBL CO PTE  LTD | 0218-1266 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5542 | Eurasip Journal on Advances in Signal Processing S / Unknown | 1687-6172 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5543 | EURASIP JOURNAL ON ADVANCES IN  SIGNAL PROCESSING / SPRINGER | 1687-6180 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5544 | JOURNAL OF ENZYME INHIBITION AND  MEDICINAL CHEMIS / TAYLOR & FRANCIS LTD | 1475-6366 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5545 | JAMA CARDIOLOGY / AMER MEDICAL ASSOC | 2380-6583 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5546 | MIDDLE EAST JOURNAL / MIDDLE EAST INST | 1940-3461 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5547 | Roeper Review Taylor and Francis Ltd. / Unknown | 0278-3193 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5548 | LITERARY IMAGINATION / OXFORD UNIV PRESS | 1523-9012 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5549 | MATHEMATICS AND MECHANICS OF  SOLIDS / SAGE PUBLICATIONS LTD | 1081-2865 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5550 | BIOLOGY & PHILOSOPHY / SPRINGER | 0169-3867 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5551 | Revista de  Administracao Publica Fundacao Getulio / Unknown | 1982-3134 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5552 | JOURNAL OF SHIP RESEARCH / SOC NAVAL ARCHITECTS & MARINE  ENGINEERS | 1542-0604 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5553 | ADVANCED QUANTUM TECHNOLOGIES / WILEY | 2511-9044 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5554 | ADVANCES IN HIGH ENERGY PHYSICS / WILEY | 1687-7357 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5555 | GEMS & GEMOLOGY / GEMOLOGICAL INST AMER | 0016-626X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5556 | RESEARCH EVALUATION / OXFORD UNIV PRESS | 0958-2029 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5557 | High Temperature Material Processes Begell House I / Unknown | 1093-3611 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5558 | Public Health and Life Environment Federal Center  / Unknown | 2619-0788 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5559 | FAMILY BUSINESS REVIEW / SAGE PUBLICATIONS INC | 0894-4865 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5560 | CHINA & WORLD ECONOMY / WILEY | 1671-2234 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5561 | International Journal of Knowledge-Based and Intel / N°   ISSN   E-ISSN | 1327-2314 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5562 | International Journal of Technology Marketing Inde / Unknown | 1741-878X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5563 | EARTH SCIENCES RESEARCH JOURNAL / UNIV NACIONAL DE COLOMBIA | 2339-3459 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5564 | JOURNAL OF AFRICAN MEDIA STUDIES / INTELLECT LTD | 2040-199X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5565 | Anthropological Journal of European Cultures Bergh / Unknown | 1755-2931 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5566 | Chinese Medicine and Culture Lippincott Williams a / Unknown | 2589-9473 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5567 | Boyhood Studies Berghahn Journals / Unknown | 2375-9267 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5568 | Aloma Facultat de Psicologia, Ciencies de l'Educac / Unknown | 2339-9694 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5569 | Patristica et Mediaevalia Institute of Philosophy  / N°   ISSN   E-ISSN | 2683-9636 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5570 | Latin American Legal Studies Universidad Adolfo Ib / Unknown | 0719-9112 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5571 | EUROPACE / OXFORD UNIV PRESS | 1099-5129 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5572 | CHEMICAL GEOLOGY / ELSEVIER | 0009-2541 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5573 | INTERNATIONAL JOURNAL OF LEGAL  MEDICINE / SPRINGER | 0937-9827 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5574 | JOURNAL OF BIOMOLECULAR  STRUCTURE & DYNAMICS / TAYLOR & FRANCIS INC | 0739-1102 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5575 | JOURNAL OF ASIAN EARTH SCIENCES / PERGAMON-ELSEVIER SCIENCE LTD | 1367-9120 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5576 | BIOLOGIA PLANTARUM / ACAD SCIENCES CZECH REPUBLIC,  INST EXPE | 1573-8264 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5577 | SYSTEM / ELSEVIER SCI LTD | 0346-251X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5578 | PHYTOCHEMISTRY LETTERS / ELSEVIER | 1874-3900 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5579 | Nursing Administration Quarterly Lippincott Willia / Unknown | 0363-9568 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5580 | BMB REPORTS / KOREAN SOCIETY BIOCHEMISTRY &  MOLECULAR | 1976-670X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5581 | International Journal of Learning, Teaching and Ed / Unknown | 1694-2493 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5582 | Cahiers du Monde Russe Editions EHESS: Ecole des H / Unknown | 1777-5388 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5583 | GPS SOLUTIONS / SPRINGER HEIDELBERG | 1080-5370 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5584 | CALIFORNIA AGRICULTURE / UNIV CALIFORNIA, OAKLAND,  DIVISION AGRI | 2160-8091 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5585 | COMMUNICATIONS CHEMISTRY / NATURE PORTFOLIO | 2399-3669 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5586 | Proceedings of the ACM on Interactive, Mobile, Wea / Unknown | 2474-9567 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5587 | APPLIED PSYCHOPHYSIOLOGY AND  BIOFEEDBACK / SPRINGER/PLENUM PUBLISHERS | 1090-0586 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5588 | Vestnik Volgogradskogo Gosudarstvennogo Universite / Unknown | 2312-8704 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5589 | Allelopathy Journal International Allelopathy Foun / Unknown | 0974-1240 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5590 | Journal of Asia-Pacific Biodiversity National Scie / Unknown | 2287-9544 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5591 | ENVIRONMENT AND HISTORY / WHITE HORSE PRESS | 1752-7023 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5592 | ASCLEPIO-REVISTA DE HISTORIA DE LA  MEDICINA Y DE  / CONSEJO SUPERIOR  INVESTIGACIONES CIENTI | 1988-3102 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5593 | INTERNATIONAL JOURNAL FOR  MULTISCALE COMPUTATIONA / BEGELL HOUSE INC | 1543-1649 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5594 | INTERNATIONAL JOURNAL OF LAW  POLICY AND THE FAMIL / OXFORD UNIV PRESS | 1360-9939 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5595 | Análise Psicológica / Unknown | 2182-2980 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5596 | NUCLEUS / TAYLOR & FRANCIS INC | 1949-1034 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5597 | Women's Health Reports Mary Ann Liebert Inc. / Unknown | 2688-4844 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5598 | DECISION ANALYSIS / INFORMS | 1545-8490 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5599 | Journal of Asian Pacific Communication John Benjam / Unknown | 0957-6851 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5600 | International Journal of Automotive Engineering So / Unknown | 2185-0992 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5601 | Journal of the Association for Consumer Research U / Unknown | 2378-1815 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5602 | Frontiers in Research Metrics and Analytics Fronti / Unknown | 2504-0537 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5603 | CENTRAL EUROPE / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1479-0963 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5604 | FRONTIERS OF MATHEMATICS / SPRINGER HEIDELBERG | 2731-8648 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5605 | Computer Methods and Programs in Biomedicine Updat / Unknown | 2666-9900 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5606 | Clinical Medicine Insights: Arthritis and Musculos / Unknown | 1179-5441 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5607 | Bulletin of Atmospheric Science and Technology Spr / Unknown | 2662-1495 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5608 | Miscellanea Hadriatica et Mediterranea University  / Unknown | 2718-1170 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5609 | GAS SCIENCE AND ENGINEERING / ELSEVIER | 2949-9097 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5610 | SIXTEENTH CENTURY JOURNAL / UNIV CHICAGO PRESS | 0361-0160 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5611 | FRONTIERS IN CELL AND  DEVELOPMENTAL BIOLOGY / FRONTIERS MEDIA SA | 2296-634X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5612 | CLINICAL CARDIOLOGY / WILEY | 0160-9289 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5613 | JOURNAL OF AUTISM AND  DEVELOPMENTAL DISORDERS / SPRINGER/PLENUM PUBLISHERS | 0162-3257 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5614 | JOURNAL OF NANOPARTICLE  RESEARCH / SPRINGER | 1388-0764 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5615 | Urologia Journal Sage Publications / Unknown | 0391-5603 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5616 | TOXICOLOGY IN VITRO / PERGAMON-ELSEVIER SCIENCE LTD | 0887-2333 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5617 | European Journal of Lipid Science and Technology W / Unknown | 1438-7697 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5618 | EUROPEAN JOURNAL OF LIPID SCIENCE  AND TECHNOLOGY / WILEY | 1438-9312 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5619 | RUSI Journal Routledge / Unknown | 1744-0378 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5620 | CURRENT ORGANIC CHEMISTRY / BENTHAM SCIENCE PUBL LTD | 1385-2728 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5621 | INSECT SCIENCE / WILEY | 1672-9609 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5622 | CURRENT OPINION IN  OTOLARYNGOLOGY & HEAD AND NECK / LIPPINCOTT WILLIAMS & WILKINS | 1068-9508 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5623 | Scientia Sinica Technologica Science Press / Unknown | 1674-7259 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5624 | Food Processing: Techniques and Technology Kemerov / Unknown | 2313-1748 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5625 | SEMINARS IN DIAGNOSTIC PATHOLOGY / W B SAUNDERS CO-ELSEVIER INC | 0740-2570 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5626 | JOURNAL OF BELIEFS & VALUES- STUDIES IN RELIGION & / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1361-7672 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5627 | JOURNAL OF BIOINFORMATICS AND  COMPUTATIONAL BIOLO / WORLD SCIENTIFIC PUBL CO PTE  LTD | 0219-7200 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5628 | Urology Times Advanstar Communications Inc. / Unknown | 2150-7384 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5629 | REVUE INTERNATIONALE DE  PHILOSOPHIE / REVUE INT PHILOSOPHIE | 2033-0138 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5630 | CANADIAN JOURNAL OF  EXPERIMENTAL PSYCHOLOGY-REVUE / CANADIAN PSYCHOLOGICAL  ASSOC | 1196-1961 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5631 | DYNAMICAL SYSTEMS-AN  INTERNATIONAL JOURNAL / TAYLOR & FRANCIS LTD | 1468-9367 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5632 | RESOURCE AND ENERGY ECONOMICS / ELSEVIER | 0928-7655 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5633 | EMPIRICA / SPRINGER | 0340-8744 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5634 | Journal of the Canadian Society of Forensic Scienc / Unknown | 0008-5030 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5635 | Journal of the Turkish German Gynecology Associati / Unknown | 1309-0399 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5636 | Hormone Molecular Biology and Clinical Investigati / Unknown | 1868-1883 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5637 | Journal of Crop Science and Biotechnology Springer / Unknown | 1975-9479 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5638 | CANNABIS AND CANNABINOID  RESEARCH / MARY ANN LIEBERT, INC | 2378-8763 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5639 | INTERNATIONAL JOURNAL OF  FORENSIC MENTAL HEALTH / SAGE PUBLICATIONS LTD | 1499-9013 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5640 | Decision Science Letters Growing Science / Unknown | 1929-5812 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5641 | Critical Inquiry in Language Studies Routledge / Unknown | 1542-7595 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5642 | Malaysian Journal of Syariah and Law Faculty of Sy / Unknown | 2590-4396 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5643 | Maternal-Fetal Medicine Wolters Kluwer Health / Unknown | 2641-5895 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5644 | International Journal of Electronic Customer Relat / Unknown | 1750-0664 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5645 | Biophysics Reports Science China Press / Unknown | 2364-3439 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5646 | Smart Energy Elsevier Ltd / Unknown | 2666-9552 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5647 | Food Studies Common Ground Research Networks / Unknown | 2160-1941 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5648 | Crossings Intellect Ltd. / Unknown | 2040-4352 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5649 | ANNUAL REVIEW OF VISION SCIENCE / ANNUAL REVIEWS | 2374-4642 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5650 | Suma de Negocios Fundacion Universitaria Konrad Lo / Unknown | 2215-910X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5651 | Nonlinear Phenomena in Complex Systems Education a / Unknown | 1561-4085 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5652 | Teologicka Reflexe Karolinum - Nakladatelstvi Univ / Unknown | 2788-0796 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5653 | APPLIED ENERGY / ELSEVIER SCI LTD | 0306-2619 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5654 | FRONTIERS IN NEUROLOGY / FRONTIERS MEDIA SA | 1664-2295 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5655 | CHEMICAL ENGINEERING &  TECHNOLOGY / WILEY-V C H VERLAG GMBH | 0930-7516 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5656 | JOURNAL OF AAPOS / MOSBY-ELSEVIER | 1091-8531 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5657 | ENERGY & ENVIRONMENTAL SCIENCE / ROYAL SOC CHEMISTRY | 1754-5692 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5658 | MOLECULAR CANCER RESEARCH / AMER ASSOC CANCER RESEARCH | 1541-7786 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5659 | MEDICINE SCIENCE AND THE LAW / SAGE PUBLICATIONS INC | 0025-8024 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5660 | JOURNAL OF HOSPITAL MEDICINE / WILEY | 1553-5592 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5661 | JOURNAL OF GEOGRAPHICAL SCIENCES / SCIENCE PRESS | 1009-637X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5662 | NEUROSCIENCE BULLETIN / SPRINGER | 1673-7067 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5663 | STOCHASTIC ANALYSIS AND  APPLICATIONS / TAYLOR & FRANCIS INC | 0736-2994 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5664 | EMPLOYEE RELATIONS / EMERALD GROUP PUBLISHING LTD | 0142-5455 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5665 | INTERNATIONAL JOURNAL OF  RESEARCH IN MARKETING / ELSEVIER | 0167-8116 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5666 | Acta Botanica Malacitana Universidad de Malaga / Unknown | 2340-5074 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5667 | INTERNATIONAL JOURNAL OF GAME  THEORY / SPRINGER HEIDELBERG | 0020-7276 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5668 | JOURNAL OF CONSUMER AFFAIRS / WILEY | 0022-0078 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5669 | GENEVA PAPERS ON RISK AND  INSURANCE-ISSUES AND PR / PALGRAVE MACMILLAN LTD | 1018-5895 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5670 | FOLK LIFE-JOURNAL OF ETHNOLOGICAL  STUDIES / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 0430-8778 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5671 | MINDS AND MACHINES / SPRINGER | 0924-6495 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5672 | Budownictwo i Architektura Politechnika Lubelska / Unknown | 2544-3275 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5673 | Public Policy and Administration Mykolo Romerio Un / Unknown | 2029-2872 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5674 | Oncology in Clinical Practice Wydawnictwo Via Medi / Unknown | 2450-6478 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5675 | DISCOVER NANO / SPRINGER | 2731-9229 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5676 | Journal of Orthoptera Research Orthopterists' Soci / Unknown | 1937-2426 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5677 | PHOTOACOUSTICS / ELSEVIER GMBH | 2213-5979 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5678 | JOURNAL OF WINE ECONOMICS / CAMBRIDGE UNIV PRESS | 1931-4361 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5679 | ARDEA / NEDERLANDSE ORNITHOLOGISCHE  UNIE | 2213-1175 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5680 | Journal of Ophthalmic Inflammation and Infection S / Unknown | 1869-5760 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5681 | ACM TRANSACTIONS ON  RECONFIGURABLE TECHNOLOGY AND / ASSOC COMPUTING MACHINERY | 1936-7406 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5682 | Cuadernos de Historia Moderna Universidad Complute / Unknown | 1988-2475 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5683 | Green Analytical Chemistry Elsevier B.V. / Unknown | 2772-5774 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5684 | Journal of Cognitive Enhancement Springer Nature / Unknown | 2509-3290 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5685 | International Journal of Emergency Services Emeral / Unknown | 2047-0894 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5686 | Acta Iadertina University of Zadar / Unknown | 1849-1243 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5687 | Jurnal Hukum Islam Faculty of Sharia, Universitas  / Unknown | 2502-7719 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5688 | Revue Francaise d'Ethique Appliquee ERES / Unknown | 2494-5757 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5689 | International Journal of Legal Discourse De Gruyte / Unknown | 2364-8821 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5690 | Internet Pragmatics John Benjamins Publishing Comp / Unknown | 2542-3851 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5691 | Categories and General Algebraic Structures with A / Unknown | 2345-5861 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5692 | BEST PRACTICE & RESEARCH-CLINICAL  ANAESTHESIOLOGY / ELSEVIER | 1878-1608 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5693 | BIORESOURCE TECHNOLOGY / ELSEVIER SCI LTD | 0960-8524 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5694 | INTERNATIONAL JOURNAL OF SOLIDS  AND STRUCTURES / PERGAMON-ELSEVIER SCIENCE LTD | 0020-7683 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5695 | ZEITSCHRIFT FUR KRISTALLOGRAPHIE- CRYSTALLINE MATE / WALTER DE GRUYTER GMBH | 2194-4946 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5696 | REVISTA DE NEUROLOGIA / IMR PRESS | 1576-6578 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5697 | CHEMMEDCHEM / WILEY-V C H VERLAG GMBH | 1860-7179 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5698 | JOURNAL OF PEDIATRIC  OPHTHALMOLOGY & STRABISMUS / SLACK INC | 0191-3913 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5699 | OIL & GAS JOURNAL / PENNWELL PUBL CO ENERGY  GROUP | 0030-1388 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5700 | COMPUTING / SPRINGER WIEN | 0010-485X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5701 | FUNDAMENTAL & CLINICAL  PHARMACOLOGY / WILEY | 0767-3981 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5702 | Neuro-Ophthalmology Taylor and Francis Ltd. / Unknown | 0165-8107 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5703 | Oncology Issues Slack Incorporated / Unknown | 1046-3356 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5704 | JOURNAL OF AEROSPACE  ENGINEERING / ASCE-AMER SOC CIVIL ENGINEERS | 0893-1321 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5705 | PUBLICATIONS OF THE RESEARCH  INSTITUTE FOR MATHEM / EUROPEAN MATHEMATICAL SOC- EMS | 0034-5318 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5706 | BLOOD PRESSURE MONITORING / LIPPINCOTT WILLIAMS & WILKINS | 1359-5237 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5707 | MICROBIAL GENOMICS / MICROBIOLOGY SOC | 2057-5858 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5708 | Communications Materials Springer Nature / Unknown | 2662-4443 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5709 | DIACHRONICA / JOHN BENJAMINS PUBLISHING CO | 0176-4225 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5710 | Research in Economics Academic Press / N°   ISSN   E-ISSN | 1090-9451 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5711 | JOURNAL OF ORGANIZATIONAL  BEHAVIOR MANAGEMENT / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 0160-8061 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5712 | MEDICAL MOLECULAR MORPHOLOGY / SPRINGER JAPAN KK | 1860-1480 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5713 | Psychoanalytic Perspectives Routledge / Unknown | 2163-6958 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5714 | International Journal of Hydrology Science and Tec / Unknown | 2042-7808 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5715 | Economic Annals-XXI Institute of Society Transform / Unknown | 1728-6239 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5716 | Integrated Science Springer / Unknown | 2662-9461 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5717 | STATE POLITICS & POLICY QUARTERLY / CAMBRIDGE UNIV PRESS | 1532-4400 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5718 | Journal of Biologically Active Products from Natur / Unknown | 2231-1866 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5719 | Evidence-based HRM Emerald Publishing / N°   ISSN   E-ISSN | 2049-3983 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5720 | ASAP Journal Johns Hopkins University Press / Unknown | 2381-4721 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5721 | MATHEMATICS AND FINANCIAL  ECONOMICS / SPRINGER HEIDELBERG | 1862-9660 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5722 | Biologie Aujourd'hui EDP Sciences / Unknown | 2105-0678 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5723 | MUSICA HODIE / UNIV FEDERAL GOIAS | 2317-6776 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5724 | Journal of Theoretical and Applied Mechanics (Bulg / Unknown | 0861-6663 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5725 | Proceedings of the Institution of Civil Engineers: / Unknown | 2043-9911 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5726 | ADOLESCENT RESEARCH REVIEW / SPRINGER INT PUBL AG | 2363-8346 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5727 | Journal of Holistic Nursing and Midwifery Guilan U / Unknown | 2588-3720 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5728 | Philologia Classica Saint Petersburg State Univers / Unknown | 2618-6969 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5729 | International Journal of Environmental Sustainabil / Unknown | 2325-1085 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5730 | JOURNAL OF FRACTAL GEOMETRY / EUROPEAN MATHEMATICAL SOC- EMS | 2308-1309 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5731 | Demografie Cesky Statisticky Urad / Unknown | 1805-2991 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5732 | ORGANIC LETTERS / AMER CHEMICAL SOC | 1523-7060 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5733 | PHYSIOLOGIA PLANTARUM / WILEY | 0031-9317 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5734 | POLYMER ENGINEERING AND SCIENCE / WILEY | 0032-3888 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5735 | BURNS / ELSEVIER SCI LTD | 0305-4179 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5736 | PSYCHOLOGICAL BULLETIN / AMER PSYCHOLOGICAL ASSOC | 0033-2909 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5737 | JOURNAL OF AIRCRAFT / AMER INST AERONAUTICS   ASTRONAUTICS | 1533-3868 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5738 | NURSE EDUCATION TODAY / CHURCHILL LIVINGSTONE | 1532-2793 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5739 | SURFACE ENGINEERING / SAGE PUBLICATIONS INC | 0267-0844 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5740 | DIALECTICA / PHILOSOPHIE.CH | 1746-8361 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5741 | Dirasat: Human and Social Sciences The University  / Unknown | 2663-6190 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5742 | Canadian Journal of Hospital Pharmacy Canadian Soc / Unknown | 1920-2903 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5743 | BIOMEDICAL MICRODEVICES / SPRINGER | 1387-2176 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5744 | JOURNAL OF VINYL & ADDITIVE  TECHNOLOGY / WILEY | 1083-5601 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5745 | BOIS ET FORETS DES TROPIQUES / CIRAD-CENTRE COOPERATION INT  RECHERCHE  | 1777-5760 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5746 | PATHOBIOLOGY / KARGER | 1015-2008 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5747 | RILCE-REVISTA DE FILOLOGIA  HISPANICA / UNIV NAVARRA, SERVICIO  PUBLICACIONES | 2174-0917 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5748 | LITERATURE COMPASS / WILEY | 1741-4113 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5749 | IEEE INTELLIGENT TRANSPORTATION  SYSTEMS MAGAZINE / IEEE-INST ELECTRICAL ELECTRONICS  ENGINE | 1939-1390 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5750 | MIND & LANGUAGE / WILEY | 0268-1064 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5751 | BIOCELL / TECH SCIENCE PRESS | 0327-9545 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5752 | Inra Productions Animales Institut national de rec / Unknown | 2273-7766 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5753 | ECONOMIC SYSTEMS / ELSEVIER | 0939-3625 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5754 | COMPUTATIONAL PARTICLE  MECHANICS / SPRINGER INT PUBL AG | 2196-4378 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5755 | Tizard Learning Disability Review Emerald Group Pu / Unknown | 1359-5474 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5756 | SCOTTISH GEOGRAPHICAL JOURNAL / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1470-2541 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5757 | Global Society Taylor and Francis Ltd. / Unknown | 1360-0826 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5758 | Logistique et Management Informa UK Ltd / Unknown | 2377-9640 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5759 | MOTIVATION SCIENCE / EDUCATIONAL PUBLISHING  FOUNDATION-AMERI | 2333-8113 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5760 | European Company and Financial Law Review Walter d / Unknown | 1613-2548 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5761 | Neuroscience Journal of Shefaye Khatam Shefa Neuro / Unknown | 2345-4814 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5762 | HISTORIA AGRARIA / UNIV MURCIA | 2340-3659 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5763 | Izvestiya Vuzov. Poroshkovaya Metallurgiya i Funkt / Unknown | 2412-8767 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5764 | Scottish Archaeological Journal Edinburgh Universi / Unknown | 1471-5767 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5765 | Proceedings of the Institution of Civil Engineers: / Unknown | 1755-0785 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5766 | Computer Science AGH University of Science and Tec / Unknown | 2300-7036 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5767 | Revista Criminalidad Policia Nacional de Colombia / Unknown | 2256-5531 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5768 | Revista Colombiana de Matematicas Universidad Naci / Unknown | 2357-4100 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5769 | Problems of Applied Mathematics and Mathematical M / Unknown | 2074-5893 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5770 | Sleep Medicine: X Elsevier B.V. / Unknown | 2590-1427 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5771 | Mathematical Statistics and Learning European Math / Unknown | 2520-2324 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5772 | JOURNAL OF CLINICAL INVESTIGATION / AMER SOC CLINICAL  INVESTIGATION INC | 1558-8238 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5773 | Current Developments in Nutrition Elsevier B.V. / Unknown | 2475-2991 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5774 | PUBLIC ADMINISTRATION REVIEW / WILEY | 0033-3352 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5775 | SOIL & TILLAGE RESEARCH / ELSEVIER | 0167-1987 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5776 | JOURNAL OF APPLIED TOXICOLOGY / WILEY | 0260-437X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5777 | CHINESE JOURNAL OF AERONAUTICS / ELSEVIER SCIENCE INC | 1000-9361 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5778 | ECONOMIC RECORD / WILEY | 0013-0249 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5779 | REVISTA PANAMERICANA DE SALUD  PUBLICA-PAN AMERICA / PAN AMER HEALTH ORGANIZATION | 1680-5348 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5780 | EARLY CHILDHOOD EDUCATION  JOURNAL / SPRINGER | 1082-3301 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5781 | EUROPEAN JOURNAL OF MARKETING / EMERALD GROUP PUBLISHING LTD | 0309-0566 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5782 | REVIEW OF METAPHYSICS / PHILOSOPHY EDUCATION SOC, INC | 2154-1302 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5783 | ASIAN STUDIES REVIEW / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1035-7823 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5784 | CELLULAR & MOLECULAR BIOLOGY  LETTERS / BMC | 1425-8153 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5785 | Baltistica Vilnius University, Department of Balti / Unknown | 2345-0045 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5786 | Apunts. Educacion Fisica y Deportes Institut Nacio / Unknown | 2014-0983 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5787 | DYNAMICS OF ATMOSPHERES AND  OCEANS / ELSEVIER | 0377-0265 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5788 | SOCIAL PSYCHOLOGY OF EDUCATION / SPRINGER | 1381-2890 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5789 | Tourism and Hospitality Research SAGE Publications / Unknown | 1467-3584 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5790 | International Journal of Rotating Machinery John W / Unknown | 1023-621X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5791 | Clinical Dentistry (Russia) Clinical Dentistry LLC / Unknown | 2713-2846 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5792 | Biologicni Studii Ivan Franko National University  / Unknown | 2311-0783 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5793 | EPIDEMIOLOGIC REVIEWS / OXFORD UNIV PRESS INC | 0193-936X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5794 | Kavkazskij Entomologiceskij Bulleten Southern Scie / Unknown | 2713-1785 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5795 | Journal of Agricultural Extension Agricultural Ext / Unknown | 2408-6851 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5796 | MIKROBIYOLOJI BULTENI / ANKARA MICROBIOLOGY SOC | 0374-9096 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5797 | INTERNATIONAL JOURNAL OF ISLAMIC  AND MIDDLE EASTE / EMERALD GROUP PUBLISHING LTD | 1753-8394 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5798 | CANADIAN JOURNAL OF CRIMINOLOGY  AND CRIMINAL JUST / UNIV TORONTO PRESS INC | 1707-7753 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5799 | SOFT MATERIALS / TAYLOR & FRANCIS INC | 1539-445X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5800 | Comunicacion y Sociedad (Mexico) Universidad de Gu / Unknown | 2448-9042 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5801 | INTERNATIONAL JOURNAL OF  BUSINESS COMMUNICATION / SAGE PUBLICATIONS INC | 2329-4884 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5802 | HBRC Journal Taylor and Francis Ltd. / Unknown | 1687-4048 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5803 | INTERNATIONAL JOURNAL OF  PHYSICAL MODELLING IN  G / EMERALD GROUP PUBLISHING LTD | 1346-213X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5804 | Journal of Endometriosis and Pelvic Pain Disorders / Unknown | 2284-0273 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5805 | ANNUAL REVIEW OF CONDENSED  MATTER PHYSICS / ANNUAL REVIEWS | 1947-5454 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5806 | Infection Ecology and Epidemiology Taylor and Fran / Unknown | 2000-8686 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5807 | Journal of Thyroid Research John Wiley and Sons Lt / Unknown | 2042-0072 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5808 | Memoria e Ricerca Societa Editrice Il Mulino / N°   ISSN   E-ISSN | 1972-523X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5809 | APPLIED MATHEMATICS IN SCIENCE  AND ENGINEERING / TAYLOR & FRANCIS LTD | 2769-0911 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5810 | Anuario de Psicologia Universitat de Barcelona / Unknown | 1988-5253 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5811 | NEUROMUSCULAR DISORDERS / PERGAMON-ELSEVIER SCIENCE LTD | 0960-8966 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5812 | MONATSHEFTE FUR MATHEMATIK / SPRINGER WIEN | 0026-9255 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5813 | CORROSION / NATL ASSOC CORROSION ENG | 1938-159X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5814 | EUROPEAN JOURNAL OF ORAL  SCIENCES / WILEY | 0909-8836 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5815 | LANGUAGE IN SOCIETY / CAMBRIDGE UNIV PRESS | 0047-4045 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5816 | GENETICS RESEARCH / WILEY | 0016-6723 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5817 | ETHNOMUSICOLOGY / SOC ETHNOMUSICOLOGY INC | 2156-7417 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5818 | ENTERPRISE & SOCIETY / CAMBRIDGE UNIV PRESS | 1467-2227 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5819 | JOURNAL OF DEMOCRACY / JOHNS HOPKINS UNIV PRESS | 1086-3214 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5820 | THEORY OF COMPUTING SYSTEMS / SPRINGER | 1432-4350 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5821 | JOURNAL OF THE ANATOMICAL  SOCIETY OF INDIA / WOLTERS KLUWER MEDKNOW  PUBLICATIONS | 0003-2778 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5822 | Journal of the Korean Society for Railway Korean S / Unknown | 2288-2235 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5823 | SCHOOL PSYCHOLOGY INTERNATIONAL / SAGE PUBLICATIONS LTD | 0143-0343 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5824 | OXFORD REVIEW OF ECONOMIC  POLICY / OXFORD UNIV PRESS | 0266-903X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5825 | INTERNATIONAL JOURNAL OF  PERIODONTICS & RESTORATI / QUINTESSENCE PUBLISHING CO INC | 1945-3388 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5826 | EUROPEAN JOURNAL OF APPLIED  MATHEMATICS / CAMBRIDGE UNIV PRESS | 0956-7925 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5827 | Bulletin for International Taxation International  / Unknown | 2352-9202 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5828 | KNOWLEDGE ENGINEERING REVIEW / CAMBRIDGE UNIV PRESS | 0269-8889 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5829 | SOCIAL PHILOSOPHY AND POLICY / CAMBRIDGE UNIV PRESS | 0265-0525 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5830 | Production Associacao Brasileira de Engenharia de  / Unknown | 1980-5411 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5831 | Journal of Long-Term Effects of Medical Implants B / Unknown | 1050-6934 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5832 | CLINICAL AND EXPERIMENTAL  OTORHINOLARYNGOLOGY / KOREAN SOC OTORHINOLARYNGOL | 2005-0720 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5833 | Housing and Society Taylor and Francis Ltd. / Unknown | 0888-2746 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5834 | EUROPEAN SPORT MANAGEMENT  QUARTERLY / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1618-4742 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5835 | Philip Roth Studies Purdue University Press / N°   ISSN   E-ISSN | 1940-5278 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5836 | Journal of Digital and Social Media Marketing Henr / Unknown | 2050-0084 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5837 | Archaeologiai Ertesito Akademiai Kiado / Unknown | 0003-8032 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5838 | Turismo y Sociedad Universidad Externado de Colomb / Unknown | 2346-206X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5839 | East Asian Archives of Psychiatry Hong Kong Academ / Unknown | 2224-7041 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5840 | Annals of Maxillofacial Surgery Wolters Kluwer Med / Unknown | 2249-3816 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5841 | BULLETIN OF THE AMERICAN SOCIETY  OF OVERSEAS RESE / UNIV CHICAGO PRESS | 2769-3589 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5842 | Journal of Hydrology X Elsevier B.V. / Unknown | 2589-9155 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5843 | Cornova Institute of Czech Literature Czech Academ / Unknown | 2787-9151 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5844 | JOURNAL OF ORGANIC CHEMISTRY / AMER CHEMICAL SOC | 1520-6904 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5845 | ANNALS OF THE NEW YORK ACADEMY  OF SCIENCES / WILEY | 0077-8923 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5846 | JOURNAL OF ENVIRONMENTAL  CHEMICAL ENGINEERING / ELSEVIER SCI LTD | 2213-2929 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5847 | HISTORISCHE ZEITSCHRIFT / WALTER DE GRUYTER GMBH | 0018-2613 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5848 | Leading Edge Society of Exploration Geophysicists / Unknown | 1938-3789 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5849 | Journal of Physical Education, Recreation and Danc / Unknown | 0730-3084 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5850 | INORGANIC MATERIALS / MAIK  NAUKA/INTERPERIODICA/SPRINGER | 0020-1685 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5851 | MACROMOLECULAR BIOSCIENCE / WILEY-V C H VERLAG GMBH | 1616-5187 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5852 | AMERICAN JOURNAL OF CHINESE  MEDICINE / WORLD SCIENTIFIC PUBL CO PTE  LTD | 0192-415X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5853 | ARCHAEOMETRY / WILEY | 0003-813X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5854 | CHILD PSYCHIATRY & HUMAN  DEVELOPMENT / SPRINGER | 0009-398X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5855 | FACIAL PLASTIC SURGERY / THIEME MEDICAL PUBL INC | 0736-6825 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5856 | CONTRIBUTIONS TO INDIAN  SOCIOLOGY / SAGE PUBLICATIONS INDIA  PVT LTD | 0069-9659 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5857 | EUROPEAN UROLOGY FOCUS / ELSEVIER | 2405-4569 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5858 | Revista Mexicana de Urologia Sociedad Mexicana de  / Unknown | 2007-4085 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5859 | CLINICS IN LIVER DISEASE / W B SAUNDERS CO-ELSEVIER INC | 1089-3261 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5860 | Breathe European Respiratory Society / Unknown | 2073-4735 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5861 | STUDIES IN PSYCHOLOGY / SAGE PUBLICATIONS INC | 0210-9395 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5862 | EUROPEAN PSYCHOLOGIST / HOGREFE PUBLISHING CORP | 1016-9040 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5863 | ALLERGY ASTHMA & IMMUNOLOGY  RESEARCH / KOREAN ACAD ASTHMA ALLERGY &  CLINICAL I | 2092-7363 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5864 | JOURNAL OF REAL ESTATE RESEARCH / TAYLOR & FRANCIS INC | 0896-5803 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5865 | Natural Language Engineering Cambridge University  / Unknown | 1351-3249 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5866 | Annals of Clinical and Experimental Neurology Eco- / Unknown | 2409-2533 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5867 | World Review of Entrepreneurship, Management and   / Unknown | 1746-0573 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5868 | JOURNAL OF SYSTEMATIC  PALAEONTOLOGY / TAYLOR & FRANCIS LTD | 1477-2019 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5869 | JOURNAL OF ADVANCED  PROSTHODONTICS / KOREAN ACAD PROSTHODONTICS | 2005-7814 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5870 | JOURNAL OF SCHOOL VIOLENCE / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1538-8220 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5871 | Review of Korean Studies The Academy of Korean Stu / Unknown | 2733-9351 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5872 | Wildlife Society Bulletin Wiley-Blackwell / Unknown | 0091-7648 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5873 | Psychological Injury and Law Springer New York / Unknown | 1938-971X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5874 | Archiwum Kryminologii  Institute of Law Studies of / Unknown | 2719-4280 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5875 | Military Behavioral Health Taylor and Francis Ltd. / Unknown | 2163-5781 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5876 | Network Science Cambridge University Press / N°   ISSN   E-ISSN | 2050-1242 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5877 | ACM Transactions on Management Information Systems / N°   ISSN   E-ISSN | 2158-656X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5878 | Current Sleep Medicine Reports Springer Internatio / Unknown | 2198-6401 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5879 | Advances in Ophthalmology and Optometry Elsevier I / Unknown | 2452-1760 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5880 | Acta Universitatis Sapientiae, Mathematica Springe / Unknown | 1844-6094 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5881 | Journal of Alloys and Metallurgical Systems Elsevi / Unknown | 2949-9178 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5882 | Journal of Interventional Medicine KeAi Publishing / Unknown | 2590-0293 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5883 | Language Teaching for Young Learners John Benjamin / Unknown | 2589-2053 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5884 | Lasers in Engineering / Unknown | 1026-7069 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5885 | LASERS IN ENGINEERING / OLD CITY PUBLISHING INC | 1029-029X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5886 | PLANT PHYSIOLOGY / OXFORD UNIV PRESS INC | 0032-0889 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5887 | LANCET ONCOLOGY / ELSEVIER SCIENCE INC | 1470-2045 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5888 | Educational Forum Taylor and Francis Ltd. / Unknown | 0013-1725 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5889 | BMGN-THE LOW COUNTRIES  HISTORICAL REVIEW / KONINKLIJK NEDERLANDS  HISTORISCH GENOOT | 2211-2898 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5890 | FOLIA MICROBIOLOGICA / SPRINGER | 0015-5632 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5891 | Town Planning Review Liverpool University Press / Unknown | 0041-0020 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5892 | INTERNATIONAL JOURNAL OF  ADHESION AND ADHESIVES / ELSEVIER SCI LTD | 0143-7496 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5893 | BIOANALYSIS / TAYLOR & FRANCIS LTD | 1757-6180 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5894 | EUROPEAN JOURNAL OF TRAUMA AND  EMERGENCY SURGERY / SPRINGER HEIDELBERG | 1863-9933 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5895 | ENVIRONMENTAL ENGINEERING  SCIENCE / MARY ANN LIEBERT, INC | 1092-8758 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5896 | JOURNAL OF MOLECULAR  ENDOCRINOLOGY / BIOSCIENTIFICA LTD | 1479-6813 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5897 | Scopus: Journal of East African Ornithology Nature / Unknown | 0250-4162 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5898 | EARTHQUAKE ENGINEERING AND  ENGINEERING VIBRATION / SPRINGER | 1671-3664 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5899 | POLICING & SOCIETY / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1043-9463 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5900 | e-Prime - Advances in Electrical Engineering, Elec / Unknown | 2772-6711 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5901 | Research Journal of Chemistry and Environment Worl / Unknown | 2278-4527 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5902 | PROCEEDINGS OF THE INSTITUTION OF  MECHANICAL ENGI / SAGE PUBLICATIONS LTD | 1475-0902 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5903 | International Journal of Services, Technology and  / Unknown | 1460-6720 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5904 | Espacio, Tiempo y Forma, Serie VII: Historia del A / Unknown | 2340-1478 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5905 | Ukrainian Botanical Journal Publishing House Akade / Unknown | 2415-8860 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5906 | MATHEMATICS OF CONTROL SIGNALS  AND SYSTEMS / SPRINGER LONDON LTD | 0932-4194 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5907 | Theology and Sexuality Taylor and Francis Ltd. / Unknown | 1355-8358 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5908 | ANIMAL BIODIVERSITY AND  CONSERVATION / MUSEU DE CIENCIES NATURALS- ZOOLOGIA | 2014-928X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5909 | Spatial and Spatio-temporal Epidemiology Elsevier  / Unknown | 1877-5845 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5910 | Soudobe Dejiny Institute of Contemporary History o / Unknown | 2695-0952 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5911 | Journal of Structural Fire Engineering Emerald Gro / Unknown | 2040-2317 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5912 | Contemporary Review of the Middle East SAGE Public / Unknown | 2347-7989 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5913 | INTERNATIONAL JOURNAL OF  MULTIMEDIA INFORMATION   / SPRINGER | 2192-6611 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5914 | Giant Elsevier B.V. / Unknown | 2666-5425 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5915 | INFORMATION AND INFERENCE-A  JOURNAL OF THE IMA / OXFORD UNIV PRESS | 2049-8764 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5916 | Learning and Teaching Berghahn Journals / Unknown | 1755-2281 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5917 | Journal of Comparative Asian Development IGI Globa / Unknown | 2150-5403 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5918 | Harmonia: Journal of Arts Research and Education U / Unknown | 2541-2426 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5919 | Rakenteiden Mekaniikka Aalto-yliopisto - Rakennust / Unknown | 1797-5301 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5920 | Avicenna Journal of Medical Biotechnology Avicenna / Unknown | 2008-4625 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5921 | Soil and Environment Soil Science Society of Pakis / Unknown | 2075-1141 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5922 | Scandinavian Journal of Information Systems  The I / Unknown | 0905-0167 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5923 | Open Mathematics Walter de Gruyter GmbH / Unknown | 1874-1045 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5924 | MICHIGAN LAW REVIEW / MICH LAW REV ASSOC | 1939-8557 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5925 | PHILOSOPHY AND  PHENOMENOLOGICAL RESEARCH / WILEY | 0031-8205 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5926 | CANCER SCIENCE / WILEY | 1347-9032 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5927 | JOURNAL OF ENGINEERING  THERMOPHYSICS / PLEIADES PUBLISHING INC | 1810-2328 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5928 | Jurnal Teknologi Penerbit UTM Press / Unknown | 2180-3722 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5929 | EUROPEAN ECONOMIC REVIEW / ELSEVIER | 0014-2921 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5930 | INTERNATIONAL JOURNAL OF  NEUROPSYCHOPHARMACOLOGY / OXFORD UNIV PRESS | 1461-1457 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5931 | JOURNAL OF NEUROINTERVENTIONAL  SURGERY / BMJ PUBLISHING GROUP | 1759-8486 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5932 | JOURNAL OF INTERNATIONAL  BUSINESS STUDIES / PALGRAVE MACMILLAN LTD | 0047-2506 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5933 | Journal of Maxillofacial and Oral Surgery Springer / Unknown | 0972-8279 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5934 | Oxidation of Metals Springer / Unknown | 0030-770X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5935 | LEIDEN JOURNAL OF INTERNATIONAL  LAW / CAMBRIDGE UNIV PRESS | 0922-1565 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5936 | JOURNAL OF ZOOLOGICAL  SYSTEMATICS AND EVOLUTIONAR / WILEY | 0947-5745 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5937 | LEARNING & MEMORY / COLD SPRING HARBOR LAB PRESS,  PUBLICATI | 1549-5485 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5938 | REVISTA DE HISTORIA ECONOMICA- JOURNAL OF IBERIAN  / CAMBRIDGE UNIV PRESS | 0212-6109 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5939 | ANIMAL BIOTECHNOLOGY / TAYLOR & FRANCIS INC | 1049-5398 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5940 | POETICA-ZEITSCHRIFT FUR SPRACH- UND LITERATURWISSE / BRILL | 0303-4178 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5941 | HEC FORUM / SPRINGER | 0956-2737 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5942 | LEARNING DISABILITIES RESEARCH &  PRACTICE / SAGE PUBLICATIONS INC | 0938-8982 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5943 | JOURNAL OF THE HISTORY OF  SEXUALITY / UNIV TEXAS PRESS | 1535-3605 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5944 | Current Trends in Biotechnology and Pharmacy Assoc / Unknown | 2230-7303 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5945 | RAIRO-OPERATIONS RESEARCH / EDP SCIENCES S A | 2804-7303 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5946 | Issues and Studies World Scientific Publishing Co. / Unknown | 1013-2511 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5947 | Water Science and Engineering Editorial Office of  / Unknown | 2405-8106 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5948 | Journal of Integrated Circuits and Systems Brazili / Unknown | 1807-1953 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5949 | SOLDAGEM & INSPECAO / ASSOC BRASIL SOLDAGEM | 1980-6973 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5950 | GREY SYSTEMS-THEORY AND  APPLICATION / EMERALD GROUP PUBLISHING LTD | 2043-9377 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5951 | International Journal of Computational Biology and / Unknown | 1756-0756 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5952 | Obrana a Strategie University of Defence / Unknown | 1802-7199 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5953 | Epigenomes Multidisciplinary Digital Publishing In / Unknown | 2075-4655 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5954 | De Jure: Jurnal Hukum dan Syar'iah Maulana Malik I / Unknown | 2528-1658 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5955 | Produccion y Limpia Corporacion Universitaria Lasa / Unknown | 2323-0703 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5956 | JOURNAL OF HOLY LAND AND  PALESTINE STUDIES / EDINBURGH UNIV PRESS | 2054-1988 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5957 | MODERN CHINESE LITERATURE AND  CULTURE / FOREIGN LANGUAGE PUBL | 2328-966X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5958 | Victoriographies Edinburgh University Press / Unknown | 2364-4583 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5959 | JOURNAL OF THE ASSOCIATION FOR  INFORMATION SYSTEM / ASSOC INFORMATION SYSTEMS | 1558-3457 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5960 | Saudi Endodontic Journal Wolters Kluwer Medknow Pu / Unknown | 2320-1495 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5961 | MICROWAVE AND OPTICAL  TECHNOLOGY LETTERS / WILEY | 0895-2477 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5962 | PHYSIOLOGY & BEHAVIOR / PERGAMON-ELSEVIER SCIENCE LTD | 0031-9384 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5963 | BIOORGANIC & MEDICINAL CHEMISTRY / PERGAMON-ELSEVIER SCIENCE LTD | 0968-0896 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5964 | Journal of Fish Biology Wiley-Blackwell Publishing / Unknown | 0022-1112 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5965 | JOURNAL OF FISH BIOLOGY / WILEY | 1095-8649 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5966 | MEDICAL HYPOTHESES / ELSEVIER | 0306-9877 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5967 | MATHEMATICAL PROCEEDINGS OF THE  CAMBRIDGE PHILOSO / CAMBRIDGE UNIV PRESS | 0305-0041 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5968 | REPRODUCTIVE BIOMEDICINE ONLINE / ELSEVIER SCI LTD | 1472-6483 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5969 | JOURNAL OF CLINICAL LIPIDOLOGY / ELSEVIER SCIENCE INC | 1876-4789 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5970 | Philippine Studies: Historical and Ethnographic Vi / Unknown | 2244-1638 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5971 | INTERNATIONAL JOURNAL OF CLINICAL  ONCOLOGY / SPRINGER JAPAN KK | 1341-9625 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5972 | JOURNAL OF BEHAVIOR THERAPY AND  EXPERIMENTAL PSYC / PERGAMON-ELSEVIER SCIENCE LTD | 0005-7916 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5973 | LANGUAGE SPEECH AND HEARING  SERVICES IN SCHOOLS / AMER SPEECH-LANGUAGE-HEARING  ASSOC | 1558-9129 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5974 | MARINE MICROPALEONTOLOGY / ELSEVIER | 0377-8398 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5975 | APPLIED MATHEMATICS AND  OPTIMIZATION / SPRINGER | 0095-4616 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5976 | Geographica Helvetica Copernicus Publications / Unknown | 0016-7312 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5977 | ECOLOGY OF FOOD AND NUTRITION / TAYLOR & FRANCIS INC | 0367-0244 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5978 | PATTERN ANALYSIS AND APPLICATIONS / SPRINGER | 1433-7541 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5979 | ANNALES DE L INSTITUT HENRI  POINCARE-PROBABILITES / INST MATHEMATICAL STATISTICS- IMS | 1778-7017 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5980 | RIDE-THE JOURNAL OF APPLIED  THEATRE AND PERFORMAN / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1356-9783 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5981 | MANAGEMENT LEARNING / SAGE PUBLICATIONS LTD | 1350-5076 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5982 | Crop Research Gaurav Publications / N°   ISSN   E-ISSN | 2454-1761 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5983 | REVIEW OF FAITH & INTERNATIONAL  AFFAIRS / ROUTLEDGE JOURNALS, TAYLOR &  FRANCIS LT | 1557-0274 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5984 | MICROBIOLOGY AND MOLECULAR  BIOLOGY REVIEWS / AMER SOC MICROBIOLOGY | 1092-2172 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5985 | CHRONIC RESPIRATORY DISEASE / SAGE PUBLICATIONS LTD | 1479-9723 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5986 | JOURNAL OF OBSESSIVE-COMPULSIVE  AND RELATED DISOR / ELSEVIER | 2211-3649 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5987 | ZEITSCHRIFT DER DEUTSCHEN  GESELLSCHAFT FUR  GEOWI / E SCHWEIZERBARTSCHE  VERLAGSBUCHHANDLUNG | 1861-4094 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5988 | Moscow University Biological Sciences Bulletin Ple / Unknown | 0096-3925 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5989 | CYTOJOURNAL / SCIENTIFIC SCHOLAR LLC | 1742-6413 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5990 | Advances in Geo-Energy Research Yandy Scientific P / Unknown | 2208-598X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5991 | Paradigmi Societa Editrice Il Mulino / Unknown | 2035-357X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5992 | Sibirskiy Psikhologicheskiy Zhurnal Tomsk State Un / Unknown | 2411-0809 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5993 | Zeitschrift fur Technikfolgenabschatzung in Theori / Unknown | 2568-020X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5994 | Journal of Politics in Latin America SAGE Publicat / Unknown | 1866-802X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5995 | Mizan Law Review St Mary's University / Unknown | 2309-902X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5996 | Population Review Sociological Demography Press / Unknown | 1549-0955 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5997 | AJO International Elsevier B.V. / Unknown | 2950-2535 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5998 | REVISTA MEXICANA DE CIENCIAS  GEOLOGICAS / CENTRO GEOCIENCIAS UNAM | 2007-2902 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 5999 | Studia Historica, Historia Antigua Ediciones Unive / Unknown | 2530-4100 (ISSN) | Verified | Verified fallback to Open Access Pipeline |
| 6000 | Journal of Pharmaceutical and Biomedical Analysis  / Unknown | 2949-771X (ISSN) | Verified | Verified fallback to Open Access Pipeline |
