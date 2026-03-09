# Overview
This document defines the column naming convention used across all tables in the brazil_trade database. The goal is to ensure consistency, readability, and ease of use when querying or updating the data.

# Table Names
Table names maintain the same name as the source files in order to facilitate future updates. For example, the file NCM.csv maps to the table ncm in the database.

# Column Name Structure
Column names follow a structured format of up to four words separated by underscores:

                                              [description]_[reference]_[specifier1]_[specifier2]

Each word serves a specific purpose:
| Position	| Role	| Description |
|---|---|---|
| 1st word	| Description	| What type of data the column contains | 
| 2nd word	| Reference	| What the column refers to | 
| 3rd word	| Specifier 1	| Additional context such as aggregation level | 
| 4th word	| Specifier 2	| Language or further detail | 

Not all columns require all four words. Simpler columns may only use two. 

# Description Words
The first word describes the nature of the data in the column:
| Word	| Meaning |
|---|---|
| codigo	| A numeric or alphanumeric identifier code	|
| nome	| A full name	|
| descricao	| A description	|
| categoria	| A category label	|
| sigla	| An abbreviation or acronym	|
| regiao	| A region	|
| estado	| A state	|
| produto	| A product	|
| grupo	| A group	|
| divisao	| A division	|
| secao	| A section	|
| item	| An item	|
| unidade	| A unit of measurement	|

# Reference Words
The second word specifies what the column is referring to:
| Word	| Meaning	|
|---|---|
| ncm	| Nomenclatura Comum do Mercosul	|
| nbm	| Nomenclatura Brasileira de Mercadorias	|
| sh2, sh4, sh6	| Harmonized System at 2, 4 or 6 digit level	|
| pais	| Country	|
| uf	| Brazilian state (Unidade Federativa)	|
| municipio	| Municipality	|
| isic	| International Standard Industrial Classification	|
| cuci	| Standard International Trade Classification (SITC)	|
| cgce	| Classification by Broad Economic Categories	|
| urf	| Customs checkpoint (Unidade da Receita Federal)	|
| via	| Transport route	|
| ppe	| Export Price Index	|
| ppi	| Producer Price Index	|
| fat_agreg	| Aggregated factor	|

# Specifier Words
The third and fourth words add further detail:
| Word	| Meaning	|
|---|---|
| ing	| Column value is in English	|
| n1, n2, n3	| Hierarchy level (e.g. N1 = broadest, N3 = most granular)	|
| agregada	| Aggregated category	|
| detalhada	| Detailed category	|

# Examples
| Column Name	| Description |	Reference	| Specifier |
|---|---|---|---|
| codigo_ncm	| Code	| NCM	| —	|
| nome_ncm_ing	| Name	| NCM	| In English	|
| descricao_sh4_ing	| Description	| SH4	| In English	|
| categoria_n1	| Category	| Level 1	| —	|
| categoria_agregada	| Aggregated | —	| —	—	|
| codigo_subset_exp	| Code	| Export subset	| —	|
| nome_pais_ing	| Name	| Country	| In English	|
| sigla	| Abbreviation	| —	| —	|

# Notes
- All column names are in lowercase 
- Words are separated by underscores 
- Portuguese is the default language — no language specifier is added for Portuguese columns 
- Columns are named based on their content, not their original source name 
