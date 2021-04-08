# 1. User Manual

<p align="center">
<img src="./image/psyche.png" alt="drawing" width="200"/>
</p>


- [1. H.A.M.L. User Manual (CSE 485/486 NASA Geological Mapping Group)](#1-user-manual)
  - [1.1. Setup](#11-setup)
    - [1.1.1. Step 1 - Python Dependencies](#111-step-1---python-dependencies)
    - [1.1.2. Step 2 - Run the app](#112-step-4---run-the-app)
  - [1.2. Main Screen](#12-main-screen)
  - [1.3. 1.2 Buttons](#13-12-buttons)
    - [1.3.1. `Open Image and Run Prediction`](#131-open-image-and-run-prediction)
    - [1.3.2. `Detect on Sample Image`](#132-detect-on-sample-image)
    - [1.3.3. `Draw`](#133-draw)
    - [1.3.4. `Exit`](#134-exit)
  - [1.4. Video Link](#14-video-link)

## 1.1. Setup
**This project is supported on Linux. Not tested on Windows or macOS..**

In order to get started clone this repository:

```zsh
git clone https://github.com/avilla11/GeologicalMapping_12A_2021.git
```

### 1.1.1. Step 1 - Python Dependencies
**This project requires python3 and pip**

**This project requires the following Python dependencies:**
1. PySimpleGUI
2. PyCDA
3. Numpy
4. OpenCV

To download all the dependencies, simply run `scripts/install.py` using the command:
```zsh
python3 scripts/install.py
```

### 1.1.2. Step 4 - Run the app
Run the app using the following `gui.py` file:

```zsh
python3 src/gui.py
```

## 1.2. Main Screen
This project has 4 buttons. They are:
1. Open Image and Run Prediction
2. Detect on Sample Image
3. Draw
4. Exit
![Main Menu](image/mainmenu.png?raw=true "Main Menu Label")

## 1.3. 1.2 Buttons
Explanation on Buttons:

### 1.3.1. `Open Image and Run Prediction`
Here you can select any image from your computer and open it to run the automated crater detection. Results will be outputted to a CSV in the directory
you specify.
![Browse For Image](image/browseforimage.png?raw=true "Browse For Image")
![Results](image/craterresults.png?raw=true "Results")
![CSV Results](image/csv.png?raw=true "CSV Results")

### 1.3.2. `Detect on Sample Image`
Performs automated crater detection on a sample image from PyCDA. Useful to see how detailed results can be with error correction.
![Sample Image Results](image/sampleresults.png?raw=true "Sample Image Results")

### 1.3.3. `Draw`
Allows the user to select any image from their computer and draw on it. Useful to manually draw craters on an image or to cross out craters that the program has
incorrectly identified. Note: to use this feature, you must select the image you wish to draw on when the program starts. 
![Browse For Image](image/drawbrowse.png?raw=true "Browse For Image")
![Drawing](image/drawresults.png?raw=true "Drawing")

### 1.3.4. `Exit`
Allows the user to exit the program. The useer can also press the x at the top right to quit the program.

![Library Record Label](image/Library-Record-Label.png?raw=true "Library Record Label")
![Update Record Label](image/Update-Record-Label.png?raw=true "Update Record Label")

## 1.4. Video Demo of App
See a demo of the app [here](https://www.youtube.com/watch?v=4YLGX1ezpxA&ab_channel=AurelioVillalobos)

