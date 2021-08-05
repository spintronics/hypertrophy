in an effort to minimize the amount of libraries we need to learn, i will select libraries that are not as robust
this means that we will have to do more coding but it will be easier to understand, hopefully

server:

- python 3.9+
- for the database mongodb (atlas) using their connector
- for the api flask
- unittest for testing

postman is a nice tool for testing and api as you build it

I recommend mostly ignoring the database at the start. Mongo is a document store so it's basically just objects (python dictionary). I would use the fixtures to define the data and the api then worry about persisting it in mongo once much of that work has been done and tests passed.

client:
I am personally much more interested in flutter but for the sake of simplicity I will choose to use web technologies.
This will allow you to run it fairly easily without having to install and troubleshoot all the stuff involved with getting flutter up and running. Probably opt for angular
