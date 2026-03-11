# Brazil Trade Analysis

![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-blue)

State-level analysis of Brazil's international trade performance using 30 years of official trade data from the Brazilian Ministry of Development, Industry and Trade (MDIC/Comex Stat).

---

## Project Overview

This project was born out of two years of working with over 50 companies on their internationalization strategies — helping them enter Brazil or expand from Brazil into new markets. A recurring challenge was the lack of accessible, granular trade data to support market entry decisions. This project builds the infrastructure and analysis to address that gap.

The project is structured in four phases:

- **Phase 1 (Complete):** Build an automated ETL pipeline to download, clean and load 30 years of Brazilian trade data into a PostgreSQL database
- **Phase 2 (In Progress):** Conduct state-level trade analysis covering market dependency, geographic concentration, municipality-level trade hotspots and bilateral trade flow forecasting
- **Phase 3 (Planned):** Python visualisations using matplotlib, seaborn and plotly — charts and exploratory visuals embedded in analysis notebooks
- **Phase 4 (Planned):** Interactive Power BI dashboard for business-facing presentation of trade insights

---

## Technical Stack

- **Python** — pandas, sqlalchemy, psycopg2, requests, dotenv, matplotlib, seaborn, plotly
- **PostgreSQL** — local database hosting 131+ million rows of trade data
- **Power BI** — interactive dashboard for business-facing trade insights
- **Git/GitHub** — version control and project documentation

---

## Repository Structure

```
brazil-state-trade-analysis/
├── SRC/
│   ├── download_data.py            # Automated download of all trade data from MDIC
│   ├── Database_creation.py        # Creates the brazil_trade PostgreSQL database
│   ├── etl_trade.py                # ETL pipeline for core trade tables
│   └── etl_supporting_tables.py    # ETL pipeline for 20 supporting lookup tables
├── Column Naming Convention.md     # Column naming standards used across all tables
├── .gitignore
└── README.md
```

---

## Database Structure

The `brazil_trade` PostgreSQL database contains:

### Core Trade Tables (131+ million rows)

| Table | Description | Rows |
|---|---|---|
| `imp` | Imports by NCM product code (1997-2026) | — |
| `exp` | Exports by NCM product code (1997-2026) | — |
| `imp_mun` | Imports by Municipality (1997-2026) | — |
| `exp_mun` | Exports by Municipality (1997-2026) | — |

### Supporting Lookup Tables (20 tables)

| Category | Tables |
|---|---|
| Product Classifications | `ncm`, `nbm`, `nbm_ncm`, `ncm_sh`, `ncm_cuci`, `ncm_isic`, `ncm_fat_agreg`, `ncm_ppi`, `ncm_ppe`, `ncm_unidade`, `ncm_cgce_n1`, `ncm_cgce_n2`, `ncm_cgce_n3` |
| Countries & Blocs | `pais`, `pais_bloco` |
| States & Municipalities | `uf`, `uf_mun` |
| Logistics | `via`, `urf` |
| Classification Crosswalks | `isic_cuci` |

---

## Phase 1 — ETL Pipeline

### 1. Automated Download (`download_data.py`)
- Downloads all trade data directly from MDIC's official database
- Covers 4 datasets across 1997–2026 (IMP, EXP, IMP_MUN, EXP_MUN) plus all 18 supporting tables
- Smart skip logic prevents re-downloading existing files
- Current year always re-downloaded as it is updated monthly
- SSL handling for Brazilian government server

### 2. Database Creation (`Database_creation.py`)
- Creates the `brazil_trade` PostgreSQL database programmatically
- Credentials managed securely via `.env` file — never hardcoded

### 3. Trade Data ETL (`etl_trade.py`)
- Loads all 4 core trade tables into PostgreSQL
- Chunked processing (100,000 rows at a time) to handle large file sizes
- Automated timestamped backups before any data transformation

### 4. Supporting Tables ETL (`etl_supporting_tables.py`)
- Cleans and loads all 20 supporting lookup tables
- Column renaming follows the convention defined in `Column Naming Convention.md`
- Drops unnecessary columns including Spanish language columns

---

## Phase 2 — Analysis (Coming Soon)

Planned analyses include:

- **Geographic Concentration & Market Dependency** — which countries Brazil depends on and how this has shifted over 30 years
- **State-Level Competitiveness** — which Brazilian states drive exports and in which sectors
- **Municipality-Level Trade Hotspots** — granular analysis of emerging trade municipalities
- **Transport Route & Logistics Analysis** — how Brazilian trade moves and how this varies by product
- **Bilateral Trade Flow Forecasting** — time series forecasting of trade flows with key partners

---

## Phase 3 — Python Visualisations (Planned)

Exploratory and analytical charts embedded in Jupyter notebooks, covering:

- Trade flow trends over 30 years by state and product
- Geographic concentration maps
- State-level export competitiveness charts
- Municipality hotspot visualisations
- Bilateral trade flow forecasting plots

Tools: matplotlib, seaborn, plotly

---

## Phase 4 — Power BI Dashboard (Planned)

An interactive business-facing dashboard built on top of the PostgreSQL database, designed for non-technical stakeholders. Will allow dynamic filtering by state, product category, country, and year.

---

## Data Sources

All data is sourced from official Brazilian government databases:

- **Comex Stat (MDIC)** — [base-de-dados-bruta](https://www.gov.br/mdic/pt-br/assuntos/comercio-exterior/estatisticas/base-de-dados-bruta)
  - Core trade data: imports and exports by NCM and by Municipality (1997–2026)
  - Supporting classification tables: product codes, country codes, state and municipality codes

---

## Setup

### Prerequisites
- Python 3.8+
- PostgreSQL 17
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/Eduardo-kohn/brazil-state-trade-analysis.git

# Install dependencies
pip install pandas sqlalchemy psycopg2-binary python-dotenv requests

# Create a .env file in the root directory with your PostgreSQL credentials
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=brazil_trade
```

### Running the Pipeline

```bash
# Step 1 - Download all data
python SRC/download_data.py

# Step 2 - Create the database
python SRC/Database_creation.py

# Step 3 - Load core trade data
python SRC/etl_trade.py

# Step 4 - Load supporting tables
python SRC/etl_supporting_tables.py
```

---

## Column Naming Convention

All columns across all tables follow a structured naming convention documented in [`Column Naming Convention.md`](./Column%20Naming%20Convention.md).

The convention follows the structure:
```
[description]_[reference]_[specifier]
```
For example: `codigo_ncm`, `nome_pais_ing`, `descricao_sh4`

---

## Author

**Eduardo Kohn**
[LinkedIn](https://www.linkedin.com/in/[your-linkedin-handle]) | [GitHub](https://github.com/Eduardo-kohn)
