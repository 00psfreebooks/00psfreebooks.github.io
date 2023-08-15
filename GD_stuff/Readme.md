# Google Drive Library Setup

## Getting Started

1. Use [this link](https://support.google.com/mail/answer/56256?hl=en) to create a new google account
2. Login to google drive using the new google account
    1. Create new folders with the names of the categories of books that you want to host
    2. Upload your books to google drive and sort them into the new folders
    
**Tip #1** 

*Having bookmarks to manage the new google account independent of my personal bookmarks is very helpful. I use a different chrome profile with sync turned on for managing the new google account. This way, I can keep bookmarks separate and use extensions with logins created using the new google account.*

**Tip #2**

*I use google drive desktop for managing files on google drive. Google drive desktop will upload new files asynchronously so you don't have to keep a browser tab, browser window, or even file manager window on your computer open when adding books. In addition, you can copy and modify files in google drive using not only your file explorer, but also your system's terminal & auxillary file management tools which I will safely guess are superior to Google's GUI*

## File Organization - The Specifics

Books are organized into categories based on the theme or topic of their content. Categories of books are represented by folders in the google drive. Individual books are represented by the files inside the folders of the google drive. 

**General Example**

```
Google Drive/
├─ category1/
│  ├─ book1
│  ├─ book6
│  ├─ book7
├─ category2/
│  ├─ book3
│  ├─ book5
│  ├─ book8
├─ category3/
│  ├─ book2
│  ├─ book4
```

**Specific Example**

```
My Drive/
├─ business/
│  ├─ The_Richest_Man_In_Babylon.pdf
│  ├─ Your_Next_Five_Moves.pdf
│  ├─ Rich_Dad_Poor_Dad.pdf
├─ mindset/
│  ├─ A_Hackers_Mind.pdf
│  ├─ Breathe.pdf
├─ survival/
│  ├─ Anarchist_Cookbook.pdf
│  ├─ Ammunition_Handbook.pdf
```

**Tip #3**

*Check out [the example](https://00psfreebooks.github.io/) if you get stuck trying to name your categories.*

## Setting up GH Pages

1. Setup a new github account with the new google account
2. Fork this repo [here](https://github.com/00psfreebooks/00psfreebooks.github.io/fork)
    1. Use the new github account
    2. Name the repo fork the same as your username followed by "*.github.io*"
        1. Example name for the github repo - "eleethaxor.github.io"
3. In the repo settings of the new fork, enable github pages.
    1. Go to Settings > Code & Automation > Pages
    2. Under "*Build and deployment*", under "*Source*", select "*Deploy from a branch*"
    3. Under "*Build and deployment*", under "*Branch*", use the branch dropdown menu and select "*main*".
    4. Change "*/ (root)*" to "*/docs*" and click save
    5. If you want to setup a custom domain, feel free to do so

**Tip #4**

*Use a password manager to help keep track of all your accounts. I prefer to use dashlane for something like this. In fact, after I setup a new chrome profile with the new user account, I install the dashlane chrome extension on the new chrome profile, and setup a dashlane account using the new google account. This way, I don't mix some of my personal passwords with passwords for project aliases, effectively ghost people on the internet, like this one.*

## Setting Up A Google Cloud Project

1. Create a new google project for free [here](https://developers.google.com/workspace/guides/create-project)
    1. Make sure to use the new google account
2. Follow [this guide](https://developers.google.com/workspace/guides/enable-apis) to enable api access to your cloud project
    1. Enable the google drive api [here](https://console.cloud.google.com/marketplace/product/google/drive.googleapis.com)
3. Setup Oauth
    1. Visit the [Oauth Consent Screen](https://console.cloud.google.com/apis/credentials/consent)
    2. Click "*Edit App*"
        1. Name the app
        2. Use the new gmail address for the email
        3. Since you setup a new github account and followed the specific naming protocol for the new github repo, things are less complicated. Your domain is now your new github username followed by "*github.io*". Keeping with the previous example, we'll use "*eleethaxor.github.io*"
            1. Example homepage - "https://eleethaxor.github.io/"
        4. Enter the same domain, followed by "*/privacy*" for the link to your privacy policy
            1. Example - "https://eleethaxor.github.io/privacy"
        5. Enter the same domain, followed by "*/tos*" for the link to your terms of service
            1. Example - "https://eleethaxor.github.io/tos"
        6. Enter the domain into autorized domains
            1. Example - "eleethaxor.github.io"
        7. Also add "*github.com*" to authorized domains
        8. Enter the new gmail address into developer contact info
        9. Click "*Save and Continue*"
        10. Add the following api scopes if they are not already present
            1. /auth/drive
            2. /auth/drive.file
            3. /auth/drive.appdata
            4. /auth/drive.readonly
            5. /auth/drive.metadata.readonly
        11. Click "*Save and Continue*"
        12. If you want to add more users, feel free to do so.
            1. Added users are the people with permission to modify files on the new google account's google drive using the new cloud project's api. 
            2. Your website and books will still be accessable to the public.
        13. Click "*Save and Continue*"
        14. Click "*Back to Dashboard*"
4. Create Credentials
    1. Manage the project's credentials [here](https://console.cloud.google.com/apis/credentials)
        1. Make sure your in the correct google cloud project
    2. Click "*+ Create Credentials*" and select "*Oauth Client ID*"
    3. Select "*Web Application*"
    4. Enter the name "*CLient1*" in the name field to keep things simple
    5. You should not need to enter any javascript origins or redirect urls
    6. Click "*Create*"
5. Store Credentials
    1. Visit the project's credentials [here](https://console.cloud.google.com/apis/credentials)
    2. Under "*OAuth 2.0 Client IDs*", click the down arrow next to the new "*Client1*" entry
    3. Select "*Downlaod JSON*"
    4. Save the JSON File as "credentials.json" in a secure directory 

**Tip #5**

*You don't need to add any users to the list of authorized users for the cloud project's api. You can simply setup a github codespace (foreshadowing) and be perfectly fine managing everything through the github account of the new google account.*

## Setting Up A Codespace

> Upon executing the google drive script the first time, you will be asked to authenticate and "token.pickle" will be generated
> If you do get a "invalid_grant: Token has been expired or revoked.", simply delete "token.pickle" and re-run this script to re-authenticate
> Re-authentication will not work from a github codespace, and steps to work around this are documented below

### Vanilla VSCode

1. Open up the new repository fork in vscode
2. Create a new directory named "creds" in the parent folder
3. Copy credentials.json into creds/
4. Run the following from the parent directory

```
python site_maker_GD.py
```

5. Commit changes

### Github Codespaces

> You only need to follow steps 1-3 if you are just setting up a codespace
>
> You only need to follow steps 4-6 if you don't have a token.pickle file in your codespace or are having issues with the token.pickle file.
>
> Otherwise, you should be able to simply open up the codespace after you add books to the google drive, run the google drive script, commit changes, and let the site run itself.

1. Visit your repository fork on github
2. Add a repository secret
    1. Navigate to Settings > Secrets & Variables > Codespaces
    2. Clicke the "*New Repository Secret*" button
    3. Enter "*CREDENTIALSJSON*" in the name field
    4. Copy and paste the contents of the "*credentials.json*" file into the secret field
    5. Click "*Add Secret*"
3. Exit the repository settings page and go back to the main code page 
4. Click the green "*Code*" button as if you were to clone the repository, but click on "*Codespaces*" instead of "*Local*"
5. Click the "*+*" to create a new codespace on main
6. Generate a token.pickle file (you need to do this on your local machine)
    1. Clone the repository locally on your machine
    2. Create a new directory named "creds" in the parent folder
    3. Copy credentials.json into creds/
    4. Run the following from the parent directory & follow the authentication link if it is generated

    ```
    python site_maker_GD.py
    ```

    5. Upload the creds folder to the new github codespace in your webbrowser (not the github repository)
        1. You should be able to drag and drop the folder from your file manager/explorer into the codespace file tree
        2. Delete "*credentials.json*" from the github codespace, but keep the "*token.pickle*"

7. You should be able to run the following from inside the codespace now:

```
python site_maker_GD.py
```

## Google analytics

Simply replace *new_gtag* string at the top of the [Goolgle Drive Site Generator Script](https://github.com/00psfreebooks/00psfreebooks.github.io/blob/main/site_maker_GD.py) to the gtag that you want to use, and re-run the script. The script will replace all instances of *old_gtag* with *new_gtag*. I am assuming that you can figure out how to get a data stream for a desktop/web application for google analytics up and running.

## Overview of Script Interaction With Google Drive

The [Goolgle Drive Site Generator Script](https://github.com/00psfreebooks/00psfreebooks.github.io/blob/main/site_maker_GD.py) uses every folder on the google drive as a category, and uses every file in each category as a book. Currently, only *pdf* files are considered books. The following actions are taken:

1. Scan all folders in google drive
2. Scan all files in each folder
3. Create a web page for referencing each category of books
4. For every category of books (folder in google drive), create a web page that references each book in each category (each pdf file in each folder in google drive)

* Note - this is not a complete overview of the script, but a simple explanation for how the script should work with google drive
* It is not intended for there to exist any folders inside the category folders
* It is not intended for there to exist any folders or files on the google drive that are not supposed to be scanned
* It is intended for the entire google drive of the new google account to be used for the sole purpose of a hosting platform for the single purpose of a digital book library
