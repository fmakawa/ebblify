## INSTALL INSTRUCTIONS
1. virtualenv
2. python 3.6
3. django 2.1.1
4. use 'pip install -r requirements.txt' to install dependent packages for project
5. collect static
6. create superuser for project
7. runserver

## TO NOTE:
1. I used the in-built django auth but allauth would be a better package to use.
   It enables use of social accounts which is important if using enterprise software
   and accounts.
2. The messaging system I built isn't robust. It needs a way to group conversations and a
   way to add multiple people to a conversation and not just the two people involved.
3. Django-postman is a package that would do all this including features such as notifications,
   read, etc
4. I tweaked it such that both interfaces, Admin and Messaging Profiles are easy to use. But there
   is a lot of optimization still required.
5. 
