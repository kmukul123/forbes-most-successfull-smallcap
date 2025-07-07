import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface ListData {
  listName: string;
  listSubHeading: string;
  listCompanies: CompanyData[];
}

export interface CompanyData {
    [key: string]: any; // Add index signature for dynamic property access
    RANK?: number;
    COMPANY?: string;
    INDUSTRY?: string;
    '52-WEEK RETURN (%)'?: number;
    'REVENUE (millions USD)'?: number;
    year?: number;
    TICKER?: string;
    DESCRIPTION?: {
        [key: string]: string;
    };
}

@Injectable({
    providedIn: 'root'
})
export class Data {
    private americasDataUrl = 'assets/data/Americas_2025.json';
    private asiaDataUrl = 'assets/data/forbes_asia_200_report_2024.json';

  constructor(private http: HttpClient) { }

  getAmericasData(): Observable<ListData> {
    return this.http.get<ListData>(this.americasDataUrl);
  }

  getAsiaData(): Observable<ListData> {
    return this.http.get<ListData>(this.asiaDataUrl);
  }
}

