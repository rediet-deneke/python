def is_palindrome(s):

  start = 0
  end = len(s) - 1
  for i in range(0, len(s)//2):
    if s[start] != s[end]:
      return False
    start += 1
    end -= 1
    
  
  # Replace this placeholder return statement with your code
  return True