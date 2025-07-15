# Hidden Test Metadata Simplified Guide

## Overview

To simplify the process of creating hidden tests, we have significantly streamlined the structure of metadata.json, keeping only the fields that are actually used by the plugin.

## Simplified Metadata Structure

```json
{
  "id": "exercise_name",
  "title": "Exercise Title", 
  "description": "Brief description of what the exercise requires",
  "hints": [
    "Hint 1: First suggestion for improvement",
    "Hint 2: Second suggestion for improvement",
    "Hint 3: Third suggestion for improvement"
  ]
}
```

## Field Descriptions

- **id**: Unique identifier for the exercise, must match the folder name
- **title**: Title of the exercise, used for display
- **description**: Brief description of the exercise, explaining what students need to accomplish
- **hints**: Array of improvement suggestions that AI will provide when tests fail

## Steps to Create a New Hidden Test

1. Create a new folder under `tests/` directory, the folder name becomes the exercise ID
2. Copy `metadata_template.json` to the new folder and rename it to `metadata.json`
3. Edit `metadata.json` and fill in the corresponding fields
4. Create the test file `test_[exercise_name].py`

## Examples

Refer to the complete examples in `tests/fib/` and `tests/sort/` folders.

## Plugin Usage Instructions

The plugin automatically reads the `hints` field from metadata. When tests fail, the AI will generate improvement suggestions based on these hints and error information.

## Important Notes

- Removed fields include: `difficulty`, `tags`, `function_name`, `function_signature`, `requirements`, `test_cases`, `learning_objectives`
- These fields are not used by the plugin, removing them greatly simplifies metadata writing
- If you need this information, you can provide it through comments in the test files 