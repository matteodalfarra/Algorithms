public class TwoToOne 
{
  
	public static string Longest (string s1, string s2) 
  {
    string alp = "abcdefghijklmnopqrstuvwxyz";
    string s3 = s1+s2;
    string result = string.Empty;
    foreach (char c in alp)
    {
        if (s3.Contains(c) && !result.Contains(c))
        {
            result += c;
        }
    }
    return result;
  }
}