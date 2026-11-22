using System.Activities;
using System.ComponentModel;
using System.Diagnostics;

namespace AskQuestionCustomActivity
{
    public class AskQuestion : CodeActivity
    {
        // category for easier identification in the workflow designer
        [Category("Input")]
        [RequiredArgument]
        public InArgument<Dictionary<int, Tuple<string, string>>> QuestionsDictionary { get; set; }

        [Category("Input")]
        [RequiredArgument]
        public InArgument<int> QuestionNumber { get; set; }

        [Category("Input")]
        [RequiredArgument]
        public InArgument<string> UserAnswer { get; set; }

        [Category("Input/Output")]
        [RequiredArgument]
        public InOutArgument<List<bool>> UserCorrectAnswerList { get; set; }

        [Category("Input/Output")]
        [RequiredArgument]
        public InOutArgument<int> UserCorrectAnswerCount { get; set; }

        [Category("Output")]
        public OutArgument<string> QuestionText { get; set; }

        [Category("Output")]
        public OutArgument<bool> IsCorrect { get; set; }
        protected override void Execute(CodeActivityContext context)
        {
            var questions = QuestionsDictionary.Get(context);
            int questionNumber = QuestionNumber.Get(context);
            string userAnswer = UserAnswer.Get(context);

            // Get the question and correct answer.
            var question = questions[questionNumber];

            string questionText = question.Item1;
            string correctAnswer = question.Item2;

            // Compare the user's answer with the correct answer.
            bool isCorrect = string.Equals(
                    userAnswer?.Trim(),
                    correctAnswer.Trim(),
                    StringComparison.OrdinalIgnoreCase
               );

            // The last question is always considered correct.
            if (questionNumber == 5)
            {
                isCorrect = true;
            }

            // Update the results list.
            var results = UserCorrectAnswerList.Get(context);
            results.Add(isCorrect);

            // Update the correct answer counter.
            int correctCount = UserCorrectAnswerCount.Get(context);

            if (isCorrect)
            {
                correctCount++;
            }

            // Return the updated values.
            QuestionText.Set(context, questionText);
            IsCorrect.Set(context, isCorrect);
            
            UserCorrectAnswerList.Set(context, results);
            UserCorrectAnswerCount.Set(context, correctCount);


        }

    }
}
