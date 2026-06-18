from flask import Flask
from flask import jsonify
app = Flask(__name__)

def calibration(amount):
    # calculate the 
    res = []
    coins = [175,395,440,627,692] # weight in mg of toonies, loonies, quarters, dimes nickels (from lightest to heaviest, not monetary denom.)
    coin_lookup = {692: "toonies", 
                   627: "loonies", 
                   440: "quarters", 
                   395: "nickels", 
                   175: "dimes"}

   
    # record the number of coins that evenly divide and the remainder
    rem = int(amount)
    for coin in reversed(coins): # start with the heaviest coin
        num, rem = divmod(rem, coin)
        if num:
            res.append({num:coin_lookup[coin]})
    # append the coin type and number of coins that had no remainder
        
   # while rem > 0:
    #    coin = coins.pop()
     #   num, rem = divmod(rem, coin)
      #  if num:
       #     if coin in coin_lookup:
        #        res.append({num:coin_lookup[coin]})
    print(f"amount={amount}")
    print(f"coin={coin}, num={num}, rem={rem}")
    print(amount)
    return res


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return 'coin-weight service running: /weight/<miligrams>'

@app.route('/weight/<miligrams>')
def weightroute(miligrams):
    print(f"Make weight for {miligrams}")
    amount = f"{miligrams}"
    result = calibration(float(amount))
    return jsonify(result)
    
    
@app.route('/100/weight/<grams>/<miligrams>')
def change100route(grams, miligrams):
    print(f"Make weight for {miligrams}")
    amount = f"{miligrams}"
    amount100 = float(amount) * 100
    print(f"This is the {amount} X 100")
    result = calibration(amount100)
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
