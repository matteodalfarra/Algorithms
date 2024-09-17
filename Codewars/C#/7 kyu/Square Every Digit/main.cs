using System;

public class Kata
{
  public static int SquareDigits(int n)
  {
    string result = string.Empty;
    for (int i = 0; i < n.ToString().Length; i++)
    {
        int number = int.Parse(n.ToString().Substring(i, 1));
        result += ((int)(Math.Pow(number, 2))).ToString();
    }

    return int.Parse(result);
  }
}