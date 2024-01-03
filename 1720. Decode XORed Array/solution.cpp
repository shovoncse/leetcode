class Solution {
public:
    vector<int> decode(vector<int>& encoded, int first) {
        vector<int>ans;
        ans.push_back(first);
        for(auto i: encoded){
          ans.push_back(ans.back()^i);
        }

        return ans;
    }
};