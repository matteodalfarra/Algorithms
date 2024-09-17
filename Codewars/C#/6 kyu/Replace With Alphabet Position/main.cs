using System;
using System.Collections.Generic;

public static class Kata
{
  public static string AlphabetPosition(string text)
  {
    Dictionary<string, int> letters = new Dictionary<string, int>()
    {
        {"A", 1},
        {"B", 2},
        {"C", 3 },
        {"D", 4 },
        {"E", 5 },
        {"F", 6 },
        {"G", 7 },
        {"H", 8 },
        {"I", 9 },
        {"J", 10 },
        {"K", 11 },
        {"L", 12 },
        {"M", 13 },
        {"N", 14 },
        {"O", 15 },
        {"P", 16 },
        {"Q", 17},
        {"R", 18 },
        {"S", 19 },
        {"T", 20 },
        {"U", 21},
        {"V", 22 },
        {"W", 23 },
        {"X", 24 },
        {"Y", 25 },
        {"Z", 26 },
    };

    text = text.ToUpper();
    string result = string.Empty;
    for  (int i = 0; i < text.Length; i++)
    {
        if (letters.ContainsKey(text.Substring(i, 1)))
        {
            if (result.Length != 0)
                result  += " " + letters[text.Substring(i, 1)];
            else
                result += letters[text.Substring(i, 1)];
        }
    }
    
    return result;
  }
}