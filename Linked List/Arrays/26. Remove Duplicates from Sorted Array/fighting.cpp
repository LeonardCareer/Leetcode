#include <vector>
#include <iostream>
using namespace std;

int removeDuplicates(vector<int> &nums)
{
    if(nums.empty()){
        return 0;
    }

    int place = 1;
    for (int i = 1; i < nums.size(); i++)
    {
        if (nums[i] != nums[place - 1])
        {
            nums[place] = nums[i];
            place++;
        }
    }
    return place;
}

int main()
{
    vector<int> nums;
    nums.push_back(1);
    nums.push_back(1);
    nums.push_back(2);
    int x = removeDuplicates(nums);
    cout << x;
    cout << "\n";
    for (int i = 0; i < nums.size(); i++)
    {
        cout << nums[i];
        cout << " ";
    };
}
