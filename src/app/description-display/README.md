# Description Display Component

This component is responsible for rendering and allowing edits to the `DESCRIPTION` field of a company's data.

## Features

*   **Dynamic Section Rendering**: The component dynamically renders sections based on the keys present in the `DESCRIPTION` object of the input `companyData`. This means if you add a new key-value pair to the `DESCRIPTION` object in the JSON, it will automatically be displayed and be editable.
*   **Rich Text Formatting**: It formats the description text, converting custom markdown and tags into styled HTML. The supported formats are:
    *   `**text**` for **bold** text.
    *   `[pos]text[/pos]` for <span class="positive">positive</span> highlights.
    *   `[neg]text[/neg]` for <span class="negative">negative</span> highlights.
    *   `[highlight]text[/highlight]` for <span class="highlight">general</span> highlights.
    *   `[Link Text](URL)` for hyperlinks.
    *   Double newlines for paragraph breaks.
*   **Edit Mode**: The component has an "Edit" mode that allows users to modify the raw description text for each section in text areas.
*   **Save and Cancel**:
    *   **Save**: Emits the updated company data to the parent component.
    *   **Cancel**: Discards any changes and reverts to the display mode.

## Inputs and Outputs

*   **@Input() `companyData`**: The full data object for a single company.
*   **@Output() `onSave`**: An event emitter that outputs the entire updated `companyData` object when the user saves their changes.

## Usage

Integrate the component into a parent template like this:

```html
<app-description-display
  [companyData]="selectedCompany"
  (onSave)="handleDescriptionUpdate($event)">
</app-description-display>
```
