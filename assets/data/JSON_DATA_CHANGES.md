# JSON Data Restructuring Documentation

This document outlines the changes made to the stock data JSON files within this project.

## Objective

The primary objective was to centralize detailed stock information into a single `stocks.json` file while retaining only essential identifying information (`Rank`, `year`, `TICKER`/`Ticker`) in the original source files (`Americas_2025.json` and `forbes_asia_200_report_2024.json`). This approach aims to improve data management and prevent data duplication.

## Changes Implemented

1.  **Centralization to `stocks.json`:**
    *   All comprehensive company data, including detailed descriptions, financial metrics, and other relevant fields, from both `Americas_2025.json` and `forbes_asia_200_report_2024.json` has been extracted and consolidated into `src/assets/data/stocks.json`.
    *   Each entry in `stocks.json` is keyed by its `TICKER` (or `Ticker`) for easy lookup.

2.  **Pruning of Original Files:**
    *   The `listCompanies` array within `src/assets/data/Americas_2025.json` and `src/assets/data/forbes_asia_200_report_2024.json` has been modified.
    *   Each company object in these original files now contains only the `Rank`, `year`, and `TICKER` (or `Ticker`) fields.
    *   All other company-specific details (e.g., `COMPANY`, `INDUSTRY`, `DESCRIPTION`, financial figures) have been removed from these original files.
    *   The top-level metadata (e.g., `listName`, `listCode`, `columns`, `listSubHeading`) in the original files has been preserved.

3.  **Data Transformation Details:**
    *   **Ticker Key Consistency:** The script handles variations in ticker key casing (`TICKER` vs. `Ticker`) across the source files.
    *   **Description Field:** The nested `overview` sub-key within the `DESCRIPTION` field from the original files has been flattened and its content directly assigned to the `DESCRIPTION` field in `stocks.json`.
    *   **Financial Data Keys:** Differences in financial data keys (`REVENUE (millions USD)` in Americas, `Sales ($M)`, `Net Income ($M)`, `Market Value ($M)` in Asia) have been mapped appropriately to their respective fields in `stocks.json`.
    *   **Country/Territory:** For companies from `Americas_2025.json`, the `Country/Territory` field is explicitly set to "USA" in `stocks.json`.
    *   **Duplicate Ticker Handling:** For duplicate tickers found across or within the source files (e.g., `5248.KL` in `forbes_asia_200_report_2024.json`), the data from the *last encountered entry* for that ticker is retained in `stocks.json` ("last one wins" logic).

## Verification

Before pruning the original files, a C# verification tool (`JsonVerificationTool`) was used to confirm that all data from the original source files was correctly extracted and transformed into `stocks.json`. This ensured data integrity and prevented any loss of information during the restructuring process.

## File Locations

*   **Original Source Files (now pruned):**
    *   `src/assets/data/Americas_2025.json`
    *   `src/assets/data/forbes_asia_200_report_2024.json`
*   **Consolidated Stock Data:**
    *   `src/assets/data/stocks.json`
