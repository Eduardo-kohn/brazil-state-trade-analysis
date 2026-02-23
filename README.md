# Brazil State Trade Analysis
A structural and econometric analysis of Brazil’s state-level export performance, integrating trade theory, panel data modeling, and reproducible, production-oriented data engineering to evaluate competitiveness, diversification, and structural determinants of trade outcomes.

## Technical Stack
- Python (pandas, statsmodels, scikit-learn)  
- SQL  
- Power BI  
- Panel econometrics  
- Clustering & diagnostics

## Project Scope:
- State-level panel dataset (multi-year)
- Structural export indicators (concentration & specialization)
- Econometric modeling (cross-section + panel)
- Residual-based performance diagnostics
- Policy-oriented Power BI dashboards

## Research Questions
- What structural factors explain variation in state-level export performance?
- Are Brazilian states overly dependent on specific export sectors?
- Which states outperform expectations given their economic fundamentals?
- How sensitive are exports to macroeconomic conditions?
- What structural patterns emerge from clustering and segmentation analysis?

## Methodological Components
- Data Engineering: cleaning, harmonization, panel construction, transformations  
- Trade Structure Metrics: HHI, RCA, export per capita, trade balance  
- Econometric Modeling: OLS, fixed effects, diagnostics (VIF, residual analysis)  
- Advanced Analytics: Cook’s distance, k-means clustering, simulations  
- Visualization: Interactive Power BI dashboards


## Workflow
1. Problem Framing
    - Define dependent and structural control variables
    - Establish theoretical framework (trade competitiveness & diversification)

2. Data Engineering
    - Source integration (COMEX, IBGE, Central Bank)
    - ETL pipelines in Python
    - SQL-based panel dataset construction
    - Log transformations and lag structures

3. Feature Construction
    - Herfindahl–Hirschman Index (Export Concentration)
    - Revealed Comparative Advantage (Sector Specialization)
    - Export per capita
    - Trade balance indicators
    - Structural productivity controls

4. Econometric Modeling
    - Cross-sectional OLS
    - Fixed effects panel models
    - Robustness checks
    - Multicollinearity diagnostics (VIF)
    - Residual-based performance scoring

5. Advanced Analytics
    - Cook’s distance (influential observations)
    - K-means clustering (structural segmentation)
    - Predictive simulations

6. Visualization & Policy Translation
    - Interactive Power BI dashboards
    - Structural comparison tools
    - Executive summary view for decision-makers

## Structural Indicators
- HHI -> Measure export concentration and vulnerability
- RCA -> Identify sector-level specialization
- Residual Score -> Detect over- and under-performance
- Cluster Assignment -> Structural segmentation of states


## Data Sources
### Primary trade and macroeconomic data sourced from:
- ComexStat
- Instituto Brasileiro de Geografia e Estatística (IBGE)
- Banco Central do Brasil

## Key Outputs
- Structured state-level panel dataset (ready for replication)
- Export concentration and specialization rankings
- State performance scores (residual-based benchmarking)
- Cluster-based structural segmentation
- Executive Power BI dashboard for policy simulation
