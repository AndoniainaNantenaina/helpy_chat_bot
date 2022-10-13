<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h1 align="center">Helpy chatbot</h1>

  <p align="center">
    A simple python chatbot project for simple use !
    <br />
    <a href="#doc_begin"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/AndoniainaNantenaina/helpy_chat_bot/">View Demo</a>
    ·
    <a href="https://github.com/AndoniainaNantenaina/helpy_chat_bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/AndoniainaNantenaina/helpy_chat_bot/issues">Request Feature</a>
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

A simple open-source chatbot project powered by Python 3.10.5 and Tensorflow for simple use.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

The tools used for the implementation of this project are the following:

* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* ![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
* ![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="doc_begin"></a>
<!-- GETTING STARTED -->
## Getting Started

In order to properly use and operate <b>Helpy chatbot</b>, you will need to follow the following instructions :

### Prerequisites

After cloning the project, it's necessary to install all required python packages that are stored in the <b>requirements.txt</b> file.
* <b>pip</b>

  ```sh
  pip install -r requirements.txt
  ```

### Installation

_For the model to work with the project, it will have to be trained._

_For this, in the `main.py` file, the training function processing the ``intents.json`` file in <b>JSON</b> format_

```sh
    # Vérification si le model est déjà entrainé
    if os.path.exists('chat_model'):
        print(Fore.YELLOW + "Start messaging with the bot (type quit to stop)!" + Style.RESET_ALL)
        chat()
    else:
        loadAndTrainModel('intents.json')
        print(Fore.YELLOW + "Start messaging with the bot (type quit to stop)!" + Style.RESET_ALL)
        chat()
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

* Option 1 : Generating EXE file

```sh
pyinstaller --onefile main.py

cd /dist/

.\main.exe
```

* Option 2 : Launch directly

```sh
python -m venv venv

.\venv\Scripts\activate

(venv) python main.py
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Andoniaina Nomenjanahary - ando.andoniaina.nantenaina@esti.mg

Project Link: [https://github.com/AndoniainaNantenaina/helpy_chat_bot/](https://github.com/AndoniainaNantenaina/helpy_chat_bot/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
