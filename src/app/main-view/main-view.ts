import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Data, CompanyData } from '../data';
import { ReusableTable } from '../reusable-table/reusable-table';

@Component({
  selector: 'app-main-view',
  standalone: true,
  imports: [CommonModule, ReusableTable],
  templateUrl: './main-view.html',
  styleUrls: ['./main-view.css']
})
export class MainView implements OnInit {
  americasData: CompanyData[] = [];
  asiaData: CompanyData[] = [];
  americasColumns: string[] = ['RANK', 'COMPANY', 'INDUSTRY', '52-WEEK RETURN (%)', 'REVENUE (millions USD)', 'TICKER'];
  asiaColumns: string[] = ['Rank', 'Company', 'Country/Territory', 'Industry', 'Sales ($M)', 'Net Income ($M)', 'Market Value ($M)'];
  
  activeDataSet: 'americas' | 'asia' = 'americas';

  constructor(private dataService: Data) { }

  ngOnInit(): void {
    this.dataService.getAmericasData().subscribe(data => {
      this.americasData = data;
      console.log('loaded Americas Data:', this.americasData.length);
    });
    this.dataService.getAsiaData().subscribe(data => {
      this.asiaData = data;
      console.log('Asia Data:', this.asiaData.length);
    });
  }

  setActiveDataSet(dataSet: 'americas' | 'asia'): void {
    this.activeDataSet = dataSet;
  }
}
