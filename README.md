# The_Quiz-Game
Quiz Game
Description
The Quiz Game is an interactive console-based application that allows users to create, manage, and play quiz games. Users can add custom questions, options, and answers, as well as start the game to test their knowledge. The game keeps track of the player's score and prize money based on their answers.

Features
Add custom questions along with multiple-choice options.
Remove specific questions or clear all questions from the quiz.
Start the quiz and answer questions to accumulate points and prize money.
Display a list of all current questions, options, and answers.
Requirements
Python 3.x
Usage
Clone the repository:

bash
Copy code
git clone https://github.com/iamgarou/The_Quiz-Game.git
cd quiz-game
Run the application:

bash
Copy code
python quiz_game.py
Follow the prompts:

Choose an option from the main menu:
Start the game
Add a question
Remove a specific question
Clear all questions
List all questions
Input your choices as prompted.
Example
Start the Game:

Select option 1 to start the quiz.
Answer questions as they are presented. For example:
markdown
Copy code
Question: What is the capital of France?
1. Berlin
2. Madrid
3. Paris
4. Rome
Your choice: 3
Correct Answer.
Your current prize money: 1800.0
Add a Question:

Select option 2 to add a new question.
Enter your question, options, and the correct answer when prompted.
Remove a Question:

Select option 3 to remove a specific question by its index number.
Clear All Questions:

Choose option 4 to delete all saved questions after confirmation.
List All Questions:

Select option 5 to view all currently saved questions, options, and answers.
Notes
Make sure to have quiz_questions.txt, quiz_options.txt, and quiz_answers.txt in the same directory for the application to function correctly.
The application handles basic input validation to ensure a smooth user experience.

License
This project is licensed under the MIT License - see the LICENSE file for details.
