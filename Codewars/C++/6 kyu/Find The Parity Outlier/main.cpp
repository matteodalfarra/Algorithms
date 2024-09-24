int FindOutlier(std::vector<int> arr)
{
    int oddCount = 0;
    int evenCount = 0;
    int lastEven = 0;
    int lastOdd = 0;

    for (int i = 0; i < arr.size(); i++){
        if (arr[i] % 2 == 0){
            evenCount++;
            lastEven = arr[i];
        } else {
            oddCount++;
            lastOdd = arr[i];
        }
    }

    if (oddCount > evenCount){
        return lastEven;
    } else {
        return lastOdd;
    }
}