'''2525. Categorize Box According to Criteria
Given four integers length, width, height, and mass, representing the dimensions and mass of a box, respectively, return a string representing the category of the box.

The box is "Bulky" if:
Any of the dimensions of the box is greater or equal to 104.
Or, the volume of the box is greater or equal to 109.
If the mass of the box is greater or equal to 100, it is "Heavy".
If the box is both "Bulky" and "Heavy", then its category is "Both".
If the box is neither "Bulky" nor "Heavy", then its category is "Neither".
If the box is "Bulky" but not "Heavy", then its category is "Bulky".
If the box is "Heavy" but not "Bulky", then its category is "Heavy".
Note that the volume of the box is the product of its length, width and height.

 

Example 1:

Input: length = 1000, width = 35, height = 700, mass = 300
Output: "Heavy"
Explanation: 
None of the dimensions of the box is greater or equal to 104. 
Its volume = 24500000 <= 109. So it cannot be categorized as "Bulky".
However mass >= 100, so the box is "Heavy".
Since the box is not "Bulky" but "Heavy", we return "Heavy".'''

class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        res = ""
        if length >= 10 ** 4 or width >= 10 ** 4 or height >= 10 ** 4 or length * width * height >= 10 ** 9:
            res = "Bulky"
        if mass >= 100 :
            res += "Heavy"
        if res == "BulkyHeavy":
            return "Both"
        if not res:
            return "Neither"
        if res == "Bulky":
            return res
        if res == "Heavy":
            return res            
            
