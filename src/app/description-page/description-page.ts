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
  company: CompanyData | undefined;
  companyList: CompanyData[] = [];
  currentIndex: number = -1;

  constructor(
    private route: ActivatedRoute, 
    private router: Router,
    private dataService: Data,
    private location: Location
  ) { }

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      const stockTicker = params.get('stockTicker');
      if (stockTicker) {
        forkJoin({
          americas: this.dataService.getAmericasData(),
          asia: this.dataService.getAsiaData()
        }).subscribe(({ americas, asia }) => {
          this.companyList = [...americas.listCompanies, ...asia.listCompanies];
          this.currentIndex = this.companyList.findIndex(c => c['TICKER'] === stockTicker);
          this.company = this.companyList[this.currentIndex];
        });
      }
    });
  }

  goBack(): void {
    this.router.navigate(['/']);
  }

  goToPrevious(): void {
    if (this.currentIndex > 0) {
      const previousTicker = this.companyList[this.currentIndex - 1]['TICKER'];
      this.router.navigate(['/description', previousTicker]);
    }
  }

  goToNext(): void {
    if (this.currentIndex < this.companyList.length - 1) {
      const nextTicker = this.companyList[this.currentIndex + 1]['TICKER'];
      this.router.navigate(['/description', nextTicker]);
    }
  }
}
