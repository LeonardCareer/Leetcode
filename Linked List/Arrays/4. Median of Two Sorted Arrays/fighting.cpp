#include <vector>
#include <iostream>
using namespace std;

class Solution
{
public:
    double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2)
    {
        int total = nums1.size() + nums2.size();
        if (total % 2 == 1)
        {
            return findKstNumber(nums1, nums2, total / 2 + 1);
        }
        else
        {
            return (findKstNumber(nums1, nums2, total / 2) + findKstNumber(nums1, nums2, total / 2 + 1)) / 2.0;
        }
    }

    double findKstNumber(vector<int> &nums1, vector<int> &nums2, int k)
    {
        if (nums1.size() > nums2.size())
        {
            return findKstNumber(nums2, nums1, k);
        }

        if (nums1.size() == 0)
        {
            return nums2[k - 1];
        }

        if (k == 1)
        {
            return min(nums1[0], nums2[0]);
        }

        int mid1 = min(int(k / 2), int(nums1.size()));
        int mid2 = k - mid1;

        if (nums1[mid1 - 1] > nums2[mid2 - 1])
        {
            vector<int> newNums2 = vector<int>(nums2.begin() + mid2, nums2.end());
            return findKstNumber(nums1, newNums2, k - mid2);
        }
        else if (nums1[mid1 - 1] < nums2[mid2 - 1])
        {
            vector<int> newNums1 = vector<int>(nums1.begin() + mid1, nums1.end());
            return findKstNumber(newNums1, nums2, k - mid1);
        }
        else
        {
            return nums1[mid1 - 1];
        }
    }
};

int main()
{

    int x[] = {1, 2, 3, 4, 5, 6, 7, 8};
    int y[] = {1, 2, 3, 4, 5};
    vector<int> a;
    vector<int> b;
    a.assign(x, x + sizeof(x) / sizeof(int));
    b.assign(y, y + sizeof(y) / sizeof(int));
    Solution temp;
    cout << temp.findMedianSortedArrays(a, b) << endl;
}