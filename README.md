# Algorithm Practice

## Goals

- Practice at least 1 algorithm per day for 100 (business) days
- Share insights around logic and across languages

## Resources

- [Udemy course: 100 Algorithm Challenge](https://www.udemy.com/course/100-algorithms-challenge/learn/lecture/10510502?start=0#overview)
- [whiteboarding-meetup repo](https://git.generalassemb.ly/eloisebarrow/whiteboarding-meetup/blob/master/algorithms.md)
- [javascript-algorithms repo](https://github.com/trekhleb/javascript-algorithms#data-structures)
- [codewars.com](https://www.codewars.com/)
- [hackerrank.com](https://www.hackerrank.com/)

### Problem 1

```
Given a two-digit integer, return the sum of its digits.

Input: 29
Output: 11

Input: 30
Output: 3
```

### Problem 2

```
Write a function called oddsEvens that given a string, prints its even-indexed and odd-indexed characters as space-separated strings on a single line.

Input: Hacker
Output: Hce akr

```

### Problem 3

```
Write a function called isAnagram that, given 2 strings, returns true if the strings are anagrams
isAnagram("cinema", "iceman") == True
isAnagram("randum" "werdz") == False
```

### Problem 4

```
Given an array of strings, return another array containing all of its longest strings.

Input: ["aba", "aa", "ad", "vcd", "aba"]
Output: ["aba", "vcd", "aba"]
```

### Problem 5

```
Write a function called largestNumber that will return the largest value from an array.

Input: [1,2,5,10]
Output: 10
```

### Problem 6

```
Write a function called printArr that will print the items of an array.

Input: ['sally','monique','caleb']
Output: 

sally
monique
caleb

```

### Problem 7

```
Write a function called isPalindrome that, given a string, returns true
if the string is a palindrome, and false if not

Input: isPalindrome("tacocat")
Output: True

Input: isPalindrome("nottacocat")
Output: False

Additional levels of difficulty:
Input: isPalindrome("Race car")
Output: True

Input: isPalindrome("a man, a plan, a canal - panama")
Output: True
```

### Problem 8

```
Write a function called likes which takes in an array, containing the names of people who like an item. It must return the display text as shown in the examples and is dependent on the number of elements in the array.

Input: likes([])
Output: "no one likes this"

Input: likes(["Peter"])
Output: "Peter likes this"

Input: likes(["Jacob", "Alex"])
Output: "Jacob and Alex like this"

Input: likes(["Max", "John", "Mark"])
Output: "Max, John and Mark like this"

Input: likes(["Alex", "Jacob", "Mark", "Max"])
Output: "Alex, Jacob and 2 others like this"
```

### Problem 9

```
Create a function called findMissingNums that takes in two arrays. Iterate over the first array and the number you are iteratring over is NOT present in the second array, push the number into it. Once the loop is complete return the second array.

Input: [0,1,2,3,4,5,6,7,8,9], [2,3,7,9]
Output: [ 2, 3, 7, 9, 0, 1, 4, 5, 6, 8 ]
```

### Problem 10

```
Write a function called phoneBook that given two parameters, the first being an array of hashes containing n number of names and phone numbers and the second being an array of friends names will then will assemble a phone book that maps the 'friends' array of names to their respective phone numbers if they are found in the first array. Each found entry will print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry is not found, print Not found instead.

Input 1: [{sam:99912222},{tom:11122222},{harry:12299933}]
Input 2: ['sam','ed','harry']

Output:
sam=99912222
NOT FOUND
harry:12299933
```

### Problem 11

```
Write a function called twoSum that given an array of integers and a target number, returns two array integers that add up to the target.

Input: [3, 2, 5, 7, 11, 15], 9
Output: Return [2, 7]
```