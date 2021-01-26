# RedditMon

RedditMon is a dumb and janky little package I threw together so that I could learn how to package a python project.

## Installation

1. Clone this repo to your location of choice.
1. Navigate to the cloned repo
1. Install with pip by using `pip install -e .`
1. ????
1. Profit!!!

## Usage

To use this module (assuming you have it installed), create a config file in your home directory with the name `redditmon.config.ini` that contains the details of your reddit API account. Look at [this example](example_redditmon.config.ini) to see how to structure the file. Once you have your config file in place, you can launch the module directly by issuing `python3 -m redditmon <subredditname>`. Use `python3 -m redditmon --help` for more information.
