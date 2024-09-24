#include <string>
#include <vector>

std::vector<std::string> towerBuilder(unsigned nFloors) {
    int floor = nFloors * 2 - 1;
    int limit = 0;
    std::vector<std::string> tower;
    
    for (int i = 0; i < nFloors; i++){
        std::string line = "";
        for (int j = 1; j <= floor; j++){
            if (j <= limit || j > floor - limit)
                line += " ";
            else
                line += "*";
        }
        limit++;
        tower.insert(tower.begin(), line);     
    }
  
    return tower;
}