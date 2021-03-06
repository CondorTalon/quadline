# Quadline

A Connect 4 inspired game, created using `python` and its `pygame` library.

## Navigation 
<a name="top"></a> 
1.  [Description](#intro) 
    - [Screenshots of the Game](#screen)
2. [How to Install and Run Quadline](#install)
3. [Documentation for Quadline](#documen)
4. [Developers](#devs)
5. [Contributions](#contrib)
6. [License](#license)

## <a name="intro"></a>Game Description 

The object of Quadline is to connect four of your pieces in a straight line, in any direction. Play is done on a 7 by 6 grid. Players take turns dropping a piece from the top of a column of their choice; the piece will then fall to the lowest unoccupied space in that column.

The line of four may be finished at either end, or from the middle. Players must play their pieces strategically, both offensively and defensively, to build their line of four and block their opponent from doing the same.

If the board fills up without either player creating a line of four, the game is counted as a draw.

[Return to top](#top)




## <a name="screen"></a>Screenshots

![Title Screen](https://i.imgur.com/3wLthBM.png)
![Gameplay Screen](https://i.imgur.com/fBXdEfr.png)
![Game Over Screen](https://i.imgur.com/sUsiEaw.png)

[Return to top](#top)


## <a name="documen"></a>Documentation and Directory Structure

The documentation and the information about our directory can be found in the Wiki Page of our repository. Have a look at it by clicking [here](https://github.com/CondorTalon/quadline/wiki/Quadline-Wiki).

[Return to top](#top)



## <a name="install"></a>How to Install and Run Quadline 

**For `Windows` Operating Systems:**  
To install and run `Quadline`, you'll first need to download `Pygame`.  
* Download link: https://www.pygame.org/download.shtml  
  
Once you've downloaded `Pygame`, you'll then need to download the zip file containing the game files or simply clone it though a terminal.
* Zip link: https://github.com/CondorTalon/quadline/archive/master.zip  
* Clone link: https://github.com/CondorTalon/quadline.git  
(To clone the game files from the repository, open your terminal and navigate into a directory of your choice using `cd C:\Users\...\...\`. Then copy the repository into the directory of your choice by using `git clone https://github.com/CondorTalon/quadline.git`)  
  
After cloning or extracting the game files from the zip, you'll find various `.py` files. To launch the game, run the `QuadlineGUI.py` using a python IDE of your choice.

[Return to top](#top)

## <a name="devs"></a>Developers of Quadline

The game Quadline was created by Team While, a group of students from University of Toronto Mississauga. Quadline was created in the course CSC290: Communication Skills for Computer Scientists. The members of the team are :

- Ethan Chung
- Jagdev Singh Jhajj
- Muhammad Naqvi
- Richard Seo
- Nai-An Yu (Andy)

[Return to top](#top)

## <a name="contrib"></a>Contributions  
  
### Ethan:  
My code contributions to the project includes: creating the GUI of the game, creating the grid class with methods to update the grid model, and adding additional methods into the game and player classes. Once the grid, game, and player classes have been created, I connected the classes together and ensured that the backend of the game successfully runs. After making sure the backend runs properly, I linked the game model with the GUI and created buttons and handlers for the GUI to update the model as needed. I did some testing afterward to make sure the frontend portrays the model correctly. Part of the documentation for the grid and game class typed up by me. For the README, I contributed by writing up the ‘How to Install and Run Quadline’ section.

### Jagdev:

For this project, I mainly contributed by creating the abstract classes for the major classes and providing a concrete structure for our code. I documented the classes and abstract methods I had created. My fellow team members then structured the code based on the class structure that I had provided. I wrote the manual for our game that explains the game's gameplay and it's features. For the README, I wrote the Documentation and explained the Directory Structure of our game in the Wiki Page of our repository. The complete Wiki Page was scripted by me. 

### Muhammad: 

For this project, I worked on creating the grid class and worked along with other members to implement methods that will update the grid model. I contributed to the commenting in our code to make sure other developers who come across the game are able to comprehend our code. For the README, I contributed by creating the general outline for the README file, worked on "License Information", "Developers of Quadline", and "Navigation" section. I also worked on the navigation system that allows for quick access to each section of the README file and allows the reader to quickly get back to the 'Navigation' section by clicking the "Return to top" buttons at the end of each section. 

### Richard:

I created the main methods used in the main Quadline method, namely "get_current_player", "is_game_over" and "make_move". For the README, I provided the screenshots by hosting them on an image-hosting site (imgur), and wrote the Game Description section. I also provided my account on Github to host the repo.

### Andy:

I improved on some other methods throughout the QuadlineGrid and Quadline class, and created a few new methods, notably "check_quadline". I also created a uniform docstring format for my team to use in the methods of our code to make our code easily understandable. For the README file, I contributed in the Documentation by adding the "Extending the game" section. I also made edits to fix minor typos and mistakes on both the code and the documentation.

[Return to top](#top)



## <a name="license"></a>License Information

## MIT License 

Copyright (c) 2019 CondorTalon

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


[Return to top](#top)


