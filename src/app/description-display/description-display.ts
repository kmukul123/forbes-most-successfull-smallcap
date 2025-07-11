import { Component, Input, Output, EventEmitter, OnChanges, SimpleChanges, ViewChildren, QueryList, SimpleChange } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { CompanyData } from '../data';
import { RichTextEditorComponent } from '../rich-text-editor/rich-text-editor';
import { QuillModule } from 'ngx-quill';
import Quill from 'quill';

@Component({
  selector: 'app-description-display',
  standalone: true,
  imports: [CommonModule, FormsModule, RichTextEditorComponent, QuillModule],
  templateUrl: './description-display.html',
  styleUrls: ['./description-display.css']
})
export class DescriptionDisplay implements OnChanges {
  @Input() companyData: CompanyData | null = null; // Input property to receive company data.
  @Output() onSave = new EventEmitter<CompanyData>(); // Output event to notify parent component of saved changes.

  @ViewChildren(RichTextEditorComponent) richTextEditors!: QueryList<RichTextEditorComponent>; // Accesses RichTextEditorComponent instances.

  isEditing = false; // Flag to control edit mode for the description.
  // editableDescription will now hold Delta objects for display and editing.
  // Delta objects are Quill's internal representation of rich text content.
  editableDescription: { [key: string]: any } = {};
  descriptionKeys: string[] = []; // Stores the keys (sections) of the company description.
  // Configuration for the rich text editor toolbar.
  toolbarConfig = {
    toolbar: [
      ['bold', 'italic', 'underline', 'strike'],
      ['link'],
      [{ 'color': [] }, { 'background': [] }],
      ['positive', 'negative', 'highlight'] // Custom formats for positive, negative, and highlight.
    ]
  };

  private converterQuill: Quill; // Internal Quill instance for HTML to Delta conversion.

  constructor() {
    // Initialize a headless Quill instance for converting between HTML and Delta formats.
    const div = document.createElement('div');
    this.converterQuill = new Quill(div);
  }

  /**
   * Lifecycle hook that responds when Angular sets or resets data-bound input properties.
   * Bug Fix: Ensures that when `companyData` changes, the editable description is reset
   * to reflect the new data, preventing stale data from being displayed.
   * @param changes Object of changes to input properties.
   */
  ngOnChanges(changes: SimpleChanges): void {
    if (changes['companyData'] && this.companyData) {
      this.resetEditableDescription();
    }
  }

  /**
   * Toggles the editing mode for the description.
   * When entering edit mode, it ensures the rich text editors are populated with the current content.
   */
  toggleEdit(): void {
    this.isEditing = !this.isEditing;
    if (this.isEditing) {
      // Use setTimeout to ensure richTextEditors QueryList is populated after view has rendered
      // the editable components.
      // This is a common pattern for QueryList access.
      setTimeout(() => {
        this.richTextEditors.forEach(editorComponent => {
          const key = editorComponent.id;
          if (key && this.editableDescription[key]) {
            editorComponent.setEditorContent(this.editableDescription[key]);
          }
        });
      });
    }
  }

  /**
   * Saves the edited description.
   * Converts the Delta content from the rich text editors back into custom tag format
   * and emits the updated CompanyData object to the parent component.
   * Bug Fix: Ensures that after saving, the displayed description remains visible
   * and reflects the saved changes by updating `editableDescription`.
   */
  save(): void {
    if (this.companyData) {
      const descriptionForSave: any = {};
      this.richTextEditors.forEach(editorComponent => {
        const key = editorComponent.id;
        if (key) {
          // Convert Quill Delta content back to custom tag string format for saving.
          descriptionForSave[key] = this.convertDeltaToCustomTags(editorComponent.getEditorContent());
        }
      });
      // Create a new object with updated description and emit it.
      const updatedData = { ...this.companyData, DESCRIPTION: descriptionForSave };
      this.onSave.emit(updatedData);
      
      // Update editableDescription for immediate display in read-only mode after saving.
      // This prevents the description from disappearing or showing old content.
      for (const key of this.descriptionKeys) {
        this.editableDescription[key] = this.convertLegacyTextToDelta(descriptionForSave[key]);
      }
      this.isEditing = false; // Exit edit mode.
    }
  }

  /**
   * Cancels the editing process.
   * Reverts any unsaved changes by resetting the editable description to the original data.
   * Bug Fix: Explicitly calls `resetEditableDescription()` to ensure the view reverts
   * to the original state, preventing the description from disappearing on cancel.
   */
  cancel(): void {
    this.isEditing = false; // Exit edit mode.
    this.resetEditableDescription(); // Revert changes by re-processing the original data.
  }

  /**
   * Populates `editableDescription` with Delta objects converted from `companyData.DESCRIPTION`.
   * This method is called on `ngOnChanges` and `cancel()` to ensure the display is always correct.
   */
  private resetEditableDescription(): void {
    if (this.companyData && this.companyData.DESCRIPTION) {
      this.descriptionKeys = Object.keys(this.companyData.DESCRIPTION);
      const description = this.companyData.DESCRIPTION as any;
      for (const key of this.descriptionKeys) {
        const content = description[key];
        // Convert the plain text content (with custom tags) to Quill Delta format.
        this.editableDescription[key] = this.convertLegacyTextToDelta(content);
      }
    } else {
      this.descriptionKeys = [];
      this.editableDescription = {};
    }
  }

  /**
   * Converts legacy text format (with custom tags like [pos], [neg], [highlight], links) to Quill Delta format.
   * This allows the rich text editor to correctly display and interpret the custom tags.
   * @param text The legacy text content.
   * @returns Quill Delta object.
   */
  private convertLegacyTextToDelta(text: string): any {
    if (!text) {
      return { ops: [] };
    }

    let html = text;
    // Replace custom tags with HTML equivalents for Quill to parse.
    html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    html = html.replace(/\[pos\](.*?)\[\/pos\]/g, '<span class="positive">$1</span>');
    html = html.replace(/\[neg\](.*?)\[\/neg\]/g, '<span class="negative">$1</span>');
    html = html.replace(/\[highlight\](.*?)\[\/highlight\]/g, '<span class="highlight">$1</span>');
    html = html.replace(/\[(.*?)\]\((.*?)\)/g, '<a href="$2" target="_blank">$1</a>');

    // Ensure the HTML is wrapped in a <p> tag if it's not already, for consistent Quill parsing.
    if (!html.startsWith('<p>')) {
      html = `<p>${html}</p>`;
    }

    // Use Quill's clipboard module to convert HTML to Delta.
    const delta = this.converterQuill.clipboard.convert({ html: html });
    return delta;
  }

  /**
   * Converts Quill Delta format back to the custom tag string format for storage.
   * This reverses the process of `convertLegacyTextToDelta`.
   * @param delta The Quill Delta object.
   * @returns String content with custom tags.
   */
  private convertDeltaToCustomTags(delta: any): string {
    if (!delta || !delta.ops) {
      return '';
    }
    // Create a temporary Quill instance to convert Delta to HTML.
    const tempQuill = new Quill(document.createElement('div'));
    tempQuill.setContents(delta);
    let html = tempQuill.root.innerHTML;

    // Replace HTML equivalents back to custom tags.
    html = html.replace(/<p><br><\/p>/g, '\n\n'); // Handle empty paragraphs.
    html = html.replace(/<p>(.*?)<\/p>/g, '$1\n\n'); // Convert paragraphs to newlines.
    html = html.replace(/<strong>(.*?)<\/strong>/g, '**$1**');
    html = html.replace(/<span class="positive">(.*?)<\/span>/g, '[pos]$1[\/pos]');
    html = html.replace(/<span class="negative">(.*?)<\/span>/g, '[neg]$1[\/neg]');
    html = html.replace(/<span class="highlight">(.*?)<\/span>/g, '[highlight]$1[\/highlight]');
    html = html.replace(/<a href="(.*?)" target="_blank">(.*?)<\/a>/g, '[$2]($1)');
    return html.trim(); // Trim any leading/trailing whitespace.
  }

  /**
   * Helper function to convert a snake_case or camelCase string to Title Case with spaces.
   * Used for displaying section headers in a user-friendly format.
   * @param key The string to convert.
   * @returns The converted string in Title Case.
   */
  getTitleCase(key: string): string {
    return key.replace(/_/g, ' ').replace(/\w\S*/g, (txt) => txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase());
  }

  /**
   * Returns an array of keys from companyData, excluding the 'DESCRIPTION' key.
   * @returns An array of strings representing the keys to display.
   */
  getCompanyDataKeys(): string[] {
    if (!this.companyData) {
      return [];
    }
    return Object.keys(this.companyData).filter(key => key !== 'DESCRIPTION');
  }
}