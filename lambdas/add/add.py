# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import json

def lambda_handler(event, context):
       print(event)
       
       # Check if we're processing a batch or single operation
       if 'batch' in event and event['batch'] == True:
           return process_batch(event)
       else:
           return process_single(event)
   
   def process_single(event):
       first = event['input']['first']
       second = event['input']['second']
       third = event['input']['third']
       result = event['input']['result']
       
       print(f"FIRST: {first}, SECOND: {second}, THIRD: {third}")
       
       result = int(result) + int(second)
       
       print(f"RESULT: {result}")
       
       response = {
           "first": first,
           "second": second,
           "third": third,
           "result": int(result)
       }
       
       event['input'] = response
       
       ']
   batch(event): []
       for item in event['input']['items']:['first']['second'].get('third', 0)   in batch mode item.get('result', 0)   mode
           _result = int(result) + int(second)
           
           
               "first": first,
               "second": second,
               "third": third,
               "result": int(new_result)
           })
       
       items": results}
