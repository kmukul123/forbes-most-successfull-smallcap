import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

// Defines the structure for a list of companies, including metadata like name and subheading.
export interface ListData {
  listName: string; // The main title of the company list (e.g., "Forbes Asia’s 200 Best Under A Billion").
  listSubHeading: string; // A subheading or date associated with the list (e.g., "AUGUST 06, 2024").
  listCompanies: CompanyData[]; // An array of company data objects within this list.
}

// Defines the structure for individual company data.
// Uses an index signature to allow for flexible property access, as column names can vary.
export interface CompanyData {
    [key: string]: any; // Allows accessing properties dynamically, e.g., company["RANK"].
    RANK?: number; // Optional rank of the company.
    COMPANY?: string; // Optional company name.
    INDUSTRY?: string; // Optional industry of the company.
    '52-WEEK RETURN (%)'?: number; // Optional 52-week return percentage.
    'REVENUE (millions USD)'?: number; // Optional revenue in millions USD.
    year?: number; // Optional year of the data.
    TICKER?: string; // Optional stock ticker symbol.
    DESCRIPTION?: { // Optional object containing various descriptions of the company.
        [key: string]: string; // Dynamic keys for different description sections (e.g., "overview", "insider_ownership").
    };
}

@Injectable({
    providedIn: 'root'
})
export class Data {
    // URLs for fetching company data from JSON files.
    private americasDataUrl = 'assets/data/Americas_2025.json';
    private asiaDataUrl = 'assets/data/forbes_asia_200_report_2024.json';

  constructor(private http: HttpClient) { }

  // Fetches the Americas companies data.
  // Returns an Observable of ListData, which includes list metadata and company array.
  getAmericasData(): Observable<ListData> {
    return this.http.get<ListData>(this.americasDataUrl);
  }

  // Fetches the Asia companies data.
  // Returns an Observable of ListData, which includes list metadata and company array.
  getAsiaData(): Observable<ListData> {
    return this.http.get<ListData>(this.asiaDataUrl);
  }
}

