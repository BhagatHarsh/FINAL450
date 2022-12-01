/*
Intuition
If two intervals are overlapping, the new interval will start from the starting time of the first interval and end at the ending time of the maximum end time of the two intervals.

This approach can be generalised for n intervals: If n intervals are overlapping, the resultant interval will start at the starting time of the first interval and end at the ending time of the maximum end time of the n intervals.

Approach
Sort the given 'intervals' array. This will ensure that the interval with the lowest starting time is at the beginning.

Iterate the entire array and initialize a variable 'maxEnd' as the ending value of the ith interval. Also, initialize another variable 'j' with the value after the ith interval.

Now, while j is less than the size of the array and the starting time of j is less than (or equal to) maxEnd, assign maxEnd the maximum value of maxEnd and ending time. Finally, increment j.

Once loop is exited (upon either or both conditions being false), pushback into the solution the starting value of i and maxEnd as the starting and ending times of the new interval respectively.

Since i will eventually get incremented (due to it being in for loop) and j is now pointing to the new interval, re-initialize i as the value prior to j.

Complexity
Time complexity: O(nlogn)
Space complexity: O(n)
*/

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        int n=intervals.size();
        vector<vector<int>> sol;

        sort(intervals.begin(), intervals.end());

        for(int i=0;i<n;i++){
            int maxEnd=intervals[i][1];
            int j=i+1;

            while((j<n)&&(intervals[j][0]<=maxEnd)){
                maxEnd=max(maxEnd, intervals[j][1]);
                j++;
            }
            sol.push_back({intervals[i][0], maxEnd});
            i=j-1;
        }   
        return sol;
    }
};