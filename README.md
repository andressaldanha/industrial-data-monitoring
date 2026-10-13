
<div align="center">

#  Industrial Data Monitoring

### Industrial Data Analytics | Python | Databricks

**Transforming industrial production data into actionable insights.**

![Python](https://img.shields.io/badge/Python-6D28D9?style=for-the-badge&logo=python&logoColor=white)
![Databricks](https://img.shields.io/badge/Databricks-6D28D9?style=for-the-badge&logo=databricks&logoColor=white)
![Data Engineering](https://img.shields.io/badge/Data_Engineering-6D28D9?style=for-the-badge)

</div>

---

## 📌 Project Overview

This project focuses on monitoring industrial production records to identify efficiency deviations and potential inconsistencies in downtime reporting.

It uses Python and Databricks to process production data through a structured data pipeline.

## 🎯 Objectives

- Identify production records with efficiency below 90%.
- Detect records with efficiency above 100%.
- Analyze standard and actual operation times.
- Identify potential missing downtime records.
- Improve data quality and analytical visibility.

## 🏗️ Data Architecture

### Bronze Layer
Raw data ingestion and initial preprocessing.

### Silver Layer
Data cleaning, standardization, and validation.

## 📊 Business Rules

| Indicator | Rule |
|---|---|
| Low efficiency | Below 90% |
| Expected range | 90% to 100% |
| Above expected | Greater than 100% |
| Excess time | MAX(Actual Time - Standard Time, 0) |
| Downtime difference | (Actual Time - Standard Time) - Reported Downtime |

## 🛠️ Technologies

- Python
- Pandas
- Databricks
- Excel / OpenPyXL
- Data Engineering

## 🔒 Data Privacy

This public portfolio project will use synthetic data. No confidential company information or employee records will be published.


## 📊 Processing Results

The Bronze and Silver layers were tested using
12 synthetic industrial production records.

### Efficiency Monitoring

| Classification | Records |
|---|---:|
| Below 90% | 6 |
| Within expected range | 3 |
| Above 100% | 3 |
| **Total** | **12** |

### Downtime Validation

The Silver layer identified **3 records with potential missing downtime**.

These records are flagged for investigation based on
differences between standard time, actual operation time,
and reported downtime.

### Data Pipeline

Excel Dataset → Bronze Layer → Silver Layer

**Bronze:** Data ingestion, column validation and type conversion.

**Silver:** Efficiency classification, excess time calculation
and downtime consistency checks.

> All data used in this public project is synthetic.
> The results do not represent real company operations.


## 🚧 Project Status

**In development**

Upcoming steps include publishing the Bronze and Silver processing code with synthetic examples and documenting the validation results.

---

<div align="center">

Developed by **Andressa Saldanha** 💜

</div>

