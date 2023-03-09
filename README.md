# E-diary scripts

The e-diary placed here:

https://github.com/devmanorg/e-diary/tree/master


### How to install

```
git clone https://github.com/Gennadynemchin/e-diary.git
```
Then put it into your application. For example:
Your app located in 'datacenter' folder. 
So you have to put the 'management' folder to datacenter folder:
```
datacenter/management/commands
```

### How to start

#### If you want to make new commendation - run in terminal:
```
python manage.py create_commendation 'name' 'subject'
```
Replace ```'name'``` by requested name surname and ```'subject'```
by nesessary subject.

#### If you are going to fix your marks then:
```
python manage.py fix_marks 'name'
```
Replace ```'name'``` by requested name surname


#### for removing chastisements:
```
python manage.py remove_chastisements 'name'
```
Replace ```'name'``` by requested name surname

