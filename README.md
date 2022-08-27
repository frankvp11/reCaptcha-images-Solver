1) Figure out how to get screenshots of well-the screen.
2) Then use NLP to figure out what "class" the recaptcha wants to identify. 
3) Get Detectron2 working and create an api. 
4) Use some type of AI to "blur out" or white out the rest of the image so that Detectron2 doesn't get the ads - most difficult 
5) Then take the infered x,y coords for clicking. 
6) Use pyautogui to click at those coords - figure out a way that it doesn't overlap with the images
7) 
