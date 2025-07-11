import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { CompanyData, Data } from '../data';
import { CommonModule } from '@angular/common';
import { DescriptionDisplay } from '../description-display/description-display';
import { HammerModule } from '@angular/platform-browser';
import { Location } from '@angular/common';
import { forkJoin } from 'rxjs';

@Component({
  selector: 'app-description-page',
  standalone: true,
  imports: [CommonModule, DescriptionDisplay, HammerModule],
  templateUrl: './description-page.html',
  styleUrls: ['./description-page.css']
})
export class DescriptionPage implements OnInit {
  company: CompanyData | undefined; // The currently displayed company's data
  companyList: CompanyData[] = []; // The full list of companies for navigation
  currentIndex: number = -1; // Index of the current company in the companyList
  listCode: string | null | undefined; // The list code of the current company

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
      this.listCode = params.get('listCode'); // Assign to class property

      if (stockTicker && this.listCode) {
        this.dataService.getListData(this.listCode).subscribe(data => {
          if (data) {
            this.companyList = data.listCompanies;
            this.currentIndex = this.companyList.findIndex(c => c['TICKER'] === stockTicker);
            this.company = this.companyList[this.currentIndex];
          }
        });
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
    if (this.currentIndex > 0 && this.listCode) {
      const previousTicker = this.companyList[this.currentIndex - 1]['TICKER'];
      this.router.navigate(['/description', previousTicker, this.listCode]);
    }
  }

  /**
   * Navigates to the next company in the companyList.
   * Disables the button if already at the last company.
   */
  goToNext(): void {
    if (this.currentIndex < this.companyList.length - 1 && this.listCode) {
      const nextTicker = this.companyList[this.currentIndex + 1]['TICKER'];
      this.router.navigate(['/description', nextTicker, this.listCode]);
    }
  }

  /**
   * Handles the save event from the DescriptionDisplay component.
   * Updates the company data in the Data service's in-memory cache.
   * @param updatedCompany The CompanyData object with updated description.
   */
  onDescriptionSave(updatedCompany: CompanyData): void {
    if (this.listCode) {
      this.dataService.updateCompanyData(updatedCompany, this.listCode);
      // Re-assign company to trigger change detection if needed, though updateCompanyData modifies in place
      this.company = { ...updatedCompany };
    }
  }
}
