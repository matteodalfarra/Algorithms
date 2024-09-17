using System;
using System.Numerics;
using System.Security.AccessControl;

public static class Kata 
{
  public static int TrailingZeros(int n)
  {
        int count = 0;
        for (int i = 5; n / i >= 1; i *= 5)
        {
            count += n / i;
        }
        return count;

  }
}