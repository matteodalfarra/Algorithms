#include <vector>

std::vector<unsigned int> removeSmallest(const std::vector<unsigned int>& numbers) {
  int min = numbers[0];
  int index = 0;
  for (int i = 0; i < numbers.size(); i++){
      if ((numbers[i] < min) || (numbers[i] == min && i < index)){
          min = numbers[i];
          index = i;
      }
  }

  std::vector<unsigned int> n;

  for (int i = 0; i < numbers.size(); i++){
      if (i != index){
          n.push_back(numbers[i]);
      }
  }
  return n;
}