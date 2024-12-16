# Cat Memes Gacha
#### Video Demo:
#### Description:
Cat Memes Gacha is a simple gacha web application where you collect 15 different types of cat memes. I programmed this web application for CS50 Final Project as I have been playing gacha games for almost a decade. I'm only familiar with designing web systems and applications so I decided to base it there. 

 A gacha game's main feature is its random number generation. There are 1 (one) 5-Star Cat, 5 (five) 4-Star Cats, and 9 (nine) 3-star Cats in this web application. The user/player can choose between two options when trying to get the cats: 1 (one) pull and 5 (five) pulls. There is a coin system where the player is only allowed to do a total of 100 pulls which resets every 60 seconds when the number of coins reaches 0.

The Flask web framework is used to run Cat Memes Gacha in a web browser. Using the Random module, the cats' rarity depends on the number of stars, wherein 5-Star is the rarest and 3-Star is common. The weights of the cats are: 1 (one) for 5-Star, 5 (five) for 4-Star, and 20 for 3-Star. The Threading module is used to start the function to reset the coins when it reaches 0. The player can see the time left for the coins to be refreshed. The Time module is used for the countdown of the reset which is passed using jsonify of Flask to the frontend.

Templates written in HTML and TailwindCSS are used for the frontend of the Cat Memes Gacha web application. A base template (base.html) is the parent template used for designs that reoccurs in the web application. The Jinja2 template is used to create dynamic contents by defining the block with child templates. The main page (index.html), collections page (collections.html), and gacha result page (result.html) are the child templates.

The static folder includes the images used in the web application. This consists of all the cat memes images which are drawn by yours truly. Other than the collectible cat meme images, there is also an image for Unobtained cats. This image is used as a placeholder for the cats that aren't collected yet through gacha.