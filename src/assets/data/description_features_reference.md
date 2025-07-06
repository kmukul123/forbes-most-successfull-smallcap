# Description Field Features Reference

This document outlines the various formatting and highlighting features supported within the *nested properties* of the `DESCRIPTION` field in the company data JSON files (e.g., `Americas_2025.json`). The `DESCRIPTION` field is now an object containing `overview`, `insider_ownership`, `balancesheet`, and `scalability` properties. Each of these properties can utilize the formatting described below. These features are processed and rendered by the `formatDescription` function in `reusable-table.ts` to enhance readability and highlight key information.

## Supported Formatting:

1.  **Paragraphs**: Newlines (`\n\n`) within the description text are converted into HTML paragraph breaks (`</p><p>`), ensuring the text is structured into readable paragraphs.

2.  **Bold Text**: Text enclosed within double asterisks (`**text**`) will be rendered as **bold** (e.g., `<strong>text</strong>`). This follows standard Markdown syntax.

## Custom Highlighting Tags:

We use custom tags to apply specific styling (colors) to important phrases within the description. These tags are converted into HTML `<span>` elements with corresponding CSS classes.

1.  **Positive Highlight**: `[pos]Your positive text here[/pos]`
    *   Use this tag to highlight positive aspects, such as strong financial indicators, good management practices, or favorable market conditions.
    *   Example: `[pos]Insider ownership is substantial[/pos]`

2.  **Negative Highlight**: `[neg]Your negative text here[/neg]`
    *   Use this tag to highlight potentially negative aspects, such as high debt, significant risks, or challenging market conditions.
    *   Example: `[neg]moderate amount of debt[/neg]`

3.  **General Highlight**: `[highlight]Your general highlight text here[/highlight]`
    *   Use this tag for general emphasis on important points that are neither strictly positive nor negative, such as unique business models, proprietary technology, or key growth drivers.
    *   Example: `[highlight]Highly scalable business model[/highlight]`

## Links to References:

Links to external references can be embedded directly within the description using standard Markdown link syntax.

1.  **Markdown Link**: `[Link Text](URL)`
    *   The `formatDescription` function will convert this into a clickable HTML `<a>` tag.
    *   Example: `[link to GigaCloud website](http://www.gigacloud.com)`

## Processing in `reusable-table.ts` (`formatDescription` function):

The `formatDescription` function is responsible for parsing the raw text from the JSON `DESCRIPTION` field and converting these custom tags and Markdown elements into appropriate HTML for display. It performs the following transformations:

*   `**text**` -> `<strong>text</strong>`
*   `[pos]...[/pos]` -> `<span class="positive">...</span>`
*   `[neg]...[/neg]` -> `<span class="negative">...</span>`
*   `[highlight]...[/highlight]` -> `<span class="highlight">...</span>`
*   `[link text](URL)` -> `<a href="URL">Link Text</a>`
*   `\n\n` -> `</p><p>` (and wraps the entire output in initial/final `<p>` tags).

This approach allows for flexible and rich text formatting within the description fields while keeping the data structure clean and manageable.
