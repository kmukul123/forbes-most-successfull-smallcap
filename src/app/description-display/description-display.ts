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
  @Input() companyData: CompanyData | null = null;
  @Output() onSave = new EventEmitter<CompanyData>();

  @ViewChildren(RichTextEditorComponent) richTextEditors!: QueryList<RichTextEditorComponent>;

  isEditing = false;
  // editableDescription will now hold Delta objects for display and editing
  editableDescription: { [key: string]: any } = {};
  descriptionKeys: string[] = [];
  toolbarConfig = {
    toolbar: [
      ['bold', 'italic', 'underline', 'strike'],
      ['link'],
      [{ 'color': [] }, { 'background': [] }],
      ['positive', 'negative', 'highlight']
    ]
  };

  private converterQuill: Quill;

  constructor() {
    const div = document.createElement('div');
    this.converterQuill = new Quill(div);
  }

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['companyData'] && this.companyData && this.companyData.DESCRIPTION) {
      this.descriptionKeys = Object.keys(this.companyData.DESCRIPTION);
      const description = this.companyData.DESCRIPTION as any;
      for (const key of this.descriptionKeys) {
        const content = description[key];
        this.editableDescription[key] = this.convertLegacyTextToDelta(content);
      }
    }
  }

  toggleEdit(): void {
    this.isEditing = !this.isEditing;
    if (this.isEditing) {
      // When entering edit mode, ensure editors are populated with current content
      // Use setTimeout to ensure richTextEditors QueryList is populated
      setTimeout(() => {
        this.richTextEditors.forEach(editorComponent => {
          const key = editorComponent.id;
          if (key && this.editableDescription[key]) {
            editorComponent.setEditorContent(this.editableDescription[key]);
          }
        });
      });
    } else {
      // When exiting edit mode, revert changes if cancelled
      this.ngOnChanges({ companyData: new SimpleChange(null, this.companyData, false) });
    }
  }

  save(): void {
    if (this.companyData) {
      const descriptionForSave: any = {};
      this.richTextEditors.forEach(editorComponent => {
        const key = editorComponent.id;
        if (key) {
          descriptionForSave[key] = this.convertDeltaToCustomTags(editorComponent.getEditorContent());
        }
      });
      const updatedData = { ...this.companyData, DESCRIPTION: descriptionForSave };
      this.onSave.emit(updatedData);
      // Update editableDescription for immediate display in read-only mode
      for (const key of this.descriptionKeys) {
        this.editableDescription[key] = this.convertLegacyTextToDelta(descriptionForSave[key]);
      }
      this.isEditing = false;
    }
  }

  cancel(): void {
    this.isEditing = false;
    // Revert changes by re-processing the original data
    this.ngOnChanges({ companyData: new SimpleChange(null, this.companyData, false) });
  }

  private convertLegacyTextToDelta(text: string): any {
    if (!text) {
      return { ops: [] };
    }

    let html = text;
    html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    html = html.replace(/\[pos\](.*?)\[\/pos\]/g, '<span class="positive">$1</span>');
    html = html.replace(/\[neg\](.*?)\[\/neg\]/g, '<span class="negative">$1</span>');
    html = html.replace(/\[highlight\](.*?)\[\/highlight\]/g, '<span class="highlight">$1</span>');
    html = html.replace(/\[(.*?)\]\((.*?)\)/g, '<a href="$2" target="_blank">$1</a>');

    if (!html.startsWith('<p>')) {
      html = `<p>${html}</p>`;
    }

    const delta = this.converterQuill.clipboard.convert({ html: html });
    return delta;
  }

  private convertDeltaToCustomTags(delta: any): string {
    if (!delta || !delta.ops) {
      return '';
    }
    const tempQuill = new Quill(document.createElement('div'));
    tempQuill.setContents(delta);
    let html = tempQuill.root.innerHTML;

    html = html.replace(/<p><br><\/p>/g, '\n\n');
    html = html.replace(/<p>(.*?)<\/p>/g, '$1\n\n');
    html = html.replace(/<strong>(.*?)<\/strong>/g, '**$1**');
    html = html.replace(/<span class="positive">(.*?)<\/span>/g, '[pos]$1[\/pos]');
    html = html.replace(/<span class="negative">(.*?)<\/span>/g, '[neg]$1[\/neg]');
    html = html.replace(/<span class="highlight">(.*?)<\/span>/g, '[highlight]$1[\/highlight]');
    html = html.replace(/<a href="(.*?)" target="_blank">(.*?)<\/a>/g, '[$2]($1)');
    return html.trim();
  }

  // Helper to get the title case for the section headers
  getTitleCase(key: string): string {
    return key.replace(/_/g, ' ').replace(/\w\S*/g, (txt) => txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase());
  }
}