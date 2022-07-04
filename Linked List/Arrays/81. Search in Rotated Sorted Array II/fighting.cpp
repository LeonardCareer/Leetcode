#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    bool search(vector<int> &nums, int target)
    {
        int start = 0;
        int end = nums.size() - 1;
        while (start <= end)
        {
            int mid = (start + end) / 2;

            if (nums[mid] == target)
            {
                return true;
            }

            if (nums[start] < nums[mid])
            {
                if (nums[start] <= target && nums[mid] > target)
                {
                    end = mid - 1;
                }
                else
                {
                    start = mid + 1;
                }
            }
            else if (nums[start] == nums[mid])
            {
                start++;
            }
            else
            {
                if (nums[mid] < target && target <= nums[end])
                {
                    start = mid + 1;
                }
                else
                {
                    end = mid - 1;
                }
            }
        }
        return false;
    }
};

int main()
{
    vector<int> nums;
    int mynums[] = {2, 5, 6, 0, 0, 1, 2};
    // nums.assign(mynums, mynums + sizeof(mynums) / sizeof(int));
    nums.assign(mynums, mynums + (*(&mynums + 1) - mynums));

    Solution temp;
    int target = 0;
    cout << temp.search(nums, target) << endl;
    // for (int i = 0; i < nums.size(); i++)
    // {
    //     cout << nums[i] << endl;
    // }
}