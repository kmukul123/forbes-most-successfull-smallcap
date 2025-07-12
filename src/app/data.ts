import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { map } from 'rxjs/operators';

// Defines the structure for a list of companies, including metadata like name and subheading.
export interface ListData {
  listName: string; // The main title of the company list (e.g., "Forbes Asia’s 200 Best Under A Billion").
  listSubHeading: string; // A subheading or date associated with the list (e.g., "AUGUST 06, 2024").
  listCode: string; // Unique identifier for the list (e.g., 'americas', 'asia')
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
    'REVENUE (MILLIONS USD)'?: number; // Optional revenue in millions USD.
    year?: number; // Optional year of the data.
    TICKER?: string; // Optional stock ticker symbol.
    DESCRIPTION?: { // Optional object containing various descriptions of the company.
        [key: string]: string; // Dynamic keys for different description sections (e.g., "overview", "insider_ownership").
    };
}

function normalizeData(data: ListData): ListData {
  const normalizedCompanies = data.listCompanies.map(company => normalizeKeysToUppercase(company));
  return { ...data, listCompanies: normalizedCompanies, listCode: data.listCode };
}

function normalizeKeysToUppercase(obj: any): any {
  if (typeof obj !== 'object' || obj === null) {
    return obj;
  }

  if (Array.isArray(obj)) {
    return obj.map(item => normalizeKeysToUppercase(item));
  }

  const newObj: { [key: string]: any } = {};
  for (const key in obj) {
    if (Object.prototype.hasOwnProperty.call(obj, key)) {
      const newKey = key.toUpperCase();
      newObj[newKey] = normalizeKeysToUppercase(obj[key]);
    }
  }
  return newObj;
}

export { normalizeData, normalizeKeysToUppercase };

@Injectable({
    providedIn: 'root'
})
export class Data {
    // URLs for fetching company data from JSON files.
    private americasDataUrl = 'assets/data/Americas_2025.json';
    private asiaDataUrl = 'assets/data/forbes_asia_200_report_2024.json';

    // In-memory cache for fetched data to prevent re-fetching and persist edits.
    private _americasData: ListData | null = null;
    private _asiaData: ListData | null = null;

  constructor(private http: HttpClient) { }

  /**
   * Fetches the Americas companies data.
   * If data is already in cache, returns it immediately. Otherwise, fetches from JSON and caches it.
   * @returns An Observable of ListData, which includes list metadata and company array.
   */
  getAmericasData(): Observable<ListData> {
    if (this._americasData) {
      return of(this._americasData);
    }
    return this.http.get<ListData>(this.americasDataUrl).pipe(
      map(data => {
        this._americasData = normalizeData(data);
        return this._americasData;
      })
    );
  }

  /**
   * Fetches the Asia companies data.
   * If data is already in cache, returns it immediately. Otherwise, fetches from JSON and caches it.
   * @returns An Observable of ListData, which includes list metadata and company array.
   */
  getAsiaData(): Observable<ListData> {
    if (this._asiaData) {
      return of(this._asiaData);
    }
    return this.http.get<ListData>(this.asiaDataUrl).pipe(
      map(data => {
        this._asiaData = normalizeData(data);
        return this._asiaData;
      })
    );
  }

  /**
   * Retrieves the ListData object for a given listCode.
   * @param listCode The unique identifier for the list (e.g., 'Forbes_America_SmallCap_2024', 'Forbes_Under_A_Billion_Asia_2024').
   * @returns An Observable of ListData or undefined if the listCode is not recognized.
   */
  getListData(listCode: string): Observable<ListData | undefined> {
    if (listCode === 'Forbes_America_SmallCap_2024') {
      return this.getAmericasData();
    } else if (listCode.toLowerCase() === 'Forbes_Under_A_Billion_Asia_2024'.toLowerCase()) {
      return this.getAsiaData();
    }
    return of(undefined);
  }

  /**
   * Updates a company's data in the in-memory cache within its specific list.
   * It searches for the company by its TICKER within the specified listCode.
   * @param updatedCompany The CompanyData object with updated information.
   * @param listCode The list code (e.g., 'americas', 'asia') where the company belongs.
   */
  updateCompanyData(updatedCompany: CompanyData, listCode: string): void {
    const normalizedUpdatedCompany = normalizeKeysToUppercase(updatedCompany);

    if (listCode.toLowerCase() === 'Forbes_America_SmallCap_2024'.toLowerCase() && this._americasData) {
      const index = this._americasData.listCompanies.findIndex(c => c.TICKER === normalizedUpdatedCompany.TICKER);
      if (index !== -1) {
        this._americasData.listCompanies[index] = normalizedUpdatedCompany;
      }
    } else if (listCode.toLowerCase() === 'Forbes_Under_A_Billion_Asia_2024'.toLowerCase() && this._asiaData) {
      const index = this._asiaData.listCompanies.findIndex(c => c.TICKER === normalizedUpdatedCompany.TICKER);
      if (index !== -1) {
        this._asiaData.listCompanies[index] = normalizedUpdatedCompany;
      }
    }
  }
}

