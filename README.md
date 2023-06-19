# VULCAN GRADES EXPORTING
App to exporting grades from [Vulcan](https://vulcan.edu.pl/)' by Cocolak
E-mail: cocolak333@gmail.com

## APP USAGE
### First time launch / Registration
- run 'main.py'.
- select any mode (1 or 2).
- the application will not detect the files and will ask you if you want to register.
- select 'y'.
- now you need to log in to your school's Vulcan account in browser (https://uonetplus.vulcan.net.pl/symbol)
- then go to Mobile access/Dostęp mobilny in your student/parent panel and click "generate access code".
![image](https://raw.githubusercontent.com/Cocolak/vulcan-grades-export/master/docs/qrkod.jpg)
- you need rewrite the data located below the QR code into the application (pay attention to the letter case).
![image](https://raw.githubusercontent.com/Cocolak/vulcan-grades-export/master/docs/login.png)
- you are now logged in, all data has been saved in "!_reg"

### The application shuts down
- if the application shuts down, try deleting the '!_reg' folder and logging in again

## MODES
### `less` mode
- date_created, 
- full grade e.g. 4+, 5-,
- grade value (float) e.g. 4.0, 5.0, 
- short subject name e.g. pr.SK, wf, j. polski.

### `more` mode
- period.number,
- date created,
- full grade e.g. 4+, 5-,
- grade value (float) e.g. 4.0, 5.0,
- grade description,
- category e.g. Sprawdzian, Kartkówka,
- full subject name,
- short subject name e.g. pr.SK, wf, j. polski,
- full teacher name (name + surname).

## APP INFO
### Future plans:
- possibility of exporting other data (attendance, messages etc.),
- automatic calculation of subject averages and overall average,
- I will develop an app to analyse grades,

### Modules used
- [vulcan](https://github.com/kapi2289/vulcan-api)
```console
$ pip install vulcan-api
```
- [consolemenu](https://github.com/aegirhall/console-menu)
```console
$ pip install console-menu
```
- [pandas](https://pandas.pydata.org)
```console
$ pip install pandas
```
- [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)
- [asyncio](https://docs.python.org/3/library/asyncio.html)
- [os](https://docs.python.org/3/library/os.html)