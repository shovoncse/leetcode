class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        vector<int> arr;

        // Count the number of "beams" in each string
        for (int i = 0; i < bank.size(); ++i) {
            int beams = count(bank[i].begin(), bank[i].end(), '1');
            if (beams > 0) {
                arr.push_back(beams);
            }
        }

        // If there are less than 2 "beams," return 0
        if (arr.size() < 2) {
            return 0;
        }

        // Calculate the sum using a loop
        int sum_result = 0;
        for (int i = 0; i < arr.size() - 1; ++i) {
            sum_result += arr[i] * arr[i + 1];
        }

        return sum_result;
    }
};