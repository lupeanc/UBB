using System.Activities;
using System.Activities.Expressions;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;

namespace InitializeQuizCustomActivity
{
    public class InitializeQuiz : CodeActivity
    {
        [RequiredArgument]
        public InArgument<string> QuizName { get; set; }

        public OutArgument<Dictionary<int, Tuple<string, string>>> QuestionDictionary { get; set; }
        public OutArgument<List<bool>> UserCorrectAnswerList { get; set; }
        public OutArgument<int> UserCorrectAnswerCount { get; set; }
        protected override void Execute(CodeActivityContext context)
        {
            string quizName = QuizName.Get(context);

            var questionDictionary = new Dictionary<int, Tuple<string, string>>();

            if(quizName == "Project Hail Mary")
            {
                questionDictionary.Add(1, Tuple.Create("Project Hail Mary came out in April? True or False", "True"));
                questionDictionary.Add(2, Tuple.Create("How many millions of kilograms of astrophage did Mary need to get to Tau Ceti?", "2"));
                questionDictionary.Add(3, Tuple.Create("Ryan Gosling plays the role of main character dr.Grace? True or False", "True"));
                questionDictionary.Add(4, Tuple.Create("Rocky is voiced by Morgan Freeman. True or False", "False"));
                questionDictionary.Add(5, Tuple.Create("Who is your favourite character?", ""));
            } else
            {
                questionDictionary.Add(1, Tuple.Create("Iron Lung came out in January. True or False?", "True"));
                questionDictionary.Add(2, Tuple.Create("What was the number of the SM the convict was on?", "13"));
                questionDictionary.Add(3, Tuple.Create("Mark 'Markiplier' Fischbach plays the role of 'Convict'. True or False", "True"));
                questionDictionary.Add(4, Tuple.Create("Ethan Nestor plays Jack, the engineer. True or False", "False"));
                questionDictionary.Add(5, Tuple.Create("Who is your favourite character?", ""));
            }

            
            QuestionDictionary.Set(context, questionDictionary);
            UserCorrectAnswerList.Set(context, new List<bool>());
            UserCorrectAnswerCount.Set(context, 0);
        }

    }
}
