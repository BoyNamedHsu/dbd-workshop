# Making Your Own Websites
Making your own website is pretty easy! There are just a few steps needed to get things set up, but once you do, making websites is as simple as dragging and dropping different components. No programming needed!

-- gif of drag and drop

## Setting Things Up
### Step 1: Install Unity
_Database Detective: Minor Crimes Division_ uses Unity as the engine, so you'll need to install it to make websites for the game. You can visit [this link](todo.com) to install the latest version of Unity.

-- replace link from todo.com

### Step 2: Unzip and Move _Unity Web Assets.zip_
Now, unzip and move the contents of [_Unity Web Assets.zip_](/Custom%20Websites/Unity%20Website%20Assets.zip) into Unity's default _Assets_ folder.

-- gif of replacing Assets folder 

You now have everything you need to make your website!

## Making Your Website
In the _Websites_ folder in _Assets_, you can view some websites that have already been made, one of them being _example.com.prefab_.

-- photo of example.com

This website demonstrates everything a custom website is capable of, such as displaying images as well as buttons that open other websites and download tables. Let's first go over how to add images to your website.

### Adding Images
First, add a _UI Image_ component and drag and drop your image file to the _Sprite_ field in the _UI Image_ component.

-- gif of dragging and dropping

You might need to configure your image file to the properties below.

-- image of settings of drag and drop

And that's it! Use your mouse to move this image to wherever you want it to be!

-- gif of moving image

Next, let's go over the functionality of buttons and the scripts that allow this to work.

### Website.cs
-- post copy of script here

This script should sit at the root of each website. However, if you open this script, you can see that there isn't actually any code! That's because there is a script of the exact same name (with the same functions definitions) as _Website.cs_ in _Database Detective_, which is what is actually being called when your website is opened within the game.

This also means that code that you write in this script will not work, as this script is merely a way to know which functions compiled within the game should be called.

These functions are meant to be executed when a button is clicked. To make a button, just add the _Button_ component to an image! Then, add an OnClick behavior and drag and drop the root component where the Website.cs script lives.

-- gif of above

Then, select the appropriate function that should be used when the button is clicked.

#### -- InnerLink
This function opens 

#### -- DownloadHiddenTable
This function allows for tables that are marked "hidden" to be downloaded.

### CursorChanger.cs (and CursorChangerExist.cs)
These scripts allow for the cursor to change to the finger pointer 

## Exporting and Testing


