#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int first = -1;
        int last = -1;

        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] == target) {
                if(first == -1) first = i;
                last = i;
            }
        }

        return {first, last};
    }
};

// Sample main function to test the solution
int main() {
    Solution obj;
    vector<int> nums = {5, 7, 7, 8, 8, 10};
    int target = 8;

    vector<int> result = obj.searchRange(nums, target);
    cout << "[" << result[0] << ", " << result[1] << "]" << endl;

    return 0;
}
