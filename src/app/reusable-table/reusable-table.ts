import { Component, Input, ViewChild, OnInit, OnChanges, SimpleChanges } from '@angular/core';
import { environment } from '../../environments/environment';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';


import { animate, state, style, transition, trigger } from '@angular/animations';
import { CompanyData } from '../data';
import { DescriptionDisplay } from '../description-display/description-display';

@Component({
  selector: 'app-reusable-table',
  standalone: true,
  imports: [CommonModule, FormsModule, DescriptionDisplay],
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
  selectedRow: CompanyData | null = null;
  get enableDownloadButton(): boolean {
    return environment.enableDownloadButton;
  }

  ngOnInit(): void {
    console.log('enableDownloadButton:', this.enableDownloadButton);
    this.filterData(); // Initialize filteredData using the filterData method
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

  toggleRow(row: any): void {
    this.selectedRow = this.selectedRow === row ? null : row;
  }

  /**
   * Handles the save event from the DescriptionDisplay component.
   * This method is crucial for ensuring data consistency across the table.
   * Bug Fix: Previously, saving a description would cause the expanded row to collapse
   * and the downloaded JSON to not reflect the changes. This was due to:
   * 1. `selectedRow` not being updated to point to the modified object in `filteredData`.
   * 2. The original `data` array not being updated, leading to outdated downloads.
   * 
   * @param updatedData The CompanyData object with the updated description.
   */
  onDescriptionSave(updatedData: CompanyData): void {
    // Find the index of the updated company in the original data array.
    // It's important to update the original data source (`this.data`) so that
    // subsequent operations (like filtering or downloading) use the latest information.
    const indexInOriginalData = this.data.findIndex(item => item['Rank'] === updatedData['Rank']);
    if (indexInOriginalData !== -1) {
      this.data[indexInOriginalData] = updatedData; // Update the original data array
    }

    // Find the index of the updated company in the currently filtered data array.
    // This ensures that the displayed data is also up-to-date.
    const indexInFilteredData = this.filteredData.findIndex(item => item['Rank'] === updatedData['Rank']);
    if (indexInFilteredData !== -1) {
      this.filteredData[indexInFilteredData] = updatedData; // Update the filtered data array
      // Bug Fix: Update `selectedRow` to point to the newly updated object.
      // This prevents the expanded description from disappearing after saving,
      // as the reference to the object in `filteredData` remains valid.
      this.selectedRow = this.filteredData[indexInFilteredData]; 
    }
  }

  /**
   * Formats a column key into a more readable header string.
   * Converts snake-case or camelCase to Title Case with spaces.
   * @param key The column key string (e.g., '52-WEEK RETURN (%)', 'Net Income ($M)').
   * @returns Formatted string (e.g., '52-Week Return (%)', 'Net Income ($M)').
   */
  formatColumnHeader(key: string): string {
    // Handle specific cases that are already well-formatted or have special characters
    if (key.includes('(') || key.includes('%')) {
      return key; // Return as is if it contains parentheses or percentage sign
    }
    // Replace underscores with spaces, then convert to Title Case
    return key
      .replace(/_/g, ' ')
      .replace(/([A-Z])/g, ' $1') // Add space before capital letters
      .replace(/^./, (str) => str.toUpperCase()); // Capitalize the first letter
  }
}