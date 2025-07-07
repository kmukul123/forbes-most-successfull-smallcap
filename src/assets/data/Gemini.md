can you update information in @src\assets\data\forbes_asia_200_report_2024.json in the same way as description is there in @Americas_2025.json the different companies. Find information which would be important for someone who wants to buy the whole   company. only update the data in the description in json, rename debt to balancesheet. rename main to overview. and put   numbers like insider ownership debt and cash level in relevant sections along with the links for reference where you have found the exact information. also highlight any important information as per format in   @description_features_reference.md. dont put generic links like generic investor relations page  but link to the page where the exact reference material can be find like link to exact sec filing and link it to exact material found on the page.

yes do this for all the companies and if possible optimize the number of search queries so we  can do it faster

 also add other important numbers like roce, roic, stock dilutions or buybacks etc where you can find them and other information for a buyer of whole company like information about the moat of the company in the relevant section under description json field. Try to put information which is likely to be correct. Anytime you can find any of the above numbers for more then one year it would be good to know them and the trend they are moving to. If you have any other insights for the buyer of the whole company that would be useful please put them

 please update json by adding data for the companies in the json one by one starting from the top. please verify json is valid after every change and fix if it is not valid   Be careful if you have to put special characters in json. if you can validate json via a tool or a script that will be great. THe file is under git and you can stage it after every successful and valid change. do a diff before staging changes and verify the diff that they are expected company only and all good Dont move to the next company before fixing json validation error. Refer to @json_formatting_approaches.md for the previous learnings and errors encountered.

## JSON Data Management Best Practices

When working with JSON files, especially for complex data structures like company descriptions, adhere to the following best practices to avoid common pitfalls:

1.  **Programmatic Modification over Direct String Replacement**:
    *   **Avoid**: Directly using `replace` with large, complex JSON strings for `new_string` and `old_string`. This is highly prone to escaping errors, syntax issues, and makes maintaaining JSON validity extremely difficult.
    *   **Prefer**: Implement a programmatic approach. Read the entire JSON file content, parse it into a data structure (e.g., Python dictionary or JavaScript object), modify the specific fields within the data structure, and then serialize the entire structure back into a JSON string before writing it to the file. This ensures proper escaping and structural integrity.

2.  **Strict JSON Validation**:
    *   Always validate the JSON file after *every* modification. Use a reliable JSON validation tool (e.g., `python -m json.tool` or a similar utility for the relevant language/environment).
    *   Do not proceed to the next step or company until the JSON file is confirmed to be valid. Fix any validation errors immediately.

3.  **Absolute Paths for File Operations**:
    *   Always use absolute paths for all file reading and writing operations (e.g., `read_file`, `write_file`, `replace`). Relative paths can lead to "file not found" errors, especially in dynamic execution environments.
    *   If the absolute path is unknown, use `glob` or `run_shell_command` to locate the file first.

4.  **Incremental Changes and Verification**:
    *   Process changes one company or logical unit at a time.
    *   After each successful modification and validation, use `git diff` to review the changes and `git add` to stage them. This provides a clear audit trail and allows for easier rollback if issues arise.

5.  **Handling Special Characters**:
    *   Be extremely cautious when inserting special characters (e.g., double quotes, newlines, backslashes) into JSON string values. Programmatic serialization (as recommended in point 1) will handle this automatically. If manual string construction is unavoidable, ensure all necessary escaping rules are followed.

By following these guidelines, the process of updating JSON data will be more robust, less error-prone, and easier to debug.