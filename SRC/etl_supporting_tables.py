#################### CREDENTIALS ####################
load_dotenv()

DB_USER     = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST     = os.getenv("DB_HOST")
DB_PORT     = os.getenv("DB_PORT")
DB_NAME     = os.getenv("DB_NAME")

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

folder_path = r"C:\Users\e_koh\Downloads\State Analysis\brazil-state-trade-analysis\Data\Supporting Tables"

def read_file(filename):
    filepath = os.path.join(folder_path, filename)
    if filename.endswith('.csv'):
        return pd.read_csv(filepath, encoding='latin1', sep=';')
    else:
        return pd.read_excel(filepath)

def load_to_db(df, table_name):
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Loaded: {table_name} ({len(df):,} rows)")

#################### NBM ####################
df = read_file('NBM.csv')
df.rename(columns={
    'CO_NCM'  : 'codigo_ncm',
    'NO_NBM'  : 'nome_nbm'
}, inplace=True)
load_to_db(df, 'nbm')

#################### NCM_UNIDADE ####################
df = read_file('NCM_UNIDADE.csv')
df.rename(columns={
    'NO_UNID' : 'nome_unidade',
    'SG_UNID' : 'sigla'
}, inplace=True)
load_to_db(df, 'ncm_unidade')

#################### NBM_NCM ####################
df = read_file('NBM_NCM.csv')
df.rename(columns={
    'CO_NBM'  : 'codigo_nbm',
    'CO_NCM'  : 'codigo_ncm'
}, inplace=True)
load_to_db(df, 'nbm_ncm')

#################### NCM_FAT_AGREG ####################
df = read_file('NCM_FAT_AGREG.csv')
df.rename(columns={
    'CO_FAT_AGREG'    : 'codigo_fat_agreg',
    'NO_FAT_AGREG'    : 'categoria_detalhada',
    'NO_FAT_AGREG_GP' : 'categoria_agregada'
}, inplace=True)
load_to_db(df, 'ncm_fat_agreg')

#################### URF ####################
df = read_file('URF.csv')
df.rename(columns={
    'CO_URF' : 'codigo_urf',
    'NO_URF' : 'nome_aduaneira'
}, inplace=True)
# Remove the replicated code and ' - ' from the nome_aduaneira column
# e.g. "123456 - Porto de Santos" → "Porto de Santos"
df['nome_aduaneira'] = df['nome_aduaneira'].str.replace(
    df['codigo_urf'].astype(str) + ' - ', '', regex=False
)
load_to_db(df, 'urf')

#################### NCM_PPI ####################
df = read_file('NCM_PPI.csv')
df.drop(df.columns[2], axis=1, inplace=True)
df.rename(columns={
    'CO_PPI'     : 'codigo_ppi',
    'NO_PPI'     : 'nome_ppi',
    'NO_PPI_ING' : 'nome_ppi_ing'
}, inplace=True)
load_to_db(df, 'ncm_ppi')

#################### NCM_PPE ####################
df = read_file('NCM_PPE.csv')
df.drop(df.columns[2], axis=1, inplace=True)
df.rename(columns={
    'CO_PPE'     : 'codigo_ppe',
    'NO_PPE'     : 'nome_ppe',
    'NO_PPE_ING' : 'nome_ppe_ing'
}, inplace=True)
load_to_db(df, 'ncm_ppe')

#################### ISIC_CUCI ####################
df = read_file('ISIC_CUCI.csv')
df.rename(columns={
    'CO_ISIC_SECAO'  : 'codigo_isic',
    'NO_ISIC_SECAO'  : 'nome_isic',
    'CO_CUCI_GRUPO'  : 'codigo_cuci',
    'NO_CUCI_GRUPO'  : 'nome_cuci'
}, inplace=True)
load_to_db(df, 'isic_cuci')

#################### NCM_CGCE ####################
df = read_file('NCM_CGCE.csv')
df.drop(columns=['NO_CGCE_N3_ESP', 'NO_CGCE_N2_ESP', 'NO_CGCE_N1_ESP'], inplace=True)
df.rename(columns={
    'CO_CGCE_N3'     : 'codigo_n3',
    'NO_CGCE_N3'     : 'categoria_n3',
    'NO_CGCE_N3_ING' : 'categoria_n3_ing',
    'CO_CGCE_N2'     : 'codigo_n2',
    'NO_CGCE_N2'     : 'categoria_n2',
    'NO_CGCE_N2_ING' : 'categoria_n2_ing',
    'CO_CGCE_N1'     : 'codigo_n1',
    'NO_CGCE_N1'     : 'categoria_n1',
    'NO_CGCE_N1_ING' : 'categoria_n1_ing',
}, inplace=True)

# Split into 3 separate tables
df_n1 = df[['codigo_n1', 'categoria_n1', 'categoria_n1_ing']].drop_duplicates()
df_n2 = df[['codigo_n2', 'categoria_n2', 'categoria_n2_ing']].drop_duplicates()
df_n3 = df[['codigo_n3', 'categoria_n3', 'categoria_n3_ing']].drop_duplicates()

load_to_db(df_n1, 'ncm_cgce_n1')
load_to_db(df_n2, 'ncm_cgce_n2')
load_to_db(df_n3, 'ncm_cgce_n3')

#################### VIA ####################
df = read_file('VIA.csv')
df.rename(columns={
    'CO_VIA' : 'codigo_via',
    'NO_VIA' : 'nome_via'
}, inplace=True)
load_to_db(df, 'via')

#################### UF ####################
df = read_file('UF.csv')
df.rename(columns={
    'CO_UF'    : 'codigo_uf',
    'SG_UF'    : 'sigla',
    'NO_UF'    : 'nome_estado',
    'NO_REGIAO': 'nome_regiao'
}, inplace=True)
load_to_db(df, 'uf')

#################### PAIS_BLOCO ####################
df = read_file('PAIS_BLOCO.csv')
df.drop(df.columns[4], axis=1, inplace=True)
df.rename(columns={
    'CO_PAIS'     : 'codigo_pais',
    'CO_BLOCO'    : 'codigo_bloco',
    'NO_BLOCO'    : 'nome_bloco',
    'NO_BLOCO_ING': 'nome_bloco_ing'
}, inplace=True)
load_to_db(df, 'pais_bloco')

#################### NCM_ISIC ####################
df = read_file('NCM_ISIC.csv')
# Delete columns 4, 8, 12, 16 (0-indexed: 3, 7, 11, 15) in reverse order to preserve positions
df.drop(df.columns[[15, 11, 7, 3]], axis=1, inplace=True)
df.rename(columns={
    'CO_ISIC_CLASSE'     : 'codigo_classe',
    'NO_ISIC_CLASSE'     : 'nome_classe',
    'NO_ISIC_CLASSE_ING' : 'nome_classe_ing',
    'CO_ISIC_GRUPO'      : 'codigo_grupo',
    'NO_ISIC_GRUPO'      : 'nome_grupo',
    'NO_ISIC_GRUPO_ING'  : 'nome_grupo_ing',
    'CO_ISIC_DIVISAO'    : 'codigo_divisao',
    'NO_ISIC_DIVISAO'    : 'nome_divisao',
    'NO_ISIC_DIVISAO_ING': 'nome_divisao_ing',
    'CO_ISIC_SECAO'      : 'codigo_secao',
    'NO_ISIC_SECAO'      : 'nome_secao',
    'NO_ISIC_SECAO_ING'  : 'nome_secao_ing'
}, inplace=True)
load_to_db(df, 'ncm_isic')

#################### NCM_CUCI ####################
df = read_file('NCM_CUCI.csv')
df.rename(columns={
    'CO_CUCI_ITEM'   : 'codigo_item',
    'NO_CUCI_ITEM'   : 'nome_item',
    'CO_CUCI_SUB'    : 'codigo_subgrupo',
    'NO_CUCI_SUB'    : 'nome_subgrupo',
    'CO_CUCI_GRUPO'  : 'codigo_grupo',
    'NO_CUCI_GRUPO'  : 'nome_grupo',
    'CO_CUCI_DIVISAO': 'codigo_divisao',
    'NO_CUCI_DIVISAO': 'nome_divisao',
    'CO_CUCI_SEC'    : 'codigo_secao',
    'NO_CUCI_SEC'    : 'nome_secao'
}, inplace=True)
load_to_db(df, 'ncm_cuci')

#################### NCM_SH ####################
df = read_file('NCM_SH.csv')
# Delete columns 3, 7, 11, 15 (0-indexed: 2, 6, 10, 14) in reverse order
df.drop(df.columns[[14, 10, 6, 2]], axis=1, inplace=True)
df.rename(columns={
    'CO_SH6'        : 'codigo_sh6',
    'NO_SH6_POR'    : 'descricao_sh6',
    'NO_SH6_ING'    : 'descricao_sh6_ing',
    'CO_SH4'        : 'codigo_sh4',
    'NO_SH4_POR'    : 'descricao_sh4',
    'NO_SH4_ING'    : 'descricao_sh4_ing',
    'CO_SH2'        : 'codigo_sh2',
    'NO_SH2_POR'    : 'descricao_sh2',
    'NO_SH2_ING'    : 'descricao_sh2_ing',
    'CO_NCM_SECROM' : 'codigo_secao_ncm',
    'NO_SEC_POR'    : 'descricao_secao',
    'NO_SEC_ING'    : 'descricao_secao_ing'
}, inplace=True)
load_to_db(df, 'ncm_sh')

#################### NCM ####################
df = read_file('NCM.csv')
# Delete column 13 (0-indexed: 12)
df.drop(df.columns[12], axis=1, inplace=True)
df.rename(columns={
    'CO_NCM'        : 'codigo_ncm',
    'CO_UNID'       : 'codigo_unidade',
    'CO_SH6'        : 'codigo_sh6',
    'CO_PPE'        : 'codigo_ppe',
    'CO_PPI'        : 'codigo_ppi',
    'CO_FAT_AGREG'  : 'codigo_grupo_agregado',
    'CO_CUCI_ITEM'  : 'codigo_cuci',
    'CO_CGCE_N3'    : 'codigo_cgce',
    'CO_SIIT'       : 'codigo_siit',
    'CO_ISIC_CLASSE': 'codigo_isic',
    'CO_EXP_SUBSET' : 'codigo_subset_exp',
    'NO_NCM_POR'    : 'nome_ncm',
    'NO_NCM_ING'    : 'nome_ncm_ing'
}, inplace=True)
load_to_db(df, 'ncm')

#################### PAIS ####################
df = read_file('PAIS.csv')
# Delete column 6 (0-indexed: 5)
df.drop(df.columns[5], axis=1, inplace=True)
df.rename(columns={
    'CO_PAIS'      : 'codigo_pais',
    'CO_PAIS_ISON3': 'codigo_ison3',
    'CO_PAIS_ISOA3': 'codigo_isoa3',
    'NO_PAIS'      : 'nome_pais',
    'NO_PAIS_ING'  : 'nome_pais_ing'
}, inplace=True)
load_to_db(df, 'pais')

#################### UF_MUN ####################
df = read_file('UF_MUN.csv')
# Delete column 3 (0-indexed: 2)
df.drop(df.columns[2], axis=1, inplace=True)
df.rename(columns={
    'CO_MUN_GEO': 'codigo_municipio',
    'NO_MUN'    : 'nome_municipio',
    'SG_UF'     : 'sigla_uf'
}, inplace=True)
load_to_db(df, 'uf_mun')

print("\nAll supporting tables loaded successfully")
