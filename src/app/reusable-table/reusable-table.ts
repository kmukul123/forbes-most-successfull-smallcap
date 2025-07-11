import { Component, Input, ViewChild, OnInit, OnChanges, SimpleChanges } from '@angular/core';
import { environment } from '../../environments/environment';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';


import { animate, state, style, transition, trigger } from '@angular/animations';
import { CompanyData } from '../data';

@Component({
  selector: 'app-reusable-table',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterModule],
  templateUrl: './reusable-table.html',
  styleUrls: ['./reusable-table.css'],
  animations: [
    trigger('detailExpand', [
      state('collapsed,void', style({ height: '0px', minHeight: '0' })),
      state('expanded', style({ height: '*' })),
      transition('expanded <=> collapsed', animate('225ms cubic-bezier(0.4, 0.0, 0.2, 1)')),
    ]),
  ],
})
export class ReusableTable implements OnInit, OnChanges {
  @Input() data: CompanyData[] = [];
  @Input() columns: string[] = [];
  @Input() tableTitle: string = '';
  @Input() tableSubHeading: string = '';

  filteredData: CompanyData[] = [];
  filterText: string = '';
  editingCell: { rowIndex: number, key: string, element: HTMLInputElement } | null = null;
  get enableDownloadButton(): boolean {
    return environment.enableDownloadButton;
  }

  ngOnInit(): void {
    console.log('enableDownloadButton:', this.enableDownloadButton);
    this.filteredData = [...this.data]; // Create a shallow copy
  }

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['data']) {
      this.filterData();
    }
  }

  filterData(): void {
    const lowerCaseFilter = this.filterText.trim().toLowerCase();
    if (!lowerCaseFilter) {
      this.filteredData = [...this.data]; // Reset to original data if filter is empty
      return;
    }

    this.filteredData = this.data.filter(companyData => {
      return this.columns.some(key => {
        const value = companyData[key as keyof CompanyData];
        return value && value.toString().toLowerCase().includes(lowerCaseFilter);
      });
    });
  }

  startEdit(event: MouseEvent, rowIndex: number, key: string): void {
    if (key.toLowerCase() === 'rank') {
      return;
    }
    this.editingCell = { rowIndex, key, element: event.target as HTMLInputElement };
  }

  saveEdit(rowIndex: number, key: string, value: any): void {
    const companyData = this.filteredData[rowIndex];
    const originalValue = companyData[key as keyof CompanyData];
    if (typeof originalValue === 'number') {
      (companyData as any)[key] = parseFloat(value) || null;
    } else {
      (companyData as any)[key] = value;
    }
    this.editingCell = null;
  }

  downloadJson(): void {
    const jsonString = JSON.stringify(this.data, null, 2);
    const blob = new Blob([jsonString], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'data.json';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }

  onDescriptionSave(updatedData: CompanyData): void {
    const indexInOriginalData = this.data.findIndex(item => item['TICKER'] === updatedData['TICKER']);
    if (indexInOriginalData !== -1) {
      this.data[indexInOriginalData] = updatedData;
    }

    const indexInFilteredData = this.filteredData.findIndex(item => item['TICKER'] === updatedData['TICKER']);
    if (indexInFilteredData !== -1) {
      this.filteredData[indexInFilteredData] = updatedData;
    }
  }
}