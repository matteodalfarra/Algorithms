# include <string>

std::string disemvowel(const std::string& str) {
    std::string vowel = "aeiouyAEIOUY";
    std::string newStr = "";

    for (int i = 0; i < str.size(); i++){ 
        if (vowel.find(str[i]) == std::string::npos){
            newStr += str[i];
        }
    }
  
    return newStr;
}