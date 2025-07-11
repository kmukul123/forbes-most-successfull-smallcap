import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CompanyData, Data } from '../data';
import { CommonModule } from '@angular/common';
import { DescriptionDisplay } from '../description-display/description-display';

@Component({
  selector: 'app-description-page',
  standalone: true,
  imports: [CommonModule, DescriptionDisplay],
  templateUrl: './description-page.html',
  styleUrls: ['./description-page.css']
})
export class DescriptionPage implements OnInit {
  company: CompanyData | undefined;

  constructor(private route: ActivatedRoute, private dataService: Data) { }

  ngOnInit(): void {
    const stockTicker = this.route.snapshot.paramMap.get('stockTicker');
    if (stockTicker) {
      this.dataService.getAmericasData().subscribe(data => {
        this.company = data.listCompanies.find(c => c['TICKER'] === stockTicker);
      });
      this.dataService.getAsiaData().subscribe(data => {
        const company = data.listCompanies.find(c => c['TICKER'] === stockTicker);
        if (company) {
          this.company = company;
        }
      });
    }
  }
}
