# PrimeNumTech Scraping Project

This project scrapes information from a specific webpage and extracts data from the table. The extracted information includes post date, quest number, category code, bid/request name, and bid closing date.

## Table of Contents

- [About](#about)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## About

This Python project utilizes Selenium and BeautifulSoup to scrape data from a webpage and extract relevant information from the table. The extracted data can be used for various purposes, such as analysis or tracking upcoming bids.

## Getting Started

### Prerequisites

- [Python](https://www.python.org/downloads/) installed
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed (optional)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/vatsrounak/PrimeNumTech_ScrapingProject
   ```

2. Change to the project directory:

   ```bash
   cd Scrapping_PrimeNumTech
   ```

3. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     .venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source .venv/bin/activate
     ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the following command to execute the scraper script:

```bash
python scrape_postings.py
```

The script will print the extracted information from the table.

## Dependencies

- beautifulsoup4==4.10.0
- pandas==1.3.3
- selenium==3.141.0

## Contributing

If you'd like to contribute to the project, follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes and commit them: `git commit -m 'Description of changes'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```

