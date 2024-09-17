using System;
using System.ComponentModel.Design;
using System.Collections.Generic;

public class Persist 
{
	public static int Persistence(long n) 
	{
		int result = 0;
    List<int> ints = new List<int>();
    while (n >= 10)
    {
        ints.Clear();
        for (int i = 0; i < n.ToString().Length; i++)
        {
            ints.Add(int.Parse(n.ToString().Substring(i, 1)));
        }

        n = 1;
        foreach (int i in ints)
        {
            n *= i; 
        }
        result++;
    }
    
    return result;
	}
}