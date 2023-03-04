# Remove Background

- before
![](./before.png)

- after

![](./after.png)

- directory structure

```bash
.
├── after.png
├── before.png
├── images
│   ├── after
│   └── before
├── main.py
├── readme.md
└── requirements.txt
```

## init

```bash
$ brew update && brew install ffmpeg
$ python3 -m venv ./.venv
$ echo '.venv' >> .gitignore
$ source .venv/bin/activate
```

## dependency

```bash
$ pip install --upgrade pip
$ pip install backgroundremover

```

## run
> [Flags](https://github.com/nadermx/backgroundremover/blob/bcb82f429df39d60612e73510812c01f2e11bf56/backgroundremover/cmd/cli.py#L13)

Please note that when you first run the program, it will check to see if you have the u2net models, if you do not, it will get them from u2net's google drive, as they say too here, and in this repo the code that pulls it is here


```bash
backgroundremover -i "./images/before/home.png" -o "./images/after/home.png" -a -ae 15
```

- If you want to 

```bash
python main.py
```