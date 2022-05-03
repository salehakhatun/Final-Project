import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import pickle as pickle


from flask import Flask, render_template,redirect,request
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import os
from sqlalchemy import create_engine

import matplotlib.image as mpimg 

PEOPLE_FOLDER = 'static'

app = Flask(__name__,template_folder='templates')
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
@app.route("/")
def echo():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'fig3.png')
    map_img = mpimg.imread('static/Images/smart dolphin.jpg') 
    plt.figure(figsize=(15,10))
    hmax=sns.barplot(data=df,x='bedrooms',y='price',palette='Set2',zorder = 2)
    hmax.imshow(map_img,
            aspect = hmax.get_aspect(),
            extent = hmax.get_xlim() + hmax.get_ylim(),
            zorder = 1,alpha = 0.5)
    plt.xlabel("Number of bedrooms", size=20)
    plt.ylabel("price", size=20)
    plt.title("Total Price of Houses in Melbourne by bedrooms", size=25)
    plt.tight_layout()
    plt.savefig("static/Images/fig1.png")
    map_img = mpimg.imread('images/smart dolphin.jpg') 

    plt.figure(figsize=(15,10))
    hmax=sns.barplot(data=df,x='bathrooms',y='price',palette='Set2',zorder = 2)
    hmax.imshow(map_img,
            aspect = hmax.get_aspect(),
            extent = hmax.get_xlim() + hmax.get_ylim(),
            zorder = 1,alpha = 0.5)
    plt.xlabel("Number of bathrooms", size=20)
    plt.ylabel("price", size=20)
    plt.title("Total Price of Houses in Melbourne by bathrooms", size=25)
    plt.tight_layout()
    plt.savefig("static/Images/fig2.png")
    map_img = mpimg.imread('static/Images/smart dolphin.jpg') 

    plt.figure(figsize=(15,10))
    hmax=sns.barplot(data=df,x='carspaces',y='price',palette='Set2',zorder = 2)
    hmax.imshow(map_img,
            aspect = hmax.get_aspect(),
            extent = hmax.get_xlim() + hmax.get_ylim(),
            zorder = 1,alpha = 0.5)
    plt.xlabel("Number of Carport", size=20)
    plt.ylabel("price", size=20)
    plt.title("Total Price of Houses in Melbourne by Carport", size=25)
    plt.tight_layout()
    plt.savefig("static/Images/fig3.png")
    # plotting a heat map for all numeric variables
    plt.figure(figsize=(15,12))
    sns.heatmap(df.corr(),cmap = 'coolwarm',linewidth = 1,annot= True, annot_kws={"size": 9})
    plt.title('HEAT MAP', fontsize=15)
    plt.tight_layout()
    plt.savefig("static/Images/fig4.png")
    # most of the properties sold are type
    map_img = mpimg.imread('static/Images/smart dolphin.jpg')
    plt.figure(figsize=(15,10))
    hmax=sns.barplot(data=df,x='propertytype',y='price',palette='Set2',zorder = 2)
    hmax.imshow(map_img,
            aspect = hmax.get_aspect(),
            extent = hmax.get_xlim() + hmax.get_ylim(),
            zorder = 1,alpha = 0.5)
    plt.xlabel("Property Type", size=20)
    plt.ylabel("price", size=20)
    plt.title("Types Of property", size=25)
    plt.tight_layout()
    plt.savefig("static/Images/fig5.png")
    df.hist(bins=50, figsize=(15,10))
    plt.savefig("attribute_histogram_plots")
    plt.savefig("static/Images/fig6.png")
    return render_template("index.html", text=    full_filename)

@app.route("/Data_1.html")
def Data1():

        #convert the SQL database results into PANDAS data frame 
        VIC= pd.DataFrame(data_VIC).to_html(index=False,table_id="datatablesSimple",classes="VIC")
        LGA_ID= pd.DataFrame(data_LGA_ID).to_html(index=False,table_id="datatablesSimple",classes="LGA_AD")
        PostcodeLGA= pd.DataFrame(data_PostcodeLGA).to_html(index=False,table_id="datatablesSimple",classes="PostcodeLGA")
        Listings= pd.DataFrame(data_Listings).to_html(index=False,table_id="datatablesSimple",classes="Listings")
        dataList=[VIC,LGA_ID,PostcodeLGA,Listings]

    
    
    
        return render_template("Data_1.html",table=dataList)

@app.route("/Plot_3.html")
def Plot3():

     

    
    
    
        return render_template("Plot_3.html")
@app.route("/Comparison_1.html", methods=['GET', 'POST'])
def Machine():
        Listings=pd.DataFrame(data_Listings)
        vic=pd.DataFrame(data_VIC)
        postcode=pd.DataFrame(data_PostcodeLGA)
        countries1=postcode.merge(Listings, left_on='domain_id', right_on='domain_id', suffixes=(False, False))
        countries1=vic.merge(countries1, left_on='domain_id', right_on='domain_id', suffixes=(False, False))
        countries1=countries1.dropna()
        
        postcodes='#'+countries1['streetnumber']+' '+countries1['streetname']+' ' +countries1['streettype']+' '+countries1['suburb']+'!'+countries1['domain_id'].astype(str)+'@'+ countries1['postcode'].astype(str)+'$'+ countries1['propertydetailsurl']+'&'+ countries1['mediansoldprice'].astype(str)+'#';
        postcodes=postcodes.values.tolist()
        print(postcodes)
        if request.method == 'GET':
        # Just render the initial form, to get input
                return render_template('Comparison_1.html',countries1=postcodes)
      
        if request.method == 'POST':
                # Extract the input
                Postcode= request.form['Postcode']
                Bedrooms =request.form['Bedrooms']
                Bathroom =request.form['Bathroom']
                Carport = request.form['Carport']
                LandSize =request.form['LandSize']
                medianprice = request.form['medianprice']
                medianprice=medianprice.replace("$", "")
                medianprice=medianprice.replace(",", "")
                medianprice=float(medianprice)

        

                testdata=[Postcode,Bedrooms,Bathroom,Carport,LandSize,medianprice]
                my_array = np.array(testdata).reshape(1, -1)
                y_predLR = loaded_model.predict(my_array)
    
    
                return render_template("Comparison_1.html",countries1=postcodes,
                                      
                result=round(y_predLR[0]))
# for the username and password i have created a pgAdmin user acount named SQL_challange
engine = create_engine('postgresql://SQL_challange:SQL_challange@localhost:5432/property')
connection = engine.connect()
query="SELECT *                         \
        FROM vic v                      \
        FUll OUTER JOIN listings l      \
        ON v.domain_id=l.domain_id;"
#run the query
data = pd.read_sql_query(query,engine)

#convert the SQL database results into PANDAS data frame 
df= pd.DataFrame(data)
df.drop_duplicates()
drop_all_na = df.dropna(how = 'any')


query="SELECT * FROM vic"  
query1="SELECT * FROM LGA_ID"
query2="SELECT * FROM PostcodeLGA"
query3="SELECT * FROM Listings"
#run the query
data_VIC = pd.read_sql_query(query,engine)
data_LGA_ID= pd.read_sql_query(query1,engine)
data_PostcodeLGA= pd.read_sql_query(query2,engine)
data_Listings= pd.read_sql_query(query3,engine)
filename = 'static/assets/finalized_model.pkl'

 
# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))

if __name__ == "__main__":
    app.run(debug=True)