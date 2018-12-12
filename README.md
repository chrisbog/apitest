# apitest

## Overview
This application is a very simple application that uses Flask to create a very simple web based API.

## Details
After you run the application, you can hit the api calls by creating a web based url to hit each API.   There are four main calls within the application and they are defined in more detailed below:   The purpose of the application is show how easy it is to create a simple web based API.

## API Call details

### overview
```http://{ip address}:5000/```
This call just displays a message welcoming to the application:
Sample output:
```Welcome to the apitest application using flask```

### getcurrentdate
```http://{ip address}:5000/api/getcurrentdate```

This call will display the current date and time:

Sample output:
```The current time is: 2018-12-12 12:57:53.240347```

### adddaystocurrentdate
```http://{ip address}:5000/api/adddaystocurrentdate/{value}```

This call will add the number specified in the {value} paramter to the current date.

Sample output:
```
http://127.0.0.1:5000/api/adddaystocurrentdate/90

The current time is: 2018-12-12 12:59:16.426493. When we add 90 days, we get: 2019-03-12 12:59:16.426516
```

### addvaluetocurrentdate
```http://{ip address}:5000/api/addvaluetocurrentdate?value={number}&{days|minutes|hours}```

This call will demonstrate a variable paramter list with multiple choices.

Sample output:
```
http://127.0.0.1:5000/api/addvaluetocurrentdate?value=100&hours

The current time is: 2018-12-12 13:02:10.417220. When we add 100 hours, we get: 2018-12-16 17:02:10.417207
```
