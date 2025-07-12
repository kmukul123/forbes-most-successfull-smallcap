import { Component, Input, OnInit, OnChanges, SimpleChanges } from '@angular/core';
import { environment } from '../../environments/environment';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { CompanyData } from '../data';

@Component({
  selector: 'app-reusable-table',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterModule],
  templateUrl: './reusable-table.html',
  styleUrls: ['./reusable-table.css'],
})
export class ReusableTable implements OnInit, OnChanges {
  @Input() data: CompanyData[] = [];
  @Input() columns: string[] = [];
  @Input() tableTitle: string = '';
  @Input() tableSubHeading: string = '';
  @Input() listCode: string = ''; // New input for the list code

  filteredData: CompanyData[] = [];
  filterText: string = '';
  editingCell: { rowIndex: number, key: string, element: HTMLInputElement } | null = null;
  get enableDownloadButton(): boolean {
    return environment.enableDownloadButton;
  }

  ngOnInit(): void {
    console.log('enableDownloadButton:', this.enableDownloadButton);
    console.log('ReusableTable ngOnInit - data:', this.data);
    console.log('ReusableTable ngOnInit - columns:', this.columns);
    this.filteredData = [...this.data]; // Create a shallow copy
  }

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['data']) {
      console.log('ReusableTable ngOnChanges - data:', this.data);
      console.log('ReusableTable ngOnChanges - columns:', this.columns);
      this.filteredData = [...this.data]; // Ensure filteredData is updated with new data
      this.filterData();
    }
  }

  filterData(): void {
    console.log('ReusableTable filterData - data:', this.data);
    console.log('ReusableTable filterData - filterText:', this.filterText);
    const lowerCaseFilter = this.filterText.trim().toLowerCase();
    this.filteredData = this.data.filter(companyData => 
      this.columns.some(key => {
        const value = companyData[key as keyof CompanyData];
        return value && value.toString().toLowerCase().includes(lowerCaseFilter);
      })
    );
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
    (companyData as any)[key] = typeof originalValue === 'number' ? parseFloat(value) || null : value;
    this.editingCell = null;
  }

  downloadJson(): void {
    const jsonString = JSON.stringify(this.data, null, 2);
    const blob = new Blob([jsonString], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'data.json';
    a.click();
    URL.revokeObjectURL(url);
  }
}