# Making Your Own Websites
Making your own website is actually pretty easy!

There are just a few steps needed to get things set up, but once you do, making websites is as simple as dragging around different components. No programming skills needed!

## Setting Things Up
### Step 1: Install Unity
_Database Detective: Minor Crimes Division_ uses Unity as the engine, so you'll need to install it to make websites for the game. You can visit [this link](https://unity.com/releases/editor/archive) to install the latest version of Unity.


### Step 2: Unzip and Move _Unity Website Assets.zip_
Now, unzip and move the contents of [_Unity Website Assets.zip_](/Custom%20Websites/Unity%20Website%20Assets.zip) into Unity's default _Assets_ folder.

![Moving Folders](/Images/Screenshots/Move%20Assets.gif)

You now have everything you need to make your website!

## Making Your Website
In the `Resources/Websites` folder, you can view some websites that have already been made, one of them being `example.com`. If you want a website with a different name, just rename `example.com` to something else!

![Website in Editor](/Images/Screenshots/Website.png)

### Naming Your Website
Each website is a file. When you type a website in the Web Browser, it tries to access a file of that name. However, a file cannot include slashes (`/`) in the name, so you'll have to use dashes (`-`) instead. This is why the file for the web page `example.com/jumpscare` is named `example.com-jumpscare`.

_Fun Fact_: You can use dashes to replace slashes on every website in Database Detective and it'll still work!

`example.com` demonstrates everything a custom website is capable of, such as displaying images as well as buttons that download hidden tables and open other web pages. Let's first go over how to add images to your website.

### Adding Images
First, add a _UI Image_ component and drag and drop your image file to the _Sprite_ field in the _UI Image_ component.

![Moving Images](/Images/Screenshots/Ghost.gif)

If you're having trouble dragging and dropping your image to the image component, you might need to configure your image file to the properties below.

![Image Settings](/Images/Screenshots/Image%20Settings.png)

And that's it! Use your mouse to move this image component to wherever you want it to be!

Next, let's go over some scripts that are included.

### Scripts
```C#
public class Website : MonoBehaviour
{
    // Launches a website of the given url.
    public void LaunchInnerSite(string url) {}

    // Downloads a table of the given name to the player's desktop.
    // Table must be marked as hidden in the config file.
    public void DownloadHiddenTable(string tableName) {}
}
```

This is `Website.cs`, a script that should sit at the root of each website. Notice that there isn't any code! That's because the actual `Website.cs` script is in the game itself, which is what is actually being called when your website is opened within the game.

This also means that any code you write in this file will not work, as this local script is merely a way to know which functions from the "real" `Website.cs` should be called.

These functions are meant to be executed when a button is clicked. To make a button, just add the _Button_ component to an image!

![Button](/Images/Screenshots/Button.gif)

Then, add an `On Click` behavior and drag and drop the root component where the `Website.cs` script lives.

![Button](/Images/Screenshots/Functions.gif)

Then, select the appropriate function that should be used when the button is clicked.

#### DownloadHiddenTable
This function downloads tables that are marked hidden. In the button below, the `secret_table` is downloaded when clicked.

![DownloadHiddenTable](/Images/Screenshots/DownloadHiddenTable.png)

The `CursorChanger.cs` script should be attached to this button, which changes the cursor to the finger pointer when the button is hovered over.

![Cursor Change](/Images/Screenshots/Cursor.gif)

#### LaunchInnerSite
This function opens a new web page. In the button below, `example.com/jumpscare` is opened when clicked.

![LaunchInnerSite](/Images/Screenshots/LaunchInnerSite.png)

The `CursorChangerExist.cs` script should be attached to this button. This is the same as `CursorChanger.cs`, but changes the cursor back to normal when clicked.

## Exporting and Testing
Unity allows for importing and exporting custom object files through something called `AssetBundles`.

When you're done with your website(s), click on each website file within the `Project` window and enter a name for the `AssetBundle` field on the bottom of the `Inspector` window. You should use the same `AssetBundle` name for each website you want to add.

![Assigning Asset Bundle](/Images/Screenshots/AssetBundle.png)

Then, you'll want to build the `AssetBundle` by going to `Assets` on the top left and clicking on `Build AssetBundles`.

![Build Asset Bundle](/Images/Screenshots/Build.png)

Once you do so, you should see a file with the name of your asset bundle and another file with the same name but with a `.manifest` file type. Since I named my `AssetBundle` "test", I have the files `test` and `test.manifest` in my `AssetBundles` folder.

![Build Asset Bundle](/Images/Screenshots/AssetBundles%20Folder.png)

Move these two files into your case directory.

![Moving Folders](/Images/Screenshots/Move.gif)

Once you're done with that, just fill out these fields in your `json` config file with the name of your `AssetBundle` and a list of websites you've added (as well as any tables that should be initially hidden).
```json
    "hiddenTables": ["secret_table"],
    "assetBundle": "test",
    "websites": ["example.com", "example.com/jumpscare"]
```

And you're good to go! You should be able to visit all the websites you've added in the Web Browser once you've loaded your case!

![Success](/Images/Screenshots/Working.png)

If you're running into any issues, please let me know in the `custom-cases` channel in the [Database Detective Discord server](https://discord.gg/5TBXt7QSE3).

Have fun!
