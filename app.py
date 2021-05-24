from flask import Flask,jsonify,request

# inicio flask 
app=Flask(__name__)

# importo la lista de productos desde el script products
from products import products

# si hago GET a ping hago ejecuto algo
@app.route("/ping",methods=['GET'])
def ping():
    return jsonify({"message":"pong"})
    
# mostrar productos
@app.route("/products",methods=['GET'])
def getProducts():
    return jsonify({"products":products,"message":"Lista de productos"})


# mostrar producto particular
@app.route("/products/<string:product_name>",methods=['GET'])
def getProduct(product_name):
    for i in products:
        if(i['name']==product_name):
            return jsonify(i)
    return jsonify({"message":'Producto no encontrado'})

# agregar nuevo producto
@app.route("/products",methods=['POST'])
def addProduct():
    try:
        new_product={
            "name":request.json['name'],
            "price":request.json['price'],
            "quantity":request.json['quantity']
        }
        products.append(new_product)
        return jsonify({"message":"Producto agregado","products":products})
    except:
        return jsonify({"message":"Hubo un error"})

# editar producto
@app.route("/products/<string:product_name>",methods=['PUT'])
def editProduct(product_name):
    for i in products:
        if(i['name']==product_name):
            i['name']=request.json['name'];
            i['price']=request.json['price'];
            i['quantity']=request.json['quantity'];
            return jsonify({"message":"Producto Editado","products":products})
    return jsonify({"message":'Producto no encontrado'})

# eliminar producto
@app.route("/products/<string:product_name>",methods=['DELETE'])
def deleteProducto(product_name):
    for i in products:
        if(i['name']==product_name):
            products.remove(i)
            return jsonify({"message":"Producto Eliminado","products":products}) 
    return jsonify({"message":'Producto no encontrado'})


if __name__ =="__main__":
    app.run(debug=True,port=4000) #modo debug..