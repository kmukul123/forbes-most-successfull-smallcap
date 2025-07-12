import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { Data, ListData } from '../data';
import { ReusableTable } from '../reusable-table/reusable-table';
import { forkJoin } from 'rxjs';

@Component({
  selector: 'app-main-view',
  standalone: true,
  imports: [CommonModule, ReusableTable, RouterModule],
  templateUrl: './main-view.html',
  styleUrls: ['./main-view.css']
})
export class MainView implements OnInit {
  americasData?: ListData;
  asiaData?: ListData;
  americasColumns: string[] = ['RANK', 'COMPANY', 'INDUSTRY', '52-WEEK RETURN (%)', 'REVENUE (millions USD)', 'TICKER'];
  asiaColumns: string[] = ['RANK', 'COMPANY', 'COUNTRY/TERRITORY', 'INDUSTRY', 'SALES ($M)', 'NET INCOME ($M)', 'MARKET VALUE ($M)', 'TICKER'];

  activeDataSet: ListData | undefined; // Holds the currently active ListData object
  activeTitle = '';
  activeSubHeading = '';

  constructor(private dataService: Data) { }

  ngOnInit(): void {
    forkJoin({
      americas: this.dataService.getAmericasData(),
      asia: this.dataService.getAsiaData()
    }).subscribe(({ americas, asia }) => {
      console.log('MainView: americas data received:', americas);
      if (americas && americas.listCompanies && americas.listCompanies.length > 0) {
        console.log('MainView: Revenue (MILLIONS USD) from data:', americas.listCompanies[0]['REVENUE (MILLIONS USD)']);
        console.log('MainView: Revenue (millions USD) from data (lowercase):', americas.listCompanies[0]['REVENUE (millions USD)']);
      }
      this.americasData = americas;
      this.asiaData = asia;
      // Initialize with Americas data
      this.setActiveDataSet(this.americasData);
    });
  }

  /**
   * Sets the active dataset based on the provided ListData object.
   * @param data The ListData object to set as active.
   */
  setActiveDataSet(data: ListData | undefined): void {
    this.activeDataSet = data;
    console.log('MainView: activeDataSet being set:', this.activeDataSet);
    if (data) {
      this.activeTitle = data.listName;
      this.activeSubHeading = data.listSubHeading;
    } else {
      this.activeTitle = '';
      this.activeSubHeading = '';
    }
  }
}
