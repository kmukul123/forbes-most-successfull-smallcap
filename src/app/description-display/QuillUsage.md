# Description Display Component (description-display)

This component is responsible for displaying and editing company description data, which is stored in a custom tag-based format. It utilizes `ngx-quill` for rich text editing capabilities.

## Architecture Overview

The `DescriptionDisplay` component acts as a container for multiple description fields. Each field can be toggled between a read-only view and an editable rich text editor.

-   **Data Flow:**
    -   `@Input() companyData`: Receives the company data, including descriptions in a custom tag format.
    -   `editableDescription`: An internal object that stores the description content in Quill Delta format for display and editing.
    -   `@Output() onSave`: Emits the updated company data with descriptions converted back to the custom tag format.

-   **Conversion Functions:**
    -   `convertLegacyTextToDelta(text: string)`: Converts the custom tag format string into a Quill Delta object. This is used when loading data into `editableDescription` and when initializing the editor.
    -   `convertDeltaToCustomTags(delta: any)`: Converts a Quill Delta object back into the custom tag format string. This is used before saving the data.

-   **`RichTextEditorComponent` (Wrapper):**
    -   A wrapper component around `ngx-quill`'s `quill-editor`.
    -   Handles the `[content]` input (Quill Delta) and `(contentChange)` output (Quill Delta).
    -   Manages the Quill toolbar and custom format handlers.

## Issues Faced and Solutions Implemented

### 1. Initial Hanging/Freezing of the Application

**Solution:**
-   **Manual `quill.setContents()`:** For the editor to display content correctly, it was necessary to manually call `quill.setContents()` in the `onEditorCreated` callback of `RichTextEditorComponent`. This ensures the content is set after the editor is fully initialized.

### 2. `&nbsp;` Characters in Content

**Problem:** When editing and saving, `&nbsp;` (non-breaking space) characters were appearing in the saved content.

**Diagnosis:** This is a common behavior of Quill when converting HTML to plain text or when handling certain formatting.

**Solution:** The `convertDeltaToCustomTags` function was refined to handle and remove these `&nbsp;` characters during the conversion process from Quill Delta to the custom tag format.

### 3. `[object Object]` in Editor Window

**Problem:** After implementing the conversion logic, the editor window displayed `[object Object]` instead of the actual rich text content.

**Diagnosis:** This indicated a data type mismatch. The `DescriptionDisplay` component was correctly passing Quill Delta objects to `RichTextEditorComponent`, but the `quill-editor` inside `RichTextEditorComponent` was not correctly interpreting them as Delta objects.

**Solution:**
-   **Explicit `[format]="'object'"`:** Added `[format]="'object'"` to the `<quill-editor>` in `rich-text-editor.html`. This explicitly tells `ngx-quill` to treat the `content` as a Delta object.
-   **Updated `content` types:** Ensured that the `@Input() content` and `@Output() contentChange` in `rich-text-editor.ts` were typed as `any` (or `object`) to correctly handle Quill Delta objects.
-   **One-way binding with `(onContentChanged)`:** Switched from `[(ngModel)]` to `[content]` and `(onContentChanged)` in `rich-text-editor.html`. This provides more explicit control over the data flow and ensures that the `contentChange` event emits the full Delta object.

### 4. Persistent Hanging / Infinite Loop

**Problem:** Despite previous fixes, the application continued to hang when entering edit mode, with console logs showing repeated `ngOnChanges` and `onQuillContentChanged` events.

**Diagnosis:** This was a classic Angular change detection infinite loop. The `RichTextEditorComponent` was emitting `onQuillContentChanged` (even when content was set programmatically with `'silent'`), which would trigger `ngOnChanges` in the parent (`DescriptionDisplay`), causing the parent to re-evaluate and potentially re-send the same content to the child, thus creating a continuous feedback cycle.

**Solution:**
-   **Removed `(onContentChanged)` from `rich-text-editor.html`:** This completely decoupled the `rich-text-editor` from automatically emitting content changes back to the parent.
-   **Removed `contentChange` EventEmitter from `rich-text-editor.ts`:** The `RichTextEditorComponent` no longer has an output for content changes.
-   **Removed `ngOnChanges` from `rich-text-editor.ts`:** The `RichTextEditorComponent` no longer reacts to changes in its `@Input() content` by setting the editor's content. Instead, the parent component is responsible for explicitly pushing content to the editor.
-   **Introduced `setEditorContent(content: any)` method in `rich-text-editor.ts`:** This new method allows the parent component to explicitly set the editor's content programmatically, using `'silent'` to prevent unwanted events.
-   **Introduced `getEditorContent(): any` method in `rich-text-editor.ts`:** This method allows the parent component to explicitly retrieve the editor's current content when needed (e.g., on save).
-   **Parent (`DescriptionDisplay`) now explicitly pushes and pulls content:**
    -   When entering edit mode, `DescriptionDisplay` iterates through its `richTextEditors` (using `@ViewChildren`) and calls `setEditorContent()` on each instance to populate them.
    -   When saving, `DescriptionDisplay` iterates through its `richTextEditors` and calls `getEditorContent()` on each instance to retrieve the updated content.

This establishes a strict, controlled one-way data flow (parent pushes, parent pulls) that completely breaks the infinite change detection loop, ensuring stability and performance.

### 5. Editor Content Not Displaying (Content Input Undefined)

**Problem:** After implementing the explicit push/pull data flow, the editor window remained empty when entering edit mode, and console logs showed `RichTextEditorComponent: onEditorCreated - Quill editor created. Content input: undefined`.

**Diagnosis:** This indicated that the `@Input() content` in `RichTextEditorComponent` was `undefined` when the editor was created. This is a common Angular lifecycle issue where the input property might not be fully resolved when `onEditorCreated` fires. While `ngOnChanges` is designed to react to input changes, there might still be subtle timing issues or the editor might not be fully ready to receive content when `ngOnChanges` is triggered.

**Solution:**
-   **Explicit Content Push from Parent:** The most reliable solution was to explicitly push the content from the `DescriptionDisplay` component to the `RichTextEditorComponent` when the edit mode is toggled.
-   **`setTimeout` for `QueryList` population:** A `setTimeout` was used in `DescriptionDisplay`'s `toggleEdit()` method to ensure that the `QueryList` of `RichTextEditorComponent` instances (`richTextEditors`) is fully populated before attempting to call `setEditorContent()` on each editor. This addresses the timing issue where the child components might not be fully rendered and available in the `QueryList` immediately after `*ngIf` makes them visible.
-   **`setEditorContent(content: any)` method in `rich-text-editor.ts`:** This method was added to `RichTextEditorComponent` to provide a direct way for the parent to set the editor's content programmatically, using `'silent'` to prevent unwanted events.

## Current State

The component now correctly:
-   Displays descriptions in read-only mode using `quill-view`.
-   Allows editing of individual description fields using `app-rich-text-editor`.
-   Handles the conversion between the custom tag format and Quill Delta objects for both display and saving, addressing the `&nbsp;` and `[object Object]` issues.
-   The `RichTextEditorComponent` is now correctly configured to work with Quill Delta objects, and the data flow is explicitly managed by the parent component to prevent infinite loops.