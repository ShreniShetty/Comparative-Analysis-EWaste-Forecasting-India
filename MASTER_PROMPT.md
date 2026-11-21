# MASTER PROMPT: Comparative Analysis of Predictive Models for E-Waste Generation Forecasting in India

## 1. PROJECT IDENTITY & SCOPE
You are continuing development, analysis, and presentation work on the project:
**"Comparative Analysis of Predictive Models for E-Waste Generation Forecasting in India"**

This project investigates national e-waste generation trajectories in India, audits official government sources (CPCB, MoEFCC, Lok Sabha/Rajya Sabha parliamentary unstarred questions, PIB), builds and validates 7 predictive time-series and machine learning models under strict rolling-origin backtesting, performs robustness stress tests, generates multi-model forecasts through FY 2030–31, and packages the outputs into interactive dashboards, Power BI data models, and academic documentation.

---

## 2. STRICT CONSTRAINTS & NON-NEGOTIABLE RULES
1. **NO INDIVIDUAL AUTHOR / STUDENT ATTRIBUTION:**
   - NEVER mention student names, individual team members, author lists, roll numbers, or personal credentials anywhere in code, markdown documentation, reports, slides, or commit messages. Refer strictly to the project itself or the "Enterprise Information Systems (EIS) Forecasting System".
2. **PROJECT TITLE INTEGRITY:**
   - Do NOT modify or shorten the project title: *"Comparative Analysis of Predictive Models for E-Waste Generation Forecasting in India"*.
3. **DATA INTEGRITY & GROUND TRUTH:**
   - The historical ground truth is an official national time-series of $n=8$ annual observations (FY 2017–18 to FY 2024–25).
   - NEVER fabricate, interpolate, or hallucinate missing data points.
   - NEVER treat external commercial/forward-looking forecasts (e.g., ASSOCHAM-EY, NITI Aayog 14 MMT projections) as historical ground-truth training data. They are benchmark targets only.
4. **VALIDATION RIGOR:**
   - NEVER use randomized $k$-fold cross-validation or any technique that leaks future observations into past training sets. All model evaluations must follow strict chronological rolling-origin backtesting.

---

## 3. REPOSITORY & ENVIRONMENT CONFIGURATION
- **Local Project Path:** `c:\Users\aryan\Desktop\Classroom\Projects\EIS`
- **Operating System / Shell:** Windows 11 / PowerShell (`pwsh`)
- **Python Runtime:** Python 3.11 (`C:\Users\aryan\AppData\Local\Programs\Python\Python311\python.exe`)
- **Remote Git Repository (PUBLIC):** `https://github.com/aryannlodha/Comparative-Analysis-EWaste-Forecasting-India.git`
- **Active Git Branch:** `main` (tracked to `origin/main`)
- **Dependencies (`requirements.txt`):**
  - `pandas`, `numpy`, `scikit-learn`, `statsmodels`, `xgboost`, `openpyxl`, `matplotlib`, `python-pptx` (optional for slides)

### Git Quick Commands:
```powershell
# Check current repo status
git status

# Add changes and commit (strictly no author names in commit messages)
git add .
git commit -m "Update project deliverables and reports"
git push origin main
```

---

## 4. REPOSITORY ARCHITECTURE & DIRECTORY MAP
```
EIS/
├── data/
│   ├── raw/                              # Original Excel workbooks (CPCB, PIB, Rajya Sabha data)
│   └── processed/
│       ├── national_ewaste_full.csv      # Unified 8-year dataset (FY 2017-18 to FY 2024-25)
│       ├── national_ewaste_2016rules.csv # 6-year segment under 2016 EPR regime
│       ├── national_ewaste_2022rules.csv # 2-year segment under 2022 EPR regime
│       ├── external_benchmarks.csv       # External projections (ASSOCHAM, MeitY, NITI Aayog)
│       └── data_dictionary.csv           # Schema metadata
├── src/
│   ├── 01_inspect_and_audit.py           # Phase 1: Ingestion & discrepancy detection
│   ├── 02_prepare_data.py                # Phase 2: Cleaning, harmonization & framework flag
│   ├── 03_train_evaluate_forecast.py     # Master pipeline: Phases 3-7 (models, backtest, robustness, forecasts)
│   ├── generate_interactive_dashboard.py # Generates standalone HTML5/JS dashboard
│   ├── inspect_workbooks.py              # Modular raw data inspector
│   ├── audit_data.py                     # Modular audit runner
│   ├── prepare_data.py                   # Modular feature engineer
│   ├── train_models.py                   # Modular model trainer
│   ├── evaluate_models.py                # Modular backtest evaluator
│   ├── robustness_tests.py               # Modular stress tester
│   ├── generate_forecasts.py             # Modular forecast generator
│   ├── export_results.py                 # Modular CSV exporter
│   └── run_pipeline.py                   # Single-command end-to-end execution script
├── outputs/
│   ├── figures/                          # Publication-grade figures (PNG, 150 DPI)
│   │   ├── fig1_historical_trend.png     # Historical trajectory with regime break
│   │   ├── fig2_backtest_performance.png # Rolling-origin fold comparison
│   │   ├── fig3_model_comparison_metrics.png # MAE, RMSE, MAPE bar charts
│   │   ├── fig4_forecast_projections.png # Projections to FY 2030-31 across models
│   │   ├── fig5_robustness_analysis.png  # Jackknife & noise stress tests
│   │   └── fig6_forecast_fan_chart.png   # Gaussian Process 95% confidence intervals
│   ├── power_bi/                         # Clean relational tables for Power BI ingestion
│   │   ├── data_quality_report.csv       # Discrepancy log
│   │   ├── source_register.csv           # Provenance records
│   │   ├── model_metrics.csv             # MAE, RMSE, MAPE, R2 per model
│   │   ├── model_predictions.csv         # Backtest fold predictions vs actuals
│   │   ├── model_robustness_results.csv  # 4 stress test experiment outputs
│   │   ├── forecast_results.csv          # Multi-model forecasts through 2030-31
│   │   └── POWER_BI_DASHBOARD_GUIDE.md   # Star Schema, DAX formulas, visual page layout
│   ├── dashboard/
│   │   └── index.html                    # Responsive 5-page Bootstrap + Chart.js dashboard
│   └── reports/
│       ├── DATA_AUDIT_REPORT.md          # Formal data verification & source audit report
│       ├── RESEARCH_REPORT.md            # Comprehensive academic research monograph
│       └── cross_source_comparison.csv   # Source conflict reconciliation matrix
├── run_dashboard.py                      # Local HTTP server launcher for HTML dashboard
├── data_dictionary.md                    # Data fields dictionary
├── methodology.md                        # Formal mathematical model formulation
├── source_register.csv                   # Source provenance file
├── requirements.txt                      # Python library dependencies
└── README.md                             # GitHub landing page with architecture & findings
```

---

## 5. CORE EMPIRICAL FINDINGS & AUDIT RESOLUTIONS
1. **Official Data Discrepancies Resolved:**
   - **FY 2016–17 (23,330 MT):** Identified as dismantled/recycled volume under initial pilot rules, not national generation. Dropped to avoid severe positive skew.
   - **Solid Waste Misclassification:** State-level "TPD" (Tonnes Per Day) records in preliminary workbooks were verified as Municipal Solid Waste (MSW), not electronic waste. State panel models were appropriately rejected to prevent empirical contamination.
   - **Regulatory Regime Shift (2016 vs 2022 Rules):** The 2022 Rules took effect in FY 2023–24. CPCB uses registered producers’ sales and average equipment lifetimes to estimate generation. It reported 1,254,286.55 tonnes in FY 2023–24 and 1,397,955.59 tonnes in FY 2024–25. The share of the earlier decline attributable to reporting changes is unknown. [MoEFCC parliamentary reply](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2147876)
   - **Feature Engineering:** A binary `framework_flag` (0 for FY 2017–18 to 2022–23; 1 for FY 2023–24 onwards) was implemented, reducing four-fold mean absolute error by 21.7%. The two linear models differed only in the final fold, after the first new-framework year entered training.

2. **Model Performance Summary (Rolling-Origin Backtesting, 4 Folds):**
   - **Naive Baseline:** MAE = 190,280 MT | MAPE = 13.7% (Strong near-term benchmark)
   - **ARIMA(1,1,0):** MAE = 214,388 MT | MAPE = 15.5% (Best balanced dynamic model)
   - **Gaussian Process Regression:** MAE = 236,555 MT | MAPE = 16.8% (Model-implied predictive intervals, with untested coverage)
   - **Linear Regression (Framework-Aware):** MAE = 251,994 MT | MAPE = 18.7% (Conditional FY 2030–31 scenario of 2,674,580 tonnes if the fitted trend and reporting framework persist)
   - **Random Forest:** MAE = 323,631 MT | MAPE = 21.2%.
   - **XGBoost:** MAE = 361,350 MT | MAPE = 23.6%. Both fitted tree models return constant future values around 1.43 million tonnes.

3. **Key Robustness Discoveries:**
   - **Jackknife Sensitivity:** FY 2022–23 is the single highest-leverage observation (MAE rises 20.2%, from 686,221 to 824,649 tonnes, if omitted).
   - **Epistemic Uncertainty:** The fitted Gaussian process gives nominal 95% interval half-widths of 466,864 tonnes in FY 2025–26 and 1,451,730 tonnes in FY 2030–31, a 210.9% increase.

---

## 6. WHAT IS FULLY COMPLETE
- [x] Phase 1 Data Audit and Cross-Source Reconciliation Report (`DATA_AUDIT_REPORT.md`).
- [x] Phase 2 Clean Data Pipeline and Feature Engineering (`national_ewaste_full.csv`).
- [x] Phase 3–6 Model Training, Rolling-Origin Evaluation, Robustness Stress Testing, and 2030 Projections (`src/03_train_evaluate_forecast.py`).
- [x] Phase 7 Data Visualizations (6 publication-grade figures in `outputs/figures/`).
- [x] Interactive Decision-Support Web Dashboard (`outputs/dashboard/index.html` + `run_dashboard.py`).
- [x] Complete Power BI specification guide with Star Schema and DAX measures (`POWER_BI_DASHBOARD_GUIDE.md`).
- [x] Full Academic Monograph (`RESEARCH_REPORT.md`) containing literature review, mathematical formulas, empirical findings, and EIS policy implications.
- [x] GitHub Repository clean and synchronized on branch `main`.

---

## 7. WHAT REMAINS TO BE DONE (NEXT DELIVERABLES)
When asked to proceed, assist with any of the following pending deliverables:

1. **Presentation Slide Deck (`.pptx`):**
   - Generate an automated 10–12 slide professional presentation deck using `python-pptx`.
   - Topics: Title & Context, Legislative Architecture (2016 vs 2022 Rules), Data Audit Discoveries, Methodology & Rolling-Origin Backtesting, Comparative Model Metrics, The Machine Learning "Extrapolation Trap", Robustness & Monte Carlo Stress Tests, 2030 National Projections, Enterprise & Infrastructure Recommendations, Limitations & Future Scope.
2. **Oral Defense & Viva Voce Q&A Dossier:**
   - Compile a detailed defense guide for professors/examiners with technical rationales:
     - Why classical time-series out-predicts XGBoost/Random Forest on small $n$.
     - Why state-level panel regression was rejected.
     - Why Deep Learning / LSTM was deliberately avoided ($n=8$ sample size).
     - How CPCB EPR figures reconcile with the UN Global E-waste Monitor (GEM 2024).
3. **Formal College Submission Front-Matter:**
   - Generate formal print-ready academic front-matter (Title Page, Certificate of Originality, Declaration, Abstract, Table of Contents, List of Tables, List of Figures) matching Indian university guidelines.
4. **Pipeline Execution Verification:**
   - Execute and verify the master runner:
     ```powershell
     python src/run_pipeline.py
     ```

---

## 8. IMMEDIATE ACTION REQUIRED
Review the workspace, acknowledge these strict guidelines (especially zero author attribution and project title preservation), and ask the user which of the remaining deliverables they would like to generate first (e.g., Slide Deck, Viva Voce Guide, or Academic Front-Matter).
