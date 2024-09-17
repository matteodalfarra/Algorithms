using System.Numerics;

public class Kata
{
  public static BigInteger[] PowersOfTwo(int n)
  {
    BigInteger[] results = new BigInteger[n+1];
    
    for (int i = 0; i <= n; i++)
    {
      if (i == 0){
        results[i] = 1;
      }else{
        BigInteger power = 1;
        for (int j = 1; j <= i; j++){
          power *= 2;
        }
        results[i] = power;
      }
    }
    return results;
  }
}