# LinkedIn-Auto-Connector 

This is a auto connect linkedin bot wich connects the all the people on the first page of a particular company when give the name of that company 

## Getting started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

1. Install selenium. I used `pip` to install the selenium package.

``` bash
pip install selenium
pip install webdriver_manager
pip install tinydb 
   ```

2. Selenium requires a driver to interface with the chosen browser. Make sure the driver is in your path, you will need to add your `driver_path` to the `config.json` file.

I used the Chrome driver, you can download it [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). You can also download [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/), [Firefox](https://github.com/mozilla/geckodriver/releases) or [Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10/). Depends on your preferred browser.

### Usage

Fork and clone/download the repository and change the configuration file with:

* Your email linked to LinkedIn.
* Your password.
* Keywords for finding specific company's employes ID.

**Note**: It does not share your `LinkedIn` credentials, so it is safe to use.

Please feel free to comment or give suggestions/issues.
