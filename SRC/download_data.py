# Disable SSL verification warnings for Brazilian government server
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ── Configuration ─────────────────────────────────────────────────────────────
download_folder = r"C:\Users\e_koh\Downloads\State Analysis\brazil-state-trade-analysis\Data\test"

# Set the year range you want to download
############################## This Value needs to be updates Anually #####################################
START_YEAR = 1997
END_YEAR   = 2026
###########################################################################################################

# Base URLs for each dataset
BASE_NCM = "https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm"
BASE_MUN = "https://balanca.economia.gov.br/balanca/bd/comexstat-bd/mun"

# Files to download per year
datasets = [
    (f"{BASE_NCM}/IMP_{{year}}.csv",     "IMP_{year}.csv"),
    (f"{BASE_NCM}/EXP_{{year}}.csv",     "EXP_{year}.csv"),
    (f"{BASE_MUN}/IMP_{{year}}_MUN.csv", "IMP_{year}_MUN.csv"),
    (f"{BASE_MUN}/EXP_{{year}}_MUN.csv", "EXP_{year}_MUN.csv"),
]

# ── Download function ─────────────────────────────────────────────────────────
def download_file(url, destination, force=False):
    if os.path.exists(destination) and not force:
        print(f"  Skipping (already exists): {os.path.basename(destination)}")
        return

    response = requests.get(url, stream=True, verify=False)

    if response.status_code == 200:
        with open(destination, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        size_mb = os.path.getsize(destination) / (1024 * 1024)
        action = "Replaced" if os.path.exists(destination) else "Downloaded"
        print(f"  {action}: {os.path.basename(destination)} ({size_mb:.1f} MB)")
    else:
        print(f"  Failed ({response.status_code}): {url}")

# Supporting tables (single files, no year loop)
BASE_TAB = "https://balanca.economia.gov.br/balanca/bd/tabelas"

supporting_tables = [
    "NCM.csv",
    "NCM_SH.csv",
    "NCM_CUCI.csv",
    "NCM_ISIC.csv",
    "ISIC_CUCI.csv",
    "NCM_CGCE.csv",
    "NCM_FAT_AGREG.csv",
    "NCM_PPE.csv",
    "NCM_PPI.csv",
    "NCM_UNIDADE.csv",
    "NBM.csv",
    "NBM_NCM.csv",
    "PAIS.csv",
    "PAIS_BLOCO.csv",
    "UF_MUN.csv",
    "UF.csv",
    "VIA.csv",
    "URF.csv",
]

# ── Main ──────────────────────────────────────────────────────────────────────
os.makedirs(download_folder, exist_ok=True)

total_files = (END_YEAR - START_YEAR + 1) * len(datasets)
print(f"Downloading {total_files} files ({START_YEAR}–{END_YEAR})...\n")

for year in range(START_YEAR, END_YEAR + 1):
    print(f"Year {year}:")
    for url_template, filename_template in datasets:
        url         = url_template.format(year=year)
        filename    = filename_template.format(year=year)
        destination = os.path.join(download_folder, filename)
        # Always force re-download for the current year (END_YEAR)
        force = (year == END_YEAR)
        download_file(url, destination, force=force)

print("\nDownloading supporting tables...")
for filename in supporting_tables:
    url         = f"{BASE_TAB}/{filename}"
    destination = os.path.join(download_folder, filename)
    download_file(url, destination)

print("\nAll downloads complete")
