# Data Reorganization Log

This document details the changes made to the JSON data files by the `reorganize_data.py` script.

## Purpose of the Reorganization

The primary goal of this data reorganization was to establish a single source of truth for detailed company information and to streamline the Forbes list data. Previously, detailed company descriptions and some common attributes were duplicated across multiple list files. This new structure improves data consistency, reduces redundancy, and makes the data more efficient to manage and consume.

## Changes Made

### 1. Creation of `companies.json`

A new file, `companies.json`, has been created. This file now serves as the central repository for all detailed company information. It contains an array of JSON objects, where each object represents a unique company and includes the following fields:

*   `TICKER`: The stock ticker symbol (serves as a unique identifier).
*   `COMPANY`: The company's name.
*   `INDUSTRY`: The industry sector the company belongs to.
*   `52-WEEK RETURN (%)`: The company's 52-week stock return.
*   `REVENUE (millions USD)`: The company's revenue in millions of USD.
*   `DESCRIPTION`: A nested object containing detailed descriptions, including:
    *   `overview`
    *   `insider_ownership`
    *   `balancesheet`
    *   `moat`
    *   `roic_roce`
    *   `scalability`
    *   `stock_dilutions_buybacks`
    *   (All keys within `DESCRIPTION` are now consistently uppercase in the normalized data consumed by the application).

### 2. Modification of `Americas_2025.json` and `forbes_asia_200_report_2024.json`

The original list files (`Americas_2025.json` and `forbes_asia_200_report_2024.json`) have been modified to be leaner. They now contain only the information specific to their respective Forbes lists, with a reference to the detailed company data via the `TICKER`.

For each company in the `listCompanies` array within these files, the following fields are retained:

*   `RANK`: The company's rank within that specific Forbes list.
*   `TICKER`: The stock ticker symbol (acting as a foreign key to `companies.json`).
*   `year`: The year of the Forbes list.

All other detailed company information (COMPANY, INDUSTRY, 52-WEEK RETURN (%), REVENUE (millions USD), and DESCRIPTION) has been moved to `companies.json`.

### Rationale

This reorganization adheres to data normalization principles, ensuring that:

*   **Data Redundancy is Reduced:** Company details are stored only once in `companies.json`.
*   **Data Consistency is Improved:** Updates to company information only need to be made in one place.
*   **Data Management is Simplified:** It's easier to maintain and extend company-specific data independently of the list data.
*   **Application Efficiency:** The application can fetch only the necessary list data and then retrieve detailed company information on demand, potentially reducing initial load times for list views.