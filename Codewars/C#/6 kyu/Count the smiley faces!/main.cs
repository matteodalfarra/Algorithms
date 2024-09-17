using System.Collections.Generic;

public static class Kata
{
  public static int CountSmileys(string[] smileys) 
  {
    int result = 0;
    foreach (string smiley in smileys)
    {
        if (smiley.Substring(0, 1) == ";" || smiley.Substring(0, 1) == ":")
            if (smiley.EndsWith("D") || smiley.EndsWith(")"))
                if (smiley.Length == 3)
                {
                    if (smiley.Substring(1, 1) == "-" || smiley.Substring(1, 1) == "~")
                        result++;
                }  
                else
                    result++;
    }
    
    return result;
  }
}