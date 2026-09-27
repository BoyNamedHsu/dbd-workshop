# Creating Your Case
This directory contains all files that are a part of [A Case of Stolen Candy](https://steamcommunity.com/sharedfiles/filedetails/?id=3807683717) on the Steam Workshop.

The most important file for each case is a `json` file with the fields below. You can open [config.json](/Example%20Case/config.json) to view the `json` file for _A Case of Stolen Candy_ and see how each field is configured. A simplified example of this `json` file is shown below.

```json
{
	"name": "Case Name Here", // Required
	"author": "Your Name Here", // Optional
	"difficulty": "Easy/Medium/Hard", // Optional
    "concepts": ["GROUP BY", "HAVING", "etc"], // Optional
    "database": "Database Name Here", // Required
	"lockedTables": ["table1", "table2", "etc"], // Optional (Recommended)
    "evidenceFiles": ["evidence1.jpg", "evidence2.jpg"], // Required
    "previewImage": "police report 1x1.png", // Optional (Recommended)
    "culpritName": "Culprit Name Here", // Required
    "culpritArrestImage": "culprit.jpg", // Optional
    "arrestWarrant": "warrant.png", // Optional
    "voiceMessage": "message.mp3", // Optional
    "voiceMessageTranscript": "message transcript.txt", // Optional
    "queryHints": [], // Optional
    "caseHints": [] // Optional
}
```
**Note:** Comments are not legal in `json` files and are used exclusively for illustrative purposes.

## Required Fields
| Field | Description |
| :--- | :---------- |
| `name` | The name of your case. |
| `database` | The name of the database file containing tables relevant to your case. Check out the [Scripts](/Scripts/) folder for more information. |
| `evidenceFiles` | A list of image files related to the case. At least one image is required. Images should be no larger than 1000x1000. |
| `culpritName` | The name of the culprit to be arrested. |

## Optional Fields
| Field | Description |
| :--- | :---------- |
| `author` | The name of the person submitting the report (that's you!). |
| `difficulty` | The expected difficulty of the case (such as _Easy_, _Medium_, or _Hard_). This will be used as a tag on Steam Workshop. |
| `concepts` | SQL concepts that this case tests (such as _JOINS_, _GROUP BY_, _HAVING_, etc.) This will be used as tags on Steam Workshop. |
| `lockedTables` | A list of table names that shouldn't be deleted. |
| `previewImage` | The thumbnail for the case that will be shown on the Steam Workshop. You can use this template [here](/Images/Case%20Images/police%20report.psd). |
| `culpritArrestImage` | The image of the culprit to be shown when they're arrested. If no image is provided, a random appearance will be generated. 
| `arrestWarrant` | The arrest warrant for the culprit describing what they're being arrested for. The template for the warrant can be found [here](/Images/Case%20Images/warrant.psd). If no warrant is provided, a generic one will be used. |
| `voiceMessage` | A voice message that will be played once the case is loaded. |
| `voiceMessageTranscript` | The transcript of the voice message. |
| `queryHints` | A list of hints describing how SQL concepts should be used for this case. |
| `caseHints` | A list of hints describing what should be solved in general. |

**Note:** For `queryHints` and `caseHints` to render properly, you'll need to add newline characters (`\n`) between sentences. See `queryHints` in [config.json](/Example%20Case/config.json) as an example. 