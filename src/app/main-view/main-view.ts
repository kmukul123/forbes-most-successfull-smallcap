import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Data, ListData } from '../data';
import { ReusableTable } from '../reusable-table/reusable-table';
import { forkJoin } from 'rxjs';

@Component({
  selector: 'app-main-view',
  standalone: true,
  imports: [CommonModule, ReusableTable],
  templateUrl: './main-view.html',
  styleUrls: ['./main-view.css']
})
export class MainView implements OnInit {
  americasData?: ListData;
  asiaData?: ListData;
  americasColumns: string[] = ['RANK', 'COMPANY', 'INDUSTRY', '52-WEEK RETURN (%)', 'REVENUE (millions USD)', 'TICKER'];
  asiaColumns: string[] = ['Rank', 'Company', 'Country/Territory', 'Industry', 'Sales ($M)', 'Net Income ($M)', 'Market Value ($M)'];

  activeDataSet: 'americas' | 'asia' = 'americas';
  activeTitle = '';
  activeSubHeading = '';

  constructor(private dataService: Data) { }

  ngOnInit(): void {
    forkJoin({
      americas: this.dataService.getAmericasData(),
      asia: this.dataService.getAsiaData()
    }).subscribe(({ americas, asia }) => {
      this.americasData = americas;
      this.asiaData = asia;
      this.setActiveDataSet('americas');
    });
  }

  setActiveDataSet(dataSet: 'americas' | 'asia'): void {
    this.activeDataSet = dataSet;
    const data = dataSet === 'americas' ? this.americasData : this.asiaData;
    if (data) {
      this.activeTitle = data.listName;
      this.activeSubHeading = data.listSubHeading;
    }
  }
}
