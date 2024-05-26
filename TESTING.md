# PAWS & SNAPS API - Testing

## Table of Contents

- [Validation](#validation)
- [Manual Testing](#manual-testing)
   * [URL Testing](#url-testing)
   * [CRUD Testing](#crud-testing)

## Validation

- All files were passed through the [Code Institute PEP8 Validation Tool](https://pep8ci.herokuapp.com/) and came back with no errors, with the exception of some lines being too long in settings.py. As these were URL's and could not be shortened I decided to leave them in.

## Manual Testing

| Test  |Expected   | Result   |
|-------|-----------|----------|
|
|Create a new user.|A user can Signup with password and username.|As Expected.|
|Login with signup data. |The user can login with signup data.|As Expected.|
|Create Article. |A logged-in user can create an article.|As Expected.|
|Create Article. |A logged-out user cannot create an article.|As Expected.|
|Edit Article.|The article owner can edit their article.|As Expected.|
|Delete Article.|The article owner can delete their article.|As Expected.|
|User Edit Article.|A user cannot edit other users article.|As Expected.|
|User Delete Article.|A user cannot delete other users article.|As Expected.|
|Search Article.|A user can search article using title, author and category. |As Expected.|
|Read Article.|A logged-in user can read article.|As Expected.|
|Create Comment.|A logged-in user can create a comment on an article.|As Expected.|
|Create Comment.|A logged-out user cannot create a comment on an article.|As Expected.|
|Owner create Comment.|The owner of the article cannot create a comment on their article.|As Expected.|
|Edit comment.|The owner of the comment can edit their comment.|As Expected.|
|Delete comment.|The owner of the comment can delete their comment.|As Expected.|
|Like a comment.|A logged-in user can like comments.|As Expected.|
|Unlike a comment.|A logged-in user can unlike comments.|As Expected.|
|Logout |The user can logout using the logout link.|As Expected.|


### URL Testing

The following URLs were tested:

| URL         | Result |
|-------------|--------|
| /           | Pass   |
| /articles   | Pass   |
| /comments   | Pass   |
| /likes      | Pass   |
| /profiles   | Pass   |

### CRUD Testing

All apps were tested for full Create, Read, Update and Delete functionality.

| App        | Create | Read | Update | Delete |
|------------|--------|------|--------|--------|
| Comments   | Y      | Y    | Y      | Y      |
| Articles   | Y      | Y    | Y      | Y      |
| Likes      | Y      | Y    | Y      | Y      |
| Profiles   | Y      | Y    | Y      | Y      |