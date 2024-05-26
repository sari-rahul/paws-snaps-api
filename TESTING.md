# PAWS & SNAPS API - Testing

## Table of Contents

- [Validation](#validation)
- [Manual Testing](#manual-testing)
   * [URL Testing](#url-testing)
   * [CRUD Testing](#crud-testing)

## Validation

- All files were passed through the [Code Institute PEP8 Validation Tool](https://pep8ci.herokuapp.com/) and came back with no errors, with the exception of some lines being too long in settings.py. As these were URL's and could not be shortened I decided to leave them in.

## Manual Testing

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