using System.Collections.Generic;
using System;

public class Kata
{
  public static Dictionary<char, int> Count(string str)
  {
    Dictionary<char, int> letters = new Dictionary<char, int>();
    str = str.ToLower();
    foreach(char s in str)
    {
        if (letters.ContainsKey(s))
        {
            letters[s]++;
        }
        else
        {
            letters.Add(s, 1);
        }
    }
    
    return letters;
  }
}