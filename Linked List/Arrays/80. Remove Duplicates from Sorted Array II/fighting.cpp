#include <vector>
#include <iostream>
using namespace std;

class Solution
{
public:
    int removeDuplicates(vector<int> &nums)
    {
        const int FIXED_NUMBER = 2;
        if (nums.size() < FIXED_NUMBER)
        {
            return nums.size();
        }

        int place = FIXED_NUMBER;
        for (int i = FIXED_NUMBER; i < nums.size(); i++)
        {
            if (nums[i] != nums[place - FIXED_NUMBER])
            {
                nums[place] = nums[i];
                place++;
            }
        }
        return place;
    }
};

int main()
{
    vector<int> nums;
    nums.push_back(1);
    nums.push_back(1);
    nums.push_back(1);
    nums.push_back(2);
    nums.push_back(2);
    nums.push_back(2);
    nums.push_back(3);
    nums.push_back(4);

    Solution temp;
    int x = temp.removeDuplicates(nums);
    cout << x;
    cout << "\n";
    for (int i = 0; i < nums.size(); i++)
    {
        cout << nums[i];
        cout << " ";
    };
}
