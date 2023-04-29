# Political site

The following project is a basic and simply example of a campaigning website. This website contains a register page, an about page, a blog page and a login page.

## Contents

- ### Getting started
- ### Requirements
- ### Installing
- ### Run venv
- ### Docker image
- ### Usage
- ### Acknowledgements

## Getting started

Please have a look at the following instrucutions in order to know how to build and run this apllication using a **virtual environment** and **Docker**.

## Requirements

To run this project it is important to have the following on your machine:

- **Django**
- **pip**
- **Docker**

## Installing

1. Clone repository to local machine:
    - git clone https://github.com/k0b22s/politicalsite.git

2. Navigate to project directory:
    - cd PoliticalSite

3. Create a virtual env:
    - python3 -m venv venv

4. Activate virtual env:
    - source venv/bin/activate

5. Install the necessary project dependencies:    
    - pip install -r requirements.txt

6. Create the database tables:
    - python manage.py migrate

7. Create a superuser, if you want:
    - python manage.py createsuperuser


## Run venv

1. Activate venv:
    - source venv bin activate

2. Run django development server
    - python manage.py runserver

3. Access the web bvrowser for the applicatiion:
    - http://localhost:8000


## Docker image

1. If not installed. Please install docker on your machine, or user    Docker playground:
    - https://docs.docker.com/engine/install/

2. Pull the image off of docker hub:
    - docker pull k0b22s/politicalsite

3. Run the Docker container:
    - docker run -p 8000:8000 k0b22s/politicalsite

4. Access the web bvrowser for the applicatiion:
    - http://localhost:8000

5. *IMPORTANT* Remember to close the virtual env (when finished):
    - deactivate

## Usage

As stipulated in the desciption. this is a basic example of a politicalsite-campaigning website. Users can register and then log in in order to access the blog page. Furthernmore the goal of the the page is to contain information about the candidate as well as contact information.

## Acknowledgements:

- [info about me] https://k0b22s.github.io/cv_about/
