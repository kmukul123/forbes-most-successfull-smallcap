import { Component, Input, ViewChild } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { QuillEditorComponent, QuillModule } from 'ngx-quill';

@Component({
  selector: 'app-rich-text-editor',
  standalone: true,
  imports: [CommonModule, QuillModule, FormsModule],
  templateUrl: './rich-text-editor.html',
  styleUrls: ['./rich-text-editor.css']
})
export class RichTextEditorComponent {
  @ViewChild(QuillEditorComponent, { static: true }) editor!: QuillEditorComponent;

  @Input() id: string = '';
  @Input() toolbarConfig: any = {
    toolbar: [
      ['bold', 'italic', 'underline', 'strike'],
      ['blockquote', 'code-block'],
      [{ 'header': 1 }, { 'header': 2 }],
      [{ 'list': 'ordered'}, { 'list': 'bullet' }],
      [{ 'script': 'sub'}, { 'script': 'super' }],
      [{ 'indent': '-1'}, { 'indent': '+1' }],
      [{ 'direction': 'rtl' }],
      [{ 'size': ['10px', '12px', '14px', '16px', '18px', '20px', '24px', '36px'] }],
      [{ 'header': [1, 2, 3, 4, 5, 6, false] }],
      [{ 'color': [] }, { 'background': [] }],
      [{ 'font': [] }],
      [{ 'align': [] }],
      ['clean'],
      ['link', 'image', 'video'],
      ['positive', 'negative', 'highlight']
    ]
  };

  onEditorCreated(quill: any): void {
    const toolbar = quill.getModule('toolbar');
    toolbar.addHandler('positive', () => this.toggleFormat('positive'));
    toolbar.addHandler('negative', () => this.toggleFormat('negative'));
    toolbar.addHandler('highlight', () => this.toggleFormat('highlight'));
  }

  getEditorContent(): any {
    if (this.editor && this.editor.quillEditor) {
      return this.editor.quillEditor.getContents();
    }
    return null;
  }

  setEditorContent(content: any): void {
    if (this.editor && this.editor.quillEditor) {
      this.editor.quillEditor.setContents(content, 'silent');
    }
  }

  private toggleFormat(format: string): void {
    const quill = this.editor.quillEditor;
    const range = quill.getSelection(true);
    if (range && range.length !== undefined && range.index !== undefined) {
      const currentFormats = quill.getFormat(range.index, range.length);
      if (currentFormats && currentFormats[format]) {
        quill.format(format, false);
      } else {
        quill.format(format, true);
      }
    }
  }
}