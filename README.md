## Simple GUI to manage sales.
> Currently in development.

I'm using MongoDB from docker, but in the future I'll extend to other relacional database.

###  #Requeriments
Docker  
Python 3  
Virtualenv (recommended)  
### #Instalation
> May you need use "sudo" to run some commnads.  
With docker installed, run
```
docker run -d -p 27017:27017 -v --name mongo mongo:latest
```

And check if it's running  
```
docker ps
```
Now that mongo is running, go to the project's folder.  
We need create a virtualenv to wrap our application within needed dependencies...  
```
cd <root folder> # <- don't forget
virtualenv -p python3 .env
source .env
pip install -r requirements.txt
```
...then allow and run the script that I wrote to transform .ui to .py files.  
```
chmod 555 script.sh
source script.sh
```
### #Running  
Then, you can start the application typing
```
python main.py
```

Feel free to contact me if you have any question.
