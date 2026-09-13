from fastapi import FastAPI

from fastapi_mcp import FastApiMCP


app = FastAPI(title="Calculator")

@app.post('/multiply')
def multiply(a: float, b: float):
    """Multiplies two numbers. 
       float(a)
       float(b)
       a*b - > float result
    """
    result = a*b
    return {"result" : result} 

@app.post('/add')
def add(a: float, b: float) :
    """Adds two numbers.
       float(a)
       float(b)
       a+b -> float result
    """
    result = a + b
    return {"result" : result}

@app.post('/subtract')
def subtract(a: float, b: float) :
    """Subtracts the second number from the first.
       float(a)
       float(b)
       a-b -> float result
    """
    result = a - b
    return {"result" : result}

@app.post('/divide')
def divide(a: float, b: float) :
    """Divides the first number by the second.
       float(a)
       float(b)
       a/b -> float result
    """
    result = a / b
    return {"result" : result}

@app.post('/power') 
def power(base: float, exponent: float) :
    """Raises the base to the power of the exponent.
       float(base)
       float(exponent)
       base**exponent -> float result
    """
    result = base ** exponent
    return {"result" : result}

@app.post('/sqrt')
def sqrt(x: float) :
    """Returns the square root of a number.
       float(x)
       x**0.5 -> float result
    """
    result = x ** 0.5
    return {"result" : result}

@app.post('/abs') 
def abs(x: float) :
    """Returns the absolute value of a number.
       float(x)
       |x| -> float result
    """
    result = abs(x)
    return {"result" : result}

@app.post('/max')
def max(a: float, b: float) :
    """Returns the maximum of two numbers.
       float(a)
       float(b)
       max(a, b) -> float result
    """
    result = max(a, b)
    return {"result" : result}

@app.post('/min')
def min(a: float, b: float) :
    """Returns the minimum of two numbers.
       float(a)
       float(b)
       min(a, b) -> float result
    """
    result = min(a, b)
    return {"result" : result}

@app.post('/average')
def average(a: float, b: float) :
    """Returns the average of two numbers.
       float(a)
       float(b)
       (a + b) / 2 -> float result
    """
    result = (a + b) / 2
    return {"result" : result}

mcp = FastApiMCP(app, name="Calculator MCP")
mcp.mount_http()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)