from fastmcp import FastMCP

mcp = FastMCP(name = "Calculator")

@mcp.tool(
    name="multiply",
    description =" this going to multiply two numbers",
    tags={"multiply","arithmetic"}
)
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers. 
       float(a)
       float(b)
       a*b - > float result
    """
    return a * b    

@mcp.tool
def add(a: float, b: float) -> float:
    """Adds two numbers.
       float(a)
       float(b)
       a+b -> float result
    """
    return a + b    

@mcp.tool
def subtract(a: float, b: float) -> float:
    """Subtracts the second number from the first.
       float(a)
       float(b)
       a-b -> float result
    """
    return a - b    

@mcp.tool
def divide(a: float, b: float) -> float:
    """Divides the first number by the second.
       float(a)
       float(b)
       a/b -> float result
    """
    return a / b

@mcp.tool
def power(base: float, exponent: float) -> float:
    """Raises the base to the power of the exponent.
       float(base)
       float(exponent)
       base**exponent -> float result
    """
    return base ** exponent

@mcp.tool
def sqrt(x: float) -> float:
    """Returns the square root of a number.
       float(x)
       x**0.5 -> float result
    """
    return x ** 0.5

@mcp.tool
def abs(x: float) -> float:
    """Returns the absolute value of a number.
       float(x)
       |x| -> float result
    """
    return abs(x)

@mcp.tool
def max(a: float, b: float) -> float:
    """Returns the maximum of two numbers.
       float(a)
       float(b)
       max(a, b) -> float result
    """
    return max(a, b)

@mcp.tool
def min(a: float, b: float) -> float:
    """Returns the minimum of two numbers.
       float(a)
       float(b)
       min(a, b) -> float result
    """
    return min(a, b)

@mcp.tool
def average(a: float, b: float) -> float:
    """Returns the average of two numbers.
       float(a)
       float(b)
       (a + b) / 2 -> float result
    """
    return (a + b) / 2


if __name__ =="__main__":
    mcp.run()