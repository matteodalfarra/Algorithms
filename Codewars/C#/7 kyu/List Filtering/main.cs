using System.Collections;
using System.Collections.Generic;

public class ListFilterer
{
   public static IEnumerable<int> GetIntegersFromList(List<object> listOfItems)
   {
      var list2 = new List<int>();

      foreach (var item in listOfItems)
      {
          if (item is int)
          {
              list2.Add((int)item);
          }
      }
     
     return list2;
   }
}