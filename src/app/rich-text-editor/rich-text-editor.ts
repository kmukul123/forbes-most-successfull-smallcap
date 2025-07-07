import { Component, Input, Output, EventEmitter, ViewChild, OnChanges, SimpleChanges } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { QuillEditorComponent, QuillModule } from 'ngx-quill';

@Component({
  selector: 'app-rich-text-editor',
  standalone: true,
  imports: [CommonModule, QuillModule, FormsModule],
  template: `<quill-editor [modules]="toolbarConfig" (onEditorCreated)="onEditorCreated($event)" [format]="'object'"></quill-editor>`,
  styleUrls: ['./rich-text-editor.css'] // Assuming you might have a CSS file for this component
})
export class RichTextEditorComponent implements OnChanges {
  @ViewChild(QuillEditorComponent, { static: true }) editor!: QuillEditorComponent;

  // The content input for the editor, expected to be a Quill Delta object.
  @Input() content: any;
  // An ID for the editor instance, useful for identifying it in the parent component.
  @Input() id: string = '';

  // Configuration for the Quill toolbar.
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

  /**
   * ngOnChanges is called when any data-bound input property changes.
   * This is the primary mechanism for pushing content updates to the Quill editor.
   * It includes a comparison to prevent unnecessary updates and break potential infinite loops.
   */
  ngOnChanges(changes: SimpleChanges): void {
    if (changes['content']) {
      console.log('RichTextEditorComponent: ngOnChanges - content input changed', changes['content'].currentValue);
      // Ensure Quill editor instance is available and content is a valid Delta object.
      if (this.editor && this.editor.quillEditor && this.content && this.content.ops) {
        const currentEditorContent = this.editor.quillEditor.getContents();
        // Deep comparison of Delta objects to prevent infinite change detection loops.
        // Only update if the incoming content is different from the editor's current content.
        if (JSON.stringify(currentEditorContent) !== JSON.stringify(this.content)) {
          // Use setTimeout to ensure Quill is fully ready to receive content after Angular's change detection cycle.
          setTimeout(() => {
            // Set content programmatically using 'silent' source to avoid triggering text-change events.
            this.editor.quillEditor.setContents(this.content, 'silent');
            console.log('RichTextEditorComponent: ngOnChanges - Content set via setContents', this.editor.quillEditor.getContents());
          });
        }
      }
    }
  }

  /**
   * Called when the Quill editor instance is created.
   * Used to set up custom toolbar handlers and initial content if available.
   * @param quill The Quill editor instance.
   */
  onEditorCreated(quill: any): void {
    console.log('RichTextEditorComponent: onEditorCreated - Quill editor created.');
    // Initial content setting is primarily handled by ngOnChanges, but this provides a fallback/initial push.
    if (this.content && this.content.ops) {
      setTimeout(() => {
        quill.setContents(this.content, 'silent');
        console.log('RichTextEditorComponent: onEditorCreated - Content set via setContents', quill.getContents());
      });
    }
    // Set up custom toolbar handlers for positive, negative, and highlight formats.
    const toolbar = quill.getModule('toolbar');
    toolbar.addHandler('positive', () => this.toggleFormat('positive'));
    toolbar.addHandler('negative', () => this.toggleFormat('negative'));
    toolbar.addHandler('highlight', () => this.toggleFormat('highlight'));
  }

  /**
   * Retrieves the current content of the Quill editor as a Delta object.
   * This method is called by the parent component when it needs to read the editor's content (e.g., on save).
   * @returns The current content of the editor as a Quill Delta object, or null if the editor is not ready.
   */
  getEditorContent(): any {
    if (this.editor && this.editor.quillEditor) {
      return this.editor.quillEditor.getContents();
    }
    return null;
  }

  /**
   * Explicitly sets the content of the Quill editor.
   * This method is called by the parent component to push content into the editor.
   * It uses 'silent' source to prevent triggering unwanted change events.
   * @param content The content to set, expected to be a Quill Delta object.
   */
  setEditorContent(content: any): void {
    if (this.editor && this.editor.quillEditor) {
      this.editor.quillEditor.setContents(content, 'silent');
      console.log('RichTextEditorComponent: Content set via setEditorContent', this.editor.quillEditor.getContents());
    }
  }

  /**
   * Toggles a custom format (positive, negative, highlight) for the current selection in the editor.
   * @param format The name of the custom format to toggle.
   */
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