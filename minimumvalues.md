Interview Question /Hackerrank

Find the minimum possible value of k for each element in the array. If an element cannot be expressed as required, return -1 for that element.

Example
Consider n=5, arr= [5,1,4,6,10]

- 5 can be expressed as the sum of 1 + 4 = 5, so k = 2.

  - All values are greater than 0.
  - k - 1 = 1 value is an even power of 2, ie 2^2 = 4
  - One value is less than 4.

- 1 can be expressed as 1, so k = 1.

  - All values are greater than 0.
  - k - 1 = 0 values are an even power of 2
  - One value is less than 4

- 4 cannot be expressed in a format that satisfies the conditions. The answer for this element is -1.

  - If k = 1 for example, 4 = 4. Here 4 is an even power of 2 but exactly k - 1 = 0 are allowed. There is no value less than 4.
  - If k = 2 for example, 2 + 2 = 4. There is not k - 1 = 1 interger that is an even power of 2. More than one integer is less than 4.
  - If k = 3, the only numbers that satisfy are 2 + 1 + 1 = 4. Here k - 1 = 2 of the values are even powers of 2, but all of the integers are less than 4.

- 2 + 4 = 6, so k =2
- 2 + 4 + 4 = 10, so k = 3

The answer is the array [2,1,-1,2,3].
