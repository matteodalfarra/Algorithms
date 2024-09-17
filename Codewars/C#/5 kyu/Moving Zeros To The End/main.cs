using System.Collections.Generic;
using System.Linq;
public class Kata
{
  public static int[] MoveZeroes(int[] arr)
  {
    List<int> result = new List<int>();

    foreach (int i in arr)
    {
        if (i != 0)
        {
            result.Add(i);
        }
    }

    foreach (int i in arr)
    {
        if (i == 0)
            result.Add(i);
    }
    
    return result.ToArray();
  }
}