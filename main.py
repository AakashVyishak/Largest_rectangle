from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
from datetime import datetime
from typing import List


logging.basicConfig(filename='app.log', level=logging.INFO)

app = FastAPI()

class MatrixRequest(BaseModel):
    matrix: List[List[int]]

# Function to find the unique numbers matrix
    
def unique_numbers_in_matrix (matrix: List[List[int]]):
  
    res=[]
    
    for i in matrix:
        for j in i:
            if j not in res:
                res.append(j)
    return (res)
# Function to find the largest_rectangle matrix
def largest_rectangle(matrix: List[List[int]]) -> tuple:

    if not matrix or not matrix[0]:
        return 0
    n = len(matrix[0])
    m= len(matrix)    
    height = [0] * (n + 1)
    
    unique_nums = unique_numbers_in_matrix(matrix)

    ans = 0
    max_number = None
    for nums in unique_nums:
        for j in range(m):
            n=len(matrix[j])
            for i in range(n):
                if matrix[j][i] == nums:
                    height[i] = height[i] + 1
                else:
                    height[i] = 0
            stack = [-1]
                        
            for i in range(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    if h != w:
                        if h*w > ans:
                            ans = h * w
                            max_number=nums
                stack.append(i)

    return (max_number,ans)

@app.get("/")
async def root():
    return {"message": "Welcome to the largest Rectabgle problem!"}

@app.post("/largest_rectangle")
async def get_largest_rectangle(matrix_request: MatrixRequest):
    start_time = datetime.now()
    
    matrix = matrix_request.matrix

    logging.info(f"Request received at {start_time}: {matrix}")

    # Find the largest rectangle
    result = largest_rectangle(matrix)

    end_time = datetime.now()
    logging.info(f"Response sent at {end_time}: {result}, Turnaround time: {end_time - start_time}")

    return result

