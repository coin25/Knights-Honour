# Knights-Honour

In my graduating year of high school I was tasked with creating a video game using Pygame in Python. It was a fun group experience which involed 4 people.
I was the primary coder/creator of the game. My friend Joel created all of the art for the game and Braydon and Ryan ended up creating the write-up and cutscenes.
A week before the due date all groups dissolved and the individuals were tasked with adding to/completing the game. This is my version which I am very proud of.
I have added my formal write-up to the game below for those interested.


Brainstorming
Understanding the Problem
    As of November 14th we were tasked with creating a game using python as our final summative in ICS4U. Before we began we had to lay out our own criteria. The game had to be captivating, exciting, and above all else it had to be fun. We decided it would be necessary to force ourselves to work on this every night if possible. If we waited till the last second the game would have never looked as good as it does now.

Brainstorming

 Open Brainstorming

Design - Planing out the game
    Our idea was a top down RPG style game with a complete story, original artwork and a unique boss fight unlike anything we could have programmed as of last year. It would have a lot of levels with high mob-density and intense scenarios.

Algorithm  

Our algorithm Consists of the game starting at a main menu that leads to either an option to play or view the instruction screen and provides the player with an option to quit. 
Once the player hits play they will begin in a tutorial led by Ms.Gayowsky herself.

After the tutorial the player descends into the main part of the game consisting of three levels and the boss fight. When the player dies however they will see a game over screen and begin and at the beginning of their current level.

Once the player defeats the boss the credits will role and the game will have been won!




Game Creation 
Implementing our Game
    When we began to make the game we had 4 main processes to complete.
Game logic and AI
Artwork
Cut Scenes
Levels
    Austin worked on the game logic and AI which is run using Classes for each of the characters in the game. The player uses keyboard inputs while the enemies use a tracking system that tracks the player using a triangle. The mobs actually have varying AIs to enable greater variety. Some mobs run straight for you, some only move in straight lines.
    
    The artwork is all done by Joel frame-by-frame and was animated using a new module we found called pyganim. This module takes in each frame and assorts the images into an array which in turn plays the array when called. It is extremely complex and required many days of learning to implement well.

    The cut scenes and levels were created by both Ryan and Braydon using Photoshop. They also created the interface for the levels using collision detection, timers, and unique spawn locations.

Knights Honour Code

 Open Knights Honour Code

Debugging process
    The debugging process was by far the longest and most tedious process while working on this project. No matter what we added, we always had at least one or two bugs. These bugs almost always revolved around the AI and game logic. The processes taken in order to resolve these problems consisted of new code layouts and a lot of trial and error. We asked for a bit of help from outside sources, among those who helped were Dan, Anthony, and Matt. It was a long way up but we endured everything as a team and nothing was impossible.

How we met the criteria 
    This semester we learned how to do the following that involve making a game, 
Create and implement Classes 
Create sprites and use collision detection
Use/Create modules and other libraries
    All of this knowledge was applied to our game. We have a variety of classes as well as many methods that belong to those classes. We also successfully used sprites and even animated them in the process. We used a new module aside from what we learned in class and got it working perfectly into our game while making it compatible with the other libraries we used. Our game is complete and we have fulfilled our own expectations and then some in the time we were given.





Challenges
    Pyganim - This was a new module for us with new syntax. We had to first learn the syntax and then learn how to use the module properly. The hardest part however was incorporating the new module into the game. The module did not create sprites but created just their animations. This caused us to have to give everything a sprite, re-size hotboxes and rewrite the AI to play the animations properly.

    AI Tracking - We struggled with enemies following our player. It was simple to have them trace our x and y coordinates but we wanted to have varying methods of monsters finding us and the great variety made us expend a lot of extra time.

    Attacking - Our attacking hit box was a monster in it of itself. We struggled greatly with the range at which we attack and the collision of the monsters themselves. It took many hours working at home to finally make a dependable attacking system that consistently works.

    Getting Rid of Enemies - An unorthodox issue, it would originally appear to be very simple but it ended up taking many of our days. The obvious solution is to just remove the enemies from the list of enemies. This does not work. The enemies will still appear and come towards you but they wont take a heart when they hit you. To get around this bug we had to move the enemies far away where they would no longer be an issue to the player. Then when the next level began we could get around clearing the enemy list and reducing the lag.

    Optimization - Speaking of reducing the lag optimizing the game was a bit tricky. Had we not done any optimization the game would require a super computer to run. Just a couple of examples would be us removing the constantly updating walls, of which there were thousands as the game progressed and clearing the mob lists. All of this makes the game quite playable at a decent FPS on almost any computer.

Successes
    Main loop - The games main loop is something we never had much of a problem with. Everything ran smoothly on our timers and each cut scene always met its mark.  

    Attacking Animation - The attacking animation came together really well, it looks smooth and is a huge improvement over there not being an animation.

    Monster Animation - The monsters move very smoothly and properly, they look like actually monsters that could be in a real AAA game. All around we are really pleased with the quality of the animations.

    Transitions -  The game has very smooth transitions between levels that feels like an actually loading screen and are not too drawn out thanks to our optimization efforts.

Additional Features
Attack animation
Walking animations for player and enemies
109 hand drawn sprite frames
Four unique enemies 
Sinister boss
HD graphics
Four different levels with original designs and backgrounds
Critical hit chance
Random loot dropping system
Multiple weapon choices
Creative cutscenes
Captivating storyline
Working death system
Research
    We thoroughly research Pyganim to understand this new module. It was quite complex and requires days of study to use adequately, now we feel like masters of the library. This library adds a huge feature to our game and our game wouldn't be the same without it. The sprites were a bit of a hassle for Joel to make, the required him to learn how to make subtle changes in the image that felt just right, the legs couldn't move too much or too little. After many attempts we got prefect sprites all hand-drawn by Joel.
