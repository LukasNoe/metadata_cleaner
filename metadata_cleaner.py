#This is a script to clean a JSON metadata file and remove unwanted columns; then convert it into csv

import json
import csv
import pandas as pd
import numpy as np
from glob import glob

#Load and read the JSON file
def read_metadata():
    data = []
    for json_file in glob('metadata/*.json'):
        # read in the newline separated json file
        with open(json_file, 'r', encoding = 'UTF-8') as f_in:
            for line in f_in:
                data.append(json.loads(line))
    return data

def read_missing_id():
    with open('iids_missing_images.json', 'r') as missing_id:
        return set(json.load(missing_id))


#check if all ids in file are unique
def _check_all_ids_are_unique(data):
    assert len(data) == len(set([val['id'] for val in data]))

#check for objects without/too many media entries, and remove them
def _check_for_images(data, mediaCount):
    if mediaCount != 1: 
        return 0


def _create_df(data):
    cleanData = []
    missing_id = read_missing_id()
    for rows in data:
        iid = rows['id']
        if iid in missing_id:
            continue

        
        #name = rows['content']['freetext']['name']['content']
        title = rows['content']['descriptiveNonRepeating']['title']['content']
        #date = rows['content']['freetext']['date']['content']
        
        date = rows['content']['freetext'].get('date', None)
        if date:
            date = date[0]['content']
        
        #object_type = rows['content']['indexedStructured']['object_type']

        
        
        #culture = rows['content']['indexedStructured']['culture']
        #topic = rows['content']['indexedStructured']['topic']

        





    cleanData.append((iid, title, date))
    print(len(cleanData))

    df = pd.DataFrame(cleanData, columns = ['iid', 'title', 'date'])
    print(df.head(5))

#question: how to find all keys in dict?
"""
def _find_all_keys(data):
    for keys in data:
        print(keys)
"""


if __name__ == '__main__':
    # read all of the metadata
    data = read_metadata()
    
    #call missing_id function
    read_missing_id()
    
    #call clean data function
    _create_df(data)
  
   # _find_all_keys(data)


"""
    # sanity check that all ids are unique
    _check_all_ids_are_unique(data)

    # sanity check: do all entries online have one media source?
    _check_all_media_has_only_one_image(data)

    # fetch the images
    missing = download_images(data)
    
    # write those missing to file
    with open('metadata/iids_missing_images.json', 'w') as m_out:
        json.dump(missing, m_out)
"""