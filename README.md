# SoothSocial

## Overview
SoothSocial is a project that collects social media comments on a given subject and determines the overall sentiment behind them. It is being developed as a tool to aid media outlets in predicting popularity, sentiment, and recommended tone to be used when writing a story on a given subject. Ideally, it will eventually be capable of recommending which stories to report on based on a pool of current leads.

## Current State
SoothSocial is currently in the extremely experimental stages. It is currently only capable of collecting data from Twitter, and currently uses lexicon-based sentiment analysis. It is very, very rough at the moment.


## TODO:
### Next Steps:
- Switch from lexicon-based sentiment analysis to ML-based sentiment analysis, ideally using TensorFlow.
- Add modules to collect comments from Facebook, Reddit
- Add modules to retrieve data from ElasticSearch clusters.

### Future steps:
- Add geo-location to limit returns to specific areas
- Build webUI to make searches user friendly
- Add map of returned comments, and their platforms
- Add feature to restrict returns to specific areas, controlled within web UI
	(like clicking a specific section of a city to limit returns to that specific area.)


