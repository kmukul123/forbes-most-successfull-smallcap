import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { CompanyData, Data } from '../data';
import { CommonModule } from '@angular/common';
import { DescriptionDisplay } from '../description-display/description-display';
import { Location } from '@angular/common';
import { forkJoin } from 'rxjs';

@Component({
  selector: 'app-description-page',
  standalone: true,
  imports: [CommonModule, DescriptionDisplay],
  templateUrl: './description-page.html',
  styleUrls: ['./description-page.css']
})
export class DescriptionPage implements OnInit {
  company: CompanyData | undefined; // The currently displayed company's data
  companyList: CompanyData[] = []; // The full list of companies for navigation
  currentIndex: number = -1; // Index of the current company in the companyList

  constructor(
    private route: ActivatedRoute, // Provides access to route parameters
    private router: Router, // Used for programmatic navigation
    private dataService: Data, // Service to fetch and manage company data
    private location: Location // Used for browser history manipulation (though now navigating directly)
  ) { }

  ngOnInit(): void {
    // Subscribe to route parameter changes to update company data when navigating between descriptions
    this.route.paramMap.subscribe(params => {
      const stockTicker = params.get('stockTicker');
      const listCode = params.get('listCode');
      console.log('DescriptionPage: stockTicker =', stockTicker, 'listCode =', listCode);

      if (stockTicker && listCode) {
        // Fetch only the relevant list based on listCode
        if (listCode === 'Forbes_America_SmallCap_2024') {
          this.dataService.getAmericasData().subscribe(data => {
            console.log('DescriptionPage: Americas Data fetched:', data);
            this.companyList = data.listCompanies;
            this.currentIndex = this.companyList.findIndex(c => c['TICKER'] === stockTicker);
            this.company = this.companyList[this.currentIndex];
            console.log('DescriptionPage: companyList (Americas) =', this.companyList);
            console.log('DescriptionPage: currentIndex (Americas) =', this.currentIndex);
            console.log('DescriptionPage: company (Americas) =', this.company);
          });
        } else if (listCode === 'Forbes_Asia_SmallCap_2024') {
          this.dataService.getAsiaData().subscribe(data => {
            console.log('DescriptionPage: Asia Data fetched:', data);
            this.companyList = data.listCompanies;
            this.currentIndex = this.companyList.findIndex(c => c['TICKER'] === stockTicker);
            this.company = this.companyList[this.currentIndex];
            console.log('DescriptionPage: companyList (Asia) =', this.companyList);
            console.log('DescriptionPage: currentIndex (Asia) =', this.currentIndex);
            console.log('DescriptionPage: company (Asia) =', this.company);
          });
        } else {
          console.log('DescriptionPage: Unknown listCode', listCode);
        }
      } else {
        console.log('DescriptionPage: Missing stockTicker or listCode');
      }
    });
  }

  /**
   * Handles a swipe left gesture to navigate to the next company.
   */
  onSwipeLeft(): void {
    this.goToNext();
  }

  /**
   * Handles a swipe right gesture to navigate to the previous company.
   */
  onSwipeRight(): void {
    this.goToPrevious();
  }

  /**
   * Navigates back to the main list page.
   * Uses router.navigate to ensure a consistent return to the root path.
   */
  goBack(): void {
    this.router.navigate(['/']);
  }

  /**
   * Navigates to the previous company in the companyList.
   * Disables the button if already at the first company.
   */
  goToPrevious(): void {
    if (this.currentIndex > 0) {
      const previousTicker = this.companyList[this.currentIndex - 1]['TICKER'];
      const currentListCode = this.companyList[this.currentIndex]['listCode']; // Get listCode of current company
      this.router.navigate(['/description', previousTicker, currentListCode]);
    }
  }

  /**
   * Navigates to the next company in the companyList.
   * Disables the button if already at the last company.
   */
  goToNext(): void {
    if (this.currentIndex < this.companyList.length - 1) {
      const nextTicker = this.companyList[this.currentIndex + 1]['TICKER'];
      const currentListCode = this.companyList[this.currentIndex]['listCode']; // Get listCode of current company
      this.router.navigate(['/description', nextTicker, currentListCode]);
    }
  }

  /**
   * Handles the save event from the DescriptionDisplay component.
   * Updates the company data in the Data service's in-memory cache.
   * @param updatedCompany The CompanyData object with updated description.
   */
  onDescriptionSave(updatedCompany: CompanyData): void {
    const currentListCode = this.companyList[this.currentIndex]['listCode']; // Get listCode of current company
    this.dataService.updateCompanyData(updatedCompany, currentListCode);
    // Re-assign company to trigger change detection if needed, though updateCompanyData modifies in place
    this.company = { ...updatedCompany };
  }
}
