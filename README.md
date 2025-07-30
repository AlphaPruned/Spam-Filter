# 📬 Spam Filter using Probabilistic Classification

A Python-based spam filter that classifies SMS messages as spam or not spam using probabilistic reasoning, word frequency analysis, and text preprocessing. The model is trained directly from a labeled CSV file using basic conditional probability logic (similar to Naive Bayes).

---

## 📌 Overview

This project demonstrates a custom-built spam classifier trained from real SMS data. It processes a dataset, builds frequency dictionaries for spam and non-spam messages, and uses those statistics to classify new input messages using fundamental probabilistic principles without relying on external machine learning libraries.

**Key Features:**
- Custom probabilistic classification algorithm
- Text preprocessing and tokenization
- Word frequency analysis
- Real-time message classification
- Educational implementation of Naive Bayes concepts

---

## 📁 Project Structure

```
Spam-Filter/
├── 📄 Spam_filter.py     # Main script for building the model and classifying messages
├── 📄 SMS_list.csv       # Input dataset (tab-separated) with labeled SMS messages
└── 📄 README.md          # This documentation file
```

---

## 📊 Dataset Requirements

### CSV Format: `SMS_list.csv`

The dataset must be a **tab-separated** `.csv` file with two columns: **Label** and **Message**

**Example format:**
```
spam	WINNER!! You have won a free ticket to Bahamas!
notspam	Are we still on for lunch today?
spam	Congratulations! You've won £1000 cash prize!
notspam	Can you pick up some groceries on your way home?
```

**Important Notes:**
- Use `spam` or `notspam` as labels
- Ensure **no header row** in the CSV file
- Use **tab separation** between label and message
- Place this file in the same directory as `Spam_filter.py`

---

## 🧹 Features & Workflow

### 🔤 Text Preprocessing
- **Cleaning**: Removes digits, punctuation, and special symbols using regex
- **Normalization**: Converts all text to uppercase for consistency
- **Tokenization**: Splits messages into individual words
- **Stopword Removal**: Filters out high-frequency, non-informative words

### 🎯 Training Process
- **Dictionary Building**: Creates two frequency dictionaries (`spam_word` and `n_spam_word`)
- **Word Counting**: Tracks occurrence of each word in spam vs. non-spam messages
- **Probability Calculation**: Computes conditional probabilities for classification

### 🔍 Classification Algorithm
- **Input Processing**: Cleans and tokenizes new messages using the same preprocessing
- **Probability Computation**: Calculates likelihood of each word belonging to spam/non-spam
- **Decision Making**: Uses probabilistic reasoning to classify the entire message

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.6+** (no additional libraries required)
- **Dataset**: Properly formatted `SMS_list.csv` file

### Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AlphaPruned/Spam-Filter.git
   cd Spam-Filter
   ```

2. **Prepare your dataset:**
   - Ensure `SMS_list.csv` is in the same directory as `Spam_filter.py`
   - Verify the tab-separated format with no headers

3. **Run the spam filter:**
   ```bash
   python Spam_filter.py
   ```

4. **Test with messages:**
   ```
   Enter the message: You've been selected to win a free phone!
   m is spam
   ```

---

## 🔍 Example Usage

### Sample Interactions:

**Spam Detection:**
```
Enter the message: WINNER! You have won a lottery of $1000!
m is spam
```

**Non-Spam Detection:**
```
Enter the message: Your package has arrived. Collect it today.
m is not a spam
```

**Marketing Spam:**
```
Enter the message: FREE! Click here to claim your reward now!
m is spam
```

**Normal Conversation:**
```
Enter the message: Let's meet for coffee tomorrow at 3 PM
m is not a spam
```

---

## ⚙️ Algorithm Details

### Probabilistic Classification Process:

1. **Training Phase:**
   - Parse labeled dataset
   - Build word frequency dictionaries for each class
   - Calculate prior probabilities for spam/non-spam

2. **Prediction Phase:**
   - Preprocess input message
   - For each word, calculate: P(word|spam) and P(word|not_spam)
   - Apply Bayes' theorem to determine final classification

3. **Decision Rule:**
   ```
   If P(spam|message) > P(not_spam|message):
       Classify as SPAM
   Else:
       Classify as NOT SPAM
   ```

---

## 🔬 Implementation Notes

### Strengths:
- **Educational Value**: Clear implementation of probabilistic classification concepts
- **No Dependencies**: Uses only Python standard library
- **Customizable**: Easy to modify preprocessing and classification logic
- **Transparent**: All probability calculations are explicit and traceable

### Limitations:
- **No Smoothing**: May face zero probability issues with unseen words
- **Underflow Risk**: Probabilities can underflow for very long messages
- **Simple Preprocessing**: Basic text cleaning without advanced NLP techniques
- **No Cross-Validation**: Limited evaluation methodology

### Potential Improvements:
- Add Laplace smoothing for unseen words
- Implement logarithmic probabilities to prevent underflow
- Include more sophisticated text preprocessing
- Add model evaluation metrics (precision, recall, F1-score)

---

## 📈 Performance Considerations

- **Speed**: Fast classification due to simple probability calculations
- **Memory**: Efficient storage using Python dictionaries
- **Scalability**: Performance depends on vocabulary size and message length
- **Accuracy**: Depends heavily on training data quality and size

---

## 👤 Author

**Arnav Rajesh Kadu**
- GitHub: [@AlphaPruned](https://github.com/AlphaPruned)

---

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

1. **Bug Fixes**: Report and fix any issues
2. **Feature Enhancements**: Add smoothing, logging, or evaluation metrics
3. **Documentation**: Improve code comments and documentation
4. **Dataset**: Contribute additional training data

### How to Contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

## 📬 Contact

For questions, suggestions, or collaboration opportunities:
- Open an issue on GitHub
- Contact through GitHub profile

---

## 🙏 Acknowledgments

- Thanks to the SMS Spam Collection dataset contributors
- Inspired by classical machine learning approaches to text classification
