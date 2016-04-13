questions = {
    "strong": "Do ye like yer drinks strong? ",
    "salty": "Do ye like it with a salty tang? ",
    "bitter": "Are ye a lubber who likes it bitter? ",
    "sweet": "Would ye like a bit of sweetness with yer poison? ",
    "fruity": "Are ye one for a fruity finish? ",}

import random

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],}

#create a dictionary to store the user's answers to questions on preferences
answers = {}

#define the user_preferences function
def user_preferences():
    
    for x in questions:
        #print(x) - used print function to show it was the KEY 
        #print(questions[x]) - used print function to show it was the VALUE
        
        #store the user's responses to the questions in the VALUE slot of the questions dictionary as the variable "answer"
        answer = input(questions[x])
        
        #turn the answer into a Boolean that is stored in the answers dictionary in the VALUE position. 
        if answer == "yes":
            
            answers[x] = True
        
        else:
            
            answers[x] = False
    
    #print(answers) - can use print function to show that answers were stored correctly in the dictionary "answers"
    
    return answers
    
#def make_drink(preferences, ingredients): blocked out original to change code. 
def make_drink(answers, ingredients):     
    #look up values in answers dictionary
    #if answers in Value position are true, choose an ingredient at random from the ingredients dictionary
    print("I made you a drink, here are the ingredients: ")
    
    for key, value in answers.items():
       
        if value == True:
            
            print("A {0}".format(ingredients[key][random.randint(0,2)]))
    
    return

if __name__ == "__main__":
    user_preferences()
    make_drink(answers, ingredients)
    
#if __name__ == "__main__":
    #answers = user_preferences()
    #make_drink(answers, ingredients)