from flask import Flask,request
from datetime import datetime,timedelta


print ("apitest starting\n")
app = Flask(__name__)

#
# This route will display when the home page is hit.
#
@app.route('/')
def index():
    return "Welcome to the apitest application using flask\n"

#
# this route will implement the getcurrentdate function call to return the date
#
@app.route('/api/getcurrentdate',methods=['GET'])

def getcurrenttime():
    return ("The current time is: "+str(datetime.now()))

#
# This route will implement the adddaystocurrentdate function call
#
@app.route('/api/adddaystocurrentdate/<int:numdays>', methods=['GET'])

def adddatetocurrentdate(numdays):
    return ("The current time is: " + str(datetime.now())+".  When we add "+str(numdays)+" days, we get: " +str(datetime.now()+ timedelta(days=numdays) ) )

#
# This route will implement the adddaystocurrentdate function call and accept a variable paramter list
#
@app.route('/api/addvaluetocurrentdate', methods=['GET'])

def addcurrenttime():
    if 'value' in request.args:
        val=int(request.args['value'])
    else:
        return "Error: No value field provided, please specify a value to add"

    if 'days' in request.args:
        newdate=datetime.now()+ timedelta(days=val)
        param = 'days'
    elif 'minutes' in request.args:
        newdate = datetime.now() + timedelta(minutes=val)
        param = 'minutes'
    elif 'hours' in request.args:
        newdate = datetime.now() + timedelta(hours=val)
        param = 'hours'
    else:
        return "Error: parameter field provided. Please specify one out of: (day, minutes, hours)"

    return ("The current time is: " + str(datetime.now())+".  When we add "+str(val)+" "+param+", we get: " +str(newdate ) )






if __name__ == '__main__':
    app.run()

