# Translation-System
## Description
This is the initial base of a fifth year graduation project named **Artificial Intelligence-Based Translation System** at AlBaath University, Faculty of Informatics Engineering, Department of *Software Engineering and Information Systems*.
## Installation and Usage
1. Setup a python virtual environment (optional but recommended)  
   `python -m venv myenv`
2. Activate myenv using *PowerShell*  
   `myenv\Scripts\Activate.PS1`
3. Install required dependencies  
   `pip install django`
4. Start django development server
   `python manage.py runserver`
5. Navigate to [127.0.0.1:8000/home/](http://127.0.0.1:8000/home/)
## Notes
- The site renders a simple UI in which users can input English text to be translated to Arabic.
- The translation is done by OPUS-MT English to Arabic model using Hugging Face hosted API [link](https://huggingface.co/Helsinki-NLP/opus-mt-tc-big-en-ar)
