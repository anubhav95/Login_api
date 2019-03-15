import pyodbc 
from flask import Flask,jsonify,request

app=Flask(__name__)

conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};Server=(localdb)\pytest;Database=test;")
@app.route('/q1/<string:id>',methods=['GET'])
def read(id):
	
	cursor= conn.cursor()
	cursor.execute("select * from product where product_code_id=?",[id])
	items=[]
	for row,o,p,q in cursor:
		items.append({"Product Code":row,"Product name":o,"Price":p,"Image_path":q})
		
	
	return jsonify(items)
	conn.close()

@app.route('/login/',methods=['GET'])
def login():
	user  = request.args.get('user',type=str)
	pass1  = request.args.get('pass1',type=str)


	
	

	#username  = user
	#password  = pass1
	cursor= conn.cursor()
	cursor.execute("select * from login where username=? and password=?",[user,pass1])
	items1=[]
	for username1,password1 in cursor:
		items1.append({"username":username1,"password":password1})
		
	if(len(items1)>0):
		return jsonify({"status":"granted"})

	else:
		return jsonify({"status":"declined"})

	

	conn.close()

@app.route('/signup/',methods=['POST'])
def signup():

	data=request.get_json()
	user  = data['user']
	pass1  = data['pass1']
	
	

	
	cursor= conn.cursor()
	cursor.execute("insert into login(username,password) values('%s','%s')"%(user,pass1))
	conn.commit()

	return jsonify({"status":"true"})
	
	'''if(request.method == 'GET'):	
		cursor1=conn.cursor()
		cursor1.execute("select * from login where username=? and password=?",[user,pass1])
		items1=[]
	
		for username1,password1 in cursor1:
			items1.append({"username":username1,"password":password1})
		
		if(len(items1)>0):
			return jsonify({"status":"granted"})

		else:
			return jsonify({"status":"declined"})'''

	

	conn.close()	


@app.route('/find/',methods=['GET','POST'])
def find():
	user  = request.args.get('user',type=str)
	pass1  = request.args.get('pass1',type=str)
	


	cursor1=conn.cursor()
	cursor1.execute("select * from login where username=? and password=?",[user,pass1])
	items2=[]
	print(user)
	print(pass1)
	for username1,password1 in cursor1:
		items2.append({"username":username1,"password":password1})
		
	return jsonify(items2)
	

	conn.close()


if __name__ == '__main__':
   app.run(debug=True,port=8080)