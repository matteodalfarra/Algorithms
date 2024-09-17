public static class Kata
{
  // return masked string
  public static string Maskify(string cc)
  {
    if (cc.Length > 4)
    {
      int l = cc.Length - 4;
      cc = cc.Substring(l);

      for (int i = 0; i < l; i++)
      {
          cc = "#" + cc;
      }
      return cc;
    }
    else
      return cc;
  }
}