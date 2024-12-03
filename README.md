# Edgeword-Finder

A Python-based tool for discovering words that match specific patterns at their edges. Filter, analyze, and uncover unique word lists tailored to your needs.

## Features

- **Edgeword Matching**: Identify words where the beginning and end match specific criteria. 
- **Custom Filtering**: Apply filters for rarity, common names, or unusual word types. 
- **Multi-Dataset Integration**: Combines word data from multiple sources to create extensive and customizable searches. You can use any dictionary you'd like.
- **Deduplication & Sorting**: Automatically removes duplicates and sorts results alphabetically. Note: ALphabeticAL is an edgeword of order 2!
- **Flexible Parameters**: Adjustable settings for pattern length, frequency thresholds, and filtering options.  Note: lower frequency parameters correspond to more results.

## Installation

1. Clone this repository: 
   git clone https://github.com/your-username/edgeword-finder.git
2. Install the required dependencies: 
   pip install -r requirements.txt

## Usage

Run the tool from the command line: 
python main.py

### User Prompts

- **Number of Letters**: Specify the number of letters to match at the start and end of each word. 
- **Include Unusual Words**: Decide whether to include or filter out rare words, names, or places. 
- **Frequency Threshold**: Set a threshold for word frequency, with a default of 0.00000001.

## Attribution

The term **Edgeword** was coined by Andrew T. Cadotte. Any derivative works or discussions related to this project should credit the original author.

## License

This project is licensed under the **Apache 2.0 License**. See the LICENSE file for details.

## Contributions

Contributions are welcome! Please fork the repository and submit a pull request for any features or fixes.

## Contact

For questions or feedback, feel free to open an issue or contact me at cadottea@umich.edu.