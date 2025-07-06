import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface CompanyData {
    [key: string]: any; // Add index signature for dynamic property access
    RANK?: number;
    COMPANY?: string;
    INDUSTRY?: string;
    "52-WEEK RETURN (%)"?: number | null;
    "REVENUE (millions USD)"?: number | null;
    year: number;
    TICKER?: string;
    DESCRIPTION?: {
        main: string;
        insider_ownership: string;
        debt: string;
        scalability: string;
    };
    INSIDER_OWNERSHIP?: string;
    DEBT?: string;
    SCALABILITY?: string;
    Rank?: number;
    Company?: string;
    "Country/Territory"?: string;
    Industry?: string;
    "Sales ($M)"?: number;
    "Net Income ($M)"?: number;
    "Market Value ($M)"?: number;
}

@Injectable({
  providedIn: 'root'
})
export class Data {

  private americasDataUrl = 'assets/data/Americas_2025.json';
  private asiaDataUrl = 'assets/data/forbes_asia_200_report_2024.json';

  constructor(private http: HttpClient) { }

  getAmericasData(): Observable<CompanyData[]> {
    return this.http.get<CompanyData[]>(this.americasDataUrl);
  }

  getAsiaData(): Observable<CompanyData[]> {
    return this.http.get<CompanyData[]>(this.asiaDataUrl);
  }
}
