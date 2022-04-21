import flask
import pickle
import pandas as pd
import numpy as np


from sklearn.preprocessing import StandardScaler


#load models at top of app to load into memory only one time
with open('models/Dtree.pickle', 'rb') as f:
    clf_dtree= pickle.load(f)

9
# with open('models/knn_regression.pkl', 'rb') as f:
#     knn = pickle.load(f)    
#ss = StandardScaler()


# genders_to_int = {'MALE':1,
#                   'FEMALE':0}

# married_to_int = {'YES':1,
#                   'NO':0}

# education_to_int = {'GRADUATED':1,
#                   'NOT GRADUATED':0}

# dependents_to_int = {'0':0,
#                       '1':1,
#                       '2':2,
#                       '3+':3}

# self_employment_to_int = {'YES':1,
#                           'NO':0}                      

# property_area_to_int = {'RURAL':0,
#                         'SEMIRURAL':1, 
#                         'URBAN':2}




app = flask.Flask(__name__, template_folder='templates')
# @app.route('/')
# def main():
#     return (flask.render_template('index.html'))

# @app.route('/report')
# def report():
#     return (flask.render_template('report.html'))

# @app.route('/jointreport')
# def jointreport():
#     return (flask.render_template('jointreport.html'))


@app.route("/", methods=['GET', 'POST'])
def mobile():
    
    if flask.request.method == 'GET':
        
        return (flask.render_template('mobile.html'))

    
    if flask.request.method =='POST':
        
        # touch_screen
        touch_screen = flask.request.form.get('touch_screen')
        print(touch_screen)
        # Three_g
        three_g = flask.request.form.get('Three_g')

        # Dual Sim
        dual_sim = flask.request.form.get('dual_sim')
        
        # RAM
        ram = flask.request.form.get('ram')
        
        # Pixel Height
        height = flask.request.form.get('pxh')

        # Pixel Width
        width = flask.request.form.get('pxw')

        # N-cores
        ncore = flask.request.form.get('ncore')

        # Mobile weight
        weight = flask.request.form.get('mwt')

        # Battery Power
        battery = flask.request.form.get('bp')
        print(battery,ram)
        #create original output dict
        output_dict = dict()
        output_dict['touch_screen'] = touch_screen
        output_dict['three_g'] = three_g
        output_dict['ram'] = ram
        output_dict['px_width'] = width
        output_dict['px_height'] = height
        output_dict['n_cores'] = ncore
        output_dict['mobile_wt'] = weight
        output_dict['dual_sim'] = dual_sim
        output_dict['battery_power'] = battery
        # x =[0,0,0,0,0,0,0,0,0]
        # x[0] = touch_screen
        # x[1] = three_g
        # x[2] = ram
        # x[3] = width
        # x[4] = height
        # x[5] = ncore
        # x[6] = weight
        # x[7] = dual_sim
        # x[8] = battery
        
        x=np.array([touch_screen,three_g,ram,width,height,ncore,weight,dual_sim,battery])
        
        print('------this is array data to predict-------')
        print('X = '+ str(x))
        print('------------------------------------------')

        pred = clf_dtree.predict([x])
        print("Cnograts",clf_dtree.predict([x]))
        # if pred==1:
        #     res = '🎊🎊Congratulations! your Loan Application has been Approved!🎊🎊'
        # else:
        #         res = '😔😔Unfortunatly your Loan Application has been Denied😔😔'
        

 
        #render form again and add prediction
        return flask.render_template('mobile.html', 
                                     original_input=output_dict,
                                     result = pred,)


        
        # temp = pd.DataFrame(index=[1])



        # temp['genders_type'] = genders_to_int[genders_type.upper()]
        # #marriage status as boolean YES: 1 , NO: 0
        # temp['marital_status'] = married_to_int[marital_status.upper()]
        # #Dependents: No. of people dependent on the applicant (0,1,2,3+)
        # temp['dependents'] = dependents_to_int[dependents.upper()]
        # #education status as boolean Graduated, Not graduated.
        # temp['education_status'] = education_to_int[education_status.upper()]
        # #Self_Employed: If the applicant is self-employed or not (Yes, No)
        # temp['self_employment'] = self_employment_to_int[self_employment.upper()]
        # #Applicant Income
        # temp['applicantIncome'] = applicantIncome
        # #Co-Applicant Income
        # temp['coapplicantIncome'] = coapplicantIncome
        # #loan amount as integer
        # temp['loan_amnt'] = loan_amnt
        # #term as integer: from 10 to 365 days...
        # temp['term_d'] =  term_d 
        # # credit_history
        # temp['credit_history'] = credit_history
        # # property are
        # temp['property_area'] = property_area_to_int[property_area.upper()]

        # temp['loan_amnt_log']=np.log(temp['loan_amnt'])

        # Feature Engineering :
        #temp['Total_Income']= temp['applicantIncome']+temp['coapplicantIncome']
        #temp['Total_Income_log'] = np.log(temp['Total_Income'])
        #temp['EMI']= temp['loan_amnt']/temp['term_d']
        #temp['Balance Income'] = temp['Total_Income']-(temp['EMI']*1000)

        # Columns to drop and afterward Predict up on the feature engineered columns
        #temp = temp.drop(['applicantIncome', 'coapplicantIncome', 'loan_amnt', 'term_d'], axis=1)



        # Credit_History is the most important feature followed by Balance Income, Total Income, EMI. 
        # So, feature engineering helped us in predicting our target variable.
        


        
        
            
        # #make prediction
        
        
      
if __name__ == '__main__':
    app.run(debug=True)