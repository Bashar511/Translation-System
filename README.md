# Translation-System

## Description

This project is the final output of a fifth-year graduation project titled **Artificial Intelligence-Based Translation System** at AlBaath University, Faculty of Informatics Engineering, Department of *Software Engineering and Information Systems*.
The system provides a comprehensive solution for translating movies and TV subtitles, utilizing machine translation models and allowing for collaboration on translation projects.

## Installation and Usage

1. Setup a python virtual environment (optional but recommended)  
   `python -m venv myenv`
2. Activate myenv using *PowerShell*  
   `myenv\Scripts\Activate.PS1`
3. Install required dependencies  
   `pip install django requests Pillow`  
4. Navigate to the backend directory  
   `cd backend`
5. Start django development server  
   `python manage.py runserver`
6. Access the application by navigating to [127.0.0.1:8000/](http://127.0.0.1:8000/)

## Features

* *User Accounts:* Registration, login, and account management features are fully supported.
* *Collaborative Projects:* Users can create and collaborate on subtitle translation projects.
* *Subtitle Translation:* Upload and translate SRT subtitle files.
* *API Integration:* Translations are powered by machine translation models through the [Hugging Face](https://huggingface.co/) API.
