# Unsupervised Learning Case Study

In this case study you'll get to work in a situation much more like that which you'll find in both your personal projects, while interviewing, and in industry. What is meant by that? Our data is usually unstructured/dirty and our problem ill/undefined.

## The Data

There are two data sets you can choose to work from, one about UFO sightings and the other about bigfoot sightings.

### UFO Sightings

A data set of UFO sighting reports was collected from [The National UFO Reporting Center Online Database](http://www.nuforc.org/webreports.html); you can see an example report [here](http://www.nuforc.org/webreports/133/S133931.html). The data, downloadable as a zipped `json` file [here](https://s3.amazonaws.com/ufodatafordarren/ufodata.json.zip), contains the URL, raw HTML for that URL, and the time it was scraped for each report in the database along with the remnants of a database id.

### Bigfoot Sightings

A data set of bigfoot sighting reports was collected from the [Geographic Database of Bigfoot / Sasquatch Sightings & Reports](http://www.bfro.net/gdb/); you can see an example report [here](http://www.bfro.net/GDB/show_report.asp?id=13038). The data, downloadable as a zipped `json` file [here](https://s3.amazonaws.com/ufodatafordarren/bigfoot_data.json.zip), contains the URL, raw HTML for that URL, and the time it was scraped for each report in the database along with the remnants of a database id.

## The Problem

Find something interesting in the data! That's not very specific, so here are some thoughts to get you going:
* What state has the most UFO/bigfoot sightings? Can you visualize this/compare them?
* What kind of language is used to describe UFO vs. bigfoot sightings. Does it vary by region or time?

A huge part of the challenge for this case study will be getting the data into a usable form, so don't fret about finding something mind-blowingly insightful in the data. Simply verifying a suspicion you have with a model or summarizing a quality about the data that is difficult to see in the raw data is good data science.

## Resources

Turns out the person who scraped the data left the beginnings of a Python script to load the data with, but even they left a note that it's not very helpful.

```python
import json

# TODO: this doesn't scale well and doesn't help with looking at the data.
#       Possible solutions: load into pandas dataframe or mongodb, maybe both.
reports = []
with open('bigfoot_data.json') as f:
    for i in f:
        reports.append(json.loads(i))
```
