const questions = [
    {
  "question": "Artificial Intelligence is best described as:",
  "answers": [
    "only deep learning",
    "a field that creates systems able to perform tasks requiring human intelligence",
    "only rule-based programming",
    "only mathematical optimization"
  ],
  "correct": "b"
},
{
  "question": "Which statements about Classical AI are correct?",
  "answers": [
    "Knowledge is represented explicitly using rules, symbols, or logic.",
    "It usually depends on hand-crafted knowledge.",
    "It learns all knowledge automatically from large datasets.",
    "Typical methods include state-space search and expert systems."
  ],
  "correct": "abd"
},
{
  "question": "Which statements about Modern AI are correct?",
  "answers": [
    "Knowledge is learned implicitly through parameters.",
    "It is usually data-driven or statistical.",
    "Its behavior can depend on the training data.",
    "It never uses optimization."
  ],
  "correct": "abc"
},
{
  "question": "In supervised learning, a data point is usually represented as:",
  "answers": [
    "(x, y), where x is the input and y is the correct output",
    "(w, h), where w is the loss and h is the dataset",
    "(p, q), where p is the model and q is the algorithm",
    "only y, because the input is not needed"
  ],
  "correct": "a"
},
{
  "question": "What is a dataset?",
  "answers": [
    "A single prediction made by the model.",
    "A collection of examples/data points used for training or testing.",
    "The final trained model.",
    "The gradient of the loss function."
  ],
  "correct": "b"
},
{
  "question": "What is a hypothesis in machine learning?",
  "answers": [
    "A possible model or prediction rule.",
    "The true probability distribution of the data.",
    "The number of training examples.",
    "The error on the validation set."
  ],
  "correct": "a"
},
{
  "question": "What does the hypothesis space H represent?",
  "answers": [
    "The set of all possible models we are allowed to choose from.",
    "The set of all labels in the dataset.",
    "The set of all wrong predictions.",
    "The set of all validation errors."
  ],
  "correct": "a"
},
{
  "question": "In the formula h_hat in argmin over h in H of the average loss, what does h_hat mean?",
  "answers": [
    "The worst model after training.",
    "The selected/trained model with minimum average training loss.",
    "The dataset used for training.",
    "The true label of a data point."
  ],
  "correct": "b"
},
{
  "question": "What does a loss function measure?",
  "answers": [
    "How wrong the model's prediction is.",
    "How many features the input has.",
    "How many examples are in the dataset.",
    "How large the dataset file is."
  ],
  "correct": "a"
},
{
  "question": "Empirical Risk Minimization means:",
  "answers": [
    "minimizing the average loss on the available training dataset",
    "choosing a model randomly",
    "maximizing the validation error",
    "training without a loss function"
  ],
  "correct": "a"
},
{
  "question": "Why do we use empirical risk instead of true risk?",
  "answers": [
    "Because the true data distribution is usually unknown.",
    "Because training data is always infinite.",
    "Because models cannot make predictions on training data.",
    "Because loss functions are not numeric."
  ],
  "correct": "a"
},
{
  "question": "What is the i.i.d. assumption in simple terms?",
  "answers": [
    "Training and validation examples should come from the same kind of data source.",
    "The model should memorize the training data exactly.",
    "The validation set must always be easier than the training set.",
    "The algorithm must use only one data point."
  ],
  "correct": "a"
},
{
  "question": "Overfitting means:",
  "answers": [
    "the model is too simple and cannot learn the training data",
    "the model fits the training data too closely and generalizes badly",
    "the model has no parameters",
    "the dataset has no labels"
  ],
  "correct": "b"
},
{
  "question": "Underfitting means:",
  "answers": [
    "the model is too simple to capture the real pattern",
    "the model memorizes the training data perfectly",
    "the validation error is always zero",
    "the training set and validation set are identical"
  ],
  "correct": "a"
},
{
  "question": "In linear regression, h_w(x) = w^T x means:",
  "answers": [
    "the model predicts by computing a weighted sum of the input features",
    "the model chooses a random output",
    "the model only works for classification",
    "the model ignores the weights"
  ],
  "correct": "a"
},
{
  "question": "In the linear regression error (y - w^T x)^2, what is y?",
  "answers": [
    "the model's prediction",
    "the true/correct value",
    "the learning rate",
    "the number of features"
  ],
  "correct": "b"
},
{
  "question": "In the linear regression error (y - w^T x)^2, what is w^T x?",
  "answers": [
    "the true label",
    "the model's prediction",
    "the dataset size",
    "the regularization strength"
  ],
  "correct": "b"
},
{
  "question": "Ridge regression minimizes:",
  "answers": [
    "prediction error only",
    "weight penalty only",
    "prediction error plus a penalty for large weights",
    "validation error minus training error"
  ],
  "correct": "c"
},
{
  "question": "In ridge regression, alpha ||w||_2^2 is used to:",
  "answers": [
    "punish very large weights",
    "increase overfitting",
    "remove the labels from the dataset",
    "replace the prediction error completely"
  ],
  "correct": "a"
},
{
  "question": "What happens when the regularization parameter alpha is very large?",
  "answers": [
    "The model is strongly pushed toward smaller weights.",
    "The model ignores the penalty.",
    "The dataset becomes larger.",
    "The hypothesis space becomes unlimited."
  ],
  "correct": "a"
}
]