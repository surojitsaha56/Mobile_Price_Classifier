from urllib import request
import flask
import pickle
import pandas as pd
import numpy as np

import random




from sklearn.preprocessing import StandardScaler


#load models at top of app to load into memory only one time
with open('models/Dtree.pickle', 'rb') as f:
    clf_dtree= pickle.load(f)





app = flask.Flask(__name__, template_folder='templates')
@app.route('/result',methods=['GET','POST'])
def result():
    if request.method=="POST":
        r=request.form
        return flask.render_template("result.html",res=r)
    
@app.route('/', methods = ['GET', 'POST'])
def main():
        return flask.render_template('home.html')



@app.route("/mobile", methods=['GET', 'POST'])
def mobile():
    
    if flask.request.method == 'GET':
        
        return (flask.render_template('mobile.html'))

    
    if flask.request.method =='POST':
        
        touch_screen = flask.request.form.get('touch_screen')
        print(touch_screen)
        three_g = flask.request.form.get('Three_g')

        dual_sim = flask.request.form.get('dual_sim')
        
        ram = flask.request.form.get('ram')
        
        height = flask.request.form.get('pxh')

        width = flask.request.form.get('pxw')

        ncore = flask.request.form.get('ncore')

        weight = flask.request.form.get('mwt')

        battery = flask.request.form.get('bp')
        print(battery,ram)
        output_dict = dict()
        output_dict['Touch_Screen'] = touch_screen
        output_dict['3G'] = three_g
        output_dict['RAM (MB)'] = ram
        output_dict['Pixel_Width'] = width
        output_dict['Pixel_Height'] = height
        output_dict['Number_of_Cores'] = ncore
        output_dict['Mobile_weight (gms)'] = weight
        output_dict['Dual_Sim'] = dual_sim
        output_dict['Battery_Power (mAh)'] = battery
        
        x=np.array([touch_screen,three_g,ram,width,height,ncore,weight,dual_sim,battery])
        
        print('------this is array data to predict-------')
        print('X = '+ str(x))
        print('------------------------------------------')

        pred = clf_dtree.predict([x])

        price = 0
        #Predicting price
        if pred == [0]:
            price = random.randrange(5000, 7000, 500)
        elif pred == [1]:
            price = random.randrange(7000, 10000, 500)
        elif pred == [2]:
            price = random.randrange(10000, 15000, 500)
        else:
            price = random.randrange(15000, 30000, 500)


        print("Congrats",clf_dtree.predict([x]))
        
        return flask.render_template('result.html', 
                                     original_input=output_dict,
                                     result = pred, price = price)


        
        
      
if __name__ == '__main__':
    app.run(debug=True)