# Presence 3D

This project is similar to presence, with 3 D representation. Considering the lab size, it may be very ambitious to expect exact location, hence only broad classification can be tried like: 

- Reception area
- Server room
- Opposite sides of the lab

The outcomes as of now are like: 

If X's laptop is in the reception area, hence a laptop would be rendered there.

If Y's phone has been tracked over Lab Table(right) , hence would be rendered there.

The opensource project [https://github.com/schollz/find](https://github.com/schollz/find) has been used for wi-fi fingerprinting.

### (For reference) How to setup:
Ideally two virtualenvs would be preferred. One with python 3 and another with python 2.

Activate the venv with python 2 and run this cmd in project root.
```bash
$ pip install -r requirements.txt
```

Activate the venv with python 3  and run this cmd in project-root/find/ directory.
```bash
$ pip3 install -r requirements.txt
```

### Main Server Set up for wi-fi fingerprints processing
Inside the project-root/find directory

```bash
$(python3 venv) sudo python3 server.py
```

### Presence-3d server Setup

Inside the project-root

```bash
$(python2 venv) python manage.py runserver
```