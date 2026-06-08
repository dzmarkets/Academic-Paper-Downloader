from src.core.utils import clean_filename, register_discovered_url
from src.network.downloader import download_file

def try_publisher_direct(doi, title, status_label=None):
    """Strategy: Construct direct download link for known open-access publisher DOI prefixes."""
    if not doi:
        return False
    if doi.startswith("http://") or doi.startswith("https://"):
        return False

    doi_lower = doi.lower()
    
    # Define publisher rules mapping DOI prefixes to their direct URL structures
    # and readable names
    rules = [
        # (Prefixes/Keywords, Name, URL Template, Filename Prefix)
        (["10.1007", "10.1186", "10.1134", "10.1057"], "Springer Open / BMC / Pleiades / Palgrave", "https://link.springer.com/content/pdf/{doi}.pdf", "Springer_"),
        (["10.3390"], "MDPI", "https://www.mdpi.com/article/{doi}/pdf", "MDPI_"),
        (["10.3389"], "Frontiers", "https://www.frontiersin.org/articles/{doi}/pdf", "Frontiers_"),
        (["10.1002", "10.1111", "10.22541"], "Wiley (OA)", "https://onlinelibrary.wiley.com/doi/pdf/{doi}", "Wiley_"),
        (["10.1080"], "Taylor & Francis", "https://www.tandfonline.com/doi/pdf/{doi}", "TF_"),
        (["10.1088", "10.3847"], "IOP Science / AAS", "https://iopscience.iop.org/article/{doi}/pdf", "IOP_"),
        (["10.1021"], "ACS (OA)", "https://pubs.acs.org/doi/pdf/{doi}", "ACS_"),
        (["10.1093"], "Oxford Academic", "https://academic.oup.com/doi/pdf/{doi}", "OUP_"),
        (["10.1177"], "Sage (OA)", "https://journals.sagepub.com/doi/pdf/{doi}", "Sage_"),
        (["10.1146"], "Annual Reviews", "https://www.annualreviews.org/doi/pdf/{doi}", "AR_"),
        (["10.1103"], "APS", "https://journals.aps.org/prl/pdf/{doi}", "APS_"),
        (["10.1086"], "University of Chicago Press", "https://www.journals.uchicago.edu/doi/pdf/{doi}", "Chicago_"),
        (["10.1098"], "Royal Society", "https://royalsocietypublishing.org/doi/pdf/{doi}", "Royal_"),
        (["10.1061"], "ASCE", "https://ascelibrary.org/doi/pdf/{doi}", "ASCE_"),
        (["10.1108"], "Emerald", "https://www.emerald.com/insight/content/doi/{doi}/pdf", "Emerald_"),
        (["10.1137"], "SIAM", "https://epubs.siam.org/doi/pdf/{doi}", "SIAM_"),
        (["10.1515"], "De Gruyter", "https://www.degruyter.com/document/doi/{doi}/pdf", "DeGruyter_"),
        (["10.1142"], "World Scientific", "https://www.worldscientific.com/doi/pdf/{doi}", "WorldScientific_"),
        (["10.1089"], "Mary Ann Liebert", "https://www.liebertpub.com/doi/pdf/{doi}", "Liebert_"),
        (["10.1055"], "Georg Thieme", "https://www.thieme-connect.com/products/ejournals/pdf/{doi}.pdf", "Thieme_"),
        (["10.1145"], "ACM", "https://dl.acm.org/doi/pdf/{doi}", "ACM_"),
        (["10.1071"], "CSIRO", "https://www.publish.csiro.au/pdf/{doi}", "CSIRO_"),
        (["10.1152"], "American Physiological Society", "https://journals.physiology.org/doi/pdf/{doi}", "APSPhysio_"),
        (["10.1128"], "American Society for Microbiology", "https://journals.asm.org/doi/pdf/{doi}", "ASM_"),
        (["10.3366"], "Edinburgh University Press", "https://www.euppublishing.com/doi/pdf/{doi}", "EUP_"),
        (["10.1287"], "INFORMS", "https://pubsonline.informs.org/doi/pdf/{doi}", "INFORMS_"),
        (["10.2514"], "AIAA", "https://arc.aiaa.org/doi/pdf/{doi}", "AIAA_"),
    ]
    
    # Handle Nature Nature-based suffixes differently since they use suffix after 10.1038/
    if doi_lower.startswith("10.1038/"):
        suffix = doi.split("10.1038/", 1)[1].strip()
        url = f"https://www.nature.com/articles/{suffix}.pdf"
        name = "Nature"
        filename_prefix = "Nature_"
        
        print(f"\n--- [STRATEGY] Querying {name} Direct Link ---")
        if status_label:
            status_label.config(text=f"Querying {name} Direct...", fg="#00ADB5")
            
        register_discovered_url(url, f"{name} Direct PDF")
        filename = f"{filename_prefix}{clean_filename(title if title else suffix)}.pdf"
        print(f"[INFO] Constructing {name} direct URL: {url}")
        if download_file(url, filename):
            return True
        return False
        
    # Standard prefix rules
    for prefixes, name, url_template, filename_prefix in rules:
        if any(doi_lower.startswith(p + "/") for p in prefixes):
            print(f"\n--- [STRATEGY] Querying {name} Direct Link ---")
            if status_label:
                status_label.config(text=f"Querying {name} Direct...", fg="#00ADB5")
                
            url = url_template.replace("{doi}", doi)
            
            register_discovered_url(url, f"{name} Direct PDF")
            filename = f"{filename_prefix}{clean_filename(title if title else doi.replace('/', '_'))}.pdf"
            print(f"[INFO] Constructing {name} direct URL: {url}")
            if download_file(url, filename):
                return True
            break
            
    return False
