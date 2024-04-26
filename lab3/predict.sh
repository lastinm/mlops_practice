#!/bin/bash

# toxic
curl -X 'POST' 'http://127.0.0.1:8000/predict/' -H 'Content-Type: application/json' -d '{ sepal_length: 5.2, sepal_width: 3.1, petal_length: 4.2, petal_width: 1.1 }'

