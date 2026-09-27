# Database Detective: Official Workshop Guide
![Alt text](Images/Screenshots/Workshop%20Banner.jpg)
Want to report a crime? Just submit a case to the Custom Crimes Division! This police division is responsible for solving crimes reported by ordinary law-abiding citizens of Los Zorangeles like yourself.

Submitting a police report is easy, so don't be intimidated! Once you follow these simple steps, your case will be available for all our Database Detectives to solve.

## Step 1: Create Your Case
In order to file a report, you'll need to create a `json` file in a separate folder with the fields below. Don't worry if this looks like a lot, only a few of these fields are actually required.

```json
{
	"name": "Case Name Here", // Required
	"author": "Your Name Here", // Optional
	"difficulty": "Easy/Medium/Hard", // Optional
    "concepts": ["GROUP BY", "HAVING", "etc"], // Optional
    "database": "Database Name Here", // Required
	"lockedTables": ["table1", "table2", "etc"], // Optional (Recommended)
    "evidenceFiles": ["evidence.jpg"], // Required
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
One of the required fields is the name of a **SQLite3 database file** that should be provided in the same folder as this `json` file. This database file can be created any way you want! The database file for [this case](https://steamcommunity.com/sharedfiles/filedetails/?id=3807683717) was created using a python script which can be found in the [Scripts](Scripts/) folder.

Another requirement is at least one image file that can be used as evidence. This image file should also be in the same folder as the `json` file. 

You can head to the [Example Case](Example%20Case/) folder for a detailed description of each field within this `json` file. This folder contains the full contents of [this case](https://steamcommunity.com/sharedfiles/filedetails/?id=3807683717) in the Steam Workshop.

## Step 2: Submit Your Case
Once you're done with your case report, move the folder to the directory listed below.
| OS | Directory |
| :--- | :---------- |
| Windows | `/Users/[YOUR USER NAME]/AppData/LocalLow/HsuCorp/copOS` |
| Mac | `/Users/[YOUR USER NAME]/Library/Application Support/com.HsuCorp.copOS` |
| Linux | `/home/[YOUR USER NAME]/.config/unity3d/HsuCorp/copOS/` |

This directory should also have the database files and save files for _Database Detective_.

![Splash Screen](Images/Screenshots/Folder.png)

Then, open _Database Detective_ and click on _Custom Crimes Division_ as your department.

![Splash Screen](Images/Screenshots/Splash.png)

You should see the _Custom Cases_ icon. ![Custom Cases Icon](Images/Screenshots/icon.png)

Once you open the _Custom Cases_ panel, your case should appear! You can click _Load Case_ to see if everything works as expected.

![Custom Cases Panel](Images/Screenshots/Custom%20Cases.jpg)

## Step 3: Upload Your Case
 
Once you've confirmed everything works as expected, you can click _Upload Case_ to upload the case to the Steam Workshop.

If the upload is successful, the page to the Steam Workshop containing your case should pop up.

Otherwise, you should see an error describing why the upload failed. If you're not sure why the upload failed, join the [Database Detective Discord server](https://discord.gg/5TBXt7QSE3) and leave a message in the `#custom-cases` channel and I'll take a look at it.

### Updating Your Case
If you want to update something you've uploaded to Steam Workshop, you need to first make sure you're subscribed to that item. Then, navigate to where **Steam** is installed and open the directory `Steam/steamapps/workshop/content/3950130`. Your workshop item that you've subscribed to should be in a folder somewhere in this directory. Make your changes here.

Then, go back to the game and open the _Custom Cases_ panel. You should see the _Update Case_ button for the Workshop Item that you own and are subscribed to. Click it and your case should be updated with the changes that you've made!

![Update Case](Images/Screenshots/Update%20Case.png)
