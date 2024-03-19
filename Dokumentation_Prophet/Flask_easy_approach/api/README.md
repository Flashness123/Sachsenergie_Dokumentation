#Calling the data:
curl --location --request POST 'http://127.0.0.1:5000/forecast-n-days' --header 'Content-Type: application/json' --data-raw '{
    "days" : 1
}'

OR

curl --location --request POST 'http://127.0.0.1:5000/forecast-n-days' --header 'Content-Type: application/json' --data-raw '{}'

OR

